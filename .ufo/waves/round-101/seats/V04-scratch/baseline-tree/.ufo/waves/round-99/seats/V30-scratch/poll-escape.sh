#!/bin/bash
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$LANE/.ufo/waves/round-99/seats
LOG=$SEATS/V30-scratch/poll-escape.log
TABLE=$LANE/corpus/knowledge/r99-gate-blind-spot-table.md
: > "$LOG"
i=0
while [ "$i" -lt 15 ]; do
  i=$((i + 1))
  ts=$(date '+%Y-%m-%d %H:%M:%S %z')
  s1=no; s5=no; table=no; scope=no
  f=$(ls $SEATS/S1-*.md 2>/dev/null | head -1)
  [ -n "${f:-}" ] && [ -s "$f" ] && s1=yes
  f=$(ls $SEATS/S5-*.md 2>/dev/null | head -1)
  [ -n "${f:-}" ] && [ -s "$f" ] && s5=yes
  [ -s "$TABLE" ] && table=yes
  [ -s "$LANE/corpus/knowledge/r99-lapse-scope-note.md" ] && scope=yes
  n=$(find "$SEATS" -maxdepth 1 -name '*.md' -type f | wc -l)
  echo "escape=$i ts=$ts s1=$s1 s5=$s5 table=$table scope=$scope seats_md=$n" | tee -a "$LOG"
  if [ "$s1" = yes ] && [ "$table" = yes ] && [ "$s5" = yes ]; then
    echo "HIT escape=$i ts=$ts" | tee -a "$LOG"
    exit 0
  fi
  [ "$i" -ge 15 ] && break
  sleep 20
done
echo "ESCAPE-EXPIRED after $i ts=$(date '+%Y-%m-%d %H:%M:%S %z')" | tee -a "$LOG"
exit 1
