#!/bin/sh
# V16 content-gated poll for S3 r99-window-lapse. 20s cadence, max 40 tries.
# Presence alone is not delivery (r98 placeholder class). Require:
#   1. S3-fixture-author.md exists and is nonempty
#   2. timeline.json contains clerk-lapse-recorded
#   3. sources.json contains clerk-lapse-note
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
FIX=$LANE/corpus/fixtures/r99-window-lapse
REPORT=$LANE/.ufo/waves/round-99/seats/S3-fixture-author.md
LOG=$LANE/.ufo/waves/round-99/seats/V16-scratch/poll.log
: > "$LOG"
i=0
while [ "$i" -lt 40 ]; do
  i=$((i + 1))
  ts=$(date '+%Y-%m-%d %H:%M:%S %z')
  dir=no; tl=no; src=no; rpt=no; ev=0; note=0
  if [ -d "$FIX" ]; then dir=yes; fi
  if [ -f "$FIX/timeline.json" ]; then
    tl=yes
    ev=$(grep -c 'clerk-lapse-recorded' "$FIX/timeline.json" 2>/dev/null || true)
  fi
  if [ -f "$FIX/sources.json" ]; then
    src=yes
    note=$(grep -c 'clerk-lapse-note' "$FIX/sources.json" 2>/dev/null || true)
  fi
  if [ -s "$REPORT" ]; then rpt=yes; fi
  echo "try=$i ts=$ts dir=$dir tl=$tl ev=$ev src=$src note=$note report=$rpt" | tee -a "$LOG"
  if [ "$ev" -ge 1 ] && [ "$note" -ge 1 ] && [ "$rpt" = yes ]; then
    echo "HIT try=$i ts=$ts" | tee -a "$LOG"
    exit 0
  fi
  if [ "$i" -ge 40 ]; then
    break
  fi
  sleep 20
done
echo "ABSENT after $i tries ts=$(date '+%Y-%m-%d %H:%M:%S %z')" | tee -a "$LOG"
exit 1
