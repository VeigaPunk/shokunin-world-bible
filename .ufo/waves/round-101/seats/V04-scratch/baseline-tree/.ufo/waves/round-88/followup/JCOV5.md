# JCOV5 — Coverage judge #5 (sibling adjacency)

Seat scope: read-only check of `kotodama-shokunin/` (its minted corpus if any)
plus `chousa-shokunin/PROVINCE.md`; decide whether `r88-m3-maya-cluster` or the
D1 table reads as either sibling's province rather than lore's canon-record;
record rejected-fit reasoning per sibling for the NEW artifacts. Axis judged:
**coverage**.

Judged tree: lore-shokunin `HEAD = 2ea9ef13a928475b13fd578740ea521bed4bd649`
(`git rev-parse HEAD`), tree clean (`git status --porcelain` → empty). No
sibling file was written; this seat's only write is this report.

## Work performed

- Read the delivered r88 artifacts on the committed tree, not on patches:
  `corpus/fixtures/r88-m3-maya-cluster/` (all 10 files),
  `corpus/knowledge/r88-sourced-inspiration-decision-table.md` (D1), and the
  `corpus/knowledge/reference-ledger.md` diff `dfd1fbc..2ea9ef1` (D3 ETCSL row).
- Read the two sibling provinces in full: `kotodama-shokunin/PROVINCE.md`,
  `AGENTS.md`, `MINT.md`, `SKILL.md`, `LOG.md` and its whole `corpus/`;
  `chousa-shokunin/PROVINCE.md`, `AGENTS.md`, `SCORECARD.md`, `SKILL.md` and
  the reference/chain/integrity knowledge notes.
- Replayed the coverage artifacts and took anchor receipts (commands below).
- Compared against the wave's own boundary seats (`.ufo/waves/round-88/S3.md`,
  `C7.md`, `C7B.md`); my rejected-fit reasoning is independent and agrees with
  their bounded-pass conclusion, and I add the chousa side they did not audit.
- No wait-check dependency was specified for this seat beyond the block's
  instruction to work with what exists; the C2 artifacts are landed and
  committed, so nothing was unavailable.

## Before → after measurements

Baseline `dfd1fbc` per `.ufo/waves/round-88/wave-spec.md`; after = delivered tree.

