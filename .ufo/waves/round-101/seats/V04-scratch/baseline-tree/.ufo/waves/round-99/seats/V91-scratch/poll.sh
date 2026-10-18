#!/bin/bash
# V91 verdict-crosscheck-freshness poll-wait. Artifact-based. Never verifies a plan.
# ENDGAME: subtract SELF. V32 is a comparison target, not a gate for starting
# independent measurement — but the final crosscheck requires V32's report.
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
SCRATCH="$LANE/.ufo/waves/round-99/seats/V91-scratch"
LOG="$SCRATCH/poll.log"
SEATS="$LANE/.ufo/waves/round-99/seats"
cd "$LANE"
echo "POLL_START $(date '+%Y-%m-%dT%H:%M:%S%z')" >> "$LOG"

artifact_ok() {
  local missing=0
  for f in \
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
    corpus/knowledge/r99-lapse-scope-note.md \
    corpus/tools/dependency_freeze.py \
    corpus/tools/dependency-freeze-contract.json
  do
    if [ ! -s "$f" ]; then
      missing=1
    fi
  done
  return $missing
}

reports_ok() {
  # Producer reports S1-S5. SELF (V91) is never in this set.
  local n
  n=$(find "$SEATS" -maxdepth 1 -type f -name 'S[1-5]*.md' | wc -l)
  [ "$n" -ge 5 ]
}

for i in $(seq 1 40); do
  ts=$(date '+%Y-%m-%dT%H:%M:%S%z')
  art=no
  rep=no
  v32=no
  if artifact_ok; then art=yes; fi
  if reports_ok; then rep=yes; fi
  if [ -s "$SEATS/V32-verdict-freshness.md" ]; then v32=yes; fi
  sreports=$(find "$SEATS" -maxdepth 1 -type f -name 'S[1-5]*.md' -printf '%f ' 2>/dev/null || true)
  freeze_sha=$(sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json 2>/dev/null | awk '{print substr($1,1,12)}' | tr '\n' ' ')
  echo "try=$i t=${ts} art=$art rep=$rep v32=$v32 sreports=[$sreports] freeze12=[$freeze_sha]" >> "$LOG"
  if [ "$art" = yes ] && [ "$rep" = yes ]; then
    echo "POLL_HIT try=$i elapsed=$(( (i-1)*20 ))s v32=$v32 $(date '+%Y-%m-%dT%H:%M:%S%z')" >> "$LOG"
    echo POLL_HIT
    exit 0
  fi
  sleep 20
done
echo "POLL_EXPIRE try=40 $(date '+%Y-%m-%dT%H:%M:%S%z')" >> "$LOG"
echo POLL_EXPIRE
exit 2
