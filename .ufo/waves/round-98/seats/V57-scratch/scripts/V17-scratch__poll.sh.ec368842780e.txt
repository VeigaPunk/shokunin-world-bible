#!/bin/sh
# V17 poll: 20s cadence, 40 tries. Waits for r98 fixture (10 files), r98 note,
# r95/r96 note addenda, and >=5 producer reports under round-98/seats.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 1
S=.ufo/waves/round-98/seats
i=0
while [ "$i" -lt 40 ]; do
  i=$((i+1))
  nfix=$(ls corpus/fixtures/r98-clerk-filing/ 2>/dev/null | wc -l)
  note=$( [ -e corpus/knowledge/r98-clerk-scope-note.md ] && echo 1 || echo 0 )
  a95=$(grep -c -i 'r98' corpus/knowledge/r95-aftermath-scope-note.md 2>/dev/null || echo 0)
  a96=$(grep -c -i 'r98' corpus/knowledge/r96-response-scope-note.md 2>/dev/null || echo 0)
  nrep=$(ls $S/R*.md 2>/dev/null | wc -l)
  echo "POLL t=${i} fixture_files=$nfix note=$note r95_addendum_hits=$a95 r96_addendum_hits=$a96 reports=$nrep $(ls $S/R*.md 2>/dev/null | tr '\n' ' ')"
  if [ "$nfix" -ge 10 ] && [ "$note" = 1 ] && [ "$a95" -ge 1 ] && [ "$a96" -ge 1 ] && [ "$nrep" -ge 5 ]; then
    echo "POLL_FULL_SET t=${i}"
    exit 0
  fi
  sleep 20
done
echo "POLL_DEADLINE t=40"
exit 0
