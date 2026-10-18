#!/bin/bash
R=/home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  missing=""
  [ -f "$R/corpus/tools/dependency_freeze.py" ] || missing="$missing dep_freeze.py"
  [ -f "$R/corpus/tools/dependency-freeze-contract.json" ] || missing="$missing dep_contract"
  [ -f "$R/corpus/fixtures/r96-crossing-response/README.md" ] || missing="$missing r96README"
  [ -f "$R/corpus/knowledge/r96-response-scope-note.md" ] || missing="$missing note"
  # Q1/Q2 rewrites: mtime after wave start (17:37)
  q12=0
  for f in corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json corpus/tools/README.md; do
    if [ "$R/$f" -nt "$R/.ufo/waves/round-96/seats/V28-scratch/wavestart.stamp" ]; then q12=$((q12+1)); fi
  done
  [ "$q12" -eq 3 ] || missing="$missing q12_rewrites=$q12/3"
  reports=$(ls "$R/.ufo/waves/round-96/seats/" 2>/dev/null | grep -c '^Q[0-9].*\.md$')
  echo "try=$i missing:$missing Qreports=$reports $(date +%H:%M:%S)"
  if [ -z "$missing" ] && [ "$reports" -ge 6 ]; then echo "ALL-LANDED"; exit 0; fi
  sleep 20
done
echo "POLL-TIMEOUT"
