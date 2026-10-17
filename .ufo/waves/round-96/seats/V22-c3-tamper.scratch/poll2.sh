#!/bin/sh
SEATS=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-96/seats
TOOL=/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency_freeze.py
CONTR=/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency-freeze-contract.json
n=0
while [ "$n" -lt 45 ]; do
  rep=$(find "$SEATS" -maxdepth 1 -name 'Q3*.md' -type f 2>/dev/null | head -1)
  if [ -n "$rep" ]; then
    # wait for 30s of mtime stability
    m1=$(stat -c %Y "$TOOL"); c1=$(stat -c %Y "$CONTR")
    sleep 30
    m2=$(stat -c %Y "$TOOL"); c2=$(stat -c %Y "$CONTR")
    if [ "$m1" = "$m2" ] && [ "$c1" = "$c2" ]; then
      echo "POLL_STABLE checks=$n report=$rep tool_mtime=$m1 contr_mtime=$c1"; exit 0
    fi
    echo "POLL_UNSTABLE checks=$n tool=$m1->$m2 contr=$c1->$c2"
  fi
  sleep 20; n=$((n+1))
done
echo "POLL_TIMEOUT checks=$n"
exit 0
