# Round 61 — citation-scout independent calibration judgment

## Verdict

**NO-GO on material new calibration at this stage.** The proposed unavailable-source distinction is sensible as a potential truth-preserving diagnostic refinement, but current evidence establishes only that the existing checker emits cascaded unknown-ID messages when sources cannot load. It does not establish a compelling downstream false conclusion or a safely bounded policy with tested outputs. Recommend no checker/fixture change absent a matched, broader probe and reviewer evidence.

## Observed evidence (not proposal)

- `corpus/fixtures/check_bible.py:41-57` sets `loaded=False` and substitutes `rows=[]` on JSON read/parse failure (lines 43-51); non-array input is also replaced with `[]` at 52-54, but does not set `loaded=False` for that case. Sources have no availability flag (contrast `entities_available`, lines 38,55-56).
- `:79-100` constructs the source ID count from admitted rows; `source_status()` returns `unknown` for count zero, and `source()` emits “unknown in-world source” (lines 90-100). `:122-126`, `:136-142`, `:157`, `:217-221`, and `:273` consume that membership status. `:237-255` uses source membership to qualify reciprocal allied relations.
- I copied `r39-ledger-source-unique` to a temp directory, removed `sources.json`, and ran the checker. It exited 1 and printed the direct `sources.json: cannot load JSON` plus 19 derived diagnostics (two ledger event-no-resolvable-source messages and unknown source-ID messages across entity first-appearance/claims, relation, and timeline). Thus the exact cascade is observed; it is not proof those IDs/text are absent.
- Prior precedent: r31’s unique/ambiguous source-ID pair tests membership cardinality (review `reports/r31-reviewer.md`, especially pair/replay); r32 shows malformed rows are excluded from admitted counts (`reports/r32-reviewer.md`, pair interpretation); r39 tests the zero-match ledger endpoint while source table is loaded (`reports/r39-reviewer.md`). R60 deliberately added table-availability semantics only for entities and cautioned against automatic generalization (`reports/r60-axis-adjudicator.md`, limits). R39 therefore does not already establish unavailable-source semantics.

## Proposed distinction and evidence gap

A possible future calibration: if the whole source registry fails to load or is non-array, report that direct loader/schema error, withhold only conclusions derived from absent source-ID membership (unknown/ambiguous, ledger “no resolvable source_id,” and source-gated certainty/reciprocity), while continuing independent structural checks. Keep ordinary unknown IDs when a valid source array loaded (even empty); retain ambiguity when duplicate valid IDs occur. Treat retained valid rows in a partly malformed array consistently with the established row-filter behavior, not as proof of completeness.

This remains a proposal, not observed checker behavior. Before adoption, compare source-unavailable, loaded-empty, loaded-partial, loaded-ambiguous, and malformed/non-array cases with the four other tables byte-identical. Exercise direct entity/claim/relation/timeline/provenance citations, both ledger endpoints, and allied reciprocity; show independent tick, dependency, entity, ledger-shape and relation checks survive. The current single temp deletion only confirms cascades, not these controls or collateral behavior.

## Falsifier, harms, and boundaries

**Falsifier:** a matched probe showing no material distinction in user-facing conclusions (for example, loader diagnostics plus unknown IDs are deliberately the desired complete report), or showing that source-only suppression hides independently actionable findings, would reject this candidate. Conversely, concrete downstream misuse of cascade wording plus tests proving narrow suppression preserves independent checks could justify a later GO.

Possible harm: suppressing affected-reference listings reduces useful triage and may hide true, independently unknown citations; an overbroad availability gate could suppress unrelated validation or create false confidence. Do not turn unavailable into CLEAN, resolved, or “source exists.”

ID membership is not cited textual evidence: the checker does not dereference source content here. A matching ID does not establish that source text supports a claim, that source is reliable/true, or that an event happened. Neither membership nor these diagnostic states decide fictional-world absence, chronology, canon, rights, licensing, ownership, or permission. Keep the source/canon/rights boundary explicit.
