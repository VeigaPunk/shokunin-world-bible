# Round 57 regression scout — dependency-cycle inventory and replay plan

## Scope and observed evidence

Read-only inventory of the active fixture corpus, checker source, and prior-round evidence. No checker, fixture, README, LOG, or checklist was changed. Active checker: `.shokunin/lore/corpus/fixtures/check_bible.py`; dependency handling is at lines 253–274. It validates string members, reports self and repeats (261–266), resolves only uniquely identified event IDs (267–271), and for uniquely resolved endpoints with nonnegative ticks reports a strict-order inversion when prerequisite tick is greater than or equal to dependent tick (272–274). There is no graph traversal in this block. This is an input consistency checker, not a causal validator.

The fixture tree contains 95 top-level fixture directories with readable `timeline.json` (the round-57 LOG baseline count); 66 have at least one nonempty dependency list. I scanned each array as currently stored, treating only string references to uniquely occurring event IDs as graph edges. **No cycle involving two or more distinct event IDs occurs in the 95 current timelines.** The only cycle-shaped cases are self-edges in `r8-deps-anomalous/` and `r22-self-repeated/`; both are already diagnosed as self dependencies and tick inversions. This is inventory evidence on current JSON, not an inference about unobserved inputs.

Path:line evidence and prior cases:

- `.shokunin/lore/corpus/fixtures/check_bible.py:253-274`: local member validation, uniqueness resolution and endpoint inversion; no transitive/graph cycle walk.
- `.shokunin/lore/corpus/fixtures/README.md:29-34`: ticks are local nonnegative sequence values, dependency IDs must have strictly earlier ticks, and contradictions prompt editorial review.
- `.shokunin/lore/corpus/fixtures/README.md:159-168`: r8 duplicate/self list behavior, and explicit note that no graph-cycle verification is claimed.
- `.shokunin/lore/corpus/fixtures/README.md:183-191`: r9 unique-target strict-earlier handling and explicit “does not establish … a graph cycle”.
- `.shokuhin/lore/corpus/knowledge/2026-10-12-lore-consistency-checklist.md:5` (path spelling in repository is `.shokuhin`? Actual inspected path is `.shokuhin/lore/corpus/knowledge/2026-10-12-lore-consistency-checklist.md`): timeline acyclicity is marked unmeasured. The actual workspace path should be verified before relying on this line citation.
- `.shokunin/lore/reports/r8-axis-adjudicator.md`: r8 credits repeated earlier prerequisite coverage; self-only was already an equal-tick inversion, and its explicit self diagnostic is clarity rather than another coverage gain. Duplicate IDs remain a separate ambiguity.
- `.shokunin/lore/reports/r9-axis-adjudicator.md`: r9 classifies duplicate target resolution as calibration, not a new consistency-rule class; it does not choose a target tick.
- `.shokunin/lore/reports/r20-axis-adjudicator-retry.md`: strict-order inversion is a local edge comparison, gated on nonnegative, uniquely resolved endpoints; no transitive ordering claim.
- `.shokunin/lore/reports/r22-axis-adjudicator.md`: malformed list members can coexist with independently checked string edges; prior validation is scoped and not universal.

## Observed versus proposed

**Observed:** For any cycle whose edges all have unique IDs and nonnegative integer endpoints, the strict-earlier condition cannot hold around the complete loop: summing the strict inequalities would imply a tick is strictly less than itself. Therefore at least one cycle edge has equal or reversed ticks and the current checker reports at least one `timeline inversion`. In fact, a directed cycle cannot be built from edges all satisfying the declared strict-earlier rule. This proof is about the numeric input rule only. Self loops also trigger existing self/inversion messages. Ambiguous IDs are not resolved for tick comparisons, and malformed members are skipped or handled by existing guards; none should be silently promoted into graph edges.

**Proposed, not observed:** The checklist’s “acyclicity unmeasured” status could be addressed by graph traversal, but a separate cycle diagnostic is not presently shown to improve an editorial decision beyond the already visible inverted edge(s). A cycle label could be additional precision about the shape of a set of input references, but there is no demonstrated operator task or misreading in the inspected prior reports. Do not implement merely to convert an unmeasured checklist row into a measured one.

## Pinned 95/474 replay plan (if a future candidate is independently justified)

1. Use the declared pinned baseline commit `e80757125b609f55aacfdd6bb7385a8e25aed3e8` and preserve the exact repository-root CLI argv, working directory, environment, and checker version. Archive stdout, stderr, and exit status for each of the 95 old fixture invocations; compare each tuple byte-for-byte against candidate tree.
2. Compare the 474 baseline fixture JSON paths byte-for-byte, not merely counts or sizes; record every path-level delta and independently justify each intended change. Include all non-JSON files in a complete path/byte audit if candidate touches fixture corpus or README.
3. Replay the proposed cycle case and matched acyclic case with equal numbers of existing edge inversions. Use distinct, unique IDs, valid schema, nonnegative ticks, and no unrelated occupancy/citation/ID errors. For boundary coverage, ensure malformed dependency members and duplicate/ambiguous IDs are not treated as valid edges. Retain existing per-edge inversion behavior unless an explicit, separately justified policy says otherwise.
4. A result that reproduces a cycle diagnostic or preserves 95/95 and 474/474 is regression evidence only, not by itself a coverage improvement. Require an independently documented operator/editorial decision that depends on cycle identity and is not answered by the emitted inversion path(s); otherwise no candidate should be built.

## Verdict

**COVERAGE: NO-GO (for implementation/admission on current evidence).** No distinct-ID cycle exists in current fixtures; prior self-loop cases already fail locally; and every fully comparable directed cycle necessarily has at least one existing equal-or-later edge finding. No concrete downstream decision requiring cycle identity was found. Checklist status “unmeasured” alone is not evidence of a material coverage gap. Depth and calibration are outside this scout’s proposed move; no material change to either is supported.

**Falsifier:** A minimal, schema-valid distinct-ID cycle and an acyclic control with the same count of inversion findings, plus a concrete editorial task in which the cycle-specific diagnosis changes the operator’s next action and the existing edge-local output does not. Then independently demonstrate boundary-safe graph construction (unique IDs and string members only), preserve all prior outputs via pinned 95 raw stdout/stderr/exit replay and 474 JSON-byte comparison, and obtain non-author review. Without that counterexample to the redundancy claim, retain NO-GO. This is about declared dependency-graph structure only; it does not establish source-text causality, event truth, objective canon, or rights.
