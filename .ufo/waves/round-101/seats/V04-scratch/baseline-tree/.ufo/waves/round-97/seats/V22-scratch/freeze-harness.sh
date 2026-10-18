#!/usr/bin/env bash
# V22 freeze-harness: exercise the DELIVERED dependency_freeze.py against
# scratch copies of the r97 fixture, with the delivered path binding satisfied.
#
# Why a harness: the delivered pin binds the canonical corpus path, and
# verifier seats may not write under corpus/. So we copy the delivered tool +
# contract byte-for-byte into a scratch ROOT whose own corpus/fixtures/ holds
# the r97 copies; --freeze then records harness-relative paths and verify
# compares like with like. Pins are keyed by directory basename, so each
# mutant is frozen first (guarded --freeze) and then mutated in place.
set -u
REPO=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$REPO/.ufo/waves/round-97/seats/V22-scratch
H=$S/harness
TOOL=$REPO/corpus/tools/dependency_freeze.py
CONTRACT=$REPO/corpus/tools/dependency-freeze-contract.json
FIX=$REPO/corpus/fixtures/r97-crossing-acknowledgment

run() { echo "\$ $*"; "$@"; echo "exit=$?"; }

echo "=== harness setup ==="
rm -rf "$H"
mkdir -p "$H/corpus/tools" "$H/corpus/fixtures"
cp "$TOOL" "$H/corpus/tools/dependency_freeze.py"
cp "$CONTRACT" "$H/corpus/tools/dependency-freeze-contract.json"
echo "delivered tool sha: $(sha256sum "$TOOL" | cut -d' ' -f1)"
echo "harness  tool sha: $(sha256sum "$H/corpus/tools/dependency_freeze.py" | cut -d' ' -f1)"
HT="$H/corpus/tools/dependency_freeze.py"

for name in r97-clean r97-deps-reduction r97-key-row-deleted; do
  cp -r "$FIX" "$H/corpus/fixtures/$name"
done

echo
echo "=== freeze each copy through the guarded path ==="
for name in r97-clean r97-deps-reduction r97-key-row-deleted; do
  run python3 "$HT" --freeze "$H/corpus/fixtures/$name"
done

echo
echo "=== baseline verify: clean copy ==="
run python3 "$HT" "$H/corpus/fixtures/r97-clean"

echo
echo "=== apply mutations in place (after pinning) ==="
python3 - "$H/corpus/fixtures/r97-deps-reduction" "$H/corpus/fixtures/r97-key-row-deleted" <<'PY'
import json, sys
from pathlib import Path

deps_dir, del_dir = (Path(p) for p in sys.argv[1:3])

p = deps_dir / "timeline.json"
data = json.loads(p.read_text(encoding="utf-8"))
before = list(data[-1]["depends_on"])
data[-1]["depends_on"] = []
p.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
print(f"deps-reduction: {data[-1]['id']} depends_on {before} -> [] (map untouched)")

p = del_dir / "timeline.json"
data = json.loads(p.read_text(encoding="utf-8"))
removed = data.pop()
p.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
print(f"key-row-deleted: removed event {removed['id']}")

mp = del_dir / "claim-excerpt-map.md"
lines = mp.read_text(encoding="utf-8").splitlines()
lines = [line for line in lines if not line.startswith("| J17 ")]
for i, line in enumerate(lines):
    if line.startswith("**Expected inventory:**"):
        lines[i] = line.replace("17 JSON facts", "16 JSON facts").replace(
            "19 total mapped rows", "18 total mapped rows").replace(
            "15 distinct excerpt anchors", "14 distinct excerpt anchors")
        print(f"key-row-deleted: {lines[i]}")
mp.write_text("\n".join(lines) + "\n", encoding="utf-8")
PY

echo
echo "=== verify deps-reduction copy (map/support self-consistent) ==="
run python3 "$HT" "$H/corpus/fixtures/r97-deps-reduction"
run python3 "$REPO/corpus/tools/map_obligations.py" "$H/corpus/fixtures/r97-deps-reduction"
run python3 "$REPO/corpus/tools/support_check.py" "$H/corpus/fixtures/r97-deps-reduction"

echo
echo "=== verify key-row-deleted copy (fully self-consistent tamper) ==="
run python3 "$HT" "$H/corpus/fixtures/r97-key-row-deleted"
run python3 "$REPO/corpus/tools/map_obligations.py" "$H/corpus/fixtures/r97-key-row-deleted"
run python3 "$REPO/corpus/tools/support_check.py" "$H/corpus/fixtures/r97-key-row-deleted"

echo
echo "=== delivered tool on a FOREIGN-path same-named copy (path binding) ==="
rm -rf "$S/foreign"
mkdir -p "$S/foreign"
cp -r "$REPO/corpus/fixtures/r96-crossing-response" "$S/foreign/r96-crossing-response"
cp -r "$FIX" "$S/foreign/r97-crossing-acknowledgment"
run python3 "$REPO/corpus/tools/dependency_freeze.py" "$S/foreign/r96-crossing-response"
run python3 "$REPO/corpus/tools/dependency_freeze.py" "$S/foreign/r97-crossing-acknowledgment"

echo
echo "=== delivered tool --freeze outside corpus/fixtures (scope guard) ==="
run python3 "$REPO/corpus/tools/dependency_freeze.py" --freeze "$S/harness/corpus/fixtures/r97-clean"
