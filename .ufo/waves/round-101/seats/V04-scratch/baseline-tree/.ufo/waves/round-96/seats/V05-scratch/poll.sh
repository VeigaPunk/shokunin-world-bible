#!/bin/bash
# V05 poll: wait for Q1's tool revision + report, and Q5's r96 map
cd /home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=.ufo/waves/round-96/seats
PRE=d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108
for i in $(seq 1 40); do
  tool_sha=$(sha256sum corpus/tools/map_obligations.py | cut -d' ' -f1)
  q1=$(ls $SEATS/Q1*.md 2>/dev/null | head -1)
  q5=$(ls corpus/fixtures/r96-crossing-response/claim-excerpt-map.md 2>/dev/null | head -1)
  if [ -n "$q1" ] && [ "$tool_sha" != "$PRE" ]; then
    echo "POLL_HIT tries=$i tool_sha=$tool_sha report=$q1 q5_map=${q5:-absent}"
    exit 0
  fi
  echo "try=$i tool_sha=$tool_sha q1_report=${q1:-absent} q5_map=${q5:-absent}"
  sleep 20
done
echo "POLL_TIMEOUT after 40 tries"
exit 1
