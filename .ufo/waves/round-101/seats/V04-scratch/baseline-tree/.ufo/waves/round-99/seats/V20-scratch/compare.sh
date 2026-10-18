#!/bin/bash
# V20 inherited-path comparison vs 4265df5. Read-only on the corpus.
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
SCRATCH=$LANE/.ufo/waves/round-99/seats/V20-scratch
cd "$LANE" || exit 1
BASE=4265df5

echo "=== HEAD ==="
git rev-parse HEAD
git diff --stat "$BASE" HEAD

echo "=== git diff --name-status $BASE ==="
git diff --name-status "$BASE"

echo "=== deletions/renames ==="
git diff --name-status --diff-filter=DR "$BASE" | wc -l
git diff --name-status --diff-filter=DR "$BASE"

echo "=== untracked excluding .ufo ==="
git ls-files --others --exclude-standard | grep -v '^\.ufo/' || true

echo "=== numstat corpus + LOG + SCORECARD + SKILL ==="
git diff --numstat "$BASE" -- corpus/ LOG.md SCORECARD.md SKILL.md

echo "=== fixture dir counts ==="
echo -n "now dirs: "; find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l
echo -n "now files: "; find corpus/fixtures -type f | wc -l
echo -n "base dirs: "; git ls-tree -d --name-only "$BASE":corpus/fixtures | wc -l
echo -n "base files: "; git ls-tree -r --name-only "$BASE" corpus/fixtures | wc -l

git ls-tree -d --name-only "$BASE":corpus/fixtures | sort > "$SCRATCH/dirs-base.txt"
find corpus/fixtures -mindepth 1 -maxdepth 1 -type d -printf '%f\n' | sort > "$SCRATCH/dirs-now.txt"
echo "=== dir diff ==="
diff -u "$SCRATCH/dirs-base.txt" "$SCRATCH/dirs-now.txt" || true

git ls-tree -r --name-only "$BASE" corpus/fixtures | sort > "$SCRATCH/files-base.txt"
find corpus/fixtures -type f -printf '%P\n' | sed 's|^|corpus/fixtures/|' | sort > "$SCRATCH/files-now.txt"
echo "=== file diff (fixtures) ==="
diff -u "$SCRATCH/files-base.txt" "$SCRATCH/files-now.txt" || true

echo "=== diff -rq archive vs worktree corpus (no pycache) ==="
diff -rq "$SCRATCH/archive/corpus" corpus | grep -v '__pycache__' || true

echo "=== SKILL.md cmp ==="
if cmp -s "$SCRATCH/archive/SKILL.md" SKILL.md; then
  echo "SKILL.md identical to 4265df5"
else
  echo "SKILL.md DIFFERS from 4265df5"
  diff -u "$SCRATCH/archive/SKILL.md" SKILL.md | head -80
fi

echo "=== changed path set ==="
{
  git diff --name-only "$BASE"
  git ls-files --others --exclude-standard | grep -v '^\.ufo/' || true
} | sort -u | tee "$SCRATCH/changed_paths.txt"
echo "changed_count=$(wc -l < "$SCRATCH/changed_paths.txt")"
