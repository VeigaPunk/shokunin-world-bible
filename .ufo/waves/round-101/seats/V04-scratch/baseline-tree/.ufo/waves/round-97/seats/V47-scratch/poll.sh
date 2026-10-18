#!/bin/bash
# V47 poll: wait for r97 fixture completeness + R1..R6 producer reports
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
FIX=$ROOT/corpus/fixtures/r97-crossing-acknowledgment
NEED="claim-excerpt-map.md contradictions.json entities.json fictional-excerpts.md inspiration-note.md README.md relations.json source-excerpt.md sources.json timeline.json"
for i in $(seq 1 40); do
  fix_ok=1
  for f in $NEED; do [ -f "$FIX/$f" ] || fix_ok=0; done
  r_ok=0
  for r in R1 R2 R3 R4 R5 R6; do
    ls $ROOT/.ufo/waves/round-97/seats/${r}-*.md >/dev/null 2>&1 && r_ok=$((r_ok+1))
  done
  echo "try=$i fix_ok=$fix_ok producers=$r_ok/6 $(date +%H:%M:%S)"
  if [ "$fix_ok" = 1 ] && [ "$r_ok" = 6 ]; then echo "READY"; exit 0; fi
  sleep 20
done
echo "TIMEOUT"
exit 1
