#!/bin/bash
# V40 pre-state negatives against the 9a3d648 baseline tool (mirror root $1)
set -u
M="$1"
TOOL="$M/corpus/tools/dependency_freeze.py"
CT="$M/corpus/tools/dependency-freeze-contract.json"
BASE="$M/base-contract.json"
FIX="$M/corpus/fixtures/r95-crossing-aftermath"

echo "### pre-a: SELF-TEST-MISMATCH exit (self_test.expected.clean.exit:=1)"
cp "$BASE" "$CT"
python3 - "$CT" <<'PY'
import json,sys
p=sys.argv[1]; c=json.load(open(p))
c["self_test"]["expected"]["clean"]["exit"]=1
json.dump(c,open(p,"w"),indent=2,ensure_ascii=False)
PY
python3 "$TOOL" --self-test; echo "EXIT=$?"

echo
echo "### pre-a2: SELF-TEST-MISMATCH via missing case key (expected set mismatch)"
cp "$BASE" "$CT"
python3 - "$CT" <<'PY'
import json,sys
p=sys.argv[1]; c=json.load(open(p))
del c["self_test"]["expected"]["clean"]
json.dump(c,open(p,"w"),indent=2,ensure_ascii=False)
PY
python3 "$TOOL" --self-test; echo "EXIT=$?"

echo
echo "### pre-b: path-less legacy pin under --freeze"
cp "$BASE" "$CT"
python3 - "$CT" <<'PY'
import json,sys
p=sys.argv[1]; c=json.load(open(p))
c["pins"]["r95-crossing-aftermath"].pop("fixture",None)
json.dump(c,open(p,"w"),indent=2,ensure_ascii=False)
PY
python3 "$TOOL" --freeze "$FIX"; echo "EXIT=$?"

echo
echo "### pre-b2: path-less legacy pin under verify"
cp "$BASE" "$CT"
python3 - "$CT" <<'PY'
import json,sys
p=sys.argv[1]; c=json.load(open(p))
c["pins"]["r95-crossing-aftermath"].pop("fixture",None)
json.dump(c,open(p,"w"),indent=2,ensure_ascii=False)
PY
python3 "$TOOL" "$FIX"; echo "EXIT=$?"

echo
echo "### pre-c: precedence text"
python3 -c "import json;print(json.load(open('$BASE'))['precedence'])"
