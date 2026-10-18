#!/bin/sh
# V47 content-gated poll for S3 + S4 r99-window-lapse delivery.
# 20s cadence, max 40 tries. Presence alone is not delivery (r98 placeholder class).
# Require:
#   1. S3-fixture-author.md exists and is nonempty
#   2. S4-fixture-docs.md exists and is nonempty
#   3. timeline.json contains clerk-lapse-recorded
#   4. sources.json contains clerk-lapse-note
#   5. fictional-excerpts.md differs from r98 (append expected) OR is a strict prefix-extension
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
FIX=$LANE/corpus/fixtures/r99-window-lapse
R98=$LANE/corpus/fixtures/r98-clerk-filing
S3=$LANE/.ufo/waves/round-99/seats/S3-fixture-author.md
S4=$LANE/.ufo/waves/round-99/seats/S4-fixture-docs.md
LOG=$LANE/.ufo/waves/round-99/seats/V47-scratch/poll.log
: > "$LOG"
i=0
while [ "$i" -lt 40 ]; do
  i=$((i + 1))
  ts=$(date '+%Y-%m-%d %H:%M:%S %z')
  s3=no; s4=no; tl=no; src=no; fic=no
  ev=0; note=0
  if [ -s "$S3" ]; then s3=yes; fi
  if [ -s "$S4" ]; then s4=yes; fi
  if [ -f "$FIX/timeline.json" ]; then
    tl=yes
    ev=$(grep -c 'clerk-lapse-recorded' "$FIX/timeline.json" 2>/dev/null || true)
  fi
  if [ -f "$FIX/sources.json" ]; then
    src=yes
    note=$(grep -c 'clerk-lapse-note' "$FIX/sources.json" 2>/dev/null || true)
  fi
  if [ -f "$FIX/fictional-excerpts.md" ] && [ -f "$R98/fictional-excerpts.md" ]; then
    fic=yes
    if cmp -s "$R98/fictional-excerpts.md" "$FIX/fictional-excerpts.md"; then
      fic=identical
    else
      fic=differs
    fi
  fi
  echo "try=$i ts=$ts s3=$s3 s4=$s4 tl=$tl ev=$ev src=$src note=$note fic=$fic" | tee -a "$LOG"
  if [ "$ev" -ge 1 ] && [ "$note" -ge 1 ] && [ "$s3" = yes ] && [ "$s4" = yes ] && [ "$fic" = differs ]; then
    echo "HIT try=$i ts=$ts" | tee -a "$LOG"
    exit 0
  fi
  if [ "$i" -ge 40 ]; then
    break
  fi
  sleep 20
done
echo "ABSENT after $i tries ts=$(date '+%Y-%m-%d %H:%M:%S %z')" | tee -a "$LOG"
exit 1
