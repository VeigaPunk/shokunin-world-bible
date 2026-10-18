#!/usr/bin/env bash
# V46 relation-scope-2 poll: wait for S3/S4 artifacts + reports (20s cadence, max 40 tries)
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 1
LOG=.ufo/waves/round-98/seats/V46-scratch/poll.log
: > "$LOG"
FX=corpus/fixtures/r98-clerk-filing
SEATS=.ufo/waves/round-98/seats
for i in $(seq 1 40); do
  ts=$(date +%H:%M:%S)
  fx="absent"; [ -d "$FX" ] && fx="$(ls "$FX" 2>/dev/null | wc -l)files"
  s3=$(ls "$SEATS"/S3-*.md 2>/dev/null | wc -l)
  s4=$(ls "$SEATS"/S4-*.md 2>/dev/null | wc -l)
  rel="absent"; [ -f "$FX/relations.json" ] && rel="present"
  map="absent"; [ -f "$FX/claim-excerpt-map.md" ] && map="present"
  rdm="absent"; [ -f "$FX/README.md" ] && rdm="present"
  echo "$ts try=$i fixture=$fx relations=$rel map=$map readme=$rdm S3report=$s3 S4report=$s4" >> "$LOG"
  if [ -d "$FX" ] && [ -f "$FX/relations.json" ] && [ -f "$FX/claim-excerpt-map.md" ] && [ -f "$FX/README.md" ] && [ "$s3" -ge 1 ] && [ "$s4" -ge 1 ]; then
    echo "$ts ALL-PRESENT" >> "$LOG"; exit 0
  fi
  sleep 20
done
echo "$(date +%H:%M:%S) POLL-EXHAUSTED" >> "$LOG"
exit 2
