import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import hashlib
import json
from pathlib import Path
import shlex
import subprocess

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
assert Path.cwd().resolve() == ROOT
SCRATCH = ROOT / '.ufo/waves/round-100/seats/V07-scratch'
FIXTURE = Path('corpus/fixtures/r100-docket-review')
FILES = (
    'entities.json', 'relations.json', 'timeline.json', 'sources.json',
    'contradictions.json', 'README.md', 'claim-excerpt-map.md',
    'fictional-excerpts.md', 'inspiration-note.md', 'source-excerpt.md',
)
TOOLS = (
    Path('corpus/tools/support_check.py'),
    Path('corpus/tools/map_obligations.py'),
    Path('corpus/tools/map-obligations-contract.json'),
)
parser = argparse.ArgumentParser()
parser.add_argument('prefix', choices=('initial', 'rerun'))
parser.add_argument('producer_report', type=Path)
args = parser.parse_args()
report = args.producer_report.resolve(strict=True)
report.relative_to(ROOT / '.ufo/waves/round-100/seats')
assert report.name.startswith('T3') and report.suffix == '.md'
paths = [*(FIXTURE / name for name in FILES), *TOOLS, report.relative_to(ROOT)]


def snapshot():
    result = {}
    for relative in paths:
        path = ROOT / relative
        data = path.read_bytes()
        result[str(relative)] = {
            'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
        }
    return result


def run(tool):
    command = ['python3', f'corpus/tools/{tool}.py', str(FIXTURE)]
    started = datetime.now().astimezone().isoformat(timespec='seconds')
    process = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
    record = {
        'command': shlex.join(command), 'started': started,
        'finished': datetime.now().astimezone().isoformat(timespec='seconds'),
        'exit': process.returncode, 'stdout': process.stdout, 'stderr': process.stderr,
    }
    for stream in ('stdout', 'stderr'):
        output = SCRATCH / f'{args.prefix}-{tool}.{stream}'
        assert output.resolve().is_relative_to(SCRATCH.resolve())
        with output.open('x', encoding='utf-8') as handle:
            handle.write(record[stream])
    return record


before = snapshot()
with ThreadPoolExecutor(max_workers=2) as pool:
    results = list(pool.map(run, ('support_check', 'map_obligations')))
after = snapshot()
record = {
    'cwd': str(ROOT), 'head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
    'before': before, 'runs': results, 'after': after, 'stable': before == after,
}
output = SCRATCH / f'{args.prefix}-verification.json'
assert output.resolve().is_relative_to(SCRATCH.resolve())
with output.open('x', encoding='utf-8') as handle:
    json.dump(record, handle, indent=2)
    handle.write('\n')
for result in results:
    print('$ ' + result['command'])
    print(result['stdout'], end='')
    print('exit=' + str(result['exit']))
    print('stderr_bytes=' + str(len(result['stderr'].encode())))
    if result['stderr']:
        print(result['stderr'], end='')
print('stable_fixture_tools_and_producer_report=' + str(record['stable']))
print('receipt=' + str(output))
raise SystemExit(0 if record['stable'] and all(result['exit'] == 0 for result in results) else 1)
