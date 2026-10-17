# CB1 — Boundary-doc refresh proposal (for the round-90 closure)

**Status: proposal only.** No `corpus/` file was changed by this seat. Ready to apply at the
r90 closure by the integrator, followed by the r88-I1 re-verification (replay the pasted blocks
after patching). Basis: delivered tree `ca7f9ef`
(checker `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`, 428 lines);
full drift inventory, freeze receipt, census, and probe output in
`.ufo/waves/round-90/followup/CB1.md`.

Apply order below matches the drift ids D1–D14 in `CB1.md`. Replacement text is written to be
pasted verbatim; line numbers are the delivered doc's (`ca7f9ef`).

---

## D4 — Header + banner (doc `:2-10`)

Replace:

```text
<!-- Refreshed at round-89 closure from seat CB1's verified proposal
     (.ufo/waves/round-89/followup/CB1-boundary-refresh.md) with seat E1's
     corrections applied; every anchor and pasted output re-derived from the
     delivered tree at 1b09f3f (checker e2bb9639). -->

> **Landed at round-89 closure** (replacing the r88-closure version). Drift inventory:
> `.ufo/waves/round-89/followup/CB1.md` (CB1-R1…R19); corrections per
> `.ufo/waves/round-89/followup/E1-boundary-update-proposal.md` §F applied.
```

with:

```text
<!-- Refreshed at round-90 closure from seat CB1's verified proposal
     (.ufo/waves/round-90/followup/CB1-boundary-refresh.md); every anchor and pasted
     output re-derived from the delivered tree at ca7f9ef (checker ff9fd2aa). -->

> **Landed at round-90 closure** (replacing the r89-closure version). Drift inventory:
> `.ufo/waves/round-90/followup/CB1.md` (CB1-D1…D14); the r89-closure proposal
> (`.ufo/waves/round-89/followup/CB1-boundary-refresh.md`) remains the prior landed revision.
```

## D3 — Revision history (doc `:23-28`)

Old tail of the source paragraph: "…round-89 seat X1 added the multi-cause summary, the
raw-vs-resolved-index cause wording, and the not-uniquely-resolvable qualification of
comparison findings (integrated in `1b09f3f`). This revision was rewritten by round-89 seat
CB1 against the delivered checker at `1b09f3f`…"

New text (from "round-89 seat X1" onward):

```text
round-89 seat X1 added the multi-cause summary, the raw-vs-resolved-index cause wording,
and the not-uniquely-resolvable qualification of comparison findings (integrated in
`1b09f3f`); round-90 composed seat X2's null guard — a null holder field never produces an
identity clause — with seat X3's integer-only tick reading per seat C9's ruling: tick order
is an integer comparison and holder-identity uncertainty does not qualify it, while genuinely
unresolved non-null holder identities still qualify chain-continuity and first-record
findings (integrated in `ca7f9ef`, checker `ff9fd2aa`). This revision was rewritten by
round-90 seat CB1 against the delivered checker at `ca7f9ef`
(`.ufo/waves/round-90/followup/CB1.md`)
```

## D4 — verified-at (doc `:35-44`)

Replace the revision labels and add the replay receipt:

```text
verified-at: RUNTIME REPLAYED on the delivered tree at `ca7f9ef` by round-90 seat CB1;
exact commands and observed output are pasted under "Commands" and in
`.ufo/waves/round-90/followup/CB1.md`. All fourteen pasted case blocks below replay
byte-identically through the delivered checker. The single `remain unassessed … first stop:`
disclosure form, every named first-stop cause (including both raw-vs-resolved wordings), the
multi-cause joining rule, the qualified chain-comparison forms, and the emission-order
asymmetry below are demonstrated by that replay, not contract text. This verifies the listed
checker behavior only; it is not a five-gate score and not a claim about fictional truth. The
baseline (`5eb9451`) triples remain as recorded in `reports/round-1/current-baseline.json`
and `reports/round-1/baseline-probes.json`.
```

## D5 — recheck (doc `:46-60`)

Replace the second and third sentences:

