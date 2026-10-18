#!/bin/bash
# V27 poll: 20s cadence, 40 tries max. Logs artifact + report state each try.
L=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$L/.ufo/waves/round-98/seats
F=$L/corpus/fixtures/r98-clerk-filing
LOG=$S/V27-scratch/poll.log
: > "$LOG"
for i in $(seq 1 40); do
  ts=$(date +%H:%M:%S)
  nf=$(ls "$F" 2>/dev/null | wc -l)
  reports=$(ls "$S"/*.md 2>/dev/null | xargs -n1 basename 2>/dev/null | tr '\n' ',')
  echo "$ts try=$i fixture_files=$nf reports=[$reports]" >> "$LOG"
  if [ "$nf" -ge 10 ] && [ -n "$reports" ]; then
    echo "$ts PRODUCERS_PRESENT try=$i" >> "$LOG"
  fi
  if [ "$nf" -ge 10 ]; then
    echo "$ts FIXTURE_PRESENT try=$i" >> "$LOG"
  fi
  sleep 20
done
echo "TIMEOUT" >> "$LOG"
exit 0
