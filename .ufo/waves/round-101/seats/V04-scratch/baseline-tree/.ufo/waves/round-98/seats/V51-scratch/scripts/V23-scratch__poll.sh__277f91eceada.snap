#!/bin/bash
R=/home/vgpnk/Projects/shokunin/lore-shokunin
cd "$R"
for i in $(seq 1 40); do
  missing=""
  # S4 artifacts
  for f in corpus/fixtures/r98-clerk-filing/README.md corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md; do
    [ -s "$f" ] || missing="$missing $f"
  done
  # S5 artifacts
  for f in corpus/knowledge/r98-clerk-scope-note.md; do
    [ -s "$f" ] || missing="$missing $f"
  done
  git diff --name-only 9a3d648 -- corpus/knowledge/r95-aftermath-scope-note.md | grep -q . || missing="$missing r95-addendum"
  git diff --name-only 9a3d648 -- corpus/knowledge/r96-response-scope-note.md | grep -q . || missing="$missing r96-addendum"
  # S2 artifact
  git diff --name-only 9a3d648 -- corpus/tools/README.md | grep -q . || missing="$missing tools-README"
  # producer reports S1 S2 S4 S5
  for s in S1 S2 S4 S5; do
    ls .ufo/waves/round-98/seats/${s}-*.md >/dev/null 2>&1 || missing="$missing REPORT:$s"
  done
  if [ -z "$missing" ]; then echo "ALL-PRESENT try=$i $(date -u +%H:%M:%S)"; exit 0; fi
  echo "try=$i $(date -u +%H:%M:%S) missing:$missing"
  sleep 20
done
echo "POLL-TIMEOUT $(date -u +%H:%M:%S)"
exit 1
