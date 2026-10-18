# Round 74 independent verification

## Scope and method

Pinned baseline: `fb63f9a33e3e4bcd886cdb7ab01540ab216fa5f9`. I created an external archive at `/tmp/lore-r74-pinned-fb63f9a33e3e4bcd886cdb7ab01540ab216fa5f9` using `git archive` and compared every file under the pinned and current `.shokunin/lore/corpus` trees by relative path and raw bytes. I also replayed every fixture directory present in the pinned corpus against the pinned checker and current checker, invoking each from its own archive/repository root with the same relative paths and comparing `(exit status, stdout bytes, stderr bytes)`. No source/canon/rights/mechanics judgment is in scope.

## Full old-corpus comparison

- Pinned corpus: **1,355 files**; current corpus: **1,356 files**.
- Removed pinned paths: **0**. Changed pinned-file bytes: **0**.
- Added current corpus path: exactly `.shokunin/lore/corpus/knowledge/r74-slate-wording-decision-table.md`.
- Thus the candidate corpus change is note-only; no old fixture, checker, source row, README, or other corpus file changed. This does not describe the separate round reports and LOG outside the corpus.

## Raw replay

The pinned corpus contains **132** fixture directories. All **132/132** old invocations matched exactly on exit status, raw stdout, and raw stderr. There were **27** exit-0 and **105** exit-1 outcomes, with zero tuple mismatches. I used relative fixture paths from both roots so path-specific missing-file diagnostics did not create artificial differences. This verifies those supplied old fixtures only; it is not exhaustive testing of arbitrary inputs or a semantic checker assessment.

## Candidate citations and wording

All note paths resolve in the delivered tree:

- Vela excerpt: `.shokunin/lore/corpus/fixtures/r72-vela-slate-claim/vela-slate-note-excerpt.md`; entity claim pointer `entities.json` `/6/claims/1`, source pointer `sources.json` `/6` (`vela-slate-note`). The claim says Vela reports reading “KEEP THE EAST GATE CLEAR” and tentatively inferring haste; the source row labels the account fictional and unverified.
- Jorin excerpt: `.shokunin/lore/corpus/fixtures/r73-jorin-slate-claim/jorin-slate-note-excerpt.md`; entity claim pointer `entities.json` `/7/claims/1`, source pointer `sources.json` `/7` (`jorin-slate-note`). The claim says Jorin reports being sent to copy a notice, reading “KEEP THE EAST GATE OPEN,” and not seeing who placed it; its source row labels the account fictional and unverified.
- The full literal excerpt strings in the note match the respective excerpt files byte-for-byte after removing only the files' final line break. Both excerpt files also match their cited claim wording in substance; no excerpt, claim, source-ID, or pointer mismatch found.
- `.shokunin/lore/corpus/fixtures/r73-jorin-slate-claim/editorial-comparison.md` exists and explicitly leaves same slate/inscription, reading times, and source relationship unresolved; it says neither account establishes a change or direct contradiction. Both referenced clause maps exist.

The note labels its three cases nonexclusive conditional possibilities, says no evidence is claimed to exist, frames each as evidence to seek, and includes residual limits. I found no assertion that a proposed identifier, observation, image, transcription, or other requested evidence presently exists. The evidence requests are hypothetical discriminators, not proof. The note does not select canon, assert common object/occasion, date a reading, establish a change, or decide report accuracy.

## Independent-verifier conclusion and limits

The pinned archive, full corpus raw-byte/path comparison, 132-fixture replay, literal excerpts, source/claim pointers, and r73 comparison support the bounded integrity statements above. I found no old-corpus regression and no invented extant-artifact assertion in the candidate note. This verifies factual alignment and scope discipline; it does **not** decide whether the new table materially improves editorial depth versus restating r73, whether its evidence tests are useful or sufficiently distinct, or whether the round should be admitted. The requested round-axis reviewer/adjudicator must make that determination. No source truth, canon, real-world rights, or game mechanics conclusion is offered.
