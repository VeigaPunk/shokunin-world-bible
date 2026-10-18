#!/bin/bash
# V71 poll: artifact-based, 20s cadence, max 40 tries.
# Success = V39 report present AND producer artifacts present.
# Never verifies a plan. Subtracts SELF from any all-reports check.
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$LANE/.ufo/waves/round-99/seats
SCR=$SEATS/V71-scratch
LOG=$SCR/poll.log
V39=$SEATS/V39-receipt.md
# also accept any V39*.md that is a report (not scratch)
MAX=40
i=0
while [ "$i" -lt "$MAX" ]; do
  i=$((i+1))
  ts=$(date -Iseconds)
  v39_hit=""
  if [ -f "$V39" ]; then
    v39_hit="$V39"
  else
    # any top-level V39-*.md report
    for f in "$SEATS"/V39-*.md; do
      if [ -f "$f" ]; then
        v39_hit="$f"
        break
      fi
    done
  fi
  arts=""
  for p in \
    "$LANE/corpus/fixtures/r99-window-lapse/timeline.json" \
    "$LANE/corpus/fixtures/r99-window-lapse/sources.json" \
    "$LANE/corpus/fixtures/r99-window-lapse/claim-excerpt-map.md" \
    "$LANE/corpus/fixtures/r99-window-lapse/README.md" \
    "$LANE/corpus/fixtures/r99-window-lapse/fictional-excerpts.md" \
    "$LANE/corpus/knowledge/r99-gate-blind-spot-table.md" \
    "$LANE/corpus/knowledge/r99-lapse-scope-note.md" \
    "$LANE/corpus/tools/dependency_freeze.py" \
    "$LANE/corpus/tools/dependency-freeze-contract.json"
  do
    if [ -e "$p" ]; then
      arts="${arts}Y"
    else
      arts="${arts}."
    fi
  done
  # producer reports (not required for V39-audit success, recorded)
  prod=""
  for s in S1 S2 S3 S4 S5; do
    hit="."
    for f in "$SEATS"/${s}-*.md; do
      if [ -f "$f" ]; then hit="Y"; break; fi
    done
    prod="${prod}${hit}"
  done
  mdcount=$(find "$SEATS" -maxdepth 1 -name '*.md' -type f | wc -l)
  line="try=$i ts=$ts v39=${v39_hit:-ABSENT} arts=$arts prod=$prod md=$mdcount"
  echo "$line" | tee -a "$LOG"
  if [ -n "$v39_hit" ]; then
    # content gate: report must be non-empty and stable across one extra check
    sz1=$(wc -c < "$v39_hit")
    sleep 3
    sz2=$(wc -c < "$v39_hit")
    echo "v39-size sz1=$sz1 sz2=$sz2 path=$v39_hit" | tee -a "$LOG"
    if [ "$sz1" -gt 200 ] && [ "$sz1" = "$sz2" ]; then
      echo "V39_LANDED path=$v39_hit bytes=$sz2 try=$i" | tee -a "$LOG"
      echo "$v39_hit" > "$SCR/v39-path.txt"
      exit 0
    fi
    echo "V39_UNSTABLE continuing" | tee -a "$LOG"
  fi
  if [ "$i" -ge "$MAX" ]; then
    echo "ABSENT after $MAX tries" | tee -a "$LOG"
    exit 2
  fi
  sleep 20
done
echo "ABSENT loop-exit" | tee -a "$LOG"
exit 2
