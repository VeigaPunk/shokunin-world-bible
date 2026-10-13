# Round 69 ledger scout — same-reference branch and malformed-side baseline

## Scope

Read the Round 69 declaration in `.shokunin/lore/LOG.md:1212-1215`, the active checker, and the R62 malformed-side fixture/report evidence. This is a map of current checker behavior only; no files other than this report were changed.

## Active branch

In `.shokunin/lore/corpus/fixtures/check_bible.py:111-126`, each contradiction side is checked independently: it must be a dictionary, have a nonempty string `event_id`, and have a `field` in `{'place_id', 'tick', 'depends_on'}`. A failing field emits a field diagnostic and continues that side's loop (`:124-126`). After both sides are processed, the distinctness check at `:139-143` only checks that each side is a dict and that `.get('event_id')` values and `.get('field')` values compare equal. It does not consult the per-side validity result, require key presence, or check nonempty event IDs / allowed fields. Consequently, identical malformed field values (and, in other input shapes, matching missing/malformed values) can also trigger `claim_a and claim_b references must differ`. This is separate from the event-index checks at `:127-138` and is not evidence about fictional events or story claims.

## Exact malformed-side baseline

`.shokunin/lore/corpus/fixtures/r62-malformed-side/contradictions.json` supplies a single row whose `claim_a` and `claim_b` are both dictionaries with the same nonempty `event_id` (`tarin-envelope-observation`) and the same invalid `field` (`bogus`). Its `timeline.json` contains `{bad`, so this also exercises an unavailable timeline. Running the baseline command

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r62-malformed-side
```

produced exit 1 and these findings:

```text
VIOLATION: timeline.json: cannot load JSON: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
VIOLATION: contradictions[0].claim_a.field: expected one of ['depends_on', 'place_id', 'tick']
VIOLATION: contradictions[0].claim_b.field: expected one of ['depends_on', 'place_id', 'tick']
VIOLATION: contradictions[0]: claim_a and claim_b references must differ
4 violation(s); no canon changed
```

Thus the malformed-both baseline retains both local field diagnostics and adds the same-reference finding. Since each side passes event-ID validation but fails field validation, neither reaches the unavailable-timeline pointer diagnostic at `:127-129`. The extra same-reference message duplicates the malformed-field fact in this fixture; the fixture alone does not establish whether that extra message is independently actionable or harmful.

## Controls and limits

The valid-reference comparator is visible in `.shokunin/lore/corpus/fixtures/r62-loaded/contradictions.json`: its two sides have allowed `place_id` fields and distinct event IDs, so it is not a valid-identical-reference control. A search of current fixture `contradictions.json` files found the R62 malformed-side row as the only matching `(event_id, field)` pair; therefore the current corpus does not provide a paired valid-identical fixture. R62 review evidence explicitly records that `r62-malformed-side` retains the two invalid-field findings and same-reference finding (`.shokunin/lore/reports/r62-reviewer.md`, section “Independent fixture replay”); the R62 independent verifier reports the same baseline behavior (`.shokunin/lore/reports/r62-independent-verifier.md`, “Candidate behaviors observed”). `.shokunin/lore/corpus/fixtures/README.md:970` likewise describes same-reference checks as independent of unavailable-timeline handling.

This maps the branch and one malformed-both baseline only. It does not test malformed-one, missing keys, non-string values, valid-identical or valid-different pairs under a candidate; it does not establish that removing the finding improves calibration, nor replay the prior CLI suite. No conclusions about source text, story contradiction, canon, rights, or mechanics are warranted.
