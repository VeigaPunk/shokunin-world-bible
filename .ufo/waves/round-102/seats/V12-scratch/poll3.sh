#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
LOG=.ufo/waves/round-102/seats/V12-scratch/poll3.log
: > "$LOG"
prev=99; same=0
for i in $(seq 1 10); do
  N=$(find .ufo/waves/round-102/seats -maxdepth 1 -name '*.md' ! -name 'V12-scope.md' | wc -l)
  M=$(git status --porcelain=v1 | grep -cE '^ ?[MDARC]' )
  echo "$(date '+%T') try=$i reports(non-self)=$N trackedmods=$M" >> "$LOG"
  if [ "$N" -ge 19 ]; then echo "$(date '+%T') FULL-ROSTER" >> "$LOG"; exit 0; fi
  if [ "$N" -eq "$prev" ]; then same=$((same+1)); else same=0; fi
  if [ "$same" -ge 4 ] && [ "$i" -ge 5 ]; then echo "$(date '+%T') STABLE-NOGROW" >> "$LOG"; exit 0; fi
  prev=$N; sleep 20
done
echo "$(date '+%T') ESCAPE3" >> "$LOG"
