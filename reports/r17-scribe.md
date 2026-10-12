# Round 17 scribe: bounded README and decision-table wording

Scope: documentation draft only. No shared README, decision-table, checker, or fixture was changed. The round-17 paired wrong-kind/valid/mixed probes are not present in the working tree at this observation; recommendations below are conditional on the declared round-17 behavior being implemented and verified.

## Observed raw CLI (current tree; not round-17 paired evidence)

Commands run from the repository root:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r11-unique-nonplace
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r16-valid-places
```

First exits 1 and prints `VIOLATION: timeline[0].place_id: not a place 'mira'` followed by `1 violation(s); no canon changed`. Second exits 1 and prints a `double-booked 'mira' at tick 7` between `harbor` and `tower`, followed by the same summary. These are separate existing controls, not a paired reproduction that a wrong-kind `mira` occupancy collision occurs. The LOG's temporary probe is the only paired observation cited in the round-17 declaration. I did not run or invent a new fixture.

## Proposed README paragraph (after round-17 evidence is admitted)

> **Round 17: unique wrong-kind place IDs and occupancy.** For this round's timeline occupancy check, an ID resolving to exactly one required-field-screened entity row whose `kind` is not `place` keeps the existing `not a place` finding but is not compared or stored as a resolved place for definite different-place occupancy. Two uniquely identified actual places still produce the existing same-actor/same-tick finding; a wrong-kind row between them does not mask that known pair. This is a narrow occupancy decision, not a claim about the event's actual location or whether a real conflict exists. It does not change count-zero IDs (round 16), duplicate/ambiguous place IDs, or other malformed entity rows. Entity/source IDs and citations do not establish prose support or canon truth.

Use only if actual paired raw outputs and unchanged baseline replay support each clause. If mixed-order control is not tested, remove the “does not mask” sentence rather than generalize from the simple pair.

## Proposed decision-table row

| Matching required-field-screened entity rows for timeline `place_id` | Occupancy decision | Diagnostic / control / limit |
|---|---|---|
| Exactly one, `kind` other than `place` | Preserve existing `not a place`; do not compare/store this row as a resolved place for definite different-place occupancy. | `r17-*` paired fixture should show a unique actor at a valid place and this wrong-kind ID on one tick: retain wrong-kind finding, withhold definite `double-booked`. It does not show the event's actual location or absence of a conflict. |
| Two uniquely identified `place` rows, distinct IDs | Retain existing `double-booked` finding for the unique actor/tick. | Positive control; wrong-kind exclusion must not suppress this known pair. |
| Known place, unique wrong-kind ID, known distinct place (same actor/tick) | Retain the known-place pair finding; keep the wrong-kind diagnostic; exclude only the wrong-kind row from occupancy. | Mixed-order control, ideally vary whether wrong-kind row is first/middle/last before claiming order robustness. |

The row describes a proposed output policy, not a general identity resolver. Avoid “valid location,” “no conflict,” “invalid event,” or any statement that cited sources prove an event. A wrong-kind entity ID remains an identifier with a structural kind mismatch; excluding it from this particular occupancy conclusion does not settle what the fiction means.

## Documentation placement

If admitted, append the round-specific section after round 16 in `corpus/fixtures/README.md`, and append the table after the existing round-16 rows in `corpus/knowledge/2026-10-12-lore-decision-table.md`. Keep baseline limitations explicit and distinguish round-17 count-one/wrong-kind from round-16 count-zero and duplicate-ID ambiguity. The top-level corpus README fixture inventory should only be updated if round-17 fixture directories actually land; list their exact names, not a prospective pattern as though it exists.
