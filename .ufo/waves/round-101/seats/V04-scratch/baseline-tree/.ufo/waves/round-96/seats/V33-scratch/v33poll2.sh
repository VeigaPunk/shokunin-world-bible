#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  if ls .ufo/waves/round-96/seats/Q3*.md >/dev/null 2>&1; then
    echo "Q3 REPORT READY after $i tries at $(date -Iseconds)"; ls -la .ufo/waves/round-96/seats/Q3*.md; exit 0
  fi
  sleep 20
done
echo "TIMEOUT after 40 tries at $(date -Iseconds)"; ls .ufo/waves/round-96/seats/ | grep -i q3 || echo "no Q3 report"
exit 1
