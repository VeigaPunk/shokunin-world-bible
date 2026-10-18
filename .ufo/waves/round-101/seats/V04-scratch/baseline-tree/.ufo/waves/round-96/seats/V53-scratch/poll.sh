#!/bin/bash
# Poll for Q4 artifacts + producer report
L=/home/vgpnk/Projects/shokunin/lore-shokunin
D=$L/corpus/fixtures/r96-crossing-response
S=$L/.ufo/waves/round-96/seats
for i in $(seq 1 40); do
  ok=1
  for f in entities.json relations.json contradictions.json inspiration-note.md source-excerpt.md sources.json timeline.json fictional-excerpts.md; do
    [ -s "$D/$f" ] || ok=0
  done
  rep=$(ls "$S"/Q4*.md 2>/dev/null | head -1)
  [ -n "$rep" ] || ok=0
  if [ "$ok" = "1" ]; then
    echo "READY after $i tries"
    ls -la "$D"
    echo "report: $rep"
    exit 0
  fi
  sleep 20
done
echo "TIMEOUT after 40 tries"
ls -la "$D" 2>&1
ls "$S"/Q4*.md 2>&1
exit 1
