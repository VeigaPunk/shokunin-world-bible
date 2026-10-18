#!/bin/bash
# V31 adjudicator poll: all 63 other seat reports + producer artifacts
R=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$R/.ufo/waves/round-98/seats
LOG=$R/.ufo/waves/round-98/scratch/V31/poll.log
for i in $(seq 1 240); do
  n=$(ls "$S"/*.md 2>/dev/null | grep -v "V31-adjudicator" | wc -l)
  arts=""
  [ -f "$R/corpus/fixtures/r98-clerk-filing/timeline.json" ] || arts="$arts fixture-timeline"
  m=$(md5sum "$R/corpus/tools/dependency_freeze.py" 2>/dev/null | cut -d' ' -f1)
  [ "$m" = "b59c3be9ea45173a7524bcda4d2fa71c" ] && arts="$arts dep-freeze-unchanged"
  echo "try $i $(date -u +%H:%M:%S) reports=$n arts:$arts" >> "$LOG"
  if [ "$n" -ge 63 ]; then echo "ALL-REPORTS at try $i $(date -u +%H:%M:%S) n=$n" >> "$LOG"; exit 0; fi
  sleep 20
done
echo "POLL-TIMEOUT after 240 tries $(date -u +%H:%M:%S) n=$(ls "$S"/*.md 2>/dev/null | grep -v V31 | wc -l)" >> "$LOG"
