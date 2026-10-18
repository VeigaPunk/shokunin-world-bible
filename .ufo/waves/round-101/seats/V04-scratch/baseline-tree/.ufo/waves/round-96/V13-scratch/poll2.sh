#!/bin/bash
R=/home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  q5=0; q6=0; r5=0; r6=0
  [ -f "$R/corpus/fixtures/r96-crossing-response/README.md" ] && [ -f "$R/corpus/fixtures/r96-crossing-response/claim-excerpt-map.md" ] && q5=1
  [ -f "$R/corpus/knowledge/r96-response-scope-note.md" ] && q6=1
  ls "$R/.ufo/waves/round-96/seats/" 2>/dev/null | grep -qE '^Q5-[A-Za-z0-9_-]+\.md$' && r5=1
  ls "$R/.ufo/waves/round-96/seats/" 2>/dev/null | grep -qE '^Q6-[A-Za-z0-9_-]+\.md$' && r6=1
  echo "try=$i q5=$q5 r5=$r5 q6=$q6 r6=$r6 $(date +%H:%M:%S)"
  if [ "$q5$r5$q6$r6" = "1111" ]; then echo "ALL-PRESENT"; exit 0; fi
  sleep 20
done
echo "TIMEOUT"; exit 1
