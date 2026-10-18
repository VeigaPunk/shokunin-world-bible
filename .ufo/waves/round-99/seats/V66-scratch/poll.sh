#!/bin/bash
# V66 poll: artifacts AND producer reports. 20s cadence, max 40 tries.
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
LOG=$ROOT/.ufo/waves/round-99/seats/V66-scratch/poll.log
cd "$ROOT" || exit 1
for try in $(seq 1 40); do
  ts=$(date -Is)
  reports=$(ls -1 .ufo/waves/round-99/seats/S*.md 2>/dev/null | xargs -n1 basename 2>/dev/null | tr '\n' ',' )
  know=$(ls -1 corpus/knowledge/r99-* 2>/dev/null | tr '\n' ',' )
  freeze_py=$(sha256sum corpus/tools/dependency_freeze.py | awk '{print $1}')
  freeze_json=$(sha256sum corpus/tools/dependency-freeze-contract.json | awk '{print $1}')
  tools_readme=$(sha256sum corpus/tools/README.md | awk '{print $1}')
  skill=$(sha256sum SKILL.md | awk '{print $1}')
  echo "try=$try ts=$ts reports=${reports:-NONE} knowledge=${know:-NONE} freeze_py=${freeze_py:0:12} contract=${freeze_json:0:12} tools_readme=${tools_readme:0:12} skill=${skill:0:12}" >> "$LOG"
  s1=0; s2=0; s5=0
  ls .ufo/waves/round-99/seats/S1-*.md >/dev/null 2>&1 && s1=1
  ls .ufo/waves/round-99/seats/S2-*.md >/dev/null 2>&1 && s2=1
  ls .ufo/waves/round-99/seats/S5-*.md >/dev/null 2>&1 && s5=1
  k1=0; k2=0
  test -f corpus/knowledge/r99-gate-blind-spot-table.md && k1=1
  test -f corpus/knowledge/r99-lapse-scope-note.md && k2=1
  if [ "$s1" = 1 ] && [ "$s2" = 1 ] && [ "$s5" = 1 ] && [ "$k1" = 1 ] && [ "$k2" = 1 ]; then
    echo "READY try=$try ts=$ts" >> "$LOG"
    exit 0
  fi
  sleep 20
done
echo "EXHAUSTED ts=$(date -Is)" >> "$LOG"
exit 2
