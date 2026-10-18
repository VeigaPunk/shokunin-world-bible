# Round 24 simplifier findings

## Minimal checker edit

In `corpus/fixtures/check_bible.py`, leave `index()` (lines 45–51) and its existing duplicate-ID finding intact. Do not change the `entities` mapping: it intentionally retains last-row lookup behavior used elsewhere. The relation endpoint loop at lines 118–121 currently tests only membership in that mapping, so a duplicate ID is treated as present and no relation-local finding is emitted.

The existing `entity_id_counts` computation at lines 125–127 is the smallest safe source of ambiguity status. Move that computation immediately before the relation loop, then add an `elif entity_id_counts[row[endpoint]] > 1` after its existing dangling check to emit one endpoint-local message, e.g. `f'{location}.{endpoint}: ambiguous entity {row[endpoint]!r}'`. Keep dangling precedence and the existing source diagnostic unchanged. This avoids changing entity indexing or any downstream resolution behavior.

## Risks / boundaries

- Check that count lookup is only performed after membership succeeds; otherwise a dangling endpoint can raise `KeyError`.
- Keep findings relation-local and per endpoint (`from` and `to` independently); do not infer a relation between duplicate rows or pick a canonical row.
- Moving the count construction earlier is behavior-neutral if it only counts valid `data['entities']` rows, as the current loop does. Preserve its later use by provenance, allied relations, and timeline checks.
- Existing relation endpoint diagnostics will intentionally gain ambiguity findings only for duplicate entity IDs. No change to the duplicate-ID diagnostic, relation schema, source checks, or other consumers is needed.

## Suggested test

Use the cited duplicate-entity fixture from the round 24 fixture scout when available. Assert that a relation endpoint referencing the duplicated ID reports both the existing `entities[...].id: duplicate entities id ...` finding and a relation-local `relations[...].from` or `.to: ambiguous entity ...` finding, while the other endpoint remains independently assessed. Compare a unique-ID control (same relation shape) and assert it has no ambiguity finding. Replay all pre-existing fixture outputs against the baseline to ensure no prior output changes.
