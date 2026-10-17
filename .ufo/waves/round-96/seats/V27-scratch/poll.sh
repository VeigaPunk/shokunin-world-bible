#!/bin/bash
# V27 scope-creep poll: wait for producer completion, then tree stability.
R=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$R/.ufo/waves/round-96/seats
LOG=$S/V27-scratch/poll.log
mkdir -p "$S/V27-scratch"
producers_done=0
stable=0
last_sig=""
for i in $(seq 1 46); do
  ts=$(date '+%H:%M:%S')
  qrep=$(ls $S/Q*.md 2>/dev/null | wc -l)
  dep=$([ -f $R/corpus/tools/dependency_freeze.py ] && echo 1 || echo 0)
  dfc=$([ -f $R/corpus/tools/dependency-freeze-contract.json ] && echo 1 || echo 0)
  fix=$([ -f $R/corpus/fixtures/r96-crossing-response/timeline.json ] && echo 1 || echo 0)
  note=$([ -f $R/corpus/knowledge/r96-response-scope-note.md ] && echo 1 || echo 0)
  nrep=$(ls $S/*.md 2>/dev/null | wc -l)
  nstatus=$(cd $R && git status --porcelain -uall | wc -l)
  sig="$nrep:$nstatus"
  if [ "$qrep" -ge 6 ] && [ "$dep" = 1 ] && [ "$dfc" = 1 ] && [ "$fix" = 1 ] && [ "$note" = 1 ]; then
    producers_done=1
  fi
  if [ "$producers_done" = 1 ]; then
    if [ "$sig" = "$last_sig" ]; then stable=$((stable+1)); else stable=0; fi
    last_sig="$sig"
  fi
  echo "$ts try=$i Qreports=$qrep dep=$dep dfc=$dfc fixture=$fix note=$note allreports=$nrep gitlines=$nstatus producers_done=$producers_done stable=$stable" >> "$LOG"
  if [ "$producers_done" = 1 ] && [ "$stable" -ge 4 ]; then
    echo "EXIT: producers done and tree stable for 4 consecutive tries at try $i" >> "$LOG"
    exit 0
  fi
  sleep 20
done
echo "EXIT: cap 46 tries reached (producers_done=$producers_done stable=$stable)" >> "$LOG"
if [ "$producers_done" = 1 ]; then exit 0; else exit 1; fi
