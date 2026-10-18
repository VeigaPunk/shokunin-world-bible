# Round 13 scribe — actor-count decision table and README proposal

Scope: documentation recommendation only. No checker, fixture, README, or shared file was edited. This note distinguishes observed behavior from the round-13 proposed calibration. Actor count means schema-valid entity rows indexed by the timeline `entity_id`, not textual names or proof of canon identity.

## Observed raw evidence

- Baseline declared in `.shokunin/lore/LOG.md` round 13 is report commit `97f766762ac78ab6bcf6523aadbd2ffa92d4f4f5`; its round-12 occupancy guard handles only counts greater than one.
- Current checker source `.shokunin/lore/corpus/fixtures/check_bible.py`, lines 225–251, first reports dangling entity when `row['entity_id'] not in entities`, computes `entity_id_counts.get(..., 0)`, treats only `> 1` as ambiguous, and otherwise adds/compares `(entity_id, tick)` in `occupied`. Thus count zero currently reaches occupancy too.
- Repo-root CLI probe (current checker): `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r12-unique-actor` printed the tick-7 `double-booked 'mira'` finding and exited 1. The same command with `r12-ambiguous-actor` printed duplicate-ID plus two local ambiguous-actor findings, no `double-booked`, and exited 1. These committed pair fixtures establish unique vs duplicate behavior, not zero-count behavior.
- Zero-count probe made a temporary copy of `r12-unique-actor` under `/tmp/lore-r13-scribe-81n4or1m/absent`, changed both timeline `entity_id` values to `unlisted`, and ran `python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/lore-r13-scribe-81n4or1m/absent`. Output: two `dangling entity 'unlisted'` findings plus `double-booked 'unlisted' at tick 7 ...`; exit 1. This was an ephemeral probe, not a committed fixture or persisted raw run artifact.

## Bounded decision table

| Schema-valid entity rows for actor ID | Current behavior observed from source/probe | Round-13 recommendation | Scope note |
|---:|---|---|---|
| 0 | Dangling `entity_id`; still participates in occupancy key; different places at same tick can produce `double-booked` (temporary raw CLI probe above). | Keep dangling finding and raw timeline row; do not compare/update occupancy for this unresolved ID. | Withholding a definite same-actor diagnostic does not mean different actors or no real conflict. |
| 1 | Normal occupancy comparison/update; distinct places for that ID and tick can produce `double-booked` (`r12-unique-actor`). | Preserve exactly. | Existing narrow same-ID/same-tick convention only. |
| >1 | Duplicate entity-ID finding plus local `ambiguous actor entity` on event rows; no occupancy comparison/update (`r12-ambiguous-actor`). | Preserve exactly. | Duplicate rows may or may not describe one actor; ambiguity is not identity resolution. |
| Malformed entity row not counted as schema-valid | Not directly probed for this count boundary in the cited pair; do not infer count semantics beyond the implementation's valid-entity index. | Preserve current malformed-row handling; do not broaden this change. | Requires separate raw probe to assert detailed output. |

## Proposed README wording (recommendation; not applied)

> **Round 13: unresolved actor IDs in occupancy reports.** A timeline `entity_id` with no schema-valid matching entity row remains a dangling-reference finding, but is not used to compare or update same-actor occupancy. A unique actor retains the existing same-tick/different-place diagnostic. Multiple matching entity rows retain the duplicate-ID and local ambiguous-actor findings and are not used for definite occupancy inference. These choices prevent a definite same-actor claim when actor identity is unresolved; they do not prove that events concern different people or that a real conflict is absent. Raw timeline rows and other diagnostics remain. The checker does not resolve identity or establish canon/source-text truth.

Do not replace the observed 3-finding temporary-probe result with the proposed behavior in historical evidence. Round-13 closure/report should cite the committed missing-vs-unique pair and named non-author replay before calling the change validated. No game-mechanics or lore-truth claim is recommended.
