#!/bin/bash
# V60 poll-wait: table + S5 report. 20s cadence. Caller records start try.
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS="$ROOT/.ufo/waves/round-99/seats"
TABLE="$ROOT/corpus/knowledge/r99-gate-blind-spot-table.md"
LOG="$SEATS/V60-scratch/poll.log"
START=${1:-11}
MAX=${2:-40}
for i in $(seq "$START" "$MAX"); do
  ts=$(date -Iseconds)
  table_state="ABSENT"
  if [[ -f "$TABLE" ]]; then
    table_state="PRESENT $(stat -c '%s bytes mtime %y' "$TABLE")"
  fi
  s5=$(find "$SEATS" -maxdepth 1 -name 'S5*.md' -printf '%f %s\n' 2>/dev/null)
  s_all=$(find "$SEATS" -maxdepth 1 -name 'S*.md' -printf '%f %s\n' 2>/dev/null)
  {
    echo ""
    echo "=== $ts poll $i ==="
    echo "table: $table_state"
    echo "S5: ${s5:-ABSENT}"
    echo "producer reports:"
    echo "${s_all:-none}"
  } | tee -a "$LOG"
  if [[ -f "$TABLE" && -n "$s5" ]]; then
    echo "POLL_HIT try=$i" | tee -a "$LOG"
    exit 0
  fi
  if [[ "$i" -lt "$MAX" ]]; then
    sleep 20
  fi
done
echo "POLL_EXHAUSTED try=$MAX table_and_or_S5 still absent" | tee -a "$LOG"
exit 2
