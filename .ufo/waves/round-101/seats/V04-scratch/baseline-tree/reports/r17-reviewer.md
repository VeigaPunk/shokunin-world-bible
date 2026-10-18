# Round 17 independent reviewer — raw replay and boundary probes

## Scope and method

Non-author review; no source, fixture, documentation, or commit edits. I inspected the round-17 LOG declaration, current checker diff and fixture README/decision-table additions, six raw fixture directories, executor evidence, and saved run `corpus/live/runs/20261012T184609Z/`. I independently ran the current checker with Python 3 against every fixture directory currently present (39 total) and compared each exit code, stdout, and stderr with its saved transcript. I also made temporary `/tmp` copies for unknown-kind, missing-kind, and duplicate-place probes; these did not alter repository files.

## Findings

- **Pair differs only in second `place_id`: confirmed.** `r17-valid-places` and `r17-wrong-after` have equal timeline rows except event 1's `place_id` (`tower` versus `mira`). Its ID, actor, tick, dependencies, description, source ID, event order, and all other fixture files match. Output changes from the expected harbor/tower `double-booked` finding to `not a place 'mira'` only.
- **Wrong-kind order controls: confirmed.** Wrong-kind-first (`wrong-before`, `wrong-first`), middle, and last each retain `not a place`; the known `harbor`/`tower` pair still reports a collision in first/middle/last three-row schedules. The two-event wrong-before control does not report a collision. The controls support these tested orders, not every possible schedule.
- **All 39 saved outputs: exact replay match.** Current output exit code, stdout, and stderr matched the saved transcript for all 39 fixtures. This includes the six round-17 cases, prior r16 missing-place controls, and the earlier 33 fixtures.
- **Unique unknown-kind probe:** changed the complete character entity's kind to `unlisted-kind` in a temporary copy of `r17-wrong-after`. It reports `unknown kind`, retains `not a place 'mira'`, and does not report double-booking. Thus the nonempty unknown-kind row is indexed, diagnosed, and excluded from occupancy as the declared guard implies. This does not make unknown kinds valid.
- **Missing-kind probe:** removing the kind field excludes that entity row from required-field-screened indexing. It reports required-kind and dangling findings (including for timeline IDs), and no collision. This is a malformed-row/dangling path, not the unique indexed wrong-kind case.
- **Residual duplicate behavior:** duplicate place ID `tower` in a temporary copy still emits `ambiguous place entity` and `double-booked` against harbor. The unique-non-place fix intentionally does not solve duplicate/ambiguous place identity; the checker can still make an overconfident raw-ID comparison in that separate case. This is correctly disclosed in the round docs/LOG and must remain an explicit limitation.
- **Text and citation limits:** the fixture descriptions consistently call themselves fixture input and disclaim source-text location. `courier-log` is only a source ID here; these fixtures and outputs do not establish what that text says, actual location, canon, or whether a real conflict exists.

## Axis recommendation

- **Calibration: improved, narrowly.** For exactly one required-field-screened entity indexed under the timeline `place_id`, when its kind is not `place`, the checker now retains the kind finding but withholds that row from definite different-resolved-place occupancy comparison and storage. The positive valid-place control and three tested mixed orders preserve known harbor/tower collision findings. Unique unknown kind follows the same exclusion while retaining its schema error.
- **Depth: unchanged.** No additional lore/canon facts or source-text evidence are established.
- **Coverage: unchanged.** This is a narrow calibration adjustment, not a new rule class. Duplicate/ambiguous place IDs remain a separate uncovered limitation.
- **Harmed axes: none found within the declared scope.** Regression replay is exact; the known residual duplicate case is not newly introduced or disguised and is explicitly outside scope.

**Recommendation: admit this single calibration move, narrowly**, subject to the stated one-row-kind scope and explicit duplicate-ID limitation. Do not generalize the result to source truth, all event orders, or all ambiguous IDs.
