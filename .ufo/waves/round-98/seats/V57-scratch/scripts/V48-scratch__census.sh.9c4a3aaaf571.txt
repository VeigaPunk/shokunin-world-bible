#!/bin/bash
# V48 census replica: repo-relative check_bible over every fixture dir (r94-r97 definition)
R=/home/vgpnk/Projects/shokunin/lore-shokunin
cd "$R" || exit 9
dirs=0; clean=0; negative=0; viol=0; odd=0
for d in corpus/fixtures/*/; do
  [ -d "$d" ] || continue
  dirs=$((dirs+1))
  out=$(python3 corpus/fixtures/check_bible.py "${d%/}" 2>&1); rc=$?
  if [ $rc -eq 0 ]; then clean=$((clean+1));
  elif [ $rc -eq 1 ]; then negative=$((negative+1)); viol=$((viol+$(printf '%s\n' "$out" | grep -c 'VIOLATION')));
  else odd=$((odd+1)); echo "ODD ${d} rc=$rc"; fi
done
echo "CENSUS dirs=$dirs clean=$clean negative=$negative violation_lines=$viol non01=$odd"
