#!/bin/bash
# V07 r96 verification battery — run from the lane repo root against the frozen revision.
set -u
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 1
S=.ufo/waves/round-96/seats/V07-scratch
TOOL=$S/map_obligations_reviewed.py

echo "### revision"
md5sum "$TOOL" corpus/tools/map_obligations.py
git hash-object corpus/tools/map_obligations.py

echo "### self-test"
python3 "$TOOL" --self-test; echo "self-test rc=$?"

echo "### contract cases"
python3 - <<'PY'
import json
d = json.load(open('corpus/tools/map-obligations-contract.json'))
cases = d['self_test']['cases']
print('cases:', len(cases), [c['id'] for c in cases])
PY

echo "### delivered map clusters (current tree)"
for d in corpus/fixtures/r87-myth-cluster corpus/fixtures/r88-m3-maya-cluster \
         corpus/fixtures/r89-inspiration-paraphrase corpus/fixtures/r93-m2-kojiki-cluster \
         corpus/fixtures/r94-paired-crossing corpus/fixtures/r95-crossing-aftermath \
         corpus/fixtures/r96-crossing-response; do
  [ -d "$d" ] || { echo "$d ABSENT"; continue; }
  out=$(python3 "$TOOL" "$d" 2>&1); rc=$?
  echo "$d rc=$rc | $(echo "$out" | tr '\n' '~')"
done

echo "### frozen r93 replay"
python3 "$TOOL" --frozen .ufo/waves/round-94/frozen/map-obligations-r93; echo "frozen rc=$?"

echo "### probe battery"
for d in $S/probes/*/; do
  n=$(basename "$d"); out=$(python3 "$TOOL" "$d" 2>&1); rc=$?
  echo "$n rc=$rc | $(echo "$out" | tr '\n' '~')"
done > "$S/probe-after.tsv"
echo "probes=$(wc -l < "$S/probe-after.tsv")"

echo "### corpus battery"
for d in $(find corpus -name entities.json -printf '%h\n' | sort); do
  out=$(python3 "$TOOL" "$d" 2>&1); rc=$?
  echo "$d rc=$rc | $(echo "$out" | tr '\n' '~')"
done > "$S/corpus-after.tsv"
echo "dirs=$(wc -l < "$S/corpus-after.tsv")"

echo "### contract audit"
python3 "$S/contract_audit.py" "$S/corpus-after.tsv"
python3 "$S/contract_audit.py" "$S/probe-after.tsv"

echo "### stdlib-only import scan"
python3 - "$TOOL" <<'PY'
import ast, sys
tree = ast.parse(open(sys.argv[1], encoding='utf-8').read())
mods = set()
for node in ast.walk(tree):
    if isinstance(node, ast.Import):
        mods.update(alias.name.split('.')[0] for alias in node.names)
    elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
        mods.add(node.module.split('.')[0])
stdlib = set(sys.stdlib_module_names)
print('imports:', sorted(mods))
print('non-stdlib:', sorted(mods - stdlib))
PY

echo "### live-tree digest"
python3 "$S/tree_digest.py"
echo "before: $(cat "$S/corpus-tree-before.txt" | wc -l) files"
