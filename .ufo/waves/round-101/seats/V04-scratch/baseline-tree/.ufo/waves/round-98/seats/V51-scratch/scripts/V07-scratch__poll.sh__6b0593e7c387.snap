#!/bin/bash
# V07 poll: artifact (contract change + r98 fixture) AND producer report (S1)
cd /home/vgpnk/Projects/shokunin/lore-shokunin
BASE=27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781
LOG=.ufo/waves/round-98/seats/V07-scratch/poll.log
: > "$LOG"
for i in $(seq 1 40); do
  TS=$(date +%H:%M:%S)
  CUR=$(sha256sum corpus/tools/dependency-freeze-contract.json 2>/dev/null | cut -d' ' -f1)
  F98=no; [ -f corpus/fixtures/r98-clerk-filing/timeline.json ] && F98=yes
  S1=$(ls .ufo/waves/round-98/seats/S1-*.md 2>/dev/null | head -1)
  [ -n "$S1" ] && S1=yes || S1=no
  echo "$TS try=$i contract_changed=$([ "$CUR" != "$BASE" ] && echo yes || echo no) r98_fixture=$F98 s1_report=$S1" >> "$LOG"
  if [ "$CUR" != "$BASE" ] && [ "$F98" = yes ] && [ "$S1" = yes ]; then
    echo "$TS READY" >> "$LOG"
    exit 0
  fi
  sleep 20
done
echo "$(date +%H:%M:%S) TIMEOUT" >> "$LOG"
exit 3
