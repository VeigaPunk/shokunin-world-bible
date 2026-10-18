# Round 24 critic: relation-local ambiguous endpoints

## Finding

The proposed meaning is only safe if “ambiguous endpoint” means that the endpoint ID occurs in more than one structurally valid entity row, not that the checker can determine which entity the relation intended. A duplicate ID is input ambiguity; it does not establish a mistaken/ambiguous in-world relationship. The diagnostic should identify the relation endpoint and ID, and explicitly avoid resolving it. It should not suppress the existing duplicate-ID finding or the existing dangling-endpoint behavior for zero matches.

The current checker builds `entities` as a last-row-wins dict: `check_bible.py:45-51`; `index('entities')` emits duplicate IDs at `:57` (the duplicate is emitted at `:49`). Relation checks at `:118-122` test only membership, so a duplicate endpoint currently passes the endpoint check. This is a real gap, but it is bounded to endpoint resolution; duplicate entity rows are already separately invalid.

## Falsification and collateral risks

- **False implication of semantic ambiguity:** `r18-duplicate-pair/entities.json` contains two `harbor` rows (last row at lines 52–60); its relation at `relations.json:2-6` is `mira -> seal`, so it does not exercise an ambiguous relation endpoint at all. The checker output on this fixture is duplicate-ID plus the independent timeline place ambiguity, not relation ambiguity. Do not cite it as proof that the proposed relation-local check works. Existing duplicate reverse fixture likewise repeats `harbor` while relation endpoints remain `mira` and `seal`.
- **Over-broad side effects:** indiscriminately changing the `entities` index or emitting ambiguity whenever the whole fixture has any duplicate would incorrectly label unrelated unique endpoints. Count lookup must be per endpoint ID and per relation side. The relation’s `from` and `to` may each need independent findings; a self-edge with duplicated ID has two endpoint occurrences but is not evidence of two distinct entities.
- **Invalid-row interaction:** only rows accepted into `data['entities']` (all required fields valid, `:32-43`) are indexed. Counting raw JSON entity IDs instead would make malformed rows alter endpoint status and create cascading diagnostics. Keep the same population as current indexing, and preserve duplicate-ID errors.
- **Other downstream invariants:** `entity_id_counts` already counts valid entity rows at `:125-127`; alliance logic guards duplicate endpoints at `:207-224`, timeline logic reports ambiguous IDs at `:225-238`, and provenance logic disables a chain on duplicate item IDs at `:129-142`. Avoid refactoring those rules or changing the last-row index semantics as collateral to this narrow feature.
- **Count semantics:** distinguish count 0 (existing dangling diagnostic), count 1 (valid resolution), and count >1 (new endpoint-local ambiguity); do not report both dangling and ambiguous for the same endpoint. Do not add kind-specific inference or choose the first/last matching row.

## Suggested test

Add a minimal fixture derived from `consistent/` with a duplicate entity ID used in exactly one relation endpoint; keep the other endpoint unique. Assert the existing duplicate-ID finding remains and exactly the affected side gets a relation-local ambiguous-entity finding. Add a unique-ID control with identical relation and a duplicate unrelated ID control proving no relation endpoint ambiguity is reported. Add a two-sided duplicate control to establish whether both `from` and `to` are reported, plus dangling and malformed-duplicate controls to ensure prior semantics. Replay the unchanged prior fixture outputs and compare paths/bytes as declared in round 24. In particular, do not rely on `r18-duplicate-pair` as the positive case: its relation does not mention `harbor`.

No fixture or checker changes made in this critic report. No source-text chronology, entity identity, or canon relationship can be inferred from IDs or schema validation.
