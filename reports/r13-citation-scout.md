# Round 13 citation and identity scout

## Observed checker behavior and probes

Inspected `.shokunin/lore/corpus/fixtures/check_bible.py`, including `source_id_counts` / `source_status()` / `source()`, entity claim validation, and the timeline loop. Also inspected `.shokunin/lore/corpus/fixtures/consistent/{sources,entities,timeline}.json`, `.shokunin/lore/corpus/fixtures/r12-unique-actor/timeline.json`, and `.shokunin/lore/corpus/fixtures/r12-ambiguous-actor/entities.json`.

Raw CLI probes:

```text
$ python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/consistent
CLEAN: schema, citations, relations, timeline; 0 violations

$ python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r12-unique-actor
VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
1 violation(s); no canon changed

$ python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r12-ambiguous-actor
VIOLATION: entities[4].id: duplicate entities id 'mira'
VIOLATION: timeline[0].entity_id: ambiguous actor entity 'mira'
VIOLATION: timeline[1].entity_id: ambiguous actor entity 'mira'
3 violation(s); no canon changed

$ python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r5-invalid-citation
VIOLATION: relations[0].source_id: unknown in-world source 'absent-source'
1 violation(s); no canon changed
```

Source references are checked through source-ID cardinality: `source()` reports an unknown or ambiguous in-world source ID, and entity first appearances/claims, relations, and timeline rows call it at their respective `source_id` fields. The timeline loop separately checks its `entity_id` against schema-valid entity rows: zero matches is a dangling entity finding; more than one is an ambiguous actor finding; one is the unique-ID case. The occupancy comparison is a further diagnostic based on `(entity_id, tick)`, not a source lookup.

The checked-in `consistent` timeline rows cite `courier-log` for both departure and arrival; the checker establishes that this source ID occurs once, not whether the cited text entails either event or whether either event is true. Likewise, presence of a unique entity ID is not proof of a real-world actor's identity. The `r5-invalid-citation` probe demonstrates a missing source ID finding, not an event-truth test.

## Recommendations (not observed checker behavior)

- Keep actor-ID resolution, source-ID resolution, and event truth distinct. A missing or duplicated actor ID can bound what occupancy can safely infer; a known citation ID does not repair actor identity.
- If suppressing a definite same-actor occupancy inference for an unresolved actor ID, retain the local dangling actor finding and event row. Describe the result as withholding that particular inference—not as showing the events involved different actors or that no conflict occurred.
- Continue to report source lookup status as citation-reference status only. Do not describe a unique citation as support, entailment, verification, or truth without inspecting source contents and a separate evidentiary method.

## Claim boundary

This scout reports checker structure and the raw CLI results above. It does not establish any event's truth, resolve actor identity, or prove that events do or do not conflict. It makes no source-text entailment, canon, or game-mechanics claim. Any proposed zero-match occupancy behavior still needs its own paired missing-actor/unique-actor evidence and regression replay.
