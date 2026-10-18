#!/bin/bash
# Continuation after host 600s kill of poll.sh at t=30. Completes tries 31-40.
# Does not truncate poll.log. Bounded stall-escape: recorded, not an extra budget.
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$LANE/.ufo/waves/round-99/seats
SCRATCH=$SEATS/V20-scratch
LOG=$SCRATCH/poll.log
echo "STALL-ESCAPE host-timeout-600s restart ts=$(date '+%Y-%m-%dT%H:%M:%S%z') continuing t=31..40" >> "$LOG"
for t in $(seq 31 40); do
  ts=$(date '+%Y-%m-%dT%H:%M:%S%z')
  fx=$(find "$LANE/corpus/fixtures/r99-window-lapse" -maxdepth 1 -type f 2>/dev/null | wc -l)
  note1=0; note2=0
  [ -f "$LANE/corpus/knowledge/r99-gate-blind-spot-table.md" ] && note1=1
  [ -f "$LANE/corpus/knowledge/r99-lapse-scope-note.md" ] && note2=1
  reports=""
  allrep=1
  for s in S1 S2 S3 S4 S5; do
    hit=$(find "$SEATS" -maxdepth 1 -name "${s}-*.md" -type f 2>/dev/null | wc -l)
    reports="${reports} ${s}:${hit}"
    [ "$hit" -ge 1 ] || allrep=0
  done
  dirs=$(find "$LANE/corpus/fixtures" -mindepth 1 -maxdepth 1 -type d | wc -l)
  echo "t=$t ts=$ts dirs=$dirs fixture_files=$fx notes=${note1},${note2} reports:${reports}" | tee -a "$LOG"
  if [ "$fx" -ge 10 ] && [ "$note1" = 1 ] && [ "$note2" = 1 ] && [ "$allrep" = 1 ]; then
    echo "READY t=$t ts=$ts" | tee -a "$LOG"
    exit 0
  fi
  if [ "$t" -lt 40 ]; then
    sleep 20
  fi
done
echo "EXHAUSTED ts=$(date '+%Y-%m-%dT%H:%M:%S%z')" | tee -a "$LOG"
exit 2
