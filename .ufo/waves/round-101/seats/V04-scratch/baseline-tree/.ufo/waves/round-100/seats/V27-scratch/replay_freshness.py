from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path
import hashlib
import json
import shlex
import shutil
import subprocess

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
SCRATCH = ROOT / '.ufo/waves/round-100/seats/V27-scratch'
assert Path.cwd() == ROOT
assert SCRATCH.resolve().is_relative_to(ROOT)
ready = json.loads((SCRATCH / 'ready-manifest.json').read_text())
for name in ready['sha256']:
    assert (ROOT / name).is_file(), name
run = SCRATCH / ('replay-' + datetime.now().strftime('%Y%m%dT%H%M%S'))
run.mkdir()
print('EVIDENCE-DIR', run.relative_to(ROOT), flush=True)
contract = json.loads((ROOT / 'corpus/tools/dependency-freeze-contract.json').read_text())
baseline = json.loads(subprocess.check_output(['git', 'show', 'fe1ce46:corpus/tools/dependency-freeze-contract.json'], cwd=ROOT))
files = set(ready['sha256'])
files.update([
    'corpus/tools/dependency_freeze.py', 'corpus/tools/map_obligations.py',
    'corpus/tools/support_check.py', 'corpus/fixtures/check_bible.py',
    'corpus/tools/map-obligations-contract.json', 'corpus/tools/boundary_doc_check.py',
    'corpus/tools/boundary-doc-contract.json', 'corpus/README.md',
    'corpus/fixtures/README.md', 'corpus/knowledge/r91-c9-watch.md',
])
for pin in contract['pins'].values():
    files.update(pin['fixture'] + '/' + name for name in pin['files'])
def snapshot():
    return {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in sorted(files)}
before = snapshot()
(run / 'before-manifest.json').write_text(json.dumps(before, indent=2) + '\n')
print('HEAD', subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(), flush=True)
print('BASELINE', 'fe1ce466e9d7427948c0abe4ecfbf961880b72ff', flush=True)
print('CONTRACT-PINS', len(contract['pins']), sorted(contract['pins']), flush=True)
unchanged = all(contract['pins'].get(name) == pin for name, pin in baseline['pins'].items())
print('OLD-PIN-FIELDS-UNCHANGED', unchanged, flush=True)
print('NEW-PINS', sorted(set(contract['pins']) - set(baseline['pins'])), flush=True)
for name in ['corpus/README.md', 'corpus/fixtures/README.md', 'corpus/knowledge/r91-c9-watch.md']:
    b = subprocess.check_output(['git', 'show', 'fe1ce46:' + name], cwd=ROOT)
    print('BASELINE-BYTE-IDENTITY', name, (ROOT / name).read_bytes() == b, flush=True)
for name in ['corpus/knowledge/r100-crossing-arc-synthesis.md', 'corpus/knowledge/r100-provenance-semantics-boundary.md']:
    text = (ROOT / name).read_text()
    print('KNOWLEDGE-METADATA', name, {label: text.startswith(label) if label == 'source:' else ('\n' + label) in text for label in ['source:', 'verified-at:', 'recheck:']}, flush=True)
fixture = ROOT / 'corpus/fixtures/r100-docket-review'
print('R100-COUNTS', {name: len(json.loads((fixture / (name + '.json')).read_text())) for name in ['entities', 'relations', 'timeline', 'sources', 'contradictions']}, flush=True)
print('FIXTURE-CENSUS', sum(p.is_dir() and (p / 'entities.json').is_file() for p in (ROOT / 'corpus/fixtures').iterdir()), flush=True)
mirror = run / 'selftest-mirror'
(mirror / 'corpus/tools').mkdir(parents=True)
(mirror / 'corpus/fixtures').mkdir(parents=True)
for name in ['dependency_freeze.py', 'dependency-freeze-contract.json', 'map_obligations.py', 'map-obligations-contract.json']:
    shutil.copy2(ROOT / 'corpus/tools' / name, mirror / 'corpus/tools' / name)
shutil.copytree(ROOT / 'corpus/fixtures/r95-crossing-aftermath', mirror / 'corpus/fixtures/r95-crossing-aftermath')
commands = []
for name in contract['pins']:
    commands.append(('freeze-' + name, ['python3', 'corpus/tools/dependency_freeze.py', contract['pins'][name]['fixture']]))
commands += [
    ('r100-bible', ['python3', 'corpus/fixtures/check_bible.py', 'corpus/fixtures/r100-docket-review']),
    ('r100-map', ['python3', 'corpus/tools/map_obligations.py', 'corpus/fixtures/r100-docket-review']),
    ('r100-support', ['python3', 'corpus/tools/support_check.py', 'corpus/fixtures/r100-docket-review']),
    ('boundary', ['python3', 'corpus/tools/boundary_doc_check.py']),
    ('c9-delivered', ['python3', 'corpus/tools/discriminate_check.py']),
    ('c9-control', ['python3', 'corpus/tools/discriminate_check.py', '--checker', 'e97613c']),
    ('r10-replay', ['python3', '.ufo/waves/round-93/deepseek/F14-postrepair-check.py']),
    ('freeze-selftest', ['python3', str((mirror / 'corpus/tools/dependency_freeze.py').relative_to(ROOT)), '--self-test']),
    ('map-selftest', ['python3', str((mirror / 'corpus/tools/map_obligations.py').relative_to(ROOT)), '--self-test']),
]
def execute(item):
    label, command = item
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, timeout=90)
    record = {'label': label, 'command': command, 'exit': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr}
    (run / (label + '.stdout')).write_text(result.stdout)
    (run / (label + '.stderr')).write_text(result.stderr)
    return record
with ThreadPoolExecutor(max_workers=8) as pool:
    results = list(pool.map(execute, commands))
for result in results:
    print('$ ' + shlex.join(result['command']), flush=True)
    print(result['stdout'].rstrip(), flush=True)
    if result['stderr']:
        print('STDERR ' + result['stderr'].rstrip(), flush=True)
    print('exit=' + str(result['exit']), flush=True)
(run / 'results.json').write_text(json.dumps(results, indent=2) + '\n')
after = snapshot()
(run / 'after-manifest.json').write_text(json.dumps(after, indent=2) + '\n')
changes = [name for name in before if before[name] != after[name]]
print('LIVE-INPUT-DRIFT', changes, flush=True)
print('LIVE-INPUTS-HASHED', len(before), flush=True)
print('RESULTS', {r['label']: r['exit'] for r in results}, flush=True)
expected = {label: (2 if label == 'c9-control' else 0) for label, _ in commands}
assert unchanged
assert all(r['exit'] == expected[r['label']] and not r['stderr'] for r in results)
assert not changes
print('V27-REPLAY-PASS', flush=True)
