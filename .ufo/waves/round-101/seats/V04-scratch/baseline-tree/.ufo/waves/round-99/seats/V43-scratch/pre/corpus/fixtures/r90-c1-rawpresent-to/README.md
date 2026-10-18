# r90-c1-rawpresent-to

Fixture scaffolding only; not sourced story evidence.

## Expected after C1 integration

The output below is the declared after-state. The unpatched checker at e97613c was replayed before the C1 fix; its before-state output matched this expectation (exact command and complete observed output are in F1.md).

- Checker exit: `1`.
- 5 violation(s); no canon changed.
- Expected complete stdout:

```text
VIOLATION: entities[1].name: required nonempty str
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[1].claims: required nonempty list
VIOLATION: entities[0].provenance[0].to_holder: dangling entity 'r90-c1-rawpresent-to-ghost'
VIOLATION: entities[0].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: holder reference to_holder 'r90-c1-rawpresent-to-ghost' present in raw entities but absent from the resolved index at entities[0].provenance[0]
5 violation(s); no canon changed
```

True-absence control line, measured with the unpatched checker: `VIOLATION: entities[0].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: holder reference to_holder 'r90-c1-rawpresent-to-absent' absent from raw entities and absent from the resolved index at entities[0].provenance[0]`. This control has no raw entity row for that id; it is not a fifth durable fixture. The raw-present id occurs only on the schema-invalid entity row and this provenance reference.
