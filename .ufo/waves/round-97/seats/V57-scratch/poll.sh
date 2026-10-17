#!/bin/bash
S=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats
for i in $(seq 1 40); do
  FIX=$(ls -d /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r97-crossing-acknowledgment 2>/dev/null)
  REPS=$(ls $S/R[1-6]*.md 2>/dev/null | wc -l)
  echo "$(date -Is) try=$i fixture=${FIX:+yes} producer_reports=$REPS"
  if [ -n "$FIX" ] && [ "$REPS" -ge 6 ]; then echo "ALL PRESENT"; exit 0; fi
  sleep 20
done
echo "POLL TIMEOUT"
