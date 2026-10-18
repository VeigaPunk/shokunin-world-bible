#!/bin/bash
SEATS=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats
for i in $(seq 1 40); do
  if ls $SEATS/R3-*.md >/dev/null 2>&1; then
    echo "R3 READY at try $i $(date -Is)"; ls $SEATS/R3-*.md; exit 0
  fi
  echo "try $i: R3 report not ready $(date -Is)"
  sleep 20
done
echo "TIMEOUT"; exit 1
