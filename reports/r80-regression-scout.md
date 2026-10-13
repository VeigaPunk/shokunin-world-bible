# Round 80 regression scout — pinned corpus and raw CLI replay

## Scope and pin

Report-only regression audit for Round 80. I read its pre-dispatch declaration in `.shokunin/lore/LOG.md`, plus the relevant r77 prior-art, critic, reviewer, verifier, and final-adjudication reports; the r79 declaration, independent verifier, reviewer, and final adjudication; and the r73 final adjudication and cited fixture context. The Round 80 declaration tests one depth hypothesis only: whether a two-beat attributed account (action plus separately described response/consequence) supports a useful scene-presentation choice beyond repeating the invented speaker’s own preference. R77 rejected generic latch texture as materially insufficient; r79 rejected a concrete ordering choice whose rationale was co-invented in the same passage. R73’s narrow admitted gain was the comparison of two separately attributed wording reports, not validation of either report as truth.

The declared baseline is clean report-last HEAD `e665e76abec8e88bd87c39f8cfe38877fedf43ed`; `git rev-parse HEAD` matched. The worktree already has a modification to `.shokunin/lore/LOG.md`; I did not alter it. I archived the pinned corpus with `git archive` to `/tmp/lore-r80-e665/.shokunin/lore/corpus`, outside the repository. No Round 80 candidate was present during this audit.

## Pinned corpus bytes

I compared the archived pin and working-tree corpus by relative path and raw bytes:

- Pinned files: **1,356**; current files: **1,356**.
- Pinned paths present and byte-identical: **1,356/1,356**.
- Missing, changed, or additional corpus paths: **0**.
- Pinned and current `fixtures/check_bible.py` SHA-256: `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81`.

## Reproduction of the 132 raw CLI tuples

Enumerated the 132 fixture directories in the pinned corpus and ran each from the archive root and from the checkout root with the same root-relative command and argv:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture-directory>
```

For each invocation I compared the unnormalized tuple `(exit status, stdout bytes, stderr bytes)`. Result: **132/132 exact matches**; pinned results comprise **27 exit 0** and **105 exit 1**, with no tuple mismatches. Lossless baseline tuple data was saved outside the repository at `/tmp/lore-r80-baseline-tuples.json` (SHA-256 `8bfa79494402348a561f2a4accaaa4e0015d684e8c06e9887c50c0019fdfb53e`). The reproduction script is `/tmp/lore_r80_replay.py`; neither file is a repository change.

This confirms the pinned corpus’s present bytes and the pinned checker’s present root-relative behavior. It does **not** test a Round 80 candidate, since none exists, and it does not establish that exit-1 fixtures represent desired behavior or that checker rules are semantically correct.

## Evidence boundaries

A future candidate should be replayed against this exact pin and compared by raw bytes/tuples; the old 132-fixture denominator must remain separate from any new fixture invocation. A CLEAN result, resolved citation ID, or unchanged replay can establish only the schema/citation checks the checker implements and regression parity. These do not determine whether prose faithfully supports its claim, whether the scene choice is useful, or whether a response is merely authored to justify the action. That is the declared non-author editorial test.

All new in-world assertions, if any, must remain attributed to explicitly fictional, unverified material. Structural pointers do not establish source authenticity, prose truth, fictional-world truth, or canon. This audit makes no finding about rights or game mechanics. I made no corpus, checker, or LOG edits and did not commit, push, or merge.
