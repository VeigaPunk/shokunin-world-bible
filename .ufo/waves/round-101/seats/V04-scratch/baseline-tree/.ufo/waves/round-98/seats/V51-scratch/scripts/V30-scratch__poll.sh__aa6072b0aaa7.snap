#!/bin/sh
# V30 poller: artifacts + producer reports, 20s cadence, max 40 tries.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 1
SEATS=.ufo/waves/round-98/seats
n=0
while [ "$n" -lt 40 ]; do
  n=$((n+1))
  ts=$(date '+%H:%M:%S')
  FIX=$(ls corpus/fixtures/r98-clerk-filing/ 2>/dev/null | wc -l)
  NOTE=$([ -f corpus/knowledge/r98-clerk-scope-note.md ] && echo 1 || echo 0)
  R95N=$([ -f corpus/knowledge/r95-aftermath-scope-note.md ] && git diff --quiet 9a3d648 -- corpus/knowledge/r95-aftermath-scope-note.md && echo 0 || echo 1)
  R96N=$([ -f corpus/knowledge/r96-response-scope-note.md ] && git diff --quiet 9a3d648 -- corpus/knowledge/r96-response-scope-note.md && echo 0 || echo 1)
  R95M=$([ -f corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md ] && git diff --quiet 9a3d648 -- corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md && echo 0 || echo 1)
  TOOL=$([ -f corpus/tools/dependency_freeze.py ] && git diff --quiet 9a3d648 -- corpus/tools/dependency_freeze.py && echo 0 || echo 1)
  CONT=$([ -f corpus/tools/dependency-freeze-contract.json ] && git diff --quiet 9a3d648 -- corpus/tools/dependency-freeze-contract.json && echo 0 || echo 1)
  TREAD=$([ -f corpus/tools/README.md ] && git diff --quiet 9a3d648 -- corpus/tools/README.md && echo 0 || echo 1)
  REP=$(ls $SEATS/*.md 2>/dev/null | grep -v 'V30-' | wc -l)
  REPLIST=$(ls $SEATS/*.md 2>/dev/null | grep -v 'V30-' | xargs -n1 basename 2>/dev/null | tr '\n' ',')
  echo "POLL t=$ts n=$n fixture_files=$FIX note=$NOTE r95note=$R95N r96note=$R96N r95map=$R95M tool=$TOOL contract=$CONT tread=$TREAD reports=$REP [$REPLIST]"
  if [ "$FIX" -ge 10 ] && [ "$NOTE" = 1 ] && [ "$R95N" = 1 ] && [ "$R96N" = 1 ] && [ "$R95M" = 1 ] && [ "$TOOL" = 1 ] && [ "$CONT" = 1 ] && [ "$TREAD" = 1 ] && [ "$REP" -ge 5 ]; then
    echo "ALL-PRESENT t=$ts n=$n"
    exit 0
  fi
  sleep 20
done
echo "POLL_DEADLINE n=$n"
exit 2
