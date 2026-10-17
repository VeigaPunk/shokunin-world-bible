# CB1 — Doc-state auditor: boundary-doc reconstruction (follow-up, round 91)

Seat: CB1 (follow-up wave). Delivered tree audited: `c2ab3d0` (`git rev-parse HEAD` =
`c2ab3d07eaa86ce58f3f9c7fdff702f4b91ea7b7`, tree clean except the untracked follow-up dir).
Target of the reconstruction: `corpus/knowledge/holder-assessment-boundary.md`, delivered sha256
`c0c59dafc32c7fdc52f30352359b2c252e7607c76010063231b8f89d223911c9`, 549 lines.

## Work performed

- **Axes:** (1) doc-state fidelity — does the delivered boundary contract describe the delivered
  checker and tree; (2) internal coherence — no duplicate/contradictory blocks, every
  cross-reference resolves; (3) reconstruction-claim accuracy — does the applied/skipped accounting
  in the commit message and the doc header match the artifact; (4) checker-freeze integrity.
- Read the delivered doc end to end, the r89-landed contract at `ca7f9ef` (630 lines, sha
  `a4b1b331…`), the mis-landed r90-closure copy at `a7c6a17` (316 lines, sha `0d42c988…`), CB1's
  r90 instruction sheet (`.ufo/waves/round-90/followup/CB1-boundary-refresh.md`, 13 fenced blocks /
  15 sections), and the delivered checker `corpus/fixtures/check_bible.py` (`ff9fd2aa…`, 428 lines).
- Method: programmatic section inventory, per-block landing matrix, normalized-text survival of every
  r89 section, line-anchor needle tests against the delivered checker, and a live replay of the doc's
  own pasted receipt block. All probes were inline python/shell; no scratch file was created
  (`df -i /tmp` reported 100 % inode use, 1708 free at start).
- No tracked file was changed; no commit, push, or sibling-repo access. Only this artifact and
  `CB1-docstate.json` were written.

## Before → after measurements

### 1. Revision chain and checker freeze

```sh
git rev-parse HEAD
sha256sum corpus/knowledge/holder-assessment-boundary.md
git show a7c6a17:corpus/knowledge/holder-assessment-boundary.md | sha256sum   # mis-landed sheet
git show ca7f9ef:corpus/knowledge/holder-assessment-boundary.md | sha256sum   # r89-landed contract
git show e97613c:corpus/knowledge/holder-assessment-boundary.md | sha256sum   # r89 closure base
sha256sum corpus/fixtures/check_bible.py
git show ca7f9ef:corpus/fixtures/check_bible.py | sha256sum
git diff --quiet ca7f9ef c2ab3d0 -- corpus/fixtures/check_bible.py; echo $?
```

Observed:

```text
HEAD=c2ab3d07eaa86ce58f3f9c7fdff702f4b91ea7b7
delivered boundary sha256: c0c59dafc32c7fdc52f30352359b2c252e7607c76010063231b8f89d223911c9  (549 lines)
r90-closure boundary sha256: 0d42c9881e1a13351ef865f6940ca6e15a717c1123056fc361ec42e346c3a60c  (316 lines)
r89-landed contract sha256: a4b1b331ba96ff5d57200517cfe1d9e4c8f6030b4fd9ec2e46f38e7fbb4b3fd2  (630 lines)
r89-landed contract @ e97613c sha256: a4b1b331ba96ff5d57200517cfe1d9e4c8f6030b4fd9ec2e46f38e7fbb4b3fd2  -
checker worktree: ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
checker at ca7f9ef: ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
checker_diff_ca7f9ef_to_delivered_exit=0
checker_diff_worktree_exit=0
```

`git diff --stat ca7f9ef c2ab3d0 -- corpus/knowledge/holder-assessment-boundary.md` →
`1 file changed, 91 insertions(+), 172 deletions(-)` (630 → 549 lines, net −81).

### 2. Heading inventory (the reconstruction lost three sections)

