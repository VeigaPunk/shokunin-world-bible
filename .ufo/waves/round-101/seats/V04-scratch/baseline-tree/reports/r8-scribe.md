# Round 8 scribe — bounded decision table and wording

**Scope:** documentation recommendation only. This report records the declared round-8 claim and observed baseline; it does not claim the proposed checker behavior has been implemented or replayed. I inspected `.shokunin/lore/LOG.md` (Round 8 declaration), `.shokunin/lore/corpus/fixtures/check_bible.py`, `.shokunin/lore/corpus/fixtures/contradictions/timeline.json`, and `.shokunin/lore/corpus/fixtures/README.md`. No round-8 fixture or run artifact was present at inspection.

## Bounded decision table (recommended wording)

| `depends_on` case | Recommended checker decision | Boundary / wording |
|---|---|---|
| Empty list or distinct, known prerequisite IDs | No dependency-list integrity finding. Continue existing prerequisite checks. | This only says the listed IDs are distinct; existing tick-order rules still apply. |
| One ID equals the current event ID | Emit one relation-local self-dependency diagnostic at that event's `depends_on` relation/list entry. | Do not remove the ID, rewrite the event, or infer causality from prose. |
| Same prerequisite ID occurs more than once in one event's list | Emit a duplicate-dependency diagnostic for the repeated occurrence(s), local to that event's dependency list. | Count repeated occurrences deterministically; do not deduplicate or alter the input. A self-reference repeated twice may receive both self and duplicate findings, as distinct anomalies. |
| Distinct ID is unknown | Retain existing unknown-event diagnostic. | This round's claim is list integrity, not resolution policy. |
| List contains a non-string value | Retain existing list-value/type diagnostic and current short-circuit behavior. | Do not promise self/duplicate analysis on a malformed list unless implementation separately specifies it. |
| Repeated event IDs or malformed event rows | Keep outside this rule; report using existing event-ID/schema behavior. | Avoid asserting the target event is uniquely identified when it is not. |

## Suggested documentation wording

> Each timeline event's `depends_on` is an explicit list of event IDs. The checker reports a self-dependency and repeated IDs within that one list as relation-local input anomalies; it does not remove or reorder entries. Distinct known prerequisites remain subject to the existing timeline-order check. Unknown IDs and malformed list values retain their existing diagnostics. These checks validate list structure and referenced IDs, not causal truth, source-text support, or game mechanics. The event's `source_id` is checked separately; a dependency-list finding does not add evidence to or alter that citation.

For the paired fixture description, recommend saying the clean case uses distinct prerequisite IDs and the anomalous case changes only the dependency list to include self and repeated entries. Name exact fixture directories and CLI outputs only after those files have been created and replayed; do not state exit codes or finding counts based on the declaration alone.

## Observed baseline and limits

In `.shokunin/lore/corpus/fixtures/check_bible.py`, `depends_on` is schema-typed as a list. The timeline loop checks that its members are strings, then iterates each member to diagnose unknown IDs and prerequisites whose ticks are not earlier than the current event. It has no observed self-ID or repeated-ID check. The existing `.shokunin/lore/corpus/fixtures/contradictions/timeline.json` includes `arrival` depending on `later`, but no self or repeated dependency. Its README-described behavior is an intentional timeline inversion, not a test of this new class. The Round 8 declaration in `.shokunin/lore/LOG.md` likewise identifies duplicate/self dependency IDs as the uncovered class.

These observations support the proposed narrow rule only. They do not establish implementation, new fixture outcomes, replay success, or an axis verdict. Preserve the existing inversion behavior and source-citation checks; report contradictions/anomalies rather than resolving them.
