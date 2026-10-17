#!/bin/bash
# V28 poll for producer landings
R=/home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  missing=""
  [ -f "$R/corpus/tools/map_obligations.py" ] || missing="$missing map_obligations.py"
  [ -f "$R/corpus/tools/map-obligations-contract.json" ] || missing="$missing contract"
  [ -f "$R/corpus/tools/dependency_freeze.py" ] || missing="$missing dep_freeze.py"
  [ -f "$R/corpus/tools/dependency-freeze-contract.json" ] || missing="$missing dep_contract"
  [ -d "$R/corpus/fixtures/r96-crossing-response" ] || missing="$missing r96fixture"
  [ -f "$R/corpus/fixtures/r96-crossing-response/README.md" ] || missing="$missing r96README"
  [ -f "$R/corpus/knowledge/r96-response-scope-note.md" ] || missing="$missing note"
  # producer reports
  reports=$(ls "$R/.ufo/waves/round-96/seats/" 2>/dev/null | grep -c '^Q')
  echo "try=$i missing:$missing Qreports=$reports $(date +%H:%M:%S)"
  if [ -z "$missing" ] && [ "$reports" -ge 6 ]; then echo "ALL-LANDED"; exit 0; fi
  sleep 20
done
echo "POLL-TIMEOUT"
