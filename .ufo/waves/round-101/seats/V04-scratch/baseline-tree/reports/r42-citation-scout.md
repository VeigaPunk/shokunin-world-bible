# Round 42 citation scout — source pointers, fields, and limits

## Evidence and boundary

- `.shokunin/lore/LOG.md:700-701` defines this as a calibration candidate, not a new checker branch: change only `claim_a.field` from `place_id` to `description`; it explicitly notes r3 already ran an unsupported-field probe.
- `.shokunin/lore/reports/r3-reviewer.md:15,19-21` confirms the temporary unsupported-field test and states the actual boundary: ledger validation checks selectors, unique event IDs, and resolvable event-source IDs; it does not prove semantic conflict, source support, or entailment. `why` is only required nonempty.
- `.shokunin/lore/corpus/fixtures/check_bible.py:76-100` allows only `place_id`, `tick`, `depends_on`, then resolves a unique event and checks that event's `source_id`. It does not retrieve source text or inspect a selected field's meaning. `.shokunin/lore/corpus/fixtures/check_bible.py:12-14` confirms timeline rows also have a `description` string, but existence in the schema does not make it an admissible ledger assertion selector.
- `.shokunin/lore/corpus/README.md:48-54` says the event's own source is the citation, the ledger copies no source/text/paraphrase, and checker validates pointers/required text—not citation truth or semantic contradiction. `.shokunin/lore/README.md:36-41` likewise separates fictional in-world `source_id` pointers from real-world inspiration.
- `.shokunin/lore/corpus/knowledge/reference-ledger.md:3-10` explicitly separates rights and AI-training-permission questions and attributes method inspiration rather than story facts. These citations do not grant rights or permission.

## Risk / calibration assessment

A documentation-only distinction between “field pointer accepted by schema” and “human semantic reading of attributed prose” is valuable, but not genuinely novel against r3 reviewer evidence and README: r3 already exercised unsupported selectors and clearly bounded the checker as non-semantic. The fact that `description` is a valid timeline field does not demonstrate that it is textual evidence for a contradiction; accepting it as a selector would risk conflating free-form event description with a structured, source-supported claim. Rejecting it establishes only the allowed-selector contract, not that descriptions are false, useless to an editor, or inadmissible in canon. Source-ID resolution establishes pointer identity only; neither it nor a ledger `why` authenticates a source, verifies its contents, establishes attributed report truth, or settles canon. Rights and AI-training permission are separate and unassessed.

**Recommendation: no-go for a calibration admission on this candidate.** The proposed controlled pair could test the existing selector gate, but its asserted semantic lesson is already documented and replayed in r3; relabeling that as new calibration would overstate novelty. Do not infer canon or rights.

## Falsifiable check (if retained as an audit only)

In temporary copies of the r35-derived control, change only `contradictions[0].claim_a.field` from `place_id` to `description`; require the negative to emit the existing `contradictions[0].claim_a.field: expected one of ...` diagnostic, while the unchanged control remains clean. Compare all five JSON files to verify the one-field mutation, then check that the checker did not modify either input. This can falsify the narrow selector-gate prediction, but a pass is not evidence of new semantic calibration, source support, rights, or canon.
