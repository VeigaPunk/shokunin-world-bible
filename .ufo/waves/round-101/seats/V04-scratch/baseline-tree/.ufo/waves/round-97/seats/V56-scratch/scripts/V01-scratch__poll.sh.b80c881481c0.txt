#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  tool_dp=$(grep -c 'dual_pointer' corpus/tools/map_obligations.py 2>/dev/null || echo 0)
  ct=$(python3 -c "import json;d=json.load(open('corpus/tools/map-obligations-contract.json'));c=d['self_test']['cases'];print(len(c), sum(1 for x in c if x['id']=='dual_pointer'))" 2>/dev/null || echo "ERR")
  r1=$(ls .ufo/waves/round-97/seats/ 2>/dev/null | grep -cE '^R0?1[-.]')
  r2=$(ls .ufo/waves/round-97/seats/ 2>/dev/null | grep -cE '^R0?2[-.]')
  echo "try=$i $(date +%T) tool_dp_mentions=$tool_dp contract_cases/dual=$ct R1report=$r1 R2report=$r2"
  if [ "$r1" -ge 1 ] && [ "$r2" -ge 1 ] && [ "$ct" != "ERR" ] && [ "${ct%% *}" -ge 25 ]; then echo "POLL-LANDED"; exit 0; fi
  sleep 20
done
echo "POLL-TIMEOUT"; exit 3
