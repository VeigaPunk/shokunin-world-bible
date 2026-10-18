#!/bin/bash
# V24 artifact/report first-seen watcher — round 97. 20s cadence, 70 min cap.
SEATS=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats
REPO=/home/vgpnk/Projects/shokunin/lore-shokunin
LOG=$SEATS/V24-scratch/artifacts.log
cd "$REPO" || exit 1
PATHS="corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json corpus/tools/README.md corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json corpus/fixtures/r96-crossing-response/claim-excerpt-map.md corpus/fixtures/r97-crossing-acknowledgment corpus/knowledge/r97-acknowledgment-scope-note.md"
s=0
echo "$(date '+%F %H:%M:%S') WATCH_START" >> "$LOG"
while [ $s -lt 4200 ]; do
  ts=$(date '+%H:%M:%S')
  for p in $PATHS; do
    if [ -e "$p" ]; then
      sig=$(stat -c '%Y:%s' "$p" 2>/dev/null)
      grep -q "FIRST $p " "$LOG" 2>/dev/null || echo "$ts FIRST $p sig=$sig" >> "$LOG"
    fi
  done
  for f in "$SEATS"/R[1-6]-*.md "$SEATS"/V[0-9][0-9]-*.md; do
    [ -e "$f" ] || continue
    b=$(basename "$f")
    grep -q "REPORT $b " "$LOG" 2>/dev/null || echo "$ts REPORT $b sig=$(stat -c '%Y:%s' "$f")" >> "$LOG"
  done
  sleep 20; s=$((s+20))
done
echo "$(date '+%F %H:%M:%S') WATCH_CAP" >> "$LOG"
