#!/bin/bash
# R1 poll: wait for R5's r97 map to carry the 17th row (timeline.json#/5) and R5's report.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
LOG=.ufo/waves/round-97/seats/scratch-R1/poll-r5.log
: > "$LOG"
MAP=corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md
for i in $(seq 1 40); do
  rows=$(grep -c "^| " "$MAP" 2>/dev/null || echo 0)
  newrow=$(grep -c "timeline.json#/5" "$MAP" 2>/dev/null || echo 0)
  inv=$(grep -o "Expected inventory:\*\* [0-9]* JSON facts; [0-9]* editorial rows; [0-9]* total mapped rows" "$MAP" 2>/dev/null | head -1)
  rep=$(ls .ufo/waves/round-97/seats/R5*.md 2>/dev/null | head -1)
  tl=$(stat -c %Y corpus/fixtures/r97-crossing-acknowledgment/timeline.json 2>/dev/null || echo 0)
  mapsha=$(sha256sum "$MAP" 2>/dev/null | cut -c1-16)
  echo "try=$i map_rows=$rows newrow=$newrow mapsha=$mapsha inv=[$inv] tl_mtime=$tl r5_report=${rep:-absent} $(date -u +%H:%M:%SZ)" >> "$LOG"
  if [ "$newrow" != "0" ] && [ -n "$rep" ]; then
    echo "POLL_HIT try=$i map_rows=$rows newrow=$newrow mapsha=$mapsha r5_report=$rep"
    exit 0
  fi
  sleep 20
done
echo "POLL_TIMEOUT after 40 tries"; exit 1
