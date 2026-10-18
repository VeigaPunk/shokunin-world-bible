#!/bin/bash
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
cd "$LANE"
LOG="$LANE/.ufo/waves/round-99/seats/V118-scratch/poll.log"
prev=""
stable=0
# continuation after the timed-out poller (tries 1-15 already logged)
for i in $(seq 16 40); do
  ts=$(date -Iseconds)
  tool=$(sha256sum corpus/tools/dependency_freeze.py | awk '{print $1}')
  ct=$(sha256sum corpus/tools/dependency-freeze-contract.json | awk '{print $1}')
  reports=$(ls -1 .ufo/waves/round-99/seats/S1*.md 2>/dev/null | tr '\n' ',' )
  [ -z "$reports" ] && reports=none
  combo="${tool}:${ct}:${reports}"
  if [ "$combo" = "$prev" ] && [ "$reports" != none ]; then
    stable=$((stable+1))
  else
    stable=0
  fi
  prev="$combo"
  echo "try=$i t=$ts report=$reports toolsha=$tool ctsha=$ct stable=$stable" | tee -a "$LOG"
  if [ "$stable" -ge 2 ]; then
    echo "POLL_HIT try=$i tool=$tool contract=$ct report=$reports" | tee -a "$LOG"
    exit 0
  fi
  sleep 20
done
echo "POLL_EXHAUSTED tries=16-40" | tee -a "$LOG"
exit 2
