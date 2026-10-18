from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
import shlex
import shutil
import subprocess

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
S = ROOT / '.ufo/waves/round-100/seats/V28-scratch'
assert Path.cwd().resolve() == ROOT
assert (S / 'ready-manifest.json').is_file()
contract = ROOT / 'corpus/tools/dependency-freeze-contract.json'
contract_before = contract.read_bytes()
commands = []

def case(name, transforms=None, fixture_name='r99-window-lapse'):
    target_root = S / 'replays' / name
    tools = target_root / 'corpus/tools'
    fixture = target_root / 'corpus/fixtures' / fixture_name
    tools.mkdir(parents=True)
    fixture.mkdir(parents=True)
    for tool in ['dependency_freeze.py', 'dependency-freeze-contract.json']:
        shutil.copy2(ROOT / 'corpus/tools' / tool, tools / tool)
    for p in (ROOT / 'corpus/fixtures' / fixture_name).iterdir():
        raw = p.read_bytes()
        if transforms and p.name in transforms:
            raw = transforms[p.name](raw)
        (fixture / p.name).write_bytes(raw)
    return target_root, tools / 'dependency_freeze.py', fixture

def changed_wording(raw):
    old = b'depends on both ninth-bell entries'
    assert raw.count(old) == 1
    return raw.replace(old, b'follows both ninth-bell entries')

def removed_edge(raw):
    data = json.loads(raw)
    assert data[-1]['id'] == 'clerk-lapse-recorded'
    data[-1]['depends_on'] = []
    return (json.dumps(data, indent=2) + '\n').encode()

def add(name, argv, expected, must=(), must_not=()):
    commands.append((name, ['python3', *[str(x) for x in argv]], expected, must, must_not))

_, tool, fixture = case('clean')
add('clean-pinned', [tool, fixture], 0, ('RESULT PASS',))
for name, transforms in [('anchor-only', {'fictional-excerpts.md': changed_wording}), ('coherent-anchor', {'fictional-excerpts.md': changed_wording, 'claim-excerpt-map.md': changed_wording})]:
    _, tool, fixture = case(name, transforms)
    add(f'{name}-freeze', [tool, fixture], 2, ('DIGEST-MISMATCH', 'fictional-excerpts.md'))
    add(f'{name}-bible', ['corpus/fixtures/check_bible.py', fixture], 0, ('CLEAN:',))
    add(f'{name}-map', ['corpus/tools/map_obligations.py', fixture], 0, ('RESULT PASS',))
    add(f'{name}-support', ['corpus/tools/support_check.py', fixture], 1 if name == 'anchor-only' else 0, ('RESULT FAIL', 'J14') if name == 'anchor-only' else ('RESULT PASS',))
_, tool, fixture = case('precedence', {'timeline.json': removed_edge})
add('semantic-before-digest', [tool, fixture], 1, ('REDUCTION-DETECTED',), ('DIGEST-MISMATCH',))
_, tool, fixture = case('combined')
add('combined-invalid-only', [tool, fixture, '--freeze', fixture], 2, ('INVALID-ARGUMENTS',), ('FREEZE ', 'DIGEST-MISMATCH', 'REDUCTION-DETECTED'))
root, tool, fixture = case('scope')
foreign = root / 'foreign/r99-window-lapse'
foreign.mkdir(parents=True)
add('scope-refusal', [tool, '--freeze', foreign], 2, ('SCOPE-REFUSED',))
root, tool, fixture = case('path')
foreign = root / 'foreign/r99-window-lapse'
shutil.copytree(fixture, foreign)
add('path-refusal', [tool, foreign], 2, ('PATH-MISMATCH',))
_, tool, fixture = case('outside-ten', {'symbolism-clause-map.md': lambda raw: raw + b'\nV28 byte-detectability bound control.\n'}, 'r88-m3-maya-cluster')
add('outside-ten-remains-unpinned', [tool, fixture], 0, ('RESULT PASS',))
_, tool, fixture = case('byte-only', {'source-excerpt.md': lambda raw: raw + b'\n'})
add('byte-only-edit', [tool, fixture], 2, ('DIGEST-MISMATCH', 'source-excerpt.md'))
env = {**os.environ, 'PYTHONDONTWRITEBYTECODE': '1', 'TMPDIR': str(S / 'tmp')}

def run(item):
    name, command, expected, must, must_not = item
    p = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, env=env, timeout=60)
    ok = p.returncode == expected and all(token in p.stdout for token in must) and all(token not in p.stdout for token in must_not) and not p.stderr
    return {'name': name, 'command': shlex.join(command), 'exit': p.returncode, 'expected_exit': expected, 'stdout': p.stdout, 'stderr': p.stderr, 'matched': ok}

results = list(ThreadPoolExecutor(max_workers=8).map(run, commands))
(S / 'boundary-replays.json').write_text(json.dumps(results, indent=2) + '\n')
transcript = ''.join('$ ' + r['command'] + '\n' + r['stdout'] + r['stderr'] + f"exit={r['exit']} matched={r['matched']}\n\n" for r in results)
(S / 'boundary-replays.txt').write_text(transcript)
print(transcript)
assert contract.read_bytes() == contract_before
for p in (S / 'replays').glob('*/corpus/tools/dependency-freeze-contract.json'):
    assert p.read_bytes() == contract_before, p
summary = {'checks': len(results), 'failed': [r['name'] for r in results if not r['matched']], 'live_contract_unchanged': True, 'mirror_contracts_unchanged': True, 'contract_sha256': hashlib.sha256(contract_before).hexdigest()}
(S / 'boundary-replays-summary.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary, sort_keys=True))
raise SystemExit(bool(summary['failed']))
