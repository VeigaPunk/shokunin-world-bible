# JCOV2 — Coverage judge #2 (map discipline), round 90

Judged tree: `ca7f9ef1646cf3fcbe58747785a8cb2e9075ae13` (baseline `e97613c`), work commit; tree clean at start and at end.
Scope: whole-claim spot audit of map entries (R3 pledge scope, T3/T4 unresolved statement included), R9
mode-label presence in maps **and** inside excerpt files, the Spence wording/`external-only` scoping, and whether
the two note-only cross-maps are counted anywhere they should not be. Freeze-then-verify (r88-I1) applied to both
delivered checkers. This report is my only repository write; all probes ran on the delivered tree or on `/tmp`
scratch; no commit, no push, sibling repos untouched.

## Work performed

- Two 60 s dependency wait-checks (`date -Is` + `ls -la …/round-90/followup` + `git log/status`), both inside one tool
  call each: started 06:54:50 -03:00, ended 06:55:50 -03:00 (check 1 inventoried the followup directory, check 2
  the HEAD/porcelain state). At both ends the followup directory held only
  `Q1-r90-debt.json` (mtime 06:29) and HEAD was `ca7f9ef` with clean porcelain output; the H2/H3/H4/JCAL\* followup
  artifacts listed later in this same run are sibling seats landing in parallel, not inputs this seat waited on.
  No gap is left by the wait: every artifact I audit is in the delivered commit.
- Reproduced both receipts from the delivered tree, audited every mode cell in both maps, verified against the
  delivered `support_check.py` semantics (module-level probe of the parsed inline labels plus two executed negative
  controls), performed a 9-check whole-claim audit over r87 E1/R3/T3/T4/H4+`entities[2]` co-map and the two r88
  Spence comparisons, verified the delivered English passage externally against Project Gutenberg eBook 53080, and
  ran the freeze-then-verify composition for `check_bible.py` (X2+X3 on `e97613c`) and for the C2 artifacts
  (M1+M2+M3+M5 on `e97613c`).
- Baseline before-state measured directly from the commit (`git ls-tree`, `git show`), not quoted from another seat.

## Before → after measurements

### 1. Receipts on the delivered tree (the C2 support command)

```sh
cd /home/vgpnk/Projects/shokunin/lore-shokunin
python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster; echo "exit=$?"
python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster; echo "exit=$?"
sha256sum corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster/claim-excerpt-map.md corpus/fixtures/r88-m3-maya-cluster/claim-excerpt-map.md
```

Observed (tail of each run):

```text
SOURCE-SUPPORT 22/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22
RESULT PASS
exit=0
SOURCE-SUPPORT 10/10; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 10/10
RESULT PASS
exit=0
66a3c4bb2ae7fc2049227e480864661606b65a629c64cbc3ce05e14589add472  corpus/tools/support_check.py
8c1b600d28c130f998a0765ae9c4ae30d828b11fe96e3cbd763cd0cf79089b9d  corpus/fixtures/r87-myth-cluster/claim-excerpt-map.md
d314d22ec2bbba149354ef30df96f39468f8f7a54e6c3a4cf824eb9d58dad290  corpus/fixtures/r88-m3-maya-cluster/claim-excerpt-map.md
```

### 2. Baseline (before) — measured from `e97613c`

```sh
git ls-tree -r --name-only e97613c | grep -E "r87-myth-cluster|r88-m3-maya-cluster|corpus/tools"
for f in gate-witness dune-register shell-charter tide-bell-tally lowwater-hymn; do git show e97613c:corpus/fixtures/r87-myth-cluster/$f-excerpt.md | grep -c "Delivery mode"; done
git show e97613c:corpus/fixtures/r88-m3-maya-cluster/fictional-excerpts.md | grep -c "Delivery mode"
```

Observed:

```text
(no claim-excerpt-map.md in either cluster; no corpus/tools/ path)
gate-witness/dune-register/shell-charter/tide-bell-tally/lowwater-hymn excerpts: 0 Delivery-mode lines each
r88 fictional-excerpts.md: 0
```

So the after-state is strictly additive: two maps that did not exist, six excerpt files that carried no R9 label,
one checker that did not exist.

### 3. Freeze-then-verify (r88-I1) — no blocking finding

