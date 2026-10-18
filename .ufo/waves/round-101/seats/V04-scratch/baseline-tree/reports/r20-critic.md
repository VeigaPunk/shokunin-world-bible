# Round 20 critic — negative tick dependency calibration

## Scope

Read-only critic. I inspected the Round 20 declaration and current checker, read the scout reports available at the time, and ran additional probes against temporary copies of `consistent/`. I wrote only this report; no checker, fixture, shared document, or commit was changed. The baseline checker is the declared `47733bf` version (the dependency scout reports its hash matches the working checker). Probe results below are baseline CLI observations, not canon or source-text evidence.

## Raw observations (not recommendations)

- Timeline rows with required fields are indexed only after exact-type screening. Negative integer ticks survive that screen and separately emit `must be nonnegative`; bool/float/missing-tick rows do not survive as timeline rows. Dependency resolution uses admitted event-ID counts: only a uniquely resolved dependency reaches the raw `events[dep]['tick'] >= row['tick']` comparison. Unknown, duplicate/ambiguous, self, and repeated references have separate handling. A non-string member in `depends_on` causes a row-level finding and skips that row's remaining timeline processing.
- Baseline probes reported a dependency inversion for `(prerequisite, dependent) = (0, -1)`, and no inversion for `(-1, 0)`, though the prerequisite tick was invalid. Thus the negative-dependent case adds an inversion finding, while the negative-prerequisite case has an invalid-tick finding but no ordering finding. Both inputs retain raw rows/references; neither output establishes actual chronology.
- Additional temporary probes: `(-1,-1)` reports two invalid-tick findings and an inversion on equal raw ticks; `(-1,0)` with two references to `departure` reports the prerequisite tick finding and the repeated-reference finding, but no inversion; `(0,-1)` with an unknown dependency reports the invalid tick and unknown reference; `(0,-1)` self-referencing `arrival` reports invalid tick, self-reference, and raw-tick inversion. These confirm comparison is downstream of unique resolution and that self-dependency can also reach the comparison. They do not test a changed candidate.
- A valid-to-valid inversion `(2,1)` remains a separate, observable rule; valid ordered `(0,1)` is clean. A negative event can be connected by multiple dependency edges, so a negative endpoint can make multiple direct comparisons unassessable under a nonnegative tick domain. This does not disable comparisons on unrelated valid-to-valid edges.
- The checker validates source-ID resolution, not source text for ticks or dependency order. The cited fictional source ID does not establish event occurrence or chronological support.

## Falsification / hidden-inversion considerations

The narrow claim is defensible only as “do not assert a definite inversion from this direct edge if either endpoint is outside the checker’s nonnegative tick domain.” It is not a claim that the dependency is satisfied, that the edge is chronological, or that the input has no hidden inversion. In particular, a valid dependent with a negative prerequisite already passes the current `>=` test; suppressing that comparison cannot expose the absence of an inversion. The tick diagnostic is the remaining evidence of invalidity, so neither baseline nor candidate should be described as validating that edge.

A broad guard around dependency processing would be wrong: it could suppress unknown/ambiguous/self/repeated findings or valid-to-valid inversions elsewhere on a row. Keep the candidate at the unique-resolution comparison itself. Check both endpoint orientations, both-negative equality/order, equal valid ticks, and a valid-to-valid inversion alongside a negative edge. In a graph with valid nodes A and C and negative-tick B, preserve an inversion on a direct A→C dependency regardless of any separate A/B or B/C edges; suppression must be per edge, not per row, chain, or graph. Do not infer that ordering through B is validated or that a transitive relation repairs the invalid tick.

The checker's independent non-string-list early `continue` is a pre-existing policy: a malformed dependency list can skip other dependencies on that row. It is outside this move; avoid claiming all unaffected dependency diagnostics are generally preserved without a control for that condition. Similarly, malformed tick rows are excluded before ID counting, while negative integer rows remain indexed. This move should not alter that distinction or duplicate-ID policy.

## Recommendations (separate from observations)

- If implemented, gate only the inversion comparison after unique dependency resolution on both endpoint ticks being nonnegative. Retain invalid-tick findings, raw events and references; do not `continue`, sanitize ticks, call a dependency satisfied, or suppress any other dependency diagnostic.
- Validate both invalid-endpoint orientations and valid controls, including an unrelated valid-to-valid inversion on the same input graph. Cover both-negative/equal inputs and self, repeated, unknown, and ambiguous references to demonstrate the guard is in the intended branch. Replay all 49 saved CLI outputs against the declared baseline/current candidate, comparing stdout, stderr, and exit status.
- Keep fixture text input-scoped. Describe any omitted comparison as unassessed due to invalid tick, not proof of no inversion, no hidden conflict, event absence, or canon truth. This is a bounded calibration opportunity, not evidence that real chronology has been repaired.

I make no axis-admission verdict: critique alone does not establish candidate implementation, full preservation, independent replay, or the separate reviewer/verifier/adjudicator evidence required by the round declaration.
