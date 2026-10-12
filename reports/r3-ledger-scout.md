# Round 3 ledger scout — minimal explicit records

## Evidence observed (existing files)

- The round-3 claim in `.shokunin/lore/LOG.md` asks for cited records with `claim_a`, `claim_b`, and `why`, preserving claims without choosing a winner.
- `corpus/fixtures/contradictions/timeline.json` has records `arrival`, `false-sighting`, and `later`. `arrival` and `false-sighting` assign Mira different places at tick 2, with source IDs `courier-log` and `archive-ledger`. `arrival.depends_on` names `later`, whose tick is 3.
- Both cited IDs resolve in `corpus/fixtures/contradictions/sources.json`; source records describe a first-person log and a municipal record, not omniscient truth.
- `corpus/fixtures/contradictions/relations.json` contains a sourced `carries` relation and a `consults` relation whose endpoint `missing-map` is absent. The latter is a dangling-reference/schema conflict, not an opposing claim in the existing records.
- `.shokunin/lore/corpus/knowledge/2026-10-12-lore-decision-table.md` already says differing locations and inverted prerequisites should be reported without selecting a winner or reordering canon.

## Recommendation (not existing behavior/evidence)

Use a small `contradictions.json` array in the contradictory fixture. Keep the required three keys and make `claim_a` / `claim_b` string references to existing records using `section#record-id[.field]`; this reuses their existing citations rather than duplicating source IDs or claim text. `why` is a short editorial explanation, not a verdict. Example:

```json
[
  {
    "claim_a": "timeline#arrival",
    "claim_b": "timeline#false-sighting",
    "why": "Both place Mira at tick 2, but at North Tower and Lantern Harbor respectively."
  },
  {
    "claim_a": "timeline#arrival.depends_on",
    "claim_b": "timeline#later.tick",
    "why": "Arrival names later as a prerequisite even though later has tick 3 and arrival tick 2."
  }
]
```

These pointers identify the exact existing cited records; the checker can resolve IDs and confirm each record has a resolvable `source_id` without attempting semantic adjudication. The pointers and examples are a proposal, not data currently present in the fixture. If the implementation prefers claim text rather than pointers, it should still retain explicit record IDs alongside text so citation provenance is unambiguous.

Do **not** fabricate a `claim_b` for `relations#missing-map`: the missing endpoint has no existing record or citation to point to, and is not an opposing assertion. Keep that as the original dangling-endpoint diagnostic. A ledger need not force every checker violation into a two-sided contradiction. Likewise, the two timeline ledger entries are editorial links to existing facts; neither proves which account or ordering is canon. `why` explains the conflict only. No record should be deleted, rewritten, or selected as correct.
