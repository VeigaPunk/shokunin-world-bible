#!/bin/bash
# V07 probe: (A) path-less legacy pin migrated in place; (B) same-named elsewhere still refused.
set -u
cd /home/vgpnk/Projects/shokunin/lore-shokunin
S=.ufo/waves/round-98/seats/V07-scratch/migrate-probe
rm -rf "$S"; mkdir -p "$S"

for R in rootA rootB; do
  mkdir -p "$S/$R/corpus/tools" "$S/$R/corpus/fixtures"
  cp corpus/tools/dependency_freeze.py "$S/$R/corpus/tools/"
  cp corpus/tools/dependency-freeze-contract.json "$S/$R/corpus/tools/"
done
cp -r corpus/fixtures/r98-clerk-filing "$S/rootA/corpus/fixtures/"
mkdir -p "$S/rootB/corpus/fixtures/moved"
cp -r corpus/fixtures/r98-clerk-filing "$S/rootB/corpus/fixtures/moved/"

# Root A: strip the fixture path from the r98 pin (legacy path-less pin)
python3 - "$S/rootA/corpus/tools/dependency-freeze-contract.json" <<'EOF'
import json, sys
p = sys.argv[1]
c = json.load(open(p))
del c["pins"]["r98-clerk-filing"]["fixture"]
json.dump(c, open(p, "w"), indent=2, ensure_ascii=False)
open(p, "a").write("\n")
print("rootA pin fixture key present:", "fixture" in c["pins"]["r98-clerk-filing"])
EOF

echo "=== PROBE A: --freeze with path-less legacy pin ==="
cd "$S/rootA"
python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/r98-clerk-filing; echo "EXIT_A=$?"
python3 - <<'EOF'
import json
c = json.load(open("corpus/tools/dependency-freeze-contract.json"))
print("after: r98 fixture field =", repr(c["pins"]["r98-clerk-filing"].get("fixture")))
EOF

echo "=== PROBE B: --freeze same-named elsewhere (must refuse) ==="
cd "$S/rootB"
python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/moved/r98-clerk-filing; echo "EXIT_B=$?"
