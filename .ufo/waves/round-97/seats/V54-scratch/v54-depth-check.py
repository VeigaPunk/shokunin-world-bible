#!/usr/bin/env python3
"""V54 independent depth checks for round 97 (r97-crossing-acknowledgment)."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
R96 = ROOT / 'corpus/fixtures/r96-crossing-response'
R97 = ROOT / 'corpus/fixtures/r97-crossing-acknowledgment'
BASE = ROOT / '.ufo/waves/round-97/seats/V54-scratch/baseline/corpus/fixtures/r96-crossing-response'


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=str(ROOT))
    return r.returncode, r.stdout + r.stderr


print('== 0. existence ==')
print('r97 dir:', R97.is_dir(), 'r96 dir:', R96.is_dir(), 'baseline r96 dir:', BASE.is_dir())
if not R97.is_dir():
    sys.exit('r97 fixture absent')
print('r97 files:', sorted(p.name for p in R97.iterdir()))

print('\n== 1. preservation: expected byte-identical copies of POST-REPAIR r96 ==')
for name in ['entities.json', 'relations.json', 'contradictions.json',
             'inspiration-note.md', 'source-excerpt.md']:
    a, b = R96 / name, R97 / name
    if not b.exists():
        print(f'  MISSING r97/{name}')
        continue
    same = a.read_bytes() == b.read_bytes()
    print(f'  {name}: byte-identical={same} r96={sha(a)[:12]} r97={sha(b)[:12]}')

print('\n== 2. timeline: inherited 5 parsed-identical + 1 new ==')
t96 = json.loads((R96 / 'timeline.json').read_text())
t97 = json.loads((R97 / 'timeline.json').read_text())
print(f'  len r96={len(t96)} len r97={len(t97)}')
print(f'  first {len(t96)} parsed-equal: {t97[:len(t96)] == t96}')
for e in t97[len(t96):]:
    print('  new event:', json.dumps(e, ensure_ascii=False))

print('\n== 3. sources: inherited 5 parsed-identical + 1 new ==')
s96 = json.loads((R96 / 'sources.json').read_text())
s97 = json.loads((R97 / 'sources.json').read_text())
print(f'  len r96={len(s96)} len r97={len(s97)}')
print(f'  first {len(s96)} parsed-equal: {s97[:len(s96)] == s96}')
for e in s97[len(s96):]:
    print('  new source:', json.dumps(e, ensure_ascii=False))

print('\n== 4. entities/relations/contradictions counts ==')
for name in ['entities.json', 'relations.json', 'contradictions.json']:
    d96 = json.loads((R96 / name).read_text())
    d97 = json.loads((R97 / name).read_text())
    print(f'  {name}: r96 len={len(d96)} r97 len={len(d97)} parsed-equal={d96 == d97}')

print('\n== 5. fictional-excerpts.md: r96 byte-prefix + appended section ==')
f96 = (R96 / 'fictional-excerpts.md').read_bytes()
f97 = (R97 / 'fictional-excerpts.md').read_bytes()
print(f'  r96 is byte-prefix of r97: {f97.startswith(f96)}')
if f97.startswith(f96):
    print('  appended bytes:')
    print(f97[len(f96):].decode('utf-8'))

print('\n== 6. tool runs on r97 ==')
for label, cmd in [
    ('check_bible', ['python3', 'corpus/fixtures/check_bible.py', str(R97)]),
    ('support_check', ['python3', 'corpus/tools/support_check.py', str(R97)]),
    ('map_obligations', ['python3', 'corpus/tools/map_obligations.py', str(R97)]),
]:
    rc, out = run(cmd)
    print(f'  --- {label} exit={rc} ---')
    print('\n'.join('  ' + l for l in out.splitlines()))

print('\n== 7. repair half: r96 map post-repair ==')
import re
mp = R96 / 'claim-excerpt-map.md'
lines = mp.read_text().split('\n')
blines = (BASE / 'claim-excerpt-map.md').read_text().split('\n')


def cells(l):
    s = l.strip()
    if s.startswith('|'):
        s = s[1:]
    if s.endswith('|'):
        s = s[:-1]
    return [c.strip() for c in s.split('|')]


for i, l in enumerate(lines, 1):
    if re.match(r'^\|[\s:|-]+\|$', l.strip()):
        print(f'  delim line {i}: {len(cells(l))} cells :: {l.strip()}')
print('  lines containing "new relation":', [i for i, l in enumerate(lines, 1) if 'new relation' in l])
print('  lines containing "new event":', [i for i, l in enumerate(lines, 1) if 'new event' in l])
import difflib
d = list(difflib.unified_diff(blines, lines, 'baseline', 'post-repair', lineterm='', n=0))
print('  --- diff baseline -> post-repair (n=0) ---')
print('\n'.join('  ' + l for l in d))
# data rows (tables) byte compare, excluding delimiter lines
def table_rows(ls):
    out = []
    for i, l in enumerate(ls, 1):
        s = l.strip()
        if s.startswith('|') and not re.match(r'^\|[\s:|-]+\|$', s):
            out.append((i, l))
    return out
tr_b, tr_p = table_rows(blines), table_rows(lines)
print(f'  table non-delimiter rows: baseline={len(tr_b)} post={len(tr_p)}')
same = sum(1 for (i, a), (j, b) in zip(tr_b, tr_p) if a == b)
print(f'  identical row bytes (zip): {same}/{min(len(tr_b), len(tr_p))}')
for (i, a), (j, b) in zip(tr_b, tr_p):
    if a != b:
        print(f'    row differs baseline:{i} post:{j}\n      base: {a[:120]}\n      post: {b[:120]}')

print('\n== 8. r96 receipts: baseline copy vs post-repair dir ==')
for label, cmd_base, cmd_now in [
    ('support_check', ['python3', 'corpus/tools/support_check.py', str(BASE)],
     ['python3', 'corpus/tools/support_check.py', str(R96)]),
    ('map_obligations', ['python3', 'corpus/tools/map_obligations.py', str(BASE)],
     ['python3', 'corpus/tools/map_obligations.py', str(R96)]),
]:
    rc1, o1 = run(cmd_base)
    rc2, o2 = run(cmd_now)
    print(f'  {label}: baseline exit={rc1} now exit={rc2} stdout-identical={o1 == o2}')
    if o1 != o2:
        print('   baseline:', o1[-500:])
        print('   now     :', o2[-500:])

print('\n== 9. census ==')
n_fs = len([p for p in (ROOT / 'corpus/fixtures').iterdir() if p.is_dir()])
r = subprocess.run(['git', 'ls-tree', '-d', '--name-only', 'f3e09f9:corpus/fixtures'],
                   capture_output=True, text=True, cwd=str(ROOT))
n_base = len([l for l in r.stdout.splitlines() if l.strip()])
print(f'  fixture dirs: baseline f3e09f9={n_base} filesystem now={n_fs}')
n_files_base = subprocess.run(['git', 'ls-tree', '-r', '--name-only', 'f3e09f9:corpus/fixtures'],
                              capture_output=True, text=True, cwd=str(ROOT)).stdout
n_files_fs = [str(p) for p in (ROOT / 'corpus/fixtures').rglob('*') if p.is_file()]
print(f'  fixture files: baseline={len(n_files_base.splitlines())} fs-now={len(n_files_fs)}')
