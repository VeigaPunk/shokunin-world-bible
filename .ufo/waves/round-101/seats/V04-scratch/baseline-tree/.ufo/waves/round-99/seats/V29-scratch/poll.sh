#!/bin/bash
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
SCR=$LANE/.ufo/waves/round-99/seats/V29-scratch
cd "$LANE" || exit 1
for i in $(seq 1 40); do
  sleep 20
  ts=$(date -Is)
  fx=$(ls corpus/fixtures/r99-window-lapse 2>/dev/null | wc -l)
  kn=$(ls corpus/knowledge/r99-*.md 2>/dev/null | wc -l)
  s3=$(test -f .ufo/waves/round-99/seats/S3-fixture-author.md && echo YES || echo NO)
  # discover S3/S4/S5 report names dynamically
  s3f=$(ls .ufo/waves/round-99/seats/S3*.md 2>/dev/null | head -1)
  s4f=$(ls .ufo/waves/round-99/seats/S4*.md 2>/dev/null | head -1)
  s5f=$(ls .ufo/waves/round-99/seats/S5*.md 2>/dev/null | head -1)
  md=$(ls .ufo/waves/round-99/seats/*.md 2>/dev/null | wc -l)
  echo "POLL $ts try=$i fixture_files=$fx knowledge=$kn S3=${s3f:-ABSENT} S4=${s4f:-ABSENT} S5=${s5f:-ABSENT} seat_md=$md" >> "$SCR/poll.log"
  # also snapshot hashes each try
  sha256sum corpus/fixtures/r99-window-lapse/* 2>/dev/null | awk '{print $1}' | sort | sha256sum >> "$SCR/poll-hashchain.txt"
  if [ -n "$s3f" ] && [ -n "$s4f" ] && [ -n "$s5f" ] && [ "$kn" -ge 2 ]; then
    echo "GATE-MET $ts try=$i" >> "$SCR/poll.log"
    # keep polling a bit? protocol says check artifacts AND producer reports exist. Gate met → exit.
    exit 0
  fi
done
echo "POLL-EXHAUSTED $(date -Is)" >> "$SCR/poll.log"
exit 0
