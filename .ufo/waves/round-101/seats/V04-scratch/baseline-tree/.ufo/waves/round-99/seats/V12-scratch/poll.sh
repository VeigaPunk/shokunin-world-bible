#!/bin/bash
# V12 poll-wait: S4 artifacts + producer report. 20s cadence, 40 tries.
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
FIX=$LANE/corpus/fixtures/r99-window-lapse
R98=$LANE/corpus/fixtures/r98-clerk-filing
SEATS=$LANE/.ufo/waves/round-99/seats
LOG=$SEATS/V12-scratch/poll.log
: > "$LOG"
hash_of() { sha256sum "$1" 2>/dev/null | awk '{print $1}'; }
r98_map=$(hash_of "$R98/claim-excerpt-map.md")
r98_readme=$(hash_of "$R98/README.md")
echo "poll-start $(date '+%H:%M:%S') r98_map=${r98_map:0:16} r98_readme=${r98_readme:0:16}" | tee -a "$LOG"
for try in $(seq 1 40); do
  ts=$(date '+%H:%M:%S')
  map_state=absent
  readme_state=absent
  if [ -f "$FIX/claim-excerpt-map.md" ]; then
    h=$(hash_of "$FIX/claim-excerpt-map.md")
    if [ "$h" = "$r98_map" ]; then map_state=same-as-r98; else map_state=moved; fi
  fi
  if [ -f "$FIX/README.md" ]; then
    h=$(hash_of "$FIX/README.md")
    if [ "$h" = "$r98_readme" ]; then readme_state=same-as-r98; else readme_state=moved; fi
  fi
  reports=""
  for f in "$SEATS"/S4*.md; do
    [ -f "$f" ] || continue
    base=$(basename "$f")
    case "$base" in
      V12*) continue ;;
    esac
    reports="$reports $base"
  done
  reports=${reports# }
  [ -z "$reports" ] && reports=none
  line="try=$try t=$ts map=$map_state readme=$readme_state reports=$reports"
  echo "$line" | tee -a "$LOG"
  if [ "$map_state" = moved ] && [ "$readme_state" = moved ] && [ "$reports" != none ]; then
    echo "READY try=$try t=$ts" | tee -a "$LOG"
    exit 0
  fi
  sleep 20
done
echo "ABSENT after 40 tries t=$(date '+%H:%M:%S')" | tee -a "$LOG"
exit 2
