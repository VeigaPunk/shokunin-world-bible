# Round 61 loader-scout — source-table availability

## Independent verdict: GO, narrowly, for calibration investigation

The current checker conflates a failed `sources.json` load with a successfully loaded empty source array for referential lookup, although it preserves a file error. This causes downstream `unknown in-world source` assertions without an available source index. A source-only availability distinction is a plausible material calibration improvement, but must be tested against loaded-empty, loaded-partial, and duplicate/ambiguous controls; this scout recommends no implementation based on this probe alone. Do not extend the r60 entity policy by assumption.

## Observed code and callers

In `.shokunin/lore/corpus/fixtures/check_bible.py`:
- `:35-57` loads each table, catches duplicate-member/OS/Unicode/JSON errors, records an error and substitutes `[]`; non-array input also becomes `[]`. Unlike entities (`:38,55-56`), no `sources_available` flag exists. Valid rows are screened at `:58-69`.
- `:79-82` builds source index/counts from accepted source rows; `:90-100` maps count 0/1/>1 to unknown/unique/ambiguous and `source()` emits missing/ambiguous citation findings.
- Source lookup callers: contradiction ledger event-source checks `:103-127`; entity first-appearance and claim citations `:133-143`; relation citations `:149-157`; item provenance citation and chain eligibility `:213-225`; timeline citations `:257-273`. These are all source-index-dependent. The event ledger emits a separate `no resolvable source_id` on zero (`:122-126`); ambiguity delegates to `source()`.
- Allied reciprocity at `:237-255` uses `source_status(candidate['source_id']) == 'unique'` for the reciprocal witness, in addition to the relation's ordinary `source()` call at `:157`. With unavailable sources, that predicate currently evaluates false and can produce a collateral “lacks a sourced reciprocal” diagnostic. Whether to suppress that conclusion is an explicit dependent-check policy question.
- Checks not depending on source index include table/row shape and ID duplication, entity kind, event pointers/fields/claim distinction, provenance record shape/holder checks and source-independent structure where eligible, relation entity endpoints, timeline entity/place/occupancy checks, and event dependency/ordering rules. Preserve these on source load failure.

## Direct temporary probe (observed current behavior)

I copied `fixtures/consistent` to `/tmp/r61-loader-scout-ef514b_e/{missing,empty,partial,ambiguous,malformed}` and ran the active checker. No repository input was changed. `consistent` has 11 references to two source IDs (`courier-log`, `archive-ledger`).

- Missing `sources.json`: exit 1, one file load error plus 11 `unknown in-world source` findings; 12 total.
- Malformed JSON `sources.json` (`{bad`): same 11 unknown findings plus JSON parse error; 12 total.
- Loaded empty `[]`: exit 1, 11 unknown findings, no loader error.
- Loaded partial `[]` (the probe accidentally used empty, not a filtered valid subset): same as empty; this does **not** establish partial-table behavior.
- Ambiguous probe duplicated the `archive-ledger` row: exit 1, duplicate ID plus four `ambiguous in-world source 'archive-ledger'` findings; sole `courier-log` references remain unique. This confirms loaded duplicate distinction but does not test allied reciprocity or ledger consumers.

Thus the evidence establishes unload-vs-empty output convergence only for the ordinary direct citation callers exercised in `consistent`; it does not establish ledger-event or allied reciprocal collateral in execution. It is preliminary, and the mislabelled partial control is a limitation to fix before admission.

## Prior art, falsifier and risk

R5 loader scout documents a different table (`entities.json`) failing into dangling-reference cascades; r60 explicitly admitted an entity-only availability gate and warned not to generalize to source/timeline tables. R31/r32 reports establish source multiplicity and malformed-row screening; they distinguish retained valid rows from excluded malformed rows. R39 covers a missing source ID in a uniquely identified contradiction event, not an unavailable source table. These make the present hypothesis testable, but do not show that source-table unavailability itself has already been calibrated.

Concrete falsifier: with four non-source tables byte-identical, malformed/missing source table should retain its actionable load error and independent checks but not claim citations are unknown solely because the index failed; loaded `[]` must retain unknown findings; loaded partial must resolve IDs in retained valid rows and call only absent IDs unknown; duplicated IDs must remain ambiguous. Test direct citations, ledger event-source branch, provenance behavior and allied reciprocal witness. Reject if the proposed suppression hides loaded-empty/missing-ID results, removes independent checks, or produces misleading “clean” status without a clear load error. Suppressing the allied reciprocal finding may lose useful triage; retaining it says only that no uniquely sourced reverse row was found, but current phrasing can be read as a substantive absence. A narrower alternative is explicit “unassessable due to unavailable sources” rather than silent suppression, at a verbosity cost.

## Boundary

Observed facts are checker input/index behavior only. A source ID establishes referential membership in the supplied table, not that its text supports a claim, that the source is authentic/reliable, or that an event occurred. No source-text/canon inference, rights, license, or permission follows. No code, fixtures, README, LOG, or commit changed; only this requested report is written.
