#!/bin/bash
# V37 verdict-adjacency poll-wait: wait for V31 report + producer reports
SEATS=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-96/seats
LOG=$SEATS/V37-scratch/poll.log
for i in $(seq 1 40); do
  echo "=== try $i $(date '+%H:%M:%S') ===" >> "$LOG"
  ls -la "$SEATS" | grep -E 'V31|Q[1-6]-' >> "$LOG" 2>&1
  V31=$(ls "$SEATS"/V31-*.md 2>/dev/null | head -1)
  QS=$(ls "$SEATS"/Q[1-6]-*.md 2>/dev/null | wc -l)
  echo "V31=[$V31] producer_reports=$QS" >> "$LOG"
  if [ -n "$V31" ] && [ "$QS" -ge 6 ]; then
    echo "READY at try $i $(date '+%H:%M:%S')" >> "$LOG"
    exit 0
  fi
  sleep 20
done
echo "TIMEOUT $(date '+%H:%M:%S')" >> "$LOG"
exit 1
