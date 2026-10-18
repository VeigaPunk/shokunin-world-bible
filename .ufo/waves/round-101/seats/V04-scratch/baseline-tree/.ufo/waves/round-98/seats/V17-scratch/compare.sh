#!/bin/sh
# V17 final comparison harness. Run from lane root after producers finish.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 1
S=.ufo/waves/round-98/seats/V17-scratch
echo "== HEAD =="; git rev-parse HEAD
echo "== git diff --name-status 9a3d648 =="
git diff --name-status 9a3d648
echo "== deletions/renames count =="
git diff --name-status --diff-filter=DR 9a3d648 | wc -l
echo "== untracked (excluding seat scratch/reports) =="
git ls-files --others --exclude-standard | grep -v 'round-98/seats'
echo "== fixture dirs =="; find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l
echo "== fixture files =="; find corpus/fixtures -type f | wc -l
echo "== dirs delta vs base =="
ls -d corpus/fixtures/*/ | sed 's|.*/\([^/]*\)/$|\1|' | sort > $S/dirs-now.txt
diff $S/dirs-base.txt $S/dirs-now.txt && echo "(dirs identical to baseline)"
echo "== files delta vs base =="
find corpus/fixtures -type f | sort > $S/files-now.txt
diff $S/files-base.txt $S/files-now.txt && echo "(files identical to baseline)"
echo "== corpus diff -rq vs archive =="
diff -rq $S/archive/corpus corpus 2>&1 | grep -v '__pycache__'
