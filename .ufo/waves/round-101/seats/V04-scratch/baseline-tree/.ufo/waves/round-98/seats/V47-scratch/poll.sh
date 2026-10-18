#!/usr/bin/env bash
# V47 r98 poll-wait: check producer artifacts AND producer reports.
# 20s cadence, max 40 tries. Logs one line per attempt.
set -u
REPO=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$REPO/.ufo/waves/round-98/seats
LOG=$REPO/.ufo/waves/round-98/seats/V47-scratch/poll.log
: > "$LOG"
for i in $(seq 1 40); do
  reports=$(ls "$SEATS"/S1-*.md "$SEATS"/S2-*.md "$SEATS"/S3-*.md "$SEATS"/S4-*.md "$SEATS"/S5-*.md 2>/dev/null | wc -l)
  tools_readme=$(git -C "$REPO" status --porcelain -- corpus/tools/README.md | wc -l)
  scope_note=$(test -f "$REPO/corpus/knowledge/r98-clerk-scope-note.md" && echo 1 || echo 0)
  r98_final=$(test -f "$REPO/corpus/fixtures/r98-clerk-filing/README.md" && grep -c "Round 98 clerk-filing" "$REPO/corpus/fixtures/r98-clerk-filing/README.md" || echo 0)
  dep_freeze=$(git -C "$REPO" status --porcelain -- corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json | wc -l)
  printf 'TRY %02d %s reports=%s tools_readme_mod=%s r98_scope_note=%s r98_readme=%s dep_freeze_mod=%s\n' \
    "$i" "$(date +%H:%M:%S)" "$reports" "$tools_readme" "$scope_note" "$r98_final" "$dep_freeze" >> "$LOG"
  if [ "$reports" -ge 5 ] && [ "$tools_readme" -ge 1 ] && [ "$scope_note" -ge 1 ]; then
    echo "POLL_DONE at try $i" >> "$LOG"
    exit 0
  fi
  sleep 20
done
echo "POLL_TIMEOUT after 40 tries" >> "$LOG"
exit 1
