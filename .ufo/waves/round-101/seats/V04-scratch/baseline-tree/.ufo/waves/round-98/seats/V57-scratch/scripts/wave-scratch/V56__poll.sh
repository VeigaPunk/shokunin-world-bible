#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
ART="corpus/fixtures/r98-clerk-filing/entities.json corpus/fixtures/r98-clerk-filing/sources.json corpus/fixtures/r98-clerk-filing/timeline.json corpus/fixtures/r98-clerk-filing/fictional-excerpts.md corpus/fixtures/r98-clerk-filing/README.md corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md corpus/knowledge/r98-clerk-scope-note.md"
for i in $(seq 1 40); do
  miss=""
  for a in $ART; do [ -e "$a" ] || miss="$miss $a"; done
  [ -z "$miss" ] && { echo "ALL-PRESENT try=$i $(date +%H:%M:%S)"; exit 0; }
  echo "try $i $(date +%H:%M:%S) missing:$miss"
  sleep 20
done
echo "TIMEOUT try=40 $(date +%H:%M:%S)"
