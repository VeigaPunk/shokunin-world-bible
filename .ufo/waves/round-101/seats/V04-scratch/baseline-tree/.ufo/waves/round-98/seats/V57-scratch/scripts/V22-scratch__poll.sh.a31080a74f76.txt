#!/bin/bash
# V22 round-98 poll: artifact + producer-report watch (20s x 40 tries)
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
LOG=.ufo/waves/round-98/seats/V22-scratch/poll.log
for i in $(seq 1 40); do
  ts=$(date +%H:%M:%S)
  tools=$(git diff --name-only 9a3d648 -- corpus/tools/ | tr '\n' ',')
  know=$(git status --porcelain -uall -- corpus/knowledge/ | awk '{print $NF}' | tr '\n' ',')
  maprows=$(grep -c '^| J' corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md 2>/dev/null)
  reports=$(ls .ufo/waves/round-98/seats/*.md 2>/dev/null | xargs -n1 basename 2>/dev/null | tr '\n' ',')
  st=$(python3 corpus/tools/dependency_freeze.py --self-test >/tmp/v22-st.out 2>&1; echo $?)
  echo "try=$i $ts tools=[$tools] knowledge=[$know] map_Jrows=$maprows df_selftest_exit=$st reports=[$reports]" >> "$LOG"
  if [ -n "$tools" ] && [ "$maprows" -ge 20 ] 2>/dev/null && [ -n "$reports" ]; then
    echo "ALL-READY try=$i $ts" >> "$LOG"; break
  fi
  sleep 20
done
echo "POLL-DONE $(date +%H:%M:%S)" >> "$LOG"
