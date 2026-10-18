#!/bin/bash
# V02 poll: S1 tool+contract bytes vs baseline 9a3d648, and S1 report
R=/home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  changed=$(git -C "$R" diff --name-only 9a3d648 -- corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json)
  rep=$(ls "$R"/.ufo/waves/round-98/seats/S1-*.md 2>/dev/null | head -1)
  if [ -n "$changed" ] && [ -n "$rep" ]; then
    echo "ALL-PRESENT try=$i $(date -u +%H:%M:%S) changed=[$changed] report=$rep"; exit 0
  fi
  echo "try $i $(date -u +%H:%M:%S) changed=[${changed//$'\n'/ }] report=[${rep:-none}]"
  sleep 20
done
echo "POLL-TIMEOUT after 40 tries $(date -u +%H:%M:%S)"
exit 1
