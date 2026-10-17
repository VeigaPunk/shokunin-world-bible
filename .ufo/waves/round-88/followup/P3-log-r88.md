# P3 — LOG r88 entry proposal

Seat P3 (round-88 follow-up wave, world-bible lane). Judged tree:
`lore-shokunin` at `2ea9ef13a928475b13fd578740ea521bed4bd649` (`2ea9ef1`),
baseline `dfd1fbc`. Tree clean at judgement start (`git status --porcelain` →
only `?? .ufo/waves/round-88/followup/`, i.e. the judging wave's own untracked
directory). Every number below is either my own replay on the delivered tree or
is attributed in-line to the follow-up seat that produced it. Scratch lives
under `/tmp/p3/`; this file and the sibling follow-up artifacts are the only
round-88-followup writes.

Deliverable: an append-ready `LOG.md` round-88 entry (under **Handoff** below),
plus the motivating evidence, measurements, and honest debt that entry must
carry. This is a proposal for the integrating owner; it is not appended here.

## Work performed

- Confirmed the tree under judgement: `git log --oneline -3` → HEAD `2ea9ef1`
  on top of `dfd1fbc`; `git status --porcelain` clean except the follow-up dir.
  Read the work commit's full file list (`git show --stat 2ea9ef1` → 103 files,
  9292 insertions, 25 deletions; 37 seat reports under `.ufo/waves/round-88/`).
- **Own census of the delivered tree.** Built `/tmp/p3/census2.py`, which runs
  `python3 -I corpus/fixtures/check_bible.py corpus/fixtures/<dir>` from the
  repo root — the *same relative-path invocation* as the baseline census — over
  every direct fixture directory, recording exit, stdout SHA-256, violation
  count, and stderr. Compared tuple-for-tuple against the wave's baseline
  artifact `patches/B1-tuples.json`.
- **Method trap found and corrected.** My first harness passed *absolute*
  fixture paths. Five fixtures (`r5-missing-file`, `r62-missing`,
  `r67-claim-source-unavailable-{control,empty,whitespace}`) embed the fixture
  path in their violation text, so the absolute-path run produced five spurious
  hash "changes" and a false `changed=14`. Re-run with the baseline's relative
  invocation → `changed=9`, matching the claim exactly. No delivered-tree claim
  is affected; the trap is recorded as a process note for future censuses.
- **C2/C3 verification on the delivered tree:** replayed both landed clusters;
  verified the OBS-1 repair mechanically with fixed-string anchor searches
  (8/8 clause anchors); verified the Maya cluster's cited clauses resolve in its
  delivered excerpt; verified the tick-9 pair is a distinct-actor/distinct-place
  occupied-slot near-miss, not a double-booking; verified the reference-ledger
  change is a pure append (`git diff --numstat` → `3 2`) with all three prior
  rows byte-identical.
- **Boundary-doc drift, independently measured.** Grepped the delivered checker
  for the two r87 disclosure strings and replayed the five recorded r85 probe
  inputs on the delivered checker, then compared the observed counts against the
  counts the two tracked knowledge docs assert.
- **Read the follow-up wave's delivered judge reports** (present at draft time,
  03:15): `JCAL1-delta.json`, `JCAL3-receipts.json`, `JCAL5-delta.json`,
  `H2-delta.json`, `JCOV3-probes.json`, `JCOV5.md`, `JDEP1.md`, `JDEP2.md`,
  `JDEP3.md` + `JDEP3-probes.json`, `JDEP4.md` + `JDEP4-drift.json`,
  `JDEP5-receipts.json`, `V2.md`, `K1.md`, `P2-scorecard-r88.md`,
  `P4-shonen.md`. No L1 verdict artifact existed at draft time.
- Two 60-second wait-checks on `followup/` (log `/tmp/P3-wait.log`): the first
  found `JDEP2.md` + `V2.md`; the second found the full roster above. Judgement
  proceeded on what existed; nothing in my verdicts depends on an absent seat.

## Before → after measurements

### C1 — delivered census and delta (my own replay)

```sh
python3 /tmp/p3/census2.py     # relative-path invocation, cwd = repo root
```

