#!/bin/bash
# V44 inherited-tools comparator: baseline 9a3d648 vs working tree
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
BASE=.ufo/waves/round-98/seats/V44-scratch/baseline-hashes.txt
OUT=.ufo/waves/round-98/seats/V44-scratch/check-out.txt
: > "$OUT"
while read -r hash path; do
  if [ ! -f "$path" ]; then echo "MISSING $path" >> "$OUT"; continue; fi
  cur=$(git hash-object "$path")
  if [ "$cur" != "$hash" ]; then echo "MODIFIED $path base=$hash cur=$cur" >> "$OUT"; fi
done < "$BASE"
# new files (tracked+untracked, excluding ignore) under corpus/fixtures and corpus/tools
git ls-files -co --exclude-standard corpus/fixtures corpus/tools | sort > .ufo/waves/round-98/seats/V44-scratch/current-paths.txt
awk '{print $2}' "$BASE" | sort > .ufo/waves/round-98/seats/V44-scratch/baseline-paths.txt
comm -13 .ufo/waves/round-98/seats/V44-scratch/baseline-paths.txt .ufo/waves/round-98/seats/V44-scratch/current-paths.txt | sed 's/^/NEW /' >> "$OUT"
echo "--- summary ---" >> "$OUT"
echo "baseline_paths=$(wc -l < .ufo/waves/round-98/seats/V44-scratch/baseline-paths.txt) current_paths=$(wc -l < .ufo/waves/round-98/seats/V44-scratch/current-paths.txt)" >> "$OUT"
echo "changed=$(grep -cE '^(MODIFIED|MISSING)' "$OUT") new=$(grep -c '^NEW' "$OUT")" >> "$OUT"
cat "$OUT"