```sh
git show e97613c:corpus/fixtures/check_bible.py > $d/corpus/fixtures/check_bible.py
(cd $d && git apply -p1 …/X2-c1-nullonly.patch && git apply -p1 …/X3-c1-tickonly.patch)
sha256sum $d/corpus/fixtures/check_bible.py corpus/fixtures/check_bible.py
# C2 artifacts:
git archive --format=tar e97613c corpus/fixtures/r87-myth-cluster corpus/fixtures/r88-m3-maya-cluster corpus/fixtures/check_bible.py | tar -xf - -C $t
for p in M1-r87-map M2-r88m3-map M3-support-script M5-span-fix; do git apply --whitespace=error --unsafe-paths --directory=$t …/$p.patch; done
```

Observed:

```text
base sha (X2 loser)  : 87d7f2b503172497d7727d81a0563051e1bc5248e738b3fd8249241185fda3f4
composed X2+X3 sha   : ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
delivered sha        : ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  → FREEZE-MATCH
M1+M2+M3+M5 composition: every delivered file identical (SAME) for both maps, all six excerpt files, both cluster
READMEs, both symbolism maps, both inspiration notes, source-excerpt.md, corpus/tools/support_check.py (66a3c4bb…)
and corpus/tools/README.md. The only DIFF is corpus/fixtures/check_bible.py, which is the X2+X3 C1 change above.
```

Retraction, recorded for honesty: my first freeze attempt printed `FREEZE-MISMATCH`, caused by `/tmp` running out of
inodes mid-`tar` (partial extraction; patches then failed silently into a truncated file). The clean single-file
composition above is the real receipt; the mismatch was an environment artifact, not a delivery defect.
`/tmp` pressure is a live constraint for this wave — my scratch was removed afterwards.

### 4. R9 mode labels — maps and excerpt files

Mode-cell audit (every table with a mode column, both maps):

```text
r87: 5 declaration cells + 14 JSON-row cells + 8 hymn-row cells = 27 cells, all `verbatim` — 0 non-R9 values
r88: 3 declaration cells + 10 JSON-row cells = 13 cells, all `verbatim` — 0 non-R9 values
```

Inline labels, actually parsed by the delivered checker (module probe of `excerpt_modes`):

```text
gate-witness-excerpt.md: ['verbatim']      dune-register-excerpt.md: ['verbatim']
shell-charter-excerpt.md: ['verbatim']     tide-bell-tally-excerpt.md: ['verbatim']
lowwater-hymn-excerpt.md: ['verbatim']     r88 fictional-excerpts.md: ['verbatim']
r88 source-excerpt.md: []                  (declared in the map's `Delivery mode` column instead)
```

Two executed controls show these labels are load-bearing, not decorative:

```text
A) r87 map E1 mode flipped to `translation` in a /tmp copy:
   SOURCE-SUPPORT 21/22; …; MODES 21/22 ; FAIL: E1: delivery mode missing or mismatched ; exit=1
B) r88 map P1 mode flipped to `paraphrase` in a /tmp copy:
   FAIL P1: retelling-support-only; anchor=found; mode=paraphrase; excerpt-mode=verbatim; 12:> Tick 9: Aru carried …
   SOURCE-SUPPORT 9/9; RETELLING-SUPPORT-ONLY 1 entries (1/1 anchors); MODES 9/10 ; exit=1
```

Control A proves map/extract agreement is enforced (a row cannot simply declare a mode the excerpt contradicts);
control B proves a paraphrase row is moved out of `SOURCE-SUPPORT` and cannot raise it.

### 5. Whole-claim spot audit — 9/9 PASS (8 entries, incl. all named ones)

One command, one observed line per audited entry (fields read from the JSON, the claim text compared against the
cited excerpt line, not only against the anchor):

```text
PASS E1 claim<-line7 :: source_id=gate-witness; line7=> I am Hara, keeper of the Mother-Tide Gate.
PASS R3 pledge scope :: rel2=shellweavers--keeps_watch_with-->reed-bell; line13=> Watch clause: Under this charter's pledge, Shellweavers keep watch with the Reed Bell.; sources.json note has the pledge boundary; map line 53 keeps the qualification
PASS T3 whole claim :: tick=3; line9=> I record the single Moon-Basin Vow of Saltmonth 4 at the Mother-Tide Gate during the first low-water bell.
PASS T4 whole claim :: tick=3; line10=> I record that same single Moon-Basin Vow of Saltmonth 4 at Ash-Dune Sanctuary during the first low-water bell.
PASS T3/T4 unresolved statement :: contradiction_id=moon-basin-vow-location; both claims are place_id fields; map line 54 preserves both as unresolved
PASS H4 + entities[2] co-map :: pointer=lowwater-hymn; claim_source=lowwater-hymn; line5=> At low water we set the shell ring beside the bowl at the Mother-Tide Gate.
PASS Spence cmp #1 anchors :: source_anchor on source-excerpt.md:5; authored_anchor=fictional-excerpts.md:8; map bullet present
PASS Spence cmp #2 anchors :: source_anchor on source-excerpt.md:5; authored_anchor=fictional-excerpts.md:7; map bullet present
PASS external-only not in mode column
AUDIT 9/9 PASS
```

