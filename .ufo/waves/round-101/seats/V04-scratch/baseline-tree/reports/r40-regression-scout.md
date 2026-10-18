# Round 40 regression scout — pinned baseline replay plan

## Scope and pinned baseline

This is a plan for a non-author regression replay only; I did not run the checker or edit fixtures, checker, LOG, README, or commit. Round 40 declares baseline work commit `e2af8f2d88fee3cf12963318097523d8ab8f7856` and report commit `729e868b889e5d2ce2bf21dc139fe4a41655a95d` at `.shokunin/lore/LOG.md:657-660`. The declared inventory is 92 prior fixture CLI tuples and 459 prior JSON paths (`LOG.md:659`). Treat the pinned report tree—not the current checkout or historical totals—as the authority for the old path set. The proposal says no r40 fixture exists at baseline (`LOG.md:658`); verify directly against the pinned object.

Relevant precedent:

- Round 14 rejected a retelling/restatement rather than a genuinely distinct observation; its disposition says later depth work must add bounded detail/uncertainty, not textual backfill (`LOG.md:204-209`). Its test scout separates exact artifact identity from human prose mapping and warns that hashes/checker success cannot establish truth (`reports/r14-test-scout.md`, “Manual hash/correspondence verification design”).
- Round 23 defined a named speaker’s report that a named thing was not present as a bounded witnessed-absence class; the map was manual and checker success did not authenticate prose (`LOG.md:339-347`). This is precedent for explicitly limiting what was not seen, not evidence for Vela’s account.
- Round 35 required matching the two reports’ claimed unique occasion before treating them as a conditional conflict, while preserving attributed uncertainty and not selecting a winner (`LOG.md:562-570`). Its regression scout’s exact-stream/status and JSON-byte replay approach is applicable (`reports/r35-regression-scout.md`, “Proposed replay and baseline check”).

## Replay procedure

1. Archive or otherwise read the tree at report commit `729e868b889e5d2ce2bf21dc139fe4a41655a95d`. Enumerate sorted fixture directories and all JSON paths under the declared fixture scope; record the manifests and verify the stated counts of 92 and 459. Confirm `.shokunin/lore/corpus/fixtures/r40-*` is absent in that tree. If the pinned inventory disagrees, report the exact paths/counts; do not silently substitute current counts.
2. For each of the 92 baseline fixture paths, run the same repository-root argv against the pinned baseline and candidate checker/tree: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>`. Capture raw stdout bytes, raw stderr bytes, and exit status separately. Require exact per-path equality for all three; do not normalize output or equate matching exit status alone with replay success. Pin/check the checker file too, so the comparison does not accidentally use a different implementation on both sides.
3. Compare each of the 459 baseline JSON paths byte-for-byte against the candidate by relative path (hash manifests may summarize, but retain path-level results). The new r40 fixture is additional and excluded from the prior-path denominator. Record missing, added, or changed old paths explicitly.
4. Run the candidate’s new fixture with the same CLI and report its complete stdout/stderr/exit. Structural exit 0 is expected by the proposal, but it only indicates checker acceptance, not prose entailment, hearing source, objective bell origin, synchrony, or canon.
5. Keep this mechanical replay separate from manual correspondence review. The proposed Vela report is an attributed statement that she heard two strokes she took to be the registry bell and did not see Sella or an envelope (`LOG.md:659`). Review must not upgrade “took to be” into objective bell identification or the non-sighting clause into proof of anyone’s actual location/absence. The report is not independent evidence for Tarin’s placement or Sella’s Tower account; preserve their existing attributed reports and unresolved ledger unchanged as specified at `LOG.md:659`.

## Risks

- Count drift: 92/459 is a pinned claim, not portable to a different checkout. Commit/object selection, untracked files, or path-scope variation can invalidate an apparent match.
- Incomplete replay: comparing only stdout, only statuses, or saved summaries can miss stderr/status/path regressions. Compare raw streams and exit code per fixture using identical argv/cwd.
- Baseline contamination: edits to any inherited source, JSON, or checker can masquerade as a new fixture. Verify exact old JSON bytes and report all fixture path changes; do not fold r40 additions into the old denominator.
- Narrative overreach: the two-stroke observation is Vela’s perception/report. It does not establish that the registry bell objectively rang, that strokes occurred at an externally synchronized Bell-7 time, that Vela saw Sella or an envelope, or that Tarin/Sella’s other reports are true or false. Do not use the new account to settle their conflict or imply canon.
- Precedent/novelty: r14 warns that new phrasing or a new source row alone is not depth. Review the bounded auditory observation and explicit non-sighting as a distinct reported perspective, not corroboration/backfill; r23’s absence precedent does not make non-sighting proof of objective absence.

## Falsifiable regression check

The replay component passes only if the pinned baseline contains exactly the declared 92 fixture paths and 459 JSON paths, the new r40 path is absent there and present in the candidate, all 92 baseline CLI tuples match exactly in raw stdout, raw stderr, and exit status, and every one of the 459 old JSON paths is byte-identical. Any count/path mismatch, missing baseline case, stream/status mismatch, changed old JSON byte, or failure to report the new fixture’s actual result falsifies the check. Separately, the proposed structural expectation is falsified if the new fixture does not exit 0; a clean exit cannot pass or falsify the human claim that Vela reports only what she heard/perceived and did not see. No regression result validates source truth, bell origin, other reports, or canon.
