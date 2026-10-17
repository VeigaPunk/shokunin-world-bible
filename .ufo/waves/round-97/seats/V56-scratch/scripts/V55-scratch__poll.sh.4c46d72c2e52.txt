#!/bin/bash
# V55 poll: wait for producer reports R1..R6 AND key artifacts
SEATS=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats
REPO=/home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  ok=1
  for r in R1 R2 R3 R4 R5 R6; do
    ls $SEATS/${r}-*.md >/dev/null 2>&1 || ok=0
  done
  [ -d $REPO/corpus/fixtures/r97-crossing-acknowledgment ] || ok=0
  [ -f $REPO/corpus/fixtures/r97-crossing-acknowledgment/sources.json ] || ok=0
  [ -f $REPO/corpus/fixtures/r97-crossing-acknowledgment/timeline.json ] || ok=0
  [ -f $REPO/corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md ] || ok=0
  [ -f $REPO/corpus/fixtures/r97-crossing-acknowledgment/README.md ] || ok=0
  [ -f $REPO/corpus/knowledge/r97-acknowledgment-scope-note.md ] || ok=0
  if [ $ok -eq 1 ]; then
    echo "READY at try $i $(date -Is)"
    ls $SEATS/R*.md
    exit 0
  fi
  echo "try $i: not ready $(date -Is)" 
  sleep 20
done
echo "TIMEOUT after 40 tries"
exit 1
