#!/bin/bash
# V34 poll-wait for C1 producer artifacts (Q1: tool, Q2: contract+README)
R=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$R/.ufo/waves/round-96/seats
for i in $(seq 1 40); do
  tool_hash=$(sha256sum $R/corpus/tools/map_obligations.py 2>/dev/null | cut -d' ' -f1)
  cases=$(python3 -c "import json;print(len(json.load(open('$R/corpus/tools/map-obligations-contract.json'))['self_test']['cases']))" 2>/dev/null)
  q1=$(ls $S/Q1*.md 2>/dev/null | head -1)
  q2=$(ls $S/Q2*.md 2>/dev/null | head -1)
  echo "try=$i t=$(date -u +%H:%M:%S) tool=$tool_hash cases=$cases q1=${q1:-none} q2=${q2:-none}"
  if [ "$tool_hash" != "d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108" ] && [ "$cases" = "24" ] && [ -n "$q1" ] && [ -n "$q2" ]; then
    echo "C1-ARTIFACTS-LANDED"
    exit 0
  fi
  sleep 20
done
echo "C1-ARTIFACTS-ABSENT-AFTER-40-TRIES"
exit 3
