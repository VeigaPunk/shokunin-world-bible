# T3 — fixture documentation (2026-10-17)

Scope: C2 component 1 documentation only. Axes: depth (complete canonical coverage of the review), calibration (exact anchors and explicit non-establishment bounds), operability (replayable checks), with inherited provenance preserved. This is a producer receipt, not a round-wide admission verdict.

## Delivered files

Only these fixture files were edited by T3, both with exact `Edit` replacements after reading T2's copies:

- `/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r100-docket-review/README.md`: identifies the continuation, 6/1/8 → 6/1/9 and 8 → 9 sources, 22 obligations, the review-only/open-entry/no-resolution bound, editorial tick/ID encoding, external-source limits, and three lane-root replay commands. Relevant final lines: 3, 7–15, 19–28.
- `/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r100-docket-review/claim-excerpt-map.md`: declares 22 JSON facts + 2 editorial rows = 24 rows, 20 distinct anchors; retains J01–J21 at map lines 22–42 and appends J22 at line 43, `timeline.json#/8`, source `clerk-review-note`, span 78–88, exact anchor at excerpt line 82. The J22 scope explanation is at map line 72.

This report is the only other T3-created file. No scratch was created. No edits to JSON, excerpts, tools, contracts, another report, or any other fixture; no nested agents, commits, pushes, or network calls.

Inheritance qualification: all 21 inherited pointer/field, raw-source-ID, excerpt-path, span, mode, and anchor cells are unchanged, as are their map-row positions and actual excerpt hit lines. Their path-qualified namespace column changes from `r99-window-lapse:…` to `r100-docket-review:…`, following the fixture's existing continuation convention. Raw map-row bytes are therefore not claimed identical across namespaces. Both documents explicitly state this qualification.

## Producer wait

T2 artifacts **and** T2's producer report were required before editing or validating the delivered fixture. Exact lane-root command, using the required 20-second cadence and 40-try maximum:

```sh
python3 -u - <<'PY'
from pathlib import Path
import time
root = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
fixture = root / 'corpus/fixtures/r100-docket-review'
seats = root / '.ufo/waves/round-100/seats'
required = ('entities.json', 'relations.json', 'timeline.json', 'sources.json', 'contradictions.json', 'fictional-excerpts.md', 'inspiration-note.md', 'source-excerpt.md')
for attempt in range(1, 41):
    missing = [name for name in required if not (fixture / name).is_file()]
    reports = sorted(path for path in seats.glob('T2*.md') if path.is_file())
    print(f'POLL {attempt}/40 missing={missing} T2_reports={[str(path.relative_to(root)) for path in reports]}', flush=True)
    if not missing and reports:
        print('READY: T2 artifacts and producer report exist', flush=True)
        break
    if attempt < 40:
        time.sleep(20)
else:
    print('ABSENT: T2 artifacts or producer report not delivered after 40 polls', flush=True)
    raise SystemExit(3)
PY
```

Observed stdout, exit 0 after approximately 80 seconds:

```text
POLL 1/40 missing=[] T2_reports=[]
POLL 2/40 missing=[] T2_reports=[]
POLL 3/40 missing=[] T2_reports=[]
POLL 4/40 missing=[] T2_reports=[]
POLL 5/40 missing=[] T2_reports=['.ufo/waves/round-100/seats/T2-fixture-author.md']
READY: T2 artifacts and producer report exist
```

Then read the actual T2 report, all three modified payload files, and both copied documentation files. No plan was accepted as delivered evidence. No all-reports poll or stall escape was needed.

## Delivered-revision gate receipts

All commands below ran from `/home/vgpnk/Projects/shokunin/lore-shokunin`, using `python3`, after both documentation edits. They were issued concurrently and all exited 0.

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r100-docket-review
```

Observed complete stdout:

```text
CLEAN: schema, citations, relations, timeline; 0 violations
```

```sh
python3 corpus/tools/map_obligations.py corpus/fixtures/r100-docket-review
```

Observed complete stdout:

```text
OBLIGATIONS raw=22 mapped=22
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24
RESULT PASS
```

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r100-docket-review
```

Observed complete stdout (the delivered tool actually invokes `grep -nF --` for every anchor):

