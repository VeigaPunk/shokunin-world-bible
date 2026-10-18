#!/usr/bin/env bash
# V47 poll-wait for V06's report (canonical negative matrix seat).
cd /home/vgpnk/Projects/shokunin/lore-shokunin
LOG=.ufo/waves/round-96/seats/V47-scratch/poll-v06.log
: > "$LOG"
for i in $(seq 1 40); do
  V06_REPORT=$(ls .ufo/waves/round-96/seats/V06-*.md 2>/dev/null | head -1)
  echo "try=$i v06_report=${V06_REPORT:-none}" >> "$LOG"
  if [ -n "$V06_REPORT" ]; then
    echo "READY try=$i v06_report=$V06_REPORT" >> "$LOG"
    exit 0
  fi
  sleep 20
done
echo "TIMEOUT v06_report=none" >> "$LOG"
exit 1
