# Round 11 independent reviewer — timeline place-ID ambiguity

## Replay and focused probes

Replayed the 24 raw fixture directories with the current CLI `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture>`. Exact outputs are preserved in `corpus/live/runs/20261012T174305Z/`. The paired fixtures both exit 1 and report `entities[2].id: duplicate entities id 'harbor'` plus `timeline[0].place_id: ambiguous place entity 'harbor'`: `r11-place-character` and `r11-character-place`. Their only semantic difference is the order of the two schema-valid `harbor` entity rows; both retain the same departure `place_id`. Thus the place-reference conclusion is invariant across the tested order, while both raw rows and the duplicate-ID diagnostic remain.

Controls: `consistent` exits 0 (`CLEAN`), confirming a unique place is accepted. `r11-unique-nonplace` exits 1 with `timeline[0].place_id: not a place 'mira'`; `r11-dangling-place` exits 1 with `timeline[0].place_id: dangling entity 'unlisted'`. Other 20 outputs (all pre-r11 fixture cases) are byte-for-byte identical in stdout/stderr and exit code to the baseline checker from `git show 4337c63:.shokunin/lore/corpus/fixtures/check_bible.py`.

Additional synthetic probes against the current checker:

- Two valid rows with ID `harbor`, both kind `place`: duplicate entity ID plus `timeline[0].place_id: ambiguous place entity 'harbor'`. This supports the requested “both rows same kind” check: repeated key itself remains ambiguous, irrespective of whether kinds agree.
- A second `harbor` row missing required `name`: only `entities[2].name: required nonempty str`; it is excluded from `data['entities']`, so no duplicate-ID or ambiguous-place finding is produced. This confirms the count is among schema-valid rows, not all raw rows.
- Two distinct entity IDs with the same display name `Shared Name` and a valid unique place reference: exits 0 clean. The active checker uses IDs for references and does not impose display-name uniqueness. This is distinct from duplicate source IDs: citations (`first_appearance`, claim/relation/timeline `source_id`) resolve in the `sources` ID namespace; e.g. `r7-item-ambiguous` emits `ambiguous in-world source 'archive-ledger'`. Neither names nor source IDs are the entity key being checked here.

## Scope review

The changed branch is limited to timeline `place_id` at checker lines 230–234. `entity_id_counts` is counted from schema-valid entity rows (lines 125–127). Count >1 emits a field-local ambiguous-place finding and skips dictionary kind lookup; count 1 preserves the existing kind test; count 0 preserves the earlier dangling check. Diff from baseline contains only this local guard. This does not resolve entity identity or canon and should not be generalized to relation endpoints, timeline actor `entity_id`, provenance, occupancy, display-name homonyms, or citation/source truth. The checker verifies structure and ID resolution, not that cited source prose supports a claim.

## Verdict

The specific calibration claim is supported: a timeline place reference no longer gets a last-row-wins kind conclusion when multiple valid entity rows share its ID, and the tested permutation yields the same ambiguity finding. No harm observed in the 20 prior fixture outputs or unique-place/non-place/dangling controls. This is evidence for the narrow rule only, not proof that every entity-ID consumer handles duplicates consistently or that either harbor row is canonically correct.
