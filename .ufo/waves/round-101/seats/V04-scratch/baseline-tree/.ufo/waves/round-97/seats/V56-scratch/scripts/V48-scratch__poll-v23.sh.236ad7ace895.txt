#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
S=.ufo/waves/round-97/seats
for i in $(seq 1 40); do
  ts=$(date +%H:%M:%S)
  f=$(ls $S/V23-*.md 2>/dev/null | head -1)
  if [ -n "$f" ]; then echo "[$ts] try=$i FOUND $f"; ls -la "$f"; exit 0; fi
  sc=$(ls -d $S/V23-scratch 2>/dev/null)
  echo "[$ts] try=$i absent (v23 scratch: ${sc:-none})"
  sleep 20
done
echo "ABSENT after 40 tries"
exit 1
