# r90-c1-rawpresent-from

Fixture scaffolding only; not sourced story evidence.

## Expected after C1 integration

The output below is the declared after-state. The unpatched checker at e97613c was replayed before the C1 fix; its before-state output matched this expectation (exact command and complete observed output are in F1.md).

- Checker exit: `1`.
- 5 violation(s); no canon changed.
- Expected complete stdout:

```text
VIOLATION: entities[2].name: required nonempty str
VIOLATION: entities[2].first_appearance: required nonempty str
VIOLATION: entities[2].claims: required nonempty list
VIOLATION: entities[0].provenance[0].from_holder: dangling entity 'r90-c1-rawpresent-from-ghost'
VIOLATION: entities[0].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: holder reference from_holder 'r90-c1-rawpresent-from-ghost' present in raw entities but absent from the resolved index at entities[0].provenance[0]
5 violation(s); no canon changed
```

The raw-present id occurs only on the schema-invalid entity row and this provenance reference.
