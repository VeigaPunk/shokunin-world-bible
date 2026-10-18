# E1 — Round-88 C1 wording proposal

Status: wording proposal only; no checker implementation changed.

Wording axes: causal accuracy; per-record disclosure coverage; input-structure versus canon boundary.

The delivered checker currently emits two relevant forms (`corpus/fixtures/check_bible.py:243,250`):

```text
{record_label}: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous
{record_label}: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity {cause} first occurred at {record_label}
```

E1's round-87 Candidate 3 improves the boundary and removes the causal conjunction, but names only the holder ambiguity; JCAL4 classified that wording as misleading when an earlier unknown-source record had already stopped comparison. These proposals retain Candidate 3's assessment-status-first approach, add the actual earliest stop record/cause, and say “in this chain” to avoid the cross-chain locator ambiguity noted by JCAL2.

## Template 1 — shape-invalid dict with ambiguous holder (first-stop variant)

```python
f'{record_label}: provenance continuity and tick-order comparisons remain unassessed from {first_stop_label} onward in this chain (input-structural finding, not sourced-canon); the shape-invalid dict at {first_stop_label} carried ambiguous holder reference {holder_field} {holder_id!r}, recognized as a stop trigger'
```

Rationale: Makes the residual path visible even though record-shape validation failed; states the unassessed scope, identifies the malformed record and holder field/id, and explicitly records that the ambiguity participates in arming the stop. The structural qualifier avoids presenting a checker finding as a canon assertion.

Overclaim risk: Emit this only when that shape-invalid/ambiguous record is the earliest stop in this chain. If an earlier record already stopped comparison, this wording would misattribute the stop; use the actual earlier-cause template instead. “Recognized as a stop trigger” must describe the implementation's real latch behavior, not merely the presence of a duplicate ID.

## Template 2 — first holder-stop cause

```python
f'{record_label}: provenance continuity and tick-order comparisons remain unassessed from {first_stop_label} onward in this chain (input-structural finding, not sourced-canon); first stop at {first_stop_label}: {first_stop_cause_summary}'
```

For a single holder cause, `first_stop_cause_summary` is `ambiguous holder reference {holder_field} {holder_id!r}`. If that same record has multiple stopping findings, the summary must name them without asserting an unmeasured within-record order.

Rationale: Replaces “because … first occurred at” with a status plus an explicit earliest-stop record and cause summary. It does not imply that a later ambiguity was the first/sole cause, and the locator is explicitly chain-scoped.

Overclaim risk: The cause and origin placeholders must come from retained first-stop state, not from the most recently observed ambiguity. The summary must reflect the first-stop record's actual findings; it must not collapse a mixed-stop chain to a later holder ambiguity.

## Template 3 — non-holder first-stop cause

```python
f'{record_label}: provenance continuity and tick-order comparisons remain unassessed from {first_stop_label} onward in this chain (input-structural finding, not sourced-canon); first stop at {first_stop_label}: non-holder cause {non_holder_cause_summary}'
```

`non_holder_cause_summary` should name the actual input finding, for example `unknown source_id 'missing-source'` or `dangling from_holder 'ghost'`, not a generic “invalid record.” The same form can describe other non-holder validation failures if they truly latched the chain stop.

Rationale: Discloses the stop even when no holder ambiguity exists and prevents a later ambiguity from replacing an earlier unknown-source/dangling-holder cause.

Overclaim risk: Include only causes that actually stop comparison. Ambiguous-but-available source citations, for example, must not be labeled a stop cause merely because they are ambiguous. For multiple simultaneous findings at the first-stop record, summarize them without claiming within-record precedence.

## Emission rule

Emit exactly one per-record stop disclosure at each record at or after the first chain stop. Choose template 1 when the first-stop record is both a shape-invalid dict and carries an ambiguous holder reference; otherwise choose template 2 for a holder-ambiguity first stop, or template 3 for a non-holder first stop. Keep the selected first-stop record and cause summary stable for the tail. Do not emit template 1 plus a generic stop disclosure at the same record: JCAL4 observed a redundant stop-record notice in the delivered checker.

These templates assume comparisons reached a record-level stop. Pre-loop suppression cases such as unavailable source data, non-item entities, or duplicate item IDs need a separate scope decision; do not invent a record-level first cause when no stop record was established.
