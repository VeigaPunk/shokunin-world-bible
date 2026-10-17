#!/bin/bash
L=/home/vgpnk/Projects/shokunin/lore-shokunin
LOG=$L/.ufo/waves/round-96/seats/V39-scratch/poll.log
for i in $(seq 0 39); do
  T=$(date +%H:%M:%S)
  q1=$( [ -f "$L/corpus/tools/map_obligations.py" ] && sha256sum "$L/corpus/tools/map_obligations.py" | cut -c1-16 || echo ABSENT )
  q2c=$( [ -f "$L/corpus/tools/map-obligations-contract.json" ] && sha256sum "$L/corpus/tools/map-obligations-contract.json" | cut -c1-16 || echo ABSENT )
  q2r=$( [ -f "$L/corpus/tools/README.md" ] && sha256sum "$L/corpus/tools/README.md" | cut -c1-16 || echo ABSENT )
  q3p=$( [ -f "$L/corpus/tools/dependency_freeze.py" ] && sha256sum "$L/corpus/tools/dependency_freeze.py" | cut -c1-16 || echo ABSENT )
  q3c=$( [ -f "$L/corpus/tools/dependency-freeze-contract.json" ] && sha256sum "$L/corpus/tools/dependency-freeze-contract.json" | cut -c1-16 || echo ABSENT )
  fx=$(ls "$L/corpus/fixtures/r96-crossing-response" 2>/dev/null | wc -l)
  q6=$( [ -f "$L/corpus/knowledge/r96-response-scope-note.md" ] && sha256sum "$L/corpus/knowledge/r96-response-scope-note.md" | cut -c1-16 || echo ABSENT )
  seats=$(ls "$L/.ufo/waves/round-96/seats"/*.md 2>/dev/null | wc -l)
  prods=$(ls "$L/.ufo/waves/round-96/seats"/Q*.md 2>/dev/null | wc -l)
  ws=$( [ -f "$L/.ufo/waves/round-96/wave-spec.md" ] && echo YES || echo no )
  echo "$i $T q1=$q1 q2c=$q2c q2r=$q2r q3p=$q3p q3c=$q3c fx=$fx q6=$q6 seats=$seats prods=$prods ws=$ws" >> "$LOG"
  sleep 20
done
echo "POLL DONE $(date +%H:%M:%S)" >> "$LOG"
