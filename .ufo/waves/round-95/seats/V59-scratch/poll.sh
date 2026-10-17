#!/bin/bash
# V59 presence-final poll: count seat reports (.md directly in seats/, excluding scratch dirs)
cd /home/vgpnk/Projects/shokunin/lore-shokunin
log=.ufo/waves/round-95/seats/V59-scratch/collection-curve.txt
i=0
while [ $i -lt 120 ]; do
  n=$(find .ufo/waves/round-95/seats -maxdepth 1 -name '*.md' -type f | wc -l)
  echo "$(date +%H:%M:%S)=$n" >> "$log"
  if [ "$n" -ge 63 ]; then echo "POLL_HIT n=$n tries=$i"; exit 0; fi
  sleep 20; i=$((i+1))
done
n=$(find .ufo/waves/round-95/seats -maxdepth 1 -name '*.md' -type f | wc -l)
echo "POLL_TIMEOUT n=$n tries=$i"
