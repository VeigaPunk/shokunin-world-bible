#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
LOG=.ufo/waves/round-98/seats/V39-scratch/poll3.log
: > "$LOG"
for i in $(seq 1 40); do
  missing=""
  [ -f corpus/knowledge/r98-clerk-scope-note.md ] || missing="$missing NOTE"
  for r in S1 S2 S3 S4 S5; do
    ls .ufo/waves/round-98/seats/${r}*.md >/dev/null 2>&1 || missing="$missing $r"
  done
  # readiness: map/README no longer r97 hashes
  m1=$(sha256sum corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md | cut -c1-8)
  m2=$(sha256sum corpus/fixtures/r98-clerk-filing/README.md | cut -c1-8)
  [ "$m1" = "49d4834e" ] && missing="$missing MAP=R97COPY"
  [ "$m2" = "d9387b7d" ] && missing="$missing README=R97COPY"
  echo "try $i $(date +%H:%M:%S) missing:${missing:-NONE}" >> "$LOG"
  [ -z "$missing" ] && exit 0
  sleep 20
done
exit 1
