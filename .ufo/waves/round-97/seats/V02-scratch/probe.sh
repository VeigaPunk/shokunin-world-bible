#!/bin/bash
# V02 r97 subset-tolerance closure battery.
# Scratch copies of delivered tool+contract, one case dropped per variant.
# Expectation: EVERY variant fails closed (exit 2, self_test_contract finding naming the drop).
set -u
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
SC=.ufo/waves/round-97/seats/V02-scratch
VAR=$SC/variants
TOOL=corpus/tools/map_obligations.py
CONTRACT=corpus/tools/map-obligations-contract.json

rm -rf "$VAR"
mkdir -p "$VAR"
sha256sum "$TOOL" "$CONTRACT" > "$SC/pins.before.txt"
cat "$SC/pins.before.txt"

for caseid in complete dual_pointer inventory_mismatch map_missing schema_drift phantom; do
  name="drop_$caseid"
  d="$VAR/$name/corpus/tools"
  mkdir -p "$d"
  cp "$TOOL" "$d/map_obligations.py"
  python3 - "$CONTRACT" "$d/map-obligations-contract.json" "$caseid" <<'EOF'
import json, sys
src, dst, drop = sys.argv[1], sys.argv[2], sys.argv[3]
c = json.load(open(src))
cases = c["self_test"]["cases"]
before = len(cases)
c["self_test"]["cases"] = [x for x in cases if x["id"] != drop]
after = len(c["self_test"]["cases"])
assert after == before - 1, (drop, before, after)
json.dump(c, open(dst, "w"), indent=2)
print(f"scratch contract: dropped {drop!r}: {before} -> {after} cases")
EOF
  echo "=== VARIANT $name ==="
  python3 "$d/map_obligations.py" --self-test > "$SC/$name.out" 2> "$SC/$name.err"
  rc=$?
  echo "exit=$rc"
  cat "$SC/$name.out"
  echo "stderr_bytes=$(wc -c < "$SC/$name.err")"
  # tool copy must be byte-identical to delivered
  cmp -s "$TOOL" "$d/map_obligations.py" && echo "tool_copy_identical=yes" || echo "tool_copy_identical=NO"
done

sha256sum "$TOOL" "$CONTRACT" > "$SC/pins.after.txt"
echo "=== pins diff (before vs after) ==="
diff "$SC/pins.before.txt" "$SC/pins.after.txt" && echo "PINS_IDENTICAL" || echo "PINS_CHANGED"
