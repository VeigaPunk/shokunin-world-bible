#!/bin/bash
# V52 poll-wait: producer P1 (map_obligations tool work) + P2 (contract/README addendum).
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 1
for i in $(seq 1 40); do
  ts=$(date +%H:%M:%S)
  p1=$(ls .ufo/waves/round-95/seats/P1-*.md 2>/dev/null | head -1)
  p2=$(ls .ufo/waves/round-95/seats/P2-*.md 2>/dev/null | head -1)
  mod=$(git status --porcelain -- corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json corpus/tools/README.md | tr '\n' ';')
  if [ -n "$p1" ] && [ -n "$mod" ]; then
    echo "$ts READY p1=$p1 p2=${p2:-none} mod=$mod"
    break
  fi
  echo "$ts waiting p1=${p1:-none} p2=${p2:-none} mod=${mod:-none}"
  sleep 20
done
echo "$(date +%H:%M:%S) POLL-DONE try=$i"
