# Round 64 lore scribe — rejected-row ID status

## Decision
**GO, narrowly, as a calibration hypothesis for a matched probe; not as a change or claim of admitted benefit.** A successfully parsed entities array containing an excluded schema-invalid row with a usable nonempty string `id` means the raw array did contain that identifier, but current valid-entity index membership cannot decide whether a reference is dangling. Treating it as certainly absent overstates what the filtered index establishes. Any proposal must preserve the row schema error and mark the reference indeterminate; the malformed row must never resolve identity, kind, holder/place/faction, or occupancy. This is not evidence that a fictional entity exists.

## Observed behavior / decision table
Checker `.shokunin/lore/corpus/fixtures/check_bible.py:65-76` sets `valid=False` for a missing/wrong/blank required field and appends only valid rows to `data`; `:78-95` indexes only that filtered data and counts valid IDs. Yet `entities_available` is set from successful array loading at `:58-63`. Thus references consult an available-but-filtered index: relation endpoints `:161-169`, timeline actor/place `:270-284`, provenance holders `:203-224`, plus faction/occupancy-dependent logic.

| Input state for referenced ID X | Current checker behavior | Safe interpretation / proposal |
|---|---|---|
| One valid X row | count 1; resolves subject to existing downstream checks | valid unique row; normal checks |
| No X row in loaded array | count 0; `dangling entity` (for provenance: `dangling entity`) | definitely absent from supplied raw array; retain dangling |
| Invalid row with usable nonempty string `id: X`, no valid X row | row-local schema error, filtered out; count 0; reference reports dangling | **proposal:** retain schema error and report local cannot-assess/matching invalid row, not dangling; do not resolve X or include it in any semantic check |
| Invalid row without usable string ID | row-local schema error; no X match; reference is dangling | retain dangling for X; no basis to associate malformed row |
| Valid duplicate X rows | both admitted, count >1; duplicate error; endpoint ambiguous; provenance suppresses chain; timeline ambiguous and no comparable place | keep ambiguity; invalid rows cannot alter duplicate count or disambiguate |
| entities file unavailable/unparseable/non-array | availability false, loader/schema diagnostic; entity-reference checks gated | unavailable is distinct from loaded empty; do not apply row-local proposal |

The raw distinction is directly visible in the loader/filter/index code above; I did not run new temporary fixtures or claim output traces beyond source inspection. The proposed indeterminate status should be local to each affected reference, preserve repair pointers (the bad row's location/field and the reference path), and leave independent source, tick, dependency and schema checks intact.

## Calibration case and falsifier
Material hypothesis: a user reading `dangling entity X` reasonably receives a stronger signal than “no valid indexed row”; when the same loaded array contains an invalid row explicitly carrying X, that signal is misleading and can direct repair toward inventing/adding an entity instead of fixing the rejected row. Prior round 60 explicitly accepts this limitation; this is a distinct state within the loaded-array branch, not another unavailable-file rule.

Precise falsifier: compare byte-matched fixtures differing only in entity rows: valid X; no X (loaded empty/other rows); invalid X (usable ID, one required field missing/invalid); invalid row with no usable ID; valid duplicate X; unavailable entities file. Reference X through relation endpoints, timeline actor and place, and provenance holder; include alliance-kind/occupancy controls. GO is falsified if invalid-X is not distinguishable from absent-X in raw parsed input, if proposal lets invalid X qualify/resolves its kind or holder/place, changes duplicate semantics, masks true dangling without a repair pointer, breaks existing empty/unavailable distinctions or independent findings, or if paired operator review finds the local “cannot assess” line no more actionable than dangling. Require non-author replay and old-output regression check before admission.

## Prior-art and harms
R16–18 established narrowly scoped withholding for unresolved/ambiguous valid IDs (place comparisons, duplicate place occupancy), not malformed rows. R60 separated unavailable from loaded-empty/partial, while expressly retaining lookups over valid rows when some entity rows are rejected. R56 showed that accurate extra local paths can fail materiality when a global finding already guides the operator; that is a direct warning here. Suppressing dangling could conceal a genuinely absent reference or duplicate-ID ambiguity, and adds a status category; a local invalid-row pointer may instead improve repair targeting. Evidence must show net operator benefit, not merely logically correct uncertainty.

No checker, fixture, README, or LOG was changed. No world/canon/source-truth/rights claim is made.
