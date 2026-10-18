#!/bin/bash
# V51 poll-wait: artifacts + producer reports + V29. 20s cadence, 40 tries.
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
SCRATCH="$ROOT/.ufo/waves/round-99/seats/V51-scratch"
SEATS="$ROOT/.ufo/waves/round-99/seats"
LOG="$SCRATCH/poll.log"
cd "$ROOT" || exit 1
for i in $(seq 0 39); do
  ts=$(date '+%Y-%m-%dT%H:%M:%S%z')
  fx=$(ls -1 corpus/fixtures/r99-window-lapse 2>/dev/null | wc -l)
  kn=$(ls -1 corpus/knowledge/r99-gate-blind-spot-table.md corpus/knowledge/r99-lapse-scope-note.md 2>/dev/null | wc -l)
  s3=$(ls -1 "$SEATS"/S3-*.md 2>/dev/null | tr '\n' ',')
  s4=$(ls -1 "$SEATS"/S4-*.md 2>/dev/null | tr '\n' ',')
  s5=$(ls -1 "$SEATS"/S5-*.md 2>/dev/null | tr '\n' ',')
  s1=$(ls -1 "$SEATS"/S1-*.md 2>/dev/null | tr '\n' ',')
  s2=$(ls -1 "$SEATS"/S2-*.md 2>/dev/null | tr '\n' ',')
  v29=$(ls -1 "$SEATS"/V29-*.md 2>/dev/null | tr '\n' ',')
  map_id=$(sha256sum corpus/fixtures/r99-window-lapse/claim-excerpt-map.md 2>/dev/null | cut -c1-12)
  readme_id=$(sha256sum corpus/fixtures/r99-window-lapse/README.md 2>/dev/null | cut -c1-12)
  excerpts_id=$(sha256sum corpus/fixtures/r99-window-lapse/fictional-excerpts.md 2>/dev/null | cut -c1-12)
  j21=$(grep -c 'J21' corpus/fixtures/r99-window-lapse/claim-excerpt-map.md 2>/dev/null || echo 0)
  seat_md=$(ls -1 "$SEATS"/*.md 2>/dev/null | wc -l)
  echo "POLL $ts try=$i fx=$fx kn=$kn S1=${s1:-ABSENT} S2=${s2:-ABSENT} S3=${s3:-ABSENT} S4=${s4:-ABSENT} S5=${s5:-ABSENT} V29=${v29:-ABSENT} map=$map_id readme=$readme_id excerpts=$excerpts_id j21=$j21 seat_md=$seat_md" >> "$LOG"
  # content gate: map no longer r98 placeholder AND knowledge notes present AND V29 present
  if [ "$map_id" != "c1099d0ee9ee" ] && [ "$kn" -ge 2 ] && [ -n "${v29:-}" ] && [ -n "${s3:-}" ] && [ -n "${s4:-}" ] && [ -n "${s5:-}" ]; then
    echo "POLL-SATISFIED $ts try=$i" >> "$LOG"
    exit 0
  fi
  sleep 20
done
echo "POLL-EXHAUSTED $(date '+%Y-%m-%dT%H:%M:%S%z')" >> "$LOG"
exit 2
