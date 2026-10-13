# Round 38 pair scout — ambiguous Sella source at Bell-7 ledger endpoint

## Proposed minimal pair (not implemented)

Use `.shokunin/lore/corpus/fixtures/r35-bell7-conflict/` for both siblings. The control is a byte-identical copy. For the negative, append one structurally valid source row to `sources.json`, with `id: "sella-bell7-note"` and distinct descriptive fields; retain the original row and every other file/row unchanged. Do not alter either timeline event, either ledger pointer, excerpt, or `why`. This is exactly one added copied-ID row, not a second Sella account or new event. The existing row occupies `r35-bell7-conflict/sources.json:21-25`; Sella event points to it at `timeline.json:31-39`, while ledger `claim_b` points uniquely to that event at `contradictions.json:8-11`.

## Checker path and complete expected output scope

The checker counts duplicate source IDs and classifies them at `check_bible.py:54-74`. Ledger processing resolves a uniquely occurring event, then checks that event's source at `:83-96`. Thus both event IDs remain unique, but the source citation reached from `claim_b` is ambiguous; no event-ID cardinality error is expected. Expected control: exit 0 and `CLEAN: schema, citations, relations, timeline; 0 violations`. Expected negative, inventory the entire stdout (not just the target finding):

```text
VIOLATION: sources[4].id: duplicate sources id 'sella-bell7-note'
VIOLATION: contradictions[0].claim_b.source_id: ambiguous in-world source 'sella-bell7-note'
2 violation(s); no canon changed
```

stderr should be empty. No `claim_a` source ambiguity is expected because its event cites `tarin-note`; no endpoint event-ID finding is expected because both IDs remain unique. This prediction is falsifiable by running `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture-dir>` on both copies and recording exact stdout, stderr, exit; any additional/missing diagnostic must be reported, not explained away. Compare all files: only the negative `sources.json` should differ, by one appended row.

## Precedent, novelty and limits

R7 already explores duplicate-source ambiguity in alliance reciprocity and item provenance (`reports/r7-executor.md`; fixture scout details `reports/r7-fixture-scout.md`), and r31 tests a duplicated citation used in entities/relations/timeline (`reports/r31-executor.md:6-23`). Those are not this ledger event-source branch. R37 exercises an ambiguous ledger endpoint **event ID**, with its exact-one guard (`reports/r37-pair-scout.md`, `check_bible.py:92-95`); this proposal holds the event unique and probes its source-ID resolution instead. Claim only coverage of a duplicated source cited through Bell-7 `claim_b`'s uniquely resolved event, not generic source ambiguity or a new checker behavior.

Risk: an added row with the same ID makes the pointer ambiguous even if one row is the original; the checker must not select a winner. The report does not imply either source's prose, authenticity, truth, or rights, nor that Sella's account is false or that the ledger proves a semantic contradiction. R35 explicitly bounds the reports as attributed and unresolved, and Tarin's Harbor pointer as his observation scene, not his own location (`reports/r35-executor.md:18-22`). No canon decision follows.
