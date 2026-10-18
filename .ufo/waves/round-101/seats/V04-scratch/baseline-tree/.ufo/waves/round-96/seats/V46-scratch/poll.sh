#!/bin/sh
# V46 poll: wait for r96 fixture files + Q4/Q5 producer reports
FIX=/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r96-crossing-response
SEATS=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-96/seats
n=0
while [ "$n" -lt 40 ]; do
  n=$((n+1))
  ok=1
  for f in entities.json relations.json contradictions.json sources.json timeline.json inspiration-note.md source-excerpt.md fictional-excerpts.md README.md claim-excerpt-map.md; do
    [ -s "$FIX/$f" ] || ok=0
  done
  [ -s "$SEATS/Q4-fixture-json.md" ] || ok=0
  [ -s "$SEATS/Q5-fixture-docs.md" ] || ok=0
  if [ "$ok" = 1 ]; then echo "POLL_HIT check=$n elapsed=$((n*20))s $(date -u +%H:%M:%S)"; exit 0; fi
  missing=""
  for f in entities.json relations.json contradictions.json sources.json timeline.json inspiration-note.md source-excerpt.md fictional-excerpts.md README.md claim-excerpt-map.md; do
    [ -s "$FIX/$f" ] || missing="$missing $f"
  done
  [ -s "$SEATS/Q4-fixture-json.md" ] || missing="$missing Q4-report"
  [ -s "$SEATS/Q5-fixture-docs.md" ] || missing="$missing Q5-report"
  echo "POLL_CHECK check=$n elapsed=$((n*20))s missing:$missing"
  sleep 20
done
echo "POLL_TERMINAL deadline elapsed=800s"
exit 0
