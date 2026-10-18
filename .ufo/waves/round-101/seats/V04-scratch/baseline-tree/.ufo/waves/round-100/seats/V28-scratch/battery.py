from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import datetime
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
M = S / 'selftest-mirror'
(M / 'corpus/tools').mkdir(parents=True)
(M / 'corpus/fixtures').mkdir(parents=True)
(S / 'tmp').mkdir(exist_ok=True)
for name in ['dependency_freeze.py', 'dependency-freeze-contract.json', 'map_obligations.py', 'map-obligations-contract.json']:
    shutil.copy2(ROOT / 'corpus/tools' / name, M / 'corpus/tools' / name)
shutil.copytree(ROOT / 'corpus/fixtures/r95-crossing-aftermath', M / 'corpus/fixtures/r95-crossing-aftermath')
env = {**os.environ, 'PYTHONDONTWRITEBYTECODE': '1', 'TMPDIR': str(S / 'tmp')}
commands = []

def add(name, argv, expected):
    commands.append((name, ['python3', *argv], expected))

fixtures = ['r88-m3-maya-cluster', 'r93-m2-kojiki-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing', 'r99-window-lapse', 'r100-docket-review']
for fixture in fixtures:
    for tool in ['support_check.py', 'map_obligations.py']:
        add(f'{tool}-{fixture}', [f'corpus/tools/{tool}', f'corpus/fixtures/{fixture}'], 0)
for fixture in ['r87-myth-cluster', 'r89-inspiration-paraphrase']:
    add(f'map-legacy-{fixture}', ['corpus/tools/map_obligations.py', f'corpus/fixtures/{fixture}'], 2)
    add(f'support-legacy-{fixture}', ['corpus/tools/support_check.py', f'corpus/fixtures/{fixture}'], 0)
for fixture in [name for name in fixtures if name not in ['r93-m2-kojiki-cluster', 'r100-docket-review']]:
    add(f'freeze-{fixture}', ['corpus/tools/dependency_freeze.py', f'corpus/fixtures/{fixture}'], 0)
add('freeze-r100-declared-unpinned', ['corpus/tools/dependency_freeze.py', 'corpus/fixtures/r100-docket-review'], 2)
add('freeze-self-test-scratch-mirror', [str(M / 'corpus/tools/dependency_freeze.py'), '--self-test'], 0)
add('map-self-test-scratch-mirror', [str(M / 'corpus/tools/map_obligations.py'), '--self-test'], 0)
add('boundary-default', ['corpus/tools/boundary_doc_check.py'], 0)
add('boundary-self-test', ['corpus/tools/boundary_doc_check.py', '--self-test'], 0)
add('discriminator-default', ['corpus/tools/discriminate_check.py'], 0)
add('discriminator-historical-control', ['corpus/tools/discriminate_check.py', '--checker', 'e97613c'], 2)
add('map-frozen-r93', ['corpus/tools/map_obligations.py', '--frozen', '.ufo/waves/round-94/frozen/map-obligations-r93'], 0)
for fixture in sorted((ROOT / 'corpus/fixtures').iterdir()):
    if fixture.is_dir():
        add(f'census-{fixture.name}', ['corpus/fixtures/check_bible.py', str(fixture.relative_to(ROOT))], None)

def run(case):
    name, argv, expected = case
    proc = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, env=env, timeout=120)
    record = {'name': name, 'command': shlex.join(argv), 'cwd': str(ROOT), 'expected_exit': expected, 'exit': proc.returncode, 'stdout': proc.stdout, 'stderr': proc.stderr}
    print(f'{name}: exit={proc.returncode} expected={expected} stdout_lines={len(proc.stdout.splitlines())} stderr_bytes={len(proc.stderr)}', flush=True)
    return record

records = list(ThreadPoolExecutor(max_workers=8).map(run, commands))
(S / 'battery-results.json').write_text(json.dumps(records, indent=2) + '\n')
transcript = ''
for record in records:
    transcript += '$ ' + record['command'] + '\n' + record['stdout'] + record['stderr'] + f"exit={record['exit']}\n\n"
(S / 'battery-transcript.txt').write_text(transcript)
census = [r for r in records if r['name'].startswith('census-')]
summary = {'timestamp': datetime.datetime.now().astimezone().isoformat(), 'checks': len(records), 'expected_exit_mismatches': [r['name'] for r in records if r['expected_exit'] is not None and r['exit'] != r['expected_exit']], 'stderr_cases': [r['name'] for r in records if r['stderr']], 'census': {'directories': len(census), 'clean': sum(r['exit'] == 0 for r in census), 'intentional_negative': sum(r['exit'] == 1 for r in census), 'other_exit': [r['name'] for r in census if r['exit'] not in [0, 1]], 'violation_lines': sum(sum(line.startswith('VIOLATION:') for line in r['stdout'].splitlines()) for r in census)}, 'mirror_byte_identity': {name: hashlib.sha256((ROOT / 'corpus/tools' / name).read_bytes()).hexdigest() == hashlib.sha256((M / 'corpus/tools' / name).read_bytes()).hexdigest() for name in ['dependency_freeze.py', 'dependency-freeze-contract.json', 'map_obligations.py', 'map-obligations-contract.json']}}
(S / 'battery-summary.json').write_text(json.dumps(summary, indent=2) + '\n')
print('SUMMARY', json.dumps(summary, sort_keys=True))
raise SystemExit(bool(summary['expected_exit_mismatches'] or summary['stderr_cases'] or summary['census']['other_exit'] or not all(summary['mirror_byte_identity'].values())))
