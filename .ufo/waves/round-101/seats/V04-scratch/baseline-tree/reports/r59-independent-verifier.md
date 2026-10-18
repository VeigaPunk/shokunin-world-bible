# Round 59 independent verifier report

## Method and baseline

Pinned the comparison baseline to Git commit `7e93686877f7773f946ab89984dee920da8e0cf7` (r58 report baseline), extracted with `git archive` into `/tmp/lore-r58`. For each of the 95 baseline fixture directories, invoked the checker from each repository root with the same repo-root-relative argv (`python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<directory>`). Compared raw stdout bytes, stderr bytes, and exit status: **95/95 tuples identical**.

Compared baseline and working fixture corpora by repo-relative path and raw bytes. Baseline contains **474 JSON files** (538 fixture files total); all 474 remain byte-identical at the same paths. Current corpus adds only 20 JSON files: five each in `r59-duplicate-harbor-tower`, `r59-duplicate-tower-harbor`, `r59-nested-duplicate`, and `r59-unique-control`. The fixture checker and README are also modified; no pre-existing JSON changed. This is a preservation comparison, not a claim that the candidate fixtures existed at the pinned baseline.

## Candidate behavior (separate from preservation)

Copied each candidate directory into the extracted baseline tree, then ran the old and current checkers from their respective roots with the identical root-relative argv and candidate bytes. This tests the candidate inputs under matching path semantics; it does not treat a newly added fixture as pinned historical material.

| Candidate | r58 checker | Current checker |
|---|---|---|
| `r59-duplicate-harbor-tower` | exit 1; `VIOLATION: timeline[1]: double-booked 'mira' at tick 1 in timeline[0] ('harbor') and 'tower'` (1 violation) | exit 1; `VIOLATION: timeline.json: duplicate object member 'place_id'; cannot load JSON` (1 violation) |
| `r59-duplicate-tower-harbor` | exit 0; `CLEAN: schema, citations, relations, timeline; 0 violations` | exit 1; `VIOLATION: timeline.json: duplicate object member 'place_id'; cannot load JSON` (1 violation) |
| `r59-nested-duplicate` | exit 0; `CLEAN: schema, citations, relations, timeline; 0 violations` | exit 1; duplicate `source_id` in entities, then six dangling-reference violations; 7 total |
| `r59-unique-control` | exit 1; double-booking violation for Mira at tick 1 (1 violation) | exit 1; same double-booking violation (1 violation) |

Thus the swapped duplicate-member order changes the old checker decision: one ordering is reported as double-booked, the reverse ordering passes clean, while the current checker rejects both at JSON loading. The nested duplicate is likewise clean under old behavior but rejected under current behavior. The unique control remains rejected identically. The exact output above includes the violation text and count; stderr was empty for all these runs.

## Current regression controls

Ran the current checker on the five existing `r5-*` fixtures using repo-root-relative paths. Each exited 1 with its expected targeted message and no stderr: `r5-missing-file` (missing contradictions file, 1 violation); `r5-invalid-json` (JSON decode error in contradictions, 1); `r5-wrong-top-level` (contradictions expected array, 1); `r5-row-shape` (contradictions[0] expected object, 1); `r5-invalid-citation` (unknown source `absent-source`, 1). The four candidate directory outputs above also preserve their full cascaded diagnostics as emitted.

This is an independent runtime/corpus comparison only. It makes no source-authority or canon claim.
