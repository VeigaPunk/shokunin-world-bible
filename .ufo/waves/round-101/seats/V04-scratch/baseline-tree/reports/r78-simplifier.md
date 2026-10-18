# Round 78 LEAF simplifier — copied ledger-side citation

## Recommendation

**Conditional GO for one narrow calibration rule; no checker change is authorized by this report.** The README supplies a relevant authority boundary: a contradiction side is documented as `(event_id, field)`, the event's own source is its citation, and “the ledger does not copy a source, text, or paraphrase that could disagree with it.” This is enough to treat a *present, conflicting* side `source_id` as an inconsistent duplicate pointer, not as a second citation authority. It is not a contract to reject arbitrary extra members or to validate all optional metadata.

If the declared matched probe confirms the clean-versus-conflicting side-copy pair, the smallest defensible behavior is: after the existing side shape, field, unique-event, and event-source checks succeed, emit one side-local diagnostic only when that side contains a string `source_id` different from the target event's `source_id`. Keep the event's source as the sole citation used by existing checks; do not select either citation, resolve the copied ID as a replacement, or cascade into a second set of source diagnostics. Missing `source_id` remains current behavior. Do not broaden to unknown-key rejection, a required side citation, or equality enforcement for arbitrary metadata. If the probe cannot establish a unique target event with a resolvable source, do not infer a conflict; retain existing diagnostics.

## Basis and limits

- Active checker validates required ledger-side `event_id` and `field`, resolves exactly one timeline event, then derives source status from that event. It never reads `side['source_id']`; extra side members are ignored. Thus a different copied ID can coexist with CLEAN, while it does not alter the checker’s effective citation.
- README round 3 gives the side form and explicitly says the event's source is its citation and the ledger does not copy a source that could disagree. This supports a narrow mismatch warning. It does **not** say all unknown keys are invalid. The r3 reviewer likewise observed extra keys are permitted and documented representation—not arbitrary object closure—as the contract.
- Round 63 is a useful caution, not contrary authority: unknown keys are ignored, and a parser-level strictness rule was NO-GO without a producer contract. Here the specific side-citation relationship has README authority; that does not justify general strict-schema behavior.
- A mismatch diagnostic would establish only disagreement between two supplied input fields. It would not establish whether either source exists, supports the event, is authentic, or is true. It must not choose a source or settle a contradiction, chronology, canon, rights, or mechanics.

**Axis:** calibration candidate only; depth and coverage unchanged. **Falsifier:** if the matched control/mismatch does not produce a plausible reader-facing attribution conflict, or independent review finds the README wording is descriptive rather than normative, stop NO-GO rather than generalizing the rule. No source-of-truth inference is made.
