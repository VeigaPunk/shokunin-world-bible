#!/bin/bash
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$ROOT/.ufo/waves/round-101/seats
LOG=$ROOT/.scratch/v26/poll.log
: > $LOG
for i in $(seq 1 40); do
  N=$(ls "$SEATS" 2>/dev/null | grep -c '\.md$')
  U1ART=$([ -f $ROOT/corpus/knowledge/r101-r10-register-first-entry.md ] && echo Y || echo N)
  PINS=$(python3 -c "import json;print(len(json.load(open('$ROOT/corpus/tools/dependency-freeze-contract.json'))['pins']))" 2>/dev/null)
  CASES=$(python3 -c "import json;print(len(json.load(open('$ROOT/corpus/tools/dependency-freeze-contract.json'))['self_test']['expected']))" 2>/dev/null)
  echo "try=$i seatreports=$N r101file=$U1ART pins=$PINS cases=$CASES $(date +%H:%M:%S)" >> $LOG
  if [ "$N" -ge 2 ] && [ "$U1ART" = "Y" ] && [ "$PINS" -ge 8 ] && [ "$CASES" -ge 19 ]; then
    echo "READY at try=$i" >> $LOG; exit 0
  fi
  sleep 20
done
echo "TIMEOUT after 40 tries" >> $LOG
