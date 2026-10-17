#!/bin/bash
# V52: byte-compare every tracked r88-r95 fixture file against dcb2d92
cd /home/vgpnk/Projects/shokunin/lore-shokunin
BASE=dcb2d92
git ls-tree -r $BASE --name-only corpus/fixtures/ | grep -E 'corpus/fixtures/r(88|89|90|91|93|94|95)-' > .ufo/waves/round-96/seats/V52-scratch/base_list.txt
n=0; bad=0
while read -r f; do
  n=$((n+1))
  if [ ! -e "$f" ]; then echo "MISSING $f"; bad=$((bad+1)); continue; fi
  a=$(git rev-parse "$BASE:$f"); b=$(git hash-object "$f")
  if [ "$a" != "$b" ]; then echo "DIFF $f baseline=$a worktree=$b"; bad=$((bad+1)); fi
done < .ufo/waves/round-96/seats/V52-scratch/base_list.txt
echo "CHECKED=$n DIFFERING=$bad"
