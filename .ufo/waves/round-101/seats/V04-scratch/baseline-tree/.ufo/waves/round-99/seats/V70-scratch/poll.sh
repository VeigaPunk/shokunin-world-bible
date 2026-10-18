#!/bin/bash
# V70 poll-wait: artifacts + all five producer reports. 20s cadence, 40 tries.
set -u
R=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$R/.ufo/waves/round-99/seats
LOG=$SEATS/V70-scratch/poll.log
cd "$R" || exit 9
for try in $(seq 1 40); do
  ts=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  reports=$(ls -1 "$SEATS"/S*.md 2>/dev/null | wc -l)
  s1=$(ls -1 "$SEATS"/S1-*.md 2>/dev/null | wc -l)
  s2=$(ls -1 "$SEATS"/S2-*.md 2>/dev/null | wc -l)
  s3=$(ls -1 "$SEATS"/S3-*.md 2>/dev/null | wc -l)
  s4=$(ls -1 "$SEATS"/S4-*.md 2>/dev/null | wc -l)
  s5=$(ls -1 "$SEATS"/S5-*.md 2>/dev/null | wc -l)
  fixfiles=$(find corpus/fixtures/r99-window-lapse -type f 2>/dev/null | wc -l)
  k1=0; k2=0
  [ -f corpus/knowledge/r99-gate-blind-spot-table.md ] && k1=1
  [ -f corpus/knowledge/r99-lapse-scope-note.md ] && k2=1
  echo "try=$try ts=$ts reports=$reports s1=$s1 s2=$s2 s3=$s3 s4=$s4 s5=$s5 fixfiles=$fixfiles ktable=$k1 knote=$k2" >> "$LOG"
  if [ "$s1" -ge 1 ] && [ "$s2" -ge 1 ] && [ "$s3" -ge 1 ] && [ "$s4" -ge 1 ] && [ "$s5" -ge 1 ] \
     && [ "$fixfiles" -ge 10 ] && [ "$k1" -eq 1 ] && [ "$k2" -eq 1 ]; then
    echo "READY try=$try ts=$ts" >> "$LOG"
    exit 0
  fi
  if [ "$try" -eq 40 ]; then
    echo "EXHAUSTED try=$try ts=$ts" >> "$LOG"
    exit 2
  fi
  sleep 20
done