```sh
grep -n '^#\{1,6\} ' corpus/knowledge/holder-assessment-boundary.md
git show ca7f9ef:corpus/knowledge/holder-assessment-boundary.md | grep -n '^#\{1,6\} '
```

Observed: `ca7f9ef` has **10 H2 sections**; the delivered doc has **7**, and its H1 appears **twice**
(`:1` and `:8`).

| ca7f9ef section | delivered state |
|---|---|
| `## The contract (round-1 baseline paragraph, kept)` (:62) | heading **gone**; 71 % of its lines survive, scattered (preamble `:69-78`, `:84-134`) |
| `## First-stop causes (delivered 1b09f3f)` (:148) | present, **label stale** (`1b09f3f`; sheet D6 said `ca7f9ef`) |
| `## Decision table…` (:182) | present; contains a **duplicated, contradictory state row** (see 6) |
| `## Editor checklist` (:197) | present, intact |
| `## Precise limits of the disclosure` (:234) | heading present; **12 of 13 r89 limit bullets lost**, Commands body grafted inside (`:243-416`) |
| `## Commands (self-contained, run from the lane root)` (:319) | heading **gone**; 89 % of its lines survive relocated into Precise limits |
| `## Evidence and citations` (:497) | present; Status-split bullets merged into it |
| `## Status split` (:578) | heading **gone**; 100 % of its bullets survive under Evidence (`:499-539`) |
| `## Measured results (parent-owned slot)` (:622) | present, intact |

### 3. r90 instruction-sheet landing matrix (13 fenced blocks, 15 sections)

```sh
python3 - # normalize whitespace, test each sheet block and each section's prescribed text
```

Observed: **9 of 13 blocks landed verbatim** (blocks 3,4,5,6,7,8,10,11,12) — this matches the
commit message's "9 pasted blocks re-validated". Per-section disposition:

| sheet section | prescribed | delivered | state |
|---|---|---|---|
| D4 header + banner (`:2-10`) | replace with r90 banner | new block **ABSENT**; old r89 comment+banner still present (`:9-16`); a third r91-written comment added (`:3-6`) and the H1 duplicated | **not applied** |
| D3 revision history | replace tail from "round-89 seat X1" | new text present (`:33-39`); old tail orphaned (`:40-44`: "delivered checker at `1b09f3f` … superseded") | applied, **spliced** |
| D4 verified-at | replace with `ca7f9ef` receipt | new text present (`:51-60`); old r89 head survives (`:46-50`) and a fragment is orphaned at `:61` | applied, **spliced** |
| D5 recheck | replace 2 sentences + `1b09f3f`→`ca7f9ef` label edits | new text present (`:62-68`); the label edit **not done** (`:412` still "does not exist at `1b09f3f`") | applied, **partial** |
| D11/D12 contract item 5 | keep r88→r89 census as history, append r90 census | r90 census present (`:126-134`) but the history sentence it should follow is **deleted**, and the item-5 tail is orphaned after it (`:132-134`) | applied, **spliced** |
| D6/D7 cause-section anchors | heading label + `{raw_presence}` + Code-column + contract-item refs remap | **none applied** (heading still `1b09f3f`, `:139`; 35 stale citations below) | **not applied** |
| D1 decision-table row 2 refs | `:343-344,:349-350,:333` → `:337,:326,:343` | not applied; **the one named skip** in the doc header (`:6`) | **skipped (named)** |
| D1/D2 decision-table row 3 | **full replacement** | new row landed verbatim (`:184`) but the old row (`:179`) was **not removed** | applied as **append** |
| D2 limits bullets | 1 replacement (done `:230-242`), 1 new bullet, 6 anchor edits, ceiling label | replacement landed; **new bullet ABSENT**; anchor edits not done; the other limits bullets **lost** | applied, **partial + content loss** |
| D9 commands header + five-gate entry | `1b09f3f`→`ca7f9ef` labels | not applied (`:412-415` still `1b09f3f`); Commands heading itself lost | **not applied** |
| D11 remaining-branches paragraph | replacement | landed verbatim (`:390-404`) | applied |
| D10 in-tree inventory | replacement numbers | landed verbatim (`:469-478`) | applied |
| D8/D12 README/citations paragraph | replacement | landed verbatim (`:490-498`) but appended after the old paragraph (`:485-489`) | applied as **append** |
| D13 status split + measured-results slot | label edits + census wording | not applied (`:499-533`, `:543` still `1b09f3f`); Status split heading lost | **not applied** |
| D12 other files | README `## Round 90`, source-prefix re-anchor, SCORECARD residue | README `## Round 90` exists at `a7c6a17` (r90 closure), and `r87-probe-source-prefix/README.md:1` already carries the delivered `:343/:326/:337` anchors at `a7c6a17` | satisfied outside r91; SCORECARD residue untouched |

