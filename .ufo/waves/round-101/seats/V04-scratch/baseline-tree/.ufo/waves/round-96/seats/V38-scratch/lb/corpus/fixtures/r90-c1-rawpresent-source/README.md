# r90-c1-rawpresent-source

Fixture scaffolding only; not sourced story evidence.

## Expected after C1 integration

The output below is the declared after-state. The unpatched checker at e97613c was replayed before the C1 fix; its before-state output matched this expectation (exact command and complete observed output are in F1.md).

- Checker exit: `1`.
- 4 violation(s); no canon changed.
- Expected complete stdout:

```text
VIOLATION: sources[1].title: required nonempty str
VIOLATION: sources[1].reliability_note: required nonempty str
VIOLATION: entities[0].provenance[0].source_id: unknown in-world source 'r90-c1-rawpresent-source-ghostsrc'
VIOLATION: entities[0].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: source reference 'r90-c1-rawpresent-source-ghostsrc' present in raw sources but absent from the resolved index at entities[0].provenance[0]
4 violation(s); no canon changed
```

The raw-present source id occurs only on the schema-invalid sources row and this provenance reference.
