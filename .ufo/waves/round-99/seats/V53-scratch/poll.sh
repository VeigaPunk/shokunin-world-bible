#!/bin/bash
# V53 poll-wait. 20s cadence, max 40 tries. Artifact-based; never verifies a plan.
# Endgame: all-reports check enumerates S1..S5 only (SELF=V53 subtracted).
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$ROOT/.ufo/waves/round-99/seats
LOG=$SEATS/V53-scratch/poll.log
FIX=$ROOT/corpus/fixtures/r99-window-lapse
cd "$ROOT" || exit 2
for i in $(seq 1 40); do
  ts=$(date +%H:%M:%S)
  miss=""
  for f in \
    corpus/tools/dependency_freeze.py \
    corpus/tools/dependency-freeze-contract.json \
    corpus/tools/README.md \
    SKILL.md \
    corpus/fixtures/r99-window-lapse/entities.json \
    corpus/fixtures/r99-window-lapse/relations.json \
    corpus/fixtures/r99-window-lapse/timeline.json \
    corpus/fixtures/r99-window-lapse/sources.json \
    corpus/fixtures/r99-window-lapse/contradictions.json \
    corpus/fixtures/r99-window-lapse/fictional-excerpts.md \
    corpus/fixtures/r99-window-lapse/inspiration-note.md \
    corpus/fixtures/r99-window-lapse/source-excerpt.md \
    corpus/fixtures/r99-window-lapse/README.md \
    corpus/fixtures/r99-window-lapse/claim-excerpt-map.md \
    corpus/knowledge/r99-gate-blind-spot-table.md \
    corpus/knowledge/r99-lapse-scope-note.md \
    .ufo/waves/round-99/seats/S1-freeze-hygiene.md \
    .ufo/waves/round-99/seats/S2-tools-docs.md \
    .ufo/waves/round-99/seats/S3-fixture-author.md \
    .ufo/waves/round-99/seats/S4-fixture-docs.md \
    .ufo/waves/round-99/seats/S5-knowledge-notes.md
  do
    if [ ! -s "$f" ]; then miss="$miss $f"; fi
  done
  # content-aware: fixture must not still be the r98 placeholder
  marker=""
  if [ -f "$FIX/README.md" ]; then
    if grep -q "window-lapse\|clerk-lapse\|tick-15\|lapse" "$FIX/README.md"; then
      marker="CONTENT-OK"
    else
      marker="PLACEHOLDER"
      miss="$miss CONTENT-PLACEHOLDER"
    fi
  fi
  # S reports must mention r99 content, not be empty stubs
  nfiles=$(ls -1 "$FIX" 2>/dev/null | wc -l)
  echo "try=$i ts=$ts files=$nfiles marker=$marker miss:${miss:- NONE}" >> "$LOG"
  if [ -z "$miss" ]; then
    echo "ALL PRESENT try=$i ts=$ts" >> "$LOG"
    exit 0
  fi
  sleep 20
done
echo "ABSENT after 40" >> "$LOG"
exit 1
