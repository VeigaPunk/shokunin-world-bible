#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
FIX=corpus/fixtures/r96-crossing-response
for i in $(seq 1 40); do
  ts=$(date -Iseconds)
  files_ok=1
  for f in README.md claim-excerpt-map.md timeline.json sources.json entities.json relations.json contradictions.json fictional-excerpts.md inspiration-note.md source-excerpt.md; do
    [ -s "$FIX/$f" ] || files_ok=0
  done
  rep=""
  for r in .ufo/waves/round-96/seats/Q5-*.md .ufo/waves/round-96/seats/P5-*.md; do
    [ -s "$r" ] && rep="$r"
  done
  if [ "$files_ok" = 1 ] && [ -n "$rep" ]; then
    echo "$ts try=$i READY files=all report=$rep"
    exit 0
  fi
  echo "$ts try=$i files_ok=$files_ok report=${rep:-none}"
  sleep 20
done
echo "$(date -Iseconds) TIMEOUT"
exit 3
