#!/bin/bash
# V87 scope-final poll-wait. Read-only. Records presence, never verifies a plan.
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS="$LANE/.ufo/waves/round-99/seats"
LOG="$SEATS/V87-scratch/poll.log"
MAX=40
SLEEP=20

producers_ready() {
  local missing=0
  for s in S1 S2 S3 S4 S5; do
    if [[ ! -s "$SEATS/${s}-report.md" && ! -s "$SEATS/${s}.md" ]]; then
      # accept either naming; also any file matching S*-*.md that is a report
      if ! compgen -G "$SEATS/${s}*.md" > /dev/null; then
        missing=1
      fi
    fi
  done
  # required producer artifacts (declaration ownership)
  local arts=(
    "$LANE/corpus/fixtures/r99-window-lapse/timeline.json"
    "$LANE/corpus/fixtures/r99-window-lapse/sources.json"
    "$LANE/corpus/fixtures/r99-window-lapse/entities.json"
    "$LANE/corpus/fixtures/r99-window-lapse/relations.json"
    "$LANE/corpus/fixtures/r99-window-lapse/contradictions.json"
    "$LANE/corpus/fixtures/r99-window-lapse/README.md"
    "$LANE/corpus/fixtures/r99-window-lapse/claim-excerpt-map.md"
    "$LANE/corpus/fixtures/r99-window-lapse/fictional-excerpts.md"
    "$LANE/corpus/fixtures/r99-window-lapse/inspiration-note.md"
    "$LANE/corpus/fixtures/r99-window-lapse/source-excerpt.md"
    "$LANE/corpus/knowledge/r99-gate-blind-spot-table.md"
    "$LANE/corpus/knowledge/r99-lapse-scope-note.md"
  )
  for a in "${arts[@]}"; do
    if [[ ! -s "$a" ]]; then
      missing=1
    fi
  done
  # S1/S2 tracked edits must exist as worktree diffs (not just baseline)
  if ! git -C "$LANE" diff --quiet -- corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json; then
    :
  else
    # both clean vs HEAD means S1 has not landed (or landed identically)
    missing=1
  fi
  return $missing
}

{
  echo "POLL-START $(date --iso-8601=seconds)"
  echo "HEAD $(git -C "$LANE" rev-parse HEAD)"
} >> "$LOG"

for i in $(seq 1 "$MAX"); do
  stamp=$(date --iso-8601=seconds)
  reports=$(find "$SEATS" -maxdepth 1 -name '*.md' -type f 2>/dev/null | wc -l)
  s_reports=$(find "$SEATS" -maxdepth 1 -name 'S*.md' -type f 2>/dev/null | wc -l)
  kb_table=0; kb_note=0
  [[ -s "$LANE/corpus/knowledge/r99-gate-blind-spot-table.md" ]] && kb_table=1
  [[ -s "$LANE/corpus/knowledge/r99-lapse-scope-note.md" ]] && kb_note=1
  fx=$(find "$LANE/corpus/fixtures/r99-window-lapse" -maxdepth 1 -type f 2>/dev/null | wc -l)
  tools_stat=$(git -C "$LANE" diff --stat -- corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json corpus/tools/README.md SKILL.md | tr '\n' ' ')
  echo "try=$i t=$stamp reports=$reports s_reports=$s_reports fixture_files=$fx kb_table=$kb_table kb_note=$kb_note tools=[$tools_stat]" >> "$LOG"
  if producers_ready; then
    echo "READY try=$i t=$stamp" >> "$LOG"
    echo READY
    exit 0
  fi
  if [[ "$i" -eq "$MAX" ]]; then
    echo "ABSENT try=$i t=$stamp" >> "$LOG"
    echo ABSENT
    exit 2
  fi
  sleep "$SLEEP"
done
