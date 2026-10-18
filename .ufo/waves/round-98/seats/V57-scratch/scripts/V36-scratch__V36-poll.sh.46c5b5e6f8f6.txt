#!/bin/bash
# V36 poll-watch: 20s cadence, tracks seat reports + producer artifacts.
# READY when all 5 producer reports (S1-S5) present AND r98 fixture dir >=10 files
# AND dependency_freeze.py differs from baseline. Stall-escape: exit if READY held
# and report count unchanged for 60 tries. Hard cap 150 tries (~50 min).
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 1
LOG=.ufo/waves/round-98/seats/V36-scratch/V36-poll.log
BASE_FREEZE=$(git show 9a3d648:corpus/tools/dependency_freeze.py | sha256sum | cut -c1-64)
prev=""; stall=0
for i in $(seq 1 150); do
  n=$(ls .ufo/waves/round-98/seats/*.md 2>/dev/null | wc -l)
  prod=$(ls .ufo/waves/round-98/seats/S[1-5]-*.md 2>/dev/null | wc -l)
  fix=$(ls corpus/fixtures/r98-clerk-filing 2>/dev/null | wc -l)
  kn=$(ls corpus/knowledge/r98-clerk-scope-note.md 2>/dev/null | wc -l)
  cur_freeze=$(sha256sum corpus/tools/dependency_freeze.py 2>/dev/null | cut -c1-64)
  [ "$cur_freeze" != "$BASE_FREEZE" ] && fm=MOD || fm=SAME
  pmd=$(find /home/vgpnk/Projects/shokunin/.ufo/waves/round-98 -name '*.md' 2>/dev/null | wc -l)
  echo "$(date '+%H:%M:%S') try=$i reports=$n producers=$prod r98fix=$fix know=$kn freeze=$fm parent_md=$pmd" >> $LOG
  ready=0
  [ "$prod" -ge 5 ] && [ "$fix" -ge 10 ] && [ "$kn" -ge 1 ] && [ "$fm" = MOD ] && ready=1
  if [ "$n" = "$prev" ]; then stall=$((stall+1)); else stall=0; prev=$n; fi
  if [ "$ready" = 1 ] && [ "$stall" -ge 60 ]; then
    echo "$(date '+%H:%M:%S') STALL READY held, reports=$n unchanged for $stall tries; exiting" >> $LOG
    exit 0
  fi
  sleep 20
done
echo "$(date '+%H:%M:%S') HARD-CAP 150 tries reached; exiting" >> $LOG
