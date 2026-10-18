#!/bin/bash
# V11 fakerepo probes: exercises --freeze accept/reject, path binding, DIGEST-MISMATCH naming
# entirely inside a sandbox mirror of the repo (ROOT = <sandbox>), so the real producer
# contract is never written. Run from repo root.
set -u
R=/home/vgpnk/Projects/shokunin/lore-shokunin
FR=$R/.ufo/waves/round-97/seats/V11-scratch/fakerepo
TMP=$R/.ufo/waves/round-97/seats/V11-scratch/tmp
export TMPDIR=$TMP
rm -rf "$FR"
mkdir -p "$FR/corpus/tools" "$FR/corpus/fixtures" "$FR/elsewhere"
cp "$R/corpus/tools/dependency_freeze.py" "$FR/corpus/tools/"
cp "$R/corpus/tools/dependency-freeze-contract.json" "$FR/corpus/tools/"
cp -a "$R/corpus/fixtures/r95-crossing-aftermath" "$FR/corpus/fixtures/"
cp -a "$R/corpus/fixtures/r95-crossing-aftermath" "$FR/elsewhere/"
ln -s "$FR/elsewhere/r95-crossing-aftermath" "$FR/corpus/fixtures/lnk-foreign"
ln -s "$FR/corpus/fixtures/r95-crossing-aftermath" "$FR/corpus/fixtures/lnk-same"
cd "$FR" || exit 1
echo "### FR-A accept: --freeze inside corpus/fixtures (fakerepo contract)"
python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/r95-crossing-aftermath; echo "exit=$?"
echo "### FR-B reject: --freeze outside corpus/fixtures"
python3 corpus/tools/dependency_freeze.py --freeze elsewhere/r95-crossing-aftermath; echo "exit=$?"
echo "### FR-C traversal bypass attempt (corpus/fixtures/../../elsewhere/...)"
python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/../../elsewhere/r95-crossing-aftermath; echo "exit=$?"
echo "### FR-D symlink inside scope -> outside (must refuse if guard resolves)"
python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/lnk-foreign; echo "exit=$?"
echo "### FR-E verify at pinned path (expect PASS)"
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath; echo "exit=$?"
echo "### FR-F verify symlink resolving TO pinned path (expect PASS)"
python3 corpus/tools/dependency_freeze.py corpus/fixtures/lnk-same; echo "exit=$?"
echo "### FR-G verify foreign copy (expect PATH-MISMATCH exit 2)"
python3 corpus/tools/dependency_freeze.py elsewhere/r95-crossing-aftermath; echo "exit=$?"
echo "### FR-H DIGEST-MISMATCH naming: tamper sources.json at the pinned path"
python3 - <<'EOF'
import json, pathlib
p = pathlib.Path("corpus/fixtures/r95-crossing-aftermath/sources.json")
p.write_text(json.dumps(json.loads(p.read_text()), indent=4) + "\n")
print("re-indented sources.json at pinned path")
EOF
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath; echo "exit=$?"
echo "### FR-I fakerepo contract pins/keys after probes"
python3 - <<'EOF'
import json
c = json.load(open("corpus/tools/dependency-freeze-contract.json"))
print("top-level keys:", sorted(c))
for k, v in c["pins"].items():
    print(f"pin {k}: fixture={v.get('fixture')!r} has_path_key={'path' in v}")
print("self_test expected count:", len(c.get("self_test", {}).get("expected", {})))
EOF
