# Round 87 provenance probe — record and chain classes

A minimal authored micro-bible exercising the record-validation, source-resolution, chain-comparison, and post-stop classes of the `check_bible.py` provenance block, one item per class group:

- `lamp` (item): record-local shape classes — non-object record, missing and extra keys, boolean and negative ticks, whitespace `from_holder`, non-string `to_holder`, dangling holders, blank `source_id`, unknown `source_id`.
- `rope` (item): ordered-comparison classes — first record with non-null `from_holder`, equal tick, reversed tick, holder discontinuity, a second discontinuity (no latch), both comparisons on one record, and an unknown source that latches the tail.
- `bell` (item): ambiguous holder identity on both fields at the first record, then a later record.
- `chime` (item): ambiguous holder identity first appearing after an earlier invalid record.
- `anvil` (item): an ambiguous source citation that does not invalidate the record, with a later prefixed chain break.

`ambig-source` is duplicated in `sources.json` and `dup` is duplicated in `entities.json`; those duplicate rows are test scaffolding, not a choice between identities or evidence about custody. Source IDs resolve only to supplied in-world records and do not establish source support or canon.

Replay from the repository root:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-probe-record-and-chain
```

Expected: 35 findings, exit 1; each class above is observable in the pasted output of `corpus/knowledge/r87-provenance-chain-decision-table.md`.
