#!/bin/bash
# V43 receipt seat — presence poll loop for round-96 seats.
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-96/seats
PARENT=/home/vgpnk/Projects/shokunin/.ufo/waves/round-96
LOG=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-96/seats/V43-scratch/V43-poll.log
MAXTRIES=330
i=0
prev=-1
stall=0
while [ $i -lt $MAXTRIES ]; do
  i=$((i+1))
  lane=$(ls "$LANE"/*.md 2>/dev/null | wc -l)
  parentn=$(find "$PARENT" -name '*.md' 2>/dev/null | wc -l)
  echo "$(date +%H:%M:%S) try=$i lane=$lane parent_tree_md=$parentn" >> "$LOG"
  if [ "$lane" -ge 64 ]; then
    echo "$(date +%H:%M:%S) DONE lane=$lane reached 64" >> "$LOG"
    exit 0
  fi
  if [ "$lane" -eq "$prev" ]; then
    stall=$((stall+1))
  else
    stall=0
  fi
  prev=$lane
  if [ "$stall" -ge 45 ] && [ "$lane" -ge 62 ]; then
    echo "$(date +%H:%M:%S) STALL lane=$lane unchanged for 45 tries (>=62 present); exiting" >> "$LOG"
    exit 0
  fi
  sleep 20
done
echo "$(date +%H:%M:%S) CAP reached tries=$MAXTRIES lane=$(ls "$LANE"/*.md 2>/dev/null | wc -l)" >> "$LOG"
