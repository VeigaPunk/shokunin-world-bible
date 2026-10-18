#!/bin/bash
# V41 poll-wait: 20s cadence, 40 tries. Waits for S1-S5 producer reports AND artifacts.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 1
S=.ufo/waves/round-98/seats
LOG=$S/V41-scratch/poll.log
for i in $(seq 1 40); do
  ts=$(date -u +%H:%M:%S)
  reports=$(ls "$S" 2>/dev/null | grep -E '^S[1-5]-.*\.md$' | sort | tr '\n' ' ')
  n=$(printf '%s' "$reports" | tr ' ' '\n' | grep -c '\.md' || true)
  tools_changed=$(git status --porcelain -- corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json | wc -l)
  r98_pinned=$(python3 -c "import json;c=json.load(open('corpus/tools/dependency-freeze-contract.json'));print('r98-clerk-filing' in c.get('pins',{}))" 2>/dev/null)
  r97_pinned=$(python3 -c "import json;c=json.load(open('corpus/tools/dependency-freeze-contract.json'));print('r97-crossing-acknowledgment' in c.get('pins',{}))" 2>/dev/null)
  echo "$ts try=$i reports_n=$n [$reports] tools_changed=$tools_changed r98_pinned=$r98_pinned r97_pinned=$r97_pinned" >> "$LOG"
  if [ "$n" -ge 5 ] && [ "$tools_changed" -ge 1 ] && [ "$r98_pinned" = "True" ]; then
    echo "$ts ALL-LANDED" >> "$LOG"
    exit 0
  fi
  sleep 20
done
echo "$(date -u +%H:%M:%S) POLL-EXHAUSTED" >> "$LOG"
exit 1
