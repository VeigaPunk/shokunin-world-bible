#!/bin/bash
# V48 relation-scope-2 poll-wait. Presence only; never verifies a plan.
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS="$LANE/.ufo/waves/round-99/seats"
FIX="$LANE/corpus/fixtures/r99-window-lapse"
LOG="$SEATS/V48-scratch/poll.log"
MAX=40
: > "$LOG"
for i in $(seq 1 "$MAX"); do
  ts=$(date '+%Y-%m-%d %H:%M:%S %Z')
  miss=""
  for f in relations.json entities.json sources.json timeline.json fictional-excerpts.md contradictions.json inspiration-note.md source-excerpt.md README.md claim-excerpt-map.md; do
    [ -f "$FIX/$f" ] || miss="$miss fixture:$f"
  done
  [ -f "$SEATS/S3.md" ] || miss="$miss report:S3"
  [ -f "$SEATS/S4.md" ] || miss="$miss report:S4"
  # also accept producer reports under other conventional names
  s3=$(ls "$SEATS"/S3*.md 2>/dev/null | head -1)
  s4=$(ls "$SEATS"/S4*.md 2>/dev/null | head -1)
  [ -n "$s3" ] && miss=$(echo "$miss" | sed 's/ report:S3//')
  [ -n "$s4" ] && miss=$(echo "$miss" | sed 's/ report:S4//')
  echo "try=$i ts=$ts s3=${s3:-ABSENT} s4=${s4:-ABSENT} miss=[$miss]" >> "$LOG"
  if [ -z "$miss" ]; then
    echo "ALL-PRESENT try=$i ts=$ts" >> "$LOG"
    echo "ALL-PRESENT try=$i ts=$ts"
    exit 0
  fi
  sleep 20
done
echo "ABSENT after $MAX tries ts=$(date '+%Y-%m-%d %H:%M:%S %Z')" >> "$LOG"
echo "ABSENT"
exit 2
