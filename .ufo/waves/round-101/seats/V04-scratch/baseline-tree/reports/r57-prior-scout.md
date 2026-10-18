# Round 57 prior-art scout — dependency graph cycles

## Scope and observed evidence

Read-only audit of the requested round 8/9/20/22 dependency prior art, initial checklist, and current dependency branch. No checker, fixture, README, or LOG file was changed by this scout. The worktree already had `.shokunin/lore/LOG.md` modified at inspection; I did not modify it. I did not run a cycle probe, so no raw CLI cycle output is claimed.

- Initial checklist explicitly lists “timeline acyclicity | ordering graph has no cycle | unmeasured” (`.shokunin/lore/corpus/knowledge/2026-10-12-lore-consistency-checklist.md:8`). This is an unmeasured checklist item, not evidence that the current checker implements graph traversal.
- Current checker does direct per-member processing only: dependency type screen at `.shokunin/lore/corpus/fixtures/check_bible.py:253-259`, then self/repeat/unknown/ambiguous checks at `261-271`, then a unique-target tick comparison at `272-274`. No graph traversal is present in this branch. The active rule is an edge-level ordering check, not explicit cycle detection.
- r8 establishes repeated prerequisite list-member coverage, not graph traversal: `.shokunin/lore/LOG.md:112-116`; adjudicator describes repeated-earlier as newly detected, self as already failing baseline inversion (`reports/r8-axis-adjudicator.md`, “Coverage — improved”).
- r9 establishes duplicate event-ID ambiguity handling, not cycle detection: `.shokunin/lore/LOG.md:128-132`; duplicate target order pair / unique control and adjudication are about refusing last-wins tick interpretation (`reports/r9-axis-adjudicator.md`, “Calibration — Improved”).
- r20 gates inversion comparison on both endpoints being nonnegative; coverage unchanged (`.shokunin/lore/LOG.md:303-306`; `reports/r20-axis-adjudicator-retry.md`, “Calibration improved”). It is not graph traversal.
- r22 allows string siblings in a mixed-type `depends_on` list to be checked while skipping malformed members; coverage improved for previously masked member findings (`.shokunin/lore/LOG.md:331-334`; `reports/r22-axis-adjudicator.md`, “Scope and limits”). It is not cycle detection and does not assess malformed members.

## Observed versus proposed

**Observed:** checklist status remains “unmeasured”; the checker reports direct edge inversions under its existing resolution/tick guards. The four cited rounds address list integrity, ID ambiguity, invalid tick endpoints, and safe member traversal respectively. None of those findings or their listed fixtures demonstrates a dedicated graph-cycle diagnostic.

**Proposed / logical constraint:** under a hypothetical cycle whose every vertex has a unique admitted ID, every edge member is a string and resolves uniquely, and all endpoint ticks are nonnegative integers, strict-earlier constraints cannot all hold around a directed cycle. Summing the strict inequalities around the loop is impossible; equivalently at least one edge must be equal-or-later and current direct comparison reports an inversion. Therefore a cycle finding in this fully eligible domain adds a graph-property label but does not by itself detect an otherwise clean dependency structure. This is a mathematical implication of the proposed domain, not a claim that a cycle fixture was run.

With missing/ambiguous IDs, malformed dependency members, or negative ticks, edges may be unknown, ambiguous, skipped, or unassessed under existing behavior. A graph routine must not silently treat those as valid resolved edges or choose an ambiguous row. Whether graph identity helps an editorial operator beyond existing local diagnostics is unproven here.

## Decision — material COVERAGE: NO-GO

Do not implement a cycle rule on this prior-art evidence. The checklist gap is real as an explicit graph-level checklist item, but the proposed input-level cycle class is not demonstrated to yield a new material finding: in the clean, unique, nonnegative case an existing edge inversion is logically unavoidable; outside that case, the checker’s local findings already expose the respective bad/unknown/ambiguous input condition or leave it unassessed. A graph-level message risks duplicating an existing inversion without a demonstrated operator decision. This is a material coverage NO-GO, not a claim that the checklist item is implemented or measured.

**Falsifier:** a controlled, schema-valid unique-ID cycle with nonnegative ticks, paired against an acyclic graph with the same number and kind of inversion findings, plus a concrete editorial task showing cycle identity leads to a distinct decision that local edge diagnostics do not support. It must retain the existing edge findings; show malformed, ambiguous, unknown, and negative-tick members are never promoted to resolved cycle edges; and demonstrate the cycle report is not redundant/noisier. If this is established, revisit the NO-GO with a minimal scoped proposal and independent replay. No clean checker result, fixture diagnostic, or source citation would establish causality, objective canon, or rights.
