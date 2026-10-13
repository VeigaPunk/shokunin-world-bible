# Round 32 executor report

Scope: created only `corpus/fixtures/r32-source-malformed/` and this report. The fixture copies all five JSON tables from `r31-source-ambiguous`; the only parsed field changed is `sources[2].title`, from `Courier Log Registry Duplicate Index` to `""`. Its `id` remains `courier-log` and every other field is unchanged. `entities.json`, `relations.json`, `timeline.json`, and `contradictions.json` are byte-identical to the admitted duplicate fixture.

Commands were run from repository root with `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture-path>`.

## Exact outputs

### malformed (`r32-source-malformed`), exit 1
```
VIOLATION: sources[2].title: required nonempty str
1 violation(s); no canon changed
```

### admitted duplicate (`r31-source-ambiguous`), exit 1
```
VIOLATION: sources[2].id: duplicate sources id 'courier-log'
VIOLATION: entities[0].first_appearance: ambiguous in-world source 'courier-log'
VIOLATION: entities[0].claims[0].source_id: ambiguous in-world source 'courier-log'
VIOLATION: entities[3].first_appearance: ambiguous in-world source 'courier-log'
VIOLATION: entities[3].claims[0].source_id: ambiguous in-world source 'courier-log'
VIOLATION: relations[0].source_id: ambiguous in-world source 'courier-log'
VIOLATION: timeline[0].source_id: ambiguous in-world source 'courier-log'
VIOLATION: timeline[1].source_id: ambiguous in-world source 'courier-log'
8 violation(s); no canon changed
```

### unique control (`r31-source-unique`), exit 0
```
CLEAN: schema, citations, relations, timeline; 0 violations
```

All commands produced no stderr (empty). The malformed row remains in raw JSON. The absence of duplicate-ID and reference ambiguity findings reports only this checker's admitted-source count after required-field validation; it says nothing about global uniqueness, source truth, canon, or rights.
