#!/bin/sh
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 1
BASE=9a3d648
python3 - <<'PY'
import subprocess, os
BASE='9a3d648'
def sh(*a): return subprocess.run(a, capture_output=True, text=True).stdout
tracked = [l for l in sh('git','ls-tree','-r','--name-only',BASE).splitlines() if not l.startswith('.ufo/')]
changed=[]; missing=[]
for p in tracked:
    if not os.path.isfile(p): missing.append(p); continue
    a=sh('git','hash-object',p).strip()
    b=sh('git','rev-parse',f'{BASE}:{p}').strip()
    if a!=b: changed.append(p)
print('tracked-non-ufo base files:', len(tracked))
print('CHANGED:'); [print('  ',p) for p in changed]
print('MISSING:'); [print('  ',p) for p in missing]
PY
