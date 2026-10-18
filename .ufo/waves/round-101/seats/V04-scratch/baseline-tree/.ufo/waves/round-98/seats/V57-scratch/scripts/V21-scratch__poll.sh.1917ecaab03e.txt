#!/bin/bash
# V21 freshness poll: producer reports (non-V files directly in seats/) + artifact states.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 1
SEATS=.ufo/waves/round-98/seats
LOG=$SEATS/V21-scratch/poll.log
BASE=.ufo/waves/round-98/seats/V21-scratch/baseline-9a3d648.sha256
for i in $(seq 1 40); do
  TS=$(date -Iseconds)
  # producer reports: regular files directly in seats/, not starting with V
  REPORTS=$(find "$SEATS" -maxdepth 1 -type f -name '*.md' ! -name 'V*' -printf '%f\n' 2>/dev/null | sort | tr '\n' ',')
  NR=$(find "$SEATS" -maxdepth 1 -type f -name '*.md' ! -name 'V*' 2>/dev/null | wc -l)
  # artifact states
  DFP=$(sha256sum corpus/tools/dependency_freeze.py | cut -c1-12)
  DFC=$(sha256sum corpus/tools/dependency-freeze-contract.json | cut -c1-12)
  R95=$(sha256sum corpus/knowledge/r95-aftermath-scope-note.md | cut -c1-12)
  R96=$(sha256sum corpus/knowledge/r96-response-scope-note.md | cut -c1-12)
  NOTE98=$([ -f corpus/knowledge/r98-clerk-scope-note.md ] && echo yes || echo no)
  R98FIX=$([ -d corpus/fixtures/r98-clerk-filing ] && echo yes || echo no)
  TRD=$([ -f corpus/tools/README.md ] && sha256sum corpus/tools/README.md | cut -c1-12)
  echo "try=$i ts=$TS reports=$NR [$REPORTS] dfp=$DFP dfc=$DFC r95note=$R95 r96note=$R96 note98=$NOTE98 fix98=$R98FIX toolsREADME=$TRD" >> "$LOG"
  if [ "$NR" -ge 5 ] && [ "$NOTE98" = yes ] && [ "$R98FIX" = yes ]; then
    echo "try=$i ts=$TS ALL-PRESENT" >> "$LOG"
    exit 0
  fi
  sleep 20
done
echo "$(date -Iseconds) POLL-EXPIRED" >> "$LOG"
exit 3
