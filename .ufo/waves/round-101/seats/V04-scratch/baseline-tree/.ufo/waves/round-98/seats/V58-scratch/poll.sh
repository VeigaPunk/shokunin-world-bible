#!/bin/bash
# V58 presence-final poll: wait until 63 non-SELF reports exist (64 incl SELF), bounded.
R=/home/vgpnk/Projects/shokunin/lore-shokunin
D=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-98/seats
LOG=$D/V58-scratch/poll.log
: > "$LOG"
for i in $(seq 1 90); do
  n=$(ls "$D"/*.md 2>/dev/null | grep -v '/V58-presence-final.md$' | wc -l)
  tot=$(ls "$D"/*.md 2>/dev/null | wc -l)
  echo "try $i $(date -u +%H:%M:%S) nonself=$n total=$tot" >> "$LOG"
  if [ "$n" -ge 63 ]; then echo "POLL-HIT nonself=$n total=$tot at try $i $(date -u +%H:%M:%S)" >> "$LOG"; exit 0; fi
  sleep 20
done
echo "POLL-TIMEOUT nonself=$(ls "$D"/*.md 2>/dev/null | grep -v '/V58-presence-final.md$' | wc -l) $(date -u +%H:%M:%S)" >> "$LOG"
exit 1
