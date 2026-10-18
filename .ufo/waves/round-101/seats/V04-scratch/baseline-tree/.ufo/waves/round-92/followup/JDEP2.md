# JDEP2 — doc attacker (r92 follow-up, world-bible lane)

Judged surface: the COMMITTED tree `c4d4823` only. No commit, no push. The only
repo write is this file. Scratch was a single `/tmp` script (removed); note: a
pre-existing `/tmp/jdep2/` directory (timestamps 04:18–04:19, contents `probes/`,
`waitchecks.log` — not this seat's, predating the wave) was removed during
cleanup before I recognized it was not mine; scratch-only, no repo content was
involved.

## Work performed

Axes: **pin/provenance honesty**, **anchor resolution**, **pasted-block replay
parity**, **certification-chain integrity** — attacking the re-derived boundary
doc (`corpus/knowledge/holder-assessment-boundary.md`, 671 lines, sha256
`8e1fe877…`) for what a receipts-only verifier (JDEP1-style) would miss.

Performed, all read-only against `c4d4823`:

1. Freeze identity + doc identity + checker identity.
2. Lineage test: replay seat D2's patch
   (`.ufo/waves/round-92/patches/D2-boundary-doc.md`) onto the r91 doc
   (`git show 396c568:…`) and byte-compare with the landed doc.
3. Extracted the doc's three `sh`→`text` block pairs programmatically and
   replayed them; compared byte-for-byte; also replayed the two direction
   fixtures and the helper-absence claim.
4. Wrote both anchor inventories out of the doc's Evidence section (the new
   ca7f9ef bullet and the orphan fragment that follows it) and resolved every
   span against the delivered checker `corpus/fixtures/check_bible.py`
   (428 lines, sha256 `ff9fd2aa…`).
5. Stale-pin sweep: `e2bb9639`, `1b09f3f`, `2b48ca7`, `ca7f9ef` occurrences with
   line numbers and tense analysis.
6. Provenance-gap grep for any r92 revision mention in the doc.
7. `corpus/tools/support_check.py` on the three C2 fixtures at HEAD.
8. Read `patches/T1-certification.json`, `R1.md`, `CB.md`, `S1.md`, `D1.md`,
   `D2.md`, `E1-edges.md`, `patches/Q1-r92-debt.json` for attribution (work-wave
   artifacts, committed).
9. Wrapper checks: fence count, heading set, provenance fixture census.

## Before → after measurements

**(1) Judgment surface identity.** Command
`git log --oneline -3 && git status --porcelain && sha256sum corpus/fixtures/check_bible.py && git show --stat c4d4823 | tail -3`:

