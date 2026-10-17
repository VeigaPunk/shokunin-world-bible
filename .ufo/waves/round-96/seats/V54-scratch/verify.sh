#!/bin/bash
# V54 relation-scope-2 verification harness
set -u
cd /home/vgpnk/Projects/shokunin/lore-shokunin
S=.ufo/waves/round-96/seats/V54-scratch
R95=corpus/fixtures/r95-crossing-aftermath
R96=corpus/fixtures/r96-crossing-response

echo "### 1. relations.json byte identity r95 -> r96"
sha256sum $R95/relations.json $R96/relations.json
cmp $R95/relations.json $R96/relations.json && echo "CMP: byte-identical (exit 0)" || echo "CMP: DIFFERS (exit $?)"

echo
echo "### 1b. chain identity r94 -> r96"
sha256sum corpus/fixtures/r94-paired-crossing/relations.json

echo
echo "### 2. r96 relation map row(s)"
grep -n 'relations\.json#/' $R96/claim-excerpt-map.md

echo
echo "### 2b. r95 relation map row (baseline)"
grep -n 'relations\.json#/' $R95/claim-excerpt-map.md

echo
echo "### 2c. relation row count r96"
grep -c 'relations\.json#/' $R96/claim-excerpt-map.md

echo
echo "### 3. map_obligations on r96"
python3 corpus/tools/map_obligations.py $R96; echo "exit=$?"

echo
echo "### 3b. map_obligations on r95 (control)"
python3 corpus/tools/map_obligations.py $R95; echo "exit=$?"

echo
echo "### 4. relation semantics in tool: r95 vs r96 diff (relation-relevant lines)"
grep -n 'relation' $S/r95-map_obligations.py > $S/r95-rel-lines.txt
grep -n 'relation' corpus/tools/map_obligations.py > $S/r96-rel-lines.txt
diff $S/r95-rel-lines.txt $S/r96-rel-lines.txt && echo "RELATION-LINES: identical" || echo "RELATION-LINES: see diff above"

echo
echo "### 4b. contract relation scope / grammar"
python3 - <<'EOF'
import json
old=json.load(open('.ufo/waves/round-96/seats/V54-scratch/r95-contract.json'))
new=json.load(open('corpus/tools/map-obligations-contract.json'))
for k in ('scope','raw_files','map_grammar','legacy_pointer_dialect','exit_codes'):
    same = old.get(k)==new.get(k)
    print(f"{k}: {'IDENTICAL' if same else 'CHANGED'}")
    if not same:
        print("  old:", json.dumps(old.get(k))[:400])
        print("  new:", json.dumps(new.get(k))[:400])
print("self_test cases old:", len(old['self_test']['cases']), "new:", len(new['self_test']['cases']))
EOF

echo
echo "### 5. r96 map declared inventory + relation mention"
grep -n 'Expected inventory' $R96/claim-excerpt-map.md
grep -n -i 'relation' $R96/claim-excerpt-map.md

echo
echo "### 6. r96 map scope line"
sed -n '1,6p' $R96/claim-excerpt-map.md

echo
echo "### 7. relation type token anywhere in r96 fixture"
grep -rn 'agreed_co_stewardship_for_this_crossing' $R96/ || echo "(no occurrences)"

echo
echo "### 8. all relation-ish tokens in r96 fixture"
grep -rn '"type"' $R96/*.json