```text
fixture_count=149 exit_counts={1: 118, 0: 31} total_violations=367 stderr_nonempty=0
changed=9 new=4 gone=0 exit_changes=0
CHG r61-independent-empty 17->18 exit 1->1
CHG r61-independent-unavailable 6->7 exit 1->1
CHG r87-masked-break-from-ambiguous 6->5 exit 1->1
CHG r87-masked-break-to-ambiguous 6->5 exit 1->1
CHG r87-probe-entry-shape 2->8 exit 1->1
CHG r87-probe-multi-invalid 6->5 exit 1->1
CHG r87-probe-nonitem-kinds 8->9 exit 1->1
CHG r87-probe-record-and-chain 34->46 exit 1->1
CHG r87-probe-shape-ambiguous 2->5 exit 1->1
NEW ['r88-m3-maya-cluster', 'r88-mixed-stop', 'r88-nonholder-stop', 'r88-shape-ambiguous-armed']
gone []
```

Baseline for the same 145 directories: 30 clean / 115 violations, 331 violation
lines, 0 stderr cases (`patches/B1-tuples.json`, independently regenerated
byte-exact by `JCAL1`). Delivered over those 145: 352 violation lines. The four
new fixtures contribute 0 + 6 + 4 + 5 = 15 lines → 367. Delivered checker:
`corpus/fixtures/check_bible.py`, SHA-256
`dcacffd6981e1af5f60b31bed20c6eccce25970444088e4ee2e30e3249411911`, 395 lines
(356 at `2b48ca7`); `git diff dfd1fbc 2ea9ef1 -- corpus/fixtures/check_bible.py`
→ +59/−20.

Disclosure semantics on the delivered tree: one template,
`{record_label}: provenance continuity and tick-order comparisons remain
unassessed (input-structural finding, not sourced-canon); first stop: {cause} at
{origin_label}`, emitted for **every** record at or after the first stopping
condition, whatever that condition is. The r87 holder-only latch and its two
notice strings are gone.

### C1 — fixture-level expectations (sibling seats, cross-checked)

- `V2` verified all three r88 fixture READMEs line-by-line against the delivered
  checker and showed each fixture discriminates (baseline checker on the same
  fixture files produces the pre-fix behavior). Its one wording nit: the phrase
  "otherwise applicable first-record chain break" in
  `r88-shape-ambiguous-armed/README.md` is a hypothetical about an unassessed
  chain, not an observable in either checker version.
- `JCAL1` invariant checks on the delivered tree: 47/47 disclosure lines match
  the exact grammar; 0 legacy-grammar survivors; 17 stop groups, each with a
  single origin and single cause; 0 violations of "every provenance record
  at/after ANY stop discloses"; qualifier present on all.
- `JCAL1` classification of the 9 changed tuples: 26 added disclosures, 13
  reworded disclosures, 1 field finding, 9 count-footers, 19 removed legacy
  disclosure lines, 0 `OTHER`.
- `SE2` (phase-2 sentinel, ran last on the delivered tree): independent
  B1-template recomputation → `unchanged=136 changed=9`; each changed fixture
  re-run twice with no nondeterminism; live probes of all four stop fixtures;
  write-scope sentinel (HEAD, reflog, `git status`, follow-up file naming,
  fleet-report location, sibling-repo scan, `/tmp` scan) → **no rule
  violations found**.

### C2 — second cluster and OBS-1 repair (my own replay)

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-m3-maya-cluster   # CLEAN, exit 0
python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster      # CLEAN, exit 0
```

- Census: fixture dirs 145 → 149; files named `inspiration-note.md` 1 → 2.
- OBS-1 repair (delivered-text option, not the `gate-witness` repoint): the r87
  hymn excerpt now reads `… beside the bowl at the Mother-Tide Gate.`; the
  attributed claim in `r87-myth-cluster/entities.json:33` now reads "The
  Low-Water Hymn places the shell ring and bowl at the Mother-Tide Gate." All
  eight clause anchors in `symbolism-clause-map.md` resolve exactly once in the
  excerpt (`grep -cF` per anchor → 1 1 1 1 1 1 1 1). The cluster's `source_id`
  is unchanged (`lowwater-hymn`), so the repair is delivered-text support, not a
  metadata repoint.
- Maya cluster: 10 files; two in-world source records (`veil-verse`,
  `paired-clock`); the cited Spence sentence's clauses resolve in the delivered
  `source-excerpt.md` (`He called out` 1, `Earth` 1, `the solid land appeared` 1
  — and the full second clause `and the solid land appeared.` matches exactly
  once); the passage-level locator is `printed p. 209`, stated in the note, the
  excerpt, and the clause map; `contradictions.json` is `[]`; the two register
  events share tick 9 with distinct actors (`aru`/`evin`) and distinct places
  (`quiet-rise`/`salt-court`), i.e. an occupied-slot near-miss.
- One literal caveat: the clause map quotes `He called out ‘Earth,’` (inner
  single quotes) while the excerpt has `He called out “Earth,”` (inner double
  quotes), so a fixed-string search for the map's *full* quoted clause returns 0
  while the excerpt's own wording returns 1. This is the M3 punctuation issue
  T1/D2 flagged in the work wave; the semantic match is exact and the two
  indexed clauses both sit in the single delivered passage.

### C3 — decision table and ledger row (my own replay)

- `corpus/knowledge/r88-sourced-inspiration-decision-table.md` — 19 lines, 7
  decision rows × 6 columns with three distinct citation columns (attribution /
  rights status / AI-training permission), plus the R1B scope note prepended as
  an HTML comment (`JDEP1` confirmed the table body is byte-identical to
  `patches/D1-table.md` except those two prepended lines). Its closing claim —
  that the checker never reads prose — is true: the checker loads JSON only.
- `corpus/knowledge/reference-ledger.md` — `git diff --numstat dfd1fbc..2ea9ef1`
  → `3 2`; row-only diff → `5a6` (pure append); the three prior data rows are
  byte-identical (`JDEP2` md5 receipts); the table now has 4 data rows × 4
  populated columns; heading broadened from "Real-world method references" to
  "Real-world references" with the "(not in-world canon)" boundary retained.
- `seed.md:26-29` (the `## Sourced inspiration` rule: three distinct questions,
  separate from in-world canon) is the cited authority and is satisfied.

