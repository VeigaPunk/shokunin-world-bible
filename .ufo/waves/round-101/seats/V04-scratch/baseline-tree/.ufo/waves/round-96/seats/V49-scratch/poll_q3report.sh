#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  rep=$(ls .ufo/waves/round-96/seats/ 2>/dev/null | grep -i "^Q3" | grep -v scratch | head -1)
  if [ -n "$rep" ]; then
    echo "Q3 REPORT at try $i: $rep"; sha256sum corpus/tools/dependency_freeze.py; date -Is; exit 0
  fi
  sleep 20
done
echo "TIMEOUT waiting Q3 report: $(date -Is)"; ls .ufo/waves/round-96/seats/ | grep -i "^Q3"; exit 3
