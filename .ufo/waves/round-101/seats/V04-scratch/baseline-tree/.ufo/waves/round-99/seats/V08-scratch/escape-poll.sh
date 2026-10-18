#!/bin/sh
# Bounded stall-escape after the 40-try budget. Recorded, not silent.
# Producer was still rewriting dependency_freeze.py at 22:38:11 (11s after try 40)
# and S1-scratch gained directories at 22:43. 20 extra tries, 20s cadence.
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS="$LANE/.ufo/waves/round-99/seats"
TOOL="$LANE/corpus/tools/dependency_freeze.py"
CONTRACT="$LANE/corpus/tools/dependency-freeze-contract.json"
LOG="$LANE/.ufo/waves/round-99/seats/V08-scratch/poll.log"
echo "STALL_ESCAPE_START $(date '+%Y-%m-%d %H:%M:%S %Z') tries=41-60 reason=producer-still-writing-at-try-40 tool_mtime_after_deadline" | tee -a "$LOG"
prev=""
stable=0
i=41
while [ "$i" -le 60 ]; do
  ts=$(date '+%H:%M:%S')
  report=$(ls -1 "$SEATS"/S1-*.md "$SEATS"/S1.md 2>/dev/null | head -1)
  report=${report:-none}
  if [ -f "$TOOL" ]; then
    toolsha=$(sha256sum "$TOOL" | awk '{print $1}')
  else
    toolsha=missing
  fi
  if [ -f "$CONTRACT" ]; then
    ctsha=$(sha256sum "$CONTRACT" | awk '{print $1}')
  else
    ctsha=missing
  fi
  echo "escape try=$i t=$ts report=$report toolsha=$toolsha ctsha=$ctsha" | tee -a "$LOG"
  if [ "$report" != none ] && [ "$toolsha" != missing ] && [ "$ctsha" != missing ]; then
    combo=$(printf '%s\n%s\n' "$toolsha" "$ctsha" | sha256sum | awk '{print $1}')
    if [ "$combo" = "$prev" ]; then
      stable=$((stable+1))
    else
      stable=0
      prev=$combo
    fi
    echo "STAB i=$i sha=$combo stable=$stable" | tee -a "$LOG"
    if [ "$stable" -ge 2 ]; then
      echo "POLL_HIT try=$i report=$report tool=$toolsha contract=$ctsha toolstate=stall-escape contractstate=stall-escape" | tee -a "$LOG"
      echo "POLL_STABLE sha=$combo" | tee -a "$LOG"
      exit 0
    fi
  else
    prev=""
    stable=0
  fi
  i=$((i+1))
  if [ "$i" -le 60 ]; then
    sleep 20
  fi
done
echo "STALL_ESCAPE_ABSENT tries=41-60" | tee -a "$LOG"
exit 2
