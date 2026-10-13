# Round 25 pair-scout — minimal fixture mutation

## Recommendation

Use a three-case fixture set focused on the endpoint loop’s uncovered `to` branch: (A) existing `r12-unique-actor` as the unique-endpoint control, (B) copy `r12-ambiguous-actor` and change only `relations[0].from` from `mira` to `seal`, yielding duplicate `mira` solely at `relations[0].to`, and (C) optional both-sides case from B changing that `from` back to `mira`. B is the smallest direct probe: one relation-field edit on the already sourced duplicate-entity fixture. C checks two findings, but adds little to branch coverage and can be deferred unless the round’s claim requires both-side behavior.

## Evidence

- The Round 25 declaration explicitly seeks duplicate `to`, optional both-side case, and unique control: `.shokunin/lore/LOG.md:366-369`.
- The checker iterates `('from', 'to')` and flags an endpoint whose ID count exceeds one: `.shokunin/lore/corpus/fixtures/check_bible.py:123-130`. Round 24 independently established the `from` behavior and notes no independent `to` fixture: `.shokunin/lore/LOG.md:362-364`.
- In `r12-ambiguous-actor`, the repeated `mira` rows are at `entities.json:3` and `:51`; the additional record cites `archive-ledger` (`entities.json:54-57`), while the relation cites `courier-log` (`relations.json:2-6`). Thus swapping the relation endpoint to `to` leaves cited relation/source intact and preserves ambiguity solely from duplicate entity IDs.
- The paired `r12-unique-actor` removes only the second `mira` entity row; its relation remains `mira -> seal`, type `carries`, source `courier-log` (`entities.json:3`; `relations.json:2-6`). It is already an exact unique-ID endpoint comparison, though not a clean whole-bible exit according to Round 24: `.shokunin/lore/LOG.md:357-363`.

## Risks / bounded claim

A paired custom `to` fixture and its duplicate-free twin could alter only the second `mira` row (or its absence), preserving every other file; however reusing and reversing `r12` relation endpoints minimizes new data. Reversing `from`/`to` changes which direction the fictional relation record asserts, not canon truth; keep it clearly a synthetic checker fixture and make no lore inference. Unique control may have unrelated existing findings, so require its output to remain unchanged and its tested endpoint to avoid an ambiguity diagnostic, not necessarily exit zero. Check exact expected location `relations[0].to` and avoid reading total-count shifts as distinct coverage. Existing fixture baseline outputs/paths remain a separate regression requirement from the proposed fixture mutation.
