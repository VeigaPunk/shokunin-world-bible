# Round 13 executor report

## Change

In `.shokunin/lore/corpus/fixtures/check_bible.py`, changed only the occupancy guard from `if not ambiguous_actor:` to `if actor_id_count == 1:`. The count is the existing required-field-screened entity-ID count; it is not a semantic character-validity or canon-identity check. Zero-count rows still emit dangling actor findings and preserve timeline events, but skip occupancy comparison/update. More-than-one retains round-12 per-row ambiguity; exactly one retains occupancy booking. No warning was added.

## Verification

Ran the checker at baseline `97f766762ac78ab6bcf6523aadbd2ffa92d4f4f5` (extracted to `/tmp/r13-check-bible-baseline.py`) and the edited checker using `python3 CHECKER FIXTURE_DIRECTORY`.

- Existing 26 fixture directories (excluding the two `r13-*` pair fixtures): stdout bytes, stderr bytes, and exit status match baseline exactly for all 26. Stderr was empty on each. Exit statuses: 0 for `ally-reciprocal`, `consistent`, `item-chain-valid`, `r10-registry-witness`, `r8-deps-distinct`, and `r9-unique-control`; 1 for the other 20.
- `r13-missing-actor`: baseline exit 1, stderr empty; stdout has dangling `unlisted` at `timeline[0].entity_id`, dangling `unlisted` at `timeline[1].entity_id`, then `VIOLATION: timeline[1]: double-booked 'unlisted' at tick 7 in timeline[0] ('harbor') and 'tower'`, followed by `3 violation(s); no canon changed`. Edited checker exit 1, stderr empty; stdout retains the two dangling lines and ends `2 violation(s); no canon changed`, with no double-booked line.
- `r13-unique-actor`: baseline and edited checker both exit 1, stderr empty, and stdout exactly `VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
1 violation(s); no canon changed
`.

## Limits

Suppressing the missing-ID booking assertion means occupancy is not assessed as a definite same-actor collision; it does not establish that the events concern different actors or that no real conflict exists. This is only an occupancy diagnostic calibration. It makes no canon or source-truth claim. No fixtures, docs, or LOG were edited by this executor; no commit made.
