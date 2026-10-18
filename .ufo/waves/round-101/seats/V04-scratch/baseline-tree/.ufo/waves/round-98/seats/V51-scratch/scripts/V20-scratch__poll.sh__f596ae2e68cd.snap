#!/bin/bash
# V20 poll: producer artifacts + all seat reports (self-excluded: V20)
R=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$R/.ufo/waves/round-98/seats
LOG=$SEATS/V20-scratch/poll.log
for i in $(seq 1 40); do
  missing=""
  for f in corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json corpus/tools/README.md \
           corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md \
           corpus/fixtures/r98-clerk-filing/entities.json corpus/fixtures/r98-clerk-filing/sources.json \
           corpus/fixtures/r98-clerk-filing/timeline.json corpus/fixtures/r98-clerk-filing/fictional-excerpts.md \
           corpus/fixtures/r98-clerk-filing/README.md corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md \
           corpus/knowledge/r98-clerk-scope-note.md; do
    [ -s "$R/$f" ] || missing="$missing $f"
  done
  for s in S1 S2 S3 S4 S5; do
    ls "$SEATS"/${s}-*.md >/dev/null 2>&1 || missing="$missing REPORT:$s"
  done
  n=$(ls "$SEATS"/*.md 2>/dev/null | wc -l)
  echo "try $i $(date -u +%H:%M:%S) reports=$n missing:$missing" >> "$LOG"
  if [ -z "$missing" ]; then echo "PRODUCERS-ALL-PRESENT try $i $(date -u +%H:%M:%S) reports=$n" >> "$LOG"; fi
  sleep 20
done
echo "POLL-TIMEOUT $(date -u +%H:%M:%S) reports=$(ls "$SEATS"/*.md 2>/dev/null | wc -l)" >> "$LOG"
