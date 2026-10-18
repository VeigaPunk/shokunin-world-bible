#!/bin/bash
# V10 c3-inherited-equality evidence capture (run from lane repo root)
cd /home/vgpnk/Projects/shokunin/lore-shokunin
echo "### 0. baseline check"
git log --oneline -1 9a3d648
echo "### 1. r97 dir byte-untouched vs 9a3d648"
git diff --stat 9a3d648 -- corpus/fixtures/r97-crossing-acknowledgment/ && echo "(empty diff above = untouched)"
echo "### 2. parsed-value parity r98 vs 9a3d648 r97"
python3 .ufo/waves/round-98/seats/V10-scratch/parity.py
echo "### 3. byte-prefix / insertion exactness"
python3 - <<'PY'
R97="corpus/fixtures/r97-crossing-acknowledgment"; R98="corpus/fixtures/r98-clerk-filing"
for f in ["entities.json","sources.json","timeline.json"]:
    a=open(f"{R97}/{f}","rb").read(); b=open(f"{R98}/{f}","rb").read()
    L=len(a)-3
    div=next((i for i in range(min(len(a),len(b))) if a[i]!=b[i]), None)
    print(f"{f}: LCP={div} == len(r97)-3 ({L}) -> {div==L}; prefix_exact={b[:L]==a[:L]}; r98[L:L+2]={b[L:L+2]!r}; r98_tail={b[-3:]!r}")
a=open(f"{R97}/fictional-excerpts.md","rb").read(); b=open(f"{R98}/fictional-excerpts.md","rb").read()
print("fictional-excerpts.md: strict byte-extension =", b.startswith(a), "; appended =", len(b)-len(a), "bytes")
PY
echo "### 4. per-file byte copies vs 9a3d648 r97 counterpart"
for f in corpus/fixtures/r98-clerk-filing/*; do b=$(basename $f); if cmp -s "$f" <(git show 9a3d648:corpus/fixtures/r97-crossing-acknowledgment/$b); then echo "IDENTICAL: $b"; else echo "differs: $b"; fi; done
echo "### 5. receipts"
python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing 2>&1 | tail -1
python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing 2>&1 | tail -2
python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing 2>&1 | tail -2
echo "### 6. map row diff (inherited 17 + new 3)"
python3 .ufo/waves/round-98/seats/V10-scratch/mapdiff.py
echo "### 7. census"
echo "baseline dirs: $(git ls-tree -d --name-only 9a3d648 corpus/fixtures/ | wc -l); worktree dirs: $(ls -d corpus/fixtures/*/ | wc -l)"
comm -13 <(git ls-tree -d --name-only 9a3d648 corpus/fixtures/ | sort) <(ls -d corpus/fixtures/*/ | sed 's:/$::' | sort)
echo "### 8. r95 repair (one line, receipts unchanged)"
git diff --stat 9a3d648 -- corpus/fixtures/r95-crossing-aftermath/
python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath 2>&1 | tail -2
python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath 2>&1 | tail -1
python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath 2>&1 | tail -2
