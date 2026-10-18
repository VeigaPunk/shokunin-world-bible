from pathlib import Path
import hashlib
import json
import re
import shlex
import subprocess

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
NOTE = ROOT / 'corpus/knowledge/r100-provenance-semantics-boundary.md'
T4 = ROOT / '.ufo/waves/round-100/seats/T4-scratch/replays'
failures = []


def check(label, condition, detail=''):
    print(f'{label}: {"PASS" if condition else "FAIL"} {detail}'.rstrip())
    if not condition:
        failures.append(label)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


assert Path.cwd().resolve() == ROOT.resolve()
text = NOTE.read_text()
paths = set()
ranges = []
previous_path = None
for token in re.findall(r'`([^`]+)`', text):
    match = re.fullmatch(r'([^:]*):(\d+)(?:-(\d+))?', token)
    if match:
        path = match.group(1) or previous_path
        if path == 'dependency_freeze.py':
            path = 'corpus/tools/dependency_freeze.py'
        if path:
            start = int(match.group(2))
            end = int(match.group(3) or match.group(2))
            ranges.append((path, start, end))
            previous_path = path
            paths.add(path)
        continue
    if token.startswith('python3 '):
        paths.add(shlex.split(token)[1])
        continue
    if token.startswith(('corpus/', '.ufo/', 'LOG.md')) and '<' not in token:
        match = re.fullmatch(r'(.*)\{([^}]+)\}', token)
        if match:
            paths.update(match.group(1) + part for part in match.group(2).split(','))
        else:
            paths.add(token.rstrip('/'))
missing = sorted(path for path in paths if not (ROOT / path).exists())
check('CITED_ARTIFACTS', not missing, f'{len(paths)} paths; missing={missing}')
invalid = []
for path, start, end in ranges:
    count = len((ROOT / path).read_text().splitlines())
    if not 1 <= start <= end <= count:
        invalid.append((path, start, end, count))
check('CITED_RANGES', not invalid, f'{len(ranges)} full/continued ranges; invalid={invalid}')
contract = ROOT / 'corpus/tools/dependency-freeze-contract.json'
check('NOTE_DELIVERED_HASH', sha(NOTE) == '29cc7d856b2600bbb03dec577487bc0f09525ab444a3e3109ef0040ab7edeb36', sha(NOTE))
check('CONTRACT_DELIVERED_HASH', sha(contract) == 'ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5', sha(contract))
for name in ('delivered-anchor', 'delivered-precedence', 'delivered-prose-control', 'delivered-self-test'):
    for rel in ('corpus/tools/dependency_freeze.py', 'corpus/tools/dependency-freeze-contract.json', 'corpus/tools/support_check.py'):
        check(f'T4_MIRROR {name}/{rel}', (T4 / name / rel).read_bytes() == (ROOT / rel).read_bytes())
for rel in ('corpus/tools/dependency_freeze.py', 'corpus/tools/dependency-freeze-contract.json', 'corpus/tools/support_check.py'):
    historical = subprocess.check_output(['git', 'show', f'4265df5:{rel}'], cwd=ROOT)
    check(f'T4_HISTORICAL {rel}', historical == (T4 / 'pre-r99-anchor' / rel).read_bytes())
old_support = subprocess.check_output(['git', 'show', '4265df5:corpus/tools/support_check.py'], cwd=ROOT)
check('PRE_R99_SUPPORT_UNCHANGED', old_support == (ROOT / 'corpus/tools/support_check.py').read_bytes())
old_table = subprocess.check_output(['git', 'show', 'fe1ce46:corpus/knowledge/r99-gate-blind-spot-table.md'], cwd=ROOT)
check('HISTORICAL_TABLE_PREFIX', (ROOT / 'corpus/knowledge/r99-gate-blind-spot-table.md').read_bytes().startswith(old_table), f'{len(old_table)} baseline bytes')
for name, fixture in (('pre-r99-anchor', 'r95-crossing-aftermath'), ('delivered-anchor', 'r95-crossing-aftermath'), ('delivered-prose-control', 'r98-clerk-filing')):
    live = ROOT / 'corpus/fixtures' / fixture
    mirror = T4 / name / 'corpus/fixtures' / fixture
    expected = (live / 'fictional-excerpts.md').read_bytes().replace(b'depends on both ninth-bell entries', b'follows both ninth-bell entries', 1)
    check(f'EXCERPT_ONLY {name}', (mirror / 'fictional-excerpts.md').read_bytes() == expected and all((mirror / filename).read_bytes() == (live / filename).read_bytes() for filename in ('entities.json', 'relations.json', 'timeline.json', 'sources.json', 'contradictions.json', 'claim-excerpt-map.md')))
live = ROOT / 'corpus/fixtures/r98-clerk-filing'
mirror = T4 / 'delivered-precedence/corpus/fixtures/r98-clerk-filing'
expected = json.loads((live / 'timeline.json').read_text())
next(row for row in expected if row['id'] == 'paired-crossing-decision')['depends_on'] = ['aru-ninth-bell']
expected_prose = (live / 'fictional-excerpts.md').read_bytes().replace(b'depends on both ninth-bell entries', b'follows both ninth-bell entries', 1)
check('SIMULTANEOUS_EDGE_AND_PROSE', json.loads((mirror / 'timeline.json').read_text()) == expected and (mirror / 'fictional-excerpts.md').read_bytes() == expected_prose)
pins = json.loads(contract.read_text())['pins']
check('EXACT_SEVEN_PIN_BOUND', len(pins) == 7 and 'r99-window-lapse' in pins and 'r100-docket-review' not in pins and all(len(pin['files']) == 10 for pin in pins.values()))
check('R88_EXTRA_FILE_UNPINNED', 'symbolism-clause-map.md' not in pins['r88-m3-maya-cluster']['files'])
print('BOUNDARY-AUDIT', 'FAIL' if failures else 'PASS', f'failures={failures}')
raise SystemExit(bool(failures))
