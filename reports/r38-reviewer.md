# Round 38 non-author reviewer — Bell-7 ledger source ambiguity

## Verdict: PASS, bounded artifact; novelty is narrow/repeated coverage

I independently inspected the inherited fixture bytes, source multiplicities, ledger/event pointers, and checker output. The bounded artifact passes its declared structural claim. Do not describe this as first coverage of ledger-source ambiguity: r7-reviewer documents a temporary probe of that general class. The durable incremental case is specifically the Bell-7 `claim_b` endpoint, whereas the r7 temporary probe exercised `claim_a` in a `consistent` clone. Whether that distinction merits a coverage-axis gain is debatable and may be merely repeated coverage of an existing branch in a new fixture/context; it is not a new rule.

## Byte and pointer audit

The r38 unique fixture contains the same nine inherited filenames as `r35-bell7-conflict`; I compared each file's bytes, and all nine match r35 exactly. The ambiguous fixture matches the unique fixture byte-for-byte for eight files; only `sources.json` differs. Its four inherited rows are retained and one duplicate `sella-bell7-note` object is appended at index 4. Source count for that ID is 1 in control and 2 in negative. Each timeline event ID occurs exactly once in both fixtures. The unchanged ledger points `claim_a` to `tarin-envelope-observation` and `claim_b` to `sella-bell7-presence`; both pointers remain uniquely resolved. `claim_a`'s cited source remains unique. Thus event-pointer uniqueness and source-ID multiplicity are distinct and correctly isolated.

## Independent checker replay / full negative inventory

Ran from repository root:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r38-ledger-source-unique
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r38-ledger-source-ambiguous
```

Control: exit 0; stdout `CLEAN: schema, citations, relations, timeline; 0 violations`; stderr empty.

Negative: exit 1; stderr empty; exactly these three diagnostics (complete inventory):

```text
VIOLATION: sources[4].id: duplicate sources id 'sella-bell7-note'
VIOLATION: contradictions[0].claim_b.source_id: ambiguous in-world source 'sella-bell7-note'
VIOLATION: timeline[3].source_id: ambiguous in-world source 'sella-bell7-note'
3 violation(s); no canon changed
```

The third, collateral `timeline[3]` finding is essential: the Sella event also cites the duplicated ID. There is no `claim_a` ambiguity, duplicate event-ID finding, or other diagnostic. This matches all consumers affected by the one-row mutation.

## Precedent and novelty boundary

The r7 reviewer report records a *temporary* `consistent` clone probe: duplicate `archive-ledger`, have `departure` cite it, then point a ledger side to that event; it yielded `contradictions[0].claim_a.source_id` ambiguity among other findings. Hence source ambiguity reached through a contradiction-ledger endpoint was already tested experimentally. The committed r7 fixtures primarily cover relation/provenance references, while r31 is a controlled relation case and r37 covers duplicate timeline-event identity, not source identity. R38 makes a durable, regression-friendly Bell-7 `claim_b` counterpart with the opposite ledger side from the r7 temporary probe. That is a limited fixture/context distinction, not a new checker capability and not broad new source ambiguity coverage. It may be repetition rather than a material axis gain; an adjudicator should weigh that honestly rather than equating a new fixture with a new rule.

## Scope limits

The checker establishes structural identifier ambiguity only. A duplicate metadata row does not authenticate or select either source, prove either testimony true or false, prove a semantic contradiction, or decide canon. The report/ledger remain unresolved; no canon or testimony truth inference is made.
