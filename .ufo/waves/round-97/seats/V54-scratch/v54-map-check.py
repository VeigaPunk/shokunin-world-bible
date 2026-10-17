#!/usr/bin/env python3
"""V54 checks on the r97 map once R5 lands: declarations, J17 row, inherited-row equality."""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
R96 = ROOT / 'corpus/fixtures/r96-crossing-response'
R97 = ROOT / 'corpus/fixtures/r97-crossing-acknowledgment'


def cells(l):
    s = l.strip()
    if s.startswith('|'):
        s = s[1:]
    if s.endswith('|'):
        s = s[:-1]
    return [c.strip() for c in s.split('|')]


def rows(path):
    out = []
    for i, l in enumerate(Path(path).read_text().split('\n'), 1):
        s = l.strip()
        if s.startswith('|') and not re.match(r'^\|[\s:|-]+\|$', s):
            out.append((i, cells(l)))
    return out


m97 = R97 / 'claim-excerpt-map.md'
m96 = R96 / 'claim-excerpt-map.md'
print('r97 map sha:', subprocess.run(['sha256sum', str(m97)], capture_output=True, text=True).stdout.strip())
print('r97 map == r96 map:', m97.read_bytes() == m96.read_bytes())

text = m97.read_text()
print('\n-- declaration / headings --')
for l in text.split('\n'):
    if 'Expected inventory' in l or l.startswith('## ') or 'obligations in this continuation' in l:
        print(' ', l)

print('\n-- delimiter rows --')
for i, l in enumerate(text.split('\n'), 1):
    if re.match(r'^\|[\s:|-]+\|$', l.strip()):
        print(f'  line {i}: {len(cells(l))} cells')

r97 = rows(m97)
r96 = rows(m96)
print(f'\nrows r96={len(r96)} r97={len(r97)}')
# compare by ID column (first cell)
d96 = {c[0]: (i, c) for i, c in r96}
for i, c in r97:
    key = c[0]
    if key in d96:
        j, b = d96[key]
        if c != b:
            diffs = [(k, x, y) for k, (x, y) in enumerate(zip(b, c)) if x != y]
            print(f'  {key}: differs from r96 row (line {j}) in {len(diffs)} cell(s):')
            for k, x, y in diffs:
                print(f'    col{k}: r96={x[:80]!r}')
                print(f'          r97={y[:80]!r}')
    else:
        print(f'  {key}: NEW row at line {i}:')
        for k, x in enumerate(c):
            print(f'    col{k}: {x[:120]!r}')
print('  IDs only in r96:', sorted(set(d96) - {c[0] for _, c in r97}))

print('\n-- new event/map alignment --')
tl = json.loads((R97 / 'timeline.json').read_text())
for k, e in enumerate(tl):
    ptr = f'timeline.json#/{k}'
    hit = [i for i, c in r97 if ptr in c[1]]
    print(f'  {ptr} ({e["id"]}) -> map line(s) {hit}')

print('\n-- tool runs --')
for label, cmd in [
    ('map_obligations', ['python3', 'corpus/tools/map_obligations.py', str(R97)]),
    ('support_check', ['python3', 'corpus/tools/support_check.py', str(R97)]),
    ('check_bible', ['python3', 'corpus/fixtures/check_bible.py', str(R97)]),
]:
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=str(ROOT))
    print(f'  {label}: exit={r.returncode}')
    print('   ' + '\n   '.join(l for l in (r.stdout + r.stderr).splitlines() if l.startswith(('OBLIGATIONS', 'INVENTORY', 'FINDING', 'RESULT', 'RECEIPT', 'SOURCE-SUPPORT', 'CLEAN', 'VIOLATION'))))
