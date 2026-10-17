#!/bin/sh
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
FIX=$ROOT/corpus/fixtures/r96-crossing-response
SEATS=$ROOT/.ufo/waves/round-96/seats
LOG=$ROOT/.ufo/waves/round-96/seats/scratch/V12/poll.log
: > "$LOG"
i=0
while [ $i -lt 40 ]; do
  i=$((i+1))
  miss=""
  for f in entities.json relations.json contradictions.json inspiration-note.md source-excerpt.md sources.json timeline.json fictional-excerpts.md README.md claim-excerpt-map.md; do
    [ -e "$FIX/$f" ] || miss="$miss $f"
  done
  q4=""; q5=""
  for p in "$SEATS"/Q4*.md; do [ -e "$p" ] && q4="$q4 $(basename $p)"; done
  for p in "$SEATS"/Q5*.md; do [ -e "$p" ] && q5="$q5 $(basename $p)"; done
  echo "CHECK t=$((i*20))s missing=[$miss] q4=[$q4] q5=[$q5]" >> "$LOG"
  if [ -z "$miss" ] && [ -n "$q4" ] && [ -n "$q5" ]; then echo "POLL_READY t=$((i*20))s" >> "$LOG"; exit 0; fi
  sleep 20
done
echo "POLL_TERMINAL t=800s" >> "$LOG"
exit 0
