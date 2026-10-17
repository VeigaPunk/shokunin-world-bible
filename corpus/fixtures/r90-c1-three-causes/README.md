# r90-c1-three-causes

Fixture scaffolding only; not sourced story evidence.

## Expected after C1 integration

The output below is the declared after-state. The unpatched checker at e97613c was replayed before the C1 fix; its before-state output matched this expectation (exact command and complete observed output are in F1.md).

- Checker exit: `1`.
- 4 violation(s); no canon changed.
- Expected complete stdout:

```text
VIOLATION: entities[0].provenance[0].tick: required nonnegative integer
VIOLATION: entities[0].provenance[0].to_holder: dangling entity 'r90-c1-three-causes-absent-holder'
VIOLATION: entities[0].provenance[0].source_id: unknown in-world source 'r90-c1-three-causes-absent-source'
VIOLATION: entities[0].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (invalid tick); holder reference to_holder 'r90-c1-three-causes-absent-holder' absent from raw entities and absent from the resolved index; source reference 'r90-c1-three-causes-absent-source' absent from raw sources and absent from the resolved index at entities[0].provenance[0]
4 violation(s); no canon changed
```

The provenance record has exactly the four required keys (`tick`, `from_holder`, `to_holder`, `source_id`) and three latching defects: negative tick, holder id `r90-c1-three-causes-absent-holder` absent from raw entities, and source id `r90-c1-three-causes-absent-source` absent from raw sources. The two absent ids occur in no valid entity row of the raw tables (they appear only as this provenance record's own references).
