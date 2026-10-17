#!/bin/bash
# poll for Q4 completion: fixture timeline.json + Q4 producer report
cd /home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  fx=0; rp=0
  [ -f corpus/fixtures/r96-crossing-response/timeline.json ] && fx=1
  ls .ufo/waves/round-96/seats/Q4*.md >/dev/null 2>&1 && rp=1
  echo "try=$i fixture=$fx report=$rp $(date +%H:%M:%S)"
  if [ "$fx" = 1 ] && [ "$rp" = 1 ]; then echo "READY"; exit 0; fi
  sleep 20
done
echo "TIMEOUT"
exit 1
