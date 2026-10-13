# Round 65 alliance source-status scout

## Scope and verdict

**NO-GO for material calibration; no checker change recommended.** I traced current source-status callers and executed matched temporary probes under `/tmp/r65-alliance` only. No repository code, fixtures, README, or LOG was changed. The hypothesis was to withhold the derived missing-reciprocal finding when the forward relation itself has an unknown or ambiguous `source_id`. The probes confirm the behavior exists, but not that it is miscalibrated: the diagnostic is explicitly about the absence of a *sourced reciprocal*, and source validity for the forward row does not supply a reverse row. Suppressing it would hide a useful separate repair pointer while leaving the direct citation error.

## Current code and observed decisions

In `corpus/fixtures/check_bible.py`, `source_status` (`:90-95`) returns `unavailable` when sources failed to load, otherwise `unknown` / `unique` / `ambiguous` from admitted-row counts. `source()` (`:97-104`) independently emits local unknown/ambiguous diagnostics. Each relation calls `source(row['source_id'], ...)` at `:155`. The later alliance pass (`:252-271`) gates on loaded entities, distinct endpoints uniquely indexed as factions, and non-self `allied_with`; it does **not** gate on the current row's source status. It searches the reverse direction and accepts a candidate only when that candidate's source status is `unique`; if none qualifies, it emits `lacks a sourced reciprocal relation` when sources are available.

Temporary CLI probes used `ally-one-way` as base, changing only the forward citation to unknown or ambiguous and optionally adding a reverse row with matching unique/ambiguous citation status. Results:

| Forward status | Reverse status | Observed relevant output |
|---|---|---|
| unique | absent | `relations[0]: ... lacks a sourced reciprocal relation` |
| unknown (`not-listed`) | absent | direct `relations[0].source_id: unknown ...` **and** missing-sourced-reciprocal |
| ambiguous (`harbor-compact` duplicated) | absent | direct ambiguous citation **and** missing-sourced-reciprocal (plus duplicate and unchanged-table references) |
| unique | unique | CLEAN, no reciprocal error |
| unknown | unique | direct unknown only; reverse qualifies the forward edge |
| unique | ambiguous | reverse ambiguity plus missing-sourced-reciprocal |
| ambiguous | unique | forward ambiguity; reverse qualifies the forward edge, but reverse row itself lacks a unique reverse witness and gets its own reciprocal error |
| unknown | ambiguous | forward unknown, reverse ambiguity, and both directed rows lack qualified reciprocal witnesses |

The duplicated-source cases naturally include duplicate-ID and other unchanged references to `harbor-compact`; counts are not presented as relation-only results. The key distinction is row-local: reciprocity asks for at least one uniquely cited reverse relation. An invalid forward citation is already reported locally, but does not establish the opposite direction.

## Precedent / convention

R2 (`reports/r2-rule-scout.md`, citations section) explicitly treated citation validation and structural reciprocal presence as independent: a bad citation on an existing reverse row was to yield its normal citation error, while reciprocity was separately decided. R7 (`reports/r7-alliance-scout.md` and LOG Round 7) deliberately changed the witness criterion: a reverse edge with ambiguous source ID cannot satisfy a uniquely sourced forward relation; an alternative unique reverse still can. R31 confirms per-relation source checks are generic, separate from the alliance witness. R61's source-table-availability work separately gates only when the entire source table is unavailable; that is not applicable to a loaded table with a row-local unknown/ambiguous ID. These precedents support independent diagnostics, not suppressing reciprocal status based on the forward row.

## Falsifier and repair-pointer harm

A material-gain case would need matched evidence that the present wording falsely conveys the forward assertion is sourced, or an accepted policy that only uniquely cited forward assertions are eligible for symmetry checking. Neither is demonstrated. The actual wording says “lacks a sourced reciprocal relation,” not “the forward alliance is true/verified.” A loaded unknown/ambiguous forward row may still need its opposite direction added (and its citation repaired); withholding the reciprocal finding loses that second actionable location. Conversely, the proposed gate would not make a structurally present reverse row valid: forward unique + reverse ambiguous already produces the intended missing-witness finding, plus the reverse citation diagnostic.

Falsifier of this NO-GO: a concrete paired operator workflow showing the forward-row reciprocal finding is misleading/actionably redundant when its citation is unknown/ambiguous, while demonstrating that removing it does not hide needed reverse-edge repair guidance. If such evidence emerges, compare both outputs with unchanged source/endpoint/other relation checks. No such evidence exists in these probes or cited prior reports.

## Boundary

This is checker-input identity/availability only. Unique source IDs establish only membership in the supplied input table, not source-text support, authenticity, canon truth, or any rights/permission status. No source prose was assessed and no fictional-world claim was made.
