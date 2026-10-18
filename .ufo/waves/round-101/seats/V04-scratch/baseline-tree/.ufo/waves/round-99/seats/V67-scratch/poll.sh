#!/bin/bash
# V67 content-gated poll. Writes one line per try. Exit 0 when all gates pass.
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$ROOT/.ufo/waves/round-99/seats
LOG=$SEATS/V67-scratch/poll.log
README_FIX=$ROOT/corpus/fixtures/r99-window-lapse/README.md
TOOLS=$ROOT/corpus/tools/README.md
SKILL=$ROOT/SKILL.md
i=0
while [ "$i" -lt 40 ]; do
  i=$((i+1))
  ts=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  miss=""
  # fixture README must no longer be the r98 placeholder
  if [ ! -f "$README_FIX" ]; then
    miss="$miss fixture-readme-absent"
  elif ! grep -q 'r99-window-lapse' "$README_FIX"; then
    miss="$miss fixture-readme-placeholder"
  elif ! grep -q 'python3' "$README_FIX"; then
    miss="$miss fixture-readme-no-command"
  fi
  # tools README r99 addendum
  if ! grep -q -E 'Round-99|Round 99|round-99 addendum|r99 addendum' "$TOOLS"; then
    # looser: any r99 mention in tools README
    if ! grep -q 'r99' "$TOOLS"; then
      miss="$miss tools-readme-no-r99"
    fi
  fi
  # SKILL freeze row updated past r98 17-case / JSON-only bound
  if grep -q '17 cases' "$SKILL" && grep -q 'markdown/prose half remains open' "$SKILL"; then
    miss="$miss skill-freeze-row-unupdated"
  fi
  # producer reports (S2 owns tools README + SKILL; S4 owns fixture README)
  for s in S2 S4; do
    if ! ls "$SEATS"/${s}*.md >/dev/null 2>&1; then
      miss="$miss ${s}-report-absent"
    fi
  done
  # also note S1/S5 for the log, not gating this seat's command set
  extra=""
  for s in S1 S3 S5; do
    if ! ls "$SEATS"/${s}*.md >/dev/null 2>&1; then
      extra="$extra ${s}-absent"
    fi
  done
  echo "try=$i ts=$ts miss=${miss:-NONE} extra=${extra:-none}" >> "$LOG"
  if [ -z "$miss" ]; then
    echo "READY try=$i" >> "$LOG"
    exit 0
  fi
  sleep 20
done
echo "ABSENT after 40" >> "$LOG"
exit 1
