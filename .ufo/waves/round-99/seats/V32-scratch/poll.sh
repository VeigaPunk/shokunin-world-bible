#!/bin/bash
# V32 verdict-freshness poll-wait. Artifact-based. Never verifies a plan.
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
SCRATCH="$LANE/.ufo/waves/round-99/seats/V32-scratch"
LOG="$SCRATCH/poll.log"
SEATS="$LANE/.ufo/waves/round-99/seats"
cd "$LANE"
echo "POLL_START $(date '+%Y-%m-%dT%H:%M:%S%z')" >> "$LOG"

artifact_ok() {
  # Required durable artifacts for a freshness verdict on delivered bytes.
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
    corpus/knowledge/r99-lapse-scope-note.md
  do
    if [ ! -s "$f" ]; then
      missing=1
    fi
  done
  # Freeze pair must differ from r98 closure pins if C1 landed, but presence is enough to start.
  if [ ! -s corpus/tools/dependency_freeze.py ] || [ ! -s corpus/tools/dependency-freeze-contract.json ]; then
    missing=1
  fi
  return $missing
}

reports_ok() {
  # Producer reports. ENDGAME: subtract SELF (V32 is not a producer).
  local n
  n=$(find "$SEATS" -maxdepth 1 -type f -name 'S[1-5]*.md' | wc -l)
  [ "$n" -ge 5 ]
}

for i in $(seq 1 40); do
  ts=$(date '+%Y-%m-%dT%H:%M:%S%z')
  art=no
  rep=no
  if artifact_ok; then art=yes; fi
  if reports_ok; then rep=yes; fi
  sreports=$(find "$SEATS" -maxdepth 1 -type f -name 'S[1-5]*.md' -printf '%f ' 2>/dev/null || true)
  freeze_sha=$(sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json 2>/dev/null | awk '{print substr($1,1,12)}' | tr '\n' ' ')
  echo "try=$i t=${ts} art=$art rep=$rep sreports=[$sreports] freeze12=[$freeze_sha]" >> "$LOG"
  if [ "$art" = yes ] && [ "$rep" = yes ]; then
    echo "POLL_HIT try=$i elapsed=$(( (i-1)*20 ))s $(date '+%Y-%m-%dT%H:%M:%S%z')" >> "$LOG"
    echo POLL_HIT
    exit 0
  fi
  sleep 20
done
echo "POLL_EXPIRE try=40 $(date '+%Y-%m-%dT%H:%M:%S%z')" >> "$LOG"
echo POLL_EXPIRE
exit 2
