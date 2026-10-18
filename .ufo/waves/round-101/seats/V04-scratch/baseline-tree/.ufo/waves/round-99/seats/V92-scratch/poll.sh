#!/bin/bash
# V92 poll-wait. 20s cadence, max 40 tries. Never verify a plan.
# Gate: V50 report (the quoted-output source) + S1-S5 reports + C1/C2 artifacts.
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS="$ROOT/.ufo/waves/round-99/seats"
LOG="$SEATS/V92-scratch/poll.log"
cd "$ROOT" || exit 1

for try in $(seq 1 40); do
  ts=$(date '+%H:%M:%S')
  missing=""
  present=""
  for s in S1 S2 S3 S4 S5 V50; do
    hit=$(find "$SEATS" -maxdepth 1 -type f -name "${s}*.md" 2>/dev/null | head -1)
    if [ -z "$hit" ]; then
      missing="$missing REPORT:$s"
    else
      present="$present $s"
    fi
  done
  for art in \
    corpus/tools/dependency_freeze.py \
    corpus/tools/dependency-freeze-contract.json \
    corpus/fixtures/r99-window-lapse/timeline.json \
    corpus/fixtures/r99-window-lapse/sources.json \
    corpus/fixtures/r99-window-lapse/fictional-excerpts.md \
    corpus/fixtures/r99-window-lapse/README.md \
    corpus/fixtures/r99-window-lapse/claim-excerpt-map.md \
    corpus/knowledge/r99-gate-blind-spot-table.md \
    corpus/knowledge/r99-lapse-scope-note.md
  do
    if [ ! -f "$ROOT/$art" ]; then
      missing="$missing ART:$(basename "$art")"
    fi
  done
  nrep=$(find "$SEATS" -maxdepth 1 -type f -name '*.md' | wc -l)
  echo "try $try $ts reports=$nrep present=[$present] missing:$missing" >> "$LOG"
  if [ -z "$missing" ]; then
    echo "ALL-PRESENT try $try $ts" >> "$LOG"
    echo "ALL-PRESENT try $try $ts"
    exit 0
  fi
  sleep 20
done
echo "TIMEOUT after 40" >> "$LOG"
echo "TIMEOUT"
exit 2
