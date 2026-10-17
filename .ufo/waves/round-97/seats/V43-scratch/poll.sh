#!/bin/bash
# V43 poll-wait: 20s cadence, 40 tries. Ready when r97 fixture (10 files) exists AND R1..R6 reports exist.
cd /home/vgpnk/Projects/shokunin/lore-shokunin
S=.ufo/waves/round-97/seats
F=corpus/fixtures/r97-crossing-acknowledgment
LOG=$S/V43-scratch/poll.log
echo "POLL_START $(date -Is)" >> $LOG
for i in $(seq 1 40); do
  have=1; miss=""
  for f in entities.json relations.json contradictions.json inspiration-note.md source-excerpt.md sources.json timeline.json fictional-excerpts.md README.md claim-excerpt-map.md; do
    [ -f "$F/$f" ] || { have=0; miss="$miss $f"; }
  done
  reports=0; rmiss=""
  for r in 1 2 3 4 5 6; do
    if ls $S/R$r-*.md >/dev/null 2>&1; then reports=$((reports+1)); else rmiss="$rmiss R$r"; fi
  done
  tot=$(ls $S/*.md 2>/dev/null | wc -l)
  echo "CHECK i=$i t=$((i*20))s fixture_ok=$have miss=[$miss] producers=$reports/6 missing_reports=[$rmiss] total_reports=$tot" >> $LOG
  if [ "$have" = "1" ] && [ "$reports" = "6" ]; then echo "POLL_READY i=$i elapsed=$((i*20))s" >> $LOG; exit 0; fi
  sleep 20
done
echo "POLL_ABSENT after 40 tries" >> $LOG
exit 1
