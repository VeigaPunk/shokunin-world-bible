#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
clean=0; neg=0; other=0; lines=0; total=0; otherlist=""
for d in corpus/fixtures/*/; do
  name=${d%/}
  total=$((total+1))
  out=$(python3 corpus/fixtures/check_bible.py "$name" 2>/dev/null); rc=$?
  case $rc in
    0) clean=$((clean+1));;
    1) neg=$((neg+1));;
    *) other=$((other+1)); otherlist="$otherlist $name:$rc";;
  esac
  n=$(printf '%s\n' "$out" | grep -c "^VIOLATION")
  lines=$((lines+n))
done
echo "CENSUS dirs=$total clean=$clean negative=$neg other=$other violation_lines=$lines"
[ -n "$otherlist" ] && echo "OTHER:$otherlist"
