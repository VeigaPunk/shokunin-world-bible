#!/bin/bash
# V33 producer poll: artifacts AND producer reports. 20s cadence, max 40.
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS="$ROOT/.ufo/waves/round-99/seats"
LOG="$SEATS/V33-scratch/poll.log"
cd "$ROOT" || exit 1
echo "POLL_START $(date '+%Y-%m-%d %H:%M:%S %z')" >> "$LOG"
for i in $(seq 1 40); do
  arts=0
  missing=""
  for f in \
    corpus/tools/dependency_freeze.py \
    corpus/tools/dependency-freeze-contract.json \
    corpus/tools/README.md \
    SKILL.md \
    corpus/fixtures/r99-window-lapse/entities.json \
    corpus/fixtures/r99-window-lapse/relations.json \
    corpus/fixtures/r99-window-lapse/contradictions.json \
    corpus/fixtures/r99-window-lapse/timeline.json \
    corpus/fixtures/r99-window-lapse/sources.json \
    corpus/fixtures/r99-window-lapse/fictional-excerpts.md \
    corpus/fixtures/r99-window-lapse/README.md \
    corpus/fixtures/r99-window-lapse/claim-excerpt-map.md \
    corpus/fixtures/r99-window-lapse/inspiration-note.md \
    corpus/fixtures/r99-window-lapse/source-excerpt.md \
    corpus/knowledge/r99-gate-blind-spot-table.md \
    corpus/knowledge/r99-lapse-scope-note.md
  do
    if [ -f "$f" ]; then arts=$((arts+1)); else missing="$missing $f"; fi
  done
  reps=$(ls -1 "$SEATS"/S*-*.md 2>/dev/null | wc -l)
  snames=$(ls -1 "$SEATS"/S*-*.md 2>/dev/null | xargs -n1 basename 2>/dev/null | tr '\n' ' ')
  # hashes of mutable producer files so mid-flight churn is visible
  hpy=$(sha256sum corpus/tools/dependency_freeze.py 2>/dev/null | cut -c1-12)
  hct=$(sha256sum corpus/tools/dependency-freeze-contract.json 2>/dev/null | cut -c1-12)
  htl=$(sha256sum corpus/fixtures/r99-window-lapse/timeline.json 2>/dev/null | cut -c1-12)
  hsrc=$(sha256sum corpus/fixtures/r99-window-lapse/sources.json 2>/dev/null | cut -c1-12)
  hfx=$(sha256sum corpus/fixtures/r99-window-lapse/fictional-excerpts.md 2>/dev/null | cut -c1-12)
  hrd=$(sha256sum corpus/fixtures/r99-window-lapse/README.md 2>/dev/null | cut -c1-12)
  hmap=$(sha256sum corpus/fixtures/r99-window-lapse/claim-excerpt-map.md 2>/dev/null | cut -c1-12)
  htbl=$(sha256sum corpus/knowledge/r99-gate-blind-spot-table.md 2>/dev/null | cut -c1-12)
  hnote=$(sha256sum corpus/knowledge/r99-lapse-scope-note.md 2>/dev/null | cut -c1-12)
  echo "POLL t=$(date '+%H:%M:%S') try=$i arts=$arts/16 reps=$reps/5 py=$hpy ct=$hct tl=$htl src=$hsrc fx=$hfx rd=$hrd map=$hmap tbl=$htbl note=$hnote names=[$snames] missing=[$missing]" >> "$LOG"
  if [ "$arts" -eq 16 ] && [ "$reps" -ge 5 ]; then
    echo "ALL-PRESENT t=$(date '+%Y-%m-%d %H:%M:%S %z') try=$i" >> "$LOG"
    exit 0
  fi
  sleep 20
done
echo "TIMEOUT t=$(date '+%Y-%m-%d %H:%M:%S %z') arts=$arts reps=$reps" >> "$LOG"
exit 2
