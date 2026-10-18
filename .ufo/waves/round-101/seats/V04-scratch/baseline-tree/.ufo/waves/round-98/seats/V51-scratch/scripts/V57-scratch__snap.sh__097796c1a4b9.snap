#!/bin/bash
# V57 quick snapshot: report counts, absent V seats, live poll procs, tails of key poll logs.
R=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$R/.ufo/waves/round-98/seats
OUT=$S/V57-scratch/checks.log
{
echo "===== $(date -u +%H:%M:%SZ) round_elapsed_min=$(( ($(date +%s) - 1792279656) / 60 ))"
echo "reports: total=$(ls $S/*.md 2>/dev/null | wc -l) S=$(ls $S/S[1-5]-*.md 2>/dev/null | wc -l) V=$(ls $S/V[0-9][0-9]-*.md 2>/dev/null | wc -l)"
echo "absent_V: $(for k in $(seq -w 1 59); do ls $S/V$k-*.md >/dev/null 2>&1 || printf 'V%s ' $k; done)"
echo "absent_S: $(for k in 1 2 3 4 5; do ls $S/S$k-*.md >/dev/null 2>&1 || printf 'S%s ' $k; done)"
echo "live_poll_procs: $(ps -eo cmd | grep -E 'round-98.*(poll|watch)|lore-shokunin.*(poll\.sh|watch\.py)' | grep -v V57-scratch | grep -vc grep)"
for s in V58 V30 V19 V43 V49 V50 V24 V35 V40 V56 V36 V59 V51 V27 V26 V20 V45; do
  for d in $S/$s-scratch $R/.ufo/waves/round-98/scratch/$s; do
    f=$(ls $d/*poll*.log $d/*poll*.out 2>/dev/null | head -1)
    [ -n "$f" ] && echo "[$s] $(tail -1 $f | cut -c1-170)"
  done
done
echo "newest_reports: $(ls -t $S/*.md 2>/dev/null | head -6 | xargs -n1 basename | tr '\n' ' ')"
} >> $OUT
tail -n 26 $OUT
