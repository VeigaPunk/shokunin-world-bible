# Round 6 independent review — provenance checker and fixtures

## Scope and raw replay

Read the active raw checker (`corpus/fixtures/check_bible.py`), both raw `item-chain-*` fixture trees, the round-6 LOG clarification, fixture README, and executor/critic reports. The checker has an optional `provenance` field on entities (not a separate table). I independently invoked the CLI for 12 committed inputs, using the documented root-relative command; stderr was empty in all 12:

| Input | Exit | Observation |
|---|---:|---|
| `consistent` | 0 | `CLEAN` |
| `contradictions` | 1 | Same three seeded findings: dangling `missing-map`, inversion, double-booking |
| `ally-reciprocal` | 0 | `CLEAN` |
| `ally-one-way` | 1 | Missing reciprocal finding |
| `contradictions-ledger-malformed` | 1 | Its ledger finding plus the same three seeded findings |
| `r5-missing-file` | 1 | Missing `contradictions.json` |
| `r5-invalid-json` | 1 | Invalid JSON in `contradictions.json` |
| `r5-wrong-top-level` | 1 | Expected array |
| `r5-row-shape` | 1 | Expected object |
| `r5-invalid-citation` | 1 | Unknown `absent-source` |
| `item-chain-valid` | 0 | `CLEAN` |
| `item-chain-broken` | 1 | Exactly one local chain-break violation at `entities[3].provenance[2]`; expected `harbor`, got `mira` |

The new fixture directories are byte-for-byte the same in `sources`, `relations`, `timeline`, and `contradictions`. Their only difference is `entities[3].provenance[2].from_holder` (`harbor` versus `mira`). Each has a `seal` item with a null-predecessor initial record at tick 0 and cited records at ticks 3 and 4. The pair isolates the declared predecessor mismatch well. Existing baseline outcomes above reproduce; no claim about their historical stdout bytes is needed for this review.

## Adversarial behavior probes

I called the imported checker against in-memory copies of the valid fixture, changing one aspect per probe (these are review probes, not committed fixtures):

- Equal and descending provenance ticks each emit a local strict-increase diagnostic; rows are not sorted. The implementation updates its reference tick afterward, so subsequent checks follow input order.
- An initial non-null `from_holder` emits the first-record chain-break diagnostic.
- A boolean tick is rejected as not an exact nonnegative integer.
- Missing provenance passes; an empty provenance list also passes.
- Provenance on a non-item is reported.
- Duplicating the item ID or a referenced holder ID emits the existing duplicate-entity-ID finding, but suppresses chain judgments (no misleading chain-break conclusion). Duplicate IDs are not silently selected by the entity index for this rule.
- Duplicating a source ID emits the existing duplicate-source-ID error, but provenance chain judgments still run; source lookup checks membership in the last-write-wins source index. Thus the checker does not establish unambiguous source identity when IDs collide. This is an existing global indexing weakness exposed at the new citation boundary, not evidence that the source text supports a record.

A malformed provenance row (wrong keys/type, unresolved endpoint/source) emits a shape/reference diagnostic and disables chain judgment for that row and the remainder of that item's sequence. Later valid rows are still shape-checked but not chained. This is conservative and avoids inventing a predecessor, though the CLI does not say chain checking was suspended.

## False positives and semantic limits

The tested rule is an explicit *data convention*, not evidence of factual custody. A resolvable source ID does not attest that its record supports the asserted holder/tick. The initial null-predecessor row declares an acquisition/starting holder by convention; it does not establish that this is the item's actual first holder. No source conflict is reconciled, no missing intervals/transfers are found, and no continuity is inferred from the clean fixture's `carries` relation or claims. Transfer ticks remain local to this list, not comparable to timeline ticks. These limits are stated in LOG/README and the diagnostics do not say which assertion is true.

No false positive appeared in the paired fixture or the 12-case replay. Ordinary, unrelated bibles without provenance remain accepted. Explicitly present but malformed provenance is an error, as declared. The output label for the successful new case still says `CLEAN: schema, citations, relations, timeline` and omits provenance; this is an underinclusive success summary (not a false claim that transfer semantics were proven). It may be worth including provenance in that label if CLI summaries are intended to enumerate checks.

One semantic edge to keep visible: after a chain mismatch, the checker retains that record's `to_holder` as the next row's expected predecessor. This follows the declared “retain both records” / list-order convention and does not choose between sources, but a later row can consequently receive a follow-on mismatch relative to a disputed row. Diagnostics should be understood as local consistency findings, not a reconstructed canonical chain.

## Assessment

The implementation matches the clarified narrow contract on the tested cases: optional/no-inference behavior, explicit initial record, exact record shape, resolvable IDs, unambiguous item/holder IDs for chain comparisons, input-order increasing ticks, local predecessor diagnostics, and no inference from other lore fields. The clean/broken fixture pair is appropriately minimal. Duplicate source IDs remain an ambiguity caveat: the general checker reports them, while the provenance loop nevertheless performs chain checks against the cited rows. The work supports a bounded coverage improvement, not complete provenance verification or canon truth. No code or fixture edits made.
