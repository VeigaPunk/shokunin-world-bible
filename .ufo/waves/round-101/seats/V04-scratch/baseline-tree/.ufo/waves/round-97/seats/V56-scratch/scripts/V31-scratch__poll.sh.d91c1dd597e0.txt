#!/bin/bash
# V31 poll-wait: C1 producers R1 (tool) + R2 (contract/README) artifacts + reports.
cd /home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=.ufo/waves/round-97/seats
for i in $(seq 1 40); do
  tool_changed=0; contract25=0; r1rep=0; r2rep=0
  git diff --quiet f3e09f9 -- corpus/tools/map_obligations.py || tool_changed=1
  python3 - <<'EOF' && contract25=1 || contract25=0
import json,sys
c=json.load(open('corpus/tools/map-obligations-contract.json'))
ids=[x['id'] for x in c.get('self_test',{}).get('cases',[])]
sys.exit(0 if (len(ids)>=25 and 'dual_pointer' in ids) else 1)
EOF
  ls "$SEATS" 2>/dev/null | grep -Eq '^R1.*\.md$' && r1rep=1
  ls "$SEATS" 2>/dev/null | grep -Eq '^R2.*\.md$' && r2rep=1
  echo "poll $i $(date +%H:%M:%S) tool_changed=$tool_changed contract25=$contract25 r1rep=$r1rep r2rep=$r2rep"
  if [ "$tool_changed" = 1 ] && [ "$contract25" = 1 ] && [ "$r1rep" = 1 ] && [ "$r2rep" = 1 ]; then
    echo "READY after $i polls"; exit 0
  fi
  sleep 20
done
echo "TIMEOUT after 40 polls"; exit 3
