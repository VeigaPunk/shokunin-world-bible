# Round 78 independent reviewer — copied ledger-side `source_id`

## Verdict

**NO-GO on a checker change on the current record.** The conflict is demonstrably silent to the checker, but silence alone does not establish a misleading review or a distinct repair. Under the documented ledger convention, the side-level value is not a second citation: it is an extra, ignored member. A narrow mismatch diagnostic is conceivable, but the evidence does not yet justify turning this tolerated metadata into a new validation constraint.

## Independent assessment

The active checker path (`corpus/fixtures/check_bible.py`, lines 111–138) reads a side's `event_id` and `field`, resolves exactly one timeline event, and checks that event row's `source_id`. It never reads `side['source_id']`. The generic row loader checks required fields rather than rejecting extras. The r78 probe’s matched copies confirm the consequence: absent, equal, conflicting, and integer-valued extra side `source_id` all remain CLEAN; unresolved endpoint and unresolved actual event source still take their existing diagnostic paths. This establishes checker behavior, not what a person inferred.

README Round 3 is fairly explicit about citation authority: sides are “of the form” `{ "event_id": "...", "field": "..." }`; the event's own source is the citation; and the ledger “does not copy a source ... that could disagree with it.” Read together, this is enough to tell an editor following the documented convention not to use the extra member as an alternate or overriding citation. It is **not** an explicit closed-object schema: the README does not say additional keys are invalid, and checker practice is permissive. R3 reviewer directly observed that sides allow extra keys and judged that not a correctness issue for the then-current fixtures. Thus the README supplies an authority boundary, but not clear policy for rejecting an undocumented extension key.

The distinction matters for materiality. A key named `source_id` with a different value is plausibly confusing to a reader who encounters the JSON without the README, and may look more intentional than arbitrary metadata. But no report or probe demonstrates a reader taking it as citation-bearing, an editor changing attribution, or a downstream consumer using it. R3/r7/r39 concern the event's actual source reference (and its unknown/ambiguous resolution), not this extra value. R63 is useful compatibility caution: permissively ignored extras do not alone establish a false checked result or warrant a new rejection rule. These are limits on inference, not proof that nobody could be confused.

## What repair would differ?

A conflict-only warning, if later justified, should say only that the side's copied value disagrees with the uniquely resolved event's `source_id`; it must not resolve the copied ID, choose either source, or create second-citation diagnostics. The likely immediate repair would be to remove the redundant side member so the ledger conforms to the documented pointer form—not to change the event's source pointer. Changing that event pointer would require separate review of the underlying data, which this checker cannot settle. If an editor instead meant the side value as authoritative, that would be an undocumented schema change requiring an explicit contract and a decision about which source governs. Current evidence shows no such intent. A general extra-key ban would be broader still and unsupported.

## Axes and falsifier

- **Calibration: unchanged; material improvement unproved.** The matched probe confirms the ignored value can coexist with CLEAN, but not that CLEAN materially misleads a reader of this documented format or that a diagnostic changes an independent review decision.
- **Depth: unchanged.** No lore assertion, source support, or interpretation is added.
- **Coverage: unchanged.** No checker candidate or fixture was added; baseline corpus replay is not candidate evidence.
- **Harm: no candidate tested.** A narrow warning may be low-risk, but could encode an unsupported constraint on tolerated metadata; broader extra-key rejection risks compatibility and is not in scope.

A useful falsifier for this NO-GO would be a blind, non-author editor review of matched inputs (absent/equal/conflicting side value) showing that the conflicting value is actually treated as a citation and causes a specific, different repair; then demonstrate that the proposed warning changes that decision without interpreting arbitrary extensions. If reviewers follow README and treat it as inert, or the only proposed repair is removing an undocumented redundant key with no consequential attribution difference, retain NO-GO. No candidate exists to assess.

This review makes no finding about source-text support or authenticity, fictional truth, canon, chronology, rights, or mechanics. No checker, fixture, README, corpus, or LOG changes were made; this report is the only file written.
