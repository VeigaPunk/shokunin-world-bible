#!/bin/bash
# V44 readiness gate: wait until R1+R2 reports exist AND tool+contract shas stable 3x20s.
REPO=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$REPO/.ufo/waves/round-97/seats
TOOL=$REPO/corpus/tools/map_obligations.py
CONTRACT=$REPO/corpus/tools/map-obligations-contract.json
LOG=$SEATS/V44-scratch/gate.log
: > "$LOG"
for n in $(seq 1 40); do
  r1=$(ls $SEATS/R1-*.md 2>/dev/null | head -1)
  r2=$(ls $SEATS/R2-*.md 2>/dev/null | head -1)
  cur=$(sha256sum "$TOOL" "$CONTRACT" 2>/dev/null | sha256sum | cut -c1-16)
  echo "GATE try=$n t=$((n*20))s r1=${r1:-none} r2=${r2:-none} sha=$cur" >> "$LOG"
  if [ -n "$r1" ] && [ -n "$r2" ]; then
    prev=""
    stable=0
    for i in $(seq 1 12); do
      cur=$(sha256sum "$TOOL" "$CONTRACT" 2>/dev/null | sha256sum | cut -c1-16)
      if [ "$cur" = "$prev" ]; then stable=$((stable+1)); else stable=0; fi
      echo "STAB i=$i sha=$cur stable=$stable" >> "$LOG"
      if [ $stable -ge 2 ]; then
        echo "GATE_READY sha=$cur r1=$r1 r2=$r2" >> "$LOG"
        exit 0
      fi
      prev=$cur
      sleep 20
    done
    echo "GATE_UNSTABLE last=$prev" >> "$LOG"
    exit 4
  fi
  sleep 20
done
echo "GATE_ABSENT r1=${r1:-none} r2=${r2:-none}" >> "$LOG"
exit 3
