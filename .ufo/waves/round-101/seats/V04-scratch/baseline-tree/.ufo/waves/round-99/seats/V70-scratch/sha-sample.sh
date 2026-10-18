#!/bin/bash
# V70: SHA-256 comparison of a deterministic 10% inherited-file sample
# against baseline commit 4265df5. Selection: LC_ALL=C sorted git ls-tree
# paths under corpus/fixtures, keep 1-based lines where NR % 10 == 0.
set -u
R=/home/vgpnk/Projects/shokunin/lore-shokunin
SCR=$R/.ufo/waves/round-99/seats/V70-scratch
cd "$R" || exit 9
export LC_ALL=C
BASE=4265df5
git ls-tree -r --name-only "$BASE" -- corpus/fixtures | sort > "$SCR/inherited-files.txt"
total=$(wc -l < "$SCR/inherited-files.txt")
awk 'NR % 10 == 0' "$SCR/inherited-files.txt" > "$SCR/sample-10pct.txt"
sample=$(wc -l < "$SCR/sample-10pct.txt")
echo "INHERITED_FILES=$total SAMPLE_10PCT=$sample"
mismatch=0
missing=0
ok=0
: > "$SCR/sha-sample.tsv"
while IFS= read -r f; do
  if [ ! -f "$f" ]; then
    missing=$((missing+1))
    printf 'MISSING\t%s\n' "$f" >> "$SCR/sha-sample.tsv"
    continue
  fi
  base_sha=$(git show "$BASE:$f" | sha256sum | awk '{print $1}')
  work_sha=$(sha256sum "$f" | awk '{print $1}')
  if [ "$base_sha" = "$work_sha" ]; then
    ok=$((ok+1))
    printf 'MATCH\t%s\t%s\n' "$work_sha" "$f" >> "$SCR/sha-sample.tsv"
  else
    mismatch=$((mismatch+1))
    printf 'MISMATCH\tbase=%s\twork=%s\t%s\n' "$base_sha" "$work_sha" "$f" >> "$SCR/sha-sample.tsv"
  fi
done < "$SCR/sample-10pct.txt"
echo "SAMPLE_OK=$ok SAMPLE_MISMATCH=$mismatch SAMPLE_MISSING=$missing"