### Depth drift — the one harm I measured myself

```sh
grep -c "unassessed at this and all later records because holder identity is ambiguous" corpus/fixtures/check_bible.py   # 0
grep -c "unassessed because ambiguous holder identity" corpus/fixtures/check_bible.py                                   # 0
for case in r85-control r85-unique-break-control r85-masked-ambiguous r85-isolated-ambiguous r85-harbor-repro; do
  python3 corpus/fixtures/check_bible.py corpus/live/runs/round-85/probe-inputs/"$case"; done
```

```text
r85-control              CLEAN (exit 0)
r85-unique-break-control 1 finding (exit 1)
r85-masked-ambiguous     4 findings (exit 1)
r85-isolated-ambiguous   3 findings (exit 1)
r85-harbor-repro         6 findings (exit 1)
```

Both superseded r87 disclosure strings are absent from the delivered checker
(0 occurrences each), yet they are still presented as current delivered behavior
in two tracked knowledge docs:

- `corpus/knowledge/holder-assessment-boundary.md` — carries the dead item-level
  notice string at `:64`, in the decision table at `:104`, and inside its pasted
  "Commands" replay at `:201`/`:209`/`:216`; its `verified-at` line pins the
  contract to `2b48ca7`; its own `recheck` clause says to re-verify "whenever
  the provenance branch of `corpus/fixtures/check_bible.py` changes … or either
  notice string or format changes" — that trigger fired at `2ea9ef1` and was not
  honoured. Its asserted probe counts (masked 5 / isolated 4 / harbor 7) are now
  wrong: delivered is 4 / 3 / 6.
- `corpus/knowledge/r87-provenance-chain-decision-table.md` — rows 14 and 27 and
  nine pasted output blocks carry the dead strings and the `:242-250` code
  anchors, which no longer exist (the delivered file is 395 lines, not 356).

Both docs were last touched at `dfd1fbc`; neither is in the `2ea9ef1` diff.
`JDEP4` reaches the same conclusion independently and files it as
**depth: harmed (bounded)**, scope "checker-semantics fidelity of the
`corpus/knowledge` doc set". `P4` flags the same file as box-3 instruction-
surface drift.

## Findings & named debt

### Per-axis verdicts on the delivered tree