```text
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24; DISTINCT-ANCHORS 20/20
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS J01: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J02: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J03: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J04: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J05: source-support; mode=verbatim; anchor=found; 17:> The Chalk Stair is the named rain-dark crossing between Quiet Rise and Salt Court.
PASS J06: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J07: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J08: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J09: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J10: source-support; mode=verbatim; anchor=found; 18:> After both Tick 9 entries above, Aru and Evin met at the Chalk Stair at tick 10.
PASS J11: source-support; mode=verbatim; anchor=found; 19:> There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.
PASS J12: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J13: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J14: source-support; mode=verbatim; anchor=found; 20:> Their tick-10 decision depends on both ninth-bell entries: Aru's north-lantern entry at Quiet Rise and Evin's south-bell entry at Salt Court. After agreeing to share stewardship for this crossing only, they chalked one temporary route mark together at the midpoint.
PASS J15: source-support; mode=verbatim; anchor=found; 26:> Tick 11: I waited at the Chalk Stair through the agreed bell.
PASS J16: source-support; mode=verbatim; anchor=found; 37:> Tick 12: I was at Salt Court through the same agreed bell.
PASS J17: source-support; mode=verbatim; anchor=found; 48:> Tick 13: I received Evin's response at the Chalk Stair.
PASS J18: source-support; mode=verbatim; anchor=found; 60:> I am Maren, clerk of the Chalk Stair registry, and I record the matter OPEN.
PASS J19: source-support; mode=verbatim; anchor=found; 59:> Tick 14: I filed both pending accounts at the Chalk Stair registry.
PASS J20: source-support; mode=verbatim; anchor=found; 59:> Tick 14: I filed both pending accounts at the Chalk Stair registry.
PASS J21: source-support; mode=verbatim; anchor=found; 70:> Tick 15: The crossing-window named in the original minute has closed.
PASS J22: source-support; mode=verbatim; anchor=found; 82:> Tick 16: After my lapse record, I made the first-passage docket review at the Chalk Stair.
PASS S01: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
PASS S02: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
RECEIPT JSON-FACTS 22; EDITORIAL-ROWS 2; TOTAL-ROWS 24
SOURCE-SUPPORT 22/22; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 24/24; VALIDATED-ROWS 24/24
RESULT PASS
```

These receipts are bounded: structural validity, one-to-one obligation inventory, and lexical anchor/mode/span validation. They do not establish whole-claim entailment, testimony truth, source authentication, chronology authentication, rights, permission, dependency semantics, or canon.

## Independent inheritance, fixed-string, and inventory replay

Exact lane-root command. `-B` prevents this import-based check from creating any bytecode files. It uses the delivered `support_check.grep_anchor` helper, which executes real `grep -nF --` calls without a shell, and compares complete outputs against the unchanged r99 excerpt, itself checked against baseline `fe1ce46`.

```sh
python3 -B - <<'PY'
import hashlib
import importlib.util
import json
import subprocess
from pathlib import Path
root = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
assert Path.cwd().resolve() == root.resolve()
old = root / 'corpus/fixtures/r99-window-lapse'
new = root / 'corpus/fixtures/r100-docket-review'
assert new.resolve() == root / 'corpus/fixtures/r100-docket-review'
def baseline(name):
    return subprocess.check_output(['git', 'show', f'fe1ce46:corpus/fixtures/r99-window-lapse/{name}'], cwd=root)
assert (old / 'claim-excerpt-map.md').read_bytes() == baseline('claim-excerpt-map.md')
assert (old / 'fictional-excerpts.md').read_bytes() == baseline('fictional-excerpts.md')
old_rows = [(number, text) for number, text in enumerate(baseline('claim-excerpt-map.md').decode().splitlines(), 1) if text.startswith('| J')]
new_rows = [(number, text) for number, text in enumerate((new / 'claim-excerpt-map.md').read_text().splitlines(), 1) if text.startswith('| J')]
assert (len(old_rows), len(new_rows)) == (21, 22)
for (old_number, old_text), (new_number, new_text) in zip(old_rows, new_rows):
    assert old_number == new_number
    assert new_text.replace('r100-docket-review:', 'r99-window-lapse:') == old_text
print('INHERITED MAP ROWS 21/21 same map lines 22-42; qualification-only change r99-window-lapse -> r100-docket-review')
spec = importlib.util.spec_from_file_location('support_check', root / 'corpus/tools/support_check.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
old_facts, _, old_inventory = module.parse_map(old / 'claim-excerpt-map.md')
new_facts, _, new_inventory = module.parse_map(new / 'claim-excerpt-map.md')
old_json = [row for row in old_facts if row['kind'] == 'json']
new_json = [row for row in new_facts if row['kind'] == 'json']
assert new_json[:-1] == old_json
assert [row for row in new_facts if row['kind'] == 'editorial'] == [row for row in old_facts if row['kind'] == 'editorial']
assert new_inventory == (22, 2, 24, 20)
for old_row, new_row in zip(old_json, new_json):
    old_hits, old_error = module.grep_anchor(old_row['anchor'], module.resolve_excerpt(old, old_row['path']))
    new_hits, new_error = module.grep_anchor(new_row['anchor'], module.resolve_excerpt(new, new_row['path']))
    assert not old_error and not new_error
    assert old_hits and old_hits == new_hits
    print(f"GREP-NF {new_row['id']} unchanged span={new_row['span']} hits={[number for number, _ in new_hits]}")
print('INHERITED JSON ANCHORS 21/21 identical grep -nF output and excerpt line numbers')
review = new_json[-1]
assert review['id'] == 'J22' and review['span'] == '78-88' and review['mode'] == 'verbatim'
review_cells = module.cells(new_rows[-1][1])
assert review_cells[1].split('`')[1] == 'timeline.json#/8'
assert review_cells[2] == '`clerk-review-note`'
hits, error = module.grep_anchor(review['anchor'], module.resolve_excerpt(new, review['path']))
old_hits, old_error = module.grep_anchor(review['anchor'], old / review['path'])
assert not error and not old_error and not old_hits and [number for number, _ in hits] == [82]
print(f"REVIEW J22 pointer=timeline.json#/8 source=clerk-review-note span=78-88 new_hits={[number for number, _ in hits]} inherited_hits={old_hits}")
print(hits[0][1])
assert (new / 'fictional-excerpts.md').read_bytes().startswith(baseline('fictional-excerpts.md'))
print(f"EXCERPT BYTE-PREFIX {len(baseline('fictional-excerpts.md'))}/{len(baseline('fictional-excerpts.md'))} preserved")
tables = {name: json.loads((new / f'{name}.json').read_bytes()) for name in ('entities', 'relations', 'timeline', 'sources', 'contradictions')}
for name in ('entities', 'relations', 'contradictions'):
    assert tables[name] == json.loads(baseline(f'{name}.json'))
