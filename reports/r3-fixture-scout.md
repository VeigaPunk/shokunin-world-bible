# Round 3 fixture scout: valid/malformed contradiction ledger pair

## Evidence observed

- `.shokunin/lore/corpus/fixtures/contradictions/` currently contains only `entities.json`, `relations.json`, `timeline.json`, and `sources.json`; there is no ledger file. The sibling `consistent/` fixture has the same four-file layout.
- In `contradictions/timeline.json`, `arrival` is Mira at tick 2 in `tower`, depends on `later` (tick 3), and cites `courier-log`. `false-sighting` is Mira at tick 2 in `harbor` and cites `archive-ledger`; `later` cites `archive-ledger`. These rows account for existing timeline-inversion and double-booking reports.
- In `contradictions/relations.json`, `relations[1]` is `mira -> missing-map` (`consults`), citing `courier-log`; there is no `missing-map` entity in `entities.json`. This is the existing dangling-endpoint case, not a pair of two resolvable claims.
- `contradictions/sources.json` defines both `courier-log` and `archive-ledger`. Entity claim convention is an object with `statement` and `source_id` (see `entities.json`); timeline rows use `id`, `description`, and `source_id` (see `timeline.json`). The checker currently requires exactly the four sections listed in `.shokunin/lore/corpus/fixtures/check_bible.py`'s `FIELDS`; it does not load an optional ledger.
- Current baseline conflict outputs are documented in `.shokunin/lore/LOG.md` round 1 and round 2 closure: dangling endpoint, timeline inversion, double booking. I did not run or change the checker/fixtures.

## Recommendation (not existing behavior)

Use a single optional file, `contradictions/contradictions.json`, as an array of ledger records with stable `id`, `claim_a`, `claim_b`, and nonempty `why`. Represent each claim as a small reference object `{section, id, statement, source_id}`; for this fixture, `section: "timeline"` and event IDs resolve uniquely against `timeline.json`, and `source_id` resolves against `sources.json`. Require the referenced row's actual description/source to match the copied values (or omit copied statement and derive it from the row) so the ledger cannot invent a citation. This is an editorial cross-reference, not semantic proof.

A valid pair can contain these two records, preserving both assertions without choosing a winner:

1. `same-tick-location`: claim A references `arrival` (Mira at tick 2 / tower, `courier-log`); claim B references `false-sighting` (Mira at tick 2 / harbor, `archive-ledger`). `why` states the same character is recorded at different places at the same tick.
2. `arrival-before-later-dependency`: claim A references `arrival` and its `depends_on: ["later"]` (source `courier-log`); claim B references `later` (tick 3, source `archive-ledger`). `why` states the tick-2 event depends on a tick-3 event.

For the malformed counterpart, copy the valid ledger and make exactly one targeted defect, e.g. change the second record's `claim_b.id` to `absent-event` while retaining its citation fields. This should produce a ledger-local unresolved-reference diagnostic and nonzero exit, while the normal checker still reports the original three fixture violations. A simpler missing-field defect (remove `why`) is also valid, but tests only shape validation rather than claim resolution. Keep the malformed fixture independent, e.g. `contradictions-ledger-malformed/`, copying the existing contradiction tables byte-for-byte and adding the defective ledger; do not alter `contradictions/`.

The dangling `missing-map` relation should remain untouched and should not be falsely represented as a pair of resolvable cited claims: making a second claim about a nonexistent entity would undermine the declared reference-resolution requirement. Its existing checker violation can coexist with the valid ledger and remain among the three original outputs. Likewise, do not use a malformed ledger that replaces/omits the seeded tables; it should be an additive ledger defect only.

## Scope note

Recommendations above are fixture design only. No files other than this scout report were edited; no checker execution, implementation, or fixture mutation was performed.