```text
Re-verify whenever the provenance branch of `corpus/fixtures/check_bible.py` changes — in
particular the comparison gate (`:322`) and its branches, chain continuity (`:327-337`) and
tick order (`:323-326`) — whenever the `remain unassessed` template string or any named
first-stop cause changes, whenever the raw entity/source counters, the `is not uniquely
resolvable` detail string, the null guard in `holder_identity_detail` (`:169-170`), or the
`; ` cause-joining rule changes, or whenever any `corpus/live/runs/round-85/probe-inputs/`
JSON byte changes.
```

In the same block, change "does not exist at `1b09f3f`" to "does not exist at `ca7f9ef`".

## D11/D12 — Contract item 5 (doc `:118-135`)

Keep the r88→r89 census sentence as history, then append:

```text
Round-90 verification (seat CB1, `ca7f9ef`): the r89 checker (`e2bb9639`) and the delivered
checker (`ff9fd2aa`), run against the same 160 fixture directories, produced 0 exit-code
changes, 0 stderr changes, and 0 changed stdout tuples; four new directories
(`r90-c1-rawpresent-to`, `r90-c1-rawpresent-from`, `r90-c1-rawpresent-source`,
`r90-c1-three-causes`) were added in the same commit, making 164 fixture directories
(B1's 160-row tuple receipt replayed, 0 mismatches).
```

## D6/D7 — Cause section anchors (doc `:148-180`)

- Heading `:148`: `First-stop causes (delivered 1b09f3f)` → `First-stop causes (delivered ca7f9ef)`.
- `{raw_presence}` refs in `:154`: `:272`, `:285`, `:306` → `:274`, `:287`, `:308`.
- Cause-table Code column remap: `:198-199`→`:200-201`; `:200-201`→`:202-203`;
  `:202-203`→`:204-205`; `:215-221`→`:217-223`; `:222-248`→`:224-250`; `:257-260`→`:259-262`;
  `:261-264`→`:263-266`; `:265-268`→`:267-270`; `:269-273`→`:271-275`; `:279-286`→`:281-288`;
  `:274-278`→`:276-280`; `:287-297`→`:289-299`; `:298-301`→`:300-303`; `:302-307`→`:304-309`;
  `:308-310`→`:310-312`.
- Multi-cause paragraph `:173-180`: `:256`→`:258`, `:313-316`→`:315-318`.
- Contract items 1–4 refs: `:206-208`→`:208-210`; `:275`→`:277`, `:288`→`:290`,
  `:292-297`→`:294-299`, `:182`→`:184`; `:225-233`→`:227-235`, `:236-244`→`:238-246`,
  `:215-221`→`:217-223`.

## D1 — Decision-table row 2 code refs (doc `:187`)

Replacement for the parenthetical: `(delivered :343-344, :349-350, :333; …)` → 
`(delivered :337, :326, :343; …)` — the definite chain-break, tick, and first-record forms.

## D1/D2 — Decision-table row 3 (doc `:188`), full replacement

```text
| A referenced holder ID is **not uniquely resolvable**: ≥ 2 raw entity rows carry it but exactly one survives the field check | Chain-continuity and first-record findings that involve that ID are qualified: `{record_label}: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: {detail}; got {…!r}` (or, when only the observed side is unresolvable, `expected from_holder {…!r}; got {…!r}; {detail}`), and the first-record form `… possible provenance chain break, not a definite identity mismatch: {detail}; first record must have from_holder null` (`:330-335`, `:339-341`). Tick findings are NOT qualified: `{record_label}.tick: provenance tick {…} must be greater than previous tick {…}` with no identity note (`:323-326`). A null holder field contributes no clause and never triggers qualification (`:169-170`). `{detail}` is `{reference} {id!r} is not uniquely resolvable ({raw} raw entity rows carry this id, but only {indexed} is in the resolved index)` (`:171-175`) | That the chain is definitely broken, or definitely intact — the chain finding's expected or observed holder is not a single row, so the mismatch may be an artifact of the rejected duplicate. It does not make tick order, an integer comparison, uncertain. It also does not name which raw row was rejected; read that row's own `VIOLATION:` line | Repair the duplicate first (rename or merge, per the checklist), rerun, and re-read the chain comparison as a definite finding. A tick line already reads as definite while the duplicate remains. Delivered evidence: `r89-fn2-unresolved-chain-break` (expected side) versus `r89-fn2-control` (unqualified control); CB1's round-90 edge probe adds observed-side, null-observed/expected-unresolved, and unqualified-tick receipts (`CB1.md`) |
```

