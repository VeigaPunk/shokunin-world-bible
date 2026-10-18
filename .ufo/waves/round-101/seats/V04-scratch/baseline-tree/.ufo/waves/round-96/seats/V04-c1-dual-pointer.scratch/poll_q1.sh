#!/bin/bash
# Poll for Q1 completion: producer report + dual_pointer in tool + contract self-test cases >= 24.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
SEATS=.ufo/waves/round-96/seats
for i in $(seq 1 40); do
  report=$(ls "$SEATS"/Q1*.md 2>/dev/null | head -1)
  hits=$(grep -c 'dual_pointer' corpus/tools/map_obligations.py 2>/dev/null)
  hits=${hits:-0}
  cases=$(python3 -c "import json;print(len(json.load(open('corpus/tools/map-obligations-contract.json'))['self_test']['cases']))" 2>/dev/null)
  cases=${cases:-0}
  if [ -n "$report" ] && [ "$hits" -ge 1 ] && [ "$cases" -ge 24 ]; then
    echo "READY attempt=$i report=$report dual_pointer_hits=$hits cases=$cases"
    exit 0
  fi
  echo "wait attempt=$i report=${report:-none} dual_pointer_hits=$hits cases=$cases"
  sleep 20
done
echo "TIMEOUT after 40 attempts"
exit 1
