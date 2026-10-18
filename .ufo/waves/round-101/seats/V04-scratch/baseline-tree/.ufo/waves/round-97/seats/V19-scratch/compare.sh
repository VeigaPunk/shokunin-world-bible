#!/bin/bash
set -u
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
S=.ufo/waves/round-97/seats/V19-scratch
MAP=corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
echo "=== 1. git diff f3e09f9 -- map ==="
git diff f3e09f9 -- "$MAP"
echo "=== 2. diff --stat (whole r96 fixture) ==="
git diff --stat f3e09f9 -- corpus/fixtures/r96-crossing-response/
echo "=== 3. post sha256 ==="
sha256sum "$MAP"
echo "=== 4. data rows post vs baseline ==="
grep -E '^\| (J[0-9]{2}|S[0-9]{2}) ' "$MAP" > $S/post-datarows.txt
if cmp -s $S/baseline-datarows.txt $S/post-datarows.txt; then echo "DATAROWS-IDENTICAL $(wc -l < $S/post-datarows.txt) rows"; else echo "DATAROWS-DIFFER"; diff $S/baseline-datarows.txt $S/post-datarows.txt; fi
echo "=== 5. non-data-row lines changed vs baseline ==="
diff <(grep -vE '^\| (J[0-9]{2}|S[0-9]{2}) ' $S/r96-map-baseline.md) <(grep -vE '^\| (J[0-9]{2}|S[0-9]{2}) ' "$MAP")
echo "=== 6. support_check post ==="
python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response > $S/r96-support-post.txt 2>&1; echo "exit=$?"
diff $S/r96-support-pre.txt $S/r96-support-post.txt && echo "SUPPORT-RECEIPT-IDENTICAL" || echo "SUPPORT-OUTPUT-DIFFERS"
echo "=== 7. map_obligations post ==="
python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response > $S/r96-mapobl-post.txt 2>&1; echo "exit=$?"
diff $S/r96-mapobl-pre.txt $S/r96-mapobl-post.txt && echo "MAPOBL-RECEIPT-IDENTICAL" || echo "MAPOBL-OUTPUT-DIFFERS"
echo "=== 8. delimiter cell counts post ==="
awk -F'|' '{n=NF-2; if(n>0) printf "%d:%d ", NR, n}' "$MAP" | tr ' ' '\n' | grep -n .
