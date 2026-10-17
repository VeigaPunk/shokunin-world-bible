#!/bin/bash
# V28 tree audit: blob-level change set vs baseline f3e09f9 (tracked) + untracked audit
L=/home/vgpnk/Projects/shokunin/lore-shokunin
cd "$L" || exit 1
echo "== git diff --name-status f3e09f9 =="
git diff --name-status f3e09f9
echo "== untracked outside .ufo/waves/round-97/ =="
git status --porcelain -uall | grep '^??' | grep -v '^?? .ufo/waves/round-97/'
echo "== blob-level corpus tree compare =="
python3 - <<'PY'
import subprocess, pathlib
L = pathlib.Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
base = {}
out = subprocess.run(['git','-C',str(L),'ls-tree','-r','--name-only','f3e09f9','corpus'],capture_output=True,text=True).stdout.split()
for p in out:
    blob = subprocess.run(['git','-C',str(L),'rev-parse',f'f3e09f9:{p}'],capture_output=True,text=True).stdout.strip()
    base[p]=blob
now = {}
for f in sorted((L/'corpus').rglob('*')):
    if f.is_file() and '__pycache__' not in str(f):
        p = str(f.relative_to(L))
        blob = subprocess.run(['git','-C',str(L),'hash-object',str(f)],capture_output=True,text=True).stdout.strip()
        now[p]=blob
changed = sorted(p for p in base if p in now and base[p]!=now[p])
added   = sorted(p for p in now if p not in base)
missing = sorted(p for p in base if p not in now)
print(f"base corpus files: {len(base)}")
print("CHANGED:", changed)
print(f"ADDED count: {len(added)}")
for p in added: print("  A", p)
print("MISSING:", missing)
PY
echo "== symlink / non-regular audit in new corpus paths =="
find corpus/fixtures/r97-crossing-acknowledgment corpus/knowledge/r97-acknowledgment-scope-note.md -not -type f -o -type l 2>/dev/null
echo "== other pinned docs diff vs baseline =="
git diff --stat f3e09f9 -- PROVINCE.md SHONEN.md SKILL.md README.md l0-questions.md SCORECARD.md | cat
echo "== wave-dir containment (lane-internal untracked outside round-97) =="
git status --porcelain -uall | grep '^??' | grep -v '^?? .ufo/waves/round-97/' | grep -c '^??' || true
