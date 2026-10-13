# Round 85 — independent Sol axis adjudication

**Verdict: ADMIT — calibration improved (bounded); depth unchanged; coverage
unchanged; no axis harmed.** The admitted object is a *checker-defect
discovery*, not a checker or fixture change: a demonstrated silent-latch
masking defect in `check_bible.py` provenance holder handling, isolated by a
strict matched pair and shown operatively dangerous by a sealed non-author
operator. Adjudicated at pinned work commit `0b45095c`
(`lore r85: masked provenance diagnostic evidence (author+verifier+sealed)`);
working tree clean, branch `craft/lore-r1` untouched. No corpus, checker,
fixture, README, LOG, or SCORECARD edit was made by this adjudicator; this
report is the only file written.

## What I independently verified (not trusted)

### Mechanism — direct read of `.shokunin/lore/corpus/fixtures/check_bible.py`

- L212-214: `to_holder` count==0 → `dangling entity` diagnostic + `valid=False`.
- L215-216: `to_holder` count>1 → `valid = False` with **no appended error**.
- L217-224: `from_holder` symmetric — count==0 voices `dangling entity`
  (L220-222), count>1 sets `valid=False` silently (L223-224).
- L234-237: any `not valid` record resets `previous_holder`/`previous_tick`
  AND latches `can_check_chain = False` before `continue` — chain comparison
  is disabled for **all later records of that item**, not just the offending
  record.
- L238-243: the chain-break comparison runs only under `can_check_chain`.
- Contrast sweep: every other `valid=False` path in the same loop emits a
  diagnostic (tick type L203-205, nonempty-holder gates L206-211, dangling
  L212-214/L220-222, source gate L225-233 via `source()` which itself appends
  `unknown`/`ambiguous in-world source` at L103-109). The two holder count>1
  branches are the **only** silent invalidations. Every other ambiguity site
  in the checker reports locally: sources L107-108, relation endpoints
  L167-168, and (per the verifier's read, consistent with the README'd rules)
  timeline actor/place and dependency sites.
- README L112-115 promises ambiguous duplicate IDs "are not silently
  interpreted as a valid chain" — satisfied in the letter (the record is
  invalidated, exit 1) but the silent *invalidation* and the downstream
  assessment latch are undocumented; nowhere does the text disclose that a
  duplicated holder suppresses the rest of that item's chain findings.

### Matched pair — run and diff myself, stdout/stderr separated

All runs `python3 .shokunin/lore/corpus/fixtures/check_bible.py
.shokunin/lore/corpus/live/runs/round-85/probe-inputs/<name>`:

