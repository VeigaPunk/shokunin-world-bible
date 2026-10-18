#!/bin/bash
# V87 poll continuation. Tries 16-40. Read-only. Appends to poll.log.
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS="$LANE/.ufo/waves/round-99/seats"
LOG="$SEATS/V87-scratch/poll.log"
SLEEP=20

producers_ready() {
  local missing=0
  for s in S1 S2 S3 S4 S5; do
    if ! compgen -G "$SEATS/${s}*.md" > /dev/null; then
      missing=1
    fi
  done
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
    [[ -s "$a" ]] || missing=1
  done
  if git -C "$LANE" diff --quiet -- corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json; then
    missing=1
  fi
  return $missing
}

echo "POLL-CONT-START $(date --iso-8601=seconds) note=first-window-killed-at-try15-by-host-timeout" >> "$LOG"

for i in $(seq 16 40); do
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
  if [[ "$i" -eq 40 ]]; then
    echo "ABSENT try=$i t=$stamp" >> "$LOG"
    echo ABSENT
    exit 2
  fi
  sleep "$SLEEP"
done