| axis | verdict | receipt | bound |
|---|---|---|---|
| calibration | **improved** | My census: 149 dirs, `0=31/1=118`, 367 lines, 0 stderr, 9 changed + 4 new, 0 exit changes. `JCAL1`: 47/47 disclosure lines on grammar, 0 legacy survivors, 17/17 stop groups single-cause, 0 at/after-stop coverage violations. `V2`: all three fixture READMEs verify line-by-line and each fixture discriminates. | Two pre-r87 compatibility exceptions (below); the 9 changed tuples were not adjudicated tuple-by-tuple by a follow-up seat beyond `JCAL1`'s classification; disclosure is per-item provenance chain, not global; non-dict records cannot carry an ambiguous holder id (stated bound in the commit); unavailable-source-table suppression semantics unchanged. |
| coverage | **improved (bounded)** | Second sourced-mythology family landed and replayable; census 145→149; inspiration notes 1→2; both clusters exit 0; OBS-1 repaired with 8/8 clause anchors. `JCOV5` verdict "improved (bounded)"; both sibling provinces reject the new artifacts as their own (kotodama: no generated system, empty `synthesis/`; chousa: D1 is world-bible record shape, its one method overlap is consumed lore-side). | One printed-page locator, not three; checker `CLEAN` is structural and is not prose support. |
| depth | **improved on the artifact surface; harmed (bounded) on the doc surface — not a clean improvement** | Improved: 7-row table with three distinct citation columns (`JDEP1` "improved", `JDEP3` "improved (bounded)", 3 uncovered inspired-content classes named); ledger row pure append, 4×4 populated (`JDEP2` "IMPROVED", locator `122–163` verified against the live ETCSL page). Harmed: the two knowledge docs above still present removed checker output as current (`JDEP4` "harmed (bounded)"). | Per the round rule "a trade anywhere is NOT an improvement", depth is **not** recorded as improved while the two docs misdescribe the delivered checker. Refreshing them (or explicitly accepting the drift) is the gating step. |

No axis is `unchanged`; none is `unprovable-but-better`; **no L1 verdict
artifact existed at draft time**, so admission remains L1's call. The round
record must not present depth as a clean gain.

### Named debt (all carried into the proposed entry)

1. **Two pre-r87 compatibility exceptions (not a zero-change claim).** Of the
   133 pre-round-87 fixture dirs, 131 are byte-identical; two changed, both pure
   additions: `r61-independent-empty` 17 → 18 findings and
   `r61-independent-unavailable` 6 → 7, each gaining exactly one disclosure
   (`provenance attached to a non-item entity` and `source table unavailable`,
   both at `entities[0].provenance`) and a count footer. This is the intended
   effect of the non-holder stop disclosures, but it is a compatibility
   exception against r87's "133 tuples byte-identical" precedent and must be
   recorded as such, not as zero change (`V1` first surfaced it; `JCAL1`
   confirms both are pure additions).
2. **Unlanded alternatives.** Present as patches only under
   `.ufo/waves/round-88/patches/`, absent from the delivered tree, with none of
   their fixture names landed: `X2-c1-orderonly.patch` (shape-arm only; leaves
   mixed-stop and non-holder gaps), `X3-c1-firstcause.patch` (first-cause only),
   `X4-c1-notice.patch` (rejected-record notice variant), `M1-cluster2.patch`
   (Kojiki; 6 locators → 4 excerpt lines), `M2-cluster2.patch` (Völuspá),
   `F2-r88-fixtures.patch` (`f2-r88-{malformed,dangling,shape}-*` — I verified
   these three fixture dirs are **not** in the tree), and
   `D2-decision-table.md` / `D2-ledger-rows.md` (five-stage workflow draft; its
   r88 row is a template explicitly not to be registered). `M1`/`M2` remain the
   unselected distinct-family candidates; `M3` was the selected one.
3. **Locator count-1.** The landed Maya cluster delivers exactly **one** distinct
   passage locator (`printed p. 209`); both indexed clauses sit in that one
   passage. The wave-spec C2 wording asked for "passage-level locators" (plural),
   and the unlanded `M1` draft demonstrated six locators resolving to four
   excerpt lines. `JCOV5` files this as D-JCOV5-3.
4. **Kotodama handoff contract absent.** `kotodama-shokunin/PROVINCE.md:19-21`
   names `corpus/knowledge/synthesis/worldbible-integration-contract.md` as the
   load-bearing lore↔kotodama handoff, and `test -f` → absent in both lanes
   (kotodama's `synthesis/` is empty; lore has no `corpus/knowledge/synthesis/`
   at all). Carried unchanged from r87's K2 finding; `S3` named it, `JCOV5`
   filed it as D-JCOV5-1, and `K1` escalated it as this round's one authorized
   `l0-questions.md` append (file now 4 lines; round-4 / round-81 / round-87
   lines byte-unchanged; `git status` → ` M l0-questions.md`, uncommitted at
   draft time).
5. **Boundary-doc drift (the depth harm).** `holder-assessment-boundary.md` and
   `r87-provenance-chain-decision-table.md` describe removed behavior, carry
   dead code anchors, and both carry a self-invalidating recheck trigger that
   fired at `2ea9ef1` without being honoured. `JDEP4` files the harm; `P4` flags
   box-3 drift. Not repaired this round (no seat owned the write).
