# Round 84 critic — duplicate event IDs and occupancy

## Verdict

**The declared withholding premise is falsified on the checker’s stated input-structural terms.** A duplicate timeline `id` makes a reference to that ID ambiguous; it does not make the two admitted raw timeline rows disappear, merge, or become unavailable for the occupancy comparison. If both rows independently contain a uniquely resolved actor ID, the same nonnegative local tick, and distinct uniquely typed place IDs, they are two supplied structural assertions that satisfy the checker’s booking predicate. The duplicate-ID diagnostic and definite input-structural `double-booked` diagnostic can both be warranted. Withholding the latter solely because the rows share an event label would discard an independently witnessed input conflict, not improve calibration. This is a **NO-GO** for the proposed suppress/qualify rule absent a different, demonstrated user-facing misreading that does not conflate row identity with event-reference identity.

## Code-path evidence

The active checker counts timeline IDs and reports duplicates separately (`corpus/fixtures/check_bible.py:45–62`). Its occupancy pass later iterates `for location, row in data['timeline']` over the admitted timeline rows (`:269–294`). For each row it checks actor count, place resolvability/kind, and nonnegative tick; if eligible, it keys occupancy by `(row['entity_id'], row['tick'])` and compares the current `place_id` with the prior row’s place (`:288–294`). The event `id` and its count do not occur in that predicate. `source(row['source_id'], ...)` is also called separately (`:285`); source status is not the occupancy gate. Therefore duplicate IDs can create a separate reference ambiguity while the two raw rows still provide both operands for the structural comparison.

This is not equivalent to resolving a dependency or ledger endpoint *by* a duplicate ID. The r9/r37 prior art treats such an ID lookup as ambiguous and refuses to choose a row; r37’s duplicate-ledger endpoint is non-unique precisely because it must dereference the ID. Occupancy need not dereference either row by ID: it is comparing the two rows already present in the input list. No row selection or “first/last event” assumption is needed.

## Falsification and controls

The discriminating pair proposed by the declaration holds actor, local tick, and distinct typed places constant and changes only whether the two rows’ IDs are equal. If those raw rows are otherwise schema-valid and meet the existing gates, the checker’s occupancy result should remain the same in both cases; only duplicate-ID/reference findings differ. That is the appropriate matched probe and the relevant baseline is the raw row pair, not the uniqueness of its label. A duplicated ID may make claims *about which single event a pointer denotes* unassessable. It does not erase the fact that one input row says place A and another says place B for the same uniquely identified actor/tick.

Prior rounds reinforce the distinction rather than support the proposed gate:

- R12 withheld booking when the **actor entity ID** was duplicated. That ambiguity strikes the identity operand itself; the checker cannot know whether rows concern the same actor. R84 stipulates a uniquely resolved actor, so this precedent does not transfer.
- R16 and R19 gate occupancy on valid/resolvable places and nonnegative ticks, respectively: those conditions affect whether the comparison operands are comparable. R84 stipulates those gates pass.
- R52 retained a raw booking when event-source IDs were ambiguous, because actor/place/tick fields independently established the input collision. It expressly distinguishes that result from source-supported or canon truth. Duplicate event IDs likewise should not be confused with duplicate actor IDs or with source-text validation.
- R37’s endpoint guard is relevant contrast: it refuses to dereference a duplicated event ID as a unique ledger endpoint, but does not establish that two raw timeline rows cease to be independently inspectable.

A real matched CLI replay is still useful to confirm exact current output for the proposed rows, including duplicate-ID and local diagnostics, and to ensure no extra warnings obscure it. But output parity is the code-path prediction; it would not by itself establish narrative truth. If the duplicate-ID pair produces no booking despite satisfying the above gates, that would falsify this analysis and warrant investigation of the exact input shape/eligibility, not an assumption that ID ambiguity itself blocks occupancy.

## Scope and limits

This is a finding about checker inputs: two rows with the same actor ID/tick and distinct place IDs meet the tool’s structural double-booking rule. It does **not** establish two distinct in-world events, separate witnesses, that either cited source supports the location, actual co-location, chronology, canon conflict, rights, or mechanics. Conversely, ambiguous event identity does not prove the location comparison false or unassessable. The checker’s duplicate-ID warning should remain visible alongside the structural finding, so a reader can distinguish ambiguous event references from the independently observable row-level conflict. Do not infer that a duplicate label means either row is the “real” event, or silently select one.
