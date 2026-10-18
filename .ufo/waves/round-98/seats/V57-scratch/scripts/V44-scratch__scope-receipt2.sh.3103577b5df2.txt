#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
S=.ufo/waves/round-98/seats/V44-scratch
BASE=.ufo/waves/round-98/seats/V44-scratch/baseline-corpus-hashes.txt
chk() { # $1 = grep filter label
  label="$1"; filt="$2"
  grep -E "$filt" "$BASE" | sort -k2 > "$S/tmp-base.txt"
  while read -r h p; do echo "$(git hash-object "$p") $p"; done < "$S/tmp-base.txt" | sort -k2 > "$S/tmp-cur.txt"
  ch=$(diff <(cut -d' ' -f1 "$S/tmp-base.txt") <(cut -d' ' -f1 "$S/tmp-cur.txt") | grep -c '^<')
  echo "[$label] paths=$(wc -l < "$S/tmp-base.txt") changed=$ch"
  diff "$S/tmp-base.txt" "$S/tmp-cur.txt" | grep '^[<>]' | sed 's/^/    /'
}
chk "1 four-tools" 'check_bible\.py$|support_check\.py$|boundary_doc_check\.py$|discriminate_check\.py$'
chk "2 fixture-JSON" '^[0-9a-f]+ corpus/fixtures/.*\.json$'
chk "3 live-probe-JSON" '^[0-9a-f]+ corpus/live/.*\.json$'
chk "4 tool-contract-JSON" '^[0-9a-f]+ corpus/tools/.*\.json$'
chk "5 all-corpus-JSON" '^[0-9a-f]+ corpus/.*\.json$'
