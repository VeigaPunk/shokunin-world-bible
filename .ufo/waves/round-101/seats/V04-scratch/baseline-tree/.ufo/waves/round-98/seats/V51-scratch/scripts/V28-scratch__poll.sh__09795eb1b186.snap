#!/bin/bash
# V28 poll: producer reports S1-S5 + key artifacts (20s cadence, 40 tries)
R=/home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  missing=""
  for f in corpus/fixtures/r98-clerk-filing/entities.json corpus/fixtures/r98-clerk-filing/sources.json corpus/fixtures/r98-clerk-filing/timeline.json corpus/fixtures/r98-clerk-filing/fictional-excerpts.md corpus/fixtures/r98-clerk-filing/README.md corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md corpus/knowledge/r98-clerk-scope-note.md; do
    [ -s "$R/$f" ] || missing="$missing $f"
  done
  for s in S1 S2 S3 S4 S5; do
    ls "$R"/.ufo/waves/round-98/seats/${s}-*.md >/dev/null 2>&1 || missing="$missing REPORT:$s"
  done
  if [ -z "$missing" ]; then echo "ALL-PRESENT at try $i $(date -u +%H:%M:%S)"; exit 0; fi
  echo "try $i $(date -u +%H:%M:%S) missing:$missing"
  sleep 20
done
echo "POLL-TIMEOUT after 40 tries $(date -u +%H:%M:%S)"
exit 1