for name in ('timeline', 'sources'):
    assert tables[name][:-1] == json.loads(baseline(f'{name}.json'))
counts = tuple(len(tables[name]) for name in ('entities', 'relations', 'timeline', 'sources', 'contradictions'))
assert counts == (6, 1, 9, 9, 0)
event = tables['timeline'][-1]
assert (event['id'], event['tick'], event['entity_id'], event['place_id'], event['depends_on'], event['source_id']) == ('clerk-review-first-passage', 16, 'clerk-maren', 'chalk-stair', ['clerk-lapse-recorded'], 'clerk-review-note')
print('INVENTORY entities=6 relations=1 events=9 sources=9 contradictions=0')
print('NEW EVENT clerk-review-first-passage tick=16 actor=clerk-maren place=chalk-stair depends_on=[clerk-lapse-recorded]')
excerpt_lines = (new / 'fictional-excerpts.md').read_text().splitlines()
for number in range(82, 87):
    print(f'REVIEW QUOTE {number}:{excerpt_lines[number-1]}')
for name in ('README.md', 'claim-excerpt-map.md'):
    text = (new / name).read_text()
    assert not any(line.rstrip() != line for line in text.splitlines()), name
    assert text.endswith('\n'), name
    print(f'DELIVERED {name} sha256={hashlib.sha256((new / name).read_bytes()).hexdigest()}')
