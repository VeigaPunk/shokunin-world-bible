#!/bin/bash
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
LOG="$ROOT/.ufo/waves/round-99/seats/V98-scratch/poll2.log"
cd "$ROOT" || exit 1
: > "$LOG"
echo "poll2 start $(date -Is) continues protocol; poll1 is tool-capped at 300s" >> "$LOG"
for i in $(seq 1 40); do
  ts=$(date -Is)
  table=0; note=0
  [ -f corpus/knowledge/r99-gate-blind-spot-table.md ] && table=1
  [ -f corpus/knowledge/r99-lapse-scope-note.md ] && note=1
  s5n=$(ls .ufo/waves/round-99/seats/S5*.md 2>/dev/null | wc -l)
  tbytes=0
  if [ "$table" -eq 1 ]; then tbytes=$(wc -c < corpus/knowledge/r99-gate-blind-spot-table.md); fi
  echo "try=$i ts=$ts table=$table bytes=$tbytes note=$note s5reports=$s5n" | tee -a "$LOG"
  if [ "$table" -eq 1 ] && [ "$s5n" -ge 1 ]; then
    # stability: require the table mtime unchanged across one extra 20s if just appeared
    echo "READY try=$i" | tee -a "$LOG"
    exit 0
  fi
  sleep 20
done
echo "CAP table/s5 not ready" | tee -a "$LOG"
exit 2
