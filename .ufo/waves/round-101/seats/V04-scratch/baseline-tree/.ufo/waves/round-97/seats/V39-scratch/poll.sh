#!/bin/bash
# V39 poll: producer artifacts + reports. 20s cadence, up to 40 tries.
cd /home/vgpnk/Projects/shokunin/lore-shokunin
LOG=.ufo/waves/round-97/seats/V39-scratch/poll.log
: > "$LOG"
for i in $(seq 1 40); do
  ts=$(date +%H:%M:%S)
  r1=$(ls corpus/tools/map_obligations.py >/dev/null 2>&1 && git diff --stat f3e09f9 -- corpus/tools/map_obligations.py | wc -l)
  r2=$(git diff --stat f3e09f9 -- corpus/tools/map-obligations-contract.json corpus/tools/README.md | wc -l)
  r3=$(git diff --stat f3e09f9 -- corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json | wc -l)
  r4=$(git diff --stat f3e09f9 -- corpus/fixtures/r96-crossing-response/claim-excerpt-map.md | wc -l; ls corpus/fixtures/r97-crossing-acknowledgment/ 2>/dev/null | wc -l)
  r5=$(ls corpus/fixtures/r97-crossing-acknowledgment/README.md corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md 2>/dev/null | wc -l)
  r6=$(ls corpus/knowledge/r97-acknowledgment-scope-note.md 2>/dev/null | wc -l)
  reps=$(ls .ufo/waves/round-97/seats/R[1-6]*.md 2>/dev/null | wc -l)
  echo "$ts try=$i diff1=$r1 diff2=$r2 diff3=$r3 r96map+r97dir=$r4 r5=$r5 r6=$r6 Rreports=$reps" >> "$LOG"
  if [ "$r1" -gt 0 ] && [ "$r2" -gt 0 ] && [ "$r3" -gt 0 ] && [ "$r4" -gt 1 ] && [ "$r5" -eq 2 ] && [ "$r6" -eq 1 ] && [ "$reps" -ge 6 ]; then
    echo "$ts ALL-PRESENT" >> "$LOG"; exit 0
  fi
  sleep 20
done
echo "$(date +%H:%M:%S) POLL-TIMEOUT" >> "$LOG"
