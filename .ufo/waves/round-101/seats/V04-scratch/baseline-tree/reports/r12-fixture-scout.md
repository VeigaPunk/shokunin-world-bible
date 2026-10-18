# Round 12 fixture scout: duplicate actor versus unique actor

## Observed probe (baseline)

Baseline checker was extracted without modification from declaration commit `954a1b712590f9b89aed6757e72a8bd4af5c8848`:

```sh
git show 954a1b712590f9b89aed6757e72a8bd4af5c8848:.shokunin/lore/corpus/fixtures/check_bible.py > /tmp/lore-r12-baseline-check_bible.py
```

Two scratch fixtures were built under `/tmp/lore-r12-fixture-scout/{duplicate-actor,unique-actor}` from the valid `consistent` fixture. Each uses the same two timeline events: distinct event IDs, tick 7, actor ID `mira`, different valid places (`harbor`, `tower`), empty dependencies, and valid source IDs. Their event rows otherwise match. The duplicate case adds one schema-valid `mira` entity row with a different name and a cited claim; the unique case retains the single existing `mira` entity row. Thus the entity table is the only intended case difference, and the raw duplicate row remains present.

Commands:

```sh
python3 /tmp/lore-r12-baseline-check_bible.py /tmp/lore-r12-fixture-scout/duplicate-actor
python3 /tmp/lore-r12-baseline-check_bible.py /tmp/lore-r12-fixture-scout/unique-actor
```

Observed CLI output (stderr empty in both cases):

```text
# duplicate-actor, exit 1
VIOLATION: entities[4].id: duplicate entities id 'mira'
VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
2 violation(s); no canon changed

# unique-actor, exit 1
VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
1 violation(s); no canon changed
```

This establishes that the baseline emits the occupancy collision in both cases, despite the duplicate actor-ID finding in the first. It does not establish that either event is canonical; the two places are only distinct in-world event assertions.

## Recommendation (not yet implemented)

Use this as the paired calibration fixture: under a duplicated, schema-valid actor ID, retain the duplicate entity-ID finding and event rows, add a timeline actor-reference ambiguity finding, and suppress only the inferred `double-booked` conclusion for that actor/tick. Preserve the `double-booked` finding for the otherwise identical unique-actor case. Avoid suppressing unrelated timeline checks or resolving either event as truth. For integration, copy these examples into the repository's normal fixture convention; this scout created no repository fixture and changed no checker.
