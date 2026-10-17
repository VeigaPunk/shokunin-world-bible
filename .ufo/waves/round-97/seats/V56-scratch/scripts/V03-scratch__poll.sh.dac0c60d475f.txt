#!/bin/bash
# V03 poll for R1: report exists AND map_obligations.py sha != r96 baseline 2b0ba815...
REPO=/home/vgpnk/Projects/shokunin/lore-shokunin
cd "$REPO" || exit 9
LOG="$REPO/.ufo/waves/round-97/seats/V03-scratch/poll.log"
BASE=2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8
for i in $(seq 1 40); do
  sha=$(sha256sum corpus/tools/map_obligations.py | cut -d' ' -f1)
  rep=absent; [ -f .ufo/waves/round-97/seats/R1-*.md ] && rep=present
  r97=absent; [ -f corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md ] && r97=present
  echo "POLL_CHECK try=$i tool_sha=$sha q1_report=$rep r97_map=$r97 t=$(date -Is)" >> "$LOG"
  if [ "$sha" != "$BASE" ] && [ "$rep" = present ]; then
    echo "POLL_HIT try=$i tool_sha=$sha report=$(ls .ufo/waves/round-97/seats/R1-*.md) r97_map=$r97 t=$(date -Is)" >> "$LOG"
    echo "POLL_HIT try=$i tool_sha=$sha r97_map=$r97"; exit 0
  fi
  sleep 20
done
echo "POLL_TERMINAL tries=40 status=absent" >> "$LOG"
echo "POLL_TERMINAL tries=40 status=absent"; exit 1
