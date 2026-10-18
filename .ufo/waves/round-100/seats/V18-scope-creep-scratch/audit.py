from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import os
import re
import subprocess

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
PARENT = ROOT.parent
WAVE = ROOT / '.ufo/waves/round-100'
SEATS = WAVE / 'seats'
SELF = 'V18'
assert Path.cwd().resolve() == ROOT
assert Path(__file__).resolve().is_relative_to(SEATS / 'V18-scope-creep-scratch')


def git(*args, cwd=ROOT):
    return subprocess.check_output(['git', *args], cwd=cwd, text=True)


def owner(path):
    if path in {'SKILL.md', 'corpus/tools/README.md', 'corpus/tools/dependency-freeze-contract.json'}:
        return 'T1 production'
    if path in {'corpus/fixtures/r100-docket-review/README.md', 'corpus/fixtures/r100-docket-review/claim-excerpt-map.md'}:
        return 'T3 production'
    if path.startswith('corpus/fixtures/r100-docket-review/'):
        return 'T2 production'
    if path in {'corpus/knowledge/r100-crossing-arc-synthesis.md', 'corpus/knowledge/r100-provenance-semantics-boundary.md', 'corpus/knowledge/r99-gate-blind-spot-table.md'}:
        return 'T4 production'
    if path == '.ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md':
        return 'pre-existing round-98 note'
    if re.fullmatch(r'\.ufo/waves/round-100/seats/[TV]0*\d+-[^/]+\.md', path):
        return 'round-100 seat reports'
    if re.match(r'\.ufo/waves/round-100/seats/[TV]0*\d+-[^/]+/', path):
        return 'round-100 seat scratch'
    if re.match(r'\.ufo/waves/round-100/scratch/[TV]0*\d+[^/]*/', path):
        return 'round-100 seat scratch'
    return 'OUTSIDE DECLARED OWNERSHIP'


now = datetime.now(timezone.utc).isoformat()
print('SNAPSHOT_UTC', now)
print('ROOT', ROOT)
print('HEAD', git('rev-parse', 'HEAD').strip())
print('COMMAND git diff fe1ce46 HEAD --name-status')
print(git('diff', 'fe1ce46', 'HEAD', '--name-status'), end='')
print('COMMAND git diff --cached --name-status')
cached = git('diff', '--cached', '--name-status')
print(cached if cached else '(empty)', end='' if cached else '\n')
print('COMMAND git status --porcelain=v1 -uall')
raw = git('status', '--porcelain=v1', '-uall')
print('RAW_STATUS_SHA256', hashlib.sha256(raw.encode()).hexdigest())
buckets = defaultdict(list)
for line in raw.splitlines():
    path = line[3:]
    buckets[owner(path)].append(line)
for bucket, lines in sorted(buckets.items()):
    print(f'BUCKET {bucket}: {len(lines)} paths')
    if bucket.endswith('scratch'):
        groups = Counter('/'.join(line[3:].split('/')[:6]) if '/seats/' in line else '/'.join(line[3:].split('/')[:6]) for line in lines)
        for group, count in sorted(groups.items()):
            print(f'  {count} paths {group}')
    else:
        for line in lines:
            print(line)
print('TOTAL_STATUS_PATHS', sum(map(len, buckets.values())))
print('OUTSIDE_OWNERSHIP_COUNT', len(buckets['OUTSIDE DECLARED OWNERSHIP']))
print('REPORT_EXCLUSIVITY')
reports = defaultdict(list)
unexpected = []
empty = []
links = []
header_mismatches = []
for path in sorted(SEATS.glob('*.md')):
    match = re.fullmatch(r'([TV])0*(\d+)-.+\.md', path.name)
    if not match:
        unexpected.append(path.name)
        continue
    seat = match[1] + str(int(match[2]))
    reports[seat].append(path.name)
    data = path.read_bytes()
    stat = path.lstat()
    if not data:
        empty.append(path.name)
    if path.is_symlink() or stat.st_nlink != 1:
        links.append(path.name)
    header = next((line for line in data.decode('utf-8', errors='replace').splitlines() if line.startswith('# ')), '')
    header_ids = {m[1] + str(int(m[2])) for m in re.finditer(r'\b([TV])0*(\d{1,2})\b', header)}
    if header_ids and seat not in header_ids:
        header_mismatches.append((path.name, header))
    print(seat, path.name, 'bytes', len(data), 'sha256', hashlib.sha256(data).hexdigest())
