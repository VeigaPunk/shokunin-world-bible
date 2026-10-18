#!/usr/bin/env bash
# V42 poll-wait: artifacts + producer reports; 20s cadence, max 40 tries.
cd /home/vgpnk/Projects/shokunin/lore-shokunin
LOG=.ufo/waves/round-98/seats/V42-scratch/V42-poll.log
: > "$LOG"
for i in $(seq 1 40); do
  missing=()
  [ -f corpus/tools/dependency_freeze.py ] || missing+=("depfreeze")
  grep -q '"r98-clerk-filing"' corpus/tools/dependency-freeze-contract.json 2>/dev/null || missing+=("pin-r98")
  grep -q '"r97-crossing-acknowledgment"' corpus/tools/dependency-freeze-contract.json 2>/dev/null || missing+=("pin-r97")
  head -1 corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md 2>/dev/null | grep -q '^# r98' || missing+=("map-r98")
  grep -q 'r98' corpus/fixtures/r98-clerk-filing/README.md 2>/dev/null || missing+=("readme-r98")
  for s in S1 S2 S3 S4 S5; do
    ls .ufo/waves/round-98/seats/${s}*.md >/dev/null 2>&1 || missing+=("REPORT:$s")
  done
  if [ ${#missing[@]} -eq 0 ]; then
    echo "try $i $(date +%H:%M:%S) ALL PRESENT" >> "$LOG"; break
  fi
  echo "try $i $(date +%H:%M:%S) missing: ${missing[*]}" >> "$LOG"
  sleep 20
done
echo "poll done $(date +%H:%M:%S)" >> "$LOG"
