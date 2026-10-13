# Round 27 regression-scout — baseline replay specification

## Baseline and scope

Round 27 identifies work baseline `afe5ed54dddec767fbb4615723e75bcd0e554518` and report baseline `bb4c6c971faeaed48c7dbdf57ceb90fcfc873a21`; acceptance is exact preservation of 76 prior fixture outcomes and 379 prior JSON paths (`.shokunin/lore/LOG.md`, Round 27 declaration). This checkout currently has 76 immediate fixture directories and 379 recursively discovered JSON files under `.shokunin/lore/corpus/fixtures/`; these counts are inventory, not proof that the current bytes match the baseline.

## Replay protocol

Use the baseline checker from the declared work commit, not the candidate checker as its own oracle. Confirm baseline fixture directory/path inventory and bytes against that commit before replay. For every sorted pre-existing fixture directory invoke baseline and candidate checker separately and capture exact exit status, stdout bytes, and stderr bytes; require all 76 triples identical. Compare every sorted pre-existing JSON relative path byte-for-byte; require 379/379 unchanged. Exclude only newly introduced r27 fixture files from the historical comparison. Record command, commit, inventory counts, and per-fixture differences (if any) in the independent verifier report. If the baseline corpus cannot be established, report a blocker rather than claiming regression success.

## Behavior and risks

The checker iterates both relation endpoints in one loop (`.shokunin/lore/corpus/fixtures/check_bible.py:123-130`), independently tests membership and duplicate admitted-ID counts (`:118-129`), and indexes admitted entities (`:45-58`). Thus a relation whose `from` and `to` IDs are each duplicated should produce endpoint-local findings for each; this code reading predicts behavior but is not replay evidence. Risks: a test may conflate two diagnostics with relationship truth, infer canon or real-world referent resolution, or miss that duplicate-ID diagnostics are separate from endpoint ambiguity. Exact replay protects prior behavior; byte comparison protects historical fixture inputs.

## Focused proposed test

Use the declared matched control and both-duplicated case: preserve the same `mira -> seal` relation, citation, and shared tables, with the control duplicating only admitted `seal`, and the case duplicating admitted `mira` as well. Independently run both cases. Expected: control retains duplicate-ID findings and only `relations[0].to` ambiguity; both-duplicate case retains duplicate-ID findings and exactly one `relations[0].from` and one `relations[0].to` ambiguity. Check that all shared JSON tables are byte-identical and only the intended admitted entity addition distinguishes the pair. This tests diagnostic coverage only; it does not establish whether the cited relation is true or resolve canon.

## Evidence locations

- Round 27 baseline revisions, 76/379 regression condition, and paired-case expectations: `.shokunin/lore/LOG.md` Round 27 declaration (search heading `Round 27 — 2026-10-13`).
- Endpoint loop and endpoint-specific ambiguity checks: `.shokunin/lore/corpus/fixtures/check_bible.py:123-130`.
- Distinct admitted entity-ID counting: `.shokunin/lore/corpus/fixtures/check_bible.py:118-122`.
- Entity indexing and duplicate-ID diagnostic: `.shokunin/lore/corpus/fixtures/check_bible.py:45-58`.
