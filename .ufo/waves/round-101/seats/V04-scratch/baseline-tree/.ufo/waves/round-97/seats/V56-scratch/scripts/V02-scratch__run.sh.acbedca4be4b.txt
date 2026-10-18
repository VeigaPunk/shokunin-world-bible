#!/bin/bash
# V02 r97 delivered-revision battery: 25/25 self-test, cross-check, determinism, residue, hash guard.
set -u
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
SC=.ufo/waves/round-97/seats/V02-scratch
TOOL=corpus/tools/map_obligations.py
CONTRACT=corpus/tools/map-obligations-contract.json

sha256sum "$TOOL" "$CONTRACT" > "$SC/pins.delivered.txt"
cat "$SC/pins.delivered.txt"
git status --porcelain > "$SC/gitstatus.before.txt"
ls -d map-obligations-self-test-* 2>/dev/null | wc -l > "$SC/residue.before.txt"
cat "$SC/residue.before.txt"

echo "=== RUN 1 ==="
python3 "$TOOL" --self-test > "$SC/selftest.1.out" 2> "$SC/selftest.1.err"
echo "exit=$?"
cat "$SC/selftest.1.out"
echo "stderr_bytes=$(wc -c < "$SC/selftest.1.err")"

echo "=== RUN 2 (determinism) ==="
python3 "$TOOL" --self-test > "$SC/selftest.2.out" 2> "$SC/selftest.2.err"
echo "exit=$?"
cmp -s "$SC/selftest.1.out" "$SC/selftest.2.out" && echo "STDOUT_IDENTICAL" || echo "STDOUT_DIFFERS"
cmp -s "$SC/selftest.1.err" "$SC/selftest.2.err" && echo "STDERR_IDENTICAL" || echo "STDERR_DIFFERS"

echo "=== CROSS-CHECK (independent parser) ==="
python3 "$SC/crosscheck.py" "$SC/selftest.1.out"
echo "crosscheck_exit=$?"

echo "=== COUNTS ==="
echo "pass_lines=$(grep -c '^SELF-TEST PASS ' "$SC/selftest.1.out")"
echo "fail_lines=$(grep -c '^SELF-TEST FAIL ' "$SC/selftest.1.out")"
echo "result_lines=$(grep -c '^RESULT ' "$SC/selftest.1.out")"
echo "total_lines=$(wc -l < "$SC/selftest.1.out")"

sha256sum "$TOOL" "$CONTRACT" > "$SC/pins.delivered.after.txt"
diff "$SC/pins.delivered.txt" "$SC/pins.delivered.after.txt" && echo "PINS_IDENTICAL" || echo "PINS_CHANGED"
git status --porcelain > "$SC/gitstatus.after.txt"
diff "$SC/gitstatus.before.txt" "$SC/gitstatus.after.txt" && echo "GIT_STATUS_IDENTICAL" || echo "GIT_STATUS_CHANGED"
ls -d map-obligations-self-test-* 2>/dev/null | wc -l > "$SC/residue.after.txt"
echo "residue_before=$(cat "$SC/residue.before.txt") residue_after=$(cat "$SC/residue.after.txt")"
