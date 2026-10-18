#!/bin/bash
# V28 round-98 C1/C2 operability probes — mirror roots only; delivered files never written.
set -u
R=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$R/.ufo/waves/round-98/seats/V28-scratch
P=$S/probes
rm -rf "$P"; mkdir -p "$P"
cd "$R"

mirror() { # $1 = case dir; copies tool+contract into $P/$1/corpus/tools
  local d="$P/$1"
  mkdir -p "$d/corpus/tools" "$d/corpus/fixtures"
  cp corpus/tools/dependency_freeze.py "$d/corpus/tools/"
  cp corpus/tools/dependency-freeze-contract.json "$d/corpus/tools/"
  echo "$d"
}

echo "=== M1: C1b path-less legacy pin migrated in place by --freeze ==="
M1=$(mirror legacy-migrate)
cp -r corpus/fixtures/r95-crossing-aftermath "$M1/corpus/fixtures/"
python3 - "$M1/corpus/tools/dependency-freeze-contract.json" <<'PY'
import json,sys
p=sys.argv[1]; c=json.load(open(p))
print("pre: fixture key present =", "fixture" in c["pins"]["r95-crossing-aftermath"])
del c["pins"]["r95-crossing-aftermath"]["fixture"]
json.dump(c,open(p,"w"),indent=2,ensure_ascii=False); open(p,"a").write("\n")
print("pre: fixture key deleted")
PY
python3 "$M1/corpus/tools/dependency_freeze.py" --freeze "$M1/corpus/fixtures/r95-crossing-aftermath"
echo "M1-EXIT=$?"
python3 - "$M1/corpus/tools/dependency-freeze-contract.json" <<'PY'
import json,sys
c=json.load(open(sys.argv[1]))
print("post: migrated fixture value =", repr(c["pins"]["r95-crossing-aftermath"].get("fixture")))
PY

echo "=== M2: C2 scratch REDUCTION-DETECTED on the r97 tick-13 edge ==="
M2=$(mirror r97-edge)
cp -r corpus/fixtures/r97-crossing-acknowledgment "$M2/corpus/fixtures/"
python3 - "$M2/corpus/fixtures/r97-crossing-acknowledgment/timeline.json" <<'PY'
import json,sys
p=sys.argv[1]; t=json.load(open(p))
for r in t:
    if r["id"]=="acknowledgment-aru-records":
        r["depends_on"]=[d for d in r["depends_on"] if d!="response-evin-salt-court"]
json.dump(t,open(p,"w"),indent=2); open(p,"a").write("\n")
PY
python3 "$M2/corpus/tools/dependency_freeze.py" "$M2/corpus/fixtures/r97-crossing-acknowledgment"
echo "M2-EXIT=$?"

echo "=== M3: C1a SELF-TEST-MISMATCH exits 2 under a flipped expectation (pin load-bearing) ==="
M3=$(mirror neutralized)
cp -r corpus/fixtures/r95-crossing-aftermath "$M3/corpus/fixtures/"
python3 - "$M3/corpus/tools/dependency-freeze-contract.json" <<'PY'
import json,sys
p=sys.argv[1]; c=json.load(open(p))
c["self_test"]["expected"]["clean"]["exit"]=1
json.dump(c,open(p,"w"),indent=2,ensure_ascii=False); open(p,"a").write("\n")
print("flipped clean exit -> 1")
PY
python3 "$M3/corpus/tools/dependency_freeze.py" --self-test
echo "M3-EXIT=$?"

echo "=== M4: same-named-elsewhere refusal retained (SCOPE-REFUSED) ==="
M4=$(mirror foreign-freeze)
mkdir -p "$M4/corpus/fixtures/foreign"
cp -r corpus/fixtures/r95-crossing-aftermath "$M4/corpus/fixtures/foreign/"
python3 "$M4/corpus/tools/dependency_freeze.py" --freeze "$M4/corpus/fixtures/foreign/r95-crossing-aftermath"
echo "M4-EXIT=$?"

echo "=== M5: r98 tick-14 edge REDUCTION-DETECTED (chain endpoint now pinned) ==="
M5=$(mirror r98-edge)
cp -r corpus/fixtures/r98-clerk-filing "$M5/corpus/fixtures/"
python3 - "$M5/corpus/fixtures/r98-clerk-filing/timeline.json" <<'PY'
import json,sys
p=sys.argv[1]; t=json.load(open(p))
for r in t:
    if r["id"]=="clerk-filing-open":
        r["depends_on"]=[d for d in r["depends_on"] if d!="acknowledgment-aru-records"]
json.dump(t,open(p,"w"),indent=2); open(p,"a").write("\n")
PY
python3 "$M5/corpus/tools/dependency_freeze.py" "$M5/corpus/fixtures/r98-clerk-filing"
echo "M5-EXIT=$?"
