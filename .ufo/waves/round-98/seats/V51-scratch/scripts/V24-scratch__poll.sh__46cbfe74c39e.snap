#!/bin/sh
# V24 r98 adjacency poller: 20s cadence, N tries (default 40), logs reports + artifact signature.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 1
S=.ufo/waves/round-98/seats
LOG=$S/V24-scratch/poll.log
N=${1:-40}
n=0
echo "POLL_START $(date '+%Y-%m-%d %H:%M:%S %z') tries=$N" >> "$LOG"
while [ "$n" -lt "$N" ]; do
  n=$((n+1))
  repnames=$(ls "$S"/*.md 2>/dev/null | xargs -r -n1 basename | grep -v '^V24' | sort | tr '\n' ' ')
  reports=$(printf '%s' "$repnames" | wc -w)
  fix=$(ls corpus/fixtures/r98-clerk-filing/ 2>/dev/null | wc -l)
  fixsig=$(ls corpus/fixtures/r98-clerk-filing/ 2>/dev/null | md5sum | cut -c1-8)
  note=$([ -f corpus/knowledge/r98-clerk-scope-note.md ] && echo 1 || echo 0)
  toolsig=""
  for f in corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json corpus/tools/README.md corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md; do
    h=$(sha256sum "$f" 2>/dev/null | cut -c1-8)
    toolsig="$toolsig$h:"
  done
  por=$(git status --porcelain -uall 2>/dev/null | wc -l)
  echo "T=$(date '+%H:%M:%S') n=$n reports=$reports [$repnames] r98fix=$fix sig=$fixsig note=$note tools=$toolsig porcelain=$por" >> "$LOG"
  sleep 20
done
echo "POLL_END $(date '+%Y-%m-%d %H:%M:%S %z') tries=$n" >> "$LOG"
