#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
SEATS=.ufo/waves/round-98/seats
LOG=$SEATS/V52-scratch/poll.log
: > "$LOG"
for i in $(seq 1 40); do
  TS=$(date +%H:%M:%S)
  MODS=$(git status --porcelain | awk '{print $2}' | tr '\n' ',')
  REPORTS=$(ls -1 $SEATS/ 2>/dev/null | grep -E '^S[1-5]-.*\.md$' | tr '\n' ',')
  NR=$(ls -1 $SEATS/ 2>/dev/null | grep -cE '^S[1-5]-.*\.md$')
  FIX=$(ls corpus/fixtures/r98-clerk-filing/ 2>/dev/null | wc -l)
  KN=$(test -f corpus/knowledge/r98-clerk-scope-note.md && echo 1 || echo 0)
  echo "try=$i ts=$TS fixfiles=$FIX note=$KN nreports=$NR reports=[$REPORTS] mods=[$MODS]" >> "$LOG"
  if [ "$NR" -ge 5 ] && [ "$FIX" -ge 10 ] && [ "$KN" -ge 1 ]; then
    echo "COMPLETE try=$i" >> "$LOG"; exit 0
  fi
  sleep 20
done
echo "TIMEOUT after 40 tries" >> "$LOG"; exit 1
