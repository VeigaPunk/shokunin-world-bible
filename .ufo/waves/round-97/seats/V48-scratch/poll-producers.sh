#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
S=.ufo/waves/round-97/seats
for i in $(seq 1 18); do
  ts=$(date +%H:%M:%S)
  have=""
  for p in R3 R4 R5 R6; do
    f=$(ls $S/$p-*.md 2>/dev/null | head -1)
    [ -n "$f" ] && have="$have $p" || have="$have ${p}:absent"
  done
  echo "[$ts] try=$i$have"
  if [ "$have" = " R3 R4 R5 R6" ]; then echo "ALL-PRODUCERS-FOUND"; exit 0; fi
  sleep 20
done
echo "PRODUCERS-PARTIAL after 18 tries"
exit 1
