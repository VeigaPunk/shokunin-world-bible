import concurrent.futures
from collections import Counter
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
SCRATCH = ROOT / '.ufo/waves/round-100/seats/V29-scratch'
SEATS = ROOT / '.ufo/waves/round-100/seats'
assert Path.cwd().resolve() == ROOT
assert SCRATCH.resolve().is_relative_to(ROOT)
reports = {}
for path in SEATS.iterdir():
    match = re.fullmatch(r'T0?([1-4])-.*\.md', path.name)
    if match and path.is_file() and path.stat().st_size:
        reports[int(match[1])] = path.name
if set(reports) != {1, 2, 3, 4}:
    print('ABSENT PRODUCER REPORTS', sorted({1, 2, 3, 4} - set(reports)))
    raise SystemExit(2)
print('PRODUCER REPORTS PRESENT', reports)

fixture = Path('corpus/fixtures/r100-docket-review')
files = ['entities.json', 'relations.json', 'timeline.json', 'sources.json', 'contradictions.json', 'README.md', 'claim-excerpt-map.md', 'fictional-excerpts.md', 'inspiration-note.md', 'source-excerpt.md']
relevant = [
    'PROVINCE.md', 'SHONEN.md', 'SKILL.md',
    'corpus/fixtures/check_bible.py',
    'corpus/tools/dependency_freeze.py', 'corpus/tools/dependency-freeze-contract.json',
    'corpus/tools/README.md', 'corpus/tools/map_obligations.py',
    'corpus/tools/map-obligations-contract.json', 'corpus/tools/support_check.py',
    'corpus/tools/boundary_doc_check.py', 'corpus/tools/boundary-doc-contract.json',
    'corpus/knowledge/r99-gate-blind-spot-table.md',
    'corpus/knowledge/r100-crossing-arc-synthesis.md',
    'corpus/knowledge/r100-provenance-semantics-boundary.md',
] + [str(fixture / name) for name in files]

def snapshot():
    return {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in relevant}

def original(path):
    return subprocess.check_output(['git', 'show', 'fe1ce46:' + str(path)], cwd=ROOT)

def run(command):
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    return {'command': command, 'exit': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr}

before = snapshot()
contract_path = Path('corpus/tools/dependency-freeze-contract.json')
old_contract = json.loads(original(contract_path))
contract = json.loads((ROOT / contract_path).read_bytes())
assert set(contract['pins']) - set(old_contract['pins']) == {'r99-window-lapse'}
assert all(contract['pins'][name] == value for name, value in old_contract['pins'].items())
assert len(contract['pins']) == 7
assert [name for name in old_contract if old_contract[name] != contract[name]] == ['revision', 'pins']
assert contract['schema_version'] == contract['payload_schema_version'] == 2
pin = contract['pins']['r99-window-lapse']
assert pin['payload_schema_version'] == 2
assert pin['pinned_files'] == files
assert set(pin['files']) == set(files)
assert all(hashlib.sha256((ROOT / pin['fixture'] / name).read_bytes()).hexdigest() == pin['files'][name] for name in files)
print('C1 seven pins; old_pin_changes=[]; changed_top_level=[revision,pins]; schema=2; r99_file_hashes=10/10')

inherited = {}
for table in ('entities', 'relations', 'timeline', 'sources', 'contradictions'):
    old = json.loads(original(Path('corpus/fixtures/r99-window-lapse') / (table + '.json')))
    new = json.loads((ROOT / fixture / (table + '.json')).read_bytes())
    if table in ('timeline', 'sources'):
        assert new[:-1] == old
        assert len(new) == len(old) + 1
    else:
        assert new == old
    inherited[table] = [len(old), len(new)]
assert inherited == {'entities': [6, 6], 'relations': [1, 1], 'timeline': [8, 9], 'sources': [8, 9], 'contradictions': [0, 0]}
for name in ('entities.json', 'relations.json', 'contradictions.json', 'inspiration-note.md', 'source-excerpt.md'):
    assert (ROOT / fixture / name).read_bytes() == original(Path('corpus/fixtures/r99-window-lapse') / name)
