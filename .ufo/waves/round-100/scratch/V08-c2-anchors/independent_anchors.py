from pathlib import Path
from dataclasses import dataclass, replace
import hashlib
import json
import re
import subprocess

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
BASELINE = 'fe1ce46'
OLD = ROOT / 'corpus/fixtures/r99-window-lapse'
NEW = ROOT / 'corpus/fixtures/r100-docket-review'


@dataclass(frozen=True)
class Row:
    id: str
    cells: tuple
    path: str
    first: int
    last: int
    anchor: str


def code_cell(cell):
    m = re.fullmatch(r'`([^`]+)`', cell)
    assert m, f'Not a single code cell: {cell!r}'
    return m.group(1)


def parse_rows(text):
    rows = []
    for line in text.splitlines():
        if not re.match(r'^\|\s*[JS]\d+\s*\|', line):
            continue
        cells = tuple(c.strip() for c in line.strip().strip('|').split('|'))
        is_json = cells[0].startswith('J')
        assert len(cells) == (8 if is_json else 7), cells
        path_i, span_i, anchor_i = (4, 5, 7) if is_json else (3, 4, 6)
        m = re.fullmatch(r'(\d+)(?:-(\d+))?', cells[span_i])
        assert m, f'Invalid span: {cells[span_i]!r}'
        first, last = int(m.group(1)), int(m.group(2) or m.group(1))
        rows.append(Row(cells[0], cells, code_cell(cells[path_i]), first, last, code_cell(cells[anchor_i])))
    return rows


def locations(row, excerpt):
    return [n for n, line in enumerate(excerpt, 1) if row.anchor in line]


def anchor_errors(row, excerpt):
    errors = []
    if not 1 <= row.first <= row.last <= len(excerpt):
        errors.append('invalid-range')
    hits = locations(row, excerpt)
    if not hits:
        errors.append('anchor-absent')
    if any(n < row.first or n > row.last for n in hits):
        errors.append('out-of-span')
    return errors


def frozen_bytes(name):
    rel = (OLD / name).relative_to(ROOT).as_posix()
    p = subprocess.run(['git', 'show', f'{BASELINE}:{rel}'], cwd=ROOT, capture_output=True, check=True)
    current = (OLD / name).read_bytes()
    assert p.stdout == current, f'r99 changed from baseline: {rel}'
    return p.stdout


assert Path.cwd().resolve() == ROOT.resolve()
reports = sorted(p for p in (ROOT / '.ufo/waves/round-100/seats').glob('T3*') if p.is_file())
assert reports, 'T3 producer report is absent; never verify a plan'
for name in ('README.md', 'claim-excerpt-map.md', 'fictional-excerpts.md', 'source-excerpt.md'):
    assert (NEW / name).is_file(), f'Missing delivered artifact: {name}'
print('PRODUCER-REPORTS', ', '.join(str(p.relative_to(ROOT)) for p in reports))

old_map = frozen_bytes('claim-excerpt-map.md').decode('utf-8')
old_excerpts = frozen_bytes('fictional-excerpts.md')
old_external = frozen_bytes('source-excerpt.md')
new_map = (NEW / 'claim-excerpt-map.md').read_text()
new_excerpts = (NEW / 'fictional-excerpts.md').read_bytes()
new_external = (NEW / 'source-excerpt.md').read_bytes()
old_rows = parse_rows(old_map)
new_rows = parse_rows(new_map)
old_json = [r for r in old_rows if r.id.startswith('J')]
new_json = [r for r in new_rows if r.id.startswith('J')]
new_editorial = [r for r in new_rows if r.id.startswith('S')]
assert [r.id for r in old_json] == [f'J{n:02d}' for n in range(1, 22)]
assert [r.id for r in new_json] == [f'J{n:02d}' for n in range(1, 23)]
assert [r.id for r in new_editorial] == ['S01', 'S02']
print('ROW-INVENTORY JSON=22 EDITORIAL=2 TOTAL=24')

