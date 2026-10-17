#!/bin/bash
# V52 poll-wait: producers R1..R6 reports + r97 map no longer an r96 copy
cd /home/vgpnk/Projects/shokunin/lore-shokunin
LOG=.ufo/waves/round-97/seats/V52-scratch/poll.log
: > $LOG
for i in $(seq 1 40); do
  ts=$(date +%H:%M:%S)
  reports=$(ls .ufo/waves/round-97/seats/R*.md 2>/dev/null | wc -l)
  mapdiff=no
  cmp -s corpus/fixtures/r96-crossing-response/claim-excerpt-map.md corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md 2>/dev/null || mapdiff=yes
  echo "$ts try=$i producer_reports=$reports r97map_changed=$mapdiff" >> $LOG
  if [ "$reports" -ge 6 ] && [ "$mapdiff" = yes ]; then echo "$ts READY" >> $LOG; exit 0; fi
  sleep 20
done
echo "$(date +%H:%M:%S) TIMEOUT" >> $LOG