## D2 — Limits bullets (doc `:234-317`)

- "Comparison findings can be non-definite" (`:267-276`), full replacement:

```text
- Comparison findings can be non-definite, but only for holder-identity comparisons. When a
  **non-null** holder id involved in a chain-continuity or first-record comparison has ≥ 2 raw
  entity rows of which exactly one is in the resolved index, the finding is rewritten as
  `input-structural finding, not sourced-canon; possible provenance chain break, not a
  definite identity mismatch: …` or, for the first record, `… : {detail}; first record must
  have from_holder null` (`:330-335`, `:339-341`). The expected and the observed side are both
  tested and either can trigger it (`:328-329`, `:339`); a `None` side contributes no clause
  (`:169-170`). Tick comparisons are not in this class: strict tick order is decided by the
  two validated integer tick values, so an unresolved holder id cannot qualify it — the only
  tick prefix comes from an independently ambiguous source citation (`:323-326`; seat C9's
  round-90 ruling). A plain duplicate whose rows both pass validation cannot reach a
  comparison at all: it makes the referencing record ambiguous and therefore invalid, which
  stops the chain instead.
```

- Scope bullet (`:234-241`): `:313-319`, `:320` → `:315-321`, `:322`.
- Causes-collected bullet (`:246-257`): `:256`, `:313-316` → `:258`, `:315-318`.
- Emission-order bullet (`:277-280`): `:220`, `:247`, `:317-318` → `:222`, `:249`, `:319-320`.
- Ambiguous-source bullet (`:300-305`): `:311-312` → `:313-314`.
- Chain-eligibility bullet (`:306-312`): delivered `:198-203` → `:200-205`.
- Measurement-ceiling bullet (`:313-317`): "No such score exists for `1b09f3f`" → `ca7f9ef`.

New bullet to add after "Comparison findings can be non-definite" (retires Q89-050's
doc-side residue):

```text
- The two r89 hedged shapes are repaired at `ca7f9ef`: a `from_holder: null` follow-on and a
  tick inversion are definite structural findings, and the qualification above is bounded to
  chain-continuity/first-record comparisons of genuinely unresolved non-null IDs. (A null
  follow-on whose expected side is itself an unresolved non-null id stays qualified — the
  break is genuine, the expected holder is not a single row.)
```

## D9 — Commands header + five-gate entry (doc `:321-332`, `:480-495`)

- "against the checker at `1b09f3f`" (`:322`) → "at `ca7f9ef`"; the pasted outputs are
  byte-identical and stay as-is.
- "That helper does not exist at `1b09f3f`" (`:491-492`) and "no five-gate score is recorded
  for this tree" → `ca7f9ef` (helper still absent; verified).

## D11 — Remaining-branches paragraph (doc `:460-478`), replacement

```text
The six single-cause branches without their own durable fixture each have one now, and replay
as one cause plus one disclosure per affected record: `r89-c1-invalid-tick` (`first stop:
malformed record (invalid tick) at entities[3].provenance[1]`, 4 violations),
`r89-c1-invalid-from-holder` (3), `r89-c1-invalid-to-holder` (3), `r89-c1-malformed-source-id`
(`entities[2].provenance[1]`, 3). Round-90 added durable fixtures for the two `present in raw …
but absent from the resolved index` wordings (`r90-c1-rawpresent-to`, `r90-c1-rawpresent-from`,
`r90-c1-rawpresent-source`) and for a three-cause valid-key record (`r90-c1-three-causes`,
`malformed record (invalid tick); holder reference to_holder … ; source reference …`); their
delivered output is pasted in the r90 work wave (`.ufo/waves/round-90/F1.md`) and replayed by
CB1 at `ca7f9ef`. Still scratch-only, with no durable fixture in the tree: the observed-side and
first-record FN-2 chain forms, and the null-chain definite form. The tick-under-unresolved-holder
FN-2 sub-branch no longer exists — r90's integer-only tick reading removed it (seat C9's ruling);
its would-be fixture was never built and is not owed. Evidence for the remaining shapes is
CB1's round-90 edge probe (`/__cb1_probe__`, receipts in
`.ufo/waves/round-90/followup/CB1.md`) and the r90 seats' probes (B3, C5, C9). Round-88's
scratch evidence for the remaining families (non-dict record, non-item provenance, duplicate
item id, unavailable source table, both-fields ambiguity at one record, tick-masks-ambiguity) is
recorded in `/tmp/cb1/probes2`, `/tmp/cb1/probes3` and
`.ufo/waves/round-88/followup/CB1.md` §3; note that `/tmp` reached inode exhaustion on
2026-10-17, so that scratch may not survive.
```

