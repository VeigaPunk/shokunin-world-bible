#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  Q1=$(ls .ufo/waves/round-96/seats/ 2>/dev/null | grep -cE '^Q1[^/]*\.md$')
  Q2=$(ls .ufo/waves/round-96/seats/ 2>/dev/null | grep -cE '^Q2[^/]*\.md$')
  N=$(python3 -c "
import json
try:
  c=json.load(open('corpus/tools/map-obligations-contract.json'))
  print(len(c['self_test']['cases']))
except Exception: print('ERR')" 2>/dev/null)
  P=$(python3 corpus/tools/map_obligations.py --self-test 2>/dev/null | grep -c '^SELF-TEST PASS ')
  H=$(python3 corpus/tools/map_obligations.py --self-test 2>/dev/null | grep '^SELF-TEST CASES' | head -1)
  echo "try=$i Q1md=$Q1 Q2md=$Q2 cases=$N pass_lines=$P header='$H' $(date +%T)"
  if [ "$Q1" -ge 1 ] && [ "$Q2" -ge 1 ] && [ "$N" = "24" ]; then
    echo "READY"; exit 0
  fi
  sleep 20
done
echo "TIMEOUT"; exit 1
