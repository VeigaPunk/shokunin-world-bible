#!/usr/bin/env bash
# V06 poll2: wait specifically for S1's REPORT FILE (not its scratch dir).
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
for i in $(seq 1 36); do
  ts=$(date +%H:%M:%S)
  rep=$(ls .ufo/waves/round-98/seats/S1*.md 2>/dev/null | tr '\n' ' ')
  csha=$(sha256sum corpus/tools/dependency-freeze-contract.json | cut -d' ' -f1)
  tsha=$(sha256sum corpus/tools/dependency_freeze.py | cut -d' ' -f1)
  echo "poll2 try $i $ts | S1report=[$rep] tool=$tsha contract=$csha"
  if [ -n "$rep" ]; then echo "POLL2-SATISFIED at try $i"; exit 0; fi
  sleep 20
done
echo "POLL2-TIMEOUT: S1 report ABSENT after 36 tries (~12min)"
exit 1
