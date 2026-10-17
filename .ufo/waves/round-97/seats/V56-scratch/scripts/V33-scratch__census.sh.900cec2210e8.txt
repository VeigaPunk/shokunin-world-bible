#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
clean=0; neg=0; other=0; lines=0; total=0
for d in corpus/fixtures/*/; do
  total=$((total+1))
  out=$(TMPDIR=$PWD/.ufo/waves/round-97/seats/V33-scratch/tmp python3 corpus/fixtures/check_bible.py "$d" 2>&1); rc=$?
  n=$(printf '%s\n' "$out" | grep -c "VIOLATION" || true)
  lines=$((lines+n))
  case $rc in 0) clean=$((clean+1));; 1) neg=$((neg+1));; *) other=$((other+1)); echo "OTHER($rc): $d";; esac
done
echo "CENSUS dirs=$total clean=$clean negative=$neg other=$other violation_lines=$lines"
