# Round 57 critic — dependency-cycle coverage

## Verdict

**Material COVERAGE: NO-GO.** Do not implement a cycle diagnostic on the present evidence. The checklist identifies acyclicity as unmeasured, but that is a broad checklist item, not proof that the checker currently misses an actionable error. With unique event IDs, string dependency members, and nonnegative ticks, any directed cycle must contain at least one edge whose prerequisite tick is greater than or equal to its dependent tick. The active checker already reports that edge as a `timeline inversion` (strict-earlier rule); thus a cycle line does not newly reject an otherwise accepted graph. The relation's graph-cycle identity could be informative, but no demonstrated operator task shows it changes a decision beyond the existing indexed inversion. Do not count “cycle detected” as material coverage merely because it labels the same invalid ordering more globally.

## Evidence observed

- `.shokunin/lore/corpus/fixtures/check_bible.py:253-274` processes each dependency member; non-strings are skipped after the row-level type warning (`254-259`), self/repeated IDs are diagnosed (`261-266`), unknown and duplicate event IDs are excluded / marked ambiguous (`267-271`), and only uniquely resolved endpoints with nonnegative ticks get the strict-earlier inversion comparison (`272-274`). There is no graph traversal.
- `.shokunin/lore/corpus/knowledge/2026-10-12-lore-consistency-checklist.md:4` lists “timeline acyclicity” as unmeasured. It does not specify treatment of malformed references or establish an unmet editorial need.
- README Round 8 documents that the `r8-deps-anomalous` self-edge already emits both a self-dependency and equal-tick inversion; the distinct earlier control is clean (`corpus/fixtures/README.md`, Round 8 section). I reran both: anomalous emits repeated-prerequisite, self-dependency, and inversion; control is clean.
- README Round 9 documents ambiguous event-ID targets as not eligible for a tick comparison (Round 9 section). I reran `r9-dup-low-high` and `r9-dup-high-low`: each reports duplicate ID and `ambiguous dependency event`, identically under target-row reversal; unique control is clean. A graph pass must not choose a last-wins node or invent an edge endpoint here.
- README Round 20 documents that negative endpoint ticks retain invalid-tick diagnostics but are withheld from definite ordering comparison (Round 20 section). A graph pass treating raw negative ticks as valid ordering evidence would create a false assurance or false cycle claim; treating them as graph edges still cannot imply chronology.
- README Round 22 documents that non-string members are skipped while string siblings are still checked (Round 22 section). My rerun of `r22-clean-inversion`, `r22-mixed-last`, and `r22-mixed-first` confirms the mixed lists retain the same string-edge inversion plus a type warning. A graph pass must not coerce `null`/objects/arrays into IDs or let a malformed member fabricate adjacency.
- I reran `r20-valid-order` (clean), `r20-valid-inversion` (one inversion), `r20-valid-equal` (equal-tick inversion, plus independent booking), and `r20-mixed-edges` (negative endpoint tick finding plus a separate valid-to-valid inversion). These show existing local findings survive independent edges; they do not demonstrate that a graph-level duplicate finding adds a new corrective action.

These CLI observations are checker-input behavior only. The sources are fictional ID references; none of this establishes source-text causality, objective chronology, canon, or rights.

## Proposed vs observed

**Observed:** There is no explicit DFS/SCC/cycle check in the active loop. Unique nonnegative valid cycles cannot evade all strict-earlier edge checks. Duplicate targets, malformed members and negative ticks have explicit existing uncertainty boundaries.

**Proposed, not observed:** A future graph diagnostic could name a cycle path after filtering to uniquely resolved event IDs and valid string edges, while preserving all current local diagnostics. That would be a new *label*, not proven material coverage. It could also generate redundant noise, especially when a long cycle yields multiple inversions, or false positives if an implementation builds adjacency from malformed/ambiguous rows. No implementation or graph probe is authorized by this critic assignment.

## Falsifier / reconsideration gate

Reconsider only if a paired, schema-valid unique-ID graph demonstrates a concrete editorial operation that cannot be performed from the existing per-edge inversion(s), and an independent operator can show that cycle-path output changes that operation. Include an acyclic control with the same number of inversions, plus malformed-member, duplicate/ambiguous-ID, and negative-tick boundaries; require no new cycle claims from excluded edges and exact regression replay. If the only difference is naming the already-reported inversion cluster, material coverage remains **NO-GO**. No checker/fixture/README/LOG edits were made.
