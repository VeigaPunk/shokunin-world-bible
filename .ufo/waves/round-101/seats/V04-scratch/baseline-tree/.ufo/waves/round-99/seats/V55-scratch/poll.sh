#!/bin/sh
# V55 claim-text-audit poll. 20s cadence, max 40 tries.
# Artifacts AND producer reports. Content gates so a placeholder is not delivery.
# ENDGAME is not this poll: this waits for producers only.
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$LANE/.ufo/waves/round-99/seats
LOG=$SEATS/V55-scratch/poll.log
FIX=$LANE/corpus/fixtures/r99-window-lapse
: > "$LOG"
i=0
while [ "$i" -lt 40 ]; do
  i=$((i + 1))
  ts=$(date '+%Y-%m-%d %H:%M:%S %z')
  s1=no; s2=no; s3=no; s4=no; s5=no
  [ -s "$SEATS/S1-freeze-hygiene.md" ] && s1=yes
  [ -s "$SEATS/S2-tools-docs.md" ] && s2=yes
  [ -s "$SEATS/S3-fixture-author.md" ] && s3=yes
  [ -s "$SEATS/S4-fixture-docs.md" ] && s4=yes
  [ -s "$SEATS/S5-knowledge-notes.md" ] && s5=yes
  table=no; note=no
  [ -s "$LANE/corpus/knowledge/r99-gate-blind-spot-table.md" ] && table=yes
  [ -s "$LANE/corpus/knowledge/r99-lapse-scope-note.md" ] && note=yes
  ev=0; src=0; map21=0
  if [ -f "$FIX/timeline.json" ]; then
    ev=$(grep -c 'clerk-lapse-recorded' "$FIX/timeline.json" 2>/dev/null || true)
  fi
  if [ -f "$FIX/sources.json" ]; then
    src=$(grep -c 'clerk-lapse-note' "$FIX/sources.json" 2>/dev/null || true)
  fi
  if [ -f "$FIX/claim-excerpt-map.md" ]; then
    map21=$(grep -c 'clerk-lapse' "$FIX/claim-excerpt-map.md" 2>/dev/null || true)
  fi
  freeze_h=$(sha256sum "$LANE/corpus/tools/dependency_freeze.py" | awk '{print substr($1,1,12)}')
  contract_h=$(sha256sum "$LANE/corpus/tools/dependency-freeze-contract.json" | awk '{print substr($1,1,12)}')
  echo "try=$i ts=$ts s1=$s1 s2=$s2 s3=$s3 s4=$s4 s5=$s5 table=$table note=$note ev=$ev src=$src map21=$map21 freeze=$freeze_h contract=$contract_h" | tee -a "$LOG"
  if [ "$s1" = yes ] && [ "$s2" = yes ] && [ "$s3" = yes ] && [ "$s4" = yes ] && [ "$s5" = yes ] \
     && [ "$table" = yes ] && [ "$note" = yes ] && [ "$ev" -ge 1 ] && [ "$src" -ge 1 ] && [ "$map21" -ge 1 ]; then
    echo "HIT try=$i ts=$ts" | tee -a "$LOG"
    exit 0
  fi
  if [ "$i" -ge 40 ]; then
    break
  fi
  sleep 20
done
echo "ABSENT after $i tries ts=$(date '+%Y-%m-%d %H:%M:%S %z')" | tee -a "$LOG"
exit 1
