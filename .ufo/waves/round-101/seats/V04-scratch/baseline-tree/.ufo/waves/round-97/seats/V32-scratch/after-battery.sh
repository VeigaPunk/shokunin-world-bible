#!/bin/bash
# V32 r97 after-battery: documented commands, chain, self-tests, exit contract.
# Run from the lane root. Read-only w.r.t. the live tree.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
S=$PWD/.ufo/waves/round-97/seats/V32-scratch/after
mkdir -p "$S"

echo "### FROZEN REVISION"
sha256sum corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json \
  corpus/tools/README.md corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json \
  corpus/fixtures/r96-crossing-response/claim-excerpt-map.md \
  corpus/fixtures/r97-crossing-acknowledgment/README.md corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md \
  corpus/knowledge/r97-acknowledgment-scope-note.md 2>&1

echo; echo "### SELF-TESTS"
python3 corpus/tools/map_obligations.py --self-test; echo "map_selftest_exit=$?"
python3 corpus/tools/dependency_freeze.py --self-test; echo "dep_selftest_exit=$?"

echo; echo "### DEP CHAIN VERIFY"
for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response r97-crossing-acknowledgment; do
  echo "-- $f"; python3 corpus/tools/dependency_freeze.py corpus/fixtures/$f; echo "  exit=$?"
done

echo; echo "### MAP CORPUS PATHS"
for f in r88-m3-maya-cluster r93-m2-kojiki-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response r97-crossing-acknowledgment; do
  echo "-- $f"; python3 corpus/tools/map_obligations.py corpus/fixtures/$f; echo "  exit=$?"
done

echo; echo "### R97 FIXTURE README REPLAY BLOCK (as written in the delivered README)"
python3 corpus/fixtures/check_bible.py corpus/fixtures/r97-crossing-acknowledgment; echo "exit=$?"
python3 corpus/tools/support_check.py corpus/fixtures/r97-crossing-acknowledgment | tail -3; echo "exit=${PIPESTATUS[0]}"
python3 corpus/tools/map_obligations.py corpus/fixtures/r97-crossing-acknowledgment; echo "exit=$?"

echo; echo "### R96 FIXTURE RECEIPTS (post-repair)"
python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response; echo "exit=$?"
python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response | tail -3; echo "exit=${PIPESTATUS[0]}"
python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response; echo "exit=$?"

echo; echo "### FAIL-CLOSED PATHS"
python3 corpus/tools/map_obligations.py corpus/fixtures/r87-myth-cluster; echo "exit=$?"
python3 corpus/tools/map_obligations.py corpus/fixtures/r89-inspiration-paraphrase; echo "exit=$?"
python3 corpus/tools/map_obligations.py; echo "noarg_exit=$?"
python3 corpus/tools/dependency_freeze.py; echo "dep_noarg_exit=$?"
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r87-myth-cluster; echo "dep_unpinned_exit=$?"

echo; echo "### HELP PATHS"
python3 corpus/tools/map_obligations.py --help > "$S/map-help.txt" 2>&1; echo "map_help_exit=$? result_lines=$(grep -c '^RESULT' "$S/map-help.txt")"
python3 corpus/tools/dependency_freeze.py --help > "$S/dep-help.txt" 2>&1; echo "dep_help_exit=$? result_lines=$(grep -c '^RESULT' "$S/dep-help.txt")"

echo; echo "### FROZEN R93 REPLAY"
python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93 | tail -2; echo "exit=${PIPESTATUS[0]}"

echo; echo "### CENSUS"
ls -d corpus/fixtures/*/ | wc -l
