#!/bin/bash
# V04 r97 poll: wait for R1 report + R1/R2 artifacts, then sha stability.
REPO=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$REPO/.ufo/waves/round-97/seats
TOOL=$REPO/corpus/tools/map_obligations.py
CONTRACT=$REPO/corpus/tools/map-obligations-contract.json
n=0
while [ $n -lt 40 ]; do
  n=$((n+1))
  rep=$(ls $SEATS/R1-*.md 2>/dev/null | head -1)
  if [ -n "$rep" ] && [ -f "$TOOL" ] && [ -f "$CONTRACT" ]; then
    echo "POLL_HIT try=$n report=$rep"
    break
  fi
  echo "POLL_CHECK try=$n t=$((n*20))s report=${rep:-none} tool=$(test -f $TOOL && echo yes || echo no)"
  sleep 20
done
if [ -z "$rep" ]; then echo "POLL_ABSENT tries=$n"; exit 3; fi
# sha stability: 3 consecutive checks 20s apart, all identical
prev=""
stable=0
for i in $(seq 1 12); do
  cur=$(sha256sum $TOOL $CONTRACT | sha256sum | cut -d' ' -f1)
  if [ "$cur" = "$prev" ]; then stable=$((stable+1)); else stable=0; fi
  echo "STAB_CHECK i=$i sha=$cur stable=$stable"
  if [ $stable -ge 3 ]; then echo "POLL_STABLE sha=$cur"; exit 0; fi
  prev=$cur
  sleep 20
done
echo "POLL_UNSTABLE last=$prev"; exit 4