6. **Ledger completeness and row shape.** `JDEP2` F2: the Spence 1913 reference
   that the newly landed Maya cluster actually cites and delivers (`p. 209`
   excerpt) is **not** registered — `grep -c Spence corpus/knowledge/reference-ledger.md`
   → 0 — while the external-only ETCSL citation is. F3: the ETCSL row omits the
   decision table's own requested delivery-status statement / literal
   `external-only / unverified` marker. Both are integration-completeness gaps,
   not defects of the landed row.
7. **Documentation sub-axis.** `corpus/fixtures/README.md` still has no
   `## Round 87` or `## Round 88` section (last section is Round 83) —
   `JCOV5` D-JCOV5-2, carried from r87. `corpus/README.md:6` still describes the
   ledger as "real-world method citations" after the heading was broadened.
8. **Stale present-tense claims inside the new table.** `JDEP4` measured that
   the table's OBS-1 row still says in the present tense that "r87's
   `entities.json:33` attributes a Gate claim to a hymn with no matching
   place/threshold terms" — true at `dfd1fbc`, false at `2ea9ef1` since the
   excerpt was repaired in the same commit. The table also understates what the
   checker validates (it also validates contradictions, `allied_with`
   reciprocity, and timeline occupancy).
9. **Three uncovered inspired-content classes in the new table** (`JDEP3`):
   rights-blocked source disposition (S1), a fictional source presented as
   excerpted but paraphrased (S2), and a mythology parallel that conflicts with
   landed canon (S3). None is a regression; each is a residual class the table
   does not govern.
10. **Process notes.**
    - The author→verifier barrier held as designed: authors produced patches and
      reports only, and patch-level verification happened in this phase against
      the delivered tree. `W1`/`W2` explicitly left every axis `PENDING-L1`; `P2`
      drafted the scorecard before any judge landed, so **`P2-scorecard-r88.md`
      is superseded by the judge roster now on disk** and must be re-cut against
      it, not appended as-is.
    - Census method: fixture invocations must use the same relative path form as
      the baseline or path-embedding fixtures produce false deltas (my
      absolute-path run reported `changed=14`; the relative run reports the true
      `changed=9`).
    - Roster count: the persisted `wave-spec.md` declares 35 seats, enumerates 31
      names, and 37 reports landed; the six unnamed supplementaries (`V1`,
      `C5B`, `C6B`, `C7B`, `J1`, `R1B`) carried the round's decisive verification
      (`Q2` §1). The spec is prose-only, so the count/roster check is not
      mechanical; r86's machine-readable `wave-spec.json` +
      `wave-validation.json` pair would fix it, plus a `phase` field and a
      target-revision hash per seat (`Q2` §3, r89 recommendation).
    - **The delivered revision is not `X1-c1.patch`.** I verified this myself:
      applying `patches/X1-c1.patch` to a clean `dfd1fbc` archive and diffing
      against the delivered checker leaves exactly one 4-line hunk that composes
      the same-record cause summary
      (`'malformed record (unexpected field set); ambiguous holder identity {cause}'`).
      That is the integrator amendment closing `C5B`'s falsification. It is
      reachable only through the commit message — no seat-visible amendment
      artifact exists — and no phase-1 seat verified the amended revision; the
      delivered-tree verification is this judging wave's job (`Q2` §5).
      Recommend an `AMEND-*.md` artifact with before/after hashes for r89.
    - `K1`'s boundary audit reported "JCOV5 never delivered fleet-wide" after a
      6×10 s poll; `JCOV5.md` landed at 03:14, i.e. the wait raced the arrival.
      Both reach the same no-bleed conclusion, but the record should not carry
      K1's "missing JCOV5" as a fact.
    - `Q1` and `S3` both reported an untracked
      `corpus/fixtures/__pycache__/check_bible.cpython-314.pyc` outside their
      write scopes; it is not present in the delivered commit and `.gitignore`
      does not name it. Worth a `.gitignore` line or `PYTHONDONTWRITEBYTECODE=1`
      in the census recipe.
    - No saturation and no retirement declared: the `capabilities` table is
      still empty and no 0–10 rubric exists, so the stagnation window N is not
      declarable. The historical duplicate-name rejection remains in force.
    - No commit, push, or merge by this seat; no registry write; no fabricated
      receipt. Province verdict from `K1`: r88 is **province-clean** (every
      changed path under `lore-shokunin/`; no rights ruling; no contradiction
      resolution; no chousa-method or kotodama-craft absorption).
    - SHONEN: no `[x]`, no promotion; `SHONEN.md` byte-unchanged this round
      (`git diff --stat dfd1fbc 2ea9ef1 -- SHONEN.md` → empty). Box 2's
      "logged in LOG.md" clause is satisfied only once this entry is appended.

