#!/bin/sh
# V44 r96 poll-wait: wait for Q4+Q5 fixture files and all six producer reports.
# 20s cadence, up to 40 tries. Prints a terminal line on completion or deadline.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
fx=corpus/fixtures/r96-crossing-response
s=0; n=0
while [ "$s" -lt 800 ]; do
  missing=""
  for f in "$fx/README.md" "$fx/claim-excerpt-map.md" "$fx/entities.json" "$fx/relations.json" "$fx/contradictions.json" "$fx/inspiration-note.md" "$fx/source-excerpt.md" "$fx/sources.json" "$fx/timeline.json" "$fx/fictional-excerpts.md"; do
    [ -e "$f" ] || missing="$missing $f"
  done
  reports=$(ls .ufo/waves/round-96/seats/Q*.md 2>/dev/null | wc -l)
  if [ -z "$missing" ] && [ "$reports" -ge 6 ]; then
    echo "POLL_HIT elapsed=${s}s checks=$n reports=$reports fixture_files=10"
    ls .ufo/waves/round-96/seats/Q*.md
    exit 0
  fi
  sleep 20; s=$((s+20)); n=$((n+1))
  echo "POLL_CHECK t=${s}s missing='$missing' reports=$reports"
done
echo "POLL_DEADLINE elapsed=${s}s checks=$n reports=$reports missing='$missing'"
exit 1
