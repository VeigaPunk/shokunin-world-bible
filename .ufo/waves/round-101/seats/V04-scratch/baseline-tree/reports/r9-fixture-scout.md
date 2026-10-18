# Round 9 fixture scout — duplicate-event order pair and unique control

Scope: observational fixture design/probes only. I did not edit the checker, fixtures, shared docs, or commit. Current checker: `.shokunin/lore/corpus/fixtures/check_bible.py`. Baseline files copied from `.shokunin/lore/corpus/fixtures/consistent/` (including valid `mira`, `harbor`, `tower`, and `courier-log` references).

## Proposed paired inputs

Use three valid event rows with existing entity/source references in each pair fixture:

- target `same` at tick 1, no dependencies;
- target `same` at tick 5, no dependencies;
- `consumer` at tick 3, `depends_on: ["same"]`.

The pair changes **only the order of the two `same` rows**. Keep consumer last and all other fields/sections byte-identical. The current index counts duplicate event IDs but overwrites its lookup with the last row; the dependency comparison then uses that last row (`check_bible.py`, `index('timeline')`, `event_id_counts`, final timeline dependency loop). This matches the specific baseline ambiguity noted in `.shokunin/lore/reports/r8-schema-scout.md`.

## Probe evidence

I ran the repo CLI `python3 .shokunin/lore/corpus/fixtures/check_bible.py <probe-dir>` on three copies under `/tmp/lore-r9-scout-k2u25n9u`. These are temporary probe inputs, not committed fixtures.

- `order-low-high` (`same` ticks 1 then 5, consumer tick 3): exit 1; output:
  ```
  VIOLATION: timeline[1].id: duplicate timeline id 'same'
  VIOLATION: timeline[2].depends_on: timeline inversion 'same' tick 5 not before 'consumer' tick 3
  2 violation(s); no canon changed
  ```
- `order-high-low` (`same` ticks 5 then 1, otherwise identical): exit 1; output:
  ```
  VIOLATION: timeline[1].id: duplicate timeline id 'same'
  1 violation(s); no canon changed
  ```
  The pair demonstrates the current order-sensitive inference: reversing target rows removes the inversion finding.
- `unique-control` has one `only` target at tick 1 and a tick-3 consumer depending on `only` (same valid source/entity setup): exit 0; output `CLEAN: schema, citations, relations, timeline; 0 violations`.

## Recommendations (separate from observations)

1. For the round-9 anomaly pair, expected future behavior should retain the duplicate-ID finding and report a local ambiguity at `consumer.depends_on[0]` for `same`, without comparing either duplicate tick. The ambiguity finding and remaining findings should be identical under row reversal; do not choose or merge either target row.
2. Keep the unique control as a clean regression: exactly one target ID resolves normally, and the earlier tick remains valid.
3. Treat this as duplicate-ID lookup calibration only. It does not validate causal meaning or source-text support.
