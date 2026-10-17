#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
log=.ufo/waves/round-95/seats/V59-scratch/watch.txt
for i in $(seq 1 110); do
  n=$(find .ufo/waves/round-95/seats -maxdepth 1 -name '*.md' -type f | wc -l)
  p1=$(stat -c '%Y %s' corpus/tools/map_obligations.py 2>/dev/null | md5sum | cut -c1-8)
  p2=$(stat -c '%Y %s' corpus/tools/map-obligations-contract.json 2>/dev/null | md5sum | cut -c1-8)
  p3=$(ls corpus/fixtures/r95-crossing-aftermath/ 2>/dev/null | md5sum | cut -c1-8)
  p4=$(ls corpus/fixtures/r95-crossing-aftermath/README.md corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md 2>/dev/null | wc -l)
  p5=$([ -e corpus/knowledge/r95-aftermath-scope-note.md ] && echo Y || echo N)
  echo "$(date +%H:%M:%S) reports=$n p1=$p1 p2=$p2 p3=$p3 p4files=$p4 p5=$p5" >> "$log"
  if [ "$n" -ge 63 ]; then echo "WATCH_HIT n=$n" >> "$log"; exit 0; fi
  sleep 30
done
echo "WATCH_TIMEOUT" >> "$log"
