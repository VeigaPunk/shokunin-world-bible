import hashlib
import json
import pathlib
import subprocess
import sys
import tarfile
import tempfile

REF = sys.argv[1] if len(sys.argv) > 1 else 'f3e09f9'
ROOT = sys.argv[2] if len(sys.argv) > 2 else 'corpus/fixtures'
EXPECTED_DIRS = int(sys.argv[3]) if len(sys.argv) > 3 else 171
ALLOW_NEW_DIRS = set(sys.argv[4].split(',')) if len(sys.argv) > 4 and sys.argv[4] else set()
ALLOW_MODIFIED = set(sys.argv[5].split(',')) if len(sys.argv) > 5 and sys.argv[5] else set()
OUT = sys.argv[6] if len(sys.argv) > 6 else None

repo = pathlib.Path.cwd()


def sha256(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1 << 16), b''):
            h.update(chunk)
    return h.hexdigest()


def tree_snapshot(base):
    base = pathlib.Path(base)
    files = {}
    dirs = set()
    for p in sorted(base.rglob('*')):
        rel = p.relative_to(base).as_posix()
        if p.is_symlink():
            files[rel] = 'symlink:' + str(p.readlink())
        elif p.is_dir():
            dirs.add(rel)
        elif p.is_file():
            files[rel] = sha256(p)
    top_dirs = {d.split('/', 1)[0] for d in dirs}
    return files, dirs, top_dirs


tmp = pathlib.Path(tempfile.mkdtemp(prefix='v41-archive-', dir=str(repo / '.ufo/waves/round-97/seats/V41-scratch')))
tar_path = tmp / 'ref.tar'
with tar_path.open('wb') as fh:
    r = subprocess.run(['git', 'archive', '--format=tar', REF, ROOT], stdout=fh, stderr=subprocess.PIPE)
    if r.returncode != 0:
        print('git archive failed:', r.stderr.decode())
        raise SystemExit(2)
extract = tmp / 'extract'
extract.mkdir()
with tarfile.open(tar_path) as tf:
    tf.extractall(extract)

base = extract / ROOT
work = repo / ROOT
base_files, base_dirs, base_top = tree_snapshot(base)
work_files, work_dirs, work_top = tree_snapshot(work)

inherited = {k: v for k, v in base_files.items() if k in work_files and work_files[k] == v}
modified = sorted(k for k in base_files if k in work_files and work_files[k] != base_files[k])
deleted = sorted(k for k in base_files if k not in work_files)
new = sorted(k for k in work_files if k not in base_files)
new_top_dirs = sorted(work_top - base_top)
gone_top_dirs = sorted(base_top - work_top)
unexpected_new_dirs = sorted(d for d in new_top_dirs if d not in ALLOW_NEW_DIRS)
reasons = []
if len(work_top) != EXPECTED_DIRS:
    reasons.append(f'top_dirs {len(work_top)} != expected {EXPECTED_DIRS}')
if unexpected_new_dirs:
    reasons.append(f'unexpected new dirs {unexpected_new_dirs}')
if gone_top_dirs:
    reasons.append(f'gone dirs {gone_top_dirs}')
verdict = 'PASS' if not reasons else 'FAIL'

receipt = {
    'ref': REF,
    'root': ROOT,
    'baseline_top_dirs': len(base_top),
    'work_top_dirs': len(work_top),
    'baseline_all_dirs': len(base_dirs),
    'work_all_dirs': len(work_dirs),
    'baseline_files': len(base_files),
    'work_files': len(work_files),
    'inherited_files': len(inherited),
    'modified_inherited': modified,
    'deleted_inherited': deleted,
    'new_top_dirs': new_top_dirs,
    'gone_top_dirs': gone_top_dirs,
    'new_files_count': len(new),
    'new_files': new,
    'unexpected_new_dirs': unexpected_new_dirs,
    'verdict': verdict,
    'reasons': reasons,
}
print(json.dumps(receipt, indent=2))
if OUT:
    pathlib.Path(OUT).write_text(json.dumps(receipt, indent=2) + '\n')
print(f"CENSUS {verdict}: dirs={len(work_top)} files={len(work_files)} modified={len(modified)} deleted={len(deleted)} new={len(new)}")
if verdict != 'PASS':
    raise SystemExit(1)