### 4. Content survival of the r89-landed contract (normalized text, whole-file search)

| r89 section | r89 lines | lines kept | % |
|---|---|---|---|
| preamble (:1-61) | 61 | 43 | 78 % |
| The contract (:62-147) | 86 | 50 | 71 % |
| First-stop causes (:148-181) | 34 | 29 | 100 % |
| Decision table (:182-196) | 15 | 11 | 92 % |
| Editor checklist (:197-233) | 37 | 31 | 100 % |
| **Precise limits (:234-318)** | **85** | **9** | **11 %** |
| Commands (:319-496) | 178 | 108 | 89 % (heading lost, body relocated) |
| Evidence and citations (:497-577) | 81 | 65 | 86 % |
| Status split (:578-621) | 44 | 38 | 100 % (heading lost) |
| Measured results (:622-630) | 9 | 8 | 100 % |

Lost limit bullets (absent from the whole delivered file): scope tail ("records of that item. The
stop is permanent for that run…"), one-form-one-boundary, causes-collected, cause-wording
raw-vs-rejected, emission-order, duplicated-item-id, everything-else, three-states, no-truth-claims,
ambiguous-source, chain-eligibility, measurement-ceiling. Also lost: the two opening lines of the
baseline paragraph ("Baseline `5eb9451` behavior, kept: a duplicated holder ID inside an item's
`provenance` records silently invalidates that record, permanently latches") whose tail is orphaned
at `:69-78`.

### 5. Checker line anchors: 35 unlabeled stale citations (needle test)

```sh
python3 - # for each claim, is the needle inside the cited range of corpus/fixtures/check_bible.py?
```

14 of 26 needle tests **FAIL** on the cited range; every failing needle is found exactly **+2 lines**
later, matching the r90 sheet's own remap (`:198-199`→`:200-201`, `:206-208`→`:208-210`,
`:257-260`→`:259-262`, `:275`→`:277`, `:288`→`:290`, `:313-316`→`:315-318`, `:182`→`:184` …). The 12
"PASS" results are boundary coincidences: the needle sits on the last line of the cited range while
the construct actually starts two lines later (e.g. cause row 4 cites `:215-221`; the non-dict branch
is `:217-223`).

Stale citations by region (r90 remap not applied):

| region | count | examples |
|---|---|---|
| contract items 1–4 + cause-section prose + cause table (`:84`–`:166`) | 29 | `:206-208`@84, `:275`@108, `:288`@108, `:225-233`@115, `:236-244`@118, `:198-203`@142, `:272`/`:285`/`:306`@145, whole cause-table Code column `:149-162`, `:256`+`:313-316`@166 |
| decision table (`:178-179`) | 6 | `:343-344`, `:349-350` (points **outside** the provenance block; it is the r89 tick-identity block that r90 **removed**), `:333`, plus old row-3 `:327-333`, `:334-344`, `:168-173` |
| **total unlabeled** | **35** | silently wrong against the delivered checker |
| Evidence block labeled "Checker at delivered `1b09f3f` (435 lines, sha `e2bb9639`)" | 13 | `:168-173`, `:182`, `:185-352`, `:191`, `:192-194`, `:198-203`, `:206-208`, `:212-214`, `:215-221`, `:222-248`, `:249-312`, `:313-319`, `:425-435` — internally consistent r89 history, but the dossier's "delivered" inventory should now be `ff9fd2aa`/428 lines |

### 6. Duplicate and contradictory content

```sh
grep -n 'not uniquely resolvable' corpus/knowledge/holder-assessment-boundary.md
```

- H1 duplicated at `:1` and `:8`.
- **Decision table carries the "not uniquely resolvable" state twice**: old row at `:179` (r89
  wording: "…and for ticks `{record_label}.tick: input-structural finding…holder identity is not
  uniquely resolvable: {details}…` (`:327-333`, `:334-344`, `:345-350`); `{detail}` … (`:168-173`)")
  and the r90 replacement row at `:184` ("**Tick findings are NOT qualified** … (`:323-326`)"). The
  two rows state mutually exclusive outputs and cite mutually exclusive anchors (`:345-350` is the
  block r90 deleted).
- "Rules text / README" paragraph twice: `:485-489` (r89 text) and `:490-498` (r90 text, correct
  refs `:1008-1011`, `:1012-1015`).

### 7. Splice / truncation inventory (exact delivered lines)

- `:37-44` — new r90 revision-history sentence immediately followed by the orphaned r89 tail
  ("delivered checker at `1b09f3f` (`.ufo/waves/round-89/followup/CB1.md`); the r88 contract …").
- `:46-50` — old `verified-at: RUNTIME REPLAYED … 1b09f3f by round-89 seat CB1` head survives, cut
  mid-clause ("the multi-cause joining rule, the qualified"), followed by the new `:51-60` paragraph
  and an orphaned fragment at `:61`.
- `:69-78` — the baseline-paragraph tail (baseline `:212-224/:234-237/:238-245/:246-247` refs) sits
  where the recheck paragraph's continuation should be.
- `:126-134` — the r90 census paragraph is inserted mid-sentence inside contract item 5 ("every
  existing fictional JSON byte are [Round-90 verification…] (`:82-83`, `:85-91`, `:97`). Cause
  wording distinguishes …").
- `:227-230` — the scope bullet truncates mid-clause ("at the first stop and ALL later") and is
  followed by the D2 replacement bullet.
- `:243` — orphaned tail of the Commands intro ("are pinned in `reports/round-1/current-baseline.json`):")
  followed by the grafted `sh`/output blocks (`:245-416`).
- `:412`, `:499-533`, `:543` — labels still `1b09f3f` (D9/D13 unapplied).

### 8. Live receipts on the delivered tree (the parts that are sound)

```sh
bash -c 'for case in r85-control r85-unique-break-control r85-masked-ambiguous r85-isolated-ambiguous r85-harbor-repro; do echo "=== $case ==="; python3 corpus/fixtures/check_bible.py corpus/live/runs/round-85/probe-inputs/"$case"; echo "[rc=$?]"; done'
```

Observed: 29 stdout lines, stderr empty, **byte-identical to the pasted expected block** at
delivered `:254-282` (`pasted == observed : True`). All 7 fenced blocks in the delivered doc are
byte-identical to their `ca7f9ef` originals (sha comparison of all 7: 7/7 shared hashes).

Inventory drift: `len(dirs with provenance) = 35` at the delivered tree (33 claimed "at `ca7f9ef`");
the two r91 additions `r91-c1-null-chain`, `r91-c1-tick-unresolved` carry provenance and are not
mentioned anywhere in the doc.

Cross-reference check: the doc still points readers to `"Commands"` 4× (`:47`, `:52`, `:500`,
`:546`) and `"The contract"` 2× (`:19-20` "kept verbatim in \"The contract\" below"; `:425-426` "the
baseline paragraph of \"The contract\" cites"), and the verified-at paragraph promises "All fourteen
pasted case blocks **below**" — none of those headings exist in the delivered file.

## Findings & named debt

**Verdicts (per axis, delivered tree only).**

- **Checker-freeze integrity: unchanged.** `ff9fd2aa…` at worktree, `ca7f9ef`, and delivered; both
  diffs exit 0. Corroborates the work-wave CB1 negative drift result and K1's freezer check.
- **Doc-state fidelity: harmed relative to the declared target** (`ca7f9ef` + the sheet's 14
  doc-edit sections), **improved relative to `a7c6a17`** — a contract is back at the tracked path
  and all 9 landed blocks are verbatim, but the assembly is not the prescribed document: 3 headings
  lost, 13 limit bullets lost, 2 contradictory duplicate rows, 4 splices, 35 unlabeled stale anchors.
- **Reconstruction accounting: harmed.** The delivered file shows **9 of 13 sheet blocks landed**,
  **5 prescribed items unapplied** (D4 header/banner, D6/D7 anchor remap, D1 row 2, D9 labels, D13
  labels) plus 1 absent new bullet, while the doc header names **exactly one** skipped item
  (`:3-6`: "Skipped as named debt: D1 — Decision-table row 2 code refs"). The round brief's "2 items
  named as skipped debt" is not in the artifact; K1's follow-up and JDEP3 already flag the same
  disposition gap independently.
- **Internal coherence: harmed.** See 6 and 7.

**F1 — R91-CB1-DOC-ASSEMBLY-DEFECT (named debt, exceeds the one named item).** The reconstruction is
not derivable by incremental patch: it must be re-derived from `ca7f9ef` by applying the sheet's 14
sections. Evidence: 49 stale citations, 3 lost headings, 13 lost limit bullets, 4 splice sites.

**F2 — Decision-table contradiction (highest-severity content defect).** `:179` (retired) vs `:184`
(current) for the same reference state, with mutually exclusive tick semantics. A reader of the
delivered contract gets both the r90 ruling and its retraction; `:179` also cites the deleted
`:345-350` block. The claimed "D1/D2 applied" is technically true of the *text*, false of the
*replacement*.

**F3 — Named skipped item understates real debt.** Only D1 row 2 is named; D4 header/banner, D6/D7
(35 citations), D9, D13 and the missing D2 bullet are unapplied and unnamed. Conversely, D1 row 2's
impact is real but *smaller* than the nameless ones: its three anchors (`:343-344`, `:349-350`,
`:333`) land on the unqualified first-record form, unrelated relation-loop code, and the qualified
branch's `if from_detail:` — a reader cannot see the "definite" forms the row claims.

**F4 — Evidence inventory describes the r89 checker as "delivered" (13 citations).** The block at
`:429-441` still reads "Checker at **delivered `1b09f3f`** (435 lines, sha `e2bb9639…`)" and lists
r89 numbering; the delivered checker is `ff9fd2aa`, 428 lines. Coherence risk: a verifier who
replays those anchors on the delivered tree lands two lines early.

**F5 — Lost contract text (named debt: R91-CB1-LIMITS-LOSS).** 12 of 13 "Precise limits" bullets and
the baseline paragraph's opening are gone from the file entirely (they exist only at `ca7f9ef`).
This is content regression, not a formatting issue: the limits section is the doc's boundary of
claim, and the axis-integrity states ("three states, not two", "no truth claims") are no longer
stated in the tracked contract.

**F6 — Two delivered-state claims in the surviving text are stale.** (i) "There is no `## Round 90`
section at `ca7f9ef`" (`:494`) — true of `ca7f9ef`, false of the delivered tree, because README has
carried `## Round 90` since `a7c6a17` (verified: `git show a7c6a17:corpus/fixtures/README.md` line
1016); the doc therefore understates where the r90 semantics are recorded. (ii) The in-tree
inventory (`:469-478`) says 33 provenance directories and does not mention the two r91 fixtures that
now carry provenance (measured 35 on the delivered tree).

**F7 — What is sound (no harm claimed).** The 9 landed blocks are verbatim; all 7 fenced replay
blocks are byte-identical to `ca7f9ef` and the r85 five-case block still replays byte-identically on
the delivered tree (live receipt above); the checker is frozen; `r87-probe-source-prefix/README.md`
is correctly re-anchored; README `## Round 90` exists.

**r92 recommendations (ordered).**

1. **Re-derive, do not patch:** rebuild `corpus/knowledge/holder-assessment-boundary.md` from
   `git show ca7f9ef:corpus/knowledge/holder-assessment-boundary.md` and apply the 14 sheet sections
   exactly, then re-run the sheet's own "Verified-unchanged" list (all 7 blocks byte-identical; the
   r85 replay). Do not attempt to fix the delivered file in place — the splice offsets are unknown.
2. If re-derivation is not taken: minimum repair set = delete old row `:179` (keep `:184`); delete
   the old Rules-text paragraph `:485-489`; restore the lost limit bullets + baseline head from
   `ca7f9ef`; restore the 3 headings; remove the duplicate H1 `:1`/`:8`; apply the 35+13 anchor
   remaps; apply D4/D9/D13 labels; add the D2 new bullet.
3. Amend the header debt list to name every unapplied item (D4, D6/D7, D9, D13 + the D2 new bullet),
   not just D1 row 2.
4. Land a durable verification of the reconstruction itself: a checked-in diff receipt
   (`git diff ca7f9ef <rebuilt>` reviewed against the sheet) so an integration of this kind cannot
   pass silent — the r91 wave had no seat whose write scope covered the boundary doc (CB1's work
   seat was audit-only, correctly; the defect is that the *integration step* had no second reader).
5. Consider a `corpus/knowledge/` README/index note that names which tracked doc is the "delivered"
   contract revision, since the path silently held an instruction sheet for one round.

## Handoff

- Wrote only this artifact plus `.ufo/waves/round-91/followup/CB1-docstate.json` (machine-readable
  counts). No tracked change, no commit/push, no sibling-repo access, no scratch file.
- **Parent action:** the delivered boundary doc must not be recorded as a coherent contract. Two
  options: (a) r92 re-derivation (recommended), (b) explicit debt entry naming the assembly defect +
  the F5 content loss. Either way the round record should say the reconstruction landed 9/13 blocks
  and names 1 of ≥5 unapplied items.
- **Impact statement for the C3/claim evidence:** the boundary doc is *documentation*, not the
  checker — the delivered checker behavior, the r91 discriminating fixtures, and the C9 watch
  artifact are unaffected by this audit. The harm is to doc-state fidelity and to any verifier who
  follows the doc's anchors.
- **Gaps:** the 60-second wait-checks ran against the follow-up directory only; no dependency of this
  seat's evidence on sibling follow-up artifacts exists, so their arrival or absence does not change
  any number above. I did not re-derive the corrected doc myself (out of write scope); the repair
  recipe in r92-1/2 is complete but unexecuted. I did not audit
  `corpus/knowledge/r88-sourced-inspiration-decision-table.md` (C3 landing) or the C2 support-command
  changes — other seats' scope.
- **Wait receipts (60 s checks, local `-03:00`):** `check0` 08:36:31 — 20 follow-up files present;
  `check1` 08:37:31 — 30 files (H1, H3, H5, JCAL1, P3, SE2, V2 arrived); `check2` 08:38:31 —
  42 files incl. this seat's two artifacts. Task `bash-96ybsm96`, `POLL_DONE`, exit 0.
- **Cross-seat corroboration (independent, arrived after my draft; no contradictions found):** E1
  names `R91-E1-BOUNDARY-ROW3-STALE` (`:179` vs `:184`), `-SPLICE-FRAGMENTS`, `-STALE-COUNTS`,
  `-R90-SECTION`; H1 names `R91-H1-BOUNDARY-RECONSTRUCTION-SPLICED` and `-SECTIONS-LOST`; H5 files
  F3 (D6/D7 unapplied, "36 stale sites") and F4/F5 (D13 unapplied, D2 partial, three headings
  dropped, dangling `"Commands"` refs); K1 and JDEP3 flag the one-vs-two skipped-item gap. Their
  defect sets match mine; my additions are the 13-block landing matrix, the live replay receipt, the
  survival percentages, and the split of 35 unlabeled vs 13 r89-labeled stale citations.