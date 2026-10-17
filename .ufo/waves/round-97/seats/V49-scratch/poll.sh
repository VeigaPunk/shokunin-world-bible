#!/usr/bin/env bash
# V49 poll-wait: 6 producer reports + r97 artifacts, 20s cadence, 40 tries
set -u
cd /home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=.ufo/waves/round-97/seats
FIX=corpus/fixtures/r97-crossing-acknowledgment
LOG=$SEATS/V49-scratch/poll.log
: > "$LOG"
for i in $(seq 1 40); do
  reps=$(ls "$SEATS"/R[1-6]*.md 2>/dev/null | wc -l)
  fix=$(ls "$FIX"/* 2>/dev/null | wc -l)
  note=$([ -f corpus/knowledge/r97-acknowledgment-scope-note.md ] && echo 1 || echo 0)
  r96map=$(git diff --name-only f3e09f9 -- corpus/fixtures/r96-crossing-response/ | wc -l)
  tools=$(git diff --name-only f3e09f9 -- corpus/tools/ | wc -l)
  echo "try=$i reports=$reps/6 r97fixfiles=$fix scope_note=$note r96map_changed=$r96map tools_changed=$tools" | tee -a "$LOG"
  if [ "$reps" -ge 6 ]; then
    echo "ALL_PRODUCER_REPORTS_PRESENT after try=$i" | tee -a "$LOG"
    ls "$SEATS"/R[1-6]*.md >> "$LOG" 2>&1
    exit 0
  fi
  sleep 20
done
echo "POLL_TIMEOUT: reports=$(ls "$SEATS"/R[1-6]*.md 2>/dev/null | wc -l)/6" | tee -a "$LOG"
ls -la "$SEATS" >> "$LOG" 2>&1
exit 1
