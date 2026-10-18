#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  if [ -f corpus/tools/dependency_freeze.py ] && [ -f corpus/tools/dependency-freeze-contract.json ] && [ -f .ufo/waves/round-96/seats/Q3-dependency-freeze.md ]; then
    echo "READY after $i tries at $(date -Iseconds)"; exit 0
  fi
  sleep 20
done
echo "TIMEOUT after 40 tries at $(date -Iseconds)"
exit 1