| probe | my exit | my stdout |
|---|---|---|
| `r85-control` | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` |
| `r85-isolated-ambiguous` | 1 | `entities[5].id: duplicate entities id 'vault'` only |
| `r85-masked-ambiguous` | 1 | `entities[5].id: duplicate entities id 'vault'` only — the `provenance[2]` break produces **no line anywhere** |
| `r85-unique-break-control` | 1 | `entities[3].provenance[2]: provenance chain break; expected from_holder 'vault', got 'harbor'` only |
| `r85-harbor-repro` | 1 | `entities[4].id: duplicate entities id 'harbor'` + `timeline[0].place_id: ambiguous place entity 'harbor'` |

stderr empty in all five. Each output matches the recorded
`probe-r85-*.txt` files and both reports byte-for-byte.

- `diff` masked vs unique `entities.json` → `81,92d80`: exactly **12 lines**,
  one byte-identical second `vault` place object. `cmp -s`: the other four
  files (`relations`, `sources`, `timeline`, `contradictions`) byte-identical.
- Parsed both files: identical `seal` provenance in each —
  `(null→mira, t0)`, `(mira→vault, t3)`, `(harbor→tower, t4)`; `vault` id
  count is 2 in masked/isolated, 1 in unique control. `vault` appears **zero**
  times in timeline/relations/contradictions of every probe — its only
  consumer is the provenance holder field, so the masked pair is
  collateral-free: no voiced `ambiguous entity` line can fire elsewhere.
- `r85-harbor-repro` byte-matches the old-checker output Sol recorded in
  `reports/r56-axis-adjudicator.md` L16-18 — the falsifier's "exact old-case
  replay" prong is satisfied by observation, not claim.

### Baseline preservation

- `sha256sum` worktree checker = `git show 596f70e4:...check_bible.py` =
  `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81` — identical.
- `git diff --name-status 596f70e4 HEAD -- .shokunin/lore/corpus` → **164
  entries, all `A`** (round-85 run artifacts); zero modified/deleted. The
  1,368 pinned corpus files are untouched; additive telemetry only.
- Independent full replay: all **133** fixture dirs → **28 exit0 / 105
  exit1, stderr empty for every run** — matches the verifier's tuple counts
  and the r84 pin exactly.

### Non-author evidence

- Verifier (`r85-verifier.md`): five mechanical claims, zero disagreements;
  my independent runs reproduce every one.
- Sealed reviewer (`r85-sealed-reviewer.md`): blinded first repair on the
  masked output was dedup of `entities[5]` — mechanically correct but with a
  sealed defect model of "exactly one defect" that was **wrong** (the file
  carries two defects). The honest divergence: the mask did not redirect the
  first *action* (dedup is a prerequisite to detection either way); it
  falsified the *stopping point* — under single-pass trust the injected
  chain break ships as "clean". The reviewer's unsealed mechanism read
  (L157-159 counts, L212-216/L220-224 silent branches, L234-237 latch,
  L238-243 gate) matches my own.

## Per-axis disposition

- **depth: unchanged.** Probe inputs are invented test JSON under
  `corpus/live/runs/`; no fictional claim, source interpretation, custody,
  canon, chronology, rights, or mechanics content is added or asserted.
- **coverage: unchanged.** No checker, fixture, or README change; the five
  probe dirs are run telemetry, not active fixtures. Per r56 Sol: fixture
  and output counts are not axis gain. The 133-fixture active set and all
  pinned tuples are preserved.
- **calibration: improved (bounded).** The discovery corrects the lane's
  operative model of checker output. Before this round the documented rule
  was only that ambiguous holders are "not silently interpreted as a valid
  chain" (README L113). Demonstrated now: an ambiguous holder (a) emits no
  local finding — the field path is invisible — and (b) latches
  `can_check_chain` off, so a `N violation(s)` summary where all findings
  are entity-index defects is indistinguishable between "chain assessed
  clean" and "chain assessment silently stopped at record [k]". The masked
  pair proves this is not merely a missing label (the r56 case, where the
  chain was continuous and only field-local annotations were absent): a
  real defect that the checker reports verbatim under a unique holder is
  **entirely absent** under an ambiguous one. The sealed reviewer supplies
  the falsifier's operative prong — a blinded non-author operator formed a
  materially wrong defect model (one defect, file clean after dedup) from
  the masked output alone. That is an "otherwise mistaken interpretation"
  shown, per the r56 falsifier's action/interpretation disjunct.
  Calibration is the right axis: the gain is knowledge of what checker
  output does and does not guarantee, demonstrated operatively — not new
  corpus coverage and not lore depth.

### Why this clears the r56 REJECT where r56 itself did not

r56 was rejected on *materiality*: both holder records were already
invalidated, the withheld comparison hid nothing real, and no consumer task
showed changed diagnosis — "the sole candidate also lacks directional
isolation and has timeline collateral" (r56 Sol). r85 answers each clause:
`r85-isolated-ambiguous` is collateral-free and direction-isolated (vault's
only consumer is `provenance[2].to_holder`); `r85-masked-ambiguous` vs
`r85-unique-break-control` is a strict matched pair showing a *real*
downstream defect fully masked, not merely unlabeled; `r85-harbor-repro`
replays the old case byte-identically; and a sealed operator misread the
masked output in exactly the predicted way. The materiality gap is closed:
what was withheld in r56 was a label; what is withheld here is a defect.

## Bounds on the gain — stated, not smoothed

- The mask did **not** change the sealed reviewer's first physical action;
  dedup is prerequisite to detection under any output. The demonstrated harm
  is a false sense of finality, operative only under single-pass trust — a
  mandated re-run-after-repair protocol neutralizes it. Whether the lane's
  repair protocol mandates re-check is an open UNKNOWN (flagged by the
  reviewer); this bounds but does not void the calibration gain, since the
  output still under-counts defects and offers no "unassessed, not
  disproved" marker where every other ambiguity site voices one.
- The defect pair is constructed; no admitted corpus file exhibits the mask.
  Probes are telemetry: they calibrate output semantics, they do not claim
  the defect occurs in real data.
- The `from_holder` silent branch (L223-224) is symmetric in code but
  unexercised by this pair.
- The seal is self-attested inside the reviewer report (step 2 written
  before unsealing, artifacts listed as unread); internally consistent and
  consistent with the wave structure, but not independently auditable by me.

## Checker repair and r86

Admission does **not** require a checker fix now. Precedent: r83 admitted a
calibration finding with no checker edit (SCORECARD row only); r84 rejected
with no changes. The admitted value here is the demonstrated knowledge; the
natural r86 move — a repair candidate adding a local `ambiguous entity`
finding at the L215/L223 holder branches (the r56 diagnostic now backed by
demonstrated materiality), plus a design decision on whether the per-item
`can_check_chain` latch should persist silently or voice an "assessment
stopped" marker — is a **separate candidate** requiring its own wave:
a mandatory replay of all 133 pinned tuples plus the probes, since any new
diagnostic could shift baseline tuples (author's UNKNOWN stands; expected
none today because no active fixture combines provenance with a duplicated
holder, but that is unverified for a built candidate). Admitting the
discovery now, unremediated, is the correct Pareto move; conflating
discovery with remediation would either delay the finding or admit an
unverified checker change.

## Reopen conditions

- A second sealed non-author operator under the same seal who, given only
  the masked output, would *not* have certified the file clean (e.g.,
  treats any violation list as inherently incomplete and re-runs) — narrows
  the operative prong to informational, though the mechanical defect stands.
- Evidence the seal was breached (author/verifier artifacts read before the
  recorded step-2 answer): voids the operative prong; mechanical prong
  survives on my own runs.
- A built repair candidate that changes any of the 133 pinned tuples or adds
  misleading collateral — judged on its own merits in that round.
- Discovery of a third silent `valid=False` path, or evidence the
  `from_holder` branch behaves asymmetrically — widens the defect class.

## Admission summary

**ADMIT.** Calibration improved (bounded, as stated); depth and coverage
unchanged; no axis harmed. Value admitted: demonstrated, isolated,
operatively confirmed knowledge that provenance holder ambiguity in
`check_bible.py` is silently invalidating and silently disables the
remainder of that item's chain assessment, so a short violation list can
mask a real, separately reportable provenance break. Parent may record the
closure, add the calibration SCORECARD row, and commit report-last per
lane protocol. No canon, custody, source-truth, rights, or mechanics claim
is made or implied.
