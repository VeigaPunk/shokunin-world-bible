#!/bin/sh
# V44 r96 poll-wait 2: wait for Q2's contract/README rewrite + Q2 report.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
s=0; n=0
while [ "$s" -lt 800 ]; do
  rep=$(ls .ufo/waves/round-96/seats/Q2-*.md 2>/dev/null | wc -l)
  c1=$(stat -c %Y corpus/tools/map-obligations-contract.json 2>/dev/null || echo 0)
  c2=$(stat -c %Y corpus/tools/README.md 2>/dev/null || echo 0)
  ref=$(date -d '2026-10-17 17:40:00' +%s)
  if [ "$rep" -ge 1 ] && [ "$c1" -gt "$ref" ] && [ "$c2" -gt "$ref" ]; then
    echo "POLL2_HIT elapsed=${s}s checks=$n q2_report=$rep contract_mtime=$c1 readme_mtime=$c2"
    exit 0
  fi
  sleep 20; s=$((s+20)); n=$((n+1))
  echo "POLL2_CHECK t=${s}s q2_report=$rep contract_fresh=$([ "$c1" -gt "$ref" ] && echo yes || echo no) readme_fresh=$([ "$c2" -gt "$ref" ] && echo yes || echo no)"
done
echo "POLL2_DEADLINE elapsed=${s}s q2_report=$rep contract_mtime=$c1 readme_mtime=$c2"
exit 1