Notes from reading, beyond the boolean checks: R3 is honestly bounded in three places at once (the excerpt line's
`Under this charter's pledge`, `sources.json`'s "records a reciprocal pledge, not whether either faction kept it",
and map line 53) — the residual risk is the checker-semantics-free relation *type* `keeps_watch_with`, which the
map cannot fix and which the r89 SCORECARD already records as pre-existing. T3/T4 are both retained with the
`contradictions.json` pair `moon-basin-vow-location` grounding the "unresolved" statement; neither row is presented
as canon selection. E1's attribution is correct (first-person slip text; the excerpt and `sources.json` both call it
unverified).

### 6. Spence wording, external verification (not just internal consistency)

```sh
curl -sSL -o /tmp/jcov2-spence.htm https://www.gutenberg.org/files/53080/53080-h/53080-h.htm   # Project Gutenberg eBook 53080
python3  # strip tags, unescape, collapse whitespace, then substring-test both delivered clauses and locate page markers
```

Observed:

```text
clause1 "The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred
directly subsequent to that event." → verbatim match after whitespace normalization (HTML soft-wraps the line)
clause2 "He called out “Earth,” and the solid land appeared." → verbatim match, curly quotes intact, same form as delivered
page marker before clause2: [209] | after: [210]   → the sentence sits on printed p. 209, as the delivered locator says
title present: "The Myths of Mexico & Peru"; author meta: "Lewis Spence (1874–1955)"; "The Creation-Story" heading present
```

So the delivered `source-excerpt.md:5` is genuinely Spence's English prose (an elision marked `[…]` where the
Gutenberg text has the Hurakan sentence), and the map's `external-only` marker is scoped correctly: it is attached
to the *underlying K'iche primary text* ("the underlying K'iche primary text is not reproduced (`external-only`)"),
while the English prose is labelled `verbatim` — the C7 wording flag is repaired, not merely restated.

### 7. Note-only cross-maps — are they counted anywhere they should not be?

```sh
grep -rn "symbolism-clause-map\|inspiration-note" corpus/tools/support_check.py corpus/tools/README.md corpus/fixtures/check_bible.py   # exit=1, no matches
python3 - <<'PY'  # obligation recount from JSON vs map rows  (7 claims + 7 pointers + 4 relations + 4 events = 22; r88 4+4+2 = 10)
```

Observed / arithmetic:

```text
r87 JSON obligations           : 22  (entities claims 7, first_appearance 7, relations 4, timeline 4)
r87 map fact-table rows        : 22  (E1–E6, R1–R4, T1–T4 = 14 JSON rows; H1–H8 = 8 hymn readings)
r87 receipt denominators       : SOURCE-SUPPORT 22/22 and MODES 22/22 both count *rows*, i.e. 14 JSON + 8 editorial
r87 obligations with own row   : 14; prose-crosswalk only: 6 pointers (via the E rows) + entities[2].claims[0]
                                 and entities[2].first_appearance (via H4 / map line 56) = 8
r88 JSON obligations           : 10  == r88 fact-table rows 10 (P1–P4, E1–E4, T1–T2) exactly
r88 symbolism comparisons      : 2, in prose bullets (map lines 34–35) and in the separate file — not in any table,
                                 not in 10/10, not in MODES; the declaration row for source-excerpt.md:5 is inert
                                 (no fact row targets that path, so it cannot inflate the receipt)
neither symbolism-clause-map.md nor either inspiration-note.md is read by any checker (grep above; check_bible.py's
only file read is json.loads at check_bible.py:47)
```

Answer: the r88 note-only comparison is counted **nowhere** — correct. The r87 hymn cross-map is counted in exactly
one place it arguably should not be counted *as if it were JSON coverage*: 8 of the receipt's 22 slots are the
editorial H rows. The delivered map discloses this (scope line 3 "the 14 JSON facts … plus the 8 Low-Water Hymn
clauses (22 mapped rows)", the hymn section header "they are not extra JSON canon claims", and line 56's crosswalk
paragraph), so nothing is hidden — but the receipt line itself says only `SOURCE-SUPPORT 22/22`, and the numeric
coincidence with the 22 JSON obligations is exactly the C7 hazard. It remains a labeling debt in the delivered tree.

