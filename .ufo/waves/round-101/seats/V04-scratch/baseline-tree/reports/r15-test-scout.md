# Round 15 test scout — baseline replay and clause-review method

## Raw observations

- The round-15 declaration in `.shokunin/lore/LOG.md` sets the baseline at the active `r10-registry-witness` fixture and calls for a separate fictional follow-up micro-bible. It requests preservation of old fixtures/checker behavior, a clean CLI, and a non-author manual review. This report does not establish that the proposed fixture exists.
- I found **28** active fixture directories under `.shokunin/lore/corpus/fixtures/`, and **139** JSON inputs. I replayed every fixture from the repository root with `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>`.
- All 28 invocations completed. Their exit codes and stdout matched the saved per-fixture observations in `.shokunin/lore/corpus/live/runs/20261012T180109Z/` for **28/28** cases; stderr was empty. The fixture-specific outcomes were 6 exit 0 and 22 exit 1. This is replay evidence, not a judgment that each reported violation reflects defective lore. The saved outputs are records from the round-13 baseline; their expected relative-path form matters (an absolute fixture path changes the missing-file diagnostic), so replay used relative paths.
- Before replay, the sorted fixture JSON path/hash map had 139 entries and manifest SHA-256 `87ee35628b6d81c4a2291abfe21412b18e01ab3eabf529ba28562e55567ec8da` (canonical sorted JSON serialization of relative-path/hash map). Pre/post maps were equal. Checker SHA-256 before and after was `eaa2f1178c4571d8a911cb3d880068216614766d8f35922cb78d6584179dad80`.
- The active fixture corpus had no r15-named fixture directory at inspection. The replay tested the current 28 fixtures only, not the proposed new micro-bible or its prose.

## Manual new-clause review — recommendation, not performed

For the proposed fixture, have a non-author read the exact note and corresponding source/entity/timeline rows, then make a clause-level table with: source ID; verbatim excerpt span; timeline event ID and field; supported / unsupported / ambiguous. Review at least these claims separately: (1) Sella looks again at the retained carbon; (2) the location is Lantern Harbor; (3) the visible mark is blurred, blue, and oval; (4) Sella cannot identify its origin; (5) she does not attribute it to Mira or the Blue Seal. Check that note and event description align, and that none implies who made the mark, when it first appeared, seal contact, destination, motive, or corroboration. Do not interpret the existing “first bell” as a verified numeric tick.

Record the chosen follow-up source ID and event tick/dependency in the review. Confirm the event is strictly later than its dependency according to the fixture’s local tick convention, and that it resolves to unique entity, place, and source IDs. In particular, checker success establishes structural/reference consistency only; it does not validate prose entailment, source truth, canon truth, or game mechanics. Treat an invented note and matching row as internal traceability, not independent corroboration. Reject or narrow any unsupported/ambiguous clause rather than infer it from the Blue Seal motif.

If the fixture is added, repeat the same raw CLI replay over all old fixtures and compare each captured stdout/stderr/exit triple to this baseline; separately hash old JSON files and checker to test that they were untouched. Those are prospective checks, not evidence from this task.

## Scope

This scout changed no fixture, checker, shared document, or commit. It wrote only this report. The pre-existing LOG modification and other round-15 scout reports were not edited.
