#!/bin/bash
# V35 round-98 producer-artifact poll. Run from repo root. Bounded: 40 tries, 20s.
cd /home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=.ufo/waves/round-98/seats
BASE=9a3d648
for i in $(seq 1 40); do
  rep=$(ls "$SEATS" 2>/dev/null | grep -E '^S[1-5](-|\.)' | tr '\n' ' ')
  st=""
  [ -d corpus/fixtures/r98-clerk-filing ] && st="$st r98dir"
  [ -f corpus/knowledge/r98-clerk-scope-note.md ] && st="$st r98note"
  for f in corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json corpus/tools/README.md corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md; do
    git diff --quiet "$BASE" -- "$f" || st="$st $(basename $f)"
  done
  echo "try=$i reports=[$rep] artifacts=[$st]"
  case "$rep" in
    *S1*S2*S3*S4*S5*) echo "ALL5_REPORTS"; exit 0;;
  esac
  [ $i -lt 40 ] && sleep 20
done
echo "POLL_TIMEOUT"
exit 1
