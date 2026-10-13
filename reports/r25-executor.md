# Round 25 executor report

Created only `corpus/fixtures/r25-to-unique/**`, `corpus/fixtures/r25-to-ambiguous/**`, and this report. Both fixtures copy the five JSON tables from `consistent/`. The unique fixture is byte-identical across all five tables. The ambiguous fixture has the same four tables byte-identically; `entities.json` adds one structurally valid item (`id: seal`, distinct name `Seal in courier ledger`, `first_appearance: courier-log`, `claims: []`). The relation remains the copied cited `mira -> seal` relation.

## Checker results

Commands used: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r25-to-unique` and corresponding `r25-to-ambiguous`.

Unique: exit 0; stdout exactly `CLEAN: schema, citations, relations, timeline; 0 violations\n`; stderr empty.

Ambiguous: exit 1; stdout exactly:

```text
VIOLATION: entities[4].id: duplicate entities id 'seal'
VIOLATION: relations[0].to: ambiguous entity 'seal'
2 violation(s); no canon changed
```

stderr empty. The only relation-endpoint ambiguity is `relations[0].to`; `from` is not ambiguous. The duplicate-ID finding is separate.

## Pair difference and limits

Across the pair, the only byte difference is the ambiguous `entities.json`, which appends the duplicate row above; the four other JSON tables are byte-identical. The duplicate row cites a locally defined source ID in `first_appearance`; empty claims avoid adding an unsupported story claim. Citation-ID resolution does not establish that the source text supports the relation, and the checker output explicitly says no canon changed. This is a structural endpoint ambiguity probe only: no row is selected, no relation truth is asserted, and no canon resolution is made.
