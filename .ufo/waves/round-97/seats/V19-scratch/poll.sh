#!/bin/bash
# V19 poll: wait for R4 report + r96 map change vs baseline
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
BASE=.ufo/waves/round-97/seats/V19-scratch/r96-map-baseline.md
MAP=corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
R4REP=.ufo/waves/round-97/seats/R4-c3-r97-fixture-arc.md
for i in $(seq 1 40); do
  changed=0; rep=0
  cmp -s "$BASE" "$MAP" || changed=1
  ls .ufo/waves/round-97/seats/R4*.md >/dev/null 2>&1 && rep=1
  if [ "$changed" = 1 ] && [ "$rep" = 1 ]; then
    echo "READY try=$i changed=$changed report=$rep"; ls -la .ufo/waves/round-97/seats/R4*.md; exit 0
  fi
  echo "wait try=$i changed=$changed report=$rep $(date +%T)"
  sleep 20
done
echo "TIMEOUT after 40 tries; changed=$changed report=$rep"; ls -la .ufo/waves/round-97/seats/ ; exit 3
