#!/bin/bash
# V45 poll-wait: wait for R3 (dependency_freeze hardening) + R3 report + V07 report
REPO=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$REPO/.ufo/waves/round-97/seats
LOG=$SEATS/V45-scratch/poll.log
for i in $(seq 1 40); do
  TS=$(date +%H:%M:%S)
  HARD=$(grep -c "PATH-MISMATCH" $REPO/corpus/tools/dependency_freeze.py 2>/dev/null || echo 0)
  R3=$(ls $SEATS/R3*.md 2>/dev/null | head -1)
  V07=$(ls $SEATS/V07*.md 2>/dev/null | head -1)
  echo "try=$i ts=$TS path_mismatch_in_tool=$HARD r3_report=${R3:-none} v07_report=${V07:-none}" >> $LOG
  if [ "$HARD" -gt 0 ] && [ -n "$R3" ]; then
    echo "READY try=$i ts=$TS r3=$R3 v07=${V07:-none}" >> $LOG
    exit 0
  fi
  sleep 20
done
echo "TIMEOUT after 40 tries" >> $LOG
exit 1
