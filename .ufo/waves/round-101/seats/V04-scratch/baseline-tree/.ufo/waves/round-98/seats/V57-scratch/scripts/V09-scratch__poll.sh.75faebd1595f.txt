#!/bin/bash
# V09 round-98 poll: S3 owned files + S3 report; secondary: S4 map/README.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
LOG=.ufo/waves/round-98/seats/V09-scratch/poll.log
: > "$LOG"
FIX=corpus/fixtures/r98-clerk-filing
for i in $(seq 1 40); do
  missing=""
  for f in $FIX/entities.json $FIX/sources.json $FIX/timeline.json $FIX/fictional-excerpts.md; do
    [ -f "$f" ] || missing="$missing S3:$f"
  done
  if git diff --quiet 9a3d648 -- corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md; then
    missing="$missing S3:r95-map-repair"
  fi
  ls .ufo/waves/round-98/seats/S3-*.md >/dev/null 2>&1 || missing="$missing S3:report"
  missing2=""
  [ -f "$FIX/claim-excerpt-map.md" ] || missing2="$missing2 S4:map"
  [ -f "$FIX/README.md" ] || missing2="$missing2 S4:README"
  echo "$(date +%H:%M:%S) try=$i missing1[$missing ] missing2[$missing2 ]" >> "$LOG"
  if [ -z "$missing" ] && [ -z "$missing2" ]; then
    echo "POLL-DONE try=$i" >> "$LOG"; exit 0
  fi
  sleep 20
done
echo "POLL-TIMEOUT" >> "$LOG"
exit 1