old_excerpt = original(Path('corpus/fixtures/r99-window-lapse/fictional-excerpts.md'))
new_excerpt = (ROOT / fixture / 'fictional-excerpts.md').read_bytes()
assert new_excerpt.startswith(old_excerpt)
old_map = original(Path('corpus/fixtures/r99-window-lapse/claim-excerpt-map.md')).decode()
new_map = (ROOT / fixture / 'claim-excerpt-map.md').read_text()
old_rows = [line for line in old_map.splitlines() if re.match(r'^\| J\d+ \|', line)]
new_rows = [line for line in new_map.splitlines() if re.match(r'^\| J\d+ \|', line)]
assert len(old_rows) == 21 and len(new_rows) == 22
assert [row.replace('r99-window-lapse:', 'r100-docket-review:') for row in old_rows] == new_rows[:-1]
old_editorial = [line for line in old_map.splitlines() if re.match(r'^\| S\d+ \|', line)]
new_editorial = [line for line in new_map.splitlines() if re.match(r'^\| S\d+ \|', line)]
assert old_editorial == new_editorial
print('C2 inheritance=' + json.dumps(inherited, sort_keys=True))
print(f'C2 byte-identical files=5/5; excerpt_prefix={len(old_excerpt)}/{len(old_excerpt)}; inherited_map_rows=21/21 apart from namespace; new_map_rows=22; editorial_rows=2 unchanged')
blind_spot_path = Path('corpus/knowledge/r99-gate-blind-spot-table.md')
assert (ROOT / blind_spot_path).read_bytes().startswith(original(blind_spot_path))
print('C3 old blind-spot-table bytes preserved as prefix; new addenda require manual whole-text review')

chain = list(contract['pins'])
commands = [['python3', '-B', 'corpus/tools/dependency_freeze.py', 'corpus/fixtures/' + name] for name in chain]
commands.extend([
    ['python3', '-B', 'corpus/fixtures/check_bible.py', str(fixture)],
    ['python3', '-B', 'corpus/tools/support_check.py', str(fixture)],
    ['python3', '-B', 'corpus/tools/map_obligations.py', str(fixture)],
    ['python3', '-B', 'corpus/tools/boundary_doc_check.py'],
    ['python3', '-B', 'corpus/tools/discriminate_check.py'],
    ['python3', '-B', 'corpus/tools/map_obligations.py', '--frozen', '.ufo/waves/round-94/frozen/map-obligations-r93'],
])
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    receipts = list(executor.map(run, commands))
for receipt in receipts:
    print('$ ' + ' '.join(receipt['command']))
    print(receipt['stdout'], end='')
    print(receipt['stderr'], end='')
    print('observed_exit=' + str(receipt['exit']))
assert all(receipt['exit'] == 0 and not receipt['stderr'] for receipt in receipts)
print('LIVE GATES', str(len(receipts)) + '/' + str(len(receipts)), 'exit=0 stderr_empty=True')

old_names = subprocess.check_output(['git', 'ls-tree', '-d', '--name-only', 'fe1ce46:corpus/fixtures'], cwd=ROOT, text=True).splitlines()
names = old_names + ['r100-docket-review']
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    census = list(executor.map(run, [['python3', '-B', 'corpus/fixtures/check_bible.py', 'corpus/fixtures/' + name] for name in names]))
counts = Counter(receipt['exit'] for receipt in census)
violations = sum(sum(line.startswith('VIOLATION:') for line in receipt['stdout'].splitlines()) for receipt in census)
assert len(old_names) == 173 and len(names) == 174
assert dict(counts) == {1: 134, 0: 40} and violations == 421
assert not any(receipt['stderr'] for receipt in census)
assert subprocess.check_output(['git', 'diff', 'fe1ce46', '--name-only', '--', 'corpus/fixtures'], cwd=ROOT, text=True) == ''
print(f'CENSUS directories={len(names)} clean={counts[0]} intentional_negative={counts[1]} violations={violations} stderr_nonempty=0 inherited_tracked_edits=0')
after = snapshot()
assert before == after
print('DELIVERED-SNAPSHOT-STABLE', len(after), 'files')
for name, digest in after.items():
    print('SHA256', digest, name)
out = SCRATCH / 'delivery-evidence.json'
assert out.resolve().is_relative_to(SCRATCH)
out.write_text(json.dumps({'at': datetime.now().astimezone().isoformat(), 'producer_reports': reports, 'hashes': after, 'inheritance': inherited, 'receipts': receipts, 'census': census}, indent=2) + '\n')
print('EVIDENCE', out)
print('RESULT PASS: C1/live-C2 gates and preservation; dossier semantics/C3 text assessed separately')