## Findings & named debt

Per-axis verdicts for the axis this seat can judge (coverage/map discipline), stated as verdicts, not scalars:

- **coverage — improved (bounded).** Before `e97613c`: no claim→excerpt map in either cluster, zero R9 labels on
  any excerpt, no support command. After `ca7f9ef`: both maps present and reproducing (22/22, 10/10, exit 0 both),
  R9 labels present in-map and inline in 5/5 r87 excerpt files and r88's authored bundle, mode agreement and the
  retelling guard demonstrably enforced (controls A/B), all 22/10 JSON obligations reachable in the map text, and
  the 9/9 whole-claim spot audit passes with the pledge scope and the unresolved T3/T4 pair preserved. Not harmed:
  no row's span, mode, or anchor fails anywhere in the delivered tree.
- **calibration — no evidence taken by this seat, no blocking finding.** The r88-I1 freeze obligation holds for both
  delivered checkers (X2+X3 → `ff9fd2aa…` = delivered; M1+M2+M3+M5 → `66a3c4bb…` = delivered); C1 internals are
  JCAL seats' lane and I do not re-adjudicate them.
- **depth — not judged by this seat** (no C3 artifact inspected beyond what the maps cite).

Named debt, with owners visible to the integrator:

1. **JCOV2-D1 (receipt labeling, r87).** `SOURCE-SUPPORT 22/22` is 14 JSON rows + 8 editorial hymn rows; only 14 of
   the 22 JSON obligations have their own row, 8 are prose-crosswalk only. Recommend either printing the split in the
   receipt (`SOURCE-SUPPORT 14/14 JSON rows; EDITORIAL 8/8`) or adding a JSON-obligation counter, before any round
   quotes `22/22` as "all 22 JSON facts validated". Carried from C7.md:203; the delivered map's disclosure does not
   remove the ambiguity in the number itself.
2. **JCOV2-D2 (stale tool note, r87).** `corpus/fixtures/r87-myth-cluster/symbolism-clause-map.md:16` says "The
   checker does not read this map or the excerpt." True for `check_bible.py` (JSON only), false for the new
   `corpus/tools/support_check.py`, which greps `lowwater-hymn-excerpt.md` for the H1–H8 anchors (verified hits on
   lines 5/6/7). Reword to name the tool (`check_bible.py`) so the delivered note is not contradicted by a
   delivered command.
3. **JCOV2-D3 (inline label asymmetry, r88).** `source-excerpt.md` carries no inline `Delivery mode` line; its mode
   is map-declared only. Benign today (no fact row targets it), but if a future row does, the inline-agreement
   branch never fires for that file. Adding the inline label would close it at no cost.
4. **JCOV2-D4 (bibliographic detail, r88).** The delivered citations give "(London: George G. Harrap & Co., 1913)".
   The Gutenberg HTML 53080 I fetched carries title and author meta but no publisher string, so the imprint is
   unverified from the cited source (the year 1913 and the book identity do check out). Low impact; record as
   unverified rather than as verified.
5. **JCOV2-D5 (pre-existing, restated).** `relations[2].type = keeps_watch_with` is semantics-free to the checker and
   can be read as performed watch outside the map. The map, the excerpt line, `sources.json`, and the r89 SCORECARD
   all preserve the pledge boundary, so this is not new harm — but it cannot be repaired inside the map.

## Handoff

- Verdict for the integrator: C2's delivered artifacts pass an independent map-discipline audit on `ca7f9ef` —
  receipts reproduce (`exit=0`, 22/22, 10/10), mode labels exist and are enforced, all audited whole claims hold,
  the Spence passage and its `external-only` scoping are confirmed against the cited external text, and the
  note-only cross-maps are confined to their correct counts (r88 fully; r87 only as the disclosed 8 editorial rows).
- Freeze-then-verify: **match** on both checkers; no blocking finding. (One earlier mismatch reading was my own
  `/tmp` inode exhaustion during extraction and is retracted in section 3.)
- Do not forward `SOURCE-SUPPORT 22/22` as a 22-JSON-fact receipt without the JCOV2-D1 qualification; consider the
  D1/D2/D3 wordings as cheap r91 integration items.
- Files: this report only (`.ufo/waves/round-90/followup/JCOV2.md`). No tracked file, sibling repo, or other seat
  artifact changed; `corpus/tools/__pycache__/` created transiently by my module probe was removed; `/tmp` scratch
  (`jcov2-*`) removed. No commit, no push.
