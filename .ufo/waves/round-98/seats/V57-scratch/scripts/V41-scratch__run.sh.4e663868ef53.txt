#!/bin/bash
# V41 final tabulation: five gates on the tick-14-edge-dropped r98 copy + controls.
# Run ONLY after all S1-S5 reports exist and artifacts are stable.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 1
S=.ufo/waves/round-98/seats/V41-scratch
LOG=$S/final-tabulation.txt
: > "$LOG"

sec() { echo "" >> "$LOG"; echo "===== $* =====" >> "$LOG"; }

run() {  # run <label> <cmd...>  -- quotes command, output, exit code
  local label="$1"; shift
  {
    echo "--- $label"
    echo "\$ $*"
    "$@" 2>&1
    echo "EXIT=$?"
  } >> "$LOG" 2>&1
}

sec "0. Revision hashes (delivered)"
sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json \
  corpus/fixtures/check_bible.py corpus/tools/support_check.py \
  corpus/tools/map_obligations.py corpus/tools/boundary_doc_check.py >> "$LOG"
sha256sum corpus/fixtures/r98-clerk-filing/* >> "$LOG"
python3 - <<'EOF' >> "$LOG"
import json
c = json.load(open('corpus/tools/dependency-freeze-contract.json'))
pins = c.get('pins', {})
print("pins:", sorted(pins))
print("r97 pinned:", 'r97-crossing-acknowledgment' in pins)
print("r98 pinned:", 'r98-clerk-filing' in pins)
print("r98 pin fixture path:", pins.get('r98-clerk-filing', {}).get('fixture'))
print("r98 pin counts:", pins.get('r98-clerk-filing', {}).get('counts'))
print("revision:", c.get('revision'))
EOF

sec "1. Build mutated copy (tick-14 edge dropped) + mirror"
rm -rf "$S/r98-depdropped" "$S/mirror-r98"
python3 "$S/mutate.py" corpus/fixtures/r98-clerk-filing "$S/r98-depdropped" clerk-filing-open acknowledgment-aru-records >> "$LOG" 2>&1
echo "mutate EXIT=$?" >> "$LOG"
diff -u corpus/fixtures/r98-clerk-filing/timeline.json "$S/r98-depdropped/timeline.json" >> "$LOG" 2>&1
echo "diff EXIT=$? (1 = differs as intended)" >> "$LOG"
mkdir -p "$S/mirror-r98/corpus/tools" "$S/mirror-r98/corpus/fixtures"
cp corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json "$S/mirror-r98/corpus/tools/"
cp -r "$S/r98-depdropped" "$S/mirror-r98/corpus/fixtures/r98-clerk-filing"
echo "sha of mutated timeline in foreign copy vs mirror copy:" >> "$LOG"
sha256sum "$S/r98-depdropped/timeline.json" "$S/mirror-r98/corpus/fixtures/r98-clerk-filing/timeline.json" >> "$LOG"

sec "2. Five gates on the MUTATED copy"
run "check_bible (mutated)" python3 corpus/fixtures/check_bible.py "$S/r98-depdropped"
run "support_check (mutated)" python3 corpus/tools/support_check.py "$S/r98-depdropped"
run "map_obligations (mutated)" python3 corpus/tools/map_obligations.py "$S/r98-depdropped"
run "dependency_freeze (mutated, mirror)" python3 "$S/mirror-r98/corpus/tools/dependency_freeze.py" "$S/mirror-r98/corpus/fixtures/r98-clerk-filing"
run "boundary_doc_check (default, repo-level)" python3 corpus/tools/boundary_doc_check.py

sec "3. Controls on the INTACT delivered fixture"
run "check_bible (intact)" python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
run "support_check (intact)" python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing
run "map_obligations (intact)" python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
run "dependency_freeze (intact, delivered pin)" python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing
run "dependency_freeze --self-test" python3 corpus/tools/dependency_freeze.py --self-test

sec "4. Post-run hash re-check (no writes by this seat)"
sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json \
  corpus/fixtures/r98-clerk-filing/timeline.json >> "$LOG"

echo "DONE" >> "$LOG"
