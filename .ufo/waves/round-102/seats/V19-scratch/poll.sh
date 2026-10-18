#!/bin/sh
cd /home/vgpnk/Projects/shokunin/lore-shokunin
S=.ufo/waves/round-102/seats
n=0
while [ $n -lt 60 ]; do
  others=$(ls "$S"/*.md 2>/dev/null | grep -cv '/V19-')
  u1a=no; u1b=no; u2=no; rec=no
  [ -s corpus/knowledge/r102-push-synthesis-r95-r102.md ] && u1a=yes
  [ -s corpus/knowledge/r102-debt-ledger.json ] && u1b=yes
  [ -s corpus/knowledge/r102-freshness-sweep.md ] && u2=yes
  [ -e .ufo/waves/round-102/receipt.json ] && rec=yes
  echo "POLL t=$((n*20))s others=$others synth=$u1a ledger=$u1b fresh=$u2 receipt=$rec"
  if [ "$others" -ge 18 ] && [ "$u1a" = yes ] && [ "$u1b" = yes ] && [ "$u2" = yes ]; then
    echo "POLL_HIT elapsed=$((n*20))s others=$others"; exit 0
  fi
  sleep 20; n=$((n+1))
done
echo "POLL_TERMINAL deadline=1200s others=$others synth=$u1a ledger=$u1b fresh=$u2 receipt=$rec"
exit 0
