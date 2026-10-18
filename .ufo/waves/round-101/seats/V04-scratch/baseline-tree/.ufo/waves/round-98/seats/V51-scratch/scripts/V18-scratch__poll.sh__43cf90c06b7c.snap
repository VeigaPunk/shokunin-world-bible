#!/usr/bin/env bash
# V18 poller: wait for all five producer reports (S1..S5) AND the frozen artifacts
# to exist, then require a 3-consecutive stable combined sha before declaring POLL_STABLE.
# 20 s cadence, 40-try budget. Writes only under V18-scratch.
set -u
REPO=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS="$REPO/.ufo/waves/round-98/seats"
LOG="$SEATS/V18-scratch/poll.log"
: > "$LOG"
combined() {
  cd "$REPO" || exit 1
  {
    for f in \
      corpus/tools/dependency_freeze.py \
      corpus/tools/dependency-freeze-contract.json \
      corpus/tools/README.md \
      corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md \
      corpus/fixtures/r98-clerk-filing/entities.json \
      corpus/fixtures/r98-clerk-filing/relations.json \
      corpus/fixtures/r98-clerk-filing/timeline.json \
      corpus/fixtures/r98-clerk-filing/sources.json \
      corpus/fixtures/r98-clerk-filing/contradictions.json \
      corpus/fixtures/r98-clerk-filing/fictional-excerpts.md \
      corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md \
      corpus/fixtures/r98-clerk-filing/README.md \
      corpus/knowledge/r98-clerk-scope-note.md ; do
      if [ -f "$f" ]; then sha256sum "$f"; else echo "MISSING $f"; fi
    done
  } | sha256sum | awk '{print $1}'
}
prev=""; stable=0
for try in $(seq 1 40); do
  reports=0
  for n in 1 2 3 4 5; do
    ls "$SEATS"/S${n}-*.md >/dev/null 2>&1 && reports=$((reports+1))
  done
  have=0
  for f in corpus/fixtures/r98-clerk-filing/timeline.json corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md corpus/knowledge/r98-clerk-scope-note.md; do
    [ -f "$REPO/$f" ] && have=$((have+1))
  done
  # artifact sanity: timeline must carry the tick-14 event, entities 6, contract r98 pin + 17 cases
  beat=0
  if [ -f "$REPO/corpus/fixtures/r98-clerk-filing/timeline.json" ]; then
    python3 - <<'PY' && beat=1
import json,sys
t=json.load(open('/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r98-clerk-filing/timeline.json'))
e=json.load(open('/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r98-clerk-filing/entities.json'))
c=json.load(open('/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency-freeze-contract.json'))
ok = (len(t)==7 and len(e)==6 and 'r98-clerk-filing' in c['pins'] and 'r97-crossing-acknowledgment' in c['pins']
      and len(c['self_test']['expected'])==17)
sys.exit(0 if ok else 1)
PY
  fi
  sha=$(combined)
  if [ "$sha" = "$prev" ]; then stable=$((stable+1)); else stable=0; fi
  prev="$sha"
  echo "POLL_CHECK try=$try t=$((try*20))s reports=$reports/5 artifacts=$have/3 beat=$beat stable=$stable sha=$sha" >> "$LOG"
  if [ "$reports" -eq 5 ] && [ "$have" -eq 3 ] && [ "$beat" -eq 1 ] && [ "$stable" -ge 3 ]; then
    echo "POLL_STABLE try=$try sha=$sha reports=5 artifacts=3 beat=1" >> "$LOG"
    echo "POLL_STABLE try=$try sha=$sha"
    exit 0
  fi
  sleep 20
done
echo "POLL_ABSENT" >> "$LOG"
echo "POLL_ABSENT"
exit 3
