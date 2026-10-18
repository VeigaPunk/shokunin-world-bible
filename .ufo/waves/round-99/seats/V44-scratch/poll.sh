#!/bin/bash
# V44 poll-wait: S5 table + S5 report. 20s cadence, 40 tries. Subtract SELF.
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
TABLE=$LANE/corpus/knowledge/r99-gate-blind-spot-table.md
NOTE=$LANE/corpus/knowledge/r99-lapse-scope-note.md
SEATS=$LANE/.ufo/waves/round-99/seats
LOG=$SEATS/V44-scratch/poll.log
echo "poll-start $(date -Iseconds)" | tee -a "$LOG"
for try in $(seq 1 40); do
  ts=$(date -Iseconds)
  table_state=absent
  note_state=absent
  [ -s "$TABLE" ] && table_state=present
  [ -s "$NOTE" ] && note_state=present
  reports=""
  for f in "$SEATS"/S5*.md; do
    [ -f "$f" ] || continue
    base=$(basename "$f")
    case "$base" in
      V44*) continue ;;
    esac
    reports="$reports $base"
  done
  reports=${reports# }
  [ -z "$reports" ] && reports=none
  line="try=$try t=$ts table=$table_state note=$note_state reports=$reports"
  echo "$line" | tee -a "$LOG"
  if [ "$table_state" = present ] && [ "$reports" != none ]; then
    echo "READY try=$try t=$ts" | tee -a "$LOG"
    exit 0
  fi
  sleep 20
done
echo "ABSENT after 40 tries t=$(date -Iseconds)" | tee -a "$LOG"
exit 2
