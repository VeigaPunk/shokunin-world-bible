# Round 85 — author lane report (host: devin)

## Candidate considered

**Reopen of the round-56 falsifier: field-local `ambiguous entity` diagnostic at
provenance holder references.** `check_bible.py` validates `entities[i].provenance[j]`
holders (`.shokunin/lore/corpus/fixtures/check_bible.py` lines 205-224): a
`to_holder`/non-null `from_holder` resolving to **zero** admitted entity rows emits a
local `dangling entity` finding, but one resolving to **more than one** sets
`valid = False` with **no diagnostic** and silently disables chain comparison for all
later records of that item (`can_check_chain = False`). Every other ambiguity site in
the same checker reports locally: sources (line 108), relation endpoints (167-168),
timeline actor (279), place (281), dependency (313). Round 56 built this exact
two-line diagnostic plus a duplicate-`harbor` fixture; the non-author reviewer
**FAIL**ed materiality and Sol **REJECT**ed, leaving a falsifier
(`reports/r56-axis-adjudicator.md` line 41):

> a schema-admitted, collateral-free, independently isolated holder-reference case
> and a concrete operator task showing that reference-local location changes an
> otherwise mistaken action/interpretation; exact old-case replay still necessary.

This lane tested whether those preconditions are constructible and what raw outputs
show. It is an **author evidence package, not an admission claim**: the
operator-task prong requires a non-author sealed wave this lane cannot run.

## What ran

Baseline (byte-exact, manifest: `corpus/live/runs/round-85/manifest.txt`):

- HEAD `3f601981b1a28299c0b5498d6070584f26de3428`; `git diff --stat 596f70e HEAD --
  .shokunin/lore/corpus` empty → the pinned 1,368-file corpus is unchanged.
- Checker sha256 `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81`
  (same as r83/r84).
- All **133/133** fixture dirs replayed root-relative into
  `corpus/live/runs/round-85/<fixture>.txt`: **28 exit0 / 105 exit1**, all stderr
  empty — matches the r84 verifier's pinned tuple counts exactly.

Probes (`corpus/live/runs/round-85/probe-inputs/`, each an `item-chain-valid` clone;
the four non-entities files are `cmp -s` byte-identical; only `entities.json`
differs; outputs in `probe-<name>.txt`):

| probe | seeded difference | raw result |
|---|---|---|
| `r85-control` | none | exit0 `CLEAN` |
| `r85-harbor-repro` | duplicate `harbor` row (r56 case) | exit1, 2 violations: `entities[4].id: duplicate entities id 'harbor'` + `timeline[0].place_id: ambiguous place entity 'harbor'` — byte-matches the old-checker output Sol recorded |
| `r85-isolated-ambiguous` | duplicate `vault` row; `vault` consumed **only** by `provenance[2].to_holder` | exit1, **1** violation: `entities[5].id: duplicate entities id 'vault'` only — zero findings at any provenance record, no timeline/relation collateral |
| `r85-masked-ambiguous` | duplicate `vault`; `provenance[1].to_holder = 'vault'` (ambiguous); `provenance[2].from_holder = 'harbor'` (real continuity break) | exit1, **1** violation: `duplicate entities id 'vault'` only — the real `provenance[2]` chain break is **entirely absent** from output |
| `r85-unique-break-control` | same provenance as masked; `vault` **unique** | exit1, **1** violation: `entities[3].provenance[2]: provenance chain break; expected from_holder 'vault', got 'harbor'` |

Masked vs unique `entities.json` differ by exactly 12 lines — one duplicated `vault`
object; provenance records identical. `r85-harbor-repro` output shows the asymmetry
in a single run: the timeline site reports `ambiguous place entity 'harbor'` while
the two provenance holder references to the same duplicated ID report nothing.

## Byte-exact evidence

1. **Falsifier prong 1 (collateral-free isolation) is constructible.**
   `r85-isolated-ambiguous`: `vault`'s only consumer is a provenance holder field.
   Current output = one global duplicate-ID finding, nothing else; the ambiguous
   reference site and the silently skipped chain assessment are invisible. Under the
   r56 candidate this case would add exactly one line
   (`entities[3].provenance[2].to_holder: ambiguous entity 'vault'`) with no
   violation-count doubling and no unrelated collateral — the direction-isolated,
   collateral-free case r56 lacked.
2. **New mechanism beyond r56: a real downstream defect is masked, not merely
   unlabeled.** `r85-masked-ambiguous` vs `r85-unique-break-control` is a strict
   matched pair: identical provenance, identical discontinuity at `provenance[2]`;
   only the entity count differs. Unique holder → the break is reported at its exact
   path. Ambiguous holder → the checker reports a *different* violation
   (`duplicate entities id 'vault'` at `entities[5].id`) and the break produces no
   line anywhere. An operator reading the masked output sees 1 violation naming an
   entity-index defect and cannot distinguish "chain assessed clean" from
   "chain assessment silently stopped at record [1]" from output alone — the
   `unassessed, not disproved` state the lane documents everywhere else has no
   output marker here.
3. r56 reproduction is byte-identical to Sol's recorded old-checker output,
   confirming this lane's baseline matches the pinned archive behavior.

## Per-axis verdict claim (author, provisional — no verdict marked)

- **depth: unchanged.** Probe inputs are invented test JSON, not admitted lore;
  no fictional claim, source, or canon content added.
- **coverage: unchanged.** No checker/fixture/README change; probes under
  `live/runs/` are telemetry, not active fixtures (per r56 Sol: fixture/output
  counts are not axis gain).
- **calibration: potentially improved — UNPROVEN by author evidence.**
  The masked-break pair demonstrates a mechanically real reporting gap that the
  r56 case did not isolate: the silent ambiguity gate hides a defect that is
  reported when the holder resolves. But the falsifier's second prong — a
  *demonstrated* operator action change (a non-author operator shown to misread
  the masked output and to act differently with the local finding) — is not
  satisfiable by author-run evidence.

## UNKNOWNs

- Whether a non-author operator actually repairs differently given the local
  ambiguity line (the falsifier's operative prong). The masked pair supplies the
  *mechanical* precondition; the misreading must be shown by the sealed-reader wave.
- Whether the r56 materiality objection still prevails: the same first repair
  (resolve the duplicate ID) is required either way, and a rerun after dedup
  surfaces the break anyway — the marginal gain is knowing where assessment
  stopped on the first pass.
- Whether extending the local finding changes any of the 133 baseline tuples
  (expected none: no current fixture has provenance + duplicate holder; a
  candidate replay would still be mandatory).
- Whether the two seeded defects in `r85-masked-ambiguous` are dismissed as
  over-constructed; the isolated variant exists separately to bound that objection.

## Recommendation and limits

If the fleet spends a wave, the operator task should present `r85-masked-ambiguous`
output (1 violation, `duplicate entities id 'vault'`) to a sealed non-author
operator and ask for the first repair; the falsifier is satisfied only if the local
`ambiguous entity` line changes that action/interpretation versus the duplicate
finding alone. Probe inputs are invented test rows — no source-text truth, custody,
canon, chronology, rights, or mechanics is established or claimed. No corpus
baseline file, checker, README, LOG, SCORECARD, or verdict was modified; all
artifacts are additive under `corpus/live/runs/round-85/` and this report.
