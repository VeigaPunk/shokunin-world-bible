# Round 10 executor — registry witness fixture

## Artifact and limits

Created `.shokunin/lore/corpus/fixtures/r10-registry-witness/` by copying all five JSON tables from `fixtures/consistent/`, then appending only one source, entity, relation, and event. Added `registrar-copy-excerpt.md`, explicitly labeled fictional and invented fixture text. No checker, baseline fixture, or other source table was modified.

The excerpt reads: “At first bell at Lantern Harbor, I, Sella, registrar there, recorded seeing Mira leave. At Mira’s request, I left the registry destination blank and kept the carbon.” The `registrar-copy` reliability note says this is invented in-world text and bounds Sella’s report to her observation and entry, not omniscient truth or Mira’s actual destination. The excerpt says nothing about Mira’s actual destination; blank is an intentional omission at Mira’s request, not evidence of a conflicting destination or contradiction.

## New-row mapping

| Added assertion | Exact excerpt support | Boundary |
|---|---|---|
| `sella` character name Sella | “I, Sella” | A fictional speaker named in authored fixture text. |
| Entity claim “Sella is a registrar at Lantern Harbor.” | “At first bell at Lantern Harbor, I, Sella, registrar there” | Textual correspondence, not independent identity/office verification. |
| `sella` → `mira`, `records_departure` | “recorded seeing Mira leave” | Says Sella recorded seeing the departure; does not independently prove it occurred. |
| `registry-entry` description: first bell, Sella records seeing Mira leave, leaves destination blank at Mira’s request and keeps carbon | “At first bell”; “recorded seeing Mira leave”; “At Mira’s request, I left the registry destination blank and kept the carbon.” | Timeline tick 1 is aligned to baseline departure’s local sequence label; the excerpt does not define tick conversion. `depends_on` is empty because the baseline departure is also tick 1 and dependencies require a strictly earlier event. |

Each new claim-bearing row cites the unique `registrar-copy` source ID. Existing baseline rows in every table remain unchanged semantically and in original order.

## CLI and regression

- `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r10-registry-witness` exited **0**: `CLEAN: schema, citations, relations, timeline; 0 violations`. This checks structure, citation identity, relations, and timeline rules only; it does not test excerpt entailment, truth, witness access, causality, or canon.
- Regression replayed all **19** pre-existing fixture directories; each returned the same exit status as its saved round-9 run record. SHA-256 snapshots of the checker and all pre-existing fixture JSON files were identical before and after replay.
- Parsed baseline records were compared with the leading records in all five new tables: exact semantic equality passed, with only the four proposed additions and no additions to contradictions.

This report is the executor’s mapping, not independent review. The source is intentionally authored alongside the claims; neither checker success nor this mapping establishes independent corroboration or canon truth.
