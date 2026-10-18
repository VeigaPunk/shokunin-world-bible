# Round 75 regression scout — pinned old-input baseline

## Scope and disposition

This report is scoped **only to the active Round 75 coverage hypothesis**: an exact repeated directed `(from,to,type,source_id)` relation-row diagnostic. A concurrent withdrawn r75 depth declaration is out of scope; it is not a candidate, and this report proposes no registry entry. Regression inventory only. I read the active coverage declaration, `corpus/fixtures/check_bible.py`, fixture README, and relevant predecessor material: r2 duplicate-relation/alliance reports, r7 duplicate-source policy, r8 repeated dependency-list policy, r45 calibration rejection, and r59 duplicate-object-member adjudication. I made no corpus/checker/README/LOG edits and did not run a candidate. **Baseline is established; no post-candidate comparison exists yet.** Regression preservation alone would not establish the proposed coverage gain's materiality or admission.

**Pinned baseline:** `58edd17eb080fc707e959bf3dfc56d01afa54234` (Round 75 declared HEAD). Archived its `.shokunin/lore/corpus` via `git archive` outside the repository at `/tmp/lore-r75-corpus-baseline-*/.shokunin/lore/corpus` (fixture-only working copy also at `/tmp/r75-baseline-*/.shokunin/lore/corpus/fixtures`). The archive is a baseline artifact, not a candidate snapshot.

## Old fixture baseline

- 132 immediate fixture directories and 744 fixture files under `corpus/fixtures/`, including intentionally malformed/incomplete cases.
- Replayed all 132 archived fixtures with the archived baseline checker: **27 exit 0, 105 exit 1**.
- Replayed the same archived fixture tree with the current-checkout checker and compared raw `(exit code, stdout, stderr)` tuples: **132/132 byte-identical**. Using one shared fixture path avoids false stdout differences from absolute missing-file paths.
- The 132 current fixture directories and 744 files have the same relative paths and SHA-256 bytes as the pinned archive: **744/744 identical**. No removed, added, or changed fixture file.
- Full pinned corpus snapshot has 1,356 files; current corpus has the same 1,356 paths and bytes, **0 added/removed/changed**. This is pre-candidate corpus preservation, not a comparison against a future candidate.
- Exact full relation tuple `(from,to,type,source_id)` repeats: **0 among the 132 archived fixtures**. This absence does not prove such a row is invalid or useful to reject.

## Candidate comparison plan (not performed)

If a candidate is produced, first pin/archive its exact checker and corpus separately. Compare its fixture tree to the pinned archive using relative file paths and raw bytes, and report added/removed/changed paths separately; do not count the intended new matched fixtures as old-corpus regressions. Run baseline checker and candidate checker against the *same archived 132-fixture tree path*, capturing raw exit code, stdout bytes, and stderr bytes for every case. Report the per-fixture diff and totals; preserve the distinction between an intended new diagnostic and any changed old tuple. Then run the candidate's new duplicate-vs-controls and compare those raw results to baseline behavior. A clean fixture alone is not proof of semantic validity. Keep artifacts outside the repo; report paths/hashes and limitations. Do not alter existing fixtures to manufacture a baseline.

## Regression/context limits and evidence boundary

The active checker validates relation shape, endpoint identity and citation-ID membership, plus the scoped r2 reciprocal `allied_with` convention; it has no general exact repeated-relation-row check. The README and r7 policy distinguish input identifier resolution from source-text support. R2's reciprocal rule is not general deduplication; r8's repeated dependency list is a different structure; r59's duplicate JSON object-member rule has a consequential ordering probe and is not evidence that identical relation array rows are invalid. R45 is a useful calibration warning against inferring semantics from structural labels.

An exact repeated directed four-field relation is a **structural duplicate** (same values repeated in an array), and a later-index diagnostic can localize it. It does not establish that the cited source text is duplicated, that separate mentions or independent attestations do not exist, that the relation is false/redundant, or that there is one unique in-world relationship. The current relation schema has no row identity, passage/claim locator, time/scope, or multiplicity rationale. A same-edge row with a different source ID and a reversed edge are structurally distinct; the source ID itself establishes neither independent evidence nor prose support. No result here establishes source truth, canon, real-world rights, or game mechanics.

The requested baseline replay is bounded to these shipped fixtures and this checker invocation. It does not assess unshipped inputs, consumer behavior, semantic validity, or all malformed-input combinations. The schema scout likewise notes that matched duplicate/different-source/reverse controls can establish diagnostic scope but cannot resolve whether repeated equal rows are allowed representations.

## GO / NO-GO

**GO** for the regression baseline and post-candidate test procedure for the coverage hypothesis. **NO-GO to infer coverage admission or endorse a checker violation from regression evidence alone.** Before any checker candidate is admitted, the owner must decide and state an input-level convention that exact repeated relation rows are invalid regardless of underlying independent mentions, or provide a representation that gives independently addressable assertions a distinct identity/evidence location and a clear duplicate key. Preserve distinct-source and reverse-edge controls; do not label the diagnostic a canon/source-truth finding. No candidate was reviewed, no post-candidate regression comparison was made, and this scout makes no admission decision. The withdrawn depth declaration and any registry-entry candidacy are explicitly out of scope.
