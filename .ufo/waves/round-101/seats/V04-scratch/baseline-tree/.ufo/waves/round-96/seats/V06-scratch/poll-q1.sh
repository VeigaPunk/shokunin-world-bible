#!/usr/bin/env bash
# V06 poll: wait for Q1's r96 tool revision + Q1 report. 20 s cadence, 40 tries.
# Usage: poll-q1.sh
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
TOOL=$ROOT/corpus/tools/map_obligations.py
REPORT=$ROOT/.ufo/waves/round-96/seats/Q1-tool-code.md
BASE_SHA=d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108
for try in $(seq 1 40); do
  sha=$(sha256sum "$TOOL" | cut -d' ' -f1)
  if [ "$sha" != "$BASE_SHA" ] && [ -f "$REPORT" ]; then
    echo "READY try=$try tool_sha=$sha report=present"
    exit 0
  fi
  echo "WAIT try=$try tool_sha=$sha report=$([ -f "$REPORT" ] && echo present || echo absent)"
  sleep 20
done
echo "TIMEOUT try=40 tool_sha=$(sha256sum "$TOOL" | cut -d' ' -f1) report=$([ -f "$REPORT" ] && echo present || echo absent)"
exit 1
