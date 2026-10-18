#!/bin/bash
# V31 report collector: extract per-report bottom lines + verdict keywords.
R=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$R/.ufo/waves/round-98/seats
OUT=$R/.ufo/waves/round-98/scratch/V31/report-index.txt
: > "$OUT"
for f in $(ls "$S"/*.md 2>/dev/null | sort); do
  b=$(basename "$f")
  [ "$b" = "V31-adjudicator.md" ] && continue
  sz=$(stat -c%s "$f")
  bl=$(grep -n -i "bottom line" "$f" | tail -1 | cut -d: -f1)
  if [ -n "$bl" ]; then
    bline=$(tail -n +"$bl" "$f" | grep -v -i "bottom line" | grep -v '^$' | head -2 | tr '\n' ' ' | cut -c1-220)
  else
    bline=$(tail -3 "$f" | tr '\n' ' ' | cut -c1-220)
  fi
  pass=$(grep -c -o -i "PASS" "$f" 2>/dev/null); fail=$(grep -c -o -i "FAIL" "$f" 2>/dev/null)
  incon=$(grep -c -o -i "INCONCLUSIVE" "$f" 2>/dev/null); absent=$(grep -c -o -i "ABSENT" "$f" 2>/dev/null)
  echo "== $b ($sz bytes) PASS=$pass FAIL=$fail INCONC=$incon ABSENT=$absent" >> "$OUT"
  echo "   $bline" >> "$OUT"
done
echo "TOTAL reports: $(ls "$S"/*.md 2>/dev/null | grep -v V31-adjudicator | wc -l)/63" >> "$OUT"
cat "$OUT"
