#!/bin/bash
# V107 stall-escape 2: five producer reports, artifacts already seen.
# 20s cadence, max 20 (~7 min). Recorded. Does not wait on SELF.
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS="$ROOT/.ufo/waves/round-99/seats"
LOG="$SEATS/V107-scratch/poll-escape2.log"
cd "$ROOT" || exit 1
echo "ESCAPE2_START $(date '+%Y-%m-%d %H:%M:%S %z') reason=knowledge-files-landed-reports-S2-S5-still-absent" >> "$LOG"
for i in $(seq 1 20); do
  arts=0
  missing=""
  for f in \
    corpus/knowledge/r99-gate-blind-spot-table.md \
    corpus/knowledge/r99-lapse-scope-note.md \
    corpus/tools/dependency_freeze.py \
    corpus/tools/dependency-freeze-contract.json \
    corpus/tools/README.md \
    SKILL.md
  do
    if [ -f "$f" ]; then arts=$((arts+1)); else missing="$missing $f"; fi
  done
  reps=$(ls -1 "$SEATS"/S*-*.md 2>/dev/null | wc -l)
  snames=$(ls -1 "$SEATS"/S*-*.md 2>/dev/null | xargs -n1 basename 2>/dev/null | tr '\n' ' ')
  hpy=$(sha256sum corpus/tools/dependency_freeze.py 2>/dev/null | cut -c1-12)
  hct=$(sha256sum corpus/tools/dependency-freeze-contract.json 2>/dev/null | cut -c1-12)
  hrdme=$(sha256sum corpus/tools/README.md 2>/dev/null | cut -c1-12)
  hskill=$(sha256sum SKILL.md 2>/dev/null | cut -c1-12)
  htbl=$(sha256sum corpus/knowledge/r99-gate-blind-spot-table.md 2>/dev/null | cut -c1-12)
  hnote=$(sha256sum corpus/knowledge/r99-lapse-scope-note.md 2>/dev/null | cut -c1-12)
  echo "ESC2 t=$(date '+%H:%M:%S') try=$i arts6=$arts/6 reps=$reps/5 py=$hpy ct=$hct toolsrd=$hrdme skill=$hskill tbl=$htbl note=$hnote names=[$snames] missing=[$missing]" >> "$LOG"
  if [ "$arts" -eq 6 ] && [ "$reps" -ge 5 ]; then
    echo "ALL-PRESENT t=$(date '+%Y-%m-%d %H:%M:%S %z') try=$i" >> "$LOG"
    exit 0
  fi
  sleep 20
done
echo "ESCAPE2_TIMEOUT t=$(date '+%Y-%m-%d %H:%M:%S %z') arts=$arts reps=$reps" >> "$LOG"
exit 2
