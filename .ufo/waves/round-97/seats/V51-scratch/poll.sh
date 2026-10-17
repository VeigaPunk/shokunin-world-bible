#!/bin/bash
R=/home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  ok=1
  [ -f "$R/corpus/fixtures/r97-crossing-acknowledgment/relations.json" ] || ok=0
  [ -f "$R/corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md" ] || ok=0
  ls "$R"/.ufo/waves/round-97/seats/R*.md >/dev/null 2>&1 || ok=0
  if [ $ok -eq 1 ]; then echo "READY try=$i $(date +%T)"; exit 0; fi
  sleep 20
done
echo "TIMEOUT $(date +%T)"; ls -la "$R"/.ufo/waves/round-97/seats/ ; ls -la "$R"/corpus/fixtures/r97-crossing-acknowledgment/ 2>&1; exit 1
