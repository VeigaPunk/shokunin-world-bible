# Round 65 simplifier — forward-source eligibility gate

## Independent verdict: NO-GO for material calibration

The proposed gate has a plausible semantic rationale, but the actual checker and observed controls do not establish that withholding the existing missing-reciprocal finding for an unresolved **forward** citation improves an operator's repair decision. I recommend no implementation or fixture change on this evidence.

## Observed code and outputs

In `.shokunin/lore/corpus/fixtures/check_bible.py`, every admitted relation first receives its direct `source()` check. Separately, the alliance loop scans each non-self `allied_with` faction pair. Its `reciprocal` predicate asks whether a reversed allied row has `source_status(candidate['source_id']) == 'unique'`; if none qualifies and sources are available, it emits `lacks a sourced reciprocal relation` at the forward row. It does **not** gate that derived finding on the forward row's source status. Thus a missing/ambiguous forward citation can produce both a direct citation diagnostic and the missing-reciprocal pointer. This is observed implementation, not a claim that either relation is true.

Observed current CLI control: `python .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/ally-one-way` exits 1 and prints `relations[0]: allied_with faction relation 'quay-guild' -> 'bell-wardens' lacks a sourced reciprocal relation`. `ally-reciprocal` is the corresponding existing positive control; r7's report documents its clean output and a matched temporary duplicate-reverse probe. R7 specifically tested a uniquely cited forward with an ambiguously cited reverse, where the current checker accepts no reverse witness and emits the missing-reciprocal finding. That supports the reverse-side uniqueness rule, not the proposed forward-side eligibility rule.

R2 documents the originally declared convention as a relation-local missing reverse rule with independently sourced records; r7 narrowed source identity on the reverse witness. R31 records the present source-status reporter and its distinction between direct citation diagnostics and witness qualification. R61 already observes that source availability gates the alliance witness; it does not test forward-row status gating. These precedents do not prove that an unresolved forward assertion should or should not trigger the existing pointer.

## Materiality and repair-pointer tradeoff

The proposed behavior is a single additional guard: require the forward row's source status to be `unique` before reporting its missing reciprocal. That would suppress the pointer for unknown or ambiguous forward IDs while leaving the direct `unknown`/`ambiguous in-world source` finding and other endpoint/relation checks. However, the direct source finding repairs citation membership/cardinality; the reciprocal finding identifies the absent reverse relation. They point to different input locations/actions. The present evidence contains no actual paired output showing that the second pointer is redundant or misleading, nor an operator task where withholding it improves repair. It may instead remove a useful structural repair pointer precisely when both citation and direction need correction. A source-unresolved forward row remains an admitted relation row for structural checks; the checker does not otherwise equate source failure with row absence.

Accordingly **material calibration: NO-GO / unproved**. This is not a claim that the current policy is ideal; it is a stop before testing/implementation because plausible policy alone is insufficient evidence of benefit.

## Falsifier and evidence that could change the verdict

A matched temporary probe could reverse this verdict if it shows a concrete repair decision improved by gating: keep factions, relation shape, reverse state, and all non-source tables identical; vary only forward source status among unique, unknown, and ambiguous, and reverse status among absent, unique, ambiguous. Record complete stdout/stderr/exit and verify direct forward citation, endpoint and unrelated checks survive. The decisive comparison is whether a non-unique forward plus absent reverse currently produces a materially misleading second pointer, versus whether retaining it usefully identifies an independent structural repair. Preserve the r7 control: unique forward plus ambiguous reverse must still report the direct reverse citation ambiguity and missing qualified reciprocal. Unknown/ambiguous forward with a unique reverse should not acquire a missing-reciprocal finding under either policy. No source prose is needed or admissible for this test.

## Axes and boundaries

- **Calibration:** NO-GO, no material benefit demonstrated.
- **Depth:** unchanged; this would be a gating policy, not new relation analysis.
- **Coverage:** unchanged; no new fixture/probe in this review.
- **Potential harm:** suppression of a distinct reverse-edge repair pointer; accidentally gating unrelated relation checks; weakening the already evidenced reverse uniqueness behavior.

Source IDs here are input identifiers only. No inference about source text, alliance truth, fictional canon, chronology, rights, or permission follows. No checker, fixture, README, or LOG file was edited; this report is the only repository write.
