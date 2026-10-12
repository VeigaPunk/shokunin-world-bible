# Round 19 scribe — bounded documentation draft

## Raw observations (repository state inspected)

- In `corpus/fixtures/check_bible.py`, timeline schema requires an integer `tick` (`FIELDS`, lines 12–13); timeline pass reports `tick < 0` as `must be nonnegative` (around line 240).
- That pass then independently checks the actor/place identity and, when both are comparable, uses the raw `(entity_id, tick)` tuple as the occupied slot (around lines 245–252). There is no `tick >= 0` condition in this occupancy guard. Thus static code inspection shows a negative tick is diagnosed and remains eligible for occupancy comparison/storage.
- I found no negative integer tick in committed `fixtures/*/timeline.json`; this is not a paired CLI observation, and I did not run/edit fixtures or checker.
- The existing decision table documents occupancy exclusions through round 18 and explicitly limits what suppressed findings mean. The corpus README’s fixture/run inventory currently ends at round 18.

## Recommendations (proposed copy only; not applied)

### Proposed round-19 decision-table addition

| Same uniquely screened actor/tick place references | Definite occupancy decision | Limit |
|---|---|---|
| Negative integer tick, with otherwise uniquely identified actor and place | Keep `must be nonnegative` and raw timeline row; withhold occupied-slot comparison and insertion for that row. | Invalid tick is outside the checker’s admitted numeric domain. This does not establish that the event is impossible, conflict-free, or false in-world. |
| Nonnegative tick with unique actor and unique place | Retain existing same-actor/different-place `double-booked` finding. | A checker finding about fixture IDs is not source-text support or canon truth. |
| Valid nonnegative known-place pair after or between a negative-tick row | Preserve the valid pair’s `double-booked` finding in the tested order(s). | Finite order controls do not prove exhaustive pairwise behavior. |

If the round is admitted, place this after the Round 18 decision-table section. Cite only the actual new fixture paths and raw replay artifact once those exist; do not describe the table above as measured evidence before verifier replay.

### Proposed README inventory addition

If round-19 fixtures and replay artifacts are actually added, extend the fixture inventory with their exact names and extend `live/runs/` coverage to round 19. Do not predeclare filenames, assert a replay, or claim the candidate was accepted before those artifacts and non-author verification exist.

### Suggested bounded scope sentence

“The occupancy guard excludes negative ticks only. The checker retains the invalid-tick diagnostic and raw row; suppression is not evidence that the event did not occur or that no real conflict exists. Nonnegative ticks and existing actor/place identity rules are unchanged.”

## Guardrails for final prose

- Distinguish integer tick validation from dependency ordering and optional item provenance ticks; this candidate concerns timeline occupancy only.
- Do not say “no conflict,” “impossible,” “not canon,” or that a cited source supports a timeline row.
- Attribute any observed outcomes to named raw CLI artifacts and the non-author replay, not to source descriptions or this scribe note.
- Add wording only if the implementation and paired/mixed controls match it and the verifier confirms all 45 prior outputs unchanged. If not, document the actual result, or omit the claim.
