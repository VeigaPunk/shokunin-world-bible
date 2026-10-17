#!/bin/bash
# V55 delivered-tool verification batch. Run from repo root after P1 lands.
set -u
cd /home/vgpnk/Projects/shokunin/lore-shokunin
S=.ufo/waves/round-95/seats/V55-scratch
T=corpus/tools/map_obligations.py
LOG=$S/delivered-check.log
: > "$LOG"

{
echo "### 0. artifact identity"
sha256sum "$T" corpus/tools/map-obligations-contract.json
git diff --stat fb118c4 -- "$T" corpus/tools/map-obligations-contract.json
echo
echo "### 1. delivered on scratch clusters"
for m in control-pristine mut1-rename0-removerow mut2-rename2-removerow mut3-rename0-keeprow mut4-benign-extrakey mut5-rename-firstappearance; do
  echo "--- delivered on $m ---"
  python3 "$T" "$S/$m"; echo "exit=$?"
done
echo
echo "### 1b. mut1 repeated (stability)"
python3 "$T" "$S/mut1-rename0-removerow"; echo "exit=$?"
a=$(python3 "$T" "$S/mut1-rename0-removerow" 2>&1 | sha256sum | cut -d' ' -f1)
b=$(python3 "$T" "$S/mut1-rename0-removerow" 2>&1 | sha256sum | cut -d' ' -f1)
echo "mut1_run_a=$a mut1_run_b=$b identical=$([ "$a" = "$b" ] && echo yes || echo no)"
echo
echo "### 2. delivered unchanged-behavior fixtures"
for f in r93-m2-kojiki-cluster r94-paired-crossing r87-myth-cluster r89-inspiration-paraphrase r88-m3-maya-cluster; do
  echo "--- delivered on $f ---"
  python3 "$T" "corpus/fixtures/$f"; echo "exit=$?"
done
echo
echo "### 3. frozen r93 replay"
python3 "$T" --frozen .ufo/waves/round-94/frozen/map-obligations-r93; echo "exit=$?"
echo
echo "### 4. self-test"
python3 "$T" --self-test > "$S/selftest.out" 2> "$S/selftest.err"
echo "self_test_exit=$?"
echo "selftest_lines=$(grep -c '^SELF-TEST' $S/selftest.out)"
echo "selftest_pass=$(grep -c '^SELF-TEST PASS' $S/selftest.out)"
echo "stderr_bytes=$(wc -c < $S/selftest.err)"
grep -E 'map_missing|invalid_arguments' "$S/selftest.out"
tail -2 "$S/selftest.out"
echo
echo "### 5. contract JSON"
python3 - <<'PY'
import json
c = json.load(open("corpus/tools/map-obligations-contract.json"))
cases = c["self_test"]["cases"]
print("case_count:", len(cases))
print("ids:", [x["id"] for x in cases])
for cid in ("map_missing", "invalid_arguments"):
    hit = [x for x in cases if x["id"] == cid]
    print(cid, "->", hit)
PY
echo
echo "### 6. tool self-test case tuple count"
grep -c '^    "' corpus/tools/map_obligations.py
python3 - <<'PY'
import re
src = open("corpus/tools/map_obligations.py").read()
m = re.search(r"SELF_TEST_CASES = \((.*?)\)", src, re.S)
ids = re.findall(r'"([^"]+)"', m.group(1))
print("SELF_TEST_CASES:", len(ids), ids)
PY
echo
echo "### 7. leftover scratch check under repo root"
ls -d map-obligations-self-test-* 2>/dev/null || echo "none"
} >> "$LOG" 2>&1
echo "LOG WRITTEN: $LOG"
