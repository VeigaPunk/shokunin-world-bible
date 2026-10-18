#!/bin/bash
R=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$R/.ufo/waves/round-96/seats
for i in $(seq 1 40); do
  ok=1
  [ -f "$R/corpus/tools/dependency_freeze.py" ] || ok=0
  [ -f "$R/corpus/tools/dependency-freeze-contract.json" ] || ok=0
  [ -d "$R/corpus/fixtures/r96-crossing-response" ] || ok=0
  [ -f "$R/corpus/fixtures/r96-crossing-response/README.md" ] || ok=0
  [ -f "$R/corpus/knowledge/r96-response-scope-note.md" ] || ok=0
  grep -q '"schema_drift"' "$R/corpus/tools/map-obligations-contract.json" 2>/dev/null || ok=0
  reps=0
  for f in Q1 Q2 Q3 Q4 Q5 Q6; do [ -f "$S/$f"*.md ] && reps=$((reps+1)); done
  echo "try=$i ok=$ok producer_reports=$reps $(date +%T)"
  if [ "$ok" = "1" ] && [ "$reps" -ge 6 ]; then echo "ALL_PRESENT"; exit 0; fi
  sleep 20
done
echo "TIMEOUT_ABSENT"; exit 1
