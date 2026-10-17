#!/bin/bash
R=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$R/.ufo/waves/round-96/seats
for i in $(seq 1 40); do
  q2=0; v28=0; v29=0
  ls "$S"/Q2*.md >/dev/null 2>&1 && q2=1
  ls "$S"/V28-*.md >/dev/null 2>&1 && v28=1
  ls "$S"/V29-*.md >/dev/null 2>&1 && v29=1
  echo "try=$i Q2=$q2 V28=$v28 V29=$v29 $(date +%H:%M:%S)"
  if [ "$q2$v28$v29" = "111" ]; then echo "ALL-PRESENT"; exit 0; fi
  sleep 20
done
echo "TIMEOUT"
