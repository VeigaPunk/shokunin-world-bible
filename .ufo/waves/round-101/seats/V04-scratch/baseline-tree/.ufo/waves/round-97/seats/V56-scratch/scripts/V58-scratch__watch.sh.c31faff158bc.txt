#!/bin/sh
# V58 presence-final collection watcher, round 97.
# Logs HH:MM:SS=count every 20s; exits when 63 other-seat reports exist or deadline (1800s) hit.
SEATS=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats
LOG=$SEATS/V58-scratch/collection-curve.txt
s=0
while [ "$s" -le 1800 ]; do
  n=$(find "$SEATS" -maxdepth 1 -name '*.md' -type f ! -name 'V58-presence-final.md' | wc -l)
  printf '%s=%s\n' "$(date '+%H:%M:%S')" "$n" >> "$LOG"
  if [ "$n" -ge 63 ]; then echo "WATCH_HIT count=$n elapsed=${s}s" >> "$LOG"; exit 0; fi
  sleep 20; s=$((s+20))
done
n=$(find "$SEATS" -maxdepth 1 -name '*.md' -type f ! -name 'V58-presence-final.md' | wc -l)
echo "WATCH_DEADLINE count=$n elapsed=${s}s" >> "$LOG"
exit 0
