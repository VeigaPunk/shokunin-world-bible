# Round 10 critic — depth vs. row count, source claims, occupancy, causality

## Observations (repository state inspected)

- The round-10 declaration in `.shokunin/lore/LOG.md` proposes preserving `consistent/` and adding a cited micro-bible with an archivist/registry witness to Mira’s departure. At inspection, the only working-tree change was that LOG declaration; no round-10 fixture or source excerpt was present yet. This is not a judgment of an artifact I have not seen.
- The baseline `corpus/fixtures/consistent/entities.json` contains Mira, Harbor, Tower, and Seal; its claim statements cite `courier-log` or `archive-ledger`. `sources.json` gives those IDs titles and reliability notes, but no quoted source text. Thus “citation” currently means a resolvable ID, not demonstrated textual support.
- Baseline `timeline.json` has Mira depart Harbor at tick 1 and arrive at Tower at tick 2, with arrival depending on departure. In `check_bible.py`, dependency validation checks ID uniqueness and strictly earlier ticks; it does not validate causal claims, route continuity, or source-text entailment.
- Occupancy in `check_bible.py` is keyed by `(entity_id, tick)` and reports a conflict only when that entity is assigned different places at the same tick. It does not detect simultaneous incompatible events for different entities, nor does it prove a witness was present to observe an event.
- Entity `claims[].statement` is only checked for nonempty text and resolvable source ID. Relation rows receive endpoint/source-ID checks. Neither is compared against any excerpt.

## Critique / falsification risks

- More rows alone would not establish depth. Adding an archivist entity, a registry relation, and a second event could still be decorative unless the witness’s perspective changes or constrains interpretation of Mira’s departure (for example, a discrepancy, limitation, or consequential detail), rather than merely repeating it.
- “Unique source ID” is necessary for unambiguous lookup but not evidence for a claim. A source excerpt written alongside the claim can be circular self-attestation. The honest claim is that a reader can compare the assertion with the supplied fictional excerpt—not that the excerpt independently verifies canon or proves truth.
- A synchronized second account can introduce unsupported occupancy/knowledge assumptions: was the archivist at the harbor at that tick, in a position to observe Mira, or reading a registry entry later? If the excerpt is a later record, the event and the record’s creation/observation times should not be conflated. The checker will not catch those mismatches.
- The baseline timeline’s `depends_on` edge is only a structural ordering convention. A prior tick does not show that departure caused arrival, and a cited source ID does not make that causal reading supported. Avoid claiming causal validation from a clean checker result.
- The checker’s occupancy rule is narrower than ordinary “no double booking”: it allows same entity/same tick/same place multiple event rows, and does not reason about witness overlap or continuous travel. Do not present this move as validating occupancy or temporal consistency generally.

## Recommendations (not observations)

1. Keep the extension small but narratively consequential: give the archivist a distinct, bounded evidentiary role (what was seen vs. what was merely entered), and make that limitation matter to how the departure is understood. If the second perspective only duplicates Mira, prefer fewer rows.
2. Put the relevant excerpt text in the new fixture in a clearly labeled, fictional source artifact; map each added assertion to the exact excerpt passage, not just a source ID. Preserve attribution boundaries and distinguish observation time from record-entry time where relevant. State explicitly that this is authored in-world support, not independent corroboration.
3. Audit each new row manually for source-to-claim fit, witness access/presence, and same-tick entity/place assignments. Treat checker success as schema/reference/tick-rule success only. Do not infer source entailment, causality, route continuity, or general occupancy correctness from it.
4. For the depth verdict, require an actual connected narrative change and legible source mapping in the delivered artifact, not a count of added entities/relations/events. If those conditions are absent, depth is unchanged; if the source claim overstates what the excerpt supports, calibration may be harmed.

## Provisional verdict

The declared experiment is capable of testing depth, but the declaration alone does not show depth improvement. Judge only after inspecting the new excerpt and fixture. Key falsifier: if a reader cannot point to a specific meaningful detail that is both supported by the supplied excerpt and connected to the existing departure, the result is filler rows rather than demonstrated depth.
