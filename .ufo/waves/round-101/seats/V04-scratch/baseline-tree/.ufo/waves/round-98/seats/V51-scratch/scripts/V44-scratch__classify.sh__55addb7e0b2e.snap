#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
declare -A OWN=(
 [corpus/tools/dependency_freeze.py]=S1 [corpus/tools/dependency-freeze-contract.json]=S1
 [corpus/tools/README.md]=S2 [corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md]=S3
 [corpus/knowledge/r98-clerk-scope-note.md]=S5 [corpus/knowledge/r95-aftermath-scope-note.md]=S5
 [corpus/knowledge/r96-response-scope-note.md]=S5 [LOG.md]=declaration
)
echo "=== full diff vs 9a3d648 (tracked) + untracked, corpus-scoped + repo-level ==="
git status --porcelain --untracked-files=all | grep -v '^?? \.ufo/' | grep -v '^ M LOG.md' > /tmp/v44.paths
while read -r st path; do
  case "$path" in
    corpus/fixtures/r98-clerk-filing/*) echo "DECLARED S3/S4  $st $path" ;;
    .ufo/*) : ;;
    *) if [ -n "${OWN[$path]}" ]; then echo "DECLARED ${OWN[$path]} $st $path"; else echo "*** STRAY *** $st $path"; fi ;;
  esac
done < /tmp/v44.paths
echo "=== stray count ==="
grep -c 'STRAY' /tmp/v44.paths >/dev/null 2>&1
strays=0
while read -r st path; do
  case "$path" in
    corpus/fixtures/r98-clerk-filing/*|.ufo/*) : ;;
    *) [ -z "${OWN[$path]}" ] && { echo "STRAY $st $path"; strays=$((strays+1)); } ;;
  esac
done < /tmp/v44.paths
echo "STRAYS=$strays"
