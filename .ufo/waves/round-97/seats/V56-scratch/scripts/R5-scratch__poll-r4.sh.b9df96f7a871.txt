#!/bin/bash
# R5 poll for R4 artifacts: r97 fixture files + R4 report. 20s x 40.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 3
FIX=corpus/fixtures/r97-crossing-acknowledgment
REPORT=.ufo/waves/round-97/seats/R4-fixture-json.md
FILES="entities.json relations.json contradictions.json inspiration-note.md source-excerpt.md sources.json timeline.json fictional-excerpts.md"
for i in $(seq 1 40); do
  missing=""
  [ -d "$FIX" ] || missing="$missing dir"
  for f in $FILES; do [ -f "$FIX/$f" ] || missing="$missing $f"; done
  [ -f "$REPORT" ] || missing="$missing REPORT"
  if [ -z "$missing" ]; then
    echo "READY try=$i at $(date -Is)"
    ls -la "$FIX"
    stat -c '%y %s %n' corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
    echo "R96MAP-SHA $(sha256sum corpus/fixtures/r96-crossing-response/claim-excerpt-map.md)"
    exit 0
  fi
  echo "try=$i missing:$missing at $(date -Is)"
  sleep 20
done
echo "TIMEOUT after 40 tries at $(date -Is)"
exit 1
