#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
BASE=.ufo/waves/round-98/seats/V44-scratch/baseline-corpus-hashes.txt
OUT=.ufo/waves/round-98/seats/V44-scratch/check-corpus-out.txt
: > "$OUT"
while read -r hash path; do
  if [ ! -f "$path" ]; then echo "MISSING $path" >> "$OUT"; continue; fi
  cur=$(git hash-object "$path")
  if [ "$cur" != "$hash" ]; then echo "MODIFIED $path base=$hash cur=$cur" >> "$OUT"; fi
done < "$BASE"
git ls-files -co --exclude-standard corpus/ | sort > .ufo/waves/round-98/seats/V44-scratch/current-corpus-paths.txt
awk '{print $2}' "$BASE" | sort > .ufo/waves/round-98/seats/V44-scratch/baseline-corpus-paths.txt
comm -13 .ufo/waves/round-98/seats/V44-scratch/baseline-corpus-paths.txt .ufo/waves/round-98/seats/V44-scratch/current-corpus-paths.txt | sed 's/^/NEW /' >> "$OUT"
echo "--- baseline=$(wc -l < .ufo/waves/round-98/seats/V44-scratch/baseline-corpus-paths.txt) current=$(wc -l < .ufo/waves/round-98/seats/V44-scratch/current-corpus-paths.txt) modified=$(grep -c '^MODIFIED' "$OUT") missing=$(grep -c '^MISSING' "$OUT") new=$(grep -c '^NEW' "$OUT") ---" >> "$OUT"
cat "$OUT"
