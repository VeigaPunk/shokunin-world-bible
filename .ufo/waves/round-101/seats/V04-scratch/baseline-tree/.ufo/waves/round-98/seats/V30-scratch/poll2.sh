#!/bin/sh
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 1
SEATS=.ufo/waves/round-98/seats
n=0
while [ "$n" -lt 40 ]; do
  n=$((n+1)); ts=$(date '+%H:%M:%S')
  S1=$(ls $SEATS/S1-*.md 2>/dev/null | wc -l); S2=$(ls $SEATS/S2-*.md 2>/dev/null | wc -l)
  echo "POLL2 t=$ts n=$n S1=$S1 S2=$S2"
  if [ "$S1" -ge 1 ] && [ "$S2" -ge 1 ]; then echo "S1S2-PRESENT t=$ts n=$n"; exit 0; fi
  sleep 20
done
echo "POLL2-DEADLINE n=$n"; exit 2
