#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
TOOL=corpus/tools/map_obligations.py
for i in $(seq 1 40); do
  p1=$(ls .ufo/waves/round-95/seats/P1-*.md 2>/dev/null | wc -l)
  mark=$(grep -c "LEGACY_POINTER\|schema_drift" "$TOOL" 2>/dev/null)
  echo "try=$i P1_report=$p1 markers=$mark $(date +%T)"
  if [ "$p1" -ge 1 ]; then echo P1_LANDED; exit 0; fi
  sleep 20
done
echo CUTOFF; exit 1