```text
c4d4823 lore r92: C1 anchor-based doc re-derivation + residual edges, …
396c568 lore r91: closure …
c2ab3d0 lore r91: C3 R8/R10 r91 edge decisions …
<clean>
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

Checker unchanged ✓; doc at HEAD: 671 lines, sha256 `8e1fe877…` (header claim
"checker ff9fd2aa" is true of the file).

**(2) Lineage: the landed doc IS the r91 doc + D2's patch, byte-for-byte.**
Command: `git show 396c568:… > old.md; cp old.md new.md; patch -p0
--input …/D2-boundary-doc.md new.md; cmp new.md <HEAD doc>`:

```text
patch_rc=0
LANDED_EQ_R91D2=PASS
```

Base = the 549-line r91 doc `c0c59daf` (the version whose own certification
baseline failed gates C/D/E in T1's run). So the r92 artifact is a patch of the
r91 (uncertifiable) document, not a fresh 630-line `e97613c`-derived file.

**(3) Pasted-block replay: 14/14 byte-identical at HEAD.** Command: extracted
the 3 command blocks and ran them from the lane root, diffing against the
following `text` block:

```text
fences=7 sh-replay-pairs=3
block1 doc_line=346 out_line=355 cases=5 byte_equal=True rc=0 stderr_empty=True
block2 doc_line=400 out_line=406 cases=6 byte_equal=True rc=0 stderr_empty=True
block3 doc_line=456 out_line=462 cases=3 byte_equal=True rc=0 stderr_empty=True
ALL_BLOCKS_BYTE_EQUAL= True
direction r87-masked-break-from-ambiguous: rc=1 violations=5 stop_fields=['from_holder'] stop_origin=['entities[3].provenance[0]'] disclosed_records=[0,1,2]
direction r87-masked-break-to-ambiguous:   rc=1 violations=5 stop_fields=['to_holder']   stop_origin=['entities[3].provenance[0]'] disclosed_records=[0,1,2]
measure_helper: exit=2 | python3: can't open file '…/measure_holder_disclosure.py': [Errno 2] No such file or directory
```

Behavioral claims in the doc hold: 14 cases, both direction fixtures, helper
absence, empty stderr.

**(4) Anchor audit of the delivered checker (ff9fd2aa, 428 lines).**
The NEW bullet (doc `534-544`, "Checker at the r90-delivered tree `ca7f9ef`")
— **21/21 spans resolve** to the intended content (`:38-39`, `:72-76`,
`:82-83`, `:85-91`, `:93`, `:97`, `:164-166`, `:168-175`, `:184`, `:187-345`,
`:193`, `:194-196`, `:200-205`, `:208-210`, `:214-216`, `:217-223`,
`:224-250`, `:251-314`, `:315-321`, `:322-345`, `:418-428` all verified line by
line).

The ORPHAN fragment that follows it (doc `545-556`, headed only by the dangling
fragment `lines, sha256 e2bb9639…):`) — **13 of its 14 spans are wrong in the
delivered checker; 1 is a near-miss**:

| claimed (orphan) | delivered content at that span | intended content is at |
|---|---|---|
| `:182` relation-ambiguity precedent | `…endpoint: dangling entity…` append | `:184` |
| `:185-352` provenance loop | `:185` = `source(row['source_id'], …)` | loop `:187-345` |
| `:191` only-valid-on-item | `:191` = `records = item['provenance']` | `:193` |
| `:192-194` expected array + continue | `:192-194` = kind test / only-valid / `continue` | `:194-196` |
| `:198-203` item-level first-stop tests | `:198` = `previous_tick = None` | `:200-205` |
| `:206-208` disclosure template | `:206` = `chain_has_ambiguous_source = False` | `:208-210` |
| `:212-214` top-of-loop emission | `:212` = `for i, record…` | `:214-216` |
| `:215-221` non-dict branch | `:215` = `if disclosure_emitted:` | `:217-223` |
| `:222-248` key-set branch | shifted by 2 | `:224-250` |
| `:249-312` field validation/cause collection | shifted by 2 | `:251-314` |
| `:313-319` latch | shifted by 2 | `:315-321` |
| `:320-352` comparison gate + FN-2 | shifted / overshoots loop end 345 | `:322-345` |
| `:425-435` CLI/exit | file is 428 lines; `:429-435` do not exist | `:418-428` |
| `:168-173` holder_identity_detail | function header (delivered fn is `:168-175`) | near-miss |

The fragment is a *correct anchor inventory for the r89 checker*
(`git show 1b09f3f:…` sha256 `e2bb9639…`, 435 lines: `:182` precedent, loop
`:185-352`, CLI `:425-435` all verified there) — but its label was cut by the
splice. It originated verbatim from the e97613c/ca7f9ef-era bullet
`- Checker at delivered \`1b09f3f\` (…, 435 lines, sha256 \`e2bb9639…\`):` and
lost that line. So every one of its post-176 spans is off by +2 or out of file
**in the delivered checker**, i.e. an unlabeled stale pin presented as current.

**(5) Stale pins claimed as current (line numbers in the landed doc).**

- `:3-9` header: `Refreshed at round-90 closure …` / `Landed at round-90
  closure (replacing the r89-closure version)` — the document's own provenance
  block is r90; there is no r92 re-derivation provenance anywhere in the doc.
- `:83` `The delivered checker (\`1b09f3f\`) replaces the holder-only latch…`
  — present tense in "The contract"; the delivered checker is `ff9fd2aa` at
  `ca7f9ef`/HEAD (and its behavior differs: null guard, integer-only tick).
- `:161` heading `## First-stop causes (delivered \`ca7f9ef\`)` — r90 tree pinned
  as "delivered" at r92.
- `:258` `notice at \`1b09f3f\`.` — same stale framing.
- `:666` `No five-gate score is recorded for the delivered tree \`ca7f9ef\`` —
  same.
- `2b48ca7`: 3 occurrences (`:22`, `:36`, `:650`), all correctly historical
  (r87 evidence, superseded) — no 2b48ca7-as-current leftover.
- `1b09f3f`: 8 occurrences (`:27`, `:83`, `:129`, `:258`, `:580`, `:615`,
  `:625`, `:653`); `:83` and `:258` are the current-tense stale ones; `:615` is
  the orphan tail (see F3); the rest are properly historical.

**(6) Duplicate/contradictory region tails (r91-splice leftovers).**

- `:591-596` repeats the tail of the preceding bullet: the fixture list
  `r87-probe-shape-ambiguous, r88-mixed-stop, …` + `r7-item-ambiguous is
  ambiguous SOURCE only; r61-* …` + `Measured by …§M7` appears twice (`:581-588`
  and `:591-596`).
