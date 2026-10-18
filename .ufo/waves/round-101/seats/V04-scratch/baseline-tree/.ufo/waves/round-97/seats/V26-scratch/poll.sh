#!/bin/bash
# V26 poll: producers' artifacts + reports
cd /home/vgpnk/Projects/shokunin/lore-shokunin
need_fixture="corpus/fixtures/r97-crossing-acknowledgment/README.md corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md"
need_know="corpus/knowledge/r97-acknowledgment-scope-note.md"
for i in $(seq 1 40); do
  ok=1
  for f in $need_fixture $need_know; do [ -f "$f" ] || ok=0; done
  reps=0
  for r in R1 R2 R3 R4 R5 R6; do ls .ufo/waves/round-97/seats/${r}-*.md >/dev/null 2>&1 && reps=$((reps+1)); done
  if [ $ok -eq 1 ] && [ $reps -ge 6 ]; then echo "POLL_READY try=$i reps=$reps"; exit 0; fi
  echo "poll try=$i reps=$reps fixture=$([ -f corpus/fixtures/r97-crossing-acknowledgment/README.md ] && echo yes || echo no) know=$([ -f corpus/knowledge/r97-acknowledgment-scope-note.md ] && echo yes || echo no)"
  sleep 20
done
echo "POLL_TIMEOUT reps=$reps"
exit 1
