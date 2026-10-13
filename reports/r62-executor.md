# Round 62 executor — timeline availability gate

## Decision

**GO for this narrow calibration candidate.** The matched probe distinguishes failed timeline input from a decoded empty array while retaining pointer locations. This is an executor result, not a final round verdict.

## Change and fixtures

Changed `corpus/fixtures/check_bible.py`, its README, and added `r62-missing`, `r62-malformed`, `r62-duplicate-member`, `r62-nonarray`, `r62-empty`, `r62-partial`, `r62-duplicate`, `r62-loaded`, `r62-malformed-side`, and `r62-independent`. The first eight share tables from `r39-ledger-source-missing`; timeline state varies alone except the explicitly named malformed-side/independent controls. Availability is true only for decoded top-level lists. Valid ledger sides on unavailable timeline get `cannot assess event <id>: timeline.json unavailable`, retaining their locations. Ledger shape/field/distinctness and independent source/entity/relation checks remain. Loaded empty, partial, duplicate semantics stay unchanged. Failed full timeline creates no dependency rows/findings.

## Exact output evidence

From repository root, command: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<name>`.

- Old pinned checker, malformed timeline: loader JSON error; claim_a `expected exactly one timeline event 'tarin-envelope-observation'`; claim_b `expected exactly one timeline event 'sella-bell7-presence'`; 3 findings.
- Candidate malformed: same loader JSON error; claim_a `cannot assess event 'tarin-envelope-observation': timeline.json unavailable`; claim_b `cannot assess event 'sella-bell7-presence': timeline.json unavailable`; 3 findings. Exit 1.
- Candidate missing, duplicate-member, and nonarray: respective primary loader/shape error plus the same two per-pointer unavailable lines.
- Candidate loaded `[]`: two original expected-exactly-one lines, 2 findings. Candidate partial: only claim_b expected-exactly-one, 1 finding.
- Candidate loaded duplicate: duplicate `departure` ID, claim_b's existing no-resolvable-source, ambiguous dependency, and timeline[3] unknown-source; 4 findings.
- Candidate matched r39 loaded base: exactly claim_b `event 'sella-bell7-presence' has no resolvable source_id` and timeline[3] unknown `missing-sella-note`; 2 findings. Both IDs are in the timeline, correcting the pair-scout caveat; the old r39 source branch is intact.
- Malformed-side/unavailable control retains both invalid-field findings and same-reference finding in addition to load error.
- Independent relation/unavailable control retains loader error, both pointer lines, and `relations[0].from: dangling entity 'not-an-entity'`.

All runs exit 1. These outputs demonstrate a change in diagnostic certainty, not event-world truth.

## Baseline preservation

Used pinned work commit `e34a7750f098651a92099adfd6e280c59a642ed7`. Enumerated its 115 fixture directories from the Git tree and ran pinned and candidate checkers with identical root-relative arguments/cwd. All 115 `(exit, stdout bytes, stderr bytes)` tuples match exactly (0 deltas). All 574 old fixture JSON paths match pinned blobs byte-for-byte (0 mismatches). New r62 paths are outside the denominator.

## Limits

This is only supplied-JSON event-ID index availability. Loaded partial remains available under existing admitted-row semantics; duplicates remain ambiguous. Failed full timeline has no rows for dependency checks, so no dependencies are invented. Explicit per-reference messages cost output volume for large ledgers but preserve repair locations. No inference about event occurrence, source prose, chronology, truth, canon, ownership, license, permission, or rights follows.
