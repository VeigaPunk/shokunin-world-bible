# Round 60 executor report

Implemented entity-index availability gating in `corpus/fixtures/check_bible.py`. Entity-table availability is true only when `entities.json` is successfully decoded and has a list top level; invalid/missing JSON (including duplicate-member rejection) and non-arrays remain unavailable, while `[]` and valid partial arrays are available.

Unavailable entity index now suppresses entity-reference dangling/ambiguity/kind and derived relation/alliance/occupancy conclusions. Source checks on relations/timeline, timeline tick and dependency checks, and normal schema checks continue. Provenance loops naturally have no valid entity rows to process when full-file parsing fails. No source/timeline availability behavior was generalized.

Added `r60-unavailable`, `r60-empty`, and `r60-partial` fixture directories. **Parent correction below:** the initial unavailable variant also had independent timeline faults; it was split into a matched `r60-unavailable` and a fourth `r60-unavailable-independent` fixture before non-author review. Added the policy and limits to fixture README.

## Exact candidate outputs

The three fixture runs all exited 1:

- `r60-unavailable`: `entities.json: cannot load JSON: Expecting property name enclosed in double quotes: line 1 column 3 (char 2)`; `timeline[0].tick: must be nonnegative`; `timeline[1].source_id: unknown in-world source 'absent'`; `timeline[1].depends_on: unknown event 'missing'`; `4 violation(s); no canon changed`.
- `r60-empty`: dangling `relations[0].from` mira, `relations[0].to` seal, timeline 0 entity mira/place harbor, timeline 1 entity mira/place tower; `6 violation(s); no canon changed`.
- `r60-partial`: dangling `relations[0].to` seal and both timeline place IDs harbor/tower; `3 violation(s); no canon changed`.

Active old-fixture replay against the HEAD checker: **99/99** pre-existing fixture directories, exact `(exit, stdout, stderr)` comparison; only `r59-nested-duplicate` changed. Its current output is the retained duplicate-member load diagnostic and `1 violation(s); no canon changed` (exit 1), versus the prior six dependent dangling findings and total 7. This is the intended entity-unavailability delta. New fixture controls were also run under the previous checker: empty and partial outputs are unchanged; unavailable still showed dangling IDs under prior behavior.

Replay limit: this was a direct active-fixture replay against the checker at HEAD, not a pinned archival comparison of every corpus JSON byte/path or a broader external test suite. No fictional absence, source truth, canon, or rights conclusion follows. No unrelated files were changed by intent.

## Parent integration before non-author review

The initial executor `r60-unavailable` had three independent timeline faults not present in `r60-empty` and `r60-partial`, so it was not a matched table-state comparison. Parent split it: `r60-unavailable` now has the **same four non-entity tables** as empty/partial, while the original faulty timeline is preserved in a fourth fixture, `r60-unavailable-independent`. Initial four-violation output above refers to the latter current fixture, not the corrected `r60-unavailable`. Current exact outputs were rerun as follows; the matched unavailable fixture exits 1 with `VIOLATION: entities.json: cannot load JSON: Expecting property name enclosed in double quotes: line 1 column 3 (char 2)` and `1 violation(s); no canon changed`; the independent fixture exits 1 with the original four violations. Both have empty stderr. Existing 99-case replay claim is unaffected by new fixture layout; non-author pinned replay remains required.
