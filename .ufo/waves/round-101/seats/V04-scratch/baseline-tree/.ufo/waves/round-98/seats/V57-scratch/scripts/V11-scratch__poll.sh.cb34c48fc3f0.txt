#!/bin/sh
# V11 poll for S3+S4 (round 98). 20 s cadence, max 40 tries (~13 min).
FIX=/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r98-clerk-filing
R97=/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r97-crossing-acknowledgment
SEATS=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-98/seats
LOG=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-98/seats/V11-scratch/poll.log
i=1
while [ "$i" -le 40 ]; do
  ts=$(date +%H:%M:%S)
  r3=$(ls -p "$SEATS" | grep -E '^S3[^/]*\.md$' | head -1)
  r4=$(ls -p "$SEATS" | grep -E '^S4[^/]*\.md$' | head -1)
  [ -n "$r3" ] || r3=none
  [ -n "$r4" ] || r4=none
  if [ -f "$FIX/entities.json" ] && [ -f "$R97/entities.json" ]; then
    if cmp -s "$FIX/entities.json" "$R97/entities.json"; then e=same; else e=moved; fi
    if cmp -s "$FIX/timeline.json" "$R97/timeline.json"; then t=same; else t=moved; fi
    if cmp -s "$FIX/sources.json" "$R97/sources.json"; then s=same; else s=moved; fi
    if cmp -s "$FIX/claim-excerpt-map.md" "$R97/claim-excerpt-map.md"; then m=same; else m=moved; fi
  else
    e=absent; t=absent; s=absent; m=absent
  fi
  echo "try=$i t=$ts S3report=$r3 S4report=$r4 entities=$e timeline=$t sources=$s map=$m" >> "$LOG"
  if [ "$r3" != none ] && [ "$r4" != none ] && [ "$e" = moved ] && [ "$t" = moved ] && [ "$s" = moved ] && [ "$m" = moved ]; then
    echo "READY try=$i t=$ts S3report=$r3 S4report=$r4" >> "$LOG"
    exit 0
  fi
  sleep 20
  i=$((i+1))
done
echo "POLL_TERMINAL status=timeout tries=40" >> "$LOG"
exit 0