## D10 — In-tree inventory (doc `:543-553`), replacement numbers

```text
- In-tree provenance fixtures at `ca7f9ef`: 33 directories carry `provenance` (29 at
  `1b09f3f`); 13 provenance records across ten of them reference a duplicated holder id —
  `r87-masked-break-from-ambiguous`, `r87-masked-break-to-ambiguous`,
  `r87-probe-multi-invalid`, `r87-probe-nonitem-kinds`, `r87-probe-record-and-chain` (three
  records), `r87-probe-shape-ambiguous`, `r88-mixed-stop`, `r88-shape-ambiguous-armed`,
  `r89-c1-multi-cause-valid`, `r89-fn2-unresolved-chain-break` (plus the r85 live probes
  outside `corpus/fixtures`). The four round-90 fixtures carry provenance but no duplicated
  holder references (dangling raw-present ids only). `r7-item-ambiguous` is ambiguous SOURCE
  only; `r61-*` are dangling holders on a non-item entity. Measured by
  `.ufo/waves/round-90/followup/CB1.md` (r90) and §M7 of the r89 CB1 report.
```

## D8/D12 — README/citations paragraph (doc `:565-574`), replacement

```text
- Rules text: `corpus/fixtures/README.md:110-119` (provenance discipline, no inferred history,
  citation ≠ support) and `:121-128` (round-7 duplicate-source rule mirrored by this holder
  contract). The README carries `## Round 88` (`:1008-1011`) and `## Round 89` (`:1012-1015`)
  sections; the Round 89 section states the r89 cause branches and points readers to this
  document as the first-stop cause contract. There is no `## Round 90` section at `ca7f9ef`, so
  the r90 integer-only tick reading, the null guard, and the four new fixtures are stated only
  here (and in the r90 wave artifacts) until a Round 90 section lands. The r87 decision table
  (`corpus/knowledge/r87-provenance-chain-decision-table.md`) is superseded and still quotes
  removed strings; treat it as history.