- `:615-619` repeats the `The r87 decision table … treat it as history` tail
  (`:612-614` and `:617-619`) and leaves the dangling fragment `\`## Round 89\`
  section at \`1b09f3f\`, so the r89 amendments … are stated only here.` — which
  contradicts `:610` (`The README carries \`## Round 88\` (:1008-1011) and
  \`## Round 89\` (:1012-1015) sections`; verified at HEAD: Round 88 at 1008,
  Round 89 at 1012, Round 90 at 1016, Round 92 at 1020).

D2's own report says it "removed two stale partial paragraphs left by the r91
splice" — it removed two; these two plus the orphan fragment survived.

**(7) r92 provenance gap.** `grep -n "round-92\|Round 92\|r92\|c4d4823"` on the
landed doc → **no hits**; the only `e97613c` mention is one clause at `:634`
(about the r91 fixtures' README replay). The doc's Status split and Measured
results slot (`:623-671`) have no r92 row: "delivered trees" stop at
`ca7f9ef`, and the pasted-block parity is still attributed to r90.

**(8) C2 fixtures at HEAD (support command, committed state).** Command
`python3 corpus/tools/support_check.py corpus/fixtures/<f>` ×3:

```text
r87-myth-cluster:          RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 8; TOTAL-ROWS 22 | RESULT PASS | exit=0
r88-m3-maya-cluster:       RECEIPT JSON-FACTS 10; EDITORIAL-ROWS 2; TOTAL-ROWS 12 | RESULT PASS | exit=0
r89-inspiration-paraphrase: RECEIPT JSON-FACTS 1; EDITORIAL-ROWS 0; TOTAL-ROWS 1 | RESULT PASS | exit=0
```

The unreferenced-declaration WARN is closed on the committed tree ✓ (SF1 had
only verified the worktree).

**(9) Certification chain.** `patches/T1-certification.json` at HEAD says:

```text
"overall": "FAIL",
"candidate_selection": {"status": "FAIL",
  "reason": "No selected, integrated round-92 document is present at the required
   target. The tracked target remains the r91 baseline. …"},
"B_candidate_receipt_replay": {"status": "FAIL",
  "evidence": "… Baseline-only control replay passed 3/3 receipt blocks and 14/14
   cases with byte-identical stdout, expected exit codes, and empty stderr; this is
   not a candidate pass."},
baseline_control.document sha c0c59daf… (549 lines); gates C/D/E FAIL.
```

The landing commit message says `certified by T1: 3/3 receipts, 14/14 replay
cases` — those numbers are exactly T1's **baseline control**, which T1 itself
labels "not a candidate pass". No T1 certificate exists for the landed artifact
(T1 could not see the integration; Q1's ledger also records "no T1
certification … arrived by the bounded wait"). R1 `:67` and `:99` explicitly
warned: `D2's patch must not be used unchanged: its current-checker evidence is
followed by an orphan \`lines, sha256 e2bb9639…\` fragment from the old checker
inventory` / `Do not … integrate D2's orphan fragment.` The commit says
`seat D2's candidate applied directly`.

**(10) Wrapper checks.** Fences: 14 (even). Headings: 1 H1 + 10 unique H2
("exactly one heading set" ✓). Instruction markers (`instruction sheet`,
`Skipped as named debt`) absent ✓. Provenance-fixture census at HEAD: 166
fixture dirs, 35 carrying `provenance` (doc's 33 is r90-scoped; the 2 r91
fixtures are the delta).

**(11) Adjacent landed defect (residual edges, different file).**
`corpus/knowledge/r88-sourced-inspiration-decision-table.md:40` begins
`**Failed-gate disposition (clarified r92):** **Failed-gate disposition
(clarified r92):** **Owner:** …` — the label is doubled in the committed line
(the c4d4823 diff adds it doubled); `patches/E1-edges.md:11` has it once. The
R9 manual-gate and receipt-boundary wording landed correctly (`:42`, `:44`,
`:46`).

## Findings & named debt

- **JDEP2-F1 (blocks the C1 claim as stated): the R1-rejected D2 splice is the
  landed doc.** The evidence section contains an unlabeled r89 anchor inventory
  (doc `545-556`) whose spans resolve to wrong content in the delivered checker
  (13/14 wrong, 1 near-miss — table in (4)). "Every code anchor resolves" is
  false for the committed tree; R1 predicted this exact defect and the
  integration applied D2 unchanged anyway.
- **JDEP2-F2: stale pins claimed as current** — doc `:3-9` (r90 provenance),
  `:83` and `:258` (`1b09f3f` as "delivered"), `:161` and `:666` (`ca7f9ef` as
  "delivered"). No r92 pin exists anywhere. Plus one stale span in the limits
  prose the Evidence-bullet audit does not cover: doc `:330`
  `the three conditions … are now named first stops (\`:198-203\`)` — the
  delivered item-level first-stop tests are `:200-205` (verified; the same span
  is given correctly in the Evidence bullet at doc `:539`). This matches
  JDEP1's single delivered-context stale site (its gate (b), `:330`).
- **JDEP2-F3: duplicate/contradictory tails** — `:591-596` and `:615-619`
  (the latter contradicts `:610`). Two of D2's four splice leftovers were
  reported removed; two tails plus the orphan remain.
- **JDEP2-F4: certification gap.** The commit's T1 citation is the baseline
  control, not a certificate; the landed artifact has never passed the wave's
  own gates (T1 gates C/D/E-style checks would still trip on F1/F2/F3), and
  Q1's ledger does not log the splice (`grep orphan|splice|e2bb9639` on
  `patches/Q1-r92-debt.json` → no hits). Unlogged debt.
- **JDEP2-F5: D9/D13 skipped-region impact (as used by the r92 wave; note the
  r90 refresh's own D9 is instead "Commands header + five-gate entry", which
  *is* applied — the drift-id usage mismatch is recorded in S1 `:89`).**
  D9 = the delivered-checker evidence paragraph, skipped for lack of a
  replacement payload → the splice survived with two anchor bases in one list
  and no revision label. D13 = status split + measured-results, whose payload
  was r90-scoped → the doc's status/measurement sections pin `ca7f9ef` and
  carry no r92 receipt. Net: the document reads as an r90 artifact wearing
  r92 content edits.
- **JDEP2-F6 (adjacent, decision table):** doubled "clarified r92" label at
  `r88-sourced-inspiration-decision-table.md:40` (one-line fix).
- **Not a defect:** behavioral content (14/14 replay, direction fixtures,
  helper absence, C2 support receipts, exactly-one heading set, no instruction
  markers, even fence parity). The r91 "doc harm" was real and the behavioral
  repair landed; the provenance/accounting layer did not.

Not verified by this seat (gaps): the full 166-dir tuple census and the
33/13 provenance inventory numbers (adjacent receipts exist; my scope was the
doc); the claim at `:634` about the r91 fixtures' README replay; whether any
later reader follows the orphan anchors.

## Handoff

For the C1 ruling: the boundary doc's **behavioral** claims are verified on the
committed tree (14/14 blocks byte-identical, direction fixtures, helper
absence, C2 receipts PASS), but the artifact **fails its stated re-derivation/
certification claim** on provenance grounds: it is byte-equal to `r91-doc +
D2-patch` (patch rc=0, `cmp` PASS), carries the exact splice R1 said not to
ship, keeps five stale-as-current pins, and no T1 certificate exists for it
(T1's cited numbers are its baseline control, `overall: FAIL`). Minimal
repairs: delete doc `545-556` (orphan), `591-596`, `615-619`; relabel `:83`,
`:258` (`1b09f3f`→r90-era history) and `:161`, `:666` (`ca7f9ef`→r90-scoped
pin); add one r92 provenance line (header or Status) recording the anchor-based
re-derivation from `e97613c` + CB1 r90 instructions and this wave's 14/14
replay; fix the doubled label at decision-table `:40`; and either run the
certification gates against the landed doc or record the certification gap as
named debt. No commit was made; HEAD remains `c4d4823`, checker and doc bytes
unchanged by this seat — my only write is `.ufo/waves/round-92/followup/JDEP2.md`
(the `followup/` directory now also holds the sibling seats' reports —
JDEP1/JDEP4/H*/JCAL*/JCOV*/V2 etc.).

Convergence note (added after sibling landings): JDEP1 (independent certifier,
`followup/JDEP1-certification.json`) ruled the same target **FAIL — blocking on
gate (b): anchor resolution**, with the same orphan tail (`doc:545-556`, 14/21
sites mismatching) and the same stale `:198-203` span at `:330`; JDEP1 also
confirms gate (a) PASS 14/14 and gate (c) PASS, and states the r92 claim is
"not … as to certification". My measurements extend that ruling with the exact
lineage equality (`r91-doc + D2-patch`), the R1 warning trail, the T1
baseline-control conflation, and the D9/D13 skipped-region impact. No
contradiction between the two seats; the repair list above is the union of the
mechanical fixes.