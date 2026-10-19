<!-- verbatim final output of L2 seat W2RoundLore.R103Planner (read-only role), persisted by L1 lore round 103, 2026-10-19 -->
<!-- L1 note: the literal vault-reference scheme string was replaced by [vault-ref-scheme] in this persisted copy so the credential sweep prints nothing; no credential was present. -->
## r103 lore measurement plan (R103Planner, read-only, nothing written)
I ran every command below once, from the lane root via the tool's `cwd` (never `cd`), on 2026-10-19 around 21:55Z. **BEFORE means base 6cec83a**, read through a base-commit twin of each command. For README and PROVINCE the same filter reads `git show 6cec83a:<file> |` instead of the file. a7, a11 and a12 use `git grep … 6cec83a --`. Every new file is absent at base (`git ls-tree -r --name-only 6cec83a -- corpus | grep -cE 'QUALITY|SOURCES|lessons/|r103-'` → 0). The worktree is already partly written, so its values are shown as **now**, not as BEFORE.
### C1 coverage (reads corpus/README.md, PROVINCE.md, corpus/knowledge/*.md; a10 also reads corpus/SOURCES.md)
| id | measures | BEFORE | AFTER | falsifier | now |
|---|---|---|---|---|---|
| a1+a2 | CM-xx rows (declared count); each of CM-a…CM-g present | 0; 0/7 | ≥15; 7/7 | <15, or any of CM-a…g absent | 19; 7 |
| a3+a4 | `## Known gaps` + `## Frontier` headings; Frontier data rows (table rows after the separator, or bullets) | 0; 0 | 2; ≥3 | <2; <3 | 2; 5 |
| a5 | CM-a/c/e rows say `governed-method` and name their r103 slug | 0 | 3 | <3 | 3 |
| a6 | Core, Frontier and Adjacent headings under a 2026-10-19 heading in PROVINCE.md | 0 | 3 | <3 | 3 |
| a7 | knowledge files carrying `coverage-row: CM-` (declared count) | 0 | 3 | ≠3 (a 4th means a non-slug file was edited) | 3 |
| a8 | slug lines 1–4 are source:/verified-at: 2026-10-19/recheck:/coverage-row: CM-x, then a `# ` title | slugs absent | 5/5 ×3 | any <5/5 | 5/5 ×3 |
| a9 | SX placeholders left after the L1 merge | absent | 0 ×3 | >0 | 11/17/7 (before merge) |
| a10 | cited S### rows that are tier A/B, `mined`, and list the entry in used-by | absent | ≥1 ×3 | 0 for any entry (fails Q10) | 0/0/0 |
| a11 | citations of `/home/` or `kaika-w1` in this round's files | 0 | 0 | >0 (fails Q09) | 4 lines |
| a12 | base negative sweeps for CM-a / CM-c / CM-e on durable surfaces (K21 terms) | 4/1/0 files | — | a hit that governs, not one noting absence, means the row was not uncovered and Q06's governed-ground branch applies | — |
### C2 calibration (reads corpus/QUALITY.md, corpus/lessons/round-103.md, LOG.md, SCORECARD.md)
| id | measures | BEFORE | AFTER | falsifier | now |
|---|---|---|---|---|---|
| b1 | Q rows (declared count) | 0 (absent) | 10 | ≠10 | 10 |
| b2 | ids are exactly Q01…Q10 | absent | exact | DIFF | exact |
| b3 | row Qn cites lessons/round-103.md#mistakes Mn | 0 | 10 | <10 (a criterion with no lesson) | 10 |
| b4 | `## Mistakes` + `## Gate`; distinct M rows | 0; 0 | 2; 10 | <2; <10 | 2; 10 |
| b5 | each LOG/SCORECARD line cited in a Q or M row is a reject, harm, erratum, blocked or FAIL record (on the line or its `##` heading) | nothing to check | prints nothing | any MISS | MISS SCORECARD.md:383 |
### C3 depth (reads corpus/SOURCES.md; the used-by check opens C1 paths; c12–c13 read the lessons file)
| id | measures | BEFORE | AFTER | falsifier | now |
|---|---|---|---|---|---|
| c0 | SOURCES.md exists | 1 (absent) | 0 | 1 | 1 |
| c1–c7 | contract v1 census, run verbatim: row count; rows without 11 columns; tier and status histograms; duplicate ids; enum and tier-inflation; mined rows with missing used-by paths | each errors (file absent) | rows ≥1 and cover every S### the entries cite; 0 malformed; keys only from {A,B,C} and {queued,mined,rejected}; the rest print nothing | any violation line | absent |
| c8 | H1 plus Registry, Paths, Search log, Leads (unopened) | absent | 5 | <5 | absent |
| c9+c10 | rows with opened ≠ 2026-10-19; rejected rows without `REJECTED: …; flip:` | absent | print nothing | any line | absent |
| c11 | ids run S001…SNNN with no gaps, in file order | 0 (passes only because empty) | 0 with c0=0 | 1 | 0, empty |
| c12+c13 | SOURCES ids match `## Gate` ids (`- S### — URL — accessed 2026-10-19 — "`); quotes over 25 words | 0; 0 (empty) | 0; 0 with c0=0 | diff exits 1; any LONG | empty |
| c14 | `[vault-ref-scheme]` or token/sig/key query strings | 0 | 0 | >0 | 0 |
### Can each claim be verified on its own?
- **C1: the counts verify alone; admission depends on C2 and C3 by design.** a1–a9 and a11–a12 never read QUALITY.md, the lessons file or SOURCES.md, and they already moved while SOURCES.md is absent (see "now"). a10 reads C3's SOURCES.md and stays 0/0/0 without it. The entries' `source:` lines hold only SX placeholders until the L1 merge (a9), so Q10 cannot pass without C3. The bar itself is C2's text. In-flight QUALITY.md Q06 says "on any ground" (x3), which is stricter than the declared Q06. No sealed receipts exist, so all three entries fail Q06 as now written. The a11 hits also fail Q09.
- **C2: verifies alone.** b1–b5 read only C2's files plus LOG.md and SCORECARD.md, which are unchanged from base (`git status --short` shows only README.md and PROVINCE.md modified). Two links remain: C2's falsifier "an admitted C1 entry fails a Q" reads C1 files, and lessons `## Gate` holds C3's per-row records. x2: Q09's own check (QUALITY.md:20) scans all of corpus/ and prints 108 on old debt; the STATE K16 count of real dead pointers is 24. Because it uses `git grep`, it also skips the new untracked entries. As written it would reject every candidate while never checking any of them, the same "rule without a backing convention" failure Q01 describes (M1).
- **C3: the census verifies alone; rule 1 and `mined` status do not.** c0–c6, c8–c11 and c14 read only SOURCES.md. The used-by check in c1–c7 opens C1 paths, so a row can be `mined` only after C1 lands; until then it must be `queued`. c12–c13 read C2's lessons file, so contract rule 1 cannot be checked without C2. c11–c13 pass trivially while the file is absent, so they only count once c0=0.
- **Order:** L1 merge (SX→S###), then a9=0, then c0–c14, then a10, then the Q bar on the entries, then h1–h7.
### No-harm battery (STATE K31), run now on the in-flight worktree: every exit is 0
- h1 check_bible r100-docket-review: `CLEAN … 0 violations`
- h2 support_check r87: `TOTAL-ROWS 22/22 … RESULT PASS`
- h3 map_obligations r100: `raw=22 mapped=22 … RESULT PASS`
- h4 dependency_freeze: 8/8 fixtures `exit=0`
- h5 discriminate_check: `DISCRIMINATION HELD`, checker sha `ff9fd2aa…` with `matches_pin=True`
- h6 boundary_doc_check: `CERTIFIED`, receipts 3/3, cases 14/14
- h7 gate inputs: 0 tracked diffs, 0 untracked files.

x4: the only corpus-level file any gate reads is knowledge/holder-assessment-boundary.md (boundary_doc_check.py); every other input is a fixture directory or tool contract. While h7 stays 0/0, nothing this round writes can reach a gate. Re-run h1–h7 after the merge.
### Problems found in the in-flight files
- **x1, self-defeating checks:** the CM-f and CM-g `verify` cells say exit 1, but this round's own text now matches them: PROVINCE.md (via its Frontier text) for CM-f, corpus/README.md (Known gaps) for CM-g, so both exit 0. Their base twins exit 1. Pin these negative sweeps to `git grep … 6cec83a --` or exclude README and PROVINCE.
- **Claim vs artifact:** the README marks CM-c and CM-e "before r103: partial", but C1 calls them uncovered. Either restate C1 as uncovered-or-partial → governed-method, or send those rows through Q06's governed-ground branch, which needs sealed receipts (there are 0, x3). Also keep a12's term set: adding `supersed`, as the CM-e entry's recheck does, gives 15 base hits (x5), all about superseded lane documents, not in-world canon.
- **b5:** M08 anchors to SCORECARD.md:383 ("…`completed` labels do not mean 32 usable reviews"), which has no record word on its line or heading. Adjudicate it or re-anchor.
- **a11:** README:92-93 cite the ART dossier ("kaika-w1 lore-art.md"), and one cell uses the ART id "S022", which will collide with lane S### ids once SOURCES.md has 22 or more rows (Q08). PROVINCE.md:33 cites `/home/…/MANIFEST.json` and lessons:3 names the kaika-w1 dossier. All break Q09's lane-root-relative rule.
- **a8:** CM-e line 2 has extra prose after `verified-at: 2026-10-19`. It passes the prefix test used here but fails a literal "exactly these four lines" reading; L1 decides which reading applies.
### Commands (exact, as run)
```sh
grep -cE '^\| CM-[a-z0-9]+ ' corpus/README.md; for x in a b c d e f g; do grep -qE "^\| CM-$x " corpus/README.md && echo y; done | wc -l   # a1; a2
grep -cE '^## (Known gaps|Frontier)$' corpus/README.md; awk '/^## Frontier$/{f=1;next} /^## /{f=0} f&&/^\|[-| :]+\|$/{s=1;next} f&&((s&&/^\| /)||/^- /){n++} END{print n+0}' corpus/README.md   # a3; a4
for p in 'a aliases-and-name-variants' 'c in-world-dating-and-uncertain-time' 'e canon-status-and-supersession'; do set -- $p; grep -E "^\| CM-$1 " corpus/README.md | grep -F '| governed-method |' | grep -cF "corpus/knowledge/r103-$2.md"; done | grep -c '^1$'   # a5
awk '/^## .*2026-10-19/{d=1} d&&/^#+ (Core|Frontier|Adjacent)$/{n++} END{print n+0}' PROVINCE.md; grep -lE '^coverage-row: CM-' corpus/knowledge/*.md | wc -l   # a6; a7
for p in 'a aliases-and-name-variants' 'c in-world-dating-and-uncertain-time' 'e canon-status-and-supersession'; do set -- $p; awk -v cm="CM-$1" 'NR==1&&/^source: /{n++} NR==2&&/^verified-at: 2026-10-19( |$)/{n++} NR==3&&/^recheck: /{n++} NR==4&&$0=="coverage-row: "cm{n++} NR>4&&!t&&NF{t=1;if(/^# /)n++} END{print cm, n+0 "/5"}' "corpus/knowledge/r103-$2.md" 2>/dev/null || echo "CM-$1 absent"; done   # a8
grep -c 'SX[ACE][0-9]' corpus/knowledge/r103-*.md   # a9
for f in corpus/knowledge/r103-*.md; do n=0; for id in $(head -n 1 "$f" | grep -oE '\bS[0-9]{3,}\b' | sort -u); do awk -F'|' -v id="$id" -v f="$f" '{i=$2;t=$5;s=$9;gsub(/[[:space:]]/,"",i);gsub(/[[:space:]]/,"",t);gsub(/[[:space:]]/,"",s)} i==id&&t~/^[AB]$/&&s=="mined"&&index($12,f){ok=1} END{exit !ok}' corpus/SOURCES.md 2>/dev/null && n=$((n+1)); done; echo "$f AB-mined=$n"; done   # a10
grep -nE '/home/|kaika-w1' corpus/README.md PROVINCE.md corpus/knowledge/r103-*.md corpus/QUALITY.md corpus/lessons/round-103.md corpus/SOURCES.md 2>/dev/null | cut -c1-60   # a11
for t in 'alias|name variant|homonym' 'calendar|relative date|uncertain date|fuzzy date|interval algebra' 'retcon|canon tier|canon-tier|canon status'; do git grep -liE "$t" 6cec83a -- corpus/knowledge SKILL.md PROVINCE.md corpus/README.md | wc -l; done   # a12
grep -cE '^\| Q[0-9]{2} ' corpus/QUALITY.md; grep -oE '^\| Q[0-9]{2} ' corpus/QUALITY.md | tr -d '| ' | diff - <(seq -f 'Q%02g' 1 10) >/dev/null && echo exact || echo DIFF   # b1; b2
for n in $(seq -w 1 10); do grep -E "^\| Q$n " corpus/QUALITY.md | grep -cE "lessons/round-103\.md#mistakes M0?${n#0}([^0-9]|$)"; done | grep -c '^1$'   # b3
grep -cE '^## (Mistakes|Gate)$' corpus/lessons/round-103.md; grep -oE '^\| M[0-9]{1,2} ' corpus/lessons/round-103.md | sort -u | wc -l   # b4
{ grep -E '^\| Q[0-9]{2} ' corpus/QUALITY.md; grep -E '^\| M[0-9]{1,2} ' corpus/lessons/round-103.md; } | grep -oE '(LOG|SCORECARD)\.md:[0-9]+' | sort -u | while IFS=: read -r f n; do awk -v n="$n" 'NR<=n&&/^## /{h=$0} NR==n{l=$0} END{exit !((h" "l) ~ /[Rr]eject|REJECT|[Hh]arm|[Ee]rrat|ERRAT|NO-GO|[Bb]lock|BLOCK|FAIL|[Pp]hantom|slip|rolled back/)}' "$f" || echo "MISS $f:$n"; done   # b5
test -f corpus/SOURCES.md; echo $?   # c0 · c1–c7 = .tower/worktrees/kaika/fleet-ledger/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:67-80, run verbatim
grep -cE '^(# SOURCES — where .* learns|## Registry|## Paths|## Search log|## Leads \(unopened\))$' corpus/SOURCES.md   # c8
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {o=$10; gsub(/[[:space:]]/,"",o); if (o!="2026-10-19") print $2, o}' corpus/SOURCES.md; awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {s=$9; gsub(/[[:space:]]/,"",s); if (s=="rejected" && $8 !~ /REJECTED: .*; flip: /) print $2}' corpus/SOURCES.md   # c9; c10
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {i=$2; gsub(/[[:space:]]/,"",i); print i}' corpus/SOURCES.md | diff - <(seq -f 'S%03g' 1 "$(grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md)") >/dev/null; echo $?   # c11
diff <(awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {i=$2; gsub(/[[:space:]]/,"",i); print i}' corpus/SOURCES.md | sort -u) <(awk '/^## Gate$/{f=1;next} /^## /{f=0} f' corpus/lessons/round-103.md | grep -E '^- S[0-9]{3,} — [^ ]+ — accessed 2026-10-19 — "' | grep -oE '^- S[0-9]{3,}' | cut -c3- | sort -u) >/dev/null; echo $?   # c12
awk '/^## Gate$/{f=1;next} /^## /{f=0} f && /^- S[0-9]+ — /' corpus/lessons/round-103.md | awk -F'"' '{if (split($2,w," ")>25) print "LONG", $0}' | wc -l; grep -nE '[vault-ref-scheme]|[?&](token|sig|signature|key|X-Amz-[A-Za-z]+)=' corpus/SOURCES.md corpus/lessons/round-103.md corpus/knowledge/r103-*.md 2>/dev/null | wc -l   # c13; c14
python3 -B corpus/fixtures/check_bible.py corpus/fixtures/r100-docket-review >/dev/null; echo "h1 $?"; python3 -B corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster >/dev/null; echo "h2 $?"; python3 -B corpus/tools/map_obligations.py corpus/fixtures/r100-docket-review >/dev/null; echo "h3 $?"; python3 -B corpus/tools/discriminate_check.py >/dev/null; echo "h5 $?"; python3 -B corpus/tools/boundary_doc_check.py >/dev/null; echo "h6 $?"
for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response r97-crossing-acknowledgment r98-clerk-filing r99-window-lapse r100-docket-review; do python3 -B corpus/tools/dependency_freeze.py corpus/fixtures/$f >/dev/null; echo "$f exit=$?"; done   # h4
git diff --name-only 6cec83a -- corpus/fixtures corpus/tools corpus/knowledge/holder-assessment-boundary.md | wc -l; git ls-files --others --exclude-standard -- corpus/fixtures corpus/tools | wc -l   # h7
grep -rliE 'spoiler|reveal order|narrative order|fabula|syuzhet' corpus/knowledge SKILL.md PROVINCE.md; git grep -l 'kotodama-lore-adjacency' -- corpus SKILL.md PROVINCE.md   # x1
git grep -ohE '\.ufo/waves/round-[0-9]+/seats/[^ )]*' -- corpus | while read -r p; do test -e "$p" || echo "DEAD:$p"; done | wc -l; grep -c 'on any ground' corpus/QUALITY.md; ls .ufo/waves/round-103/seats/ | grep -c sealed   # x2; x3
grep -lE 'holder-assessment-boundary|PROVINCE|QUALITY|SOURCES|lessons/|corpus/README' corpus/tools/*.py corpus/fixtures/check_bible.py; git grep -liE 'retcon|canon tier|canon-tier|canon status|supersed' 6cec83a -- corpus/knowledge SKILL.md PROVINCE.md corpus/README.md | wc -l   # x4; x5
```