# Round 61 non-author reviewer — source-index availability

## Verdict

**PASS — material new calibration, narrowly scoped to unavailable `sources.json`; no-go for any broader suppression.** The changed output corrects a real status conflation: an unavailable source index is not a successfully loaded empty index. Matched controls demonstrate a meaningful distinction while preserving loaded-empty/partial/ambiguous conclusions and independent checks. The principal cost is loss of affected-reference repair pointers; I judge the retained actionable loader error and sharply bounded behavior acceptable here, while noting this is a real usability tradeoff.

Axes: **calibration improved materially**; depth and coverage **unchanged**. Falsifier: reject if any loaded-array results change, unavailable inputs are called clean/resolved, or independent checks disappear. Current fixture controls pass those tests. The old-corpus replay still needs independent non-author validation before shipping; reviewer PASS is not that replay.

## Evidence and controls

Read the r61 declaration/LOG, pair/critic/simplifier/citation and executor reports, checker and README diff, and all twelve `r61-*` directories. Current checker outputs were executed directly with Python. The six controls against `consistent` (`r61-direct-unavailable`, `-empty`, `-partial`, `-ambiguous`, `-malformed`, `-nonarray`, plus duplicate-member) each contain exactly five JSON files; all four non-source tables are byte-identical to `consistent` in every case.

- Loaded empty emits the expected 11 unknown-ID findings. Loaded partial retains the one source and emits seven findings only for missing `courier-log`. Loaded duplicate valid ID preserves duplicate plus four ambiguous-reference findings. These controls falsify a policy that treats loaded arrays as unavailable or erases loaded membership results.
- Malformed JSON, non-array and duplicate-member inputs each retain their direct load/shape diagnostic and withhold the 11 source membership conclusions. This is not CLEAN: each exits 1. The duplicate-member test itself is syntactically valid JSON but rejected by the duplicate-key loader.
- Independent-unavailable/empty pair has byte-identical other four tables. Unavailable output retains the source load error, provenance wrong-kind and both dangling-holder errors, negative timeline tick, and unknown dependency (six total). Empty retains those same independent five findings plus its expected unknown source references. Thus chain/source membership-dependent checks are withheld without skipping these independently structural faults.
- Allied unavailable/empty pair likewise shares other four tables byte-for-byte. Empty emits five unknown IDs plus missing sourced reciprocal; unavailable emits only the loader error. With no reciprocal in the fixture, the latter avoids asserting the source-gated absence from an uninspectable index; it does not infer a reciprocal or a valid alliance.
- Ledger-unavailable retains the load error plus missing event pointer, dangling relation endpoint, timeline inversion, and double-booking (five total). This verifies useful ledger/timeline checks survive. It does not separately probe every ledger status branch.

The executor’s initial independent fixture was not actually unavailable. Parent correction replaced only its `sources.json` with malformed JSON; current bytes and output now confirm the corrected case. This provenance defect is candidly disclosed and means I rely on the corrected present fixture, not the original reported run.

## Scope and risks

Code marks availability only after a top-level array parses; valid `[]` is available, and an array with rejected malformed rows remains available over admitted rows. `source_status()` returns `unavailable`, and direct reporter emits no membership conclusion in that state. The ledger’s zero-match branch is suppressed only when sources are unavailable. Provenance still validates record shape, holders and tick; chain comparison is disabled when unavailable because source resolution is required to call it sourced. This is coherent with the stated contract. A source citation string’s own malformed shape and other table structure still receive their checks.

Existing r39 controls were replayed: `r39-ledger-source-missing` (loaded source table) still reports ledger “no resolvable source_id” and timeline unknown source; the unique control remains CLEAN. So the established loaded-zero-match ledger behavior is not erased. This is an availability calibration, not a new rule that missing source IDs are acceptable.

Affected-reference lines are valuable repair pointers and their loss is the main harm; the README says so and directs repair via loader error then rerun. This does not fully tell a user which rows need rechecking. On balance, these cascades can misleadingly assert unknown/unsourced status as if a complete lookup occurred. In particular an unavailable index cannot establish no resolvable ledger source or prove a reciprocal is missing. The narrow suppression is preferable, provided the primary load error remains visible and no output suggests success.

Potential boundary: report wording says “does not infer … sourced provenance-chain certainty.” The code disables chain checks when sources unavailable rather than rendering an explicit per-chain unassessable line. This is acceptable as scoped absence of an unsupported sourced conclusion, but users must not mistake it for a verified chain. No evidence here establishes what cited source text supports, fictional-world source existence/absence, event truth, chronology, canon, authorship, rights, license, or permission.

## Required next check

The executor reports a claimed 103/103 old fixture raw stdout/stderr/exit tuple replay and 514/514 old JSON byte identity, but raw tuples were not archived and this leaf did not independently rerun the pinned HEAD comparison. Require an independent verifier to replay and enumerate deltas before admission to ship. No other material calibration falsifier was found in the current matched controls.
