# Round 75 scribe — bounded README documentation recommendation

## Scope and evidence boundary

This is a report-only documentation outline, not a checker/fixture result. The Round 75 LOG claim proposes detecting an **exact repeated relation input record** in one `relations.json` array, identified by the same directed `from`, `to`, `type`, and `source_id` values. The active checker validates required relation fields, endpoints, source-ID membership, and a sourced reciprocal convention for eligible `allied_with` records; its relation pass contains no general exact-row repetition test. The baseline inventory cited in LOG found no exact repeated tuple among the 132 shipped fixtures. `consistent/relations.json` has one `mira -> seal / carries / courier-log` row. These facts establish an uncovered input pattern, not that its future diagnostic is implemented or that every repeated row is erroneous in the fictional world.

Relevant precedent: fixtures README rounds 7–9 distinguish duplicate IDs and duplicate entries in an explicit dependency list as input-structure rules, while preserving raw records and declining canon/causal inference. Round 7 is especially pertinent: repeated source IDs make citation identity ambiguous; a unique source ID still establishes membership only, not that the source prose supports a relation. Round 2’s reciprocal-edge convention is relation-type-specific and should not be generalized into a universal relation uniqueness rule. Round 45’s critic/scout reports likewise illustrate the need not to turn an author-created fictional report or a kind label into proof of a general semantic convention. None establishes that duplicate relation rows are impossible or that distinct sources necessarily independently corroborate a claim.

## Narrow README placement and proposed wording

If a candidate is implemented and independently replayed, add a short subsection to `.shokunin/lore/corpus/fixtures/README.md`, near the existing relation/citation notes (or after the Round 2 relation convention), and link the exact matched fixtures/run evidence. Keep it explicitly input-scoped. Suggested text:

> **Exact repeated relation rows.** In this checker’s narrowly defined input rule, an exact duplicate means a later admitted record in the same `relations.json` array has the same directed `from`, `to`, `type`, and `source_id` fields as an earlier record. The diagnostic points to the repeated input row; it does not delete, merge, or choose records. A row with a different `source_id` is not an exact duplicate under this rule, even when its directed endpoints and type match. Such rows may represent separately attributed fictional reports, but the checker does not establish that their sources are independent, that either source text supports the relation, or that the relation is true. Reverse-direction rows and rows with a different relation type are outside this exact-match rule. This is a structural duplicate-input finding, not a conclusion about source truth, canon, rights, or game mechanics.

Then add only measured fixture names, commands, exit status, diagnostic location/output class, and a short boundary paragraph. The documentation must not call a different-source row “independent corroboration” as fact: `source_id` is only an in-world reference, and two IDs could still describe dependent or duplicate accounts. Avoid stating that all repeated relation assertions are invalid, that one assertion is canonical, or that a unique source ID validates its contents. Do not claim the check is semantic deduplication or detects equivalent assertions expressed with different IDs/field values.

A matched fixture explanation should make the boundaries visible without implying broader coverage:

| Input relation records | Exact-repeat rule classification | What it does **not** establish |
|---|---|---|
| Same directed endpoints, type, and same source ID repeated | Candidate exact structural duplicate (subject to measured checker behavior) | Whether the cited fictional report is true or the relation is non-canonical |
| Same directed endpoints and type, but distinct source IDs | Not an exact duplicate under the proposed key; retain both records | That sources are independent, mutually corroborating, or support the same claim |
| Reverse direction, or a different relation type | Outside this proposed exact-key rule | Whether that relation is valid, reciprocal by convention, or canon |

Only include this table if the matched controls actually exist and their raw output has been replayed; otherwise document no outcomes and leave wording explicitly proposed. In particular, distinct IDs are an input distinction, not a verified account lineage or rights/provenance conclusion.

## Limits, decision, and falsifiers

**Conditional GO for this narrow README outline** after candidate behavior, fixture distinctions, and regression replay are confirmed. The text may describe the structural key and distinguish same-source exact duplicate input from records bearing distinct source IDs. It should describe any warning/violation status exactly as observed, not promise an unmeasured output or imply a source-text review capability.

**NO-GO** for a broad “duplicate relations are invalid” policy, for treating all same-endpoint/type rows as duplicates, for calling different-source rows independent corroboration, or for claiming canon/source-truth/rights/mechanics outcomes. Also NO-GO for asserting coverage improvement or adding a results table before candidate and matched-control evidence is available. This scribe has not run a candidate or raw tuple replay and cannot adjudicate materiality/calibration.

Key unresolved risk: the schema does not by itself say whether repeating an identical row under one source ID is redundant serialization or two intentional references/mentions to the same in-world record. A future implementation would need a non-author review of that representation assumption; doc caveats alone do not prove the assumption safe. If legitimate same-source repetition is meaningful under the schema, a hard violation may harm calibration even though the duplicate is structurally detectable. Independent verification should ensure distinct-source controls remain unflagged, reverse/different-type rows are untouched, old raw CLI tuples are preserved if required by the LOG gate, and no prose claims source authentication or canon.

No README, checker, fixture, LOG, or corpus file was edited. This report is the sole output for the assigned scribe lane.
