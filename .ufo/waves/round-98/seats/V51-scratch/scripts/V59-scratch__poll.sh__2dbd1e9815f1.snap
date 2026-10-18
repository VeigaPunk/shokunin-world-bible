#!/bin/bash
R=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$R/.ufo/waves/round-98/seats
ART="corpus/fixtures/r98-clerk-filing/entities.json corpus/fixtures/r98-clerk-filing/sources.json corpus/fixtures/r98-clerk-filing/timeline.json corpus/fixtures/r98-clerk-filing/fictional-excerpts.md corpus/fixtures/r98-clerk-filing/README.md corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md corpus/knowledge/r98-clerk-scope-note.md corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json corpus/tools/README.md corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md corpus/knowledge/r95-aftermath-scope-note.md corpus/knowledge/r96-response-scope-note.md"
for i in $(seq 1 45); do
  t=$(date -u +%H:%M:%S)
  nrep=$(ls $S/*.md 2>/dev/null | wc -l)
  missA=""
  for f in $ART; do [ -s "$R/$f" ] || missA="$missA $(basename $(dirname $f))/$(basename $f)"; done
  missR=""
  for s in S1 S2 S3 S4 S5; do ls $S/${s}-*.md >/dev/null 2>&1 || missR="$missR $s"; done
  ls $S/V*.md 2>/dev/null | sed 's#.*/##;s/-.*//' | sort -u | tr '\n' ',' > $S/V59-scratch/present-v.txt
  echo "try=$i t=$t reports=$nrep missArtifacts:[$missA ] missProducerReports:[$missR ]"
  sleep 20
done
echo "POLL-TERMINAL $t"
