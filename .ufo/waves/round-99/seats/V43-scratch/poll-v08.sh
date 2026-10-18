#!/bin/sh
# V43 wait for V08's report only. Not an all-reports poll. 20s, 30 tries.
set -u
SEATS=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats
LOG=$SEATS/V43-scratch/poll-v08.log
: > "$LOG"
i=1
while [ "$i" -le 30 ]; do
  ts=$(date '+%H:%M:%S')
  report=$(ls -1 "$SEATS"/V08-*.md 2>/dev/null | head -1)
  report=${report:-none}
  echo "try=$i t=$ts report=$report" | tee -a "$LOG"
  if [ "$report" != none ]; then
    # one extra check so a mid-write report can finish
    sleep 20
    sha=$(sha256sum "$report" | awk '{print $1}')
    echo "V08_HIT try=$i report=$report sha=$sha" | tee -a "$LOG"
    exit 0
  fi
  i=$((i+1))
  if [ "$i" -le 30 ]; then
    sleep 20
  fi
done
echo "V08_ABSENT tries=30" | tee -a "$LOG"
exit 2
