# Round 21 executor report — malformed dependency member and occupancy

## Change

In `.shokunin/lore/corpus/fixtures/check_bible.py`, moved the existing guarded occupied-slot compare/store before the list-wide malformed `depends_on` diagnostic and `continue`. The `all(isinstance(dep, str) ...)` gate remains list-wide: when any member is non-string, the checker still emits one `expected event-id strings` diagnostic and skips all member-wise dependency traversal. Actor uniqueness, place existence/uniqueness/kind, and nonnegative tick guards are unchanged. Occupancy remains first-slot based; same-place rows do not replace the retained slot.

## Baseline replay

Extracted the baseline checker from commit `64d2673` and ran it and the modified checker through the Python CLI on each of the 56 fixture paths in `corpus/live/runs/20261012T191902Z/*.txt`. Compared `(exit code, stdout, stderr)` for every corresponding run: **56/56 exact matches**. No saved fixture contained a non-string member in a list-valued `depends_on`; therefore this replay found no legacy differences and does not test arbitrary inputs. The separate baseline-snapshot replay in `r21-test-scout.md` also reports 56/56 saved transcripts reproducible.

## Round 21 fixture CLI results

Ran `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture>` on all eight present `r21-*` fixture directories. Each exited 1 with empty stderr and the following stdout findings (followed by `N violation(s); no canon changed`):

| Fixture | Findings |
|---|---|
| `r21-clean` | `timeline[1]: double-booked 'mira' at tick 9 in timeline[0] ('tower') and 'harbor'` |
| `r21-malformed` | Same double-booking; `timeline[1].depends_on: expected event-id strings` |
| `r21-clean-reverse` | `timeline[1]: double-booked 'mira' at tick 9 in timeline[0] ('harbor') and 'tower'` |
| `r21-malformed-reverse` | Same reversed-order double-booking; `timeline[1].depends_on: expected event-id strings` |
| `r21-same-place` | `timeline[1].depends_on: expected event-id strings` only; no booking finding |
| `r21-invalid-tick` | `timeline[0].tick: must be nonnegative`; `timeline[1].tick: must be nonnegative`; malformed-list diagnostic; no booking finding |
| `r21-wrong-kind-place` | `timeline[1].place_id: not a place 'mira'`; malformed-list diagnostic; no booking finding |
| `r21-ambiguous-actor` | `entities[4].id: duplicate entities id 'mira'`; ambiguous actor diagnostics for timeline rows 0 and 1; malformed-list diagnostic; no booking finding |

The malformed paired fixtures therefore retain the list-wide error while reporting occupancy only when the existing actor/place/tick certainty guards pass. The clean/malformed pair differs only in the target dependency list; reverse-order pair preserves the same behavior. Output is checker analysis of fixture input, not sourced canon or proof the events occurred.

## Limits

This change is narrowly about independent occupancy analysis not being skipped due to a malformed dependency member. It does not recover valid dependency members from a mixed list: all member-wise dependency checks remain skipped for that row, as declared. No fixture, documentation, LOG, or commit was changed by this executor. No broader malformed-input behavior or facts outside the eight present fixtures were tested.
