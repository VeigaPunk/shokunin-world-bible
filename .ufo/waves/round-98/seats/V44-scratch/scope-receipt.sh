#!/bin/bash
# V44 scope receipt: four inherited tools + all inherited fixture JSON tables
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
S=.ufo/waves/round-98/seats/V44-scratch
# A) baseline side (blobs at 9a3d648)
git ls-tree -r 9a3d648 corpus/fixtures corpus/tools | grep -E '\.json$|check_bible\.py$|support_check\.py$|boundary_doc_check\.py$|discriminate_check\.py$' | awk '{print $3" "$4}' | sort -k2 > "$S/scope-baseline.txt"
# B) delivered side (working tree)
while read -r h p; do cur=$(git hash-object "$p"); echo "$cur $p"; done < "$S/scope-baseline.txt" | sort -k2 > "$S/scope-delivered.txt"
diff <(cut -d' ' -f1 "$S/scope-baseline.txt") <(cut -d' ' -f1 "$S/scope-delivered.txt") >/dev/null && VERDICT=UNCHANGED || VERDICT=CHANGED
echo "scope_paths=$(wc -l < "$S/scope-baseline.txt") verdict=$VERDICT"
echo "baseline_aggregate_sha256=$(sha256sum < "$S/scope-baseline.txt" | cut -d' ' -f1)"
echo "delivered_aggregate_sha256=$(sha256sum < "$S/scope-delivered.txt" | cut -d' ' -f1)"
echo "tools_in_scope:"; grep -E 'check_bible\.py|support_check\.py|boundary_doc_check\.py|discriminate_check\.py' "$S/scope-delivered.txt"
echo "changed_lines:"; diff "$S/scope-baseline.txt" "$S/scope-delivered.txt" | head -20
