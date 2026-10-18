#!/bin/bash
# V45 poll: wait for r98-clerk-filing artifacts (S3 4 files + S4 2 files)
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
D=corpus/fixtures/r98-clerk-filing
LOG=.ufo/waves/round-98/seats/V45-scratch/poll.log
: > "$LOG"
for i in $(seq 1 40); do
  missing=""
  for f in entities.json sources.json timeline.json fictional-excerpts.md README.md claim-excerpt-map.md; do
    [ -f "$D/$f" ] || missing="$missing $f"
  done
  if [ -z "$missing" ]; then
    echo "try $i $(date +%T) ALL-PRESENT" >> "$LOG"
    exit 0
  fi
  echo "try $i $(date +%T) missing:$missing" >> "$LOG"
  sleep 20
done
echo "EXHAUSTED $(date +%T)" >> "$LOG"
exit 1
