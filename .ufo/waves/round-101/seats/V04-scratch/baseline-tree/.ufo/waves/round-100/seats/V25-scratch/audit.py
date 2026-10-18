from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import hashlib
import json
import re
import shlex
import subprocess

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
SCRATCH = ROOT / '.ufo/waves/round-100/seats/V25-scratch'
assert Path.cwd().resolve() == ROOT
assert Path(__file__).resolve().parent == SCRATCH.resolve()
checks = []

def check(label, condition, detail):
    checks.append({'label': label, 'passed': bool(condition), 'detail': detail})
    print(label, 'PASS' if condition else 'FAIL', detail)

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

expected = {
    'corpus/knowledge/r100-crossing-arc-synthesis.md': '6fcffc8154a11419adbcaefba6d728ee544af831cb5e1b999429404c3b243acc',
    'corpus/knowledge/r100-provenance-semantics-boundary.md': '29cc7d856b2600bbb03dec577487bc0f09525ab444a3e3109ef0040ab7edeb36',
    'corpus/knowledge/r99-gate-blind-spot-table.md': 'f1b3719a3954bbae44562f9e01b99434327ff50fba0c3a0755634dc9d76830ff',
    'corpus/tools/dependency-freeze-contract.json': 'ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5',
}
for name, want in expected.items():
    actual = digest(ROOT / name)
    check('DELIVERED-SHA256', actual == want, name + ' ' + actual)
    raw = (ROOT / name).read_bytes()
    check('TEXT-HYGIENE', raw.endswith(b'\n') and not any(line.rstrip(b' \t') != line for line in raw.splitlines()), name)

name = 'corpus/knowledge/r99-gate-blind-spot-table.md'
base_result = subprocess.run(['git', 'show', 'fe1ce46:' + name], cwd=ROOT, capture_output=True)
base = base_result.stdout
current = (ROOT / name).read_bytes()
check('TABLE-HISTORICAL-PREFIX', base_result.returncode == 0 and current.startswith(base), f'baseline_bytes={len(base)} added_bytes={len(current)-len(base)}')
rows = [line for line in current.decode().splitlines() if re.match(r'\| 1[012] \|', line)]
check('TABLE-THREE-DATED-ROWS', len(rows) == 3 and all('2026-10-17 / r100' in row for row in rows), rows)

for name in ('corpus/tools/dependency_freeze.py', 'corpus/tools/support_check.py', 'corpus/tools/map_obligations.py', 'corpus/fixtures/check_bible.py'):
    base = subprocess.run(['git', 'show', 'fe1ce46:' + name], cwd=ROOT, capture_output=True)
    check('TOOL-BASELINE-IDENTITY', base.returncode == 0 and base.stdout == (ROOT / name).read_bytes(), name + ' ' + digest(ROOT / name))

historical_support = SCRATCH / 'r95-historical-anchor-removal/corpus/tools/support_check.py'
check('HISTORICAL-SUPPORT-IDENTITY', historical_support.read_bytes() == (ROOT / 'corpus/tools/support_check.py').read_bytes(), digest(historical_support))
main = json.loads((SCRATCH / 'replay-delivered.json').read_text())
controls = json.loads((SCRATCH / 'controls-delivered.json').read_text())
check('SAVED-REPLAY-RECEIPTS', len(main['checks']) == 17 and all(item['passed'] for item in main['checks']) and main['unchanged'], '17/17 expected observations; tracked live and mirror hashes unchanged')
check('SAVED-CONTROL-RECEIPTS', len(controls['results']) == 7 and all(item['expected_match'] for item in controls['results']) and controls['live_contract_before'] == controls['live_contract_after'], '7/7 expected observations; contract unchanged')
for name, saved_hash in main['after'].items():
    check('REPLAY-INPUT-STABILITY', digest(ROOT / name) == saved_hash, name)

contract = json.loads((ROOT / 'corpus/tools/dependency-freeze-contract.json').read_text())
names = sorted(contract['pins'])
check('PIN-SCOPE-BOUND', len(names) == 7 and 'r99-window-lapse' in names and 'r100-docket-review' not in names, names)
commands = [(['python3', 'corpus/tools/dependency_freeze.py', 'corpus/fixtures/' + name], 0) for name in names]
commands.append((['python3', 'corpus/tools/dependency_freeze.py', 'corpus/fixtures/r100-docket-review'], 2))

def run(item):
    argv, expected_exit = item
    result = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True)
    ok = result.returncode == expected_exit
    if expected_exit == 2:
        ok = ok and 'UNPINNED-FIXTURE' in result.stdout
    return {'command': shlex.join(argv), 'exit': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr, 'expected_match': ok}

with ThreadPoolExecutor(max_workers=8) as pool:
    receipts = list(pool.map(run, commands))
for receipt in receipts:
    print('COMMAND', receipt['command'])
    print(receipt['stdout'], end='')
    print(receipt['stderr'], end='')
    print('exit=' + str(receipt['exit']))
check('LIVE-PIN-BOUND-REPLAYS', all(item['expected_match'] for item in receipts), '7 pinned PASS; r100 UNPINNED-FIXTURE exit 2')
for name, want in expected.items():
    check('POST-AUDIT-SHA256', digest(ROOT / name) == want, name)

result = {'checks': checks, 'gate_receipts': receipts, 'expected_sha256': expected}
output = SCRATCH / 'audit-delivered.json'
assert not output.exists(), output
output.write_text(json.dumps(result, indent=2) + '\n')
print('AUDIT-CHECKS', sum(item['passed'] for item in checks), '/', len(checks))
raise SystemExit(0 if all(item['passed'] for item in checks) else 1)
