#!/bin/bash
# V123 presence poll — read-only except this scratch log.
SEATS=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
LOG=$SEATS/V123-scratch/poll.log
MAX=${1:-40}
for i in $(seq 1 "$MAX"); do
  ts=$(date -Iseconds)
  reports=$(find "$SEATS" -maxdepth 1 -name '*.md' | wc -l)
  srep=$(find "$SEATS" -maxdepth 1 -name 'S*.md' | wc -l)
  vrep=$(find "$SEATS" -maxdepth 1 -name 'V*.md' | wc -l)
  dirs=$(find "$SEATS" -mindepth 1 -maxdepth 1 -type d | wc -l)
  arts=""
  for p in \
    corpus/tools/dependency_freeze.py \
    corpus/tools/dependency-freeze-contract.json \
    corpus/tools/README.md \
    SKILL.md \
    corpus/knowledge/r99-gate-blind-spot-table.md \
    corpus/knowledge/r99-lapse-scope-note.md \
    corpus/fixtures/r99-window-lapse/README.md \
    corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
  do
    if [ -f "$ROOT/$p" ]; then arts="${arts}Y"; else arts="${arts}N"; fi
  done
  v39=$(find "$SEATS" -maxdepth 1 -name 'V39-*.md' | wc -l)
  v99=$(find "$SEATS" -maxdepth 1 -name 'V99-*.md' | wc -l)
  v101=$(find "$SEATS" -maxdepth 1 -name 'V101-*.md' | wc -l)
  echo "$ts try=$i reports=$reports S=$srep V=$vrep dirs=$dirs arts=$arts V39=$v39 V99=$v99 V101=$v101" >> "$LOG"
  # early exit only after try 8 if all 128 reports exist (unlikely; keep polling to deadline unless caller says stop)
  if [ "$reports" -ge 128 ]; then
    echo "$ts try=$i FULL-128 exiting" >> "$LOG"
    exit 0
  fi
  sleep 20
done
echo "$(date -Iseconds) DEADLINE tries=$MAX" >> "$LOG"
