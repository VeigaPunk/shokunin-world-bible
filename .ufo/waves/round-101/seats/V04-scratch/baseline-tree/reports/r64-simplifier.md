# Round 64 simplifier report — invalid entity-row ID and dangling references

## Independent decision: NO-GO for the stated candidate

A successfully parsed entity array with a rejected row does not currently retain that row in the entity index. A referenced ID present only in that rejected raw row therefore receives a `dangling entity` finding. This is a real input-index limitation, but I find no adequately demonstrated material calibration gain for suppressing it: the proposed suppression risks removing a direct repair pointer and treating an invalid row's ID as a meaningful partial identity. Keep the row-local schema diagnostic and current reference finding unless a matched practical case establishes that the latter materially misleads users.

## Code and output evidence

- `.shokunin/lore/corpus/fixtures/check_bible.py:65-76`: rows are validated against required fields; any failed field sets `valid = False`, and only valid rows are appended to `data[section]`. At `:78-87` (entity index construction), lookup/counts are consequently over admitted rows, not raw rows.
- `.shokunin/lore/corpus/fixtures/check_bible.py:161-169` checks relation endpoints against that index; `:274-283` checks timeline actor/place references against it. Provenance holder lookup at `:206-224` also uses `entity_id_counts`; it separately prevents invalid/ambiguous holders from qualifying for a chain. These are the relevant consumers; a global “raw IDs count as present” rule would be too broad.
- In temporary copies only, changing a valid referenced entity row to omit required `name` makes the schema finding and dangling lookup coexist; changing the same source to a valid complete entity row makes the dangling finding disappear. The repository's `r60-empty`, `r60-partial`, `r60-unavailable`, and `r60-unavailable-independent` controls were run unchanged: empty reports six dangling references, partial reports three, unavailable emits the loader error without dependent dangling findings, and unavailable-independent retains tick/source/dependency findings. This confirms availability is a separate, already implemented case; it does not establish benefit for invalid rows inside a loaded array. I made no repository fixture or checker change.

The candidate's central premise—that a usable string ID in a schema-invalid raw row should make membership indeterminate—cannot be represented merely by indexing that ID as present: that risks counting it as an entity, especially in duplicate/uniqueness and typed-kind checks. A purpose-built “matching row invalid” status could preserve a reference-site repair pointer, but would add status/branching, and has not been shown better than the existing explicit schema error plus dangling pointer. In particular, do not extend r60's unavailable-table policy: an invalid row is an observed row with a specific field defect in an otherwise parsed array, not an unavailable entity table.

## Smallest safe rule / falsifier

**Rule now:** no checker change. Continue resolving only admitted schema-valid rows; retain the row-local schema error and existing dangling finding for references missing from that admitted index. This does not claim the raw ID is false, the fictional entity is absent, or that the invalid row is a valid entity.

Reconsider only if a matched, concrete case shows an operator-facing false absence conclusion that is not already repaired by the paired row-local required-field diagnostic, and a narrowly worded reference diagnostic (e.g. “cannot assess: matching entity row invalid”) improves actionability while preserving a repair pointer. Falsifier for the proposed change is that the row-local schema finding plus dangling finding provides the clearer repair route, or that status handling masks a truly absent ID / duplicate ambiguity, changes valid-row kind or occupancy qualification, or breaks provenance gating. Test malformed-with-ID, malformed-without-ID, valid loaded-empty/valid-absent, valid duplicate ID, and unavailable table controls before claiming material gain.

## Harm boundaries

A malformed row's raw string ID is not evidence that a valid entity exists, has a kind, is a holder/place/faction, or participates in occupancy/alliance/provenance. Never suppress or rewrite source/tick/dependency diagnostics based on it. Any future reference-local “invalid row” pointer must not mask genuinely absent IDs or valid duplicate-ID ambiguity. No source truth, fictional-world fact, chronology, canon, rights, or permission inference follows from these structural checks.

No code, fixtures, README, or LOG changed; no commit.
