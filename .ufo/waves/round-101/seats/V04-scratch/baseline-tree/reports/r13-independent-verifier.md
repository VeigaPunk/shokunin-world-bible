# Round 13 independent verifier (non-author)

## Scope and evidence

Independent replay of the checked-in checker against the checker extracted from baseline commit `97f766762ac78ab6bcf6523aadbd2ffa92d4f4f5`. The baseline was extracted with `git show` to `/tmp/r13-check-bible-97f7667.py` (SHA-256 `7caf1933f39d1103d93883448bdd0c3f066f849ffe96a6afff37b57d8f1269b3`); current checker SHA-256 at start and end: `eaa2f1178c4571d8a911cb3d880068216614766d8f35922cb78d6584179dad80`. For each fixture directory under `.shokunin/lore/corpus/fixtures/`, ran `python3 CHECKER FIXTURE_DIR`, capturing raw stdout/stderr bytes and exit status.

## Results

- Replayed all **28** fixture directories. All **26 earlier fixtures** (excluding `r13-missing-actor` and `r13-unique-actor`) match baseline byte-for-byte in stdout and stderr and exactly in exit status: 26/26. No deviations or stderr output.
- The fixture pair has exact JSON equality in `contradictions.json`, `entities.json`, `relations.json`, and `sources.json`. In `timeline.json`, after replacing only each row's `entity_id` value with a common token, the JSON structures are exactly equal. Thus event IDs/order, ticks, places, descriptions and source IDs are held fixed; actor token is the sole difference (`unlisted` vs `mira`).
- `r13-missing-actor`: baseline exit 1; current exit 1. Both retain the two dangling actor findings at `timeline[0].entity_id` and `timeline[1].entity_id`. Baseline additionally prints `VIOLATION: timeline[1]: double-booked 'unlisted' at tick 7 in timeline[0] ('harbor') and 'tower'` (3 violations); current emits no double-booked finding (2 violations). The checker output does not book this unresolved ID as a definite same-actor collision.
- `r13-unique-actor`: baseline and current stdout/stderr/exit all match. Both retain `VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'` (exit 1).
- Hashed all **139 fixture JSON files** before and after replay. Per-file SHA-256 maps are identical; hash of sorted path/hash manifest: `8f83c0ffb696d577e34cdcf88465c3747a857c6ba960ea2dbdbe830003a039f1`. Current checker hash also unchanged across this verification.

## Limits

This verifies the stated diagnostic behavior and byte-preservation scope only. Missing actor means the checker does not assess a definite same-actor occupancy collision; it does not show the events concern different actors or prove there is no real conflict. Fixture hashes show no fixture JSON was changed during this run. No checker or fixture edits were made by this verifier; only this report is written. No commit made.
