#!/bin/bash
R=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$R/.ufo/waves/round-96/seats
for i in $(seq 1 45); do
  ok=1
  ls "$S"/Q1-*.md >/dev/null 2>&1 || ok=0
  ls "$S"/Q2-*.md >/dev/null 2>&1 || ok=0
  grep -q '"cases"' "$R/corpus/tools/map-obligations-contract.json" || ok=0
  n=$(grep -c '"id"' "$R/corpus/tools/map-obligations-contract.json")
  [ "$n" -ge 24 ] || ok=0
  grep -q 'Round-96' "$R/corpus/tools/README.md" || ok=0
  if [ $ok -eq 1 ]; then echo "Q1Q2_PRESENT try=$i cases=$n"; exit 0; fi
  sleep 20
done
echo "Q1Q2_TIMEOUT try=45"
ls "$S" | sort | tr '\n' ' '
echo
grep -c '"id"' "$R/corpus/tools/map-obligations-contract.json"
exit 1
