#!/bin/bash
# V44 r97 poll: wait for R1+R2 artifacts/reports and V04 report; log tool/contract state.
REPO=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$REPO/.ufo/waves/round-97/seats
TOOL=$REPO/corpus/tools/map_obligations.py
CONTRACT=$REPO/corpus/tools/map-obligations-contract.json
LOG=$SEATS/V44-scratch/poll.log
: > "$LOG"
n=0
while [ $n -lt 40 ]; do
  n=$((n+1))
  r1=$(ls $SEATS/R1-*.md 2>/dev/null | head -1)
  r2=$(ls $SEATS/R2-*.md 2>/dev/null | head -1)
  v04=$(ls $SEATS/V04-*.md 2>/dev/null | head -1)
  tsha=$(sha256sum "$TOOL" 2>/dev/null | cut -c1-12)
  csha=$(sha256sum "$CONTRACT" 2>/dev/null | cut -c1-12)
  ncases=$(python3 -c "import json;print(len(json.load(open('$CONTRACT'))['self_test']['cases']))" 2>/dev/null)
  dual=$(grep -c '"dual_pointer"' "$CONTRACT" 2>/dev/null)
  echo "CHECK try=$n t=$((n*20))s tool=$tsha contract=$csha cases=$ncases dual=$dual r1=${r1:-none} r2=${r2:-none} v04=${v04:-none}" >> "$LOG"
  if [ -n "$r1" ] && [ -n "$r2" ] && [ -n "$v04" ]; then
    echo "READY try=$n r1=$r1 r2=$r2 v04=$v04" >> "$LOG"
    exit 0
  fi
  sleep 20
done
echo "ABSENT tries=$n r1=${r1:-none} r2=${r2:-none} v04=${v04:-none}" >> "$LOG"
exit 3
