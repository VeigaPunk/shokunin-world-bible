#!/bin/bash
SEATS=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-96/seats
TOOL=/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/map_obligations.py
CONTRACT=/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/map-obligations-contract.json
for i in $(seq 1 90); do
  cases=$(python3 - <<'PY' 2>/dev/null
import re
s=open("/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/map_obligations.py").read()
m=re.search(r"SELF_TEST_CASES = \((.*?)\)", s, re.S)
print(len(re.findall(r'"[a-z_0-9]+"', m.group(1))) if m else -1)
PY
)
  ncontract=$(python3 -c "import json;d=json.load(open('$CONTRACT'));print(len(d.get('self_test',{}).get('cases',[])))" 2>/dev/null || echo -1)
  q1=$(ls $SEATS/*.md 2>/dev/null | grep -c '/Q1')
  q2=$(ls $SEATS/*.md 2>/dev/null | grep -c '/Q2')
  echo "try=$i cases=$cases contract=$ncontract q1reports=$q1 q2reports=$q2 $(date +%T)"
  if [ "$cases" = "24" ] && [ "$ncontract" = "24" ] && [ "$q1" -ge 1 ] && [ "$q2" -ge 1 ]; then echo "READY"; exit 0; fi
  sleep 20
done
echo "TIMEOUT"
exit 3
