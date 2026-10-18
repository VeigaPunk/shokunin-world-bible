from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import re
import shlex
import subprocess

root = Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
assert Path.cwd().resolve() == root
seats = root / '.ufo/waves/round-100/seats'
reports = sorted(p.name for p in seats.iterdir() if p.is_file() and p.name.startswith('T4') and p.suffix == '.md')
assert reports, 'T4 producer report absent: do not verify a plan'
print('PRODUCER REPORTS ' + ', '.join(reports))
dossier = root / 'corpus/knowledge/r100-crossing-arc-synthesis.md'
text = dossier.read_text()
print('DOSSIER SHA256 ' + hashlib.sha256(dossier.read_bytes()).hexdigest())
print('HEAD ' + subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip())
names = ['r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing', 'r99-window-lapse', 'r100-docket-review']
rows = [line for line in text.splitlines() if line.startswith(('| Seed ', '| Beat '))]
assert len(rows) == len(names) == 7
fixtures = []
for name, row in zip(names, rows):
    cells = [cell.strip() for cell in row.strip('|').split('|')]
    cited = re.findall(r'`([^`]+)`', cells[1])[0]
    fixture = root / cited
    assert cited == f'corpus/fixtures/{name}/'
    data = {section: json.loads((fixture / f'{section}.json').read_text()) for section in ('entities', 'relations', 'timeline', 'sources', 'contradictions')}
    event_id, event_pointer = re.findall(r'`([^`]+)`', cells[2])
    source_id, source_pointer = re.findall(r'`([^`]+)`', cells[3])
    assert event_pointer.startswith('timeline.json#/') and source_pointer.startswith('sources.json#/')
    event = data['timeline'][int(event_pointer.split('#/')[1])]
    source = data['sources'][int(source_pointer.split('#/')[1])]
    tick = int(re.search(r'tick (\d+)', cells[2]).group(1))
    assert event is data['timeline'][-1] and source is data['sources'][-1]
    assert event['id'] == event_id and event['tick'] == tick
    assert source['id'] == source_id == event['source_id']
    counts = tuple(len(data[key]) for key in ('entities', 'relations', 'timeline'))
    obligations = sum(1 + len(entity['claims']) for entity in data['entities']) + len(data['relations']) + len(data['timeline'])
    assert counts == tuple(map(int, cells[4].split('/')))
    assert len(data['sources']) == int(cells[5])
    assert obligations == int(cells[6])
    mapped = len(re.findall(r'^\| J\d+ \|', (fixture / 'claim-excerpt-map.md').read_text(), re.M))
    assert mapped == obligations
    assert data['contradictions'] == []
    print(f'ROW {name} E/R/T={cells[4]} sources={len(data["sources"])} obligations={obligations}/{mapped} event={event_id} pointer={event_pointer} tick={tick} source={source_id} source_pointer={source_pointer} contradictions=0')
    fixtures.append((fixture, data))
for (old_path, old), (new_path, new) in zip(fixtures, fixtures[1:]):
    for key in ('entities', 'timeline', 'sources'):
        assert new[key][:len(old[key])] == old[key], (new_path.name, key)
    assert new['relations'] == old['relations'] and new['contradictions'] == old['contradictions']
    assert (new_path / 'fictional-excerpts.md').read_bytes().startswith((old_path / 'fictional-excerpts.md').read_bytes())
    for filename in ('inspiration-note.md', 'source-excerpt.md'):
        assert (new_path / filename).read_bytes() == (old_path / filename).read_bytes()
    old_map = (old_path / 'claim-excerpt-map.md').read_text().splitlines()
    new_map = (new_path / 'claim-excerpt-map.md').read_text().splitlines()
    old_rows = [line for line in old_map if re.match(r'^\| J\d+ \|', line)]
    new_rows = [line for line in new_map if re.match(r'^\| J\d+ \|', line)]
    inherited_rows = [line.replace(new_path.name + ':', old_path.name + ':') for line in new_rows[:len(old_rows)]]
    assert old_rows == inherited_rows, (old_path.name, new_path.name, 'map rows')
    assert [line for line in old_map if line.startswith('| S0')] == [line for line in new_map if line.startswith('| S0')]
    assert new['timeline'][-1]['depends_on'] == [old['timeline'][-1]['id']]
    print(f'PRESERVATION {old_path.name}->{new_path.name} JSON=PASS excerpt-prefix=PASS external-bytes=PASS map={len(old_rows)}/{len(old_rows)} namespace-only edge=PASS')
old_path, _ = fixtures[-2]
new_path, new = fixtures[-1]
for filename in ('contradictions.json', 'entities.json', 'relations.json', 'inspiration-note.md', 'source-excerpt.md'):
    assert (old_path / filename).read_bytes() == (new_path / filename).read_bytes()
