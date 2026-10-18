#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
clean=0; neg=0; other=0; lines=0; dirs=0
for d in corpus/fixtures/*/; do
  n=${d%/}; n=${n#corpus/fixtures/}
  out=$(python3 corpus/fixtures/check_bible.py "corpus/fixtures/$n" 2>&1); rc=$?
  dirs=$((dirs+1))
  if [ $rc -eq 0 ]; then clean=$((clean+1)); elif [ $rc -eq 1 ]; then neg=$((neg+1)); lines=$((lines+$(printf '%s\n' "$out" | grep -c '^VIOLATION'))); else other=$((other+1)); echo "NON-01 $n rc=$rc"; fi
done
echo "CENSUS dirs=$dirs clean=$clean negative=$neg violation_lines=$lines non01=$other"
