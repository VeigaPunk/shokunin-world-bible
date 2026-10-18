#!/usr/bin/env bash
# V49 r99 poll-wait: producer artifacts AND producer reports.
# 20s cadence, max 40 tries. Never counts SELF.
set -u
REPO=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$REPO/.ufo/waves/round-99/seats
LOG=$SEATS/V49-scratch/poll.log
: > "$LOG"
for i in $(seq 1 40); do
  reports=$(ls "$SEATS"/S1-*.md "$SEATS"/S2-*.md "$SEATS"/S3-*.md "$SEATS"/S4-*.md "$SEATS"/S5-*.md 2>/dev/null | wc -l)
  tools_readme=$(git -C "$REPO" status --porcelain -- corpus/tools/README.md | wc -l)
  skill_mod=$(git -C "$REPO" status --porcelain -- SKILL.md | wc -l)
  dep_freeze=$(git -C "$REPO" status --porcelain -- corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json | wc -l)
  lapse_note=$(test -f "$REPO/corpus/knowledge/r99-lapse-scope-note.md" && echo 1 || echo 0)
  blind=$(test -f "$REPO/corpus/knowledge/r99-gate-blind-spot-table.md" && echo 1 || echo 0)
  r99_map=$(test -f "$REPO/corpus/fixtures/r99-window-lapse/claim-excerpt-map.md" && echo 1 || echo 0)
  inv=$(grep -c '21 JSON facts' "$REPO/corpus/fixtures/r99-window-lapse/claim-excerpt-map.md" 2>/dev/null || echo 0)
  ns=$(grep -c 'r99-window-lapse:' "$REPO/corpus/fixtures/r99-window-lapse/claim-excerpt-map.md" 2>/dev/null || echo 0)
  printf 'TRY %02d %s reports=%s tools_readme_mod=%s skill_mod=%s dep_freeze_mod=%s lapse_note=%s blind_table=%s r99_map=%s inv21=%s ns=%s\n' \
    "$i" "$(date +%H:%M:%S)" "$reports" "$tools_readme" "$skill_mod" "$dep_freeze" "$lapse_note" "$blind" "$r99_map" "$inv" "$ns" >> "$LOG"
  if [ "$reports" -ge 5 ] && [ "$tools_readme" -ge 1 ] && [ "$lapse_note" -ge 1 ] && [ "$blind" -ge 1 ] && [ "$inv" -ge 1 ]; then
    echo "POLL_DONE at try $i" >> "$LOG"
    exit 0
  fi
  sleep 20
done
echo "POLL_TIMEOUT after 40 tries" >> "$LOG"
exit 1
