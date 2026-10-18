#!/bin/sh
# V29 poll: wait for S5 bytes (r98 note + both addenda) and producer report
root=/home/vgpnk/Projects/shokunin/lore-shokunin
n=0; s=0
while [ "$s" -lt 840 ]; do
  note=no; r95=no; r96=no; rep=no
  [ -e "$root/corpus/knowledge/r98-clerk-scope-note.md" ] && note=yes
  grep -qiE "addendum|correction" "$root/corpus/knowledge/r95-aftermath-scope-note.md" && r95=yes
  grep -qiE "addendum|correction" "$root/corpus/knowledge/r96-response-scope-note.md" && r96=yes
  ls "$root/.ufo/waves/round-98/seats/"S5*.md >/dev/null 2>&1 && rep=yes
  echo "POLL t=${s}s note=$note r95add=$r95 r96add=$r96 s5report=$rep"
  if [ "$note" = yes ] && [ "$r95" = yes ] && [ "$r96" = yes ]; then echo "POLL_HIT elapsed=${s}s checks=$n"; exit 0; fi
  sleep 20; s=$((s+20)); n=$((n+1))
done
echo "POLL_TERMINAL deadline elapsed=${s}s checks=$n"
exit 0
