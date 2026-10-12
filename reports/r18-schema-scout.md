# Round 18 schema scout — duplicate IDs and required-field screening

## Raw observations

I ran the current `.shokunin/lore/corpus/fixtures/check_bible.py` directly against temporary JSON directories under `/tmp/r18schema-yt8y9uvq` (not repository fixtures). Each probe had one unique character `actor`, one unique place `tower`, and two timeline rows for `actor` at tick 1, one at `tower`, one at `harbor`. All required fields were present and sources resolved unless stated. The exact CLI output was:

- **Control, unique `harbor` place:** `VIOLATION: timeline[1]: double-booked 'actor' at tick 1 in timeline[0] ('tower') and 'harbor'` (exit 1).
- **Duplicate `harbor`, both rows kind `place`:** duplicate entity-ID error; `timeline[1].place_id: ambiguous place entity 'harbor'`; and the same `double-booked` finding (exit 1).
- **Mixed-kind `harbor` (`place` + `character`):** same three findings as the duplicate same-kind case (exit 1). The index/count path does not distinguish duplicate kinds: both rows pass required-field screening and count toward `entity_id_counts`; ambiguous `place_id` is retained in occupancy because current `comparable_place` treats any count other than one as comparable.
- **Duplicate same-kind non-place `mira` (`character` + `character`) used as `place_id`, with no `harbor` entity:** duplicate-ID error and `timeline[1].place_id: dangling entity 'harbor'` only (exit 1). This demonstrates no alias-based resolution: IDs are exact strings.
- **Duplicate `harbor`, second entity missing `kind`:** required-field error `entities[3].kind: required nonempty str`; that row is excluded from `data['entities']` before indexing. The remaining unique `harbor` place resolves, and the pair still gets `double-booked` (exit 1), with no ambiguous-place finding.
- **Duplicate `harbor`, second entity kind `moon`:** it passes required-field screening, is indexed, then gets `unknown kind 'moon'`; entity ID is duplicate, `harbor` is ambiguous, and the pair still gets `double-booked` (exit 1).

## Screening semantics visible in source

Per section, a row is appended to `data[section]` only if every declared field exists, has its exact declared Python type (`type(value) is expected`), and string values are nonempty after stripping. Thus an invalid required field prevents that row from contributing to duplicate-ID counts and resolution. Allowed-kind membership is a later semantic check, not required-field screening: a nonempty unknown kind remains indexed. The entity index reports a duplicate ID but overwrites its map value with the last screened-in row; timeline occupancy separately uses the count. For `place_id`, count >1 produces ambiguity regardless of whether the duplicate records are same-kind, mixed-kind, or include an unknown kind; occupancy currently admits that count because `place_id_count != 1`.

## Assessment / recommendation (not raw observation)

The current behavior confirms the declared r18 gap for both duplicate same-kind and mixed-kind IDs: they both produce an ambiguous-place diagnostic but still participate in the raw-ID `double-booked` comparison. Field-screening changes the classification: an invalid duplicate row is absent from the index, potentially making the remaining valid entity unique; a bad nonempty `kind` is not absent and keeps the ID ambiguous. If implementing the declared move, exclude count >1 references from occupancy compare **and insertion**, while retaining duplicate/ambiguous diagnostics and timeline rows. Keep the unique-place control as a guard. This is checker-ID identity handling only; it proves neither actual locations nor source-text support, canon, nor absence of a real conflict.
