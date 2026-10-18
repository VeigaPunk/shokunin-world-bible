#!/bin/bash
# V38 anchor-replica-2 poll: S3 payload + S4 map/README + S3/S4 producer reports, with 1-try md5 stability window.
R=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$R/.ufo/waves/round-98/seats/V38-scratch
FILES="corpus/fixtures/r98-clerk-filing/entities.json corpus/fixtures/r98-clerk-filing/sources.json corpus/fixtures/r98-clerk-filing/timeline.json corpus/fixtures/r98-clerk-filing/fictional-excerpts.md corpus/fixtures/r98-clerk-filing/README.md corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md"
prev=""
for i in $(seq 1 40); do
  missing=""
  for f in $FILES; do
    [ -s "$R/$f" ] || missing="$missing $f"
  done
  for s in S3 S4; do
    ls "$R"/.ufo/waves/round-98/seats/${s}-*.md >/dev/null 2>&1 || missing="$missing REPORT:$s"
  done
  if [ -z "$missing" ]; then
    cur=$(md5sum $(for f in $FILES; do echo "$R/$f"; done) | awk '{print $1}' | md5sum | awk '{print $1}')
    if [ "$cur" = "$prev" ]; then
      echo "READY-STABLE try=$i $(date -u +%H:%M:%S) md5set=$cur"; exit 0
    fi
    prev=$cur
    echo "PRESENT-UNSTABLE try=$i $(date -u +%H:%M:%S) md5set=$cur"
  else
    echo "try $i $(date -u +%H:%M:%S) missing:$missing"
    prev=""
  fi
  sleep 20
done
echo "POLL-TIMEOUT after 40 tries $(date -u +%H:%M:%S)"
exit 1
