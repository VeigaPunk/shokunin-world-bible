# Round 57 simplifier — graph-cycle proposal

## Observed evidence

- Active dependency loop is `.shokunin/lore/corpus/fixtures/check_bible.py:253-274`. It emits list-type, self, repeated, unknown/ambiguous-ID findings and, for uniquely resolved nonnegative endpoints, a direct strict-earlier inversion finding (`:272-274`). There is no traversal or cycle-specific diagnostic in this loop.
- The initial checklist labels “timeline acyclicity” unmeasured (`.shokunin/lore/corpus/knowledge/2026-10-12-lore-consistency-checklist.md:4`). That records a proposed checklist question, not evidence that the checker is required to calculate cycles or that the underlying timeline is cyclic.
- Prior dependency work bounds this scope: r8 simplified self/repeated list integrity without a graph engine (`.shokunin/lore/reports/r8-simplifier.md`, “Smallest implementation recommendation”); r9 addresses ambiguous duplicate IDs before tick comparison (`r9-simplifier.md`, “Smallest exact-one guard”); r20 restricts inversion comparison to nonnegative endpoints (`r20-simplifier.md`, “Recommendation”); r22 distinguishes malformed members (`r22-simplifier.md`, “Recommendation”). These existing local rules should not be bypassed by graph traversal.

## Simplest honest disposition: NO-GO

Do not add cycle detection on this evidence. Under the present convention, every uniquely resolved edge in a candidate cycle whose endpoints are nonnegative must satisfy strict prerequisite-before-dependent tick order to avoid an inversion. Around a directed cycle those strict inequalities cannot all hold; at least one cycle edge therefore already produces the local inversion diagnostic. A graph-level line would be a second description of the same rejected ordering edge, not demonstrated new material coverage. A cycle detector would also need to define which edges count when IDs are unknown/ambiguous, endpoints are negative, or list members malformed; the current findings intentionally localize those conditions.

A new graph pass, cycle fixture, or README rule is not proposed. The cycle may be an interesting structural description of the input dependency references, but no evidence here establishes an operator decision improved beyond the existing inversion and anomaly reports. No causal assertion follows from a `depends_on` field.

## Material axis verdict

**COVERAGE: NO-GO (no material gain demonstrated).** Keep the existing per-edge checks; make no checker or fixture change. This is a decision on this candidate, not a claim that graph cycles are never useful.

**Falsifier:** present a schema-valid, uniquely identified, all-nonnegative cyclic input and a concrete editorial task where identifying the cycle as a whole changes the operator’s next decision beyond the specific inversion line(s); demonstrate that existing output does not already let the operator locate the blocking edges, and show that a narrowly defined cycle diagnostic adds that decision without duplicate noise or changing malformed/ambiguous-edge handling. Then compare against an acyclic control with the same inversion count and replay the pinned regression corpus. Until then, no-go.

This report distinguishes checker behavior from proposed semantics. It establishes neither event truth, source-text causality, objective canon, nor rights.
