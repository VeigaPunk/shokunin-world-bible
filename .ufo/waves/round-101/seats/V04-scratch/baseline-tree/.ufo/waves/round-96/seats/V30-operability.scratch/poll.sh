#!/bin/bash
R=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$R/.ufo/waves/round-96/seats
for i in $(seq 1 40); do
  ok=1
  for f in corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json corpus/tools/README.md \
           corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json \
           corpus/fixtures/r96-crossing-response/entities.json \
           corpus/fixtures/r96-crossing-response/relations.json \
           corpus/fixtures/r96-crossing-response/contradictions.json \
           corpus/fixtures/r96-crossing-response/inspiration-note.json \
           corpus/fixtures/r96-crossing-response/source-excerpt.json \
           corpus/fixtures/r96-crossing-response/sources.json \
           corpus/fixtures/r96-crossing-response/timeline.json \
           corpus/fixtures/r96-crossing-response/fictional-excerpts.md \
           corpus/fixtures/r96-crossing-response/README.md \
           corpus/fixtures/r96-crossing-response/claim-excerpt-map.md \
           corpus/knowledge/r96-response-scope-note.md ; do
    [ -e "$R/$f" ] || { ok=0; }
  done
  for q in Q1 Q2 Q3 Q4 Q5 Q6; do
    ls "$S"/${q}-*.md >/dev/null 2>&1 || ok=0
  done
  if [ $ok -eq 1 ]; then echo "ALL_PRESENT try=$i"; exit 0; fi
  sleep 20
done
echo "TIMEOUT_ABSENT try=40"
for f in corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json corpus/fixtures/r96-crossing-response/README.md corpus/knowledge/r96-response-scope-note.md corpus/fixtures/r96-crossing-response/claim-excerpt-map.md; do
  [ -e "$R/$f" ] || echo "MISSING: $f"
done
ls "$S" | sort
exit 1
