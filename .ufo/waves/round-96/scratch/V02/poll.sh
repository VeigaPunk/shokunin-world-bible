#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  Q1=$(ls .ufo/waves/round-96/seats/ 2>/dev/null | grep -c '^Q1')
  Q2=$(ls .ufo/waves/round-96/seats/ 2>/dev/null | grep -c '^Q2')
  N=$(python3 -c "
import json,sys
try:
  c=json.load(open('corpus/tools/map-obligations-contract.json'))
  print(len(c['self_test']['cases']))
except Exception as e:
  print('ERR')
" 2>/dev/null)
  echo "try=$i Q1=$Q1 Q2=$Q2 cases=$N $(date +%T)"
  if [ "$Q1" -ge 1 ] && [ "$Q2" -ge 1 ] && [ "$N" = "24" ]; then
    echo "READY"
    ls -la .ufo/waves/round-96/seats/ | grep -E '^.*Q[12]'
    exit 0
  fi
  sleep 20
done
echo "TIMEOUT"
exit 1
