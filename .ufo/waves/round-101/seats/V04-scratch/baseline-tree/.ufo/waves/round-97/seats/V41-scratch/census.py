import hashlib
import json
import pathlib
import subprocess
import sys

root = pathlib.Path(sys.argv[1]).resolve()
out = pathlib.Path(sys.argv[2]).resolve()
fixtures = root / 'corpus/fixtures'
names = sorted(p.name for p in fixtures.iterdir() if p.is_dir())
rows = []
exit_counts = {}
violations = 0
stderr = []
unexpected = []
for name in names:
    rel = f'corpus/fixtures/{name}'
    r = subprocess.run(
        ['python3', '-I', 'corpus/fixtures/check_bible.py', rel],
        cwd=root,
        capture_output=True,
    )
    v = sum(line.startswith(b'VIOLATION:') for line in r.stdout.splitlines())
    lines_nonempty = sum(1 for line in r.stdout.splitlines() if line.strip())
    rows.append({
        'name': name,
        'exit': r.returncode,
        'violations': v,
        'lines_nonempty': lines_nonempty,
        'stderr': bool(r.stderr),
        'stdout_sha256': hashlib.sha256(r.stdout).hexdigest(),
    })
    exit_counts[r.returncode] = exit_counts.get(r.returncode, 0) + 1
    violations += v
    if r.stderr:
        stderr.append(rel)
    if r.returncode not in (0, 1):
        unexpected.append((rel, r.returncode))
summary = {
    'fixture_dirs': len(names),
    'exit_counts': dict(sorted(exit_counts.items())),
    'violation_lines': violations,
    'stderr_nonempty_count': len(stderr),
    'unexpected_exit_count': len(unexpected),
}
with out.open('w') as f:
    for row in rows:
        f.write(json.dumps(row) + '\n')
    f.write(json.dumps({'summary': summary}) + '\n')
print(json.dumps(summary))
if unexpected or stderr:
    raise SystemExit(1)
