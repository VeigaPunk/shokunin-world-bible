# Round 8 dependency scout — observed map

## Scope and evidence

This is a read-only map of the active checker and fixture inputs; no checker, fixture, or shared document was changed. The active source is `.shokunin/lore/corpus/fixtures/check_bible.py` (workspace checkout at `17736ae5ed260c4b99f98efd9b194254ccd2aa87`). The round-8 baseline named in `.shokunin/lore/LOG.md` is that same commit. The only current timeline fixture with dependency evidence inspected is `.shokunin/lore/corpus/fixtures/contradictions/timeline.json`.

## Current validation and exact insertion point

`check()` schema-loads `timeline.json` according to `FIELDS['timeline']` (around lines 18–20): each row must have an integer `tick`, string `id`, and list `depends_on`. The required-field validation does not constrain list contents. The timeline loop at `check_bible.py:226` first validates endpoints/source and nonnegative tick, then at lines 235–237 rejects the **whole dependency list** if any element is not a string (`.depends_on: expected event-id strings`) and continues, skipping occupancy and dependency checks for that row.

For string-only lists, occupied-slot checking is at lines 238–243. Direct dependencies are iterated at lines 244–248:

- `dep not in events` emits `unknown event`;
- otherwise the checker compares only `events[dep]['tick'] >= row['tick']`, emitting `timeline inversion` when the prerequisite is not strictly earlier.

The current dependency lookup uses `events`, the `index('timeline')` last-wins map created earlier, without requiring the dependency ID to occur exactly once. The counter `event_id_counts` is also built earlier (currently used by contradiction references), so duplicate event IDs are counted but not incorporated into this dependency loop.

**Exact insertion point recommendation:** after the list element type guard at lines 235–237, before slot occupancy at line 238, add a relation-local pass over `row['depends_on']` for self-reference and repeated IDs. This is the narrowest place that has a known-string list and still runs even if dependency IDs are unknown; it leaves the existing per-entry resolution/direct-tick loop at lines 244–248 intact. An alternative is to place checks inside that loop, but repeated values then require occurrence tracking and risks conflating list integrity with resolution. Do not place this in the earlier generic schema pass: it has no row-local event-loop semantics.

## Direct tick comparison: observed implications

The comparison is strictly **direct**: each listed ID is checked against the current event row's tick; there is no traversal of the prerequisite's own dependencies. A future-tick prerequisite is diagnosed even when another distinct prerequisite is valid. Equal ticks also fail (`>=`). This matches the README statement in `.shokunin/lore/corpus/fixtures/README.md` that dependency event IDs must have strictly earlier ticks.

In the observed `.shokunin/lore/corpus/fixtures/contradictions/timeline.json`, `arrival` at tick 2 lists `later`, whose tick is 3. The CLI rule therefore flags that one direct edge as an inversion. The separate `departure` (tick 1) and `later` (tick 3) rows have empty lists. This fixture tests a later prerequisite, not self-reference or repeated list entries. Existing same-tick occupancy evidence is an independent rule, not dependency validation.

Implications for proposed cases:

- A self-dependency resolves to the row's own indexed event, and its tick equals itself, so the current loop already emits a timeline inversion. A new self-list diagnostic would add the requested explicit list-integrity classification; avoid presenting it as a newly detected invalid edge or silently suppressing the existing inversion without a scoped policy decision.
- A repeated dependency ID is currently visited once per occurrence. If the prerequisite tick is earlier, repetition is silently accepted; if it is same/later, the same inversion message is emitted repeatedly. A list-local duplicate finding should be independent of tick validity and avoid redundant output from every repeated occurrence if practical.
- A valid list of distinct earlier prerequisites is checked independently and passes the dependency rule; there is no requirement to compare prerequisite ticks to one another.
- A self-reference or repeated ID can coexist with unknown-ID entries; list-integrity checks should not mask unknown-reference diagnostics. Non-string members currently trigger the row-level type diagnostic and skip all direct comparisons.

## Recommendations (not implementation)

1. Keep the move limited to list integrity: diagnose each self-reference and each repeated prerequisite ID at `timeline[i].depends_on` (or a clearly indexed child location), without modifying event rows or citations.
2. Preserve existing direct tick checks and their strict-earlier semantics. Treat any changed wording/count for self-dependency as an explicit behavior choice, since self currently also satisfies the inversion predicate.
3. Use paired fixture evidence: a clean row with two distinct, earlier prerequisites; an anomalous row with a self-ID and a duplicate ID; and, if practical, separate anomaly cases to prove diagnostic isolation. Retain the existing `contradictions` fixture's later prerequisite and run the full existing fixture matrix for regression.
4. Keep claims bounded to structural dependency-list validation and direct tick order. No causal inference, dependency traversal, source-text verification, or canon resolution is established by these checks.
