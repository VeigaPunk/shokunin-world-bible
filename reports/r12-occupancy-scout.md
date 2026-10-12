# Round 12 occupancy scout

## Observed raw paths and checker logic

- Mission/round declaration: `/tmp/mission-lore-standing.md`; `.shokunin/lore/LOG.md`, Round 12 declaration.
- Checker inspected: `.shokunin/lore/corpus/fixtures/check_bible.py` (the declared baseline is `git show 954a1b7:.shokunin/lore/corpus/fixtures/check_bible.py`).
- Existing clean fixture inspected: `.shokunin/lore/corpus/fixtures/consistent/{entities,timeline,sources}.json`. It has unique actor IDs (`mira`) and normal departure/arrival entries.
- Relevant raw implementation: `entity_id_counts` counts only schema-valid entity rows. The timeline loop checks actor dangling with `row['entity_id'] not in entities`, but never checks actor count. Occupancy is keyed solely by `(row['entity_id'], row['tick'])`. A later row reports `double-booked` iff that key is already present and its `place_id` differs from the stored place; equal-place rows share the slot. On a collision, the original slot remains stored. Thus duplicate entity IDs do not create separate actor slots: two timeline rows naming a duplicated ID at the same tick and distinct places are treated as one actor and produce a false-positive collision relative to unresolved identity. The existing duplicate-entity-ID violation is independently emitted by `index('entities')`.
- Reproduction inputs were written outside the repo under `/tmp/r12-occupancy-lotekrlu/duplicate/` and `/tmp/r12-occupancy-lotekrlu/unique/`. Both were copied from `consistent`. In `duplicate`, a second schema-valid `mira` character row was appended (with `first_appearance: courier-log`, empty claims), and timeline was replaced by two otherwise ordinary tick-7 events, actor `mira`, places `harbor` and `tower`. In `unique`, a schema-valid `nara` character row was added and the same two events used actor `nara`. Sources and place rows remain from the fixture.
- CLI invoked: `python3 .shokunin/lore/corpus/fixtures/check_bible.py <temp-case>`.

## Raw CLI output

Duplicate actor-ID case (`/tmp/r12-occupancy-lotekrlu/duplicate`):
```text
VIOLATION: entities[4].id: duplicate entities id 'mira'
VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
2 violation(s); no canon changed
DUP_EXIT:1
```

Unique actor control (`/tmp/r12-occupancy-lotekrlu/unique`):
```text
VIOLATION: timeline[1]: double-booked 'nara' at tick 7 in timeline[0] ('harbor') and 'tower'
1 violation(s); no canon changed
UNIQUE_EXIT:1
```

The control confirms the intended same-actor/different-place rule for a uniquely identified actor. The duplicate case emits the same occupancy finding in addition to the duplicate-ID finding; it does not currently mark the actor reference ambiguous. This establishes the stated false-collision premise for schema-valid duplicate actor IDs.

## Recommendation (not observed behavior)

Bound any proposed change to timeline `entity_id`: count schema-valid entity rows for the referenced actor. For count greater than one, report a local ambiguous actor reference and do not compare/insert that event into the same-actor occupancy map; leave the duplicate entity-ID finding and event rows intact. Preserve dangling actor behavior for zero matches and existing occupancy semantics for a unique actor. Do not generalize this to entity resolution, canonical identity, same-place coalescing, or other ID-bearing fields. Verify both duplicate-ID and unique-actor pair controls and replay the 24 prior cases as Round 12 declared.