print(f'R99-R100 five byte-identical files; excerpt_bytes={len((old_path / "fictional-excerpts.md").read_bytes())}->{len((new_path / "fictional-excerpts.md").read_bytes())}')
review = new['timeline'][-1]
assert (review['id'], review['tick'], review['entity_id'], review['place_id'], review['depends_on'], review['source_id']) == ('clerk-review-first-passage', 16, 'clerk-maren', 'chalk-stair', ['clerk-lapse-recorded'], 'clerk-review-note')
assert new['entities'][-1]['first_appearance'] == 'clerk-filing-note'
assert new['relations'] == [{'from': 'aru', 'to': 'evin', 'type': 'agreed_co_stewardship_for_this_crossing', 'source_id': 'crossing-minute'}]
print('REVIEW ' + json.dumps(review, sort_keys=True))
paths = set()
ranges = []
tokens = re.findall(r'`([^`\n]+)`', text) + re.findall(r'\.ufo/[A-Za-z0-9_./-]+', text)
for token in tokens:
    if not token.startswith(('corpus/', '.ufo/', 'LOG.md', str(root))):
        continue
    match = re.fullmatch(r'(.+):([0-9]+)(?:-([0-9]+))?', token)
    if match:
        token = match[1]
        first, last = int(match[2]), int(match[3] or match[2])
        line_count = len((root / token).read_text().splitlines())
        assert 1 <= first <= last <= line_count, (token, first, last, line_count)
        ranges.append((token, first, last))
    expansion = re.fullmatch(r'([^{}]+)\{([^{}]+)\}', token)
    expanded = [expansion[1] + filename for filename in expansion[2].split(',')] if expansion else [token]
    for relative in expanded:
        path = root / relative
        assert path.resolve().is_relative_to(root) and path.exists(), relative
        paths.add(path)
files = {path for path in paths if path.is_file()}
print(f'CITED PATHS {len(paths)}/{len(paths)} exist; files={len(files)} directories={len(paths)-len(files)}; explicit ranges={len(ranges)}/{len(ranges)} in bounds; contextual JSON pointers=14/14 resolve')
for relative, first, last in ranges:
    print(f'RANGE {relative}:{first}-{last} OK')
for label in ('No testimony truth.', 'No chronology authentication.', 'No expansion of duty.', 'No automatic source identity.', 'No semantic or canon certification by gates.', 'Rights and AI-training permission unassessed.'):
    assert label in text, label
    print('BOUND PRESENT ' + label)
assert 'editorial normalizations' in text and 'not literal JSON quotations' in text
assert 'seven snapshot records' in text and 'six continuation beats r95–r100' in text
print('NUMBERING seed r94 + six continuations r95-r100 explicitly distinguished')
for (fixture, _), (first, last) in zip(fixtures[1:], [(26, 29), (37, 40), (48, 51), (59, 62), (70, 74), (82, 86)]):
    lines = (fixture / 'fictional-excerpts.md').read_text().splitlines()
    print(f'MANUAL SEMANTIC EVIDENCE {fixture.name}/fictional-excerpts.md:{first}-{last}')
    for number in range(first, last + 1):
        print(f'{number}:{lines[number - 1]}')
contract = json.loads((root / 'corpus/tools/dependency-freeze-contract.json').read_text())
expected_pins = ['r88-m3-maya-cluster', *names[:-1]]
assert sorted(contract['pins']) == sorted(expected_pins)
assert names[-1] not in contract['pins']
print('PIN SET ' + ', '.join(sorted(contract['pins'])) + '; r100 unpinned as dossier states')
census = sum(path.is_dir() for path in (root / 'corpus/fixtures').iterdir())
assert census == 174
print(f'CENSUS {census}')
tools = ['corpus/fixtures/check_bible.py', 'corpus/tools/map_obligations.py', 'corpus/tools/support_check.py']
for tool in tools:
    digest = hashlib.sha256((root / tool).read_bytes()).hexdigest()
    assert re.search(rf'`{digest}` \(`{re.escape(tool)}`\)', text), (tool, digest)
    print(f'TOOL HASH MATCH {tool} {digest}')
checked_files = files | {dossier} | {root / tool for tool in tools}
initial = {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in checked_files}
commands = [['python3', tool, f'corpus/fixtures/{name}'] for name in names for tool in tools]
def run(command):
    result = subprocess.run(command, capture_output=True, text=True, env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'})
    lines = result.stdout.splitlines()
    if command[1].endswith('support_check.py'):
        lines = [line for line in lines if line.startswith(('INVENTORY', 'SOURCE-SUPPORT', 'RESULT', 'FAIL', 'WARN'))]
    return command, result, lines
with ThreadPoolExecutor(max_workers=12) as pool:
    for command, result, lines in pool.map(run, commands):
        print('COMMAND ' + shlex.join(command))
        for line in lines:
            print(line)
        if result.stderr:
            print(result.stderr.rstrip())
        print('EXIT ' + str(result.returncode))
        assert result.returncode == 0, command
assert all(hashlib.sha256(path.read_bytes()).hexdigest() == digest for path, digest in initial.items())
print(f'STABILITY {len(checked_files)}/{len(checked_files)} cited/document/tool files unchanged across gate replay')
print('RESULT PASS: byte/count/pointer/path checks and 21 live gate calls; prose conclusions require the manual review recorded in V11 report')
