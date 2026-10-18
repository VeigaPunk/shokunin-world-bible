#!/bin/bash
# V15 content-aware poll for S3–S5. 20s cadence, 40 tries. Never treats r98-byte placeholders as delivered.
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS="$ROOT/.ufo/waves/round-99/seats"
FIX="$ROOT/corpus/fixtures/r99-window-lapse"
KNOW="$ROOT/corpus/knowledge"
LOG="$SEATS/V15-scratch/poll.log"
cd "$ROOT" || exit 2
echo "POLL_START $(date -Is)" >> "$LOG"
for try in $(seq 1 40); do
  miss=""
  # S3 content markers (not mere existence)
  grep -q 'clerk-lapse-note' "$FIX/sources.json" 2>/dev/null || miss="$miss sources"
  grep -q 'clerk-lapse-recorded' "$FIX/timeline.json" 2>/dev/null || miss="$miss timeline"
  grep -q 'Round 99 lapse note' "$FIX/fictional-excerpts.md" 2>/dev/null || miss="$miss excerpts"
  # S4 content markers — README/map must no longer be r98 placeholders
  grep -q 'r99-window-lapse' "$FIX/README.md" 2>/dev/null || miss="$miss readme"
  grep -q 'clerk-lapse' "$FIX/claim-excerpt-map.md" 2>/dev/null || miss="$miss map"
  # S5 artifacts
  test -s "$KNOW/r99-gate-blind-spot-table.md" || miss="$miss table"
  test -s "$KNOW/r99-lapse-scope-note.md" || miss="$miss note"
  # producer reports (any S3-/S4-/S5- prefix)
  compgen -G "$SEATS/S3-*.md" >/dev/null || miss="$miss S3rep"
  compgen -G "$SEATS/S4-*.md" >/dev/null || miss="$miss S4rep"
  compgen -G "$SEATS/S5-*.md" >/dev/null || miss="$miss S5rep"
  if [ -z "$miss" ]; then
    echo "ALL-PRESENT try=$try $(date -Is)" | tee -a "$LOG"
    exit 0
  fi
  echo "try=$try $(date +%H:%M:%S) missing:$miss" | tee -a "$LOG"
  if [ "$try" -lt 40 ]; then
    sleep 20
  fi
done
echo "ABSENT after 40 tries $(date -Is)" | tee -a "$LOG"
exit 1
