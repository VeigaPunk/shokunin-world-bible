# Round 31 scribe: source-ID resolution decision table

## Decision table

This table describes existing checker behavior for a relation citation; it is not a proposed checker rule. The generic `source()` helper counts admitted `sources.json` IDs, then emits a local finding for zero or multiple matches (`.shokunin/lore/corpus/fixtures/check_bible.py:53-74`). Every relation row passes its `source_id` and location to that helper (`.shokunin/lore/corpus/fixtures/check_bible.py:123-130`).

| Matching source rows for relation `source_id` | Local relation diagnostic | Interpretation / boundary |
|---:|---|---|
| 0 | `relations[i].source_id: unknown in-world source '<id>'` | Citation ID is unresolved; relation is not thereby false. |
| 1 | No source-resolution diagnostic | ID uniquely resolves as a reference only; source text support is not checked. |
| 2+ | `relations[i].source_id: ambiguous in-world source '<id>'` | Identity is unresolved; no row is selected, and relation truth is not decided. The duplicate-ID diagnostic is retained too. |

The table concerns source-ID multiplicity, not whether a citation is authentic, rights-cleared, or textually supportive. The fixture README explicitly says duplicate IDs remain untouched and array order does not select one (`.shokunin/lore/corpus/fixtures/README.md:88-97`).

## Existing evidence and gap

The round-7 ambiguous fixture has two `harbor-compact` source rows (`.shokunin/lore/corpus/fixtures/r7-ally-reverse-ambiguous/sources.json:1-20`). Its reverse `allied_with` edge cites that ID (`.shokunin/lore/corpus/fixtures/r7-ally-reverse-ambiguous/relations.json:7-12`); the README describes the duplicate, local ambiguous citation, and missing *qualified* reciprocal (`.shokunin/lore/corpus/fixtures/README.md:88-104`). Thus prior coverage already includes an ambiguous **relation citation**, but only on an alliance relation, where reciprocal qualification is also at issue. Do not claim r7 lacks relation coverage.

The clean `carries` relation `mira -> seal` cites `courier-log` (`.shokunin/lore/corpus/fixtures/consistent/relations.json:1-7`), and the clean sources table has one such ID (`.shokunin/lore/corpus/fixtures/consistent/sources.json:8-13`). The current r7 fixtures therefore do not provide the controlled unique-versus-ambiguous source-ID pair for this generic, non-alliance relation class. Round 31's declared probe keeps that relation fixed and duplicates only its source ID (`.shokunin/lore/LOG.md:479-481`).

## Risks and test

**Risks.** A duplicate ID is an input identity ambiguity, not evidence the cited relation is false, unsupported, or canonically untrue. A unique ID only resolves which in-world record is named; it does not establish that record's prose supports `carries`, authenticate it, or establish rights. Avoid conflating the generic citation diagnostic with the alliance-specific missing-qualified-reciprocal behavior already seen in r7. A generic test should inventory any other output deltas induced by duplicating the source ID (claims/events may cite it too), rather than claim a relation-only output delta; this is required by the round declaration (`.shokunin/lore/LOG.md:481`).

**Test.** Compare the unchanged `consistent/` control (one `courier-log` row; relation source field unchanged) with the declared paired input containing a second structurally admitted `courier-log` row. Expected source-resolution outcome: control exits 0; duplicate case reports `relations[0].source_id: ambiguous in-world source 'courier-log'`, plus the duplicate-source-ID diagnostic and any other legitimate ambiguous-citation findings. Check the complete stdout/exit status rather than assuming only the relation reports. In the pair, retain all five control tables except the one additional source row, and verify that `relations[0]` itself remains byte-identical. Replay all 81 pre-existing fixture stdout/stderr/exit tuples and compare all 404 prior JSON path bytes unchanged, per the round's falsifiable declaration (`.shokunin/lore/LOG.md:481`). This is diagnostic input coverage only; it adds neither a checker rule nor canon truth.
