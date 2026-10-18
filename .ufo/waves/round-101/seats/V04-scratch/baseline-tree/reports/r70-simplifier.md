# Round 70 simplifier — event-ID-only comparison gate

## Recommendation

The smallest checker change matching the declaration is to add a nonempty-string `event_id` guard to the existing pair comparison at `.shokunin/lore/corpus/fixtures/check_bible.py:139–143`. Do not validate the field in this gate: preserve the current raw `field` equality test and its independent allowed-field diagnostics. In pseudocode:

```python
and isinstance(claim_a.get('event_id'), str) and claim_a['event_id'].strip()
and isinstance(claim_b.get('event_id'), str) and claim_b['event_id'].strip()
```

These conditions belong in the existing `if` alongside the current dictionary checks and unchanged raw equality checks for `event_id` and `field`. This is narrower than R69's proposed gate on both IDs and allowed fields. It suppresses only pair-level comparison when either ID is absent, non-string, or blank; it leaves comparisons in place for valid IDs even when either field is invalid. No checker or fixture edit is made in this report.

## Evidence and expected behavior

The current side loop at checker lines 112–138 reports a missing/blank/non-string `event_id` as `required nonempty string` and then continues, independently of the later pair check. The pair check at lines 139–143 compares raw `.get('event_id')` and `.get('field')` values whenever both sides are dictionaries. Thus two absent IDs (and equal absent fields) can produce a pair-level `references must differ` finding despite there being no supplied event identifier. An event ID whose string is whitespace is likewise unusable under the side loop's `.strip()` check.

The required predicate checks only event-ID usability according to the checker's existing definition. The pair's field equality comparison stays exactly as it is. In particular, `.shokunin/lore/corpus/fixtures/r62-malformed-side/contradictions.json` has matching nonempty `tarin-envelope-observation` IDs and matching invalid `bogus` fields. I ran the current checker on this fixture: exit 1; malformed timeline load error, one invalid-field finding per side, existing pair finding, and four total violations. With the proposed ID-only gate, that pair condition still holds, so R62's pair finding remains alongside both field errors. Valid identical IDs/fields likewise retain their existing pair finding; valid distinct references stay unaffected. These are expected consequences of the predicate, not candidate-run results.

## Risks, validation, and limits

This report identifies a narrow candidate, not proof of material user benefit. Suppressing the comparison for unusable IDs may remove an unhelpful duplicate-reference line, while retaining side-local required-ID and field errors. No matched candidate runs for missing, blank, non-string, or valid IDs were performed here; no candidate or full old-fixture raw-output replay was performed. The declaration's acceptance conditions still require matched missing/blank-ID cases, preservation of R62 and valid identical/distinct cases, and independent regression replay before adoption. A falsifier is evidence that the removed pair finding directs a distinct needed repair for unusable IDs, any changed R62/valid-ID behavior, or unexpected old-fixture output changes.

The evidence is limited to checker control flow, the declared round scope, and the R62 fixture/current baseline output. IDs and diagnostics do not establish event existence, source support, fictional chronology or truth, canon, rights, or game mechanics. No source-text, canon, rights, or mechanics claim is made.
