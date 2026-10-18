#!/bin/bash
# V39 poll: wait for r98 artifacts + producer reports (S3/S4/S5)
cd /home/vgpnk/Projects/shokunin/lore-shokunin
LOG=.ufo/waves/round-98/seats/V39-scratch/poll.log
: > "$LOG"
for i in $(seq 1 40); do
  missing=""
  for p in corpus/fixtures/r98-clerk-filing/entities.json \
           corpus/fixtures/r98-clerk-filing/sources.json \
           corpus/fixtures/r98-clerk-filing/timeline.json \
           corpus/fixtures/r98-clerk-filing/fictional-excerpts.md \
           corpus/fixtures/r98-clerk-filing/README.md \
           corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md \
           corpus/knowledge/r98-clerk-scope-note.md; do
    [ -f "$p" ] || missing="$missing $p"
  done
  for r in S1 S2 S3 S4 S5; do
    ls .ufo/waves/round-98/seats/${r}*.md >/dev/null 2>&1 || missing="$missing REPORT:$r"
  done
  echo "try $i $(date +%H:%M:%S) missing:${missing:-NONE}" >> "$LOG"
  [ -z "$missing" ] && exit 0
  sleep 20
done
exit 1
