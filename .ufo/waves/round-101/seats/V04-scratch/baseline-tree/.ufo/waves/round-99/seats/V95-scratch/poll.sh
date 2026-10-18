#!/bin/bash
# V95 poll-wait. Artifact-based. SELF subtracted from all-reports.
# Cadence 20s, max 40 tries. Logs only under V95-scratch.
set -u
ROOT="/home/vgpnk/Projects/shokunin/lore-shokunin"
SEATS="$ROOT/.ufo/waves/round-99/seats"
FIX="$ROOT/corpus/fixtures/r99-window-lapse"
KNOW="$ROOT/corpus/knowledge"
LOG="$SEATS/V95-scratch/poll.log"
MAX=40
i=0
while [ "$i" -lt "$MAX" ]; do
  i=$((i+1))
  ts=$(date -Is)
  fx_ok=0
  map_ok=0
  readme_ok=0
  know_ok=0
  s3=0; s4=0; s5=0
  [ -d "$FIX" ] && fx_ok=1
  if [ -f "$FIX/fictional-excerpts.md" ] && grep -q "Round 99 lapse note" "$FIX/fictional-excerpts.md"; then
    lapse=1
  else
    lapse=0
  fi
  if [ -f "$FIX/claim-excerpt-map.md" ] && grep -q "J21" "$FIX/claim-excerpt-map.md"; then
    map_ok=1
  fi
  if [ -f "$FIX/README.md" ] && grep -q "tick-15" "$FIX/README.md"; then
    readme_ok=1
  fi
  if [ -f "$KNOW/r99-lapse-scope-note.md" ] && [ -f "$KNOW/r99-gate-blind-spot-table.md" ]; then
    know_ok=1
  fi
  [ -f "$SEATS/S3-fixture-author.md" ] && s3=1
  # S4/S5 report names are not fixed; accept any S4*.md / S5*.md that is a file
  if ls "$SEATS"/S4*.md >/dev/null 2>&1; then s4=1; fi
  if ls "$SEATS"/S5*.md >/dev/null 2>&1; then s5=1; fi
  echo "try $i $ts fx=$fx_ok lapse=$lapse map=$map_ok readme=$readme_ok know=$know_ok S3=$s3 S4=$s4 S5=$s5" >> "$LOG"
  if [ "$lapse" = 1 ] && [ "$map_ok" = 1 ] && [ "$readme_ok" = 1 ] && [ "$know_ok" = 1 ] && [ "$s3" = 1 ] && [ "$s4" = 1 ] && [ "$s5" = 1 ]; then
    echo "ALL PRESENT try $i $ts" >> "$LOG"
    exit 0
  fi
  sleep 20
done
echo "ABSENT after $MAX tries $(date -Is)" >> "$LOG"
exit 2
