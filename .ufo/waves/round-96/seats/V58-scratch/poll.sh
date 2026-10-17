#!/bin/sh
# V58 presence-final poll: exit when >=63 non-V58 seat reports exist under seats/.
# 20s cadence, logs a curve line every 60s.
S=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-96/seats
L=$S/V58-scratch/poll.log
i=0
: > "$L"
while [ "$i" -lt 270 ]; do
  n=$(ls "$S"/*.md 2>/dev/null | sed 's|.*/||' | grep -cE '^(Q[1-6]|V[0-9]{2})-.*\.md$' || true)
  others=$((n))
  # subtract self if present
  if [ -f "$S/V58-presence-final.md" ]; then others=$((n-1)); fi
  if [ $((i % 3)) -eq 0 ]; then echo "$(date +%H:%M:%S) total=$n others=$others i=$i" >> "$L"; fi
  if [ "$others" -ge 63 ]; then
    echo "$(date +%H:%M:%S) POLL_HIT total=$n others=$others i=$i" >> "$L"
    echo "POLL_HIT others=$others total=$n"
    exit 0
  fi
  sleep 20
  i=$((i+1))
done
echo "$(date +%H:%M:%S) POLL_DEADLINE total=$n others=$others i=$i" >> "$L"
echo "POLL_DEADLINE others=$others total=$n"
exit 0
