#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
LOG=.ufo/waves/round-102/seats/V12-scratch/poll.log
: > "$LOG"
for i in $(seq 1 40); do
  A1=corpus/knowledge/r102-push-synthesis-r95-r102.md
  A2=corpus/knowledge/r102-debt-ledger.json
  A3=corpus/knowledge/r102-freshness-sweep.md
  U1=$(ls .ufo/waves/round-102/seats/U1-*.md 2>/dev/null | head -1)
  U2=$(ls .ufo/waves/round-102/seats/U2-*.md 2>/dev/null | head -1)
  N=$(find .ufo/waves/round-102/seats -maxdepth 1 -name '*.md' ! -name 'V12-scope.md' | wc -l)
  LIST=$(find .ufo/waves/round-102/seats -maxdepth 1 -name '*.md' -printf '%f ' 2>/dev/null)
  TS=$(date '+%T')
  if [ -f "$A1" ] && [ -f "$A2" ] && [ -f "$A3" ] && [ -n "$U1" ] && [ -n "$U2" ]; then G=GATE_OK; else G=WAIT; fi
  echo "$TS try=$i $G reports(non-self)=$N | $LIST" >> "$LOG"
  if [ "$G" = GATE_OK ]; then
    LAST=$(tail -6 "$LOG" | grep -o 'reports(non-self)=[0-9]*' | tail -1)
    PREV=$(tail -6 "$LOG" | grep -o 'reports(non-self)=[0-9]*' | head -1)
    # stable check: same report count over last 3 tries after gate
    C=$(tail -3 "$LOG" | grep -o 'reports(non-self)=[0-9]*' | sort -u | wc -l)
    if [ "$i" -ge 4 ] && [ "$C" -le 1 ]; then echo "$TS STABLE-after-gate try=$i" >> "$LOG"; exit 0; fi
  fi
  sleep 20
done
echo "$(date '+%T') ESCAPE max-tries" >> "$LOG"
exit 0
