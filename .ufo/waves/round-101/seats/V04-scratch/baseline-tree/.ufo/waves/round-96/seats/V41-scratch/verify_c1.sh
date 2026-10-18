#!/bin/bash
# V41 C1 verification (run from lane root)
set -u
S=.ufo/waves/round-96/seats/V41-scratch
T=corpus/tools/map_obligations.py

echo "=== REVISION PINS ==="
sha256sum $T corpus/tools/map-obligations-contract.json corpus/tools/README.md

echo "=== C1(b): self-test ==="
python3 $T --self-test > "$S/selftest.out" 2>&1; echo "EXIT=$?"
echo "PASS lines: $(grep -c 'SELF-TEST PASS' "$S/selftest.out")  FAIL lines: $(grep -c 'SELF-TEST FAIL' "$S/selftest.out")"
tail -3 "$S/selftest.out"
grep -E "schema_drift|inventory_mismatch" "$S/selftest.out" | head -6

echo "=== C1(b): contract case count ==="
python3 - <<'EOF'
import json
d=json.load(open('corpus/tools/map-obligations-contract.json'))
cs=d['self_test']['cases']
print('n cases:',len(cs))
print([c.get('id') for c in cs])
print('exit_codes:',d['exit_codes'])
EOF

echo "=== C1(a): deletion class (claims key + map row removed) ==="
rm -rf "$S/del2"; cp -r corpus/fixtures/r95-crossing-aftermath "$S/del2"
python3 - <<'EOF'
import json,pathlib
p=pathlib.Path('.ufo/waves/round-96/seats/V41-scratch/del2/entities.json')
d=json.loads(p.read_text()); del d[1]['claims']; p.write_text(json.dumps(d,indent=2)+"\n")
mp=pathlib.Path('.ufo/waves/round-96/seats/V41-scratch/del2/claim-excerpt-map.md')
lines=mp.read_text().split('\n'); out=[l for l in lines if not l.startswith('| J07 |')]
mp.write_text('\n'.join(out)); print('rows removed:',len(lines)-len(out))
EOF
python3 $T "$S/del2" --map claim-excerpt-map.md; echo "EXIT=$?"

echo "=== C1(a) isolation: row removed, key intact ==="
rm -rf "$S/del3"; cp -r corpus/fixtures/r95-crossing-aftermath "$S/del3"
python3 - <<'EOF'
import pathlib
mp=pathlib.Path('.ufo/waves/round-96/seats/V41-scratch/del3/claim-excerpt-map.md')
lines=mp.read_text().split('\n'); out=[l for l in lines if not l.startswith('| J07 |')]
mp.write_text('\n'.join(out)); print('rows removed:',len(lines)-len(out))
EOF
python3 $T "$S/del3" --map claim-excerpt-map.md; echo "EXIT=$?"

echo "=== C1(c): legacy dual-pointer cell ==="
rm -rf "$S/dual2"; cp -r corpus/fixtures/r88-m3-maya-cluster "$S/dual2"
python3 - <<'EOF'
import pathlib
mp=pathlib.Path('.ufo/waves/round-96/seats/V41-scratch/dual2/claim-excerpt-map.md')
t=mp.read_text()
old="| P2 | `entities[1].first_appearance` (Evin) |"
new="| P2 | `entities[1].first_appearance` (Evin): `entities[1].claims[0]` |"
assert old in t
mp.write_text(t.replace(old,new)); print('mutated P2 cell')
EOF
python3 $T "$S/dual2" --map claim-excerpt-map.md; echo "EXIT=$?"

echo "=== C1(c) isolation: unmutated r88 ==="
python3 $T corpus/fixtures/r88-m3-maya-cluster; echo "EXIT=$?"

echo "=== C1 non-regression: frozen r93 replay ==="
python3 $T --frozen .ufo/waves/round-94/frozen/map-obligations-r93; echo "EXIT=$?"

echo "=== C1 non-regression: r87/r89 fail-closed sweep ==="
n87=0; n89=0; bad=0
for d in corpus/fixtures/r87-*; do e=0; python3 $T "$d" >/dev/null 2>&1 || e=$?; n87=$((n87+1)); [ $e -ne 2 ] && { echo "NON2 $d exit=$e"; bad=1; }; done
for d in corpus/fixtures/r89-*; do e=0; python3 $T "$d" >/dev/null 2>&1 || e=$?; n89=$((n89+1)); [ $e -ne 2 ] && { echo "NON2 $d exit=$e"; bad=1; }; done
echo "r87 dirs=$n87 r89 dirs=$n89 all_exit2=$([ $bad -eq 0 ] && echo yes || echo NO)"

echo "=== C1 non-regression: full corpus sweep ==="
declare -A hist
zeros=""
for d in corpus/fixtures/*/; do
  e=0; python3 $T "$d" >/dev/null 2>&1 || e=$?
  hist[$e]=$(( ${hist[$e]:-0} + 1 ))
  [ $e -eq 0 ] && zeros="$zeros $(basename $d)"
done
echo "exit histogram:"; for k in $(echo "${!hist[@]}" | tr ' ' '\n' | sort); do echo "  exit $k: ${hist[$k]}"; done
echo "exit0 dirs:$zeros"

echo "=== C1 non-regression: 0/1/2 CLI contract ==="
python3 $T >/dev/null 2>&1; echo "no-arg EXIT=$?"
python3 $T --bogus >/dev/null 2>&1; echo "bad-flag EXIT=$?"
python3 $T corpus/fixtures/r95-crossing-aftermath >/dev/null 2>&1; echo "r95 EXIT=$?"
