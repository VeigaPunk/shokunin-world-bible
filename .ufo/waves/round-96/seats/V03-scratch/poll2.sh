#!/bin/bash
SEATS=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-96/seats
CONTRACT=/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/map-obligations-contract.json
for i in $(seq 1 120); do
  ncontract=$(python3 -c "import json;d=json.load(open('$CONTRACT'));print(len(d.get('self_test',{}).get('cases',[])))" 2>/dev/null || echo -1)
  q2=$(ls $SEATS/*.md 2>/dev/null | grep -c '/Q2')
  echo "try=$i contract=$ncontract q2reports=$q2 $(date +%T)"
  if [ "$ncontract" = "24" ] && [ "$q2" -ge 1 ]; then echo "READY"; exit 0; fi
  sleep 20
done
echo "TIMEOUT"
exit 3
