#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
FIX=corpus/fixtures/r95-crossing-aftermath
for i in $(seq 1 40); do
  ok=1
  for f in README.md claim-excerpt-map.md entities.json relations.json contradictions.json inspiration-note.md source-excerpt.md sources.json timeline.json fictional-excerpts.md; do
    [ -f "$FIX/$f" ] || ok=0
  done
  grep -q 'timeline.json#/3' "$FIX/claim-excerpt-map.md" 2>/dev/null || ok=0
  grep -q 'aftermath-missing-evin' "$FIX/timeline.json" 2>/dev/null || ok=0
  grep -q 'schema_drift' corpus/tools/map_obligations.py 2>/dev/null || ok=0
  seats=$(ls .ufo/waves/round-95/seats/P1-*.md .ufo/waves/round-95/seats/P3-*.md .ufo/waves/round-95/seats/P4-*.md 2>/dev/null | wc -l)
  echo "try=$i fixfiles=$(ls "$FIX" 2>/dev/null | wc -l) mapok=$(grep -c 'timeline.json#/3' "$FIX/claim-excerpt-map.md" 2>/dev/null) schemadrift=$(grep -c 'schema_drift' corpus/tools/map_obligations.py 2>/dev/null) reports=$seats/3 $(date +%T)"
  if [ "$ok" = 1 ]; then echo READY; exit 0; fi
  sleep 20
done
echo CUTOFF; exit 1
