#!/bin/sh
# V18 poll: wait for Q3 tool + contract + Q3 producer report; 20s cadence, 40 tries.
T=/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency_freeze.py
C=/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency-freeze-contract.json
R=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-96/seats
i=0
while [ $i -lt 40 ]; do
  i=$((i+1))
  tool=no; con=no; rep=no
  [ -e "$T" ] && tool=yes
  [ -e "$C" ] && con=yes
  ls "$R"/Q3*.md >/dev/null 2>&1 && rep=yes
  echo "POLL_CHECK try=$i t=$((i*20))s tool=$tool contract=$con report=$rep"
  if [ "$tool" = yes ] && [ "$con" = yes ] && [ "$rep" = yes ]; then
    echo "POLL_HIT try=$i"; exit 0
  fi
  sleep 20
done
echo "POLL_DEADLINE"; exit 1
