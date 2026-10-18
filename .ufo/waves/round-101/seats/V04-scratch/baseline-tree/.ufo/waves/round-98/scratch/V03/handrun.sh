#!/usr/bin/env bash
# V03 hand-run scenarios against the CURRENT working tree (delivered revision).
# Usage: bash handrun.sh <label>
set -u
cd /home/vgpnk/Projects/shokunin/lore-shokunin
LABEL="${1:-delivered}"
S=".ufo/waves/round-98/scratch/V03"
rm -rf "$S/handrun-$LABEL"
mkdir -p "$S/handrun-$LABEL"

build_mirror() {
  local case="$1"
  local root="$S/handrun-$LABEL/$case"
  mkdir -p "$root/corpus/tools" "$root/corpus/fixtures"
  cp corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json "$root/corpus/tools/"
  cp -r corpus/fixtures/r95-crossing-aftermath "$root/corpus/fixtures/"
  echo "$root"
}

# Scenario A: tampered expectation -> SELF-TEST-MISMATCH must exit 2 (C1a post-state)
ROOT_A=$(build_mirror mismatch)
python3 - "$ROOT_A" <<'EOF'
import json, pathlib, sys
p = pathlib.Path(sys.argv[1])/"corpus/tools/dependency-freeze-contract.json"
c = json.loads(p.read_text())
c["self_test"]["expected"]["clean"]["exit"] = 1
p.write_text(json.dumps(c, indent=2)+"\n")
EOF
echo "=== A: tampered expectation, hand-run --self-test ==="
python3 "$ROOT_A/corpus/tools/dependency_freeze.py" --self-test > "$S/handrun-$LABEL/A-mismatch.txt" 2>&1
echo "A exit=$?"
grep -E "^SELF-TEST [0-9]+/|FINDING|^RESULT" "$S/handrun-$LABEL/A-mismatch.txt" | tail -4

# Scenario B: reduction_edge_drop hand-run -> REDUCTION-DETECTED exit 1
ROOT_B=$(build_mirror reduction)
python3 - "$ROOT_B" <<'EOF'
import json, pathlib, sys
p = pathlib.Path(sys.argv[1])/"corpus/fixtures/r95-crossing-aftermath/timeline.json"
tl = json.loads(p.read_text())
for r in tl:
    if r["id"] == "paired-crossing-decision":
        r["depends_on"] = [d for d in r["depends_on"] if d != "evin-ninth-bell"]
p.write_text(json.dumps(tl, indent=2)+"\n")
EOF
echo "=== B: hand-dropped evin-ninth-bell edge, hand-run verify ==="
python3 "$ROOT_B/corpus/tools/dependency_freeze.py" "$ROOT_B/corpus/fixtures/r95-crossing-aftermath" > "$S/handrun-$LABEL/B-reduction.txt" 2>&1
echo "B exit=$?"
cat "$S/handrun-$LABEL/B-reduction.txt"

# Scenario C: path-less legacy pin migrated in place by --freeze (C1b post-state)
ROOT_C=$(build_mirror legacy)
python3 - "$ROOT_C" <<'EOF'
import json, pathlib, sys
p = pathlib.Path(sys.argv[1])/"corpus/tools/dependency-freeze-contract.json"
c = json.loads(p.read_text())
del c["pins"]["r95-crossing-aftermath"]["fixture"]
p.write_text(json.dumps(c, indent=2)+"\n")
EOF
echo "=== C: path-less legacy pin, hand-run --freeze ==="
python3 "$ROOT_C/corpus/tools/dependency_freeze.py" --freeze "$ROOT_C/corpus/fixtures/r95-crossing-aftermath" > "$S/handrun-$LABEL/C-legacy.txt" 2>&1
echo "C exit=$?"
cat "$S/handrun-$LABEL/C-legacy.txt"
python3 - "$ROOT_C" <<'EOF'
import json, pathlib, sys
p = pathlib.Path(sys.argv[1])/"corpus/tools/dependency-freeze-contract.json"
pin = json.loads(p.read_text())["pins"]["r95-crossing-aftermath"]
print("C migrated pin fixture field:", repr(pin.get("fixture")))
EOF
