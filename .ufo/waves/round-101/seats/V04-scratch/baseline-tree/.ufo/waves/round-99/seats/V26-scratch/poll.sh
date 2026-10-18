#!/bin/bash
# V26 poll-wait resume. Prior process logged tries 1-14 then was killed by the
# host 300s cap. This process continues tries 15-40. 20s cadence.
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS="$LANE/.ufo/waves/round-99/seats"
FIX="$LANE/corpus/fixtures/r99-window-lapse"
KNOW="$LANE/corpus/knowledge"
README="$LANE/corpus/tools/README.md"
LOG="$SEATS/V26-scratch/poll.log"
echo "RESUME ts=$(date '+%Y-%m-%dT%H:%M:%S%z') continuing at try=15 after host timeout killed tries 1-14" >> "$LOG"
for try in $(seq 15 40); do
  ts=$(date '+%Y-%m-%dT%H:%M:%S%z')
  missing=()
  for seat in S1 S2 S3 S4 S5; do
    if ! compgen -G "$SEATS/${seat}"'*.md' > /dev/null; then
      missing+=("${seat}-report")
    fi
  done
  for f in \
    "$FIX/README.md" \
    "$FIX/claim-excerpt-map.md" \
    "$KNOW/r99-gate-blind-spot-table.md" \
    "$KNOW/r99-lapse-scope-note.md" \
    "$README"
  do
    if [ ! -s "$f" ]; then
      missing+=("$(basename "$f")")
    fi
  done
  if [ -f "$FIX/README.md" ] && cmp -s "$FIX/README.md" "$LANE/corpus/fixtures/r98-clerk-filing/README.md"; then
    missing+=("S4-README-still-r98-copy")
  fi
  if [ -f "$FIX/claim-excerpt-map.md" ] && cmp -s "$FIX/claim-excerpt-map.md" "$LANE/corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md"; then
    missing+=("S4-map-still-r98-copy")
  fi
  if [ -f "$README" ] && grep -Eq 'Round-99|Round 99|r99-window-lapse' "$README"; then
    s2_state=addendum-marker-present
  else
    s2_state=no-round-99-marker
    missing+=("tools-README-no-Round-99")
  fi
  seats_n=$(find "$SEATS" -maxdepth 1 -name '*.md' 2>/dev/null | wc -l)
  echo "try=$try ts=$ts seats_md=$seats_n s2=$s2_state missing=${missing[*]:-NONE}" >> "$LOG"
  if [ ${#missing[@]} -eq 0 ]; then
    echo "ALL-PRESENT try=$try ts=$ts" >> "$LOG"
    echo "ALL-PRESENT try=$try"
    exit 0
  fi
  if [ "$try" -eq 40 ]; then
    echo "ABSENT-AFTER-40 try=$try ts=$ts missing=${missing[*]}" >> "$LOG"
    echo "ABSENT missing=${missing[*]}"
    exit 2
  fi
  sleep 20
done
