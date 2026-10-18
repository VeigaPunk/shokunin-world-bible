#!/bin/bash
# V67 poll continuation. Tries 16-40. Exit 0 when tools README r99 + S2 report exist.
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$ROOT/.ufo/waves/round-99/seats
LOG=$SEATS/V67-scratch/poll.log
TOOLS=$ROOT/corpus/tools/README.md
SKILL=$ROOT/SKILL.md
i=15
while [ "$i" -lt 40 ]; do
  i=$((i+1))
  ts=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  miss=""
  if ! grep -q -E 'r99|Round-99|Round 99|18/18|markdown_tamper|ten files|all ten' "$TOOLS"; then
    miss="$miss tools-readme-no-r99"
  fi
  skill="skill-stale"
  if ! grep -q '17 cases' "$SKILL" || ! grep -q 'markdown/prose half remains open' "$SKILL"; then
    skill="skill-changed"
  fi
  if grep -q -E '18 cases|markdown_tamper|all ten files|payload_schema_version|ten-file' "$SKILL"; then
    skill="skill-updated"
  fi
  if ! ls "$SEATS"/S2*.md >/dev/null 2>&1; then
    miss="$miss S2-report-absent"
  fi
  extra=""
  for s in S1 S5; do
    if ! ls "$SEATS"/${s}*.md >/dev/null 2>&1; then
      extra="$extra ${s}-absent"
    else
      extra="$extra ${s}-present"
    fi
  done
  echo "try=$i ts=$ts miss=${miss:-NONE} skill=$skill extra=${extra:-none}" >> "$LOG"
  if [ -z "$miss" ]; then
    echo "READY try=$i" >> "$LOG"
    exit 0
  fi
  sleep 20
done
echo "ABSENT after 40" >> "$LOG"
exit 1
