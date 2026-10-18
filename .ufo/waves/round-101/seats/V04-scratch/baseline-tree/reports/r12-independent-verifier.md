# Round 12 independent verifier

Independent, non-author replay. No checker or fixture file was edited; no commit made.

## Method and immutability

- Repository baseline checker extracted from `954a1b712590f9b89aed6757e72a8bd4af5c8848` using `git show 954a1b7:.shokunin/lore/corpus/fixtures/check_bible.py` to `/tmp/r12-baseline-check_bible.py`. Baseline checker SHA-256: `f0e87e2ff88529cdd46090324415462982d80c101d3466351df55ed46e1b804f`. Working checker SHA-256: `7caf1933f39d1103d93883448bdd0c3f066f849ffe96a6afff37b57d8f1269b3`.
- Enumerated all 26 fixture directories at `.shokunin/lore/corpus/fixtures/`; replay command for each was `python3 <checker> .shokunin/lore/corpus/fixtures/<fixture>`, capturing stdout bytes, stderr bytes, and process exit status. Used extracted baseline checker on all 26 (including the two new fixtures) and current checker on all 26.
- Snapshot SHA-256 for all 129 fixture `*.json` files before and after replay: identical (no changed path). This includes the pair fixtures.
- Old-fixture stdout, stderr, and exit status compare byte-for-byte: **24/24 identical**. stderr is empty on all 26 current runs.

### Old fixture replay comparison

- `ally-one-way`: exit 1; stdout/stderr/exit match current.
- `ally-reciprocal`: exit 0; stdout/stderr/exit match current.
- `consistent`: exit 0; stdout/stderr/exit match current.
- `contradictions`: exit 1; stdout/stderr/exit match current.
- `contradictions-ledger-malformed`: exit 1; stdout/stderr/exit match current.
- `item-chain-broken`: exit 1; stdout/stderr/exit match current.
- `item-chain-valid`: exit 0; stdout/stderr/exit match current.
- `r10-registry-witness`: exit 0; stdout/stderr/exit match current.
- `r11-character-place`: exit 1; stdout/stderr/exit match current.
- `r11-dangling-place`: exit 1; stdout/stderr/exit match current.
- `r11-place-character`: exit 1; stdout/stderr/exit match current.
- `r11-unique-nonplace`: exit 1; stdout/stderr/exit match current.
- `r5-invalid-citation`: exit 1; stdout/stderr/exit match current.
- `r5-invalid-json`: exit 1; stdout/stderr/exit match current.
- `r5-missing-file`: exit 1; stdout/stderr/exit match current.
- `r5-row-shape`: exit 1; stdout/stderr/exit match current.
- `r5-wrong-top-level`: exit 1; stdout/stderr/exit match current.
- `r7-ally-reverse-ambiguous`: exit 1; stdout/stderr/exit match current.
- `r7-item-ambiguous`: exit 1; stdout/stderr/exit match current.
- `r8-deps-anomalous`: exit 1; stdout/stderr/exit match current.
- `r8-deps-distinct`: exit 0; stdout/stderr/exit match current.
- `r9-dup-high-low`: exit 1; stdout/stderr/exit match current.
- `r9-dup-low-high`: exit 1; stdout/stderr/exit match current.
- `r9-unique-control`: exit 0; stdout/stderr/exit match current.

## Round-12 pair and attribution

`r12-ambiguous-actor` and `r12-unique-actor` have identical `timeline.json`, `sources.json`, `relations.json`, and `contradictions.json` bytes. Both timeline rows, unchanged and in order, are:

1. `id=r12-harbor`, `tick=7`, `entity_id=mira`, `place_id=harbor`, `source_id=courier-log`.
2. `id=r12-tower`, `tick=7`, `entity_id=mira`, `place_id=tower`, `source_id=courier-log`.

The source registry is the same in both: `courier-log` (Courier Mira’s Route Log, year 12) and `archive-ledger` (Lantern Harbor Registry, year 12). The unique fixture has one `mira` character entity; the ambiguous fixture adds a second valid entity row with `id=mira`, named “Mira of the second ledger.” The place entities (`harbor`, `tower`) are the same. Thus the pair changes actor-ID multiplicity, not the event rows or source IDs.

Baseline checker on ambiguous pair: exit 1, duplicate entity-ID diagnostic, and `timeline[1]: double-booked 'mira' at tick 7 ...`; 2 violations. Current checker: exit 1, duplicate entity-ID diagnostic plus `ambiguous actor entity 'mira'` for both `timeline[0]` and `[1]`; no `double-booked`; 3 violations. This is an indeterminate-identity result, not a finding that no conflict exists. On the unique control, both baseline and current output the same `double-booked 'mira'` at tick 7; exit 1, 1 violation. Therefore the new behavior is isolated to non-unique valid entity-ID occupancy, and the unique control remains enforced.

## Dangling baseline limitation and discrepancies

No discrepancies found in the 24 legacy fixture CLI outputs. In particular, `r11-dangling-place` remains byte-identical to baseline and reports only the dangling place finding. The dangling-**actor** occupancy behavior remains a known baseline limitation: the baseline occupancy key uses `(entity_id, tick)` even when actor ID membership is absent, so multiple same-tick rows with the same dangling actor ID and differing place IDs can still be attributed as `double-booked`; this round does not change it. The existing raw dangling-place fixture does not itself exercise that dangling-actor case; this statement is a scope limitation from checker behavior/round clarification, not a claimed fixture result. No broad identity or canon conclusion follows from these diagnostics.
