#!/bin/bash
# V30 poll-wait: wait for R3 delivery (tool hardened + contract 16 cases + R3 report)
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$ROOT/.ufo/waves/round-97/seats
for i in $(seq 1 40); do
  TOOL_OK=0; CONTRACT_OK=0; REPORT_OK=0
  grep -q "PATH-MISMATCH" $ROOT/corpus/tools/dependency_freeze.py 2>/dev/null && TOOL_OK=1
  python3 -c "import json,sys; c=json.load(open('$ROOT/corpus/tools/dependency-freeze-contract.json')); sys.exit(0 if len(c.get('self_test',{}).get('expected',{}))>=16 else 1)" 2>/dev/null && CONTRACT_OK=1
  ls $SEATS/R3*.md >/dev/null 2>&1 && REPORT_OK=1
  echo "try=$i tool=$TOOL_OK contract=$CONTRACT_OK r3report=$REPORT_OK $(date +%T)"
  if [ $TOOL_OK -eq 1 ] && [ $CONTRACT_OK -eq 1 ] && [ $REPORT_OK -eq 1 ]; then echo "DELIVERED"; exit 0; fi
  sleep 20
done
echo "TIMEOUT-ABSENT"; exit 1
