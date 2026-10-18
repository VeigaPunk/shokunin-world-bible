#!/bin/bash
# V52 poll-wait: producers S1+S2 reports AND delivered freeze artifacts changed vs baseline.
# 20s cadence, 40 tries. Never verifies a plan. SELF (V52) is not in the wait set.
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS="$LANE/.ufo/waves/round-99/seats"
LOG="$SEATS/V52-scratch/poll.log"
BASE=4265df5e86e4121bde4125b649b89bb1676676a5
: > "$LOG"
for i in $(seq 1 40); do
  ts=$(date -Is)
  miss=""
  # producer reports (any S1-*.md / S2-*.md)
  s1=$(find "$SEATS" -maxdepth 1 -name 'S1-*.md' -type f 2>/dev/null | head -1)
  s2=$(find "$SEATS" -maxdepth 1 -name 'S2-*.md' -type f 2>/dev/null | head -1)
  [ -n "$s1" ] || miss="$miss REPORT:S1"
  [ -n "$s2" ] || miss="$miss REPORT:S2"
  # tool bytes differ from baseline
  if git -C "$LANE" diff --quiet "$BASE" -- corpus/tools/dependency_freeze.py 2>/dev/null; then
    miss="$miss TOOL-UNCHANGED"
  fi
  if git -C "$LANE" diff --quiet "$BASE" -- corpus/tools/dependency-freeze-contract.json 2>/dev/null; then
    miss="$miss CONTRACT-UNCHANGED"
  fi
  if [ -z "$miss" ]; then
    echo "try $i $ts ALL-PRESENT s1=$s1 s2=$s2" | tee -a "$LOG"
    exit 0
  fi
  echo "try $i $ts missing:$miss" | tee -a "$LOG"
  sleep 20
done
echo "try 40 $(date -Is) ABSENT" | tee -a "$LOG"
exit 2
