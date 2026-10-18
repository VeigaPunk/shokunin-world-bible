#!/bin/sh
# V08 c1-negative-rerun poller. 20s cadence, 40 tries.
# Hit: an S1-*.md report exists under round-99 seats AND the freeze tool+contract
# combined sha is stable for 3 consecutive checks. A report against unchanged
# baseline bytes is recorded, not treated as a delivery.
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS="$LANE/.ufo/waves/round-99/seats"
TOOL="$LANE/corpus/tools/dependency_freeze.py"
CONTRACT="$LANE/corpus/tools/dependency-freeze-contract.json"
BASE_TOOL=03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b
BASE_CONTRACT=153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947
LOG="$LANE/.ufo/waves/round-99/seats/V08-scratch/poll.log"
echo "POLL_RESUME $(date '+%Y-%m-%d %H:%M:%S %Z') from_try=16 reason=prior-poller-killed-at-tool-timeout-after-try-15" | tee -a "$LOG"
prev=""
stable=0
i=16
while [ "$i" -le 40 ]; do
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
  if [ "$toolsha" = "$BASE_TOOL" ]; then toolstate=same; else toolstate=changed; fi
  if [ "$ctsha" = "$BASE_CONTRACT" ]; then ctstate=same; else ctstate=changed; fi
  echo "try=$i t=$ts report=$report tool=$toolstate contract=$ctstate toolsha=$toolsha ctsha=$ctsha" | tee -a "$LOG"
  if [ "$report" != none ] && [ "$toolsha" != missing ] && [ "$ctsha" != missing ]; then
    combo=$(printf '%s\n%s\n' "$toolsha" "$ctsha" | sha256sum | awk '{print $1}')
    if [ "$combo" = "$prev" ]; then
      stable=$((stable+1))
    else
      stable=0
      prev=$combo
    fi
    echo "STAB i=$i sha=$combo stable=$stable tool=$toolstate contract=$ctstate" | tee -a "$LOG"
    if [ "$stable" -ge 2 ]; then
      echo "POLL_HIT try=$i report=$report tool=$toolsha contract=$ctsha toolstate=$toolstate contractstate=$ctstate" | tee -a "$LOG"
      echo "POLL_STABLE sha=$combo" | tee -a "$LOG"
      exit 0
    fi
  else
    prev=""
    stable=0
  fi
  i=$((i+1))
  if [ "$i" -le 40 ]; then
    sleep 20
  fi
done
echo "POLL_ABSENT tries=40" | tee -a "$LOG"
exit 2
