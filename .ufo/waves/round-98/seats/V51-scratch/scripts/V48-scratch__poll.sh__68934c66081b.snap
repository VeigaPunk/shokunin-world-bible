#!/bin/bash
# V48 poll: producer reports S1-S5 + artifact set + total report count
R=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$R/.ufo/waves/round-98/seats
LOG=$S/V48-scratch/poll.log
for i in $(seq 1 80); do
  reports=$(ls "$S"/V*.md "$S"/S*.md 2>/dev/null | wc -l)
  missing=""
  for s in S1 S2 S3 S4 S5; do
    ls "$S"/${s}-*.md >/dev/null 2>&1 || missing="$missing REPORT:$s"
  done
  for f in corpus/fixtures/r98-clerk-filing/entities.json corpus/fixtures/r98-clerk-filing/timeline.json corpus/fixtures/r98-clerk-filing/sources.json corpus/fixtures/r98-clerk-filing/README.md corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md corpus/knowledge/r98-clerk-scope-note.md; do
    [ -s "$R/$f" ] || missing="$missing ART:$f"
  done
  echo "try $i $(date -u +%H:%M:%S) reports=$reports missing:$missing" >> "$LOG"
  if [ -z "$missing" ]; then echo "ALL-PRESENT try $i $(date -u +%H:%M:%S)" >> "$LOG"; exit 0; fi
  sleep 20
done
echo "POLL-TIMEOUT 80 tries $(date -u +%H:%M:%S)" >> "$LOG"
exit 1
