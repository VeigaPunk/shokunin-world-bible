#!/bin/bash
# poll for P1 artifact (map_obligations.py changed vs fb118c4) and V25 report
cd /home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  p1=$(git diff --name-only fb118c4 -- corpus/tools/map_obligations.py | wc -l)
  v25=$(ls .ufo/waves/round-95/seats/ 2>/dev/null | grep -ci '^V25')
  p1rep=$(ls .ufo/waves/round-95/seats/ 2>/dev/null | grep -ci '^P1')
  echo "try=$i p1_diff=$p1 v25=$v25 p1_report=$p1rep $(date +%T)"
  if [ "$p1" -ge 1 ] && [ "$v25" -ge 1 ] && [ "$p1rep" -ge 1 ]; then echo READY; exit 0; fi
  sleep 20
done
echo CUTOFF; exit 1
