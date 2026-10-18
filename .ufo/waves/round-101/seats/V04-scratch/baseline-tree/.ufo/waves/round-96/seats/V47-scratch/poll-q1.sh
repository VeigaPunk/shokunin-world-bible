#!/usr/bin/env bash
# V47 poll-wait for Q1 (hardened map_obligations.py) + Q2 (contract 24 cases) + Q1 report.
cd /home/vgpnk/Projects/shokunin/lore-shokunin
LOG=.ufo/waves/round-96/seats/V47-scratch/poll-q1.log
: > "$LOG"
for i in $(seq 1 40); do
  TOOL_SHA=$(sha256sum corpus/tools/map_obligations.py 2>/dev/null | cut -d' ' -f1)
  HAS_DUAL=$(grep -c 'dual_pointer' corpus/tools/map_obligations.py 2>/dev/null)
  HAS_INV=$(grep -c 'inventory_mismatch' corpus/tools/map_obligations.py 2>/dev/null)
  N_CASES=$(python3 -c "import json;d=json.load(open('corpus/tools/map-obligations-contract.json'));print(len(d['self_test']['cases']))" 2>/dev/null)
  Q1_REPORT=$(ls .ufo/waves/round-96/seats/Q1-*.md 2>/dev/null | head -1)
  {
    echo "try=$i tool_sha=$TOOL_SHA dual=$HAS_DUAL inv=$HAS_INV contract_cases=$N_CASES q1_report=${Q1_REPORT:-none}"
  } >> "$LOG"
  if [ "$HAS_DUAL" -ge 1 ] && [ "$HAS_INV" -ge 1 ] && [ "$N_CASES" = "24" ] && [ -n "$Q1_REPORT" ]; then
    echo "READY try=$i tool_sha=$TOOL_SHA contract_cases=$N_CASES q1_report=$Q1_REPORT" >> "$LOG"
    exit 0
  fi
  sleep 20
done
echo "TIMEOUT tool_sha=$TOOL_SHA dual=$HAS_DUAL inv=$HAS_INV contract_cases=$N_CASES q1_report=${Q1_REPORT:-none}" >> "$LOG"
exit 1