| Measurement | Command | Before | After |
|---|---|---|---|
| fixture census | `ls -d corpus/fixtures/*/ \| wc -l` | 145 | **149** |
| sourced-mythology clusters | `ls corpus/fixtures/*/inspiration-note.md \| wc -l` | 1 | **2** |
| new dirs vs baseline | `git diff --name-status dfd1fbc 2ea9ef1 \| grep '^A'` | — | 4 new: `r88-m3-maya-cluster`, `r88-mixed-stop`, `r88-nonholder-stop`, `r88-shape-ambiguous-armed` (only the first is coverage; 3 are C1 calibration fixtures) |
| Maya cluster replay | `python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-m3-maya-cluster` | — | `CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0 |
| Maya clause anchors | `grep -nF -- 'He called out “Earth,”' corpus/fixtures/r88-m3-maya-cluster/source-excerpt.md` · `grep -nF -- 'and the solid land appeared.' …` | — | both resolve at `source-excerpt.md:5` |
| Maya locator | `grep -nF -- 'printed p. 209' …/source-excerpt.md` | — | resolves at line 3 |
| OBS-1 repair | `grep -nF -- 'at the Mother-Tide Gate' corpus/fixtures/r87-myth-cluster/lowwater-hymn-excerpt.md` | r87 claim `entities.json:33` names the Gate with no matching place term in the delivered excerpt | resolves at `lowwater-hymn-excerpt.md:3`; map rows `grep -c '^| “' …/symbolism-clause-map.md` → **8** |
| OBS-1 option used | `grep -n 'source_id' corpus/fixtures/r87-myth-cluster/entities.json` | — | claim stays `source_id: lowwater-hymn` (delivered-text option); the `gate-witness` repoint option was **not** landed |

Both clusters (r87 and r88) replay `CLEAN` exit 0; the checker is structural
only and does not read prose, so this is not proof of source support.

## Findings & named debt

### Coverage-axis verdict: improved (bounded)

C2 landed a second sourced-mythology cluster (K'iche/Maya via Spence 1913) with
passage-level locators and a clause→element index, and repaired r87's OBS-1 by
naming the Gate in the delivered excerpt. Census 145→149, inspiration notes
1→2, both clusters exit 0. Bounds are named below; the gain is real and
non-traded.

### Sibling check — kotodama-shokunin: NOT its province (bounded pass, procedure unverified)

Rejected-fit reasoning for the NEW artifacts specifically:

- kotodama owns "the generative/coupling craft … mythic and symbolic systems …
  feeding the world bible" and "**refuses claiming or recording canon** —
  that is lore-shokunin (kotodama *hands off* systems; lore records and
  verifies them)" (`PROVINCE.md`). The Maya cluster's load-bearing surface is
  the canon-record shape exactly as `lore-shokunin/PROVINCE.md:3` defines it:
  `sources.json` (2 in-world source records), `entities.json` (4 entities with
  `claims`+`source_id`), `relations.json`, `timeline.json`,
  `contradictions.json`. The verse and register are authored *in-world
  documents attributed to in-world source IDs* — record inputs, not a
  generated system handed off.
- No kotodama system is present: no language sketch, phonology, pantheon,
  cosmology, naming pipeline, costume/era staging, or symbolic system. Two
  lines of verse plus a two-row register is fixture prose sized to give the
  checker one resolvable claim and one occupied-slot near-miss (both events at
  tick 9, distinct actors/places — a record check, not a mythic design).
- `symbolism-clause-map.md` is **not** a kotodama handoff: it indexes two
  clauses of the *cited Spence passage* to two specific authored fictional
  lines, carries an explicit limit column, and states "The comparison is not
  evidence of direct borrowing or of a general cultural meaning." kotodama's
  checklist item ("Every mythic/symbolic claim names its framework and its
  calibration status") governs generated systems; this map asserts no cultural
  rule and no canon.
- No duplicate surface exists to absorb: kotodama's `corpus/knowledge/synthesis/`
  (where its handoff contract lives) holds **0 files**
  (`ls -A …/synthesis/ | wc -l` → `0`), so there is no kotodama artifact this
  cluster could read as.
- **Residual adjacency (named debt, not absorption):** the authored verse is
  generative material living in lore's repo. Rejected as kotodama province
  because it is fixture-scale canon input, not a handoff-sized system. But the
  *procedure* by which generative material should arrive is unverifiable —
  `kotodama-shokunin/PROVINCE.md:21` cites
  `corpus/knowledge/synthesis/worldbible-integration-contract.md` as
  "load-bearing", and `test -f` → **absent**. This debt is carried from
  r87 (K2) and was named again by S3/C7/C7B; it is unchanged this round.

### Sibling check — chousa-shokunin: NOT its province (clear)

Rejected-fit reasoning for the NEW artifacts specifically:

- chousa owns "question framing; source hierarchy …; citation chaining and hop
  resolution; claim-vs-source verification; search-strategy taxonomy; the
  external-target approval table for a research window" and "**Refuses:** …
  Out of province → report, never absorb." Its SKILL's artifact surface is a
  runnable `tools/research-gate.sh` whose modes (`verify-claims`, `verify-chain`,
  `verify-sweeps`, `verify-integrity`, `verify-all`, `--pin/--drift`) emit
  `RESEARCH_GATE: CLEAN|DRIFT` against pre-registered `claims.jsonl` ground
  truth over **research records**, opening cited local sources only and never
  fetching.
- The D1 table's subject is the **world-bible record's sourced-inspiration
  fields** — which citation field, what value, how a claim maps to a delivered
  excerpt, and how real-world attribution stays distinct from in-world canon.
  That is `lore-shokunin/PROVINCE.md:3` ("sourced inspiration"), not research
  method. D1 is a Markdown decision table: no runnable mode, no gate exit
  contract, no research record, no `claims.jsonl`.
- Method overlap is real but **consumed, not owned**: D1's "fixed-string,
  line-numbered search such as `grep -nF -- 'anchor phrase' <excerpt-path>`"
  rule is adjacent to chousa's `CLAIM_SPAN_NOT_FOUND` / `verify-claims` span
  check. It is applied to in-world JSON claim→excerpt mapping inside the world
  bible — a domain surface chousa refuses ("research method only"). Precedent
  in the same file: lore's `reference-ledger.md` already lists PROV-O / JSON
  Schema / graphlib as method references *consumed*, and D1 cites
  `corpus/knowledge/seed.md:26-29` as its authority, not any chousa artifact.
  No chousa record, gate, or path is invoked by D1.
- The D3 ETCSL row: `reference-ledger.md` is lore's own pre-existing file
  (3 method rows at `dfd1fbc`). Adding a 4th row records a *real-world
  reference used by a lore fixture* — `lore-shokunin/PROVINCE.md:7` ("real-world
  reference works, cited with the art ledger's discipline"). chousa's
  "external-target approval table" is a different object (approval to research
  live targets), not a citation ledger for fictional-world fixtures. No overlap.

### Named debt carried / added (no scalar scores; verdicts only)

- **D-JCOV5-1 (carried, unchanged):** kotodama↔lore handoff contract absent
  (`kotodama-shokunin/corpus/knowledge/synthesis/worldbible-integration-contract.md`
  missing; `synthesis/` empty). The generative→canon procedure stays
  unverifiable; the boundary is declared but not written. Route formalization to
  the owning lanes, do not manufacture it lore-side.
- **D-JCOV5-2 (carried, unaddressed):** `corpus/fixtures/README.md` still has
  no `## Round 87` or `## Round 88` section — `grep -n 'Round 88\|Round 87\|r88\|r87'
  corpus/fixtures/README.md` → no matches; last section is "Round 83". This is
  the documentation sub-axis debt r87 recorded; r88 added no section for either
  round. Coverage-adjacent.
- **D-JCOV5-3 (limit, from C7B, confirmed here):** the Maya cluster delivers
  **one** distinct printed-page locator (`printed p. 209`), not three distinct
  passage locators. The two indexed clauses both sit in that one delivered
  passage.
- **D-JCOV5-4 (limit):** authored symbolic/verse material sits in lore's repo;
  legitimate as fixture canon input, but its provenance path is exactly the
  unverifiable procedure in D-JCOV5-1.
- Checker `CLEAN` is structural (schema/citations/relations/timeline) and is
  **not** evidence of prose support, canon truth, or rights.

## Handoff

- **Coverage for r88: improved (bounded)** — C2 second cluster landed and
  replayable; OBS-1 repaired via the delivered-text option; census 145→149,
  inspiration notes 1→2.
- **Sibling provinces do not claim either new artifact.** kotodama: canon-record
  surface + fixture-scale prose, no generated system, no duplicate surface
  (synthesis empty). chousa: D1 is world-bible record shape; the one
  method overlap (grep span preflight) is consumed lore-side, consistent with
  the ledger's existing method references; chousa's gate operates on research
  records, not world-bible JSON. Both are **rejected fits**, not absorbed scope.
- Integrator: carry D-JCOV5-1 (absent kotodama handoff contract) and D-JCOV5-2
  (no r87/r88 README section) into the round record as open debt; do not report
  the boundary procedure or the documentation sub-axis as closed.
- No commit, push, or registry write by this seat. Sibling repos read-only.
