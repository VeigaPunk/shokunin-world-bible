#!/bin/sh
# V22 poll: wait for Q3 artifacts + Q3 producer report
TOOL=/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency_freeze.py
CONTR=/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency-freeze-contract.json
SEATS=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-96/seats
n=0
while [ "$n" -lt 40 ]; do
  rep=$(ls "$SEATS"/Q3* 2>/dev/null | head -1)
  if [ -f "$TOOL" ] && [ -f "$CONTR" ] && [ -n "$rep" ]; then
    echo "POLL_HIT checks=$n tool=$(stat -c%s $TOOL) contr=$(stat -c%s $CONTR) report=$rep"
    exit 0
  fi
  sleep 20; n=$((n+1))
  echo "POLL_CHECK t=$((n*20))s tool=$([ -f $TOOL ] && echo yes || echo no) contr=$([ -f $CONTR ] && echo yes || echo no) report=${rep:-no}"
done
echo "POLL_TIMEOUT checks=$n"
exit 0
