.shokunin/lore/reports/r24-regression-scout.md

# Round 24 regression scout: baseline inventory and replay

## Baseline inventory

The round-24 declaration is `.shokunin/lore/LOG.md:349-352`; it identifies baseline commit `d0e1c73b28fdf971c41cb095d709bfcd9edeffbc` and states that relation endpoints currently receive dangling-only checks. In the checker, `index()` reports a duplicate ID but overwrites the indexed value with the last row (`.shokunin/lore/corpus/fixtures/check_bible.py:45-51`). Relation rows are validated for endpoint membership only (`:118-121`); thus duplicate entity IDs may yield the global duplicate finding but no relation-local ambiguity, and endpoint behavior may depend on last-row index order.

Current fixture inventory: 73 fixture directories (excluding README/checker), 364 JSON files. The last saved run at `.shokunin/lore/corpus/live/runs/20261012T193930Z/` contains 72 `.txt` outputs, covering all fixture directories except `r23-note-class`. This run is described in round-22 closure at `.shokunin/lore/LOG.md:358-360`; round 23 subsequently added its fixture. Its relation-focused regression set is:

- `r7-ally-reverse-ambiguous` (duplicate source IDs, not entity endpoints)
- `r11-place-character`, `r11-character-place`, `r11-unique-nonplace`, `r11-dangling-place` (duplicate/unique/missing entities, but place-field resolver)
- `r18-duplicate-pair`, `r18-duplicate-reverse`, `r18-mixed-kind`, `r18-unique-pair`, `r18-known-through-ambiguous`, `r18-duplicate-first-known` (occupancy-specific resolver)
- `consistent`, `ally-reciprocal`, `ally-one-way`, `contradictions`, and other general fixtures.

Existing coverage does not appear to exercise a relation whose `from` or `to` string maps to multiple entity rows. `r11` and `r18` are useful adjacent controls but exercise timeline fields, not relation-local diagnostics. Fixture README round-11 explicitly scopes its behavior to timeline `place_id` (`.shokunin/lore/corpus/fixtures/README.md`, “Round 11”), and round 18 likewise scopes ambiguity to occupancy.

## Exact replay

Run from repository root, preserving stdout, stderr, and exit status independently:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r11-place-character
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r11-character-place
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r11-unique-nonplace
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r18-duplicate-pair
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r18-unique-pair
```

For exact saved-run replay comparison, each command is invoked once per fixture and compare stdout bytes, stderr bytes, and exit status against `.shokunin/lore/corpus/live/runs/20261012T193930Z/<fixture>.txt`. First inspect the `.txt` format: it may encode output/status together; do not assume a shell `diff` alone proves exit-code equality. For broad regression, enumerate all fixture directories and compare each checker invocation against the corresponding saved output where present. The 72 saved outputs predate `r23-note-class`, so exclude that fixture from this historical baseline comparison or run it separately as current-only. Also retain a sorted path inventory (`git ls-tree -r --name-only d0e1c73 -- .shokunin/lore/corpus/fixtures`) for baseline-path comparison; current inventory must not be mislabeled as baseline.

## Risks / suggested test

- The dict index is last-row-wins, so a new per-relation ambiguity finding must not accidentally select a duplicate entity or alter existing dangling/other relation diagnostics. Test both endpoint roles, duplicate rows ordered either way, and unique and missing controls.
- Keep the test tightly relation-local: duplicate entity ID plus a relation referencing it should yield duplicate-ID plus a local ambiguity at the precise `.from`/`.to` location; a unique-ID relation control should not gain ambiguity. A missing endpoint should retain dangling behavior. Include duplicated IDs with differing kinds to expose accidental kind-based selection.
- Compare all historical fixture path names and exact outputs/statuses against the declared baseline/current saved run; avoid claiming 72 outputs cover fixtures added later.
- These checks establish checker behavior on invented JSON only. They do not resolve entity identity, relation meaning, source support, or canon.
