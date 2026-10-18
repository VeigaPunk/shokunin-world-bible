#!/bin/bash
# V120 verdict-summary poll. Artifact + producer reports + V28-V33 + crosschecks.
# ENDGAME: SELF is not in the wait set. Never verifies a plan.
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS="$LANE/.ufo/waves/round-99/seats"
SCRATCH="$SEATS/V120-scratch"
LOG="$SCRATCH/poll.log"
cd "$LANE" || exit 3

TARGETS=(
  V28-verdict-calibration.md
  V29-verdict-depth.md
  V30-verdict-coverage.md
  V31-verdict-operability.md
  V32-verdict-freshness.md
  V33-verdict-adjacency.md
  V51-crosscheck-depth.md
  V52-crosscheck-calibration.md
  V69-crosscheck-coverage-2.md
  V82-crosscheck-operability.md
  V91-crosscheck-freshness.md
  V107-crosscheck-adjacency.md
)
PRODUCERS=(
  S1-full-file-pins.md
  S2-tools-docs.md
  S3-fixture-author.md
  S4-fixture-docs.md
  S5-knowledge-author.md
)
ARTS=(
  corpus/fixtures/r99-window-lapse/README.md
  corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
  corpus/fixtures/r99-window-lapse/contradictions.json
  corpus/fixtures/r99-window-lapse/entities.json
  corpus/fixtures/r99-window-lapse/fictional-excerpts.md
  corpus/fixtures/r99-window-lapse/inspiration-note.md
  corpus/fixtures/r99-window-lapse/relations.json
  corpus/fixtures/r99-window-lapse/source-excerpt.md
  corpus/fixtures/r99-window-lapse/sources.json
  corpus/fixtures/r99-window-lapse/timeline.json
  corpus/knowledge/r99-gate-blind-spot-table.md
  corpus/knowledge/r99-lapse-scope-note.md
  corpus/tools/dependency_freeze.py
  corpus/tools/dependency-freeze-contract.json
  corpus/tools/README.md
  SKILL.md
)

echo "POLL_START $(date '+%Y-%m-%dT%H:%M:%S%z') self=V120 excluded" >> "$LOG"

landed() {
  local f="$1"
  [ -s "$f" ] || return 1
  # A report has landed when it carries a terminal bottom line, not a partial write.
  grep -q -E 'Bottom line|^\*\*PASS|^\*\*FAIL|^PASS |^FAIL |^INCONCLUSIVE|^ABSENT' "$f"
}

for i in $(seq 1 40); do
  ts=$(date '+%Y-%m-%dT%H:%M:%S%z')
  art_miss=0
  for a in "${ARTS[@]}"; do
    if [ ! -s "$a" ]; then
      art_miss=$((art_miss + 1))
    fi
  done
  prod_have=0
  prod_names=""
  for p in "${PRODUCERS[@]}"; do
    if [ -s "$SEATS/$p" ]; then
      prod_have=$((prod_have + 1))
      prod_names="$prod_names $p"
    fi
  done
  have=0
  miss=""
  sizes=""
  for t in "${TARGETS[@]}"; do
    f="$SEATS/$t"
    if landed "$f"; then
      have=$((have + 1))
      sz=$(wc -c < "$f" | tr -d ' ')
      sizes="$sizes $t:$sz"
    else
      if [ -e "$f" ]; then
        sz=$(wc -c < "$f" | tr -d ' ')
        miss="$miss $t(partial:$sz)"
      else
        miss="$miss $t"
      fi
    fi
  done
  echo "try=$i t=${ts} art_miss=$art_miss prod=$prod_have/5 verdicts=$have/12 miss=[$miss] prod_present=[$prod_names]" >> "$LOG"
  if [ "$have" -eq 12 ] && [ "$art_miss" -eq 0 ] && [ "$prod_have" -eq 5 ]; then
    echo "POLL_HIT try=$i elapsed=$(( (i-1)*20 ))s $(date '+%Y-%m-%dT%H:%M:%S%z')" >> "$LOG"
    echo "SIZES $sizes" >> "$LOG"
    echo POLL_HIT
    exit 0
  fi
  if [ "$i" -lt 40 ]; then
    sleep 20
  fi
done
echo "POLL_EXPIRE try=40 $(date '+%Y-%m-%dT%H:%M:%S%z') art_miss=$art_miss prod=$prod_have/5 verdicts=$have/12" >> "$LOG"
echo POLL_EXPIRE
exit 2
