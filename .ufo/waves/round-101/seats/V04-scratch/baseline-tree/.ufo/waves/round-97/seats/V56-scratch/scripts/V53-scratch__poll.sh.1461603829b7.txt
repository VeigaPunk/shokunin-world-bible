#!/bin/bash
D=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats
for i in $(seq 1 40); do
  n=$(ls "$D" 2>/dev/null | grep -c '\.md$')
  prod=$(ls "$D" 2>/dev/null | grep -E '^R[1-6]-.*\.md$' | wc -l)
  echo "try=$i t=$(date +%H:%M:%S) reports=$n producers=$prod"
  if [ "$prod" -ge 6 ] && [ "$n" -ge 20 ]; then echo "READY"; exit 0; fi
  sleep 20
done
echo "TIMEOUT reports=$n producers=$prod"; exit 1
