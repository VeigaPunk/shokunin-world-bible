#!/bin/bash
# V28 poll-wait: producers' artifacts + reports
L=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$L/.ufo/waves/round-97/seats
F=$L/corpus/fixtures/r97-crossing-acknowledgment
for i in $(seq 1 40); do
  missing=""
  for f in $F/entities.json $F/relations.json $F/contradictions.json $F/inspiration-note.md $F/source-excerpt.md $F/sources.json $F/timeline.json $F/fictional-excerpts.md $F/README.md $F/claim-excerpt-map.md $L/corpus/knowledge/r97-acknowledgment-scope-note.md; do
    [ -s "$f" ] || missing="$missing $(basename $f)"
  done
  for r in R1 R2 R3 R4 R5 R6; do
    [ -s "$S/$r.md" ] || missing="$missing report-$r"
  done
  if [ -z "$missing" ]; then echo "ALL-PRESENT try=$i"; exit 0; fi
  echo "try=$i missing:$missing"
  sleep 20
done
echo "TIMEOUT-ABSENT"; exit 1
