# Round 32 non-author reviewer report

## Independent replay

From the repository root, ran `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture>` for each target:

| Fixture | Exit | Result |
|---|---:|---|
| `r32-source-malformed` | 1 | exactly `sources[2].title: required nonempty str`; one violation |
| `r31-source-ambiguous` | 1 | duplicate source ID plus seven ambiguous citation findings; eight violations |
| `r31-source-unique` | 0 | clean; zero violations |

All three produced empty stderr. The outputs match the executor report.

## Pair and implementation check

Compared parsed source rows: the sole changed field is `sources[2].title`, populated in r31 and `""` in r32. The duplicate row's raw `id` remains `courier-log`. The other four tables (`entities.json`, `relations.json`, `timeline.json`, `contradictions.json`) are byte-identical. In `check_bible.py`, required fields are checked before a row is appended to `data[section]`; invalid rows are excluded. Both `index('sources')` and `source_id_counts` use that admitted collection. Thus this test's output is consistent with title validation excluding that row from the admitted source count. The r31 valid duplicate still exercises the ambiguous state across all seven references; the unique control is clean.

## Interpretation / caveat

The missing duplicate-ID and ambiguous-citation diagnostics in r32 mean only that this checker did not count the malformed row among admitted sources. The raw duplicate remains present. This does not establish source uniqueness in-world, whether either source is true, false, reliable, or supported by its cited text, nor canon, rights clearance, or permission for AI training. No production edits were made.
