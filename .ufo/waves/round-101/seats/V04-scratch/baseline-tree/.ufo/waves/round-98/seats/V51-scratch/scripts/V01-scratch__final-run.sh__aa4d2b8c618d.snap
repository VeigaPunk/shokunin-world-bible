#!/usr/bin/env bash
# V01 final-run: one consistent record on the delivered revision.
set -u
REPO=/home/vgpnk/Projects/shokunin/lore-shokunin
SC=$REPO/.ufo/waves/round-98/seats/V01-scratch
cd "$REPO" || exit 1
echo "===== FINAL-RUN ts=$(date +%H:%M:%S) ====="
echo "--- hashes BEFORE ---"
sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
echo "--- real-tree --self-test ---"
python3 corpus/tools/dependency_freeze.py --self-test > "$SC/final-real-selftest.out" 2>&1
echo "real-tree EXIT=$?"
tail -3 "$SC/final-real-selftest.out"
echo "--- parity ---"
python3 "$SC/harness.py" parity "$SC/final-mirror" 2>/dev/null || {
  python3 "$SC/harness.py" build "$SC/final-mirror" corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json >/dev/null
  python3 "$SC/harness.py" parity "$SC/final-mirror"
}
echo "--- A: perturbed clean.exit 0->1 (C1a primary) ---"
python3 "$SC/harness.py" build "$SC/final-A" corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json >/dev/null
python3 "$SC/harness.py" perturb-exit "$SC/final-A" clean 1
python3 "$SC/harness.py" run "$SC/final-A" | grep -E "^(EXIT=|CASE clean|SELF-TEST|FINDING|RESULT)"
echo "--- B: drop new case from contract (pin, fail-closed) ---"
python3 "$SC/harness.py" build "$SC/final-B" corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json >/dev/null
python3 "$SC/harness.py" drop-case "$SC/final-B" NEW
python3 "$SC/harness.py" run "$SC/final-B" | grep -E "^(EXIT=|FINDING|RESULT)"
echo "--- C: drop new case from FROZEN_CASES (pin, fail-closed) ---"
python3 "$SC/harness.py" build "$SC/final-C" corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json >/dev/null
python3 - <<'EOF'
from pathlib import Path
p = Path("/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-98/seats/V01-scratch/final-C/corpus/tools/dependency_freeze.py")
t = p.read_text(encoding="utf-8"); n = '    "self_test_mismatch",\n'
assert n in t, "needle missing"
p.write_text(t.replace(n, "", 1), encoding="utf-8")
print("dropped self_test_mismatch from FROZEN_CASES")
EOF
python3 "$SC/harness.py" run "$SC/final-C" | grep -E "^(EXIT=|FINDING|RESULT)"
echo "--- D: neutralized emit(2->1)+return(2->1) (load-bearing) ---"
python3 "$SC/harness.py" build "$SC/final-D" corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json >/dev/null
python3 "$SC/harness.py" neutralize-exit "$SC/final-D"
python3 "$SC/harness.py" run "$SC/final-D" | grep -E "^(EXIT=|CASE self_test_mismatch|SELF-TEST|FINDING|RESULT)"
echo "--- E: flip new case's own expectation 2->1 ---"
python3 "$SC/harness.py" build "$SC/final-E" corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json >/dev/null
python3 "$SC/harness.py" perturb-exit "$SC/final-E" self_test_mismatch 1
python3 "$SC/harness.py" run "$SC/final-E" | grep -E "^(EXIT=|CASE self_test_mismatch|SELF-TEST|FINDING|RESULT)"
echo "--- hashes AFTER ---"
sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
echo "--- leftovers ---"
ls -d dependency-freeze-self-test-* 2>/dev/null || echo "none"
echo "===== FINAL-RUN DONE ts=$(date +%H:%M:%S) ====="
