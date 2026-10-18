#!/bin/bash
# poll for P1's delivered tool (md5 change vs baseline) + P1 report
cd /home/vgpnk/Projects/shokunin/lore-shokunin
BASE=882eeebdeb2ac6ea05a8cdb1afff7ba3
for i in $(seq 1 40); do
  NOW=$(md5sum corpus/tools/map_obligations.py | cut -d' ' -f1)
  REP=$(ls .ufo/waves/round-95/seats/P1*.md 2>/dev/null | head -1)
  echo "try=$i $(date +%H:%M:%S) tool_md5=$NOW report=${REP:-none}"
  if [ "$NOW" != "$BASE" ] && [ -n "$REP" ]; then echo "DELIVERED tool+report at try=$i"; exit 0; fi
  if [ "$NOW" != "$BASE" ] && [ $i -ge 20 ]; then echo "TOOL_ONLY delivered at try=$i"; exit 2; fi
  sleep 20
done
echo "TIMEOUT after 40 tries"; exit 1
