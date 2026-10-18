# Round 20 dependency scout — lookup, inversion, and raw endpoint probes

## Raw observations

- Baseline was checked against `git show 47733bf:.shokunin/lore/corpus/fixtures/check_bible.py`; its SHA-256 (`9ab0679201218b45f006847be27c972fe244ba1b9577fe82483b233238ae27e5`) matches the working checker. All probes below ran the baseline CLI on temporary copies of `.shokunin/lore/corpus/fixtures/consistent`; no repository fixture or checker was changed.
- Timeline `tick` is schema-screened with exact `type(value) is int` before indexing. Thus bool/float ticks are excluded from indexed timeline rows; negative integers remain valid indexed rows and independently emit `timeline[i].tick: must be nonnegative`.
- Lookup builds `events` from all indexed timeline rows; `event_id_counts` is counted separately over those rows. For a dependency reference, self/repeated findings are emitted first. First-seen references then get unknown (`count == 0`) or ambiguous (`count > 1`) findings; only exactly-one references reach the direct lookup/comparison `events[dep]['tick'] >= row['tick']`. Consequently equality is inversion, a duplicate ID is not compared despite `index()` retaining a last row, and a negative integer endpoint participates without an additional validity guard. Existing order check uses raw ticks, not a filtered/sanitized projection.
- Every temporary pair below otherwise retained the consistent fixture structure, unique dependency ID (`departure`), unique dependent ID (`arrival`), source/entity/place rows, and `arrival.depends_on == ['departure']`; only the indicated event tick(s) changed. Command: `python3 .shokunin/lore/corpus/fixtures/check_bible.py <temp-dir>`.

| Probe (departure prerequisite → arrival dependent) | Raw relevant stdout | Exit |
|---|---|---|
| `0 → -1` (negative dependent) | `timeline[1].tick: must be nonnegative`; `timeline[1].depends_on: timeline inversion 'departure' tick 0 not before 'arrival' tick -1` | 1 |
| `-1 → 2` (negative prerequisite) | `timeline[0].tick: must be nonnegative` only; no inversion | 1 |
| `3 → 2` (valid inversion) | `timeline[1].depends_on: timeline inversion 'departure' tick 3 not before 'arrival' tick 2` | 1 |
| `1 → 2` (valid ordered control) | `CLEAN: schema, citations, relations, timeline; 0 violations` | 0 |
| `-2 → -1` (both negative, ordered) | Two negative-tick findings only; no inversion | 1 |
| `-1 → -2` (both negative, inverted) | Two negative-tick findings plus inversion `'departure' tick -1 not before 'arrival' tick -2` | 1 |
| `2 → 2` (valid equal-tick control) | Double-booked finding plus inversion `'departure' tick 2 not before 'arrival' tick 2` | 1 |
| `-1 → -1` (both negative, equal) | Two negative-tick findings plus inversion `'departure' tick -1 not before 'arrival' tick -1` | 1 |

`0 → -1` and `-1 → 2` demonstrate both orientations of a single invalid endpoint: it can cause an inversion finding or permit an ordering comparison that reports none. These are checker/input observations, not findings about event truth or fictional chronology.

## Recommendations (not implementation)

- If pursuing the declared calibration move, retain negative tick diagnostics and raw rows/references, but gate only the definite inversion comparison on both uniquely resolved endpoint ticks being nonnegative. Do not label an invalid-tick dependency satisfied, absent, or impossible; the narrow claim is only that this checker cannot make that ordering comparison under its admitted tick domain.
- Preserve unknown/ambiguous/self/repeated dependency diagnostics and valid-to-valid comparison behavior. Keep valid ordered, valid inversion, and equal-valid controls; ensure a negative endpoint leaves its tick diagnostic and dependency reference intact. Do not change duplicate-ID policy, type schema, occupancy, or source/canon claims.
- These bounded CLI probes do not establish hidden conflicts, event occurrence, or what cited fictional sources say. A withheld inversion is not evidence that chronology is consistent.
