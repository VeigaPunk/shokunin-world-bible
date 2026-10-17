#!/bin/bash
# poll for Q4/Q5/Q6 artifacts + producer reports
R=/home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  q4=0; q5=0; q6=0; r4=0; r5=0; r6=0
  [ -f "$R/corpus/fixtures/r96-crossing-response/sources.json" ] && [ -f "$R/corpus/fixtures/r96-crossing-response/timeline.json" ] && [ -f "$R/corpus/fixtures/r96-crossing-response/fictional-excerpts.md" ] && [ -f "$R/corpus/fixtures/r96-crossing-response/entities.json" ] && [ -f "$R/corpus/fixtures/r96-crossing-response/relations.json" ] && [ -f "$R/corpus/fixtures/r96-crossing-response/contradictions.json" ] && [ -f "$R/corpus/fixtures/r96-crossing-response/inspiration-note.md" ] && [ -f "$R/corpus/fixtures/r96-crossing-response/source-excerpt.md" ] && q4=1
  [ -f "$R/corpus/fixtures/r96-crossing-response/README.md" ] && [ -f "$R/corpus/fixtures/r96-crossing-response/claim-excerpt-map.md" ] && q5=1
  [ -f "$R/corpus/knowledge/r96-response-scope-note.md" ] && q6=1
  ls "$R/.ufo/waves/round-96/seats/" | grep -qi '^Q4' && r4=1
  ls "$R/.ufo/waves/round-96/seats/" | grep -qi '^Q5' && r5=1
  ls "$R/.ufo/waves/round-96/seats/" | grep -qi '^Q6' && r6=1
  echo "try=$i q4=$q4 r4=$r4 q5=$q5 r5=$r5 q6=$q6 r6=$r6 $(date +%H:%M:%S)"
  if [ "$q4$r4$q5$r5$q6$r6" = "111111" ]; then echo "ALL-PRESENT"; exit 0; fi
  sleep 20
done
echo "TIMEOUT"; exit 1
