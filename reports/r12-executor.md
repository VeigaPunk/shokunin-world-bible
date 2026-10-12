# Round 12 executor — actor identity ambiguity guard

## Claim and scope

When a timeline row references an entity ID represented by more than one schema-valid entity row, the checker now emits a field-local `ambiguous actor entity '<id>'` finding and does not compare or update that row in the occupied-slot table. The row is still processed for the other timeline checks (dangling actor/place, place identity/kind, source citation, tick, dependency shape and dependency rules); its raw event is not removed. Unique actors retain the existing occupancy comparison. This is an uncertainty finding, not a claim that the conflict is impossible: duplicate IDs leave identity unresolved, so a definite same-actor collision is not inferred. Dangling actor IDs have count zero and retain baseline behavior, including the existing occupancy comparison limitation.

Only `check_bible.py` and this report were changed by this executor. No fixtures, docs, LOG, or commit were made.

## Validation

Ran the available round-12 fixtures through the changed checker:

- `r12-ambiguous-actor`: exit 1, stderr empty. Output retains `entities[4].id: duplicate entities id 'mira'`, emits `timeline[0].entity_id: ambiguous actor entity 'mira'` and `timeline[1].entity_id: ambiguous actor entity 'mira'`, and does not emit `double-booked`.
- `r12-unique-actor`: exit 1, stderr empty. The unique actor still emits `timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'`.

Compared current checker against checker extracted from baseline commit `954a1b712590f9b89aed6757e72a8bd4af5c8848` on all 24 existing fixture directories. For every case, stdout bytes, stderr bytes, and exit code matched baseline exactly (24/24). Independently, the current output also matched the stored stdout payload and exit code in `.shokunin/lore/corpus/live/runs/20261012T174305Z/` for all 24. This is a comparison on the fixture directories available at execution time, not a claim about untested inputs.

## Limits

The entity count uses schema-valid entity rows, as in the checker's existing registry. Duplicate entity IDs are still separately reported. Ambiguous actor references are reported per timeline row. This rule does not decide whether duplicate rows denote one actor or multiple actors, adjudicate source truth, or resolve identity generally. A dangling actor remains subject to baseline occupancy behavior by explicit scope; no conclusion about its identity is warranted.
