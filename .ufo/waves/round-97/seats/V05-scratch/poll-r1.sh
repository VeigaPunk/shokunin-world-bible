#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=.ufo/waves/round-97/seats
for i in $(seq 1 40); do
  tool_changed=0; report=0; r2_changed=0
  if ! git diff --quiet f3e09f9 -- corpus/tools/map_obligations.py; then tool_changed=1; fi
  if compgen -G "$SEATS/R1*.md" > /dev/null; then report=1; fi
  if ! git diff --quiet f3e09f9 -- corpus/tools/map-obligations-contract.json; then r2_changed=1; fi
  echo "poll $i/40 tool_changed=$tool_changed r1_report=$report contract_changed=$r2_changed $(date +%H:%M:%S)"
  if [ "$tool_changed" = 1 ] && [ "$report" = 1 ]; then
    echo "READY: R1 tool diff + R1 report present"
    exit 0
  fi
  sleep 20
done
echo "ABSENT-TIMEOUT after 40 tries"
exit 1
