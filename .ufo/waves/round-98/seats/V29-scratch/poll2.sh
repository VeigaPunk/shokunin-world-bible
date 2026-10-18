#!/bin/sh
root=/home/vgpnk/Projects/shokunin/lore-shokunin
n=0; s=0
while [ "$s" -lt 840 ]; do
  r1=no; r2=no; r5=no
  ls "$root/.ufo/waves/round-98/seats/"S1*.md >/dev/null 2>&1 && r1=yes
  ls "$root/.ufo/waves/round-98/seats/"S2*.md >/dev/null 2>&1 && r2=yes
  ls "$root/.ufo/waves/round-98/seats/"S5*.md >/dev/null 2>&1 && r5=yes
  h=$(sha256sum "$root/corpus/tools/dependency_freeze.py" | cut -c1-8)
  hr=$(sha256sum "$root/corpus/tools/README.md" | cut -c1-8)
  echo "POLL2 t=${s}s S1rep=$r1 S2rep=$r2 S5rep=$r5 df=${h} readme=${hr}"
  if [ "$r1" = yes ] && [ "$r2" = yes ] && [ "$r5" = yes ]; then echo "POLL2_HIT elapsed=${s}s"; exit 0; fi
  sleep 20; s=$((s+20)); n=$((n+1))
done
echo "POLL2_TERMINAL deadline elapsed=${s}s"; exit 0
