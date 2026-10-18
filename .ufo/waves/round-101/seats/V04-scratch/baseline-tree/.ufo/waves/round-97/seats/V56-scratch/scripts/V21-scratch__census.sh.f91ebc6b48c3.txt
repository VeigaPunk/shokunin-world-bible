#!/bin/bash
# V21 census: run check_bible.py over every corpus/fixtures/*/ dir, repo-relative
cd /home/vgpnk/Projects/shokunin/lore-shokunin
export PYTHONDONTWRITEBYTECODE=1
out="$1"
: > "$out"
for d in corpus/fixtures/*/; do
  d="${d%/}"
  o=$(python3 corpus/fixtures/check_bible.py "$d" 2>&1); rc=$?
  n=$(printf '%s\n' "$o" | grep -c .)
  printf '%s\t%s\t%s\n' "$d" "$rc" "$n" >> "$out"
done
echo "DIRS=$(wc -l < "$out") CLEAN=$(awk -F'\t' '$2==0' "$out" | wc -l) NEG=$(awk -F'\t' '$2==1' "$out" | wc -l) OTHER=$(awk -F'\t' '$2!=0 && $2!=1' "$out" | wc -l) LINES=$(awk -F'\t' '{s+=$3} END{print s}' "$out")"
