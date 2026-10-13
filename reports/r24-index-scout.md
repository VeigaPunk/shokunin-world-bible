# Round 24 index scout — overwrite and ambiguity behavior

## Findings

`index(section)` stores one row per ID in a dict. At `check_bible.py:45-51`, it emits a duplicate-ID diagnostic when the ID is already present, then unconditionally assigns `result[row['id']] = row`. Therefore the dict keeps the **last** duplicate row; the earlier row is lost for all consumers of that index. This applies to sources, entities, timeline, and contradictions (`:53-59`). For a relation endpoint, `:118-122` tests only membership in this last-wins entity dict. A duplicated ID therefore appears resolvable and yields no relation-local ambiguity diagnostic. The duplicate entity diagnostic exists at the index creation site (`:48-50`), but lacks relation location/endpoint context.

This differs from explicitly ambiguity-aware source handling: source multiplicities are separately counted (`:54-56`), and `source_status` returns `ambiguous` for count >1 (`:64-66`); the helper reports ambiguity at the caller's field location. Entity multiplicity is also counted separately (`:125-127`) for the provenance-chain guard (`:141`), but that count is not consulted in relation endpoint validation. Thus the endpoint validator has the data needed to distinguish zero, one, and multiple rows, but currently uses last-wins membership alone.

Existing concrete cases: `corpus/fixtures/r12-ambiguous-actor/entities.json` duplicates `mira` and its `relations.json` points `from` at `mira`; equivalent cases exist in `r21-ambiguous-actor`. Each relation endpoint is accepted by the membership check despite entity index ambiguity. Other duplicate fixtures include `r18-duplicate-pair`, `r18-duplicate-reverse`, `r18-mixed-kind`, `r18-known-through-ambiguous`, and `r18-duplicate-first-known`.

## Risks / bounds

- A proposed relation-local error should be additive to (not a replacement for) the existing duplicate-ID error, and should be emitted independently for each ambiguous `from` or `to` endpoint. Preserve dangling behavior for zero matches and existing behavior for one match.
- Do not use the indexed row's `kind` to infer endpoint uniqueness: it is last-wins and order-dependent. Count rows from the validated entity list or use an explicit count map.
- Avoid changing `index()` globally to first-wins or reject duplicates early: that changes unrelated resolution behavior and can affect existing diagnostics. The targeted endpoint check is the smaller seam.
- Ambiguity means multiple fixture rows share the identifier; it does not establish which row is true, nor any canon relationship.

## Suggested test

Use `r12-ambiguous-actor` (or `r21-ambiguous-actor`) as the existing duplicate-ID case: assert the existing duplicate entity-ID message remains and a new error names the exact relation path plus `.from` and identifies `mira` as ambiguous. Add/retain a unique-ID relation control that exits cleanly. For locality, make a test with a duplicated `to` identifier and a unique `from`, asserting only `.to` receives the ambiguity message; optionally reverse the duplicate entity row order and assert the same relation-local result, demonstrating it is independent of last-wins indexing. Replay baseline fixture outputs because the diagnostic is an intentional output change only for fixtures with ambiguous relation endpoints.
