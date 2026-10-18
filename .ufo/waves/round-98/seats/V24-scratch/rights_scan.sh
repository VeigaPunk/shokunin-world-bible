#!/bin/sh
# V24 r98 adjacency — rights/mechanics language scan. Usage: rights_scan.sh <outfile>
# Run from lane repo root AFTER freeze. Scans all r98 new bytes + round diffs.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 1
OUT="${1:-/tmp/v24-rights.txt}"
BASE=9a3d648
NEW_FILES="corpus/fixtures/r98-clerk-filing/README.md corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md corpus/fixtures/r98-clerk-filing/contradictions.json corpus/fixtures/r98-clerk-filing/entities.json corpus/fixtures/r98-clerk-filing/fictional-excerpts.md corpus/fixtures/r98-clerk-filing/inspiration-note.md corpus/fixtures/r98-clerk-filing/relations.json corpus/fixtures/r98-clerk-filing/source-excerpt.md corpus/fixtures/r98-clerk-filing/sources.json corpus/fixtures/r98-clerk-filing/timeline.json corpus/knowledge/r98-clerk-scope-note.md"
{
  echo "== A. mechanics/grant phrase scan on new bytes =="
  grep -n -i -E "mechanic|gameplay|ruleset|damage|stats|balancing|hit ?point|dice|combat|level.?up|public domain|fair use|free to (use|reuse)|may be (used|reproduced)" $NEW_FILES
  echo "(rc=$?)"
  echo
  echo "== B. mechanics/grant phrase scan on round diffs (tools + r95 map repair + r95/r96 addenda) =="
  git diff $BASE -- corpus/tools/ corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md corpus/knowledge/r95-aftermath-scope-note.md corpus/knowledge/r96-response-scope-note.md | grep -n -i -E "^[+-].*(mechanic|gameplay|ruleset|damage|stats|balancing|public domain|fair use|free to (use|reuse)|may be (used|reproduced))"
  echo "(rc=$?)"
  echo
  echo "== C. broader rights/permission/canon/training hits in new bytes =="
  grep -n -i -E "rights|licen[cs]e|copyright|permission|canon|training|attribut" $NEW_FILES
  echo "(rc=$?)"
  echo
  echo "== D. adjacency-string scan (absolute paths / escapes / sibling lanes) in new bytes =="
  grep -rn -E "/home/|\\.\\./|/tmp/" $NEW_FILES
  echo "(rc=$?)"
  echo
  echo "== E. sibling-lane names in round diffs =="
  git diff $BASE -- corpus/ | grep -n -i -E "^[+-].*(kotodama|game-dev|art-east|kengaku|mado|tabi|sibling|/home/|\\.\\./)"
  echo "(rc=$?)"
  echo
  echo "== F. external-name scan in r98 JSON + knowledge note =="
  grep -n -i -E "Spence|Kojiki|Chamberlain|Gutenberg|ETCSL|Inana|Ovid|Maya|Kiche|K'iche" corpus/fixtures/r98-clerk-filing/*.json corpus/knowledge/r98-clerk-scope-note.md
  echo "(rc=$?)"
  echo
  echo "== G. byte-copy integrity: r98 preserving copy vs baseline r97 =="
  for f in README.md claim-excerpt-map.md contradictions.json entities.json fictional-excerpts.md inspiration-note.md relations.json source-excerpt.md sources.json timeline.json; do
    a=$(sha256sum corpus/fixtures/r98-clerk-filing/$f | cut -c1-12)
    b=$(git show $BASE:corpus/fixtures/r97-crossing-acknowledgment/$f | sha256sum | cut -c1-12)
    [ "$a" = "$b" ] && echo "SAME  $f $a" || echo "DIFF  $f r98=$a r97=$b"
  done
  echo
  echo "== H. fictional-excerpts prefix check (r97 3410B prefix of r98?) =="
  git show $BASE:corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md > /tmp/v24-r97-fx.md
  wc -c < /tmp/v24-r97-fx.md
  wc -c < corpus/fixtures/r98-clerk-filing/fictional-excerpts.md
  head -c 3410 corpus/fixtures/r98-clerk-filing/fictional-excerpts.md | cmp - /tmp/v24-r97-fx.md && echo "PREFIX-IDENTICAL" || echo "PREFIX-DIFFERS"
} > "$OUT" 2>&1
cat "$OUT"
