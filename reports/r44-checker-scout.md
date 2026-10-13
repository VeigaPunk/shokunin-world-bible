# Round 44 checker scout — actor resolution, occupancy, ordering

## Findings

- Timeline row shape calls the field `entity_id` and types it only as a nonempty string: `.shokunin/lore/corpus/fixtures/check_bible.py:12-13,37-43`. There is no field-level character-only schema declaration.
- Entity kinds are limited to character/place/faction/item, and valid rows are indexed; duplicate IDs overwrite the `entities` dictionary last-wins, while `entity_id_counts` separately counts all valid rows: `check_bible.py:7,45-51,107-121`.
- Timeline validation checks actor membership/dangling at `check_bible.py:228-237`; it reports ambiguity when count >1. Unlike `place_id`, it does not test a uniquely resolved actor's kind. `place_id` kind is explicitly checked at lines 238-241. Thus a unique place/faction/item ID is accepted as timeline `entity_id` (assuming all other row checks pass).
- Occupancy is keyed by `(entity_id, tick)` and only compared when actor ID is unique, place ID uniquely resolves to kind `place`, and tick is nonnegative (`check_bible.py:243-252`). Thus actor kind is not an occupancy prerequisite; same actor ID can be booked at distinct places irrespective of entity kind. The existing ambiguous-ID guard avoids treating duplicated IDs as definite identity.
- Dependencies are traversed after occupancy, independently; invalid dependency members report then continue only that dependency check (`check_bible.py:253-274`). Input row order determines which location receives the collision diagnostic; the stored slot is first row, but the conclusion is symmetric in detecting distinct places. 
- README says “A character cannot occupy different places at the same tick” (`.shokunin/lore/corpus/fixtures/README.md:29-34`), but does not define `entity_id` as necessarily character. The sentence supports character occupancy convention, not a universal ban on place/faction/item subjects.

## Ontology premise and inventory

The proposed unconditional character-only rule is **not established**. Schema uses generic `entity_id`; README occupancy statement is expressly about characters, and no checker invariant binds the generic ID to that category. Inventory of 92 fixture timeline tables finds all resolvable actors character-kind, except `r13-missing-actor`, whose two actor references are dangling (`unlisted`). This demonstrates current fixture convention, not domain ontology. I found no active fixture demonstrating a valid non-character subject, but absence is not proof that such events are invalid. Prior declarations explicitly say no global entity rule: r11 leaves actor identity out of scope (`LOG.md:158`); r12 handles ambiguous actor IDs, not actor kind (`LOG.md:167-173`).

## Risk / recommendation

Do not implement `entity_id must be character` on this evidence: it would turn a currently valid schema-level generic entity reference into a violation, potentially harming calibration for legitimate faction/item/place subjects and inventing ontology. If owner establishes that timeline records are character-location occupancy records, state that convention explicitly and make scope match it; a narrowly worded guard could then be considered. Keep dangling/ambiguous resolution, place kind, source checks, occupancy and dependency checks independent as now. Checker CLEAN remains structural and does not prove source support or fictional truth.

## Falsifiable go/no-go

**No-go now** for an unconditional kind guard. Falsifier for this conclusion: produce an authoritative schema/README convention that every timeline `entity_id` is a character (not merely that characters can occupy places), or a controlled fixture policy explicitly restricting this table to character events. If that evidence appears, proceed only if a unique `place` actor in an otherwise clean cloned timeline currently exits CLEAN, the paired `character` control remains CLEAN, the place-actor case gains exactly the scoped diagnostic, and all preexisting fixture outputs remain unchanged. If generic entity subjects are allowed, reject the proposed coverage move as ontology invention.
