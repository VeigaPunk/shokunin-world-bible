#!/bin/bash
R=/home/vgpnk/Projects/shokunin/lore-shokunin
F=$R/corpus/fixtures/r98-clerk-filing
for i in $(seq 1 40); do
  missing=""
  grep -q 'clerk-maren' "$F/entities.json" 2>/dev/null || missing="$missing entities:clerk-maren"
  grep -q 'clerk-filing-note' "$F/sources.json" 2>/dev/null || missing="$missing sources:clerk-filing-note"
  grep -q 'clerk-filing-open' "$F/timeline.json" 2>/dev/null || missing="$missing timeline:clerk-filing-open"
  grep -q 'clerk' "$F/fictional-excerpts.md" 2>/dev/null || missing="$missing excerpts:clerk"
  grep -q 'J20' "$F/claim-excerpt-map.md" 2>/dev/null || missing="$missing map:J20"
  grep -qi 'clerk' "$F/README.md" 2>/dev/null || missing="$missing readme:clerk"
  grep -qi 'clerk' "$R/corpus/knowledge/r98-clerk-scope-note.md" 2>/dev/null || missing="$missing note"
  for s in S3 S4 S5; do ls "$R"/.ufo/waves/round-98/seats/${s}-*.md >/dev/null 2>&1 || missing="$missing REPORT:$s"; done
  if [ -z "$missing" ]; then echo "ALL-PRESENT at try $i $(date -u +%H:%M:%S)"; exit 0; fi
  echo "try $i $(date -u +%H:%M:%S) missing:$missing"
  sleep 20
done
echo "POLL-TIMEOUT $(date -u +%H:%M:%S)"; exit 1
