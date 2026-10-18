#!/bin/sh
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 3
S=.ufo/waves/round-96/seats
i=0
while [ "$i" -lt 40 ]; do
  i=$((i+1))
  q2=$(ls $S/Q2*.md 2>/dev/null | tr '\n' ' ')
  v02=$(ls $S/V02*.md 2>/dev/null | tr '\n' ' ')
  v30=$(ls $S/V30*.md 2>/dev/null | tr '\n' ' ')
  n=$(ls $S/*.md 2>/dev/null | wc -l)
  echo "POLL2 t=$((i*20)) Q2='$q2' V02='$v02' V30='$v30' reports=$n tool=$(sha256sum corpus/tools/map_obligations.py | cut -c1-8) ctr=$(sha256sum corpus/tools/map-obligations-contract.json | cut -c1-8) readme=$(sha256sum corpus/tools/README.md | cut -c1-8)"
  if [ -n "$q2" ] && [ -n "$v02" ] && [ -n "$v30" ]; then echo "POLL2_ALL_PRESENT"; exit 0; fi
  sleep 20
done
echo "POLL2_DEADLINE"
exit 1
