#!/bin/bash
# Perturbation battery on SCRATCH copies of tool+contract. Never touches the live tree.
set -u
REPO=/home/vgpnk/Projects/shokunin/lore-shokunin
SCRATCH=$REPO/.ufo/waves/round-96/scratch/V02/perturb
rm -rf "$SCRATCH"; mkdir -p "$SCRATCH"
run_variant () {
  local name="$1" mutator="$2"
  local root="$SCRATCH/$name"
  mkdir -p "$root/corpus/tools"
  cp "$REPO/corpus/tools/map_obligations.py" "$root/corpus/tools/"
  cp "$REPO/corpus/tools/map-obligations-contract.json" "$root/corpus/tools/"
  python3 - "$root/corpus/tools/map-obligations-contract.json" "$name" "$mutator" <<'PY'
import json, sys
path, name, mutator = sys.argv[1], sys.argv[2], sys.argv[3]
c = json.load(open(path))
cases = c["self_test"]["cases"]
by = {x["id"]: x for x in cases}
if mutator == "flip_exit":            by["complete"]["exit"] = 1
elif mutator == "flip_findings":      by["missing"]["finding_ids"] = ["missing_obligation", "phantom_obligation"]
elif mutator == "drop_case":          cases.pop([i for i,x in enumerate(cases) if x["id"]=="schema_drift"][0])
elif mutator == "dup_case":           cases.append(dict(by["inventory_mismatch"]))
elif mutator == "bad_exit_type":      by["inventory_mismatch"]["exit"] = "1"
elif mutator == "bad_findings_type":  by["schema_drift"]["finding_ids"] = "schema_drift"
else: raise SystemExit("unknown mutator " + mutator)
json.dump(c, open(path, "w"), indent=1)
PY
  echo "=== VARIANT $name ($mutator) ==="
  ( cd "$root" && python3 corpus/tools/map_obligations.py --self-test; echo "EXIT=$?" ) 2>&1 | grep -E "FAIL|FINDING|RESULT|EXIT=" 
}
run_variant A_flip_exit flip_exit
run_variant B_flip_findings flip_findings
run_variant C_drop_case drop_case
run_variant D_dup_case dup_case
run_variant E_bad_exit_type bad_exit_type
run_variant F_bad_findings_type bad_findings_type
echo "=== scratch tree untouched check ==="
ls "$REPO/corpus/tools/" | grep -v __pycache__
