# Round 24 schema scout — relation endpoint behavior

## Findings

- Relation rows are schema-admitted only when `from`, `to`, `type`, and `source_id` are nonempty strings: `.shokunin/lore/corpus/fixtures/check_bible.py:8-14,32-43`. Thus endpoint processing can assume strings and does not need to handle JSON arrays/objects; missing, blank, or wrong-type endpoint values are rejected at the row and omitted from `data['relations']`.
- The entity index is a last-row-wins dictionary. It reports a duplicate at the later entity row but still assigns that row to `result[row['id']]` (`check_bible.py:45-52`). This means membership tests alone cannot detect relation endpoint ambiguity.
- Relation validation currently checks only dictionary membership and emits `dangling entity` when absent (`check_bible.py:118-122`). Since duplicate IDs remain present in the dictionary, both endpoints resolve as if unique. The checker already separately counts entity IDs at lines 125-127, but that count is constructed after the relation loop; a per-endpoint `entity_id_counts` status can distinguish zero, one, and multiple without changing the relation schema.
- Timeline endpoint handling is an applicable precedent: it distinguishes dangling from ambiguous actor/place using entity counts (`check_bible.py:260-269`); allied-pair validation also suppresses semantic checks unless IDs are unique (`check_bible.py:237-251`).

## Risk / boundary

Do not call an endpoint dangling when its ID exists multiple times. Report an endpoint-local ambiguity (e.g. `relations[i].from: ambiguous entity ...`) and avoid choosing a duplicate row or inferring relation semantics. Preserve the existing duplicate-ID diagnostic and existing dangling message for zero matches. In particular, malformed relation rows are filtered before endpoint resolution, so they should not generate secondary endpoint diagnostics. Source citation checking is independent and should remain unchanged.

## Suggested test

Add a fixture cloned from a clean baseline with a valid relation whose `from` (then separately `to`) names an entity ID duplicated by a second entity row. Assert the duplicate-ID finding plus the corresponding relation-local ambiguous endpoint finding, with no dangling finding for that endpoint. Include a unique-ID relation control with no endpoint error and retain a genuinely absent-ID control expecting dangling. Include wrong-type/blank endpoint controls only if ensuring schema filtering is in scope; assert required-field error and no endpoint-local follow-on. This exercises both endpoint directions and ensures no arbitrary last-row selection.
