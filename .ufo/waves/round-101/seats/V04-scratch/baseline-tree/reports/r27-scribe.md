# Round 27 scribe: bounded relation-endpoint decision table

## Scope and evidence

This is a proposed decision table for the round-27 **coverage** case only. It describes checker handling of admitted relation rows and entity-ID multiplicity; it does not decide whether a relation is true, which duplicate record is canonical, or whether any source text supports the relation.

- `.shokunin/lore/LOG.md: Round 27 — 2026-10-13` declares the matched case: same cited `mira -> seal` relation; control duplicates `seal` only, case duplicates both `mira` and `seal`; expected endpoint-local findings and preservation of 76 earlier outcomes / 379 prior JSON bytes.
- `.shokunin/lore/corpus/fixtures/check_bible.py:8-12` declares required relation fields (`from`, `to`, `type`, `source_id`) and entity fields.
- `.shokunin/lore/corpus/fixtures/check_bible.py:30-44` admits rows only after required fields have correct types and nonempty strings; malformed rows are excluded from `data`.
- `.shokunin/lore/corpus/fixtures/check_bible.py:48-67` indexes admitted entity rows and counts each admitted entity ID.
- `.shokunin/lore/corpus/fixtures/check_bible.py:135-142` checks each admitted relation's `from` and `to` independently: absent index entry => dangling; count greater than one => ambiguous; then checks relation source ID.
- `.shokunin/lore/corpus/fixtures/consistent/relations.json:1` is the cited `mira -> seal` control relation. `.shokunin/lore/corpus/fixtures/consistent/entities.json:1-4` contains the unique endpoint entities.
- `.shokunin/lore/corpus/fixtures/r25-to-ambiguous/entities.json:1-5` and `relations.json:1` provide prior target-only duplicate example; `.shokunin/lore/corpus/fixtures/r25-to-unique/relations.json:1` is its unique control.

## Proposed bounded table

| Admitted relation endpoint condition | Expected structural diagnostic | What this does not decide |
|---|---|---|
| `from` or `to` ID has zero admitted entity rows | Endpoint-local dangling entity diagnostic | No missing entity is invented. |
| Endpoint ID has exactly one admitted entity row | No ambiguity diagnostic for that endpoint (other checks still apply) | No relation truth or source support is established. |
| Endpoint ID has more than one admitted entity row | Ambiguous-entity diagnostic at that endpoint field; retain all rows | No duplicate is selected or merged; no identity/canon conclusion follows. |
| Both endpoint IDs have multiplicity greater than one | One ambiguity diagnostic for `from` and one for `to`; preserve duplicate-ID diagnostics | This is two independent endpoint checks, not evidence of a relationship between either chosen pair. |
| One endpoint is duplicated and the other unique | Ambiguity only at the duplicated endpoint | The unique endpoint check does not resolve the other endpoint. |
| A raw entity row fails required-field screening | It does not increase the admitted entity ID count; its schema error remains | Its exclusion is not evidence the row/source is false or that an ID is unique in canon. |

## Risks / limits

- Repeated endpoint checks are structural diagnostics, not a relation-level verdict. Consumers must not turn two ambiguity findings into an inferred edge or identity.
- ID multiplicity is bounded by the current row-screening contract; this table is not a claim that every malformed-input shape has been tested.
- A resolvable source ID means identifier resolution only. The checker does not test excerpt entailment, reliability, or canon truth.
- The round's coverage claim is limited to the simultaneous two-endpoint case beyond the previously exercised target-only case. Do not generalize to all relation types or all entity-reference consumers.

## Proposed test

From repository root, replay the exact pair and assert only the scoped outcomes:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r25-to-unique
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r25-to-ambiguous
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r27-from-to-ambiguous
```

The first should be clean; target-only control should show only `relations[0].to` ambiguity; the round-27 case should show both `relations[0].from` and `.to` ambiguity plus duplicate-ID errors. Verify the new case differs from its matched control only by adding an admitted duplicate `mira` row, while the relation and citations are unchanged. For regression evidence, replay all 76 pre-round directories against the declared baseline checker and compare stdout, stderr, and exit status; compare the 379 prior JSON paths byte-for-byte. These are proposed checks, not results claimed by this scribe.
