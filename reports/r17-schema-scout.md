# Round 17 schema scout: entity screening and kind semantics

## Observed raw checker behavior

Inspected `.shokunin/lore/corpus/fixtures/check_bible.py` (baseline checker named in the round-17 LOG declaration). `FIELDS["entities"]` requires `id: str`, `kind: str`, `name: str`, `first_appearance: str`, and `claims: list`. For each required field, the checker requires presence, exact Python type (`type(value) is expected`), and for strings a nonempty `.strip()`. The `valid` flag starts true and becomes false on any required-field failure. Only rows still valid are appended to `data["entities"]`; thus subsequent entity indexing/resolution only sees required-field-screened rows. Extra keys do not invalidate a row.

`KINDS` is exactly `{'character', 'place', 'faction', 'item'}`. It is checked later in the entity semantic pass (`row['kind'] not in KINDS` → `unknown kind ...`), after valid rows have been indexed. An unknown but nonempty string kind therefore remains an indexed entity; it gets an unknown-kind finding, and downstream consumers can resolve its ID. A `place_id` resolving uniquely to that entity also gets `not a place`. Missing, empty, or non-string kind fails required-field screening, so that entity row is excluded from the index; references to its ID can consequently get `dangling entity` instead. These are distinct paths: malformed required-field row (screened out) versus schema-valid string with unrecognized kind (retained, semantically invalid).

Raw CLI probes used temporary copies of the existing `consistent` fixture under `/tmp/r17-schema-tos6_bll/` (not repository fixtures): one removed `kind` from the harbor entity; one changed it to `planet`. Command: `python3 .shokunin/lore/corpus/fixtures/check_bible.py <probe-directory>`.

Missing-kind stdout:
```
VIOLATION: entities[1].kind: required nonempty str
VIOLATION: timeline[0].place_id: dangling entity 'harbor'
2 violation(s); no canon changed
```

Unknown-kind stdout:
```
VIOLATION: entities[1].kind: unknown kind 'planet'
VIOLATION: timeline[0].place_id: not a place 'harbor'
2 violation(s); no canon changed
```

This establishes how required-field screening and allowed-kind validation differ; it does not claim that a malformed or unknown-kind record establishes fictional-world truth.

## Recommendations (not current behavior)

- Keep the Round-17 calibration claim explicitly scoped to a uniquely resolved, required-field-screened entity row whose string kind is not `place`. A missing/non-string/blank kind is not in the indexed entity map and follows the dangling path; it is not an example of the proposal's unique wrong-kind case.
- Keep the allowed set explicit: `character`, `place`, `faction`, `item`. Do not treat arbitrary strings as an allowed category, and do not imply that `unknown kind` means the entity ID failed to resolve.
- For a fixture, use a complete entity with a valid nonempty string ID/name/first appearance and list-valued claims, but a recognized non-place kind (e.g. `character`); retain a separate malformed-kind control only if needed to show the screening distinction. Any finding is structural checker output, not canon adjudication.
