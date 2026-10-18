#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=.ufo/waves/round-97/seats
FIX=corpus/fixtures/r97-crossing-acknowledgment
for i in $(seq 1 40); do
  need=""
  [ -d "$FIX" ] || need="$need fixture-dir"
  for f in entities.json relations.json contradictions.json timeline.json sources.json inspiration-note.md source-excerpt.md fictional-excerpts.md; do
    [ -s "$FIX/$f" ] || need="$need $f"
  done
  for r in R4-fixture-json.md R5-fixture-docs.md R6-knowledge-note.md; do
    [ -s "$SEATS/$r" ] || need="$need $r"
  done
  if [ -z "$need" ]; then echo "READY after $i tries $(date +%H:%M:%S)"; ls -la $FIX; exit 0; fi
  echo "try $i $(date +%H:%M:%S) missing:$need"
  sleep 20
done
echo "TIMEOUT $(date +%H:%M:%S) missing:$need"; exit 1
