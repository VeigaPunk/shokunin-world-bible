#!/bin/bash
# V52 manifest: baseline blob vs worktree bytes for inherited tools + r88-r95 fixtures
cd /home/vgpnk/Projects/shokunin/lore-shokunin
BASE=dcb2d92
OUT="$1"
{
for f in corpus/tools/support_check.py corpus/tools/boundary_doc_check.py corpus/tools/boundary-doc-contract.json corpus/tools/discriminate_check.py corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json corpus/tools/README.md corpus/fixtures/check_bible.py corpus/live/rejected-r4/check_bible.py corpus/fixtures/README.md; do
  m=$(git ls-tree $BASE -- "$f" | awk '{print $1}')
  b=$(git cat-file -p "$BASE:$f" | sha256sum | cut -d' ' -f1)
  w=$(sha256sum "$f" 2>/dev/null | cut -d' ' -f1)
  echo "$f $m $b $w"
done
while read -r f; do
  m=$(git ls-tree $BASE -- "$f" | awk '{print $1}')
  b=$(git rev-parse "$BASE:$f")
  w=$(git hash-object "$f" 2>/dev/null || echo MISSING)
  echo "$f $m $b $w"
done < .ufo/waves/round-96/seats/V52-scratch/base_files.txt
} > "$OUT"
echo "lines=$(wc -l < $OUT)"; awk 'NF==4 && $3!=$4 {print "DIFF:",$0}' "$OUT" | head; echo "diffs=$(awk 'NF==4 && $3!=$4' $OUT | wc -l)"
