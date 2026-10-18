# Round 74 regression scout — pinned 132-tuple note-only replay plan

## Scope and baseline pin

The Round 74 declaration is `.shokunin/lore/LOG.md`, section “Round 74 — 2026-10-13T11:09:18.358433+00:00.” It pins delivered r73 at `fb63f9a33e3e4bcd886cdb7ab01540ab216fa5f9`; `git rev-parse HEAD` matched. The worktree had a pre-existing modification to `LOG.md`; I did not edit it. The r73 declaration/evidence and the reports `r73-replay-verifier.md`, `r73-regression-scout.md`, and `r73-reviewer.md` supply the inherited fixture, comparison boundaries, and prior replay procedure. I extracted the baseline corpus with `git archive` from the pinned commit to `/tmp/lore-r74-baseline` and used that archive for the baseline run.

The pinned `corpus/fixtures` has **132 fixture directories** and **744 files**. The pinned full corpus has **1,355 regular files**; sorted relative-path manifest SHA-256: `1d4fec19cb1dd8278b72ed80c032d9717d199e0f1f862e71ae5b096b8cc68be0`. Checker SHA-256: `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81`. The manifest digest is a locator/check, not the raw-byte equality test.

## Baseline replay captured

At the pinned archive root, each of the 132 fixture directories was run with the identical root-relative command and argv:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture-directory>
```

For every directory I captured `(exit status, stdout bytes, stderr bytes)` without normalization. The baseline has **27 exit-0** and **105 exit-1** results. The serialized ordered tuple capture is at `/tmp/lore-r74-baseline-tuples.json` (SHA-256 `d0d518fdf131ce534a20fff62fead40152f80b75535def468aa76ff015db3baa`). I ran the same invocations from the current repository root: **132/132 raw tuples match**, no mismatches; current checker bytes have the same hash. The pinned corpus and present working-tree corpus currently have the same **1,355 paths and bytes**, with no missing, added, or changed corpus paths. This is a before-change baseline only, not evidence about a future candidate.

## Intended replay after note-only change

The declaration proposes a new editorial decision-table note under `.shokunin/lore/corpus/knowledge/`, not a fixture/checker change. After that note is made, replay the exact 132 pinned directory names using the same command, cwd (repository root), and argv above; compare each candidate tuple against the archived capture, component by component and byte-for-byte. Require **132/132** matches, and report each mismatch rather than only aggregate pass/fail. Keep the new note outside the fixture denominator; do not add a fixture or alter any source/claim/checker/LOG as part of this note-only check.

Also compare the full current `.shokunin/lore/corpus` against the pinned archive by sorted relative paths and raw bytes: all baseline paths must remain present and identical, with only the declared new knowledge-note path added. Confirm the fixture directory/file manifest and checker bytes remain unchanged. A note-only addition should not affect checker outputs, but replay is still required; do not infer that merely from the file location. If more than the declared note differs, enumerate it and stop calling the change note-only until reconciled. This replay can verify repository artifacts and CLI observations only; it does not verify editorial usefulness, source attribution semantics, or factual claims.

## Relevant inherited material and limits

The delivered r73 comparison at `.shokunin/lore/corpus/fixtures/r73-jorin-slate-claim/editorial-comparison.md` cites separate Vela and Jorin excerpts/sources, quotes “KEEP THE EAST GATE CLEAR” and “KEEP THE EAST GATE OPEN,” and leaves shared slate/inscription, reading times, and source relationship unresolved. The Round 74 LOG proposal calls for a decision table that tracks those distinct pointers and frames three alternatives as questions, each with a discriminating evidence need and “not established” state. The r73 reviewer notes the checker establishes structural validity only; the comparison itself does not establish common object or occasion. Those constraints are relevant to editorial review, not regression-test evidence.

This is a plan plus an observed pinned baseline, not a candidate verification or axis verdict. The checker tests fixture structures/references, not a knowledge-note’s prose or editorial value. No source truth, canon, rights, or mechanics inference is made. I edited only this requested report; no corpus, LOG, checker, or other report was changed, and no commit/push/merge was made.
