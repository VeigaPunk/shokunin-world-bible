#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  reps=$(ls .ufo/waves/round-97/seats/R[1-6]*.md 2>/dev/null | wc -l)
  python3 corpus/tools/map_obligations.py corpus/fixtures/r97-crossing-acknowledgment >/dev/null 2>&1
  mapexit=$?
  nfiles=$(find corpus/fixtures/r97-crossing-acknowledgment -maxdepth 1 -type f 2>/dev/null | wc -l)
  echo "try=$i reports=$reps map_exit=$mapexit r97_files=$nfiles $(date +%H:%M:%S)"
  if [ "$reps" -ge 6 ] && [ "$mapexit" = 0 ]; then
    echo "POLL2_OK try=$i reports=$reps map_exit=$mapexit"
    exit 0
  fi
  sleep 20
done
echo "POLL2_TIMEOUT reports=$reps map_exit=$mapexit"
exit 1
