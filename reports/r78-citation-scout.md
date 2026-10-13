# Round 78 citation scout — ledger side pointer boundary

## Scope and verdict

Report-only audit of the r78 pre-dispatch declaration, active `check_bible.py`, fixture README, and relevant r3/r7/r39/r63 prior reports. I made no checker or fixture changes and did not test a new fixture. **GO for the narrow structural reading that a contradiction side points by `(event_id, field)` and the target event supplies the in-world source pointer. NO-GO for treating an extra side-level `source_id` as an authoritative citation, as source authentication, or as evidence of source-text support.** The audit does not establish that such an extra field materially misleads users or warrants a checker policy change; that belongs to matched behavior and independent review, not citation inference.

## Actual pointer path

The active checker requires each side to be an object with a nonempty `event_id` and an allowed `field` (`place_id`, `tick`, or `depends_on`). For a locally valid side, it resolves `event_id` against `timeline.json`; only exactly one admitted event proceeds. It then gets the source ID from that event row (`event['source_id']`) and checks the ID's status against valid rows in `sources.json`. An unknown event-source ID produces the side-local “has no resolvable source_id” finding; an ambiguous ID is checked/reported as ambiguous. The side's own extra `source_id`, if present, is not read or compared. In code, extra side properties are tolerated, so a conflicting copy could coexist with this path without replacing the event's actual source pointer.

This distinction is visible in the clean/contradiction examples: `contradictions.json` sides point to `arrival.place_id`, `false-sighting.place_id`, and the two dependency/tick fields; corresponding source IDs reside on the referenced timeline rows (`courier-log` or `archive-ledger`). The r3 README explicitly documents side form `{ "event_id": "...", "field": "..." }`, says the event's own source is the citation for the assertion, and says the ledger does not copy a source, text, or paraphrase that could disagree. Thus a copied side `source_id` is outside the documented pointer form, even though the implementation allows extra members.

## Do not conflate four layers

1. **In-world pointer resolution:** unique `event_id` plus allowed field locates an input row/field; that row's `source_id` is checked for a unique matching source row. These are supplied-data identity/index checks only.
2. **Source prose and support:** checker never opens a source excerpt or decides whether its wording supports the event/field. A resolvable source ID does not show that its record says the claim, that a quote is exact, or that a paraphrase is faithful.
3. **Authentication / world truth:** neither the side pointer nor the event's source ID authenticates a record, verifies testimony, proves the event happened, or establishes canon/chronology. The ledger's nonempty `why` is not semantically validated either.
4. **Real-world rights:** `knowledge/reference-ledger.md` is for real-world method references, separate from fictional `sources.json`; it expressly does not grant or assess reuse rights or AI-training permission. This task makes no copyright, license, reuse, training-permission, or ownership finding.

## Prior-report boundary and implication

R3's reviewer/verifier describe the ledger as structural pointers/citations, not semantic contradiction verification. R7 and R39 distinguish unique/ambiguous/unknown source-ID resolution from source-text support and testimony truth. R63 citation-scout likewise separates input/parser validity from source truth and rights. These precedents support the layer boundaries above; they do **not** establish whether readers would mistake an undocumented copied side field for the actual source, or whether adding a diagnostic would materially improve a review decision.

The declaration's hypothesis is accurately framed as a possible supplied-input attribution ambiguity, not a source-truth finding. But because the active code ignores that side copy, any “conflict” is between an inert extra member and the event's operative pointer, not two citations the checker resolves. README's documented `(event_id, field)` form helps constrain interpretation. I cannot conclude from code alone that the extra member is harmless to every reader, nor that it is a second supported citation authority. Conversely, its tolerated presence is not proof of a corrupted source or false event.

## Limits / recommendation

Do not use a side-level `source_id` to cite, authenticate, or override the target event's actual `source_id`; inspect the event row for the checker-resolved pointer and the source record/excerpt separately for any manual support review. If r78 proceeds with a matched probe, report only whether the active checker diagnoses or ignores the copied extra field and whether a reviewer faces a different repair decision. Do not turn that result into a claim about prose, authenticity, rights, chronology, mechanics, or canon. **Citation-scout disposition: conditional GO for this pointer map; NO-GO on any broader source-truth/citation-support claim and no independent basis here for checker-policy admission.**
