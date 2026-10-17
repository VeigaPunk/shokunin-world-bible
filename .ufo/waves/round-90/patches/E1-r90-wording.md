# E1 — Round-90 FN-2 wording panel

Status: wording proposal only; no checker or corpus file changed.

Axes: calibration (certainty matches the predicate); scope (identity uncertainty applies only to non-null, identity-dependent comparisons); over-claim control (structural findings do not become canon claims).

## Proposed definite templates

Keep the existing `input-structural finding, not sourced-canon; ` prefix only when `chain_has_ambiguous_source` independently requires it. Holder-resolution uncertainty must not add that prefix or an identity note to the following definite findings.

### Later record has `from_holder: null` and breaks continuity

```text
{record_label}: {"input-structural finding, not sourced-canon; " if chain_has_ambiguous_source else ""}provenance chain break; expected from_holder {previous_holder!r}, got {from_holder!r}
```

For a schema-valid later record whose `from_holder` is null, `{from_holder!r}` renders as `None`. The definite break holds even if the preceding non-null holder ID is unresolved: null is a sentinel, not a holder identity that can be compared or resolved.

**Rationale:** zero raw rows and zero indexed rows for `None` are vacuous counts, not evidence that the current holder's identity is uncertain. A later transfer record with null `from_holder` cannot continue the preceding non-null `to_holder` chain.

**Over-claim risk:** this is a definite inconsistency in the explicit record fields, not proof that no transfer occurred in the story or that the source text is false. Keep identity-dependent mismatches between unresolved non-null IDs qualified; do not apply this wording to those comparisons.

### Tick inversion, including a null transition or unresolved holder

```text
{record_label}.tick: {"input-structural finding, not sourced-canon; " if chain_has_ambiguous_source else ""}provenance tick {tick} must be greater than previous tick {previous_tick}
```

Emit this only when both records passed structural validation and `tick <= previous_tick`. Holder identity notes do not belong on this line, whether the `from_holder` is null, non-null but unresolved, or uncertain for another reason. Preserve the prefix only for an independently ambiguous source citation.

**Rationale:** strict ordering is determined by the two validated integer tick values and their record order. Holder identity is not an input to that comparison.

**Over-claim risk:** this establishes only a local ordering violation in the listed provenance records. It does not establish real-world chronology, an event date, or what transfer occurred. Do not attach uncertainty about unrelated holder identity to the tick comparison.

### Adjacent non-comparison guard: first record has non-null `from_holder`

```text
{record_label}: {"input-structural finding, not sourced-canon; " if chain_has_ambiguous_source else ""}provenance chain break; first record must have from_holder null
```

This is a positional null requirement, not an identity comparison; a non-null value violates it even if that holder ID is unresolved.

**Rationale:** the requirement concerns the first record's field shape, so holder resolution cannot make the non-null value permissible.

**Over-claim risk:** the line does not identify the actual holder or establish canon about the item's history. This guard is included to prevent the same broad qualifier from leaking into a neighboring non-comparison branch; it is not an additional FN-2 comparison case.

## Boundary: retain qualification where identity matters

For a chain comparison between non-null holder IDs, keep the existing qualified form only when at least one compared ID is demonstrably not uniquely resolvable:

```text
{record_label}: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: {expected_clause}; {observed_clause}
```

Do not qualify every chain break, every finding on a record containing any identity defect, or a tick-order finding. The fixture `r89-fn2-unresolved-chain-break` remains the positive control for the unresolved non-null comparison; `r89-fn2-control` remains the definite resolved-identity control.

## Recorded examples

```text
entities[2].provenance[1]: provenance chain break; expected from_holder 'mira', got None
entities[2].provenance[1].tick: provenance tick 1 must be greater than previous tick 2
```

These are the pre-r89/baseline forms recorded for the nullable-`from_holder` chain and tick inversion probes. The proposal restores them for those definite structural findings, while preserving independent source-ambiguity wording and the FN-2 qualifier for genuinely unresolved compared holders.
