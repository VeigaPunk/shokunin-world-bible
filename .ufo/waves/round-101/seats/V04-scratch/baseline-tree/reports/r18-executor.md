# Round 18 executor report: unique indexed places only

Scope: edited only `corpus/fixtures/check_bible.py`; no fixture, documentation, LOG, or commit changes. The occupancy comparison/insertion gate now requires `place_id` count exactly one and indexed entity kind `place`. The pre-existing dangling, ambiguous-place, and not-a-place diagnostics are untouched; the unique-actor guard remains unchanged.

## Baseline replay

Compared all 39 non-r18 fixture directories present under `corpus/fixtures/` against the checker extracted from report commit `82701ce` (`git show 82701ce:.shokunin/lore/corpus/fixtures/check_bible.py`). Each case ran via `python3 CHECKER FIXTURE_DIR`; exit code, stdout bytes, and stderr bytes were captured. Result: 39/39 exact matches; no output or exit-code differences. Cases were all present non-r18 fixture directories (39 total).

## Round-18 fixtures

Each command used `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/NAME`. Exact stdout follows; stderr was empty in all six cases. All six exit 1 (violations):

### `r18-duplicate-first-known` — exit 1

```text
VIOLATION: entities[4].id: duplicate entities id 'harbor'
VIOLATION: timeline[0].place_id: ambiguous place entity 'harbor'
VIOLATION: timeline[2]: double-booked 'mira' at tick 9 in timeline[1] ('tower') and 'quay'
3 violation(s); no canon changed
```

### `r18-duplicate-pair` — exit 1

```text
VIOLATION: entities[4].id: duplicate entities id 'harbor'
VIOLATION: timeline[1].place_id: ambiguous place entity 'harbor'
2 violation(s); no canon changed
```

### `r18-duplicate-reverse` — exit 1

```text
VIOLATION: entities[4].id: duplicate entities id 'harbor'
VIOLATION: timeline[0].place_id: ambiguous place entity 'harbor'
2 violation(s); no canon changed
```

### `r18-known-through-ambiguous` — exit 1

```text
VIOLATION: entities[4].id: duplicate entities id 'harbor'
VIOLATION: timeline[1].place_id: ambiguous place entity 'harbor'
VIOLATION: timeline[2]: double-booked 'mira' at tick 9 in timeline[0] ('tower') and 'quay'
3 violation(s); no canon changed
```

### `r18-mixed-kind` — exit 1

```text
VIOLATION: entities[4].id: duplicate entities id 'harbor'
VIOLATION: timeline[1].place_id: ambiguous place entity 'harbor'
2 violation(s); no canon changed
```

### `r18-unique-pair` — exit 1

```text
VIOLATION: timeline[1]: double-booked 'mira' at tick 9 in timeline[0] ('tower') and 'harbor'
1 violation(s); no canon changed
```

## Limits

These fixtures establish only the observed behavior of this checker on these six inputs and the unchanged baseline replay. They do not establish real place identity, actual event locations, sourced support, canon truth, or absence of conflicts where a place ID is ambiguous, absent, or wrong-kind. No fixture changes or independent non-author replay are claimed.
