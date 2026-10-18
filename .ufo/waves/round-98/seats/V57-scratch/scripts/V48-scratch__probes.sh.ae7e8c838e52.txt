#!/bin/bash
# V48 delivered-revision probes (run only after S1's delivery is stable)
# Usage: probes.sh <tool-src> <contract-src> <tag>
set +e
R=/home/vgpnk/Projects/shokunin/lore-shokunin
V=$R/.ufo/waves/round-98/seats/V48-scratch
TOOL="${1:-$R/corpus/tools/dependency_freeze.py}"
CONTRACT="${2:-$R/corpus/tools/dependency-freeze-contract.json}"
TAG="${3:-delivered}"
D="$V/$TAG"
mkdir -p "$D"
echo "=== tool sha256 ==="
sha256sum "$TOOL" "$CONTRACT"

echo "=== P1: delivered --self-test (real tree) ==="
cd "$R" && python3 "$TOOL" --self-test > "$D/self-test.out" 2>&1
echo "rc=$?"; tail -3 "$D/self-test.out"

echo "=== P2: chain verify on the six fixtures (real tree) ==="
: > "$D/chain.out"
for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response r97-crossing-acknowledgment r98-clerk-filing; do
  out=$(python3 "$TOOL" "corpus/fixtures/$f" 2>&1); rc=$?
  echo "--- $f rc=$rc" >> "$D/chain.out"; echo "$out" >> "$D/chain.out"
  echo "$f rc=$rc : $(echo "$out" | tr '\n' ' | ')"
done

echo "=== P3: fakerepo r97 edge REDUCTION-DETECTED ==="
FR="$D/fakered"
mkdir -p "$FR/corpus/tools" "$FR/corpus/fixtures"
cp "$TOOL" "$FR/corpus/tools/dependency_freeze.py"
cp "$CONTRACT" "$FR/corpus/tools/dependency-freeze-contract.json"
cp -r "$R/corpus/fixtures/r97-crossing-acknowledgment" "$FR/corpus/fixtures/"
python3 - "$FR/corpus/fixtures/r97-crossing-acknowledgment/timeline.json" <<'EOF'
import json, sys
p = sys.argv[1]
t = json.load(open(p))
for r in t:
    if r["id"] == "acknowledgment-aru-records":
        r["depends_on"] = [d for d in r["depends_on"] if d != "response-evin-salt-court"]
json.dump(t, open(p, "w"), indent=2)
print("dropped response-evin-salt-court from tick-13 depends_on")
EOF
python3 "$FR/corpus/tools/dependency_freeze.py" "$FR/corpus/fixtures/r97-crossing-acknowledgment" > "$D/reduction.out" 2>&1
echo "rc=$?"; cat "$D/reduction.out"

echo "=== P4: path-less legacy pin migration via --freeze ==="
FM="$D/fakemigrate"
mkdir -p "$FM/corpus/tools" "$FM/corpus/fixtures"
cp "$TOOL" "$FM/corpus/tools/dependency_freeze.py"
cp "$CONTRACT" "$FM/corpus/tools/dependency-freeze-contract.json"
cp -r "$R/corpus/fixtures/r95-crossing-aftermath" "$FM/corpus/fixtures/"
python3 - "$FM/corpus/tools/dependency-freeze-contract.json" <<'EOF'
import json, sys
p = sys.argv[1]
c = json.load(open(p))
del c["pins"]["r95-crossing-aftermath"]["fixture"]
json.dump(c, open(p, "w"), indent=2, ensure_ascii=False)
print("pin made path-less")
EOF
sha256sum "$FM/corpus/tools/dependency-freeze-contract.json" > "$D/migrate-before.txt"
python3 "$FM/corpus/tools/dependency_freeze.py" --freeze "$FM/corpus/fixtures/r95-crossing-aftermath" > "$D/migrate.out" 2>&1
echo "rc=$?"; cat "$D/migrate.out"
python3 - "$FM/corpus/tools/dependency-freeze-contract.json" <<'EOF'
import json, sys
c = json.load(open(sys.argv[1]))
print("pin fixture now:", c["pins"]["r95-crossing-aftermath"].get("fixture"))
EOF

echo "=== P5: flipped-expectation mismatch path (delivered) ==="
FX="$D/fakemismatch"
mkdir -p "$FX/corpus/tools" "$FX/corpus/fixtures"
cp "$TOOL" "$FX/corpus/tools/dependency_freeze.py"
cp "$CONTRACT" "$FX/corpus/tools/dependency-freeze-contract.json"
cp -r "$R/corpus/fixtures/r95-crossing-aftermath" "$FX/corpus/fixtures/"
python3 - "$FX/corpus/tools/dependency-freeze-contract.json" <<'EOF'
import json, sys
p = sys.argv[1]
c = json.load(open(p))
c["self_test"]["expected"]["clean"]["exit"] = 1
json.dump(c, open(p, "w"), indent=2, ensure_ascii=False)
print("flipped clean expectation to exit 1")
EOF
python3 "$FX/corpus/tools/dependency_freeze.py" --self-test > "$D/mismatch.out" 2>&1
echo "rc=$?"; tail -4 "$D/mismatch.out"

echo "=== done $TAG ==="
