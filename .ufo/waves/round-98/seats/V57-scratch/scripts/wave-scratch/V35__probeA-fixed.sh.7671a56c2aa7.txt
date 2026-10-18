#!/bin/bash
# V35 probe A (fixed): SELF-TEST-MISMATCH exit code, delivered vs baseline.
set -u
cd /home/vgpnk/Projects/shokunin/lore-shokunin
BASE=9a3d648
S=.ufo/waves/round-98/scratch/V35/probes
OUT=.ufo/waves/round-98/scratch/V35/probe-out
mkdir -p "$S" "$OUT"

for rev in delivered baseline; do
  root="$S/stm2-$rev"
  rm -rf "$root"; mkdir -p "$root/corpus/tools" "$root/corpus/fixtures"
  if [ "$rev" = delivered ]; then
    cp corpus/tools/dependency_freeze.py "$root/corpus/tools/dependency_freeze.py"
    cp corpus/tools/dependency-freeze-contract.json "$root/corpus/tools/dependency-freeze-contract.json"
  else
    git show "$BASE:corpus/tools/dependency_freeze.py" > "$root/corpus/tools/dependency_freeze.py"
    git show "$BASE:corpus/tools/dependency-freeze-contract.json" > "$root/corpus/tools/dependency-freeze-contract.json"
  fi
  cp -r corpus/fixtures/r95-crossing-aftermath "$root/corpus/fixtures/r95-crossing-aftermath"
  python3 - "$root" <<'EOF'
import json, sys, pathlib
root = pathlib.Path(sys.argv[1])
p = root/"corpus/tools/dependency-freeze-contract.json"
c = json.loads(p.read_text())
exp = c["self_test"]["expected"]
assert isinstance(exp, dict), type(exp)
exp["clean"]["exit"] = 1          # flip the persisted expectation for 'clean'
p.write_text(json.dumps(c, indent=2, ensure_ascii=False) + "\n")
print("cases:", len(exp), "| flipped 'clean'.exit ->", exp["clean"]["exit"])
EOF
  python3 "$root/corpus/tools/dependency_freeze.py" --self-test > "$OUT/probeA2-$rev.txt" 2>&1
  rc=$?
  echo "--- $rev exit=$rc ---"
  grep -E "SELF-TEST FAIL clean|^SELF-TEST [0-9]+/|FINDING SELF-TEST-MISMATCH|^RESULT" "$OUT/probeA2-$rev.txt"
done