print('RESULT PASS: inheritance, anchors, review isolation, counts, and documentation whitespace')
PY
```

Observed complete stdout, exit 0:

```text
INHERITED MAP ROWS 21/21 same map lines 22-42; qualification-only change r99-window-lapse -> r100-docket-review
GREP-NF J01 unchanged span=12 hits=[12]
GREP-NF J02 unchanged span=13 hits=[13]
GREP-NF J03 unchanged span=12 hits=[12]
GREP-NF J04 unchanged span=13 hits=[13]
GREP-NF J05 unchanged span=17 hits=[17]
GREP-NF J06 unchanged span=12 hits=[12]
GREP-NF J07 unchanged span=13 hits=[13]
GREP-NF J08 unchanged span=12 hits=[12]
GREP-NF J09 unchanged span=13 hits=[13]
GREP-NF J10 unchanged span=18 hits=[18]
GREP-NF J11 unchanged span=19 hits=[19]
GREP-NF J12 unchanged span=12 hits=[12]
GREP-NF J13 unchanged span=13 hits=[13]
GREP-NF J14 unchanged span=18-20 hits=[20]
GREP-NF J15 unchanged span=22-31 hits=[26]
GREP-NF J16 unchanged span=33-42 hits=[37]
GREP-NF J17 unchanged span=44-53 hits=[48]
GREP-NF J18 unchanged span=60 hits=[60]
GREP-NF J19 unchanged span=59-60 hits=[59]
GREP-NF J20 unchanged span=55-64 hits=[59]
GREP-NF J21 unchanged span=66-76 hits=[70]
INHERITED JSON ANCHORS 21/21 identical grep -nF output and excerpt line numbers
REVIEW J22 pointer=timeline.json#/8 source=clerk-review-note span=78-88 new_hits=[82] inherited_hits=[]
82:> Tick 16: After my lapse record, I made the first-passage docket review at the Chalk Stair.
EXCERPT BYTE-PREFIX 5114/5114 preserved
INVENTORY entities=6 relations=1 events=9 sources=9 contradictions=0
NEW EVENT clerk-review-first-passage tick=16 actor=clerk-maren place=chalk-stair depends_on=[clerk-lapse-recorded]
REVIEW QUOTE 82:> Tick 16: After my lapse record, I made the first-passage docket review at the Chalk Stair.
REVIEW QUOTE 83:> The entry remains open.
REVIEW QUOTE 84:> No new filings have been lodged.
REVIEW QUOTE 85:> I make no finding and resolve nothing.
REVIEW QUOTE 86:> Both accounts stand unresolved.
DELIVERED README.md sha256=a312a364d4d9476e98c0fae3f62b23bf72e73a06c508aac04ffe48cf9cf4c5fa
DELIVERED claim-excerpt-map.md sha256=16981162f8476a8fcc1bd892ac0b1b9e6cb916e1d45e6f2ea392a5eeca769244
RESULT PASS: inheritance, anchors, review isolation, counts, and documentation whitespace
```

Final `Read` inspections covered both complete edited documents (README 29 lines; map 74 lines) and confirmed the delivered pointer/anchor shapes and explicit bounds. The quoted review lines are authored content, not semantic truth certified by the gates.

## Path, status, and initial absence observations

Before this report's `Write`, this exact command exited 0:

```sh
python3 - <<'PY'
from pathlib import Path
root = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
assert Path.cwd().resolve() == root.resolve()
report = root / '.ufo/waves/round-100/seats/T3-fixture-docs.md'
assert report.resolve() == root.resolve() / '.ufo/waves/round-100/seats/T3-fixture-docs.md'
assert report.parent.resolve() == root.resolve() / '.ufo/waves/round-100/seats'
assert not report.exists()
assert not report.is_symlink()
print(f'REPORT PATH VERIFIED {report.resolve()}')
PY
```

Observed stdout:

```text
REPORT PATH VERIFIED /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/T3-fixture-docs.md
```

The scoped status command, before report creation, was:

```sh
git status --short -- corpus/fixtures/r100-docket-review .ufo/waves/round-100/seats/T3-fixture-docs.md && git diff --stat fe1ce46 -- corpus/fixtures/r99-window-lapse
```

Observed stdout, exit 0:

```text
?? corpus/fixtures/r100-docket-review/
```

The second command produced no diff: r99 was untouched. The untracked fixture is expected during the wave; the explicit Python whitespace check above validates the owned documentation rather than relying on `git diff --check` ignoring untracked files.

Initial, pre-delivery filesystem observations were recorded rather than treated as fixture verdicts:

- Direct `Read` of `/home/vgpnk/Projects/shokunin/lore-shokunin/AGENTS.md` returned `does not exist`; recursive `AGENTS.md` glob found none in the lane.
- Initial command `pwd && realpath corpus/fixtures .ufo/waves/round-100/seats && ls .ufo/waves/round-100/seats` returned the correct lane cwd and fixture path, then `realpath: .ufo/waves/round-100/seats: No such file or directory`, exit 1; its final `ls` was not executed.
- Initial r100 artifact glob found no matches and the initial T2-report glob reported the absent seats directory. The bounded wait above subsequently resolved these absences.
- `git rev-parse HEAD` observed `b5fe472957ab1e4e9c90f5613acc14cd24a288ae`; inheritance comparisons deliberately use the declared r99 closure `fe1ce46`, not an assumed current HEAD.

All delivered-revision validation commands passed. No unresolved T3 blocker or failed validation remains. Census 174, the frozen chain, synthesis dossier, and C3 are outside this seat's certification; this report does not claim those checks.

PASS — T3 README and canonical map delivered: 22/22 obligations, 22/22 lexical source support, 24/24 validated rows, CLEAN; 21 inherited anchor outputs and line numbers preserved with namespace-only qualification, and the isolated tick-16 review leaves the entry open and resolves nothing.
