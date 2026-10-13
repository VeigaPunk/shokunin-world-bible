# Round 84 simplifier — NO-GO

## Recommendation

Make no checker, documentation, or fixture change. The declared calibration premise is not established. The checker can already emit a duplicate timeline-ID finding alongside the occupancy finding; those findings concern different input properties. A duplicated event label does not, by itself, make the two schema-valid timeline rows' actor, local tick, or place fields unresolvable.

## Smallest safe interpretation

Occupancy is built directly from each admitted timeline row, not by dereferencing its event ID. It requires a unique actor entity, a uniquely identified place of kind `place`, and a nonnegative tick; then it groups by `(entity_id, tick)` and compares distinct place IDs. Event-ID counts are used for dependency and contradiction-ledger reference checks, not this occupancy path. Therefore, if two rows independently pass those occupancy gates and assert the same actor/tick at different resolved places, the structural collision remains available even if their IDs duplicate. The duplicate-ID error already exposes the labeling defect. No cited evidence shows that an editor should disregard or qualify the raw row-level comparison solely because the labels collide.

An ID-ambiguity guard or qualifier would risk suppressing/weakening an actionable structural finding. That could conceal the exact actor/tick/place conflict still present in the input; this is a plausible harm, not proof that every such pair represents two real events. Conversely, keeping the current diagnostic does not establish that either event occurred, that a citation supports it, or that fictional canon conflicts. Do not infer real dates or locations from local ticks.

## Relevant prior art and boundary

- Round 9 (`reports/r9-index-scout.md`) documents last-wins event indexing and count-guarded versus unguarded **event-reference** consumers. Its dependency ambiguity fix does not imply that occupancy should dereference event IDs; occupancy does not.
- Round 37 (`reports/r37-duplicate-scout.md`) concerns duplicate IDs at contradiction-ledger endpoints, where pointers must resolve to exactly one event. That is distinct from row-wise occupancy.
- R12/R16 occupancy work establishes actor/place eligibility gates; R19 preserves negative-tick findings without treating those rows as comparable occupancy. These checks support staying with actual occupancy fields, not adding event-ID dependence.
- R52 (`reports/r52-pair-scout.md`, `r52-axis-adjudicator.md`) found that source ambiguity can coexist with a raw occupancy collision, but rejected an unmeasured wording change. R70 (`reports/r70-critic.md`, `r70-axis-adjudicator.md`) likewise rejected an unproven event-reference warning gate because the warning could retain useful repair value. Neither is direct proof for R84, but both caution against changing diagnostics absent a demonstrated safer editor action.

## Axis / trade assessment

No demonstrated calibration improvement, no documentation need established, and no fixture-only change justified: **NO-GO**. Withholding the `double-booked` diagnostic on duplicate event IDs could harm coverage/actionability by hiding a valid structural comparison. Retaining it risks over-reading the word “double-booked” as a real-world/canon conclusion; existing checker output is structural only, and no cited evidence shows a targeted qualification would materially improve editor decisions without that tradeoff. No change is safer than either an ungrounded suppression or an untested qualifier.

This is not a claim about the truth of fictional source text, canon, rights, or mechanics. Structural citations and checker results establish no such conclusion. No checker, corpus, fixture, README, LOG, or config change was made.
