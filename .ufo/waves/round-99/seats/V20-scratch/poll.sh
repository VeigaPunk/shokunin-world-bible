#!/bin/bash
# V20 poll-wait. 20s cadence, max 40 tries. Records presence; never verifies a plan.
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$LANE/.ufo/waves/round-99/seats
SCRATCH=$SEATS/V20-scratch
LOG=$SCRATCH/poll.log
: > "$LOG"
for t in $(seq 1 40); do
  ts=$(date '+%Y-%m-%dT%H:%M:%S%z')
  fx=$(find "$LANE/corpus/fixtures/r99-window-lapse" -maxdepth 1 -type f 2>/dev/null | wc -l)
  note1=0; note2=0
  [ -f "$LANE/corpus/knowledge/r99-gate-blind-spot-table.md" ] && note1=1
  [ -f "$LANE/corpus/knowledge/r99-lapse-scope-note.md" ] && note2=1
  reports=""
  for s in S1 S2 S3 S4 S5; do
    hit=$(find "$SEATS" -maxdepth 1 -name "${s}-*.md" -type f 2>/dev/null | wc -l)
    reports="${reports} ${s}:${hit}"
  done
  dirs=$(find "$LANE/corpus/fixtures" -mindepth 1 -maxdepth 1 -type d | wc -l)
  echo "t=$t ts=$ts dirs=$dirs fixture_files=$fx notes=${note1},${note2} reports:${reports}" | tee -a "$LOG"
  # producer reports: any S*-*.md that is not scratch
  allrep=1
  for s in S1 S2 S3 S4 S5; do
    hit=$(find "$SEATS" -maxdepth 1 -name "${s}-*.md" -type f 2>/dev/null | wc -l)
    [ "$hit" -ge 1 ] || allrep=0
  done
  if [ "$fx" -ge 10 ] && [ "$note1" = 1 ] && [ "$note2" = 1 ] && [ "$allrep" = 1 ]; then
    echo "READY t=$t ts=$ts" | tee -a "$LOG"
    exit 0
  fi
  sleep 20
done
echo "EXHAUSTED ts=$(date '+%Y-%m-%dT%H:%M:%S%z')" | tee -a "$LOG"
exit 2
