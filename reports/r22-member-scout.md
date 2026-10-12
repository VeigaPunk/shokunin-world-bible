# Round 22 member scout — raw observations and recommendation

## Scope

Read-only scout. Baseline checker is `git show cc92ece:.shokunin/lore/corpus/fixtures/check_bible.py`. No checker, fixture, shared documentation, or repository history was changed. Paired inputs and captured CLI output are under `/tmp/r22-member-scout-gtr3md5l/` (temporary probe, not corpus evidence).

## Raw observation

Traversal occurs after timeline row schema validation and slot occupancy handling. In the dependency branch, the checker first evaluates `not all(isinstance(dep, str) for dep in row['depends_on'])`; if true, it appends one row-level `expected event-id strings` violation and `continue`s the *outer timeline-row loop*. Thus no string member is traversed, and all later dependency diagnostics for that row are skipped. This is list-wide, not member-local.

I ran the raw CLI (`python3 .shokunin/lore/corpus/fixtures/check_bible.py <probe-dir>`) on two generated inputs sharing the same sources/entities/relations and timeline rows except for the dependent row's dependency list:

- clean dependent list `['pre']`: exit 1; output `VIOLATION: timeline[1].depends_on: timeline inversion 'pre' tick 2 not before 'dep' tick 1` and `1 violation(s); no canon changed`.
- mixed dependent list `['pre', null]`: exit 1; output `VIOLATION: timeline[1].depends_on: expected event-id strings` and `1 violation(s); no canon changed`.

The first event is uniquely identified at tick 2 and dependent at tick 1; actor and places are unique/resolvable, both ticks nonnegative, and the probe differs only by appending null. So on these checker inputs, the malformed member masks a definite inversion finding for the valid string member. It says nothing about source-text chronology or canon. A mixed-row-order probe (dependent first, prerequisite second) likewise produced only the malformed-list diagnostic at `timeline[0]`; this confirms the row-level `continue` behavior, not an additional semantic property.

## Recommendation (not an observation)

The declared move is implementable narrowly: retain a row-level malformed-member diagnostic, then iterate only string members, skipping every non-string before set membership or event lookup. This avoids hashing/coercing malformed values (including unhashable values such as lists) while preserving current string traversal order, `seen_dependencies`, self/repeated/unknown/ambiguous checks, and nonnegative-tick inversion guard. Do not describe malformed members as satisfied or recoverable. The paired inversion case is strong evidence for the specific candidate; per-member handling should still be checked against the full 64 baseline CLI outputs and controls before recommending round admission. The report wording/count for malformed members should be decided explicitly before implementation; the baseline list-wide diagnostic is emitted once per malformed row.
