#!/bin/bash
# V18 poll: wait for 19 non-V18 reports + 3 producer artifacts (max 40 tries x 20s)
SEATS=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-102/seats
KNOW=/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/knowledge
for i in $(seq 41 100); do
  ts=$(date -u +%H:%M:%S)
  if [ -d "$SEATS" ]; then
    n=$(ls "$SEATS"/*.md 2>/dev/null | grep -v 'V18-adjudicator' | wc -l)
    arts=""
    [ -f "$KNOW/r102-push-synthesis-r95-r102.md" ] && arts="$arts C1"
    [ -f "$KNOW/r102-debt-ledger.json" ] && arts="$arts C2"
    [ -f "$KNOW/r102-freshness-sweep.md" ] && arts="$arts C3"
    echo "try $i $ts reports=$n artifacts:${arts:-none}"
    if [ "$n" -ge 19 ] && [ "${#arts}" -eq 9 ]; then
      echo "COMPLETE at try $i: 19 reports + C1+C2+C3"
      exit 0
    fi
  else
    echo "try $i $ts no seats dir yet"
  fi
  sleep 20
done
echo "POLLPATH exhausted: 40 tries, reports=$n artifacts:${arts:-none}"
exit 1
