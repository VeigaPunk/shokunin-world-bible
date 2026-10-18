#!/bin/bash
# V35 round-98 adversarial probes: C1(a) exit-2, C1(b) legacy-pin migration, C2 V46 discharge.
# Run from repo root. Scratch only; the delivered tree is never written.
set -u
cd /home/vgpnk/Projects/shokunin/lore-shokunin
BASE=9a3d648
S=.ufo/waves/round-98/scratch/V35/probes
OUT=.ufo/waves/round-98/scratch/V35/probe-out
rm -rf "$S" "$OUT"; mkdir -p "$S" "$OUT"

mirror() { # $1=name $2=tool-source-arg (path or git-ref)
  local root="$S/$1"
  mkdir -p "$root/corpus/tools" "$root/corpus/fixtures"
  if [ "$2" = "DELIVERED" ]; then
    cp corpus/tools/dependency_freeze.py "$root/corpus/tools/dependency_freeze.py"
    cp corpus/tools/dependency-freeze-contract.json "$root/corpus/tools/dependency-freeze-contract.json"
  else
    git show "$2:corpus/tools/dependency_freeze.py" > "$root/corpus/tools/dependency_freeze.py"
    git show "$2:corpus/tools/dependency-freeze-contract.json" > "$root/corpus/tools/dependency-freeze-contract.json"
  fi
  echo "$root"
}

echo "=== PROBE A: SELF-TEST-MISMATCH exit code (delivered vs baseline) ==="
for rev in delivered baseline; do
  if [ "$rev" = delivered ]; then root=$(mirror stm-delivered DELIVERED); else root=$(mirror stm-baseline "$BASE"); fi
  python3 - "$root" <<'EOF'
import json, sys, pathlib
root = pathlib.Path(sys.argv[1])
p = root/"corpus/tools/dependency-freeze-contract.json"
c = json.loads(p.read_text())
exp = c["self_test"]["expected"]
tgt = next(e for e in exp if e["id"] == "clean")
tgt["exit"] = 1 - int(tgt.get("exit", 0))   # flip the expectation
p.write_text(json.dumps(c, indent=2, ensure_ascii=False) + "\n")
print("flipped case 'clean' expected exit ->", tgt["exit"])
EOF
  python3 "$root/corpus/tools/dependency_freeze.py" --self-test > "$OUT/probeA-$rev.txt" 2>&1
  rc=$?
  echo "--- $rev exit=$rc ---"
  grep -E "SELF-TEST FAIL|FINDING|RESULT|^SELF-TEST [0-9]" "$OUT/probeA-$rev.txt" | tail -4
done

echo
echo "=== PROBE B: path-less legacy pin migrated by --freeze (delivered vs baseline) ==="
for rev in delivered baseline; do
  if [ "$rev" = delivered ]; then root=$(mirror legacy-delivered DELIVERED); else root=$(mirror legacy-baseline "$BASE"); fi
  cp -r corpus/fixtures/r95-crossing-aftermath "$root/corpus/fixtures/r95-crossing-aftermath"
  python3 - "$root" <<'EOF'
import json, sys, pathlib
root = pathlib.Path(sys.argv[1])
p = root/"corpus/tools/dependency-freeze-contract.json"
c = json.loads(p.read_text())
pin = c["pins"]["r95-crossing-aftermath"]
pin.pop("fixture", None)          # simulate the path-less legacy pin
p.write_text(json.dumps(c, indent=2, ensure_ascii=False) + "\n")
print("path-less pin keys:", sorted(pin))
EOF
  python3 "$root/corpus/tools/dependency_freeze.py" --freeze "$root/corpus/fixtures/r95-crossing-aftermath" > "$OUT/probeB-$rev.txt" 2>&1
  rc=$?
  echo "--- $rev exit=$rc ---"
  tail -4 "$OUT/probeB-$rev.txt"
  python3 - "$root" <<'EOF'
import json, sys, pathlib
root = pathlib.Path(sys.argv[1])
pin = json.loads((root/"corpus/tools/dependency-freeze-contract.json").read_text())["pins"]["r95-crossing-aftermath"]
print("post-run pin fixture field:", repr(pin.get("fixture")))
EOF
done

echo
echo "=== PROBE C: V46 discharge — scratch REDUCTION-DETECTED on the r97 tick-13 edge ==="
root=$(mirror v46 DELIVERED)
for fx in r97-crossing-acknowledgment r98-clerk-filing; do
  cp -r "corpus/fixtures/$fx" "$root/corpus/fixtures/$fx"
done
python3 "$root/corpus/tools/dependency_freeze.py" "$root/corpus/fixtures/r97-crossing-acknowledgment" > "$OUT/probeC-r97-control.txt" 2>&1
echo "r97 control exit=$?"
python3 - "$root" <<'EOF'
import json, sys, pathlib
root = pathlib.Path(sys.argv[1])
p = root/"corpus/fixtures/r97-crossing-acknowledgment/timeline.json"
data = json.loads(p.read_text())
ev = [e for e in data if e["id"] == "acknowledgment-aru-records"]
assert len(ev) == 1, ev
print("tick-13 event before:", ev[0])
ev[0]["depends_on"] = []
p.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
EOF
python3 "$root/corpus/tools/dependency_freeze.py" "$root/corpus/fixtures/r97-crossing-acknowledgment" > "$OUT/probeC-r97-mutated.txt" 2>&1
echo "r97 mutated exit=$?"
cat "$OUT/probeC-r97-mutated.txt"

echo
echo "=== PROBE D: r98 new-edge load-bearing (drop the tick-14 depends_on) ==="
python3 - "$root" <<'EOF'
import json, sys, pathlib
root = pathlib.Path(sys.argv[1])
p = root/"corpus/fixtures/r98-clerk-filing/timeline.json"
data = json.loads(p.read_text())
ev = [e for e in data if e["id"] == "clerk-filing-open"]
assert len(ev) == 1, ev
print("tick-14 event before:", ev[0])
ev[0]["depends_on"] = []
p.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
EOF
python3 "$root/corpus/tools/dependency_freeze.py" "$root/corpus/fixtures/r98-clerk-filing" > "$OUT/probeD-r98-mutated.txt" 2>&1
echo "r98 mutated exit=$?"
cat "$OUT/probeD-r98-mutated.txt"
echo done
