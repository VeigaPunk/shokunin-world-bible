#!/bin/bash
# V40 poller: waits for S1 report + tool/contract sha change vs 9a3d648 baseline.
# 40 tries, 20s cadence; then 3-consecutive-sha stability gate. Logs to $OUT.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
OUT=.ufo/waves/round-98/scratch/V40/poll.log
BASE_TOOL=b06275f3bbdeabaab615138b3004703fce701a786af882d3b732828b37722130
BASE_CT=27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781
: > "$OUT"
for i in $(seq 1 40); do
  ts=$(date +%H:%M:%S)
  report=$(ls .ufo/waves/round-98/seats/S1-*.md 2>/dev/null | head -1)
  tool=$(sha256sum corpus/tools/dependency_freeze.py | cut -d' ' -f1)
  ct=$(sha256sum corpus/tools/dependency-freeze-contract.json | cut -d' ' -f1)
  tflag="same"; [ "$tool" != "$BASE_TOOL" ] && tflag="changed"
  cflag="same"; [ "$ct" != "$BASE_CT" ] && cflag="changed"
  echo "try=$i t=$ts report=${report:-none} tool=$tflag contract=$cflag" >> "$OUT"
  if [ -n "$report" ] && [ "$tflag" = changed ] && [ "$cflag" = changed ]; then
    prev=""
    stable=0
    for j in $(seq 1 4); do
      sleep 20
      s=$( { sha256sum corpus/tools/dependency_freeze.py; sha256sum corpus/tools/dependency-freeze-contract.json; } | sha256sum | cut -d' ' -f1)
      if [ "$s" = "$prev" ]; then stable=$((stable+1)); else stable=0; fi
      echo "STAB i=$j sha=$s stable=$stable" >> "$OUT"
      prev="$s"
      [ "$stable" -ge 2 ] && break
    done
    echo "POLL_HIT try=$i report=$report tool=$tool contract=$ct" >> "$OUT"
    echo "POLL_STABLE sha=$prev" >> "$OUT"
    exit 0
  fi
  sleep 20
done
echo "POLL_TIMEOUT" >> "$OUT"
exit 1
