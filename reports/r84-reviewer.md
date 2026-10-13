# Round 84 non-author reviewer — duplicate event labels and occupancy

## Review scope

I independently read the R84 declaration and scout reports, inspected the active checker path, and reviewed the cited R9, R12, R16/R19, R37, R52, and R70 precedent. This is a critical review of the provisional NO-GO, not an axis adjudication. I made no checker or fixture change and did not treat the scouts’ outputs as source evidence.

## Matched pair and current behavior

The temporary matched pair is a useful narrow control: both rows have the same uniquely resolved actor (`mira`), nonnegative local tick (`7`), and distinct uniquely typed places (`harbor`, `tower`); only the second event `id` changes from `pair-event-b` to the already-used `pair-event-a`. The reported raw results are: distinct IDs, one `double-booked` finding; duplicate ID, that same finding plus the separate duplicate-timeline-ID finding. Both have exit 1 and empty stderr. This is consistent with the code: timeline duplicate IDs are diagnosed/indexed separately, while occupancy iterates admitted raw rows, gates on entity availability, one actor match, a unique place of kind `place`, and nonnegative tick, then groups by `(entity_id, tick)` and compares `place_id` (checker lines 269–294). Event-ID uniqueness is not an occupancy gate.

Thus the pair demonstrates output contrast, not a calibration gain. It does not establish that a reader is misled by the extant message, that the two rows have separate event referents, or that their citations support either place assertion. It also does not show that a duplicate label makes the actor/tick/place operands unassessable. In the controlled input the row-field mismatch remains exactly the same under both labels.

## Editor action and conditions must stay separate

The first repair in the duplicate-ID case should address the **event-label/reference condition**: inspect the cited material and determine whether the rows represent separate event records; only if supported, assign distinct IDs and update any dependent references. Do not select the last row, merge/delete one, or invent an event distinction merely to clear the duplicate-ID finding. Preserve both raw assertions while resolving that question. Separately review the **row-field condition**—whether the same actor/tick and different places are supported—and correct or reconcile unsupported actor, tick, or place fields against their citations. The duplicate label neither proves nor disproves that row-field mismatch. In the distinct-ID control, the label repair is absent, but the same source-check of actor/tick/place fields remains necessary; distinct IDs do not cure the row-field condition.

This distinction favors retaining both findings. A duplicate-ID warning points to ambiguous event references; the booking diagnostic reports a structural relationship among supplied row fields. Suppressing the latter can hide an actionable field-level inconsistency. A carefully worded qualifier might help only if evidence showed that editors mistake the warning for a claim about separate real events or sourced truth, and if the qualifier changed a safe repair without obscuring the field check. No blinded reader task, observed misreading, or comparative editor outcome is supplied. The word “double-booked” can invite over-reading, but that possibility alone does not establish a benefit from a duplicate-ID-specific qualifier; source/canon limits should not be smuggled into the checker’s predicate.

## Prior art and NO-GO challenge

The relevant precedents support the provisional NO-GO, with scope limits:

- R9 and R37 handle consumers that must **dereference an event ID** (dependency or ledger endpoint); duplicate cardinality makes the target ambiguous. Occupancy compares rows already present and does not select a row through that ID. These rounds do not authorize making every diagnostic on a duplicated-ID row indeterminate.
- R12’s actor-identity guard, and R16/R19’s place/tick gates, concern actual occupancy operands or eligibility. Those ambiguities can defeat the comparison; the R84 pair holds those conditions eligible.
- R52 is a useful caution, not a direct duplicate-event-ID experiment: ambiguous source IDs did not erase an independently available actor/tick/place collision. It rejected a qualifier absent measured editor benefit. It reinforces the need to separate identity namespaces and avoid propagating one ambiguity to unrelated fields.
- R70 is a materiality warning: changing a diagnostic or preserving all old outputs does not prove a safer first repair; a warning may retain independent repair value. Its event-reference case is not dispositive here.

The strongest counterargument is that a repeated event label could mean the two rows are duplicate descriptions of one event, so a definite-sounding `double-booked` message may prompt someone to change a place field before resolving what the rows denote. But that is a possible workflow hazard, not shown by this pair. The safe first action already separates ID/reference repair from field validation, and a label collision does not establish that one raw row should be discarded. The evidence does not identify a safer action caused by withholding or qualifying the booking finding. On this record, I agree with provisional **NO-GO**: no demonstrated material calibration improvement, while suppression risks losing a distinct row-field finding. Do not infer a gain from the extra duplicate-ID diagnostic or from output parity alone.

## Limits

These are invented, unverified checker inputs. A unique source ID is only structural resolution; it does not establish that a source supports a row. The outputs establish no event truth, actual location or chronology, canon, rights, or game mechanics. Local tick 7 is not a real date. This review makes no such claims.
