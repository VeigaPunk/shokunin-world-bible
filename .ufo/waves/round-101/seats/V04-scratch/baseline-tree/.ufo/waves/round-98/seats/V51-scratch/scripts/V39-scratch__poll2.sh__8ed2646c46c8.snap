#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
LOG=.ufo/waves/round-98/seats/V39-scratch/poll2.log
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
  # content-readiness: clerk-maren entity present + tick-14 event present + knowledge note nonempty
  g1=$(grep -c clerk-maren corpus/fixtures/r98-clerk-filing/entities.json 2>/dev/null || echo 0)
  g2=$(grep -c clerk-filing-open corpus/fixtures/r98-clerk-filing/timeline.json 2>/dev/null || echo 0)
  echo "try $i $(date +%H:%M:%S) missing:${missing:-NONE} clerk-maren=$g1 tick14=$g2" >> "$LOG"
  [ -z "$missing" ] && exit 0
  sleep 20
done
exit 1
