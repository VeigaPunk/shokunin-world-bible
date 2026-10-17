#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
FIX=corpus/fixtures/r95-crossing-aftermath
for i in $(seq 1 40); do
  fixok=0
  if [ -d "$FIX" ]; then
    n=$(ls "$FIX" 2>/dev/null | wc -l)
    if [ "$n" -ge 10 ]; then fixok=1; fi
  fi
  seats=$(ls .ufo/waves/round-95/seats/V08-*.md .ufo/waves/round-95/seats/V09-*.md .ufo/waves/round-95/seats/V1[0-4]-*.md 2>/dev/null | wc -l)
  echo "try=$i fix_files=$(ls "$FIX" 2>/dev/null | wc -l) seats=$seats/7 $(date +%T)"
  if [ "$fixok" = 1 ] && [ "$seats" -ge 7 ]; then echo ALL_PRESENT; exit 0; fi
  sleep 20
done
echo CUTOFF; exit 1
