#!/bin/bash
# V33 poll: wait for producer reports + key artifacts
cd /home/vgpnk/Projects/shokunin/lore-shokunin
S=.ufo/waves/round-97/seats
for i in $(seq 1 40); do
  ok=1
  for r in R1 R2 R3 R4 R5 R6; do
    ls $S/$r-*.md >/dev/null 2>&1 || ok=0
  done
  [ -d corpus/fixtures/r97-crossing-acknowledgment ] || ok=0
  [ -f corpus/knowledge/r97-acknowledgment-scope-note.md ] || ok=0
  if [ $ok -eq 1 ]; then echo "POLL-READY at try $i $(date -u +%H:%M:%S)"; ls $S/*.md; exit 0; fi
  echo "try $i $(date -u +%H:%M:%S): R=[$(ls $S/R*-*.md 2>/dev/null | wc -l)] fixture=$([ -d corpus/fixtures/r97-crossing-acknowledgment ] && echo y || echo n) note=$([ -f corpus/knowledge/r97-acknowledgment-scope-note.md ] && echo y || echo n)"
  sleep 20
done
echo "POLL-TIMEOUT after 40 tries"
ls $S/ | sort
exit 1
