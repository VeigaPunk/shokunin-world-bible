#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
LOG=.ufo/waves/round-102/seats/V12-scratch/poll2.log
: > "$LOG"
for i in $(seq 1 15); do
  N=$(find .ufo/waves/round-102/seats -maxdepth 1 -name '*.md' ! -name 'V12-scope.md' | wc -l)
  LIST=$(find .ufo/waves/round-102/seats -maxdepth 1 -name '*.md' -printf '%f ' 2>/dev/null)
  A=$(ls corpus/knowledge/r102-push-synthesis-r95-r102.md 2>/dev/null)
  echo "$(date '+%T') try=$i synth=${A:-MISSING} reports(non-self)=$N | $LIST" >> "$LOG"
  if [ -n "$A" ] && [ -n "$(ls .ufo/waves/round-102/seats/U1-*.md 2>/dev/null | head -1)" ]; then
    echo "$(date '+%T') U1-LANDED" >> "$LOG"; sleep 40; echo "$(date '+%T') audit-now" >> "$LOG"; exit 0
  fi
  sleep 20
done
echo "$(date '+%T') ESCAPE2" >> "$LOG"
exit 0