print('UNIQUE_REPORT_SEATS', len(reports))
print('OTHER_REPORT_SEATS_SELF_V18_SUBTRACTED', len(set(reports) - {SELF}))
print('PRODUCER_MISSING', sorted({f'T{i}' for i in range(1, 5)} - set(reports)))
print('DUPLICATE_REPORT_PREFIXES', {key: value for key, value in reports.items() if len(value) > 1})
print('UNEXPECTED_REPORT_FILENAMES', unexpected)
print('EMPTY_REPORTS', empty)
print('REPORT_LINK_ANOMALIES', links)
print('REPORT_HEADER_MISMATCHES', header_mismatches)
print('SCRATCH_SIZE_AUDIT logical bytes; flag file >=10MiB or directory >=50MiB')
scratch_dirs = sorted(path for path in SEATS.iterdir() if path.is_dir())
if (WAVE / 'scratch').is_dir():
    scratch_dirs += sorted(path for path in (WAVE / 'scratch').iterdir() if path.is_dir())
all_scratch_files = []
for directory in scratch_dirs:
    files = []
    for base, dirs, names in os.walk(directory, followlinks=False):
        for name in names:
            path = Path(base) / name
            files.append((path.lstat().st_size, path))
    total = sum(size for size, _ in files)
    all_scratch_files.extend(files)
    print(str(directory.relative_to(ROOT)), 'files', len(files), 'bytes', total, 'OVERSIZED' if total >= 50 * 1024 * 1024 else 'within_threshold')
large = [(size, str(path.relative_to(ROOT))) for size, path in all_scratch_files if size >= 10 * 1024 * 1024]
print('SCRATCH_TOTAL_FILES', len(all_scratch_files))
print('SCRATCH_TOTAL_LOGICAL_BYTES', sum(size for size, _ in all_scratch_files))
print('SCRATCH_FILES_GE_10MiB', sorted(large, reverse=True))
print('LARGEST_SCRATCH_FILES', [(size, str(path.relative_to(ROOT))) for size, path in sorted(all_scratch_files, key=lambda row: row[0], reverse=True)[:10]])
print('COMMAND git status --porcelain=v1 -uall [parent repository]')
parent_status = git('status', '--porcelain=v1', '-uall', cwd=PARENT)
print(parent_status if parent_status else '(empty)', end='' if parent_status else '\n')
print('PARENT_STATUS_PATHS', len(parent_status.splitlines()))
print('PARENT_WRONG_CWD_ROUND100_EXISTS', (PARENT / '.ufo/waves/round-100').exists())
print('PARENT_WRONG_CWD_CORPUS_EXISTS', (PARENT / 'corpus').exists())
print('PARENT_WRONG_CWD_SKILL_EXISTS', (PARENT / 'SKILL.md').exists())
start = int(git('show', '-s', '--format=%ct', 'b5fe472').strip())
recent_parent = []
for base, dirs, names in os.walk(PARENT, followlinks=False):
    dirs[:] = sorted(name for name in dirs if name != '.git' and not name.endswith('-shokunin'))
    for name in sorted(names):
        path = Path(base) / name
        stat = path.lstat()
        if stat.st_mtime >= start:
            recent_parent.append((str(path.relative_to(PARENT)), stat.st_size, datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat()))
print('RECENT_PARENT_FILES_OUTSIDE_ALL_LANES_SINCE_DECLARATION', recent_parent)
print('PARENT_SCRATCH_ENTRIES', sorted(path.name for path in (PARENT / '.scratch').iterdir()) if (PARENT / '.scratch').is_dir() else 'absent')
print('AUDIT_COMPLETED_UTC', datetime.now(timezone.utc).isoformat())