## Handoff

### Proposed `LOG.md` append (append-ready text; not for direct append before L1 adjudication)

> ## Round 88 — 2026-10-17 (stop-cause repair + second sourced cluster + sourced-inspiration table; luna-max work wave; work commit `2ea9ef1`)
>
> - Baseline before this round is `dfd1fbc3711f2b28597d74444819aca91fe6bc31`
>   (r87 closure; lane tree clean). The round ran as a world-bible work wave
>   recorded under `.ufo/waves/round-88/` — 37 seat reports plus prefixed patch
>   artifacts, landed as `2ea9ef1` (103 files, +9292/−25) — followed by a
>   judging/integration wave under `.ufo/waves/round-88/followup/`. The persisted
>   wave-spec manifest names 35 seats; six landed reports (`C5B`, `C6B`, `J1`,
>   `V1`, `R1B`, `C7B`) are supplementary to it. No push and no merge this round.
>
> - **Motivating evidence — C1 (calibration).** r87 admitted (bounded) that the
>   provenance-chain stop fires only for holder ambiguity and only from a valid
>   record shape, and that its disclosure named the *later* ambiguity even when
>   an earlier record had stopped assessment first. Measured at `dfd1fbc`:
>   `r87-probe-shape-ambiguous` → 2 findings, no disclosure at all;
>   the mixed-stop case → disclosures blaming the holder ambiguity at `[1]`
>   though the unknown source at `[0]` latched first; an unknown-source-only
>   stop → 1 finding and no disclosure (`patches/B3-before-state.json`,
>   `V1`, `JCAL1`).
>
> - **C1 landed — `2ea9ef1`.** `corpus/fixtures/check_bible.py` (+59/−20; 356 →
>   395 lines; SHA-256 `dcacffd6981e1af5f60b31bed20c6eccce25970444088e4ee2e30e3249411911`):
>   the holder-only latch is replaced by first-stop cause tracking over an
>   enumerated cause set (source table unavailable, provenance on a non-item
>   entity, duplicate item id, four malformed-record forms, malformed record
>   with an ambiguous holder id, dangling holder both fields, unknown source,
>   ambiguous holder identity); every record at or after the stop carries one
>   disclosure naming the *actual* first cause and its origin; a shape-invalid
>   dict record carrying an ambiguous holder id now arms the stop; simultaneous
>   same-record causes are named as a combined summary; the wording carries the
>   `(input-structural finding, not sourced-canon)` qualifier and makes no causal
>   overclaim (E1 candidate 3). Three durable fixtures land with it
>   (`r88-shape-ambiguous-armed`, `r88-mixed-stop`, `r88-nonholder-stop`).
>   Counting from the lane root:
>   `python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-mixed-stop` → 6
>   findings, exit 1, every disclosure naming `first stop: unknown source
>   'f1-mixed-missing-source' at entities[5].provenance[0]`. Closure census:
>   149 fixture dirs (was 145), exits `0=31 / 1=118`, 367 violation lines
>   (baseline-145 subset 352; baseline 331), 0 stderr cases; deltas enumerable —
>   **9 changed tuples + 4 new, 0 exit changes, no non-disclosure finding
>   removed** (the 19 replaced lines are the superseded r87 disclosure forms:
>   `JCAL1` classifies 26 added disclosures, 13 reworded disclosures, 1 field
>   finding, 9 count footers, 0 `OTHER`).
>   Corroboration: `V2` (all three fixture READMEs verified line-by-line; each
>   fixture discriminates against the baseline checker), `JCAL1` (47/47
>   disclosure lines on grammar, 0 legacy survivors, 17/17 stop groups
>   single-cause, 0 at/after-stop coverage violations), `SE2` (independent
>   B1-template recomputation: 136 unchanged / 9 changed, every changed fixture
>   re-run twice with no nondeterminism, write-scope sentinel clean),
>   `JCAL3`/`JCAL5`/`H2`.
>   Bounds: two pre-r87 fixtures are **not** preserved byte-for-byte —
>   `r61-independent-empty` 17 → 18 and `r61-independent-unavailable` 6 → 7,
>   each a single additive non-holder-stop disclosure (the other 131 pre-r87
>   dirs are unchanged); disclosure is per-item provenance chain, not global;
>   non-dict records cannot carry an ambiguous holder id (stated bound);
>   unavailable-source-table suppression semantics unchanged.
>
> - **C2 landed — `2ea9ef1` (coverage).** A second sourced-mythology family
>   distinct from r87's Sumerian/ETCSL cluster:
>   `corpus/fixtures/r88-m3-maya-cluster/` — K'iche/Maya via Lewis Spence's 1913
>   English synthesis, passage-located to printed p. 209 with the cited sentence
>   delivered in `source-excerpt.md`; a two-row clause→element symbolism index
>   with an explicit limit column; two in-world source records; a tick-9
>   occupied-slot near-miss (distinct actors and places) rather than a
>   double-booking. r87's OBS-1 is repaired by the **delivered-text** option:
>   the hymn excerpt now names the Mother-Tide Gate and the attributed claim at
>   `entities.json:33` follows it, with all eight clause anchors resolving
>   exactly once (`grep -cF` per anchor → 8 × 1). The `gate-witness` repoint
>   alternative was not landed. Counting: both clusters
>   `CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0;
>   census 145 → 149 dirs; inspiration-note files 1 → 2. Corroboration: `JCOV5`
>   (verdict improved (bounded); both sibling provinces reject the artifacts as
>   theirs), `K1` (province-clean, no bleed), `M5`/`C7B`. Bounds: one distinct
>   printed-page locator, not three; `CLEAN` is structural and is not prose
>   support; the clause map quotes the first clause with inner single quotes
>   while the excerpt uses double quotes, so only the excerpt's own wording
>   matches a fixed-string search.
>
> - **C3 landed — `2ea9ef1` (depth).**
>   `corpus/knowledge/r88-sourced-inspiration-decision-table.md` — 7 decision
>   rows × 6 columns keeping attribution, rights status, and AI-training
>   permission as three distinct columns, with locator/delivered-text rules, an
>   in-world claim→excerpt support rule (`grep -nF` anchor preflight), ledger
>   registration shape, and intra-cluster conflict handling; the R1B scope note
>   is carried as a prepended comment. `corpus/knowledge/reference-ledger.md`
>   gains the r87 ETCSL row (pure append, `3 2` numstat; three prior rows
>   byte-identical; 4 data rows × 4 populated columns; locator `122–163`
>   verified against the live ETCSL page). Corroboration: `JDEP1` (7/7 rows,
>   "improved"), `JDEP3` ("improved (bounded)"), `JDEP2` ("IMPROVED").
>   Bounds: the Spence reference the new cluster actually cites is **not**
>   registered (only the external-only ETCSL citation is); the ETCSL row omits
>   the table's own requested delivery-status / `external-only / unverified`
>   marker; the table's OBS-1 row still speaks of the repaired defect in the
>   present tense; three inspired-content classes remain uncovered
>   (rights-blocked source, paraphrased-as-excerpted fictional source, parallel
>   conflicting with landed canon).
>
> - **Depth harm recorded, not netted.** The C1 commit replaced the checker's
>   entire disclosure family without updating the two tracked knowledge docs
>   that are the fleet's behavioral reference for the provenance branch:
>   `corpus/knowledge/holder-assessment-boundary.md` and
>   `corpus/knowledge/r87-provenance-chain-decision-table.md` still present the
>   removed r87 notice strings as current delivered output, carry dead code
>   anchors (`:242-250` of a 356-line file), and each carries a recheck trigger
>   that fired at `2ea9ef1` without being honoured. Delivered probe counts are
>   4 / 3 / 6 (masked / isolated / harbor) where the boundary doc asserts
>   5 / 4 / 7. Per the round rule that a trade is not an improvement, **depth is
>   not recorded as a clean improvement** this round; refreshing the two docs is
>   the gating step (`JDEP4` files the harm; `P4` flags the same file as box-3
>   instruction-surface drift).
>
> - **Per-axis verdicts.** calibration **improved** (bounded as above);
>   coverage **improved (bounded)**; depth **improved on the artifact surface,
>   harmed (bounded) on the checker-semantics doc surface**. No axis unchanged;
>   no `unprovable-but-better`; the round is **not admitted** here — L1
>   adjudication is the remaining step and no L1 verdict artifact existed at
>   record-drafting time.
>
> - **Carried debt.** (1) The two pre-r87 compatibility exceptions above.
>   (2) Unlanded alternatives kept as patches only: `X2`/`X3`/`X4` C1 variants,
>   `M1` (Kojiki) / `M2` (Völuspá) cluster candidates, `F2` fixture set
>   (`f2-r88-*` absent from the tree), `D2` workflow/ledger drafts. (3) One
>   locator, not three, in the landed cluster. (4) The kotodama↔lore handoff
>   contract named by `kotodama-shokunin/PROVINCE.md:19-21` is still unwritten;
>   escalated as this round's `l0-questions.md` append (file 3 → 4 lines).
>   (5) The two stale knowledge docs. (6) Spence unregistered; ETCSL row's
>   delivery-status marker omitted. (7) `corpus/fixtures/README.md` has no
>   Round 87/88 section; `corpus/README.md:6` still says "method citations".
>   (8) Three uncovered inspired-content classes in the new table.
>
> - **Process.** The author→verifier barrier held: work-wave seats produced
>   patches and reports only, and patch-level verification happened in the
>   follow-up wave against the delivered tree. Two regimen gaps are recorded.
>   First, the delivered checker is not `X1-c1.patch`: it is X1 plus a 4-line
>   integrator amendment composing the same-record cause summary (the amendment
>   closing `C5B`'s falsification of X1's attribution); that amendment is visible
>   only in the commit message, no phase-1 seat verified the amended revision,
>   and no amendment artifact exists. Second, the wave-spec declares 35 seats,
>   enumerates 31, and 37 landed — the six unnamed supplementaries carried the
>   round's decisive verification — and the spec is prose-only, so the roster
>   check is not mechanical (`Q2`). Census invocations must use the
>   baseline's relative fixture paths — absolute paths make the five
>   path-embedding "missing-file" fixtures report false deltas. `P2`'s scorecard
>   draft was written before any judge landed and is superseded by the judge
>   roster; re-cut it rather than append it. `K1`'s poll for `JCOV5` raced that
>   report's arrival, so its "JCOV5 never delivered" line is not a fact.
>   `__pycache__` writes were observed outside two seats' scopes; add a
>   `.gitignore` line or pin `PYTHONDONTWRITEBYTECODE=1`.
>
> - **Province.** `K1` verdict: r88 is province-clean — every changed path is
>   under `lore-shokunin/`, no rights determination, no silent contradiction
>   resolution, no chousa-method or kotodama-craft absorption. The r87 L0 line
>   stands unamended; the round-88 L0 line is a distinct question about who
>   authors the integration contract.
>
> - **SHONEN.** No promotion, no push, no merge. `SHONEN.md` is unchanged this
>   round (`git diff --stat dfd1fbc 2ea9ef1 -- SHONEN.md` → empty); all four
>   boxes stay `[~]`/`[ ]` with no `[x]` claimed. Box 2's "logged in LOG.md"
>   clause is satisfied only once this entry is appended. No saturation or
>   retirement is declared — the `capabilities` table is still empty and no
>   rubric exists, so the stagnation window N is not declarable.

### Notes for the integrating owner (not part of the LOG text)

- Append under a new `## Round 88 — …` section at the end of `LOG.md`. No
  tracked file was written by P3.
