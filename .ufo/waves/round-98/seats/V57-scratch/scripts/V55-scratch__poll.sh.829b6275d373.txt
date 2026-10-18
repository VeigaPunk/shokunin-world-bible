#!/bin/bash
# V55 poll: wait for S4 artifacts (README.md, claim-excerpt-map.md) + S3 JSON tables + S4 report
cd /home/vgpnk/Projects/shokunin/lore-shokunin
FIX=corpus/fixtures/r98-clerk-filing
for i in $(seq 1 40); do
  missing=""
  for f in $FIX/README.md $FIX/claim-excerpt-map.md $FIX/entities.json $FIX/sources.json $FIX/timeline.json $FIX/fictional-excerpts.md; do
    [ -f "$f" ] || missing="$missing $f"
  done
  rep=$(ls .ufo/waves/round-98/seats/S4*.md 2>/dev/null | head -1)
  if [ -z "$missing" ] && [ -n "$rep" ]; then
    echo "TRY $i: ALL PRESENT: $rep"; ls -la $FIX; exit 0
  fi
  echo "TRY $i: missing:${missing:- none} S4-report:${rep:- ABSENT}"
  sleep 20
done
echo "POLL EXHAUSTED (40 tries)"
exit 3
