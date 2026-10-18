#!/bin/sh
cd /home/vgpnk/Projects/shokunin/lore-shokunin
n=0
while [ $n -lt 30 ]; do
  v12=no; v18=no
  ls .ufo/waves/round-102/seats/V12-*.md >/dev/null 2>&1 && v12=yes
  ls .ufo/waves/round-102/seats/V18-*.md >/dev/null 2>&1 && v18=yes
  echo "GRACE t=$((n*20))s V12=$v12 V18=$v18"
  [ "$v12" = yes ] && [ "$v18" = yes ] && { echo "GRACE_HIT t=$((n*20))s"; exit 0; }
  sleep 20; n=$((n+1))
done
echo "GRACE_TERMINAL deadline=600s V12=$v12 V18=$v18"
exit 0