- Figures sourced from follow-up seats rather than re-measured by me are
  attributed in-line (`V2`, `JCAL1`, `JCAL3`, `JCAL5`, `H2`, `JCOV5`, `JDEP1`,
  `JDEP2`, `JDEP3`, `JDEP4`, `K1`, `P2`, `P4`, `Q2`, `SE2`). P3's own
  re-measurements: the 149-dir
  census and its tuple delta against `B1-tuples.json`; the two cluster replays;
  the eight OBS-1 clause anchors; the Maya clause anchors and locator; the
  ledger numstat/row diff; the delivered checker SHA-256 and line count; the
  dead-string greps; the five r85 probe replays; the unlanded-patch and
  unlanded-fixture presence checks; and the X1-patch-vs-delivered diff proving
  the integrator amendment.
- Before appending: re-cut `P2-scorecard-r88.md` against the judge roster (it
  predates it and leaves all axes `PENDING-L1`), and decide whether to refresh
  the two drifted knowledge docs first. If they are refreshed, depth can be
  recorded as improved and the harm paragraph replaced with the repair receipt.
- Working-tree state at draft time (03:15 `-03:00`): `l0-questions.md` modified
  (K1's authorized append, uncommitted); `.ufo/waves/round-88/followup/`
  untracked; nothing else. If the integrating owner commits the follow-up
  artifacts before appending, drop the "uncommitted" qualifier on the L0 line.
- Scratch probes used by P3 lived under `/tmp/p3/` and are not deliverables.
