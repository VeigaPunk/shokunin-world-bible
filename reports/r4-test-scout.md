# Round 4 test scout — replay matrix

Scope: read-only inspection of `.shokunin/lore/corpus/fixtures/` and direct CLI replays from the repository root. The five existing fixture directories are `consistent`, `contradictions`, `ally-reciprocal`, `ally-one-way`, and `contradictions-ledger-malformed`. At inspection time there are no name-specific fixture directories (`list(root.glob("*name*"))` was empty); the new paired cases are therefore recommendations, not observed results.

## Existing fixture replay (observed)

Command for each row:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>
```

| Fixture | Expected/current exit | Observed salient output | Replay result |
|---|---:|---|---|
| `consistent` | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` | Pass; clean baseline retained. |
| `contradictions` | 1 | 3: dangling `relations[1].to` (`missing-map`); timeline inversion (`arrival` depends on `later`, tick 3 vs 2); double-booking (`mira`, tick 2, `tower`/`harbor`). | Pass; all three seeded diagnostics observed. |
| `ally-reciprocal` | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` | Pass; reciprocal control remains clean. |
| `ally-one-way` | 1 | 1: `relations[0]` `allied_with` edge `quay-guild` → `bell-wardens` lacks sourced reciprocal. | Pass; prior negative control reproduced. |
| `contradictions-ledger-malformed` | 1 | 4: ledger-local `claim_b.event_id` absent-event error plus the same three contradiction diagnostics. | Pass; malformed ledger diagnostic and prior errors reproduced. |

The CLI outputs above are fresh direct replays, not inferred from README claims. The checker and fixture paths inspected were `.shokunin/lore/corpus/fixtures/check_bible.py`, `.shokunin/lore/corpus/fixtures/README.md`, and the five fixture directories listed above. Each existing `entities.json` was inspected: none currently repeats a displayed `name` among distinct entity IDs.

## Proposed paired name fixtures (not yet present/replayed)

Keep the pair minimal and identical except for one entity `name` value, preserving all other tables and existing records. Both cases should use valid distinct entity IDs and already-resolvable `first_appearance`/claim source IDs; this isolates the proposed exact, case-sensitive duplicate displayed-name behavior from unrelated schema/citation failures. Cite the name-bearing entity records through their existing required source fields; do not invent a new disambiguation field unless the implementation explicitly adopts and documents one.

| Proposed fixture | Minimal distinguishing data | Expected result if round-4 claim is implemented |
|---|---|---|
| `name-distinct` (positive control) | Two valid entities with distinct IDs and distinct exact `name` strings. | Exit 0; no name-collision diagnostic. |
| `name-duplicate` (negative case) | Same data, but those two distinct IDs have the exact same case-sensitive `name`. | Exit 1; one name-local collision diagnostic identifying both IDs/record locations; no entity merged or rewritten. |

Run both commands alongside all five existing cases. Require the five existing exit/output patterns above to remain unchanged, `name-distinct` clean, and `name-duplicate` to produce the expected diagnostic. If checker policy flags every group of N identical names once, assert one diagnostic per duplicate-name group; avoid overprescribing ordering or exact punctuation. A case-only variant such as `Mira`/`mira` is outside this round's exact-equality claim and should not be conflated with the paired core test.

## Recommendations (separate from observations)

1. Add the two paired fixture directories with the same source table and valid non-name fields; change only the second entity's exact `name` between the pair.
2. Preserve the five existing replay results as regression gates, especially all three diagnostics in `contradictions` and all four in `contradictions-ledger-malformed`.
3. Check that a duplicate name reports both entity IDs/locations and does not alter fixture files or collapse IDs. Keep case folding, aliases, transliteration, and canon-level uniqueness assumptions out of the claim unless separately declared and tested.
4. After fixture creation, rerun the seven-case matrix from repo root and save command/output/exit evidence in the round's run artifact or verifier report; this scout did not create fixtures or code and cannot attest those proposed results.
