# E1 — Per-record provenance disclosure candidates

These are proposed f-string templates, not active checker output. Each is for every provenance record at or after the first holder-identity ambiguity. `record_label` is the current record label; `holder_id` is the ambiguous raw ID; `origin_record_label` is the first record where it was found ambiguous. `!r` follows the checker's existing ID-reporting style. The exact phrase `input-structural finding, not sourced-canon` preserves the structural/canon distinction used by existing provenance-chain findings (`corpus/fixtures/check_bible.py:250-254`).

## Candidate 1 — scope first

```python
f'{record_label}: input-structural finding, not sourced-canon; provenance continuity and tick-order comparisons are unassessed from {origin_record_label} onward because holder id {holder_id!r} is ambiguous'
```

Rationale: Leads with the structural/canon boundary, then names both unassessed comparisons, the ambiguous ID, and the origin record.

Risk (overclaim potential): “From … onward” could be read as a statement about canon-wide unknowability rather than the checker's latched assessment scope; the structural qualifier and explicit comparison scope reduce but do not eliminate that risk.

## Candidate 2 — cause first

```python
f"{record_label}: holder id {holder_id!r} is ambiguous at {origin_record_label}; this record's provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon)"
```

Rationale: Puts the stop cause and its origin first, while `record_label` plus “this record's” makes the disclosure local to each emitted record.

Risk (overclaim potential): “Is ambiguous at” might be misread as identifying a particular duplicate entity or as a historical/canon fact; it describes only the supplied ID's structural ambiguity.

## Candidate 3 — assessment status first

```python
f'{record_label}: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); holder id {holder_id!r} was ambiguous at {origin_record_label}'
```

Rationale: States the per-record assessment status before explaining its ID-specific origin, without calling the chain broken.

Risk (overclaim potential): “Was ambiguous at” may sound like an event in the fictional timeline; the phrase refers only to the input structure and checker stop cause.
