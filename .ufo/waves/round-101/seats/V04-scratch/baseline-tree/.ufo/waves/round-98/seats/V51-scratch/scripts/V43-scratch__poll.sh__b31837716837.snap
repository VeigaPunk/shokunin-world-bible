#!/bin/bash
# V43 pins-c9 poll: V19 report + producer reports S1-S5 + r98 artifacts
R=/home/vgpnk/Projects/shokunin/lore-shokunin
cd "$R"
FIX=corpus/fixtures/r98-clerk-filing
for i in $(seq 1 40); do
  missing=""
  ls .ufo/waves/round-98/seats/V19-*.md >/dev/null 2>&1 || missing="$missing V19-REPORT"
  for s in S1 S2 S3 S4 S5; do
    ls .ufo/waves/round-98/seats/${s}-*.md >/dev/null 2>&1 || missing="$missing REPORT:$s"
  done
  for f in $FIX/entities.json $FIX/sources.json $FIX/timeline.json $FIX/fictional-excerpts.md $FIX/README.md $FIX/claim-excerpt-map.md corpus/knowledge/r98-clerk-scope-note.md; do
    [ -s "$f" ] || missing="$missing $f"
  done
  git diff --name-only 9a3d648 -- corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json | grep -q . || missing="$missing S1-freeze-change"
  if [ -z "$missing" ]; then echo "ALL-PRESENT try=$i $(date -u +%H:%M:%S)"; exit 0; fi
  echo "try=$i $(date -u +%H:%M:%S) missing:$missing"
  sleep 20
done
echo "POLL-TIMEOUT $(date -u +%H:%M:%S)"
exit 1
