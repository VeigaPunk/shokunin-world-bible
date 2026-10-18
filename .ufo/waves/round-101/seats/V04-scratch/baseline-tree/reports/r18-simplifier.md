# Round 18 simplifier — minimal occupancy guard

## Raw observations

- In `corpus/fixtures/check_bible.py`, the timeline loop computes `place_id_count` from `entity_id_counts` (around lines 234–238). A count above one emits `ambiguous place entity`; it does not stop occupancy processing.
- `comparable_place` is currently true for counts other than one, or for a unique entity of kind `place` (line 245). The occupancy condition then requires a unique actor and a nonzero place count (line 246). Thus an ambiguous place ID (`count > 1`) is still compared/inserted as a raw ID when the actor is unique.
- Existing conditions already omit count-zero places and uniquely resolved non-place entities. A uniquely resolved place remains eligible. Duplicate actor IDs remain omitted by `actor_id_count == 1`.

## Minimal recommendation (not applied)

Add `place_id_count <= 1` to the existing occupancy condition:

```python
if actor_id_count == 1 and place_id_count != 0 and place_id_count <= 1 and comparable_place:
```

This is the smallest local change to the current predicate: among events currently eligible for occupancy comparison/insertion, only ambiguous place counts (`> 1`) become ineligible. It keeps the unique-actor requirement, count-zero exclusion, unique wrong-kind exclusion through `comparable_place`, and uniquely resolved actual-place behavior. The existing ambiguity diagnostic and timeline row remain untouched. Do not claim that suppression establishes the actual location or absence of a real conflict.

Equivalent simplification to `place_id_count == 1` would depend on preserving the existing wrong-kind check and conveys the eligibility more directly, but is a larger predicate rewrite than adding the one bound. No source or fixtures were changed for this report.
