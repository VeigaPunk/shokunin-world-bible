from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import json
import subprocess

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
SCRATCH = ROOT / '.ufo/waves/round-100/seats/V27-scratch'
assert Path.cwd() == ROOT
assert SCRATCH.resolve().is_relative_to(ROOT)
fixtures = sorted(p for p in (ROOT / 'corpus/fixtures').iterdir() if p.is_dir() and not p.name.startswith('.'))
def run(path):
    command = ['python3', 'corpus/fixtures/check_bible.py', str(path.relative_to(ROOT))]
    p = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    return {'fixture': path.name, 'command': command, 'exit': p.returncode, 'stdout': p.stdout, 'stderr': p.stderr}
with ThreadPoolExecutor(max_workers=8) as pool:
    results = list(pool.map(run, fixtures))
summary = {
    'fixture_dirs': len(results),
    'clean_exit0': sum(r['exit'] == 0 for r in results),
    'negative_exit1': sum(r['exit'] == 1 for r in results),
    'violation_lines': sum(sum(s.startswith('VIOLATION:') for s in r['stdout'].splitlines()) for r in results),
    'non01': [r['fixture'] for r in results if r['exit'] not in [0, 1]],
    'nonempty_stderr': [r['fixture'] for r in results if r['stderr']],
}
(SCRATCH / 'census.json').write_text(json.dumps({'summary': summary, 'results': results}, indent=2) + '\n')
print(json.dumps(summary, sort_keys=True))
print('R100', json.dumps(next(r for r in results if r['fixture'] == 'r100-docket-review'), sort_keys=True))
