# Round 57 — scribe: dependency cycles versus edge inversions

## Observed behavior (not proposed policy)

`check_bible.py:253-274` processes each event’s `depends_on` entries independently: it reports malformed member type (254-259), self/repeat/unknown/ambiguous ID (261-271), then compares a uniquely resolved target and dependent only when both ticks are nonnegative (272-274). There is no graph traversal or cycle diagnostic in this block. A clean checker run means only the implemented structural checks passed; it does not establish source-text support or canon (fixtures/README.md:38-48; decision table:19-21).

The invariant is decisive for admitted edges: every edge in a directed cycle cannot satisfy strict prerequisite-before-dependent ticks. Summing strict inequalities around the loop would require a tick to be strictly less than itself. Thus every cycle with unique IDs and nonnegative endpoints necessarily contains at least one already-reportable inversion. With negative endpoints, r20 explicitly withholds that edge comparison, but reports invalid tick; it does not make the cycle meaningful as a validated chronology.

## Decision table (proposed reader action)

| Input condition | Existing observed output | Proposed practical reader action |
|---|---|---|
| Unique-ID, nonnegative, valid cycle | At least one edge-local `timeline inversion`; no cycle-specific message (`check_bible.py:267-274`). | Inspect the named dependency edge(s) and repair the input schedule/dependency assertion manually. Do not add a redundant cycle alarm or infer causal truth. |
| Valid acyclic graph, same number of inversions | Same edge-local inversion findings, no cycle message. | Same action: inspect reported edge(s). An inversion is enough to identify the violated local ordering convention; no separate cycle finding needed. |
| Negative tick endpoint on a cycle edge | Invalid tick remains; that edge’s ordering comparison is skipped (`check_bible.py:272-274`; decision table:195-205). | Treat ordering as unassessed for that edge; fix/resolve the invalid tick before drawing ordering conclusions. |
| Malformed, self, repeated, unknown, or ambiguous dependency member | Existing local type/identity findings; such member is not a safely resolved graph edge (`check_bible.py:253-271`). | Resolve the input defect first; do not include the unresolved token as an established cycle edge. |

Prior art already bounds the feature. Round 8 adds duplicate-list and self-dependency findings; self-dependency retains same-tick inversion (decision table:101-106; fixtures/README.md:147-168). Round 9 refuses to choose among duplicate event IDs (decision table:110-117; README:170-188). Round 20 withholds edge comparison if either endpoint tick is negative (decision table:195-205; README:414-439). Round 22 inspects valid string siblings despite malformed members, but does not validate a causal graph (decision table:207-218; README:470-495). These are edge/member rules, not graph-cycle coverage.

The initial checklist marks “timeline acyclicity” unmeasured (checklist.md:4-7), but that status alone does not show a material operator gap. The decision table already states that strict tick ordering prevents cycles among events with valid integer ticks (decision-table.md:19-21). The checklist’s broader phrase should not override the observed checker behavior or imply causality.

## Material coverage verdict: NO-GO

Do not implement a cycle diagnostic on this evidence. For structurally valid unique-ID cycles with valid ticks, cycle membership adds no actionable distinction beyond the existing inversion edge report. An acyclic graph with an equal count of inversions presents the same practical task: inspect and correct reported edge(s). The negative-tick and ambiguous/malformed boundaries already have local diagnostics and are unassessed, not silently valid graph edges. A new cycle line risks duplicate noise without changing reader action. This is a coverage NO-GO, not a claim that an explicit graph algorithm is absent from every possible future use case.

## Falsifier

Reverse this NO-GO only with a minimal paired, schema-valid example and observed reader task where cycle membership changes a concrete editorial decision beyond the existing inversion output: a cycle case and an acyclic control with matched inversion count, same relevant local findings, and a documented action the reader can take only from cycle identity. The case must exclude malformed, negative, duplicate/ambiguous IDs and show exact raw checker output. If the pair does not change practical action, retain NO-GO. No automatic correction, sorting, source-text causality, event truth, objective canon, rights, or game-mechanics conclusion is warranted.
