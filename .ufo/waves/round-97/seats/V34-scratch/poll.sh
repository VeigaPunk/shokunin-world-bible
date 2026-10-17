#!/bin/bash
R=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$R/.ufo/waves/round-97/seats
LOG=$S/V34-scratch/poll.log
: > "$LOG"
for i in $(seq 1 40); do
  art=0; rep=0
  for f in corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json corpus/tools/README.md corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json corpus/fixtures/r96-crossing-response/claim-excerpt-map.md corpus/fixtures/r97-crossing-acknowledgment/entities.json corpus/fixtures/r97-crossing-acknowledgment/relations.json corpus/fixtures/r97-crossing-acknowledgment/contradictions.json corpus/fixtures/r97-crossing-acknowledgment/inspiration-note.md corpus/fixtures/r97-crossing-acknowledgment/source-excerpt.md corpus/fixtures/r97-crossing-acknowledgment/sources.json corpus/fixtures/r97-crossing-acknowledgment/timeline.json corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md corpus/fixtures/r97-crossing-acknowledgment/README.md corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md corpus/knowledge/r97-acknowledgment-scope-note.md; do
    [ -f "$R/$f" ] && art=$((art+1))
  done
  for r in R1 R2 R3 R4 R5 R6; do
    ls $S/$r-*.md >/dev/null 2>&1 && rep=$((rep+1))
  done
  echo "$(date +%H:%M:%S) try=$i art=$art/17 rep=$rep/6" >> "$LOG"
  if [ "$art" -ge 17 ] && [ "$rep" -ge 6 ]; then echo "READY at try=$i $(date +%H:%M:%S)" >> "$LOG"; exit 0; fi
  sleep 20
done
echo "TIMEOUT $(date +%H:%M:%S)" >> "$LOG"
exit 1
