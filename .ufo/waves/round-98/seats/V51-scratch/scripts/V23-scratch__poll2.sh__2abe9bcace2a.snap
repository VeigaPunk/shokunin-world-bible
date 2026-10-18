#!/bin/bash
R=/home/vgpnk/Projects/shokunin/lore-shokunin
cd "$R"
for i in $(seq 1 40); do
  missing=""
  head -1 corpus/fixtures/r98-clerk-filing/README.md 2>/dev/null | grep -qi 'round 98' || missing="$missing S4-README"
  grep -qi 'clerk' corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md 2>/dev/null || missing="$missing S4-MAP"
  [ -s corpus/knowledge/r98-clerk-scope-note.md ] || missing="$missing S5-NOTE"
  git diff --name-only 9a3d648 -- corpus/knowledge/r95-aftermath-scope-note.md | grep -q . || missing="$missing S5-r95add"
  git diff --name-only 9a3d648 -- corpus/knowledge/r96-response-scope-note.md | grep -q . || missing="$missing S5-r96add"
  git diff --name-only 9a3d648 -- corpus/tools/README.md | grep -q . || missing="$missing S2-TOOLSREADME"
  for s in S1 S2 S4 S5; do
    ls .ufo/waves/round-98/seats/${s}-*.md >/dev/null 2>&1 || missing="$missing REPORT:$s"
  done
  if [ -z "$missing" ]; then echo "ALL-PRESENT try=$i $(date -u +%H:%M:%S)"; exit 0; fi
  echo "try=$i $(date -u +%H:%M:%S) missing:$missing"
  sleep 20
done
echo "POLL-TIMEOUT $(date -u +%H:%M:%S)"
exit 1
