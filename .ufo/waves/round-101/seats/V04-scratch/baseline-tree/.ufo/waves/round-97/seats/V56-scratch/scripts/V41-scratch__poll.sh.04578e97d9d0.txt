#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  nfiles=$(find corpus/fixtures/r97-crossing-acknowledgment -maxdepth 1 -type f 2>/dev/null | wc -l)
  reps=$(ls .ufo/waves/round-97/seats/R[1-6]*.md 2>/dev/null | wc -l)
  echo "try=$i files=$nfiles producer_reports=$reps $(date +%H:%M:%S)"
  if [ "$nfiles" -ge 10 ] && [ "$reps" -ge 6 ]; then
    echo "POLL_OK try=$i files=$nfiles producer_reports=$reps"
    exit 0
  fi
  sleep 20
done
echo "POLL_TIMEOUT files=$nfiles producer_reports=$reps"
exit 1
