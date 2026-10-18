# Round 65 citation scout — forward citation membership boundary

## Verdict

**NO-GO on material calibration.** A source ID that is unique in the input index establishes membership/cardinality only. It does not show that the fictional source text supports the relation, establishes an alliance, or determines canon. Current code already diagnoses a forward relation’s unknown/ambiguous citation separately; withholding its derived missing-reciprocal finding may be coherent, but available evidence does not prove this is a material user-facing calibration improvement rather than loss of a useful repair pointer. No candidate or fixture probe was run by this leaf; this is an independent code/prior-art decision, not evidence of candidate behavior.

## Observed code and precedent

In `corpus/fixtures/check_bible.py`, `source_status()` returns `unknown`/`ambiguous`/`unique` from admitted source-row counts (lines 88–99); relation validation calls `source(row['source_id'], ...)` for each relation (around lines 150–159). The alliance pass then considers faction endpoints and searches for a reverse `allied_with` row whose source status is `unique` (around lines 233–250). It does **not** test the forward row’s citation status before emitting `lacks a sourced reciprocal relation`. Thus the proposed distinction is a real asymmetry in checker control flow; it is not a claim that source prose is examined.

Round 2 declares an explicit reciprocal-record convention and says citation is per relation (`r2-rule-scout.md`); it does not settle whether an unknown/ambiguous forward citation disables the convention’s missing-reverse diagnostic. Round 7 specifically established that an ambiguously cited reverse row does not qualify as a sourced witness, and that a uniquely cited forward row then receives the missing-reciprocal diagnostic (`r7-alliance-scout.md`). It does not test forward ambiguity. Round 31 distinguishes generic relation citation diagnostics from the separate alliance witness path (`r31-source-scout.md`). Round 61 gates the alliance conclusion when the whole source registry is unavailable, while retaining loaded-index distinctions; that is not equivalent to a loaded registry with an unknown/ambiguous ID (`r61-axis-adjudicator.md`). None is a direct precedent for the proposed forward-side gate.

## Calibration tradeoff and falsifier

The direct unknown/ambiguous citation diagnostic already identifies the forward row needing repair. A second “lacks sourced reciprocal” message could be read as an independent structural assertion or could be redundant once the forward assertion itself cannot be resolved by ID. Withholding it may reduce noise, but also removes a concrete relation-local pointer to the missing reverse record. The cited files do not measure which interpretation helps users, and source-ID status alone cannot decide it.

Falsifier for NO-GO: a matched probe and reviewer evidence showing that forward unknown/ambiguous rows reliably cause materially misleading reciprocal conclusions, while a narrowly gated candidate preserves the existing missing-reciprocal result for unique-forward/reverse-absent, preserves r7’s ambiguous-reverse behavior, and causes no actionable pointer loss, would justify reconsideration. Conversely, if retaining the diagnostic is the declared source-independent structural convention or users need it to repair the pair, the gating hypothesis fails.

A proper probe would hold faction entities, relation directions, and other tables fixed while varying only forward citation cardinality (unique/unknown/ambiguous) and reverse state (absent/unique/ambiguous). It must inventory direct citation, endpoint, and reciprocal outputs separately. Do not report hypothetical variants as observed outputs.

## Boundary

An input ID’s presence or uniqueness is not evidence of source-prose support, historical or fictional fact, treaty validity, alliance truth, or canon. No conclusion here concerns world alliance, authorship, authenticity, rights, copyright, licensing, or permission. No checker, fixture, README, or LOG edits were made; no code/fixture candidate or corpus regression replay was performed.
