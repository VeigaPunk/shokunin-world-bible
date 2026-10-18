#!/bin/sh
# V27 r99 adjacency — rights/mechanics language scan. Usage: rights_scan.sh <outfile>
# Run from lane repo root AFTER freeze. Scans all r99 new bytes + round diffs.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 1
OUT="${1:-/tmp/v27-rights.txt}"
BASE=4265df5
NEW_FILES="corpus/fixtures/r99-window-lapse/README.md corpus/fixtures/r99-window-lapse/claim-excerpt-map.md corpus/fixtures/r99-window-lapse/contradictions.json corpus/fixtures/r99-window-lapse/entities.json corpus/fixtures/r99-window-lapse/fictional-excerpts.md corpus/fixtures/r99-window-lapse/inspiration-note.md corpus/fixtures/r99-window-lapse/relations.json corpus/fixtures/r99-window-lapse/source-excerpt.md corpus/fixtures/r99-window-lapse/sources.json corpus/fixtures/r99-window-lapse/timeline.json corpus/knowledge/r99-gate-blind-spot-table.md corpus/knowledge/r99-lapse-scope-note.md"
{
  echo "== A. mechanics/grant phrase scan on new bytes =="
  grep -n -i -E "mechanic|gameplay|ruleset|damage|stats|balancing|hit ?point|dice|combat|level.?up|public domain|fair use|free to (use|reuse)|may be (used|reproduced)" $NEW_FILES
  echo "(rc=$?)"
  echo
  echo "== B. mechanics/grant phrase scan on round diffs (tools + skill + knowledge + fixture vs baseline) =="
  git diff $BASE -- corpus/tools/ SKILL.md corpus/knowledge/ corpus/fixtures/r99-window-lapse/ | grep -n -i -E "^[+-].*(mechanic|gameplay|ruleset|damage|stats|balancing|public domain|fair use|free to (use|reuse)|may be (used|reproduced))"
  echo "(rc=$?)"
  echo
  echo "== C. broader rights/permission/canon/training hits in new bytes =="
  grep -n -i -E "rights|licen[cs]e|copyright|permission|canon|training|attribut" $NEW_FILES
  echo "(rc=$?)"
  echo
  echo "== D. adjacency-string scan (absolute paths / escapes) in new bytes =="
  grep -n -E "/home/|\\.\\./|/tmp/" $NEW_FILES
  echo "(rc=$?)"
  echo
  echo "== E. sibling-lane names in round diffs of producer-owned paths =="
  git diff $BASE -- corpus/tools/ SKILL.md corpus/knowledge/ corpus/fixtures/r99-window-lapse/ | grep -n -i -E "^[+-].*(kotodama|game-dev|art-east|kengaku|mado-shokunin|tabi-shokunin|sibling lane|/home/|\\.\\./)"
  echo "(rc=$?)"
  echo
  echo "== F. external-name scan in r99 JSON + knowledge notes =="
  grep -n -i -E "Spence|Kojiki|Chamberlain|Gutenberg|ETCSL|Inana|Ovid|Maya|Kiche|K'iche" corpus/fixtures/r99-window-lapse/*.json corpus/knowledge/r99-gate-blind-spot-table.md corpus/knowledge/r99-lapse-scope-note.md
  echo "(rc=$?)"
  echo
  echo "== G. byte-copy integrity: r99 preserving copy vs baseline r98 =="
  for f in README.md claim-excerpt-map.md contradictions.json entities.json fictional-excerpts.md inspiration-note.md relations.json source-excerpt.md sources.json timeline.json; do
    a=$(sha256sum corpus/fixtures/r99-window-lapse/$f | cut -c1-16)
    b=$(git show $BASE:corpus/fixtures/r98-clerk-filing/$f | sha256sum | cut -c1-16)
    if [ "$a" = "$b" ]; then echo "SAME  $f $a"; else echo "DIFF  $f r99=$a r98=$b"; fi
  done
  echo
  echo "== H. fictional-excerpts prefix check (r98 bytes prefix of r99?) =="
  git show $BASE:corpus/fixtures/r98-clerk-filing/fictional-excerpts.md > /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V27-scratch/r98-fx.md
  r98n=$(wc -c < /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V27-scratch/r98-fx.md)
  r99n=$(wc -c < corpus/fixtures/r99-window-lapse/fictional-excerpts.md)
  echo "r98_bytes=$r98n r99_bytes=$r99n"
  head -c "$r98n" corpus/fixtures/r99-window-lapse/fictional-excerpts.md | cmp - /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V27-scratch/r98-fx.md && echo "PREFIX-IDENTICAL" || echo "PREFIX-DIFFERS"
  echo
  echo "== I. resolution/blame/reconciliation wording in r99 new authored files (report, not auto-fail) =="
  grep -n -i -E "resolut|blame|reconcil|closed the matter|matter is closed|finding" corpus/fixtures/r99-window-lapse/fictional-excerpts.md corpus/fixtures/r99-window-lapse/README.md corpus/fixtures/r99-window-lapse/claim-excerpt-map.md corpus/knowledge/r99-lapse-scope-note.md corpus/knowledge/r99-gate-blind-spot-table.md
  echo "(rc=$?)"
} > "$OUT" 2>&1
echo "WROTE $OUT"
wc -l "$OUT"
