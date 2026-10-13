# Round 57 graph scout — cycle coverage

## Observed repository evidence

- `.shokunin/lore/LOG.md:975-976` frames acyclicity as unmeasured, but explicitly predicts strict-earlier ticks force a cycle to contain a non-strictly-earlier edge; it asks whether cycle identity adds a decision beyond inversion.
- `.shokunin/lore/corpus/fixtures/check_bible.py:253-274` inspects dependency members individually. For unique event IDs it emits unknown/ambiguous findings or, when both indexed ticks are nonnegative, emits an inversion if dependency tick `>=` dependent tick. There is no graph traversal here.
- `.shokunin/lore/corpus/fixtures/README.md:30-33` documents dependencies as strictly earlier ticks. Lines 147-168 (r8) cover repeated/self references and explicitly disclaim graph-cycle verification; lines 172-191 (r9) cover duplicate target ambiguity, with no tick comparison. Lines 414-438 (r20) exercise negative/equal/reversed edge boundaries; lines 470-493 (r22) exercise malformed members alongside valid strings. The checklist `.shokunin/lore/corpus/knowledge/2026-10-12-lore-consistency-checklist.md:8` records timeline acyclicity as “unmeasured.”

## Proof and raw probes

Treat each usable dependency as directed from the dependent row to its prerequisite. In any directed cycle of distinct, uniquely identified events, assume every edge satisfies strict earlier ordering: for each edge dependent `u -> prerequisite v`, `tick(v) < tick(u)`. Chaining these inequalities around the cycle gives `tick(u) < tick(u)`, impossible. Therefore at least one cycle edge must fail strict-earlier ordering (equal or reversed); with all ticks nonnegative it triggers the existing inversion check. This proof does not cover edges screened out as malformed, self, unknown, ambiguous, or involving negative ticks.

I made temporary copies of the `r22-valid-order` input under `/tmp` and invoked the active checker without changing repository fixtures. In the cycle probe, the two distinct unique-ID events had ticks 0 and 1 and reciprocal dependency references; output was exit 1 with exactly `timeline[0].depends_on: timeline inversion 'r20-dependent' tick 1 not before 'r20-prereq' tick 0` (one violation). The acyclic control (ticks 0,1; later row depends on earlier) exited 0 with `CLEAN ... 0 violations`. Thus the cycle probe is already caught by existing local inversion; no new cycle-specific report exists. The cycle fixture's source text is not evidence for chronology.

## Prior coverage and distinction

r8 tests repeated/self list anomalies, not a valid multi-node cycle. r9 tests ambiguous IDs and intentionally suppresses comparison for ambiguous references. r20 tests valid-edge inversion/equality and negative endpoint suppression, including mixed edges. r22 tests strings retained beside malformed members and member-order effects. These are adjacent branch coverage, not an executed prior valid-cycle graph probe. Nonetheless, a valid cycle whose vertices are all uniquely indexed with nonnegative ticks is necessarily reported through at least one inversion. An added “cycle” line would restate the same broken ordering constraint, not establish a distinct checker decision. For negative endpoint cycles or ambiguous/malformed edges, a traversal policy would need separate semantics and could incorrectly treat unresolved references as graph edges.

## Assessment

**Material COVERAGE: NO-GO.** The candidate fails the materiality test: the cycle-specific property adds no actionable structural finding once existing inversion output is present. The only demonstrated cycle probe adds zero detection beyond that output; no justified user/editorial decision requiring an additional cycle line is evidenced. Do not implement or broaden interpretation from this probe. An acyclic equal-inversion-count control was not constructed; even if it demonstrates cycles are distinguishable in principle, it cannot overturn the no-go without a demonstrated distinct operator decision worth encoding.

**Falsifier:** a concrete, in-scope consumer must show that identifying which dependency edges form a cycle changes an editorial action that the existing per-edge inversion diagnostics cannot support, and a minimal paired cycle/acyclic input must demonstrate that added decision without interpreting malformed/ambiguous/negative references as valid edges. Otherwise the no-go stands. No causality, objective canon, rights, or source-truth claim is made.
