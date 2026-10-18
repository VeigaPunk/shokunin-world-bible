# Round 84 editor-scout — first repair under duplicate event IDs

## Finding

For two separately cited, schema-valid timeline rows, do **not** make the first repair suppress or weaken `double-booked` merely because their `id` values collide. First preserve both raw rows and repair the duplicate event-ID/reference ambiguity: establish distinct IDs only where the cited material supports treating these as separate event records, then update dependent pointers if needed. Do not pick a row by order, merge/delete one, or invent event identity. The duplicate-ID diagnostic and the occupancy diagnostic concern different fields and can both be actionable.

For the matched distinct-ID pair, there is no ID ambiguity to repair. The same uniquely resolved actor at the same accepted local tick in two distinct uniquely typed places still warrants checking the row assertions against their citations; correct the unsupported actor, tick, or place assertion (or otherwise reconcile the input) rather than treating distinct IDs as curing the booking. IDs distinguish event records; they do not make simultaneous distinct-place assertions consistent.

## Why the warning is not misdirected (with a limit)

The active checker counts timeline IDs separately (`check_bible.py`, `event_id_counts`), while occupancy iterates the admitted raw timeline rows and gates on uniquely resolved actor, uniquely resolved place of kind `place`, and nonnegative tick. The occupancy key is `(entity_id, tick)`; the comparison does not consult the event ID or `event_id_counts`. On a second different place at that slot it emits `double-booked`. Thus a duplicate label does not make the two eligible row assertions disappear or make the slot comparison depend on which duplicate event the index selects. The event-ID warning flags ambiguous references; `double-booked` flags a separate structural mismatch among fields on the rows. Removing the latter only in the duplicate-ID case would conceal the same actionable field mismatch present in the distinct-ID control.

That is only an input-structural editor warning. It does not prove the cited material supports those fields, that either event occurred, that a person truly occupied either place, or that fictional canon conflicts. If the warning is presented or read as a sourced/world-truth verdict, that interpretation is misleading; the right response is to qualify its structural scope, not suppress it on event-ID ambiguity alone.

## Prior-art checks and scope

- R9 (`reports/r9-independent-verifier.md`) treats duplicate IDs as ambiguity for dependency target resolution and avoids last-wins tick comparisons; that is a consumer of an event **reference**, unlike occupancy's direct row-field comparison.
- R12–R13 guard occupancy for ambiguous or dangling actor references; R16–R19 guard place resolution and tick eligibility. Those are direct prerequisites for trusting this particular structural slot comparison, not grounds to add event-ID uniqueness as another occupancy prerequisite.
- R21 (`2026-10-12-lore-decision-table.md`, Round 21) explicitly retains independently eligible known-place occupancy when a dependency member is malformed. R52 (`reports/r52-pair-scout.md`) likewise distinguishes raw-field occupancy from citation ambiguity and advises retaining the structural finding while limiting its interpretation.
- R37 (`reports/r37-duplicate-scout.md`) shows why duplicate event IDs must remain an explicit ambiguity for ledger endpoints; it does not establish that every consumer of raw timeline rows must be skipped.

Accordingly, I find no safe basis here for the proposed duplicate-ID-only suppression. If the message itself needs repair, narrow its interpretation to “input rows assign this actor/tick to distinct places”; do not imply sourced chronology or canon. This is a structural/editor analysis of fictional, unverified fixture data, not a canon, rights, or mechanics conclusion.
