#!/usr/bin/env bash
# V18 mutation matrix: run support_check + map_obligations on each mutant copy.
# Writes logs under V18-scratch/logs/. Reads only corpus/tools (read-only) and the mutants.
set -u
REPO=/home/vgpnk/Projects/shokunin/lore-shokunin
S="$REPO/.ufo/waves/round-98/seats/V18-scratch"
LOGS="$S/logs"
mkdir -p "$LOGS"
cd "$REPO" || exit 1
run_one() {
  local name="$1"
  local dir="$S/mutants/$name"
  [ -d "$dir" ] || { echo "MISSING $name"; return; }
  python3 corpus/tools/support_check.py "$dir" > "$LOGS/$name.support.out" 2>&1
  local se=$?
  python3 corpus/tools/map_obligations.py "$dir" > "$LOGS/$name.map.out" 2>&1
  local me=$?
  printf '%-36s support=%s map=%s\n' "$name" "$se" "$me"
}
# baseline: unmutated copy
rm -rf "$S/mutants/m0-baseline"
cp -r corpus/fixtures/r98-clerk-filing "$S/mutants/m0-baseline"
run_one m0-baseline
for m in m1-span-break m2-row-drop m2-row-drop-declared m3a-claims-rename-keep-row m3b-claims-rename-row-removed m4-claims-row-deletion m5-deps-reduction m5b-event-deletion-fully-declared m6-digest-tamper; do
  run_one "$m"
done
echo "MATRIX DONE"
