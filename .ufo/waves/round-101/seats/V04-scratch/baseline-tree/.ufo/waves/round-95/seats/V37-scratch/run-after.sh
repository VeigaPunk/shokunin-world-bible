#!/bin/bash
# V37 post-landing harness: run from repo root.
set -u
cd /home/vgpnk/Projects/shokunin/lore-shokunin
S=.ufo/waves/round-95/seats/V37-scratch
T=corpus/tools/map_obligations.py
OLD=$S/map_obligations_baseline.py

echo "== identity =="
md5sum "$T" "$OLD"
git diff fb118c4 --stat -- "$T" corpus/tools/map-obligations-contract.json

echo "== full battery (new) =="
for d in corpus/fixtures/*/; do
  [ -d "$d" ] || continue
  out=$(python3 "$T" "$d" 2>&1); rc=$?
  printf '%s\trc=%d\t%s\n' "${d%/}" "$rc" "$(echo "$out" | tr '\n' '~')"
done > $S/battery-new-full.tsv 2>&1
cut -f2 $S/battery-new-full.tsv | sort | uniq -c
echo "-- battery diff vs baseline --"
diff $S/battery-baseline-full.tsv $S/battery-new-full.tsv | head -60

echo "== scratch fixtures (new) =="
for d in $S/fixtures/*/; do
  out=$(python3 "$T" "$d" 2>&1); rc=$?
  printf '%-34s rc=%d | %s\n' "$(basename $d)" "$rc" "$(echo "$out" | tr '\n' '~')"
done

echo "== dialect probes (new) =="
for d in $S/dialect-probes/*/; do
  out=$(python3 "$T" "$d" 2>&1); rc=$?
  printf '%-24s rc=%d | %s\n' "$(basename $d)" "$rc" "$(echo "$out" | tr '\n' '~')"
done

echo "== self-test =="
python3 "$T" --self-test; echo "self-test rc=$?"

echo "== frozen r93 replay =="
python3 "$T" --frozen .ufo/waves/round-94/frozen/map-obligations-r93; echo "frozen rc=$?"

echo "== arg probes =="
out=$(python3 "$T" /tmp/v37-nomap 2>&1); echo "nomap rc=$? | $(echo "$out"|tr '\n' '~')"
out=$(python3 "$T" --self-test /tmp/v37-nomap 2>&1); echo "self-test+cluster rc=$? | $(echo "$out"|tr '\n' '~')"
out=$(python3 "$T" --bogus 2>&1); echo "unknown-flag rc=$? | $(echo "$out"|tr '\n' '~')"
out=$(python3 "$T" 2>&1); echo "no-args rc=$? | $(echo "$out"|tr '\n' '~')"
out=$(python3 "$T" --help 2>&1); echo "help rc=$? resultlines=$(echo "$out"|grep -c RESULT)"
out=$(python3 "$T" --frozen /tmp/v37-nomap corpus/fixtures/r94-paired-crossing 2>&1); echo "frozen+cluster rc=$? | $(echo "$out"|tr '\n' '~')"

echo "== mutation demo (old vs new, twice for stability) =="
for run in 1 2; do
  out=$(python3 "$OLD" $S/fixtures/mut-claims-renamed 2>&1); echo "old run$run rc=$? | $(echo "$out"|tr '\n' '~')"
  out=$(python3 "$T"   $S/fixtures/mut-claims-renamed 2>&1); echo "new run$run rc=$? | $(echo "$out"|tr '\n' '~')"
done

echo "== contract json =="
python3 - <<'PY'
import json
c = json.load(open("corpus/tools/map-obligations-contract.json"))
cases = c["self_test"]["cases"]
print("cases:", len(cases))
print("ids:", [x["id"] for x in cases])
PY

echo "== stdlib-only =="
python3 - <<'PY'
import ast, sys
tree = ast.parse(open("corpus/tools/map_obligations.py").read())
mods = set()
for n in ast.walk(tree):
    if isinstance(n, ast.Import): mods.update(a.name for a in n.names)
    elif isinstance(n, ast.ImportFrom): mods.add(n.module)
print("imports:", sorted(mods))
print("non-stdlib:", sorted(m for m in mods if m and m.split('.')[0] not in sys.stdlib_module_names))
PY
