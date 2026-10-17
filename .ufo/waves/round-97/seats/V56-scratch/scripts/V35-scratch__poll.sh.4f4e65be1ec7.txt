#!/bin/bash
SEATS=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats
DEADLINE=$(( $(date +%s) + 10800 ))
while [ $(date +%s) -lt $DEADLINE ]; do
  N=$(ls "$SEATS"/*.md 2>/dev/null | grep -v 'V35-adjudicator.md' | wc -l)
  echo "$(date -Is) reports=$N/63"
  if [ "$N" -ge 63 ]; then echo "ALL_PRESENT"; exit 0; fi
  sleep 30
done
echo "DEADLINE_REACHED"
exit 1
