#!/bin/bash
# V32 poll: producer artifacts + seat landings, 20s x 40 (round-98, lore-shokunin)
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 1
S=.ufo/waves/round-98/seats/V32-scratch
LOG=$S/poll.log
: > "$LOG"
for i in $(seq 0 39); do
  ts=$(date +%H:%M:%S)
  s1t=$(sha256sum corpus/tools/dependency_freeze.py 2>/dev/null | cut -c1-8); [ -z "$s1t" ] && s1t=ABSENT
  s1c=$(sha256sum corpus/tools/dependency-freeze-contract.json 2>/dev/null | cut -c1-8); [ -z "$s1c" ] && s1c=ABSENT
  s2=$(sha256sum corpus/tools/README.md 2>/dev/null | cut -c1-8); [ -z "$s2" ] && s2=ABSENT
  s3m=$(sha256sum corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md 2>/dev/null | cut -c1-8); [ -z "$s3m" ] && s3m=ABSENT
  fx=$(ls corpus/fixtures/r98-clerk-filing/ 2>/dev/null | wc -l)
  fxh=$(cd corpus/fixtures/r98-clerk-filing 2>/dev/null && find . -type f | sort | xargs sha256sum 2>/dev/null | sha256sum | cut -c1-8); [ -z "$fxh" ] && fxh=NA
  s5a=$(sha256sum corpus/knowledge/r98-clerk-scope-note.md 2>/dev/null | cut -c1-8); [ -z "$s5a" ] && s5a=ABSENT
  s5b=$(sha256sum corpus/knowledge/r95-aftermath-scope-note.md 2>/dev/null | cut -c1-8); [ -z "$s5b" ] && s5b=ABSENT
  s5c=$(sha256sum corpus/knowledge/r96-response-scope-note.md 2>/dev/null | cut -c1-8); [ -z "$s5c" ] && s5c=ABSENT
  prods=$(ls .ufo/waves/round-98/seats/ 2>/dev/null | grep -cE '^S[0-9].*\.md$')
  seats=$(ls .ufo/waves/round-98/seats/*.md 2>/dev/null | wc -l)
  if [ -f /home/vgpnk/Projects/shokunin/.ufo/reports/round-98/lore.md ]; then fleet=YES; else fleet=no; fi
  echo "$i $ts s1t=$s1t s1c=$s1c s2=$s2 s3m=$s3m fx=$fx fxh=$fxh s5a=$s5a s5b=$s5b s5c=$s5c prods=$prods seats=$seats fleet=$fleet" >> "$LOG"
  sleep 20
done
echo "POLL DONE $(date +%H:%M:%S)" >> "$LOG"
