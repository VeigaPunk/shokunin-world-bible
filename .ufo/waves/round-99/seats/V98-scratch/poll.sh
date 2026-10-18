#!/bin/bash
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
LOG="$ROOT/.ufo/waves/round-99/seats/V98-scratch/poll.log"
cd "$ROOT" || exit 1
: > "$LOG"
for i in $(seq 1 40); do
  ts=$(date -Is)
  table=0; note=0; s5=0
  [ -f corpus/knowledge/r99-gate-blind-spot-table.md ] && table=1
  [ -f corpus/knowledge/r99-lapse-scope-note.md ] && note=1
  s5n=$(ls .ufo/waves/round-99/seats/S5*.md 2>/dev/null | wc -l)
  echo "try=$i ts=$ts table=$table note=$note s5reports=$s5n" | tee -a "$LOG"
  if [ "$table" -eq 1 ] && [ "$s5n" -ge 1 ]; then
    echo "READY try=$i" | tee -a "$LOG"
    exit 0
  fi
  sleep 20
done
echo "CAP table/s5 not ready" | tee -a "$LOG"
exit 2