excerpts = {}
for row in new_rows:
    path = (NEW / row.path).resolve()
    assert path.is_relative_to(NEW.resolve()), row.path
    excerpts[row.path] = path.read_text().splitlines()
    errors = anchor_errors(row, excerpts[row.path])
    assert not errors, f'{row.id}: {errors}'
    print(f'ANCHOR {row.id} {row.path}:{row.first}-{row.last} hits={locations(row, excerpts[row.path])} IN-SPAN')
print('ANCHORS JSON=22/22 EDITORIAL=2/2 ALL=24/24')
print('DISTINCT-ANCHOR-PAIRS', len({(r.path, r.anchor) for r in new_rows}))

assert new_excerpts.startswith(old_excerpts), 'Inherited excerpt bytes are not an exact prefix'
assert new_external == old_external, 'External source excerpt changed'
old_lines = old_excerpts.decode('utf-8').splitlines()
assert new_excerpts.decode('utf-8').splitlines()[:len(old_lines)] == old_lines
for before, after in zip(old_json, new_json):
    assert before.cells[:3] + before.cells[4:] == after.cells[:3] + after.cells[4:], f'Inherited row fields changed: {before.id}'
    expected_namespace = before.cells[3].replace('r99-window-lapse:', 'r100-docket-review:')
    assert after.cells[3] == expected_namespace, f'Namespace not path qualification only: {before.id}'
assert [r.cells for r in old_rows if r.id.startswith('S')] == [r.cells for r in new_editorial], 'Editorial row drift'
print(f'PRESERVATION r99={BASELINE}; excerpt-prefix-lines=1-{len(old_lines)} byte-identical; J01-J21 fields/spans/anchors identical except namespace; S01-S02 identical')

fiction = excerpts['fictional-excerpts.md']
headings = [n for n, line in enumerate(fiction, 1) if re.match(r'^## Round 100\b', line) and 'review' in line.lower()]
assert len(headings) == 1, f'Expected exactly one Round 100 review heading: {headings}'
review_first = headings[0]
review_last = next((n-1 for n in range(review_first+1, len(fiction)+1) if fiction[n-1].startswith('## ')), len(fiction))
assert review_first > len(old_lines)
added = new_json[-1]
assert added.id == 'J22'
assert re.match(r'^`timeline\.json#/8`(?:\s|$)', added.cells[1])
assert code_cell(added.cells[2]) == 'clerk-review-note'
assert code_cell(added.cells[3]) == 'r100-docket-review:clerk-review-note'
assert added.path == 'fictional-excerpts.md'
assert review_first <= added.first <= added.last <= review_last, 'New row span crosses review-section bounds'
assert all(review_first <= n <= review_last for n in locations(added, fiction))
assert not locations(added, old_lines), 'New anchor occurs in inherited prose'
print(f'NEW-ANCHOR J22 pointer=timeline.json#/8 source=clerk-review-note span={added.first}-{added.last} review-section={review_first}-{review_last} hits={locations(added, fiction)} inherited-hits=0')

assert 'out-of-span' in anchor_errors(replace(added, first=1, last=1), fiction)
print('CONTROL PASS new anchor with span 1-1 rejected as out-of-span')
assert 'anchor-absent' in anchor_errors(replace(added, anchor='V08_ABSENT_ANCHOR_CONTROL'), fiction)
print('CONTROL PASS missing anchor rejected as anchor-absent')
assert 'out-of-span' in anchor_errors(added, fiction + [added.anchor])
print('CONTROL PASS duplicated new anchor after EOF rejected as out-of-span')
assert not ('V08 shifted-prefix control\n' + new_excerpts.decode('utf-8')).encode('utf-8').startswith(old_excerpts)
print('CONTROL PASS prepended line rejected by inherited-byte-prefix predicate')

for name in ('README.md', 'claim-excerpt-map.md', 'fictional-excerpts.md', 'source-excerpt.md'):
    print('DELIVERED-SHA256', name, hashlib.sha256((NEW/name).read_bytes()).hexdigest())
print('RESULT PASS: 22/22 JSON anchors in span, inherited line numbers stable, only J22 new and wholly in review section')
