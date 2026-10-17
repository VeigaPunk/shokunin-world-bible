#!/bin/bash
D=/home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  c=$(stat -c %Y "$D/corpus/tools/dependency-freeze-contract.json")
  base=$(date -d '2026-10-17 18:35:00' +%s)
  rep=$(ls "$D/.ufo/waves/round-97/seats/"R3*.md 2>/dev/null | wc -l)
  echo "try=$i t=$(date +%H:%M:%S) contract_mtime=$(stat -c %y "$D/corpus/tools/dependency-freeze-contract.json" | cut -c1-19) r3_report=$rep"
  if [ "$c" -gt "$base" ] && [ "$rep" -ge 1 ]; then echo "R3_READY"; exit 0; fi
  sleep 20
done
echo "R3_TIMEOUT"; exit 1
