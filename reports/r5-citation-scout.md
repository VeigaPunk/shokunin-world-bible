# Round 5 citation scout — unresolved in-world source

## Observed

The smallest citation mutation I tested starts from the clean fixture at `.shokunin/lore/corpus/fixtures/consistent/`. In a temporary copy (not a repository fixture), I changed only `entities.json` row 0's `first_appearance` from `courier-log` to `missing-in-world-source`; `sources.json` and all other inputs were unchanged. The checker loads source IDs from `sources.json`, then validates each entity `first_appearance` and each claim `source_id` using the same `source()` lookup.

Command (with the temporary fixture path substituted by the test run):

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/lore-r5-unknown-source-ywo6rtii/fixture
```

Observed exit: `1`. Stdout:

```text
VIOLATION: entities[0].first_appearance: unknown in-world source 'missing-in-world-source'
1 violation(s); no canon changed
```

The observed diagnostic identifies the bad location and unresolved ID; it does not report a crash, infer what the source should be, or alter data. This tests an unknown source *reference*, not whether a resolvable source actually supports the assertion.

## Minimal reproducible fixture recommendation

For a committed probe, copy the clean five-table fixture into a dedicated malformed case (for example `corpus/fixtures/citation-unknown-first-appearance/`) and change only `entities.json[0].first_appearance` to an ID absent from its unchanged `sources.json`. Keep all remaining tables byte-identical. Run from the repository root:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/citation-unknown-first-appearance
```

Expected based on the observed probe: exit `1`, exactly the location-local `unknown in-world source` citation diagnostic plus the final violation count. A useful orthogonal probe, if the table needs multiple citation locations, is changing only `entities.json[0].claims[0].source_id` instead; the checker routes that through the same lookup but reports `.claims[0].source_id`.

## Limits / recommendation

This is one observed citation-error pattern, not an exhaustive citation test. The checker verifies ID membership only; it does not validate source truth, source text, attribution, or evidentiary support. Do not call a resolvable-but-unsupportive citation invalid based on this probe. The mutation was temporary; no checker, fixture, or shared documentation was edited.
