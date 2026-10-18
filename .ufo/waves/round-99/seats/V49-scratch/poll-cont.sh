#!/usr/bin/env bash
# V49 continuation after the 300s tool timeout killed poll.sh at try 15.
# Appends; does not reset the log. Tries 16-40. Does not count SELF.
set -u
REPO=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$REPO/.ufo/waves/round-99/seats
LOG=$SEATS/V49-scratch/poll.log
echo "STALL tool-timeout killed poll.sh after try 15; resumed $(date +%H:%M:%S); gap is the tool cap, not a skipped try" >> "$LOG"
count_pat() {
  local n
  n=$(grep -c -- "$1" "$2" 2>/dev/null || true)
  printf '%s' "${n:-0}"
}
for i in $(seq 16 40); do
  reports=$(ls "$SEATS"/S1-*.md "$SEATS"/S2-*.md "$SEATS"/S3-*.md "$SEATS"/S4-*.md "$SEATS"/S5-*.md 2>/dev/null | wc -l)
  tools_readme=$(git -C "$REPO" status --porcelain -- corpus/tools/README.md | wc -l)
  skill_mod=$(git -C "$REPO" status --porcelain -- SKILL.md | wc -l)
  dep_freeze=$(git -C "$REPO" status --porcelain -- corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json | wc -l)
  lapse_note=0
  test -f "$REPO/corpus/knowledge/r99-lapse-scope-note.md" && lapse_note=1
  blind=0
  test -f "$REPO/corpus/knowledge/r99-gate-blind-spot-table.md" && blind=1
  r99_map=0
  test -f "$REPO/corpus/fixtures/r99-window-lapse/claim-excerpt-map.md" && r99_map=1
  inv=0
  if [ "$r99_map" -eq 1 ]; then
    inv=$(count_pat '21 JSON facts' "$REPO/corpus/fixtures/r99-window-lapse/claim-excerpt-map.md")
  fi
  printf 'TRY %02d %s reports=%s tools_readme_mod=%s skill_mod=%s dep_freeze_mod=%s lapse_note=%s blind_table=%s r99_map=%s inv21=%s\n' \
    "$i" "$(date +%H:%M:%S)" "$reports" "$tools_readme" "$skill_mod" "$dep_freeze" "$lapse_note" "$blind" "$r99_map" "$inv" >> "$LOG"
  if [ "$reports" -ge 5 ] && [ "$tools_readme" -ge 1 ] && [ "$lapse_note" -ge 1 ] && [ "$blind" -ge 1 ] && [ "$inv" -ge 1 ]; then
    echo "POLL_DONE at try $i" >> "$LOG"
    exit 0
  fi
  sleep 20
done
echo "POLL_TIMEOUT after 40 tries" >> "$LOG"
exit 1
