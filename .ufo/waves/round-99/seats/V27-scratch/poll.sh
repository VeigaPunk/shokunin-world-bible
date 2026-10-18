#!/bin/bash
# V27 adjacency poller — 20s cadence, 40 tries. Logs producer artifacts + reports.
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS="$LANE/.ufo/waves/round-99/seats"
LOG="$SEATS/V27-scratch/poll.log"
cd "$LANE" || exit 1
for i in $(seq 1 40); do
  ts=$(date '+%Y-%m-%d %H:%M:%S %z')
  reports=$(ls -1 "$SEATS" 2>/dev/null | grep -E '^(S[1-5]|V[0-9]+)-' | grep -v scratch || true)
  nrep=$(printf '%s\n' "$reports" | grep -c . || true)
  sreps=$(printf '%s\n' "$reports" | grep -E '^S[1-5]-' | tr '\n' ' ' || true)
  fix=$(ls -1 corpus/fixtures/r99-window-lapse 2>/dev/null | wc -l)
  table=ABSENT; note=ABSENT
  test -f corpus/knowledge/r99-gate-blind-spot-table.md && table=PRESENT
  test -f corpus/knowledge/r99-lapse-scope-note.md && note=PRESENT
  # hashes of producer-owned tracked files (short)
  hfreeze=$(sha256sum corpus/tools/dependency_freeze.py 2>/dev/null | cut -c1-12)
  hcontract=$(sha256sum corpus/tools/dependency-freeze-contract.json 2>/dev/null | cut -c1-12)
  hreadme=$(sha256sum corpus/tools/README.md 2>/dev/null | cut -c1-12)
  hskill=$(sha256sum SKILL.md 2>/dev/null | cut -c1-12)
  hprov=$(sha256sum PROVINCE.md 2>/dev/null | cut -c1-12)
  echo "try=$i ts=$ts reports=$nrep sreps=[$sreps] fixfiles=$fix table=$table note=$note freeze=$hfreeze contract=$hcontract toolsreadme=$hreadme skill=$hskill province=$hprov" >> "$LOG"
  # early exit once all 5 producer reports exist AND both knowledge files exist AND fixture has files
  ns=$(printf '%s\n' "$reports" | grep -cE '^S[1-5]-' || true)
  if [ "$ns" -ge 5 ] && [ "$table" = PRESENT ] && [ "$note" = PRESENT ] && [ "$fix" -ge 10 ]; then
    echo "POLL_READY try=$i ts=$ts" >> "$LOG"
    exit 0
  fi
  sleep 20
done
echo "POLL_END $(date '+%Y-%m-%d %H:%M:%S %z') tries=40" >> "$LOG"
exit 2
