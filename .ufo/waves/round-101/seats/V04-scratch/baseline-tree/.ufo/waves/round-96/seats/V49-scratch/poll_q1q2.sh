#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  q1=$(ls .ufo/waves/round-96/seats/ 2>/dev/null | grep -i "^Q1" | grep -v scratch | head -1)
  q2=$(ls .ufo/waves/round-96/seats/ 2>/dev/null | grep -i "^Q2" | grep -v scratch | head -1)
  if [ -n "$q1" ] || [ -n "$q2" ]; then
    echo "try $i: Q1='${q1:-absent}' Q2='${q2:-absent}'"; sha256sum corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json; date -Is; exit 0
  fi
  sleep 20
done
echo "TIMEOUT Q1/Q2: $(date -Is)"; ls .ufo/waves/round-96/seats/ | grep -iE "^Q[12]"; exit 3
