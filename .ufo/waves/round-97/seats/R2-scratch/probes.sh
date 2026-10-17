#!/bin/bash
# R2 round-97 probes: run only against the POST-R1 delivered tool.
set -u
REPO=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$REPO/.ufo/waves/round-97/seats/R2-scratch
TOOL=$REPO/corpus/tools/map_obligations.py
CONTRACT=$REPO/corpus/tools/map-obligations-contract.json

echo "### delivered tool sha256"
sha256sum "$TOOL" "$CONTRACT"

echo
echo "### PROBE A: delivered --self-test (expect 25/25 PASS, exit 0)"
cd "$REPO" || exit 9
python3 "$TOOL" --self-test
echo "probe_A_exit=$?"

probe_contract_drop() {
  local case_id="$1" dir="$2"
  rm -rf "$dir"
  mkdir -p "$dir/corpus/tools"
  cp "$TOOL" "$CONTRACT" "$dir/corpus/tools/"
  python3 - "$dir/corpus/tools/map-obligations-contract.json" "$case_id" <<'PY'
import json, pathlib, sys
path = pathlib.Path(sys.argv[1])
case_id = sys.argv[2]
contract = json.loads(path.read_text())
before = len(contract["self_test"]["cases"])
contract["self_test"]["cases"] = [c for c in contract["self_test"]["cases"] if c["id"] != case_id]
path.write_text(json.dumps(contract, indent=2) + "\n")
print(f"scratch contract: dropped {case_id!r}, cases {before} -> {len(contract['self_test']['cases'])}")
PY
  echo "--- scratch tool sha256 (must equal delivered) ---"
  sha256sum "$dir/corpus/tools/map_obligations.py"
  cd "$dir" || exit 9
  python3 corpus/tools/map_obligations.py --self-test
  echo "probe_drop_${case_id}_exit=$?"
}

echo
echo "### PROBE B1: scratch contract copy dropping an r96-ADDED case (schema_drift)"
probe_contract_drop schema_drift "$S/post/drop-schema_drift"

echo
echo "### PROBE B2: scratch contract copy dropping a CORE case (complete)"
probe_contract_drop complete "$S/post/drop-complete"

echo
echo "### PROBE C: scratch tool copy with dual_pointer emission neutralized"
C=$S/post/neutralize
rm -rf "$C"
mkdir -p "$C/corpus/tools"
cp "$TOOL" "$CONTRACT" "$C/corpus/tools/"
python3 - "$C/corpus/tools/map_obligations.py" <<'PY'
import pathlib, re, sys
path = pathlib.Path(sys.argv[1])
text = path.read_text()
pattern = r'(def second_pointer_mention\(tail\):\n(?:\s*"""[^"]*"""\n)?)'
new, count = re.subn(pattern, r'\1    return None  # R2 probe: neutralize dual_pointer emission\n', text)
if count != 1:
    raise SystemExit(f"neutralization anchor matched {count} times, expected 1")
path.write_text(new)
print("scratch tool: second_pointer_mention() short-circuited to return None")
PY
cd "$C" || exit 9
python3 corpus/tools/map_obligations.py --self-test 2>&1 | grep -E "dual_pointer|RESULT|FINDING|CASES" || true
echo "probe_neutralize_exit=${PIPESTATUS[0]}"
