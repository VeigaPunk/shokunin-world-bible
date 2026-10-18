#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
LOG=.ufo/waves/round-98/seats/V44-scratch/poll.log
: > "$LOG"
for i in $(seq 1 40); do
  ts=$(date -u +%H:%M:%SZ)
  S1=$( [ -f .ufo/waves/round-98/seats/S1-*.md ] 2>/dev/null && echo 1 || echo 0 )
  DF=$(git hash-object corpus/tools/dependency_freeze.py)
  DFC=$(git hash-object corpus/tools/dependency-freeze-contract.json)
  TR=$(git hash-object corpus/tools/README.md)
  R95=$(git hash-object corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md)
  S5=$(ls corpus/knowledge/r98-clerk-scope-note.md 2>/dev/null && echo 1 || echo 0)
  S5B=$(grep -l "correction" corpus/knowledge/r95-aftermath-scope-note.md corpus/knowledge/r96-response-scope-note.md 2>/dev/null | wc -l)
  reps=$(ls .ufo/waves/round-98/seats/S*.md 2>/dev/null | wc -l)
  echo "$ts try=$i df=$DF dfc=$DFC toolsreadme=$TR r95map=$R95 s5note=$S5 s5addenda=$S5B producer_reports=$reps" >> "$LOG"
  # done when S1 tool bytes changed AND r95 map changed AND s5 note exists AND producer reports >= 5
  if [ "$DF" != "001ad47390a04c4b20f17ac7fa0555c5175a506d" ] && [ "$R95" != "0000000000000000000000000000000000000000" ] && [ "$S5" = "1" ] && [ "$reps" -ge 5 ]; then
     echo "$ts ALL-PRESENT" >> "$LOG"; break
  fi
  sleep 20
done
echo "POLL-END $(date -u +%H:%M:%SZ)" >> "$LOG"