```

## D13 — Status split (doc `:578-620`) + measured-results slot (`:622-630`)

- OBSERVED bullet: change `(round-89 seat CB1, 1b09f3f; …)` to `(round-89 seat CB1 and
  round-90 seat CB1, ca7f9ef; …)`; change "the 165-directory two-revision census" to "the
  two-revision censuses (r89: 160 fixture dirs + 5 live probe dirs = 165; r90: 160 → 164
  fixture dirs, 0 changed tuples of the 160, 0 exit changes, 0 stderr)"; add "the round-90
  fixture replays and the fourteen pasted-block parity replay".
- "OBSERVED only in scratch probes" bullet (`:589-593`): replacement per D11 (durable list
  shrunk; tick sub-branch retired; observed-side/first-record/null-definite remain
  scratch-only).
- "REPLAYED, not scored" bullet: `1b09f3f` → `ca7f9ef`.
- Measured-results slot: revision labels `1b09f3f` → `ca7f9ef` (helper still absent; the
  cipher of recorded evidence is the 14-block replay + census + edge probes).

## D12 — Closure-adjacent actions (other files; integrator-owned)

1. `corpus/fixtures/README.md` — add before/after the current end (the r89 closure added its
   section the same way):

   ```text
   ## Round 90: definite null chains, integer-only ticks, raw-present fixtures

   `r90-c1-rawpresent-to/`, `r90-c1-rawpresent-from/`, `r90-c1-rawpresent-source/` pin the
   raw-present/schema-invalid wording for holders and sources; `r90-c1-three-causes/` pins the
   three-cause joined first-stop summary (C1, commit `ca7f9ef`). The r90 checker (seat X2's
   null guard + seat X3's integer-only tick reading, composed per seat C9's ruling) makes
   `from_holder: null` follow-ons and tick inversions definite structural findings;
   FN-2 qualification remains only for chain comparisons of genuinely unresolved non-null
   holder ids. First-stop cause contract: `corpus/knowledge/holder-assessment-boundary.md`
   (r90 refresh).
   ```

2. `corpus/fixtures/r87-probe-source-prefix/README.md:1` — the cited `:350`, `:333`, `:344`
   are r89 checker lines; at `ff9fd2aa` the same diagnostics are the first-record prefix
   (`:343`), tick prefix (`:325-326`), and chain-break prefix (`:337`). Re-anchor (Q89-032).
3. `SCORECARD.md` r89 calibration bound ("one-line fix queued for r90") and Q1's Q89-050
   residue: the r90 closure record should mark the hedged-shape repair delivered and the
   doc-side fixture-family residue retired by this refresh.

## Consolidated anchor remap (r89 doc refs → delivered `ff9fd2aa`)

Conversion rule: refs ≤ `:168` are unchanged; refs `:169-320` shift +2; the tick-identity
block (`:322-350` in the old file) is replaced by the shorter integer-only branch, so later
refs shift −7 (net). Verified landmarks:

| r89 doc ref | delivered ref | what it is |
|---|---|---|
| `:38-39`, `:72-76`, `:82-83`, `:85-91`, `:93`, `:97` | same | raw counters declared/accumulated, index construction |
| `:164-166` | same | holder count collection |
| `:168-173` | `:168-175` | `holder_identity_detail` (null guard inserted `:169-170`; detail return `:175`) |
| `:182` | `:184` | relation-endpoint ambiguity precedent |
| `:185-352` | `:187-345` | provenance loop |
| `:191` / `:192-194` | `:193` / `:194-196` | item-kind guard / `expected array` |
| `:198-203` | `:200-205` | item-level first-stop tests |
| `:206-208` | `:208-210` | disclosure template (`report_unassessed`) |
| `:212-214` | `:214-216` | top-of-loop emission |
| `:215-221` | `:217-223` | non-dict branch |
| `:222-248` | `:224-250` | key-set branch + shape-invalid holder scan |
| `:249-312` | `:251-314` | field validation and cause collection |
| `:256`, `:313-316`, `:313-319`, `:317-318` | `:258`, `:315-318`, `:315-321`, `:319-320` | cause append / join / latch |
| `:272`, `:285`, `:306` | `:274`, `:287`, `:308` | `{raw_presence}` |
| `:269-273`, `:279-286`, `:302-307`, `:308-310` | `:271-275`, `:281-288`, `:304-309`, `:310-312` | dangling holders / source reference / source unavailable |
| `:274-278`, `:287-297`, `:298-301` | `:276-280`, `:289-299`, `:300-303` | ambiguous holder / invalid source_id |
| `:275`, `:288`, `:292-297` | `:277`, `:290`, `:294-299` | local `ambiguous entity` lines |
| `:320` | `:322` | comparison gate (`first_stop is None`) |
| `:322-326` (identity on both tick sides) | `:323-326` (branch), `:328-329` (chain expected/observed) | tick vs chain evaluation |
| `:327-333` | `:330-335` | qualified chain form |
| `:334-344` | `:338-343` (qualified `:339-341`) | first-record form |
| `:345-350` | **removed** | tick identity qualification (C9 ruling) |
| `:333`, `:343-344`, `:349-350` | `:326`, `:337`, `:343` | definite tick / chain / first-record forms |
| `:220`, `:247` | `:222`, `:249` | arming-record emission |
| `:311-312` | `:313-314` | `chain_has_ambiguous_source` |
| `:425-435` | `:418-428` | CLI/exit behavior |

## Verified-unchanged (do not touch)

- All 14 pasted output blocks (r85 probes ×5; r88/r89 fixtures ×6; multi-cause + FN-2 pair ×3)
  replay byte-identically at `ca7f9ef`.
- Cause table behavior, local `ambiguous entity` shapes, the single disclosure template, the
  emission-order asymmetry, the latch/no-resume semantics, and the CLI/exit strings are
  unchanged by r90 — only line anchors move (remap above).
- `corpus/fixtures/` still contains only `check_bible.py` as a Python file;
  `measure_holder_disclosure.py` is still absent at `ca7f9ef`; the five r85 live probe inputs
  are unchanged.
