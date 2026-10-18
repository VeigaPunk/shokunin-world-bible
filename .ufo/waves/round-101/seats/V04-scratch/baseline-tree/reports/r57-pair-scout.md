# Round 57 pair scout — cycle versus equal-inversion acyclic control

## Scope and evidence

Read-only scout; no checker, fixture, README, or LOG edits. Evidence below is repository source/document inspection, not new raw CLI measurements. Active checker’s dependency handling is `corpus/fixtures/check_bible.py:253-274` (repo-relative `.shokunin/lore/`): it checks member type, self, repeated ID, unknown/duplicate event-ID resolution, then compares uniquely resolved nonnegative ticks and reports `timeline inversion` for prerequisite tick >= dependent tick. It does not traverse reachability or detect cycles explicitly.

Prior art cautions against claiming unmeasured behavior. The checklist marks “timeline acyclicity” as unmeasured (`corpus/knowledge/2026-10-12-lore-consistency-checklist.md:8`). Round 8 dependency scout discusses direct checks/list integrity and explicitly bounds them from traversal (`reports/r8-dependency-scout.md`, recommendations near end). Round 20 dependency scout records equality as inversion and unique endpoint/nonnegative boundaries (`reports/r20-dependency-scout.md`, Raw observations). Round 22 member scout records malformed-list-wide skip behavior (`reports/r22-member-scout.md`, Raw observation); avoid malformed members in this candidate. Fixture README establishes tick/dependency convention and says checker validation is not truth/canon (`corpus/fixtures/README.md`, “No file is modified…” paragraph).

## Minimal controlled pair (proposal, not observed)

Use two uniquely identified events A and B, both nonnegative ticks, with valid schema/source/entity/place fields, distinct actors/slots to avoid occupancy noise. Cycle input: A tick 1 depends on B; B tick 1 depends on A. Exactly one strict-earlier inversion per directed edge under current rule (actually both edges invert: each prerequisite tick 1 is >= dependent tick 1). Acyclic control with same two nodes and same number of inversion edges: A tick 1 has no dependencies; B tick 1 depends on A **would have zero inversions**, so instead use B tick 1 depends on A tick 1 (equal tick), and add another forward edge only if node count permits. Cleaner three-node pair:

- Cycle: A(1) depends B(2); B(2) depends A(1); C(3) independent. Exactly one inversion (A→B prerequisite reference from tick 2 to dependent tick 1); the other edge is valid.
- Acyclic control: A(1) independent; B(2) depends A(1); C(3) depends B(2), with one edge reversed to create exactly one inversion if needed: set C(1) depends B(2), but then topology A→B and B→C is acyclic and there is one inversion. Pair both have three unique IDs, two edges, one inversion, same tick multiset {1,2,3}; cycle fixture edges A depends B and B depends A, ticks A=1 B=2 yields one inversion, C=3 isolated. Acyclic fixture edges A depends B and B depends C, assign A=1, B=2, C=3, also exactly one inversion (A depends B); same counts/ticks.

All dependency members must be strings, distinct within each list, point to unique existing IDs; no self, duplicate-ID, unknown, negative tick, or malformed-list condition. Capture raw checker stdout/stderr/exit for both, plus JSON diff and prove counts. The active checker is expected to flag inversion(s) but currently has no cycle-specific output; this expectation requires a fresh raw probe before calling it observed.

## Coverage judgment

**Material COVERAGE GO:** NO-GO on present evidence. An additional graph-cycle line may merely restate an already emitted inversion; the proposed matched pair tests whether topology is independently visible, but no editorial task demonstrating a decision improved beyond locating the inversion has been evidenced. Checklist “unmeasured” is not itself a user need. Do not implement based on this scout alone.

**Falsifier / revisit condition:** demonstrate a concrete editorial review task where knowing the multi-edge dependency loop (rather than the existing inversion edge) changes the operator’s next action; then run the minimal pair and show cycle-specific reporting only for the cyclic member, preserving existing inversion and all clean outputs. If the acyclic control produces equivalent actionable information, or the cycle report adds no distinct action, keep NO-GO. A clean checker result or graph diagnostic must not be described as causal verification, objective canon, rights clearance, or event truth.
