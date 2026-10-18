from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import hashlib
import json
import shlex
import subprocess

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
SCRATCH = ROOT / '.ufo/waves/round-100/seats/V27-scratch'
assert Path.cwd() == ROOT
T4 = '.ufo/waves/round-100/seats/T4-scratch/replays/'
TABLE = (ROOT / 'corpus/knowledge/r99-gate-blind-spot-table.md').read_text()
def freeze(case, fixture):
    return ['python3', T4 + case + '/corpus/tools/dependency_freeze.py', T4 + case + '/corpus/fixtures/' + fixture]
commands = [
    ('row10-pre-r99-support', ['python3', T4 + 'pre-r99-anchor/corpus/tools/support_check.py', T4 + 'pre-r99-anchor/corpus/fixtures/r95-crossing-aftermath'], 1),
    ('row10-delivered-support', ['python3', 'corpus/tools/support_check.py', T4 + 'delivered-anchor/corpus/fixtures/r95-crossing-aftermath'], 1),
    ('row10-pre-r99-freeze', freeze('pre-r99-anchor', 'r95-crossing-aftermath'), 0),
    ('row10-delivered-freeze', freeze('delivered-anchor', 'r95-crossing-aftermath'), 2),
    ('row11-precedence', freeze('delivered-precedence', 'r98-clerk-filing'), 1),
    ('row11-prose-control', freeze('delivered-prose-control', 'r98-clerk-filing'), 2),
    ('row12-invalid', ['python3', 'corpus/tools/dependency_freeze.py', 'corpus/fixtures/r98-clerk-filing', '--freeze', 'corpus/fixtures/r98-clerk-filing'], 2),
]
for case in ['delivered-anchor', 'delivered-precedence', 'delivered-prose-control']:
    for name in ['dependency_freeze.py', 'dependency-freeze-contract.json']:
        assert (ROOT / (T4 + case + '/corpus/tools/' + name)).read_bytes() == (ROOT / 'corpus/tools' / name).read_bytes(), (case, name)
old = subprocess.check_output(['git', 'show', '4265df5:corpus/tools/support_check.py'], cwd=ROOT)
assert old == (ROOT / 'corpus/tools/support_check.py').read_bytes()
assert old == (ROOT / (T4 + 'pre-r99-anchor/corpus/tools/support_check.py')).read_bytes()
print('DELIVERED-MIRROR-TOOL-CONTRACT-IDENTITY True')
print('HISTORICAL-SUPPORT-TOOL-IDENTITY True')
contract = ROOT / 'corpus/tools/dependency-freeze-contract.json'
before = hashlib.sha256(contract.read_bytes()).hexdigest()
def run(item):
    label, cmd, expected = item
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    finding_lines = [line for line in p.stdout.splitlines() if line.startswith('FINDING ') or line.startswith('FAIL: ')]
    assert p.returncode == expected and not p.stderr, (label, p.returncode, p.stderr)
    assert all(line in TABLE for line in finding_lines), (label, finding_lines)
    if label == 'row11-precedence':
        assert 'DIGEST-MISMATCH' not in p.stdout
    if label == 'row12-invalid':
        assert len(finding_lines) == 1 and 'FREEZE ' not in p.stdout and 'DIGEST ' not in p.stdout
    return {'label': label, 'command': cmd, 'expected_exit': expected, 'exit': p.returncode, 'stdout': p.stdout, 'stderr': p.stderr, 'findings_match_published': True}
with ThreadPoolExecutor(max_workers=7) as pool:
    results = list(pool.map(run, commands))
for result in results:
    print('$ ' + shlex.join(result['command']))
    print(result['stdout'].rstrip())
    print('exit=' + str(result['exit']))
    print('PUBLISHED-FINDINGS-MATCH True')
after = hashlib.sha256(contract.read_bytes()).hexdigest()
print('LIVE-CONTRACT-UNCHANGED', before == after, before)
assert before == after
(SCRATCH / 'published-row-results.json').write_text(json.dumps(results, indent=2) + '\n')
print('PUBLISHED-ROWS 3/3 replayed; commands 7/7 expected; exact findings match; no contract write')
