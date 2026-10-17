#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
R=.ufo/waves/round-97/seats
for t in $(seq 1 40); do
  r3=$(ls $R/R3*.md 2>/dev/null | wc -l); r6=$(ls $R/R6*.md 2>/dev/null | wc -l)
  if [ "$r3" -ge 1 ] && [ "$r6" -ge 1 ]; then echo "REPORTS-READY t=$t $(date +%T) r3=$r3 r6=$r6"; exit 0; fi
  echo "t=$t $(date +%T) r3=$r3 r6=$r6"
  sleep 20
done
echo "TIMEOUT t=$(date +%T) r3=$r3 r6=$r6"; exit 7
