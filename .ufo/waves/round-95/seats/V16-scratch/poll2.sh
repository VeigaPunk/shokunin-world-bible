#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  rep=$(ls .ufo/waves/round-95/seats/P1-*.md 2>/dev/null | wc -l)
  python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath > .ufo/waves/round-95/seats/V16-scratch/live-probe.out 2>&1
  code=$?
  sha=$(sha256sum corpus/tools/map_obligations.py | cut -d' ' -f1 | cut -c1-12)
  echo "try=$i report=$rep live_exit=$code toolsha=$sha $(date +%T)"
  if [ "$rep" -ge 1 ] && [ "$code" = 0 ]; then echo READY2; exit 0; fi
  sleep 20
done
echo CUTOFF2; exit 1
