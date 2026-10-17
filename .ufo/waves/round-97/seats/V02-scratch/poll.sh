#!/bin/sh
# V02 r97 poll: R1 report + R2 report + contract 25 cases w/ dual_pointer + tool dual_pointer prepare branch.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
S=.ufo/waves/round-97/seats
i=0
while [ "$i" -lt 40 ]; do
  i=$((i+1))
  r1=$(find "$S" -maxdepth 1 -type f -name 'R1-*.md' | head -1)
  r2=$(find "$S" -maxdepth 1 -type f -name 'R2-*.md' | head -1)
  ccheck=$(python3 - <<'EOF'
import json
try:
    c = json.load(open('corpus/tools/map-obligations-contract.json'))
    ids = [x.get('id') for x in c.get('self_test', {}).get('cases', [])]
    print(len(ids), 'dual_pointer' in ids)
except Exception:
    print(0, False)
EOF
)
  dq=$(grep -c 'case_name == "dual_pointer"' corpus/tools/map_obligations.py 2>/dev/null || true)
  echo "$(date '+%T') try=$i r1=${r1:-no} r2=${r2:-no} contract=[$ccheck] dqbranch=${dq:-0}"
  if [ -n "$r1" ] && [ -n "$r2" ] && [ "$ccheck" = "25 True" ] && [ "${dq:-0}" -ge 1 ]; then
    echo "READY try=$i r1=$r1 r2=$r2 contract=25 dqbranch=$dq"
    exit 0
  fi
  sleep 20
done
echo "POLL_DEADLINE after 40 tries"
exit 1
