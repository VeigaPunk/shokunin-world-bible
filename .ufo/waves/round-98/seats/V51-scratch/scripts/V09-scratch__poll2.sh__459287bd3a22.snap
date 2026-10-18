#!/bin/bash
# V09 round-98 poll #2 (strong gate): S3 report + r98 map obligations 20/20 PASS.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
LOG=.ufo/waves/round-98/seats/V09-scratch/poll2.log
: > "$LOG"
for i in $(seq 1 40); do
  missing=""
  ls .ufo/waves/round-98/seats/S3-*.md >/dev/null 2>&1 || missing="$missing S3:report"
  out=$(python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing 2>&1)
  if ! echo "$out" | grep -q "raw=20 mapped=20"; then missing="$missing map:20/20"; fi
  if ! echo "$out" | grep -q "RESULT PASS"; then missing="$missing map:PASS"; fi
  reports=$(ls .ufo/waves/round-98/seats/ 2>/dev/null | grep -cE '^S[0-9].*\.md$')
  echo "$(date +%H:%M:%S) try=$i missing[$missing ] producer_reports_md=$reports" >> "$LOG"
  if [ -z "$missing" ]; then echo "POLL-DONE try=$i" >> "$LOG"; exit 0; fi
  sleep 20
done
echo "POLL-TIMEOUT" >> "$LOG"
exit 1
