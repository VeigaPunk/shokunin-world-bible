from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import hashlib
import json
import shlex
import subprocess
import sys

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
SCRATCH = ROOT / '.ufo/waves/round-100/seats/V25-scratch'
assert Path.cwd().resolve() == ROOT
assert Path(__file__).resolve().parent == SCRATCH.resolve()

commands = []
for case in ('clean', 'mapped-anchor-removal', 'semantic-precedence'):
    mirror = SCRATCH / case
    fixture = mirror / 'corpus/fixtures/r98-clerk-filing'
    for tool in ('dependency_freeze.py', 'check_bible.py', 'support_check.py', 'map_obligations.py'):
        script = mirror / 'corpus/tools/dependency_freeze.py' if tool == 'dependency_freeze.py' else ROOT / ('corpus/fixtures' if tool == 'check_bible.py' else 'corpus/tools') / tool
        commands.append((case + ':' + tool, ['python3', str(script), str(fixture)]))
mirror = SCRATCH / 'combined-arguments'
fixture = mirror / 'corpus/fixtures/r98-clerk-filing'
commands.append(('combined-arguments', ['python3', str(mirror / 'corpus/tools/dependency_freeze.py'), str(fixture), '--freeze', str(fixture)]))
for case in ('r95-delivered-anchor-removal', 'r95-historical-anchor-removal'):
    mirror = SCRATCH / case
    if not mirror.is_dir():
        continue
    fixture = mirror / 'corpus/fixtures/r95-crossing-aftermath'
    for tool in ('dependency_freeze.py', 'support_check.py'):
        commands.append((case + ':' + tool, ['python3', str(mirror / 'corpus/tools' / tool), str(fixture)]))

tracked = [ROOT / 'corpus/tools/dependency_freeze.py', ROOT / 'corpus/tools/dependency-freeze-contract.json', ROOT / 'corpus/tools/support_check.py', ROOT / 'corpus/tools/map_obligations.py', ROOT / 'corpus/fixtures/check_bible.py', ROOT / 'corpus/knowledge/r100-provenance-semantics-boundary.md', ROOT / 'corpus/knowledge/r99-gate-blind-spot-table.md']
tracked += sorted(SCRATCH.glob('*/corpus/tools/dependency-freeze-contract.json'))

def hashes():
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in tracked if p.is_file()}

before = hashes()

def run(item):
    label, argv = item
    result = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True)
    return {'case': label, 'command': shlex.join(argv), 'argv': argv, 'exit': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr}

with ThreadPoolExecutor(max_workers=8) as pool:
    results = list(pool.map(run, commands))
after = hashes()
checks = []
for result in results:
    label, output, code = result['case'], result['stdout'], result['exit']
    if label.startswith('clean:'):
        ok = code == 0
    elif label.startswith('mapped-anchor-removal:'):
        expected = 2 if label.endswith('dependency_freeze.py') else 1 if label.endswith('support_check.py') else 0
        ok = code == expected and ('DIGEST-MISMATCH' in output if expected == 2 else 'FAIL: J14: source-support anchor missing' in output if expected == 1 else True)
    elif label.startswith('semantic-precedence:'):
        expected = 1 if label.endswith(('dependency_freeze.py', 'support_check.py')) else 0
        ok = code == expected
        if label.endswith('dependency_freeze.py'):
            ok = ok and 'REDUCTION-DETECTED' in output and 'DIGEST-MISMATCH' not in output
    elif label == 'combined-arguments':
        ok = code == 2 and output.splitlines() == ['FINDING INVALID-ARGUMENTS: pass either a fixture (verify) or --freeze DIR, not both', 'RESULT ERROR']
    elif label.startswith('r95-'):
        expected = 1 if label.endswith('support_check.py') else 0 if label.startswith('r95-historical') else 2
        ok = code == expected
        if expected == 1:
            ok = ok and 'FAIL: J14: source-support anchor missing' in output
        elif expected == 2:
            ok = ok and 'DIGEST-MISMATCH' in output and 'fictional-excerpts.md' in output
    else:
        ok = False
    checks.append({'case': label, 'passed': ok})
    print('CASE', label)
    print('COMMAND', result['command'])
    print(output, end='')
    print(result['stderr'], end='')
    print('exit=' + str(code))
    print('EXPECTED-OBSERVATION-MATCH', ok)
unchanged = before == after
print('TRACKED-HASHES-UNCHANGED', unchanged)
print('REPLAY-CHECKS', sum(c['passed'] for c in checks), '/', len(checks))
report = {'root': str(ROOT), 'before': before, 'after': after, 'unchanged': unchanged, 'results': results, 'checks': checks}
output = SCRATCH / ('replay-' + sys.argv[1] + '.json')
assert not output.exists(), output
output.write_text(json.dumps(report, indent=2) + '\n')
print('TRANSCRIPT', output)
sys.exit(0 if unchanged and all(c['passed'] for c in checks) else 1)
