#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
R=.ufo/waves/round-97/seats
for t in $(seq 1 40); do
  ok=1
  for f in corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json corpus/tools/README.md \
           corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json \
           corpus/fixtures/r96-crossing-response/claim-excerpt-map.md \
           corpus/fixtures/r97-crossing-acknowledgment/entities.json \
           corpus/fixtures/r97-crossing-acknowledgment/relations.json \
           corpus/fixtures/r97-crossing-acknowledgment/contradictions.json \
           corpus/fixtures/r97-crossing-acknowledgment/inspiration-note.md \
           corpus/fixtures/r97-crossing-acknowledgment/source-excerpt \
           corpus/fixtures/r97-crossing-acknowledgment/sources.json \
           corpus/fixtures/r97-crossing-acknowledgment/timeline.json \
           corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md \
           corpus/fixtures/r97-crossing-acknowledgment/README.md \
           corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md \
           corpus/knowledge/r97-acknowledgment-scope-note.md ; do
    [ -e "$f" ] || { ok=0; miss="$f"; }
  done
  r1=$(ls $R/R1*.md 2>/dev/null | wc -l); r2=$(ls $R/R2*.md 2>/dev/null | wc -l)
  r3=$(ls $R/R3*.md 2>/dev/null | wc -l); r4=$(ls $R/R4*.md 2>/dev/null | wc -l)
  r5=$(ls $R/R5*.md 2>/dev/null | wc -l); r6=$(ls $R/R6*.md 2>/dev/null | wc -l)
  allr=$(( r1+r2+r3+r4+r5+r6 ))
  if [ $ok -eq 1 ] && [ $allr -ge 6 ]; then
    echo "READY t=$t $(date +%T) reports=$allr"; exit 0
  fi
  echo "t=$t $(date +%T) ok=$ok missing=${miss:-none} reports=$allr (r1=$r1 r2=$r2 r3=$r3 r4=$r4 r5=$r5 r6=$r6)"
  miss=""
  sleep 20
done
echo "TIMEOUT_ABSENT $(date +%T)"; exit 7
