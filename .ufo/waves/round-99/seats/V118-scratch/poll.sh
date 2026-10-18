#!/bin/bash
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
cd "$LANE"
LOG="$LANE/.ufo/waves/round-99/seats/V118-scratch/poll.log"
BASE_TOOL=03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b
BASE_CT=153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947
prev=""
stable=0
for i in $(seq 1 40); do
  ts=$(date -Iseconds)
  tool=$(sha256sum corpus/tools/dependency_freeze.py | awk '{print $1}')
  ct=$(sha256sum corpus/tools/dependency-freeze-contract.json | awk '{print $1}')
  reports=$(ls -1 .ufo/waves/round-99/seats/S1*.md 2>/dev/null | tr '\n' ',' )
  [ -z "$reports" ] && reports=none
  toolstate=same
  [ "$tool" != "$BASE_TOOL" ] && toolstate=changed
  ctstate=same
  [ "$ct" != "$BASE_CT" ] && ctstate=changed
  combo="${tool}:${ct}:${reports}"
  if [ "$combo" = "$prev" ] && [ "$reports" != none ] && [ "$toolstate" = changed ] && [ "$ctstate" = changed ]; then
    stable=$((stable+1))
  else
    stable=0
  fi
  prev="$combo"
  echo "try=$i t=$ts report=$reports tool=$toolstate ct=$ctstate toolsha=${tool:0:16} ctsha=${ct:0:16} stable=$stable" | tee -a "$LOG"
  if [ "$stable" -ge 2 ]; then
    echo "POLL_HIT try=$i tool=$tool contract=$ct report=$reports" | tee -a "$LOG"
    exit 0
  fi
  sleep 20
done
echo "POLL_EXHAUSTED" | tee -a "$LOG"
exit 2
