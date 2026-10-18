#!/bin/bash
# V31 C1 operability battery. Live tree is read-only except gitignored self-test scratch.
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
SCR="$LANE/.ufo/waves/round-99/seats/V31-scratch"
OUT="$SCR/c1-battery.txt"
cd "$LANE" || exit 1
exec > >(tee "$OUT") 2>&1
echo "BATTERY-START $(date '+%Y-%m-%d %H:%M:%S %z')"
echo "=== frozen hashes ==="
sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
python3 - << 'PY'
import hashlib, json
from pathlib import Path
d = json.loads(Path("corpus/tools/dependency-freeze-contract.json").read_text())
print("schema", d.get("schema_version"), "payload", d.get("payload_schema_version"), "revision", d.get("revision"))
print("pinned_files", d.get("pinned_files"))
chain = ["r88-m3-maya-cluster","r94-paired-crossing","r95-crossing-aftermath","r96-crossing-response","r97-crossing-acknowledgment","r98-clerk-filing"]
for name in chain:
    pin = d["pins"][name]
    files = pin["files"]
    print(f"PIN {name} n={len(files)} schema={pin.get('payload_schema_version')} digest={pin['content_sha256']}")
    mismatch = []
    for fn, want in sorted(files.items()):
        raw = Path("corpus/fixtures")/name/fn
        got = hashlib.sha256(raw.read_bytes()).hexdigest() if raw.is_file() else "MISSING"
        if got != want:
            mismatch.append(fn)
    print("  live-vs-pin", "MATCH" if not mismatch else "MISMATCH "+",".join(mismatch))
print("self_test", sorted(d["self_test"]["expected"]))
print("markdown_tamper", d["self_test"]["expected"].get("markdown_tamper"))
PY

echo "=== git status before ==="
git status --porcelain > "$SCR/git-before.txt"
wc -l "$SCR/git-before.txt"

echo "=== chain verify ==="
for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response r97-crossing-acknowledgment r98-clerk-filing; do
  python3 corpus/tools/dependency_freeze.py "corpus/fixtures/$f" > "$SCR/chain-$f.txt"
  echo "$f EXIT=$?"
  cat "$SCR/chain-$f.txt"
done

echo "=== r99 verify (not claimed pinned) ==="
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse > "$SCR/r99-freeze.txt"
echo "r99 EXIT=$?"
cat "$SCR/r99-freeze.txt"

echo "=== self-test ==="
python3 corpus/tools/dependency_freeze.py --self-test > "$SCR/self-test.txt"
echo "SELFTEST EXIT=$?"
tail -30 "$SCR/self-test.txt"

echo "=== exit contract live (no writes expected) ==="
python3 corpus/tools/dependency_freeze.py > "$SCR/exit-noarg.txt"
echo "noarg EXIT=$?"
cat "$SCR/exit-noarg.txt"
python3 corpus/tools/dependency_freeze.py --help > "$SCR/exit-help.txt"
echo "help EXIT=$?"
python3 corpus/tools/dependency_freeze.py --self-test corpus/fixtures/r98-clerk-filing > "$SCR/exit-misuse.txt"
echo "misuse EXIT=$?"
cat "$SCR/exit-misuse.txt"
python3 corpus/tools/dependency_freeze.py corpus/fixtures/no-such-dir/r98-clerk-filing > "$SCR/exit-missing.txt"
echo "missing-pinned-name EXIT=$?"
cat "$SCR/exit-missing.txt"
CT_BEFORE=$(sha256sum corpus/tools/dependency-freeze-contract.json | awk '{print $1}')
python3 corpus/tools/dependency_freeze.py --freeze "$SCR/not-a-fixture" > "$SCR/exit-scope.txt"
echo "scope EXIT=$?"
cat "$SCR/exit-scope.txt"
CT_AFTER=$(sha256sum corpus/tools/dependency-freeze-contract.json | awk '{print $1}')
echo "contract-after-scope $CT_BEFORE $CT_AFTER"

echo "=== mirror probes ==="
python3 "$SCR/c1-mirrors.py"

echo "=== git status after ==="
git status --porcelain > "$SCR/git-after.txt"
if cmp -s "$SCR/git-before.txt" "$SCR/git-after.txt"; then echo "GIT-STATUS-IDENTICAL"; else echo "GIT-STATUS-DIFF"; diff -u "$SCR/git-before.txt" "$SCR/git-after.txt" | head -40; fi
echo "=== hashes after ==="
sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
echo "BATTERY-END $(date '+%Y-%m-%d %H:%M:%S %z')"
