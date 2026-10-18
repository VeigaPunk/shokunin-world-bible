#!/bin/bash
# V23 poll continuation. 20s cadence, 25 more tries (total budget 40).
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
LOG="$ROOT/.ufo/waves/round-99/seats/V23-scratch/poll.log"
cd "$ROOT" || exit 1
for i in $(seq 16 40); do
  ts=$(date -Is)
  arts=0
  for f in \
    corpus/tools/dependency_freeze.py \
    corpus/tools/dependency-freeze-contract.json \
    corpus/tools/README.md \
    SKILL.md \
    corpus/fixtures/r99-window-lapse/README.md \
    corpus/fixtures/r99-window-lapse/claim-excerpt-map.md \
    corpus/fixtures/r99-window-lapse/contradictions.json \
    corpus/fixtures/r99-window-lapse/entities.json \
    corpus/fixtures/r99-window-lapse/fictional-excerpts.md \
    corpus/fixtures/r99-window-lapse/inspiration-note.md \
    corpus/fixtures/r99-window-lapse/relations.json \
    corpus/fixtures/r99-window-lapse/source-excerpt.md \
    corpus/fixtures/r99-window-lapse/sources.json \
    corpus/fixtures/r99-window-lapse/timeline.json \
    corpus/knowledge/r99-gate-blind-spot-table.md \
    corpus/knowledge/r99-lapse-scope-note.md
  do
    if [ -f "$f" ]; then arts=$((arts+1)); fi
  done
  srep=$(ls .ufo/waves/round-99/seats/S*.md 2>/dev/null | wc -l)
  allrep=$(ls .ufo/waves/round-99/seats/*.md 2>/dev/null | wc -l)
  porc=$(git status --porcelain -uall | wc -l)
  echo "try=$i ts=$ts arts=$arts/16 srep=$srep allrep=$allrep porcelain=$porc" | tee -a "$LOG"
  if [ "$arts" -eq 16 ] && [ "$srep" -ge 5 ]; then
    echo "READY try=$i" | tee -a "$LOG"
    exit 0
  fi
  sleep 20
done
echo "CAP arts/srep not ready" | tee -a "$LOG"
exit 2
