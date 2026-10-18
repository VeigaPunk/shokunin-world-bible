# Round 76 regression scout — pinned 132-tuple baseline and candidate replay plan

## Scope and pin

Report-only regression inventory for the active r76 depth hypothesis. I read the r76 LOG declaration, the delivered r73 Jorin excerpt/source/claim and maps, r74 note/review precedent, and r72/r73/r74/r75 regression reports. Baseline is pinned commit `edf3060033331c403f00e6d29b8e78e3f91c2e61` (`git rev-parse HEAD`); the worktree has a pre-existing `LOG.md` modification, which I did not touch. I archived `.shokunin/lore/corpus` directly from that commit to `/tmp/lore-r76-baseline/.shokunin/lore/corpus` with `git archive`.

The archive has **132 fixture directories**, **744 fixture files**, and **1,356 regular files** across the full corpus. The archived checker SHA-256 is `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81`. I compared archived and current working-tree corpus relative paths and raw-file hashes: **1,356/1,356 identical**, no missing, added, or changed paths. This is pre-candidate preservation only.

## Baseline raw CLI tuples

For each of the 132 archived fixture directories, I ran from `/tmp/lore-r76-baseline` with the same root-relative command and argv:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture-directory>
```

I captured `(process exit status, stdout bytes, stderr bytes)` without normalization. Baseline: **27 exit 0, 105 exit 1**. The ordered fixture-keyed tuples, with streams encoded losslessly as hex, are saved outside the repository at `/tmp/lore-r76-baseline-tuples.json` (SHA-256 `2cc36c7b85a54a95484e98876f9eeb8f116adb2345e65604bf371cd6eb857a66`). This is the pinned baseline, not a candidate comparison.

## Candidate replay plan (not performed)

No r76 candidate fixture exists in this scope; therefore there is no post-candidate replay or candidate verdict. If a candidate is produced, preserve this archive and tuple capture. For each of the same 132 directory names, invoke the pinned baseline checker and candidate checker on the same archived fixture path, from the same cwd, with identical argv; compare exit status and stdout/stderr bytes component-by-component. Require 132/132 exact old-tuple matches and enumerate any mismatch. Run the new `r76-gate-copy-request` fixture separately; do not add it to the old denominator. Compare pinned and candidate full corpus manifests and raw bytes, listing every addition/removal/change; check inherited clone files explicitly. For the declared additive clone, preserve all inherited tables and only permit the declared new source/claim and prose additions. Record the candidate checker hash; a changed checker invalidates treating this as fixture-only replay. Do not edit the corpus as part of this report.

## Attribution and evidence limits

R73’s newly authored fictional excerpt says, “I was sent to copy a gate notice. At the east steps, I read ‘KEEP THE EAST GATE OPEN’ on a slate. I did not see who put it there.” Its claim at `entities.json` `/7/claims/1` cites `jorin-slate-note` (`sources.json` `/7`). This is fixture-local attribution for a fictional, unverified account. It does **not** establish that Jorin actually received the request, who sent it, that any registry request exists, or that anyone independently corroborated Jorin’s reported purpose. A separately authored fictional registry entry—even if separately attributed in a candidate—would be newly invented fictional attribution, **not authenticated independent corroboration** absent provenance/authentication. A new source ID alone does not establish independence. Do not present such a record as an authoritative or independent witness to Jorin’s account.

R74’s editorial note/review demonstrates a bounded way to ask what evidence could distinguish hypotheses, not evidence that such evidence exists. R72/r73 precedent keeps reported perspectives separate and does not license shared occasion/object inference. The checker and tuple replay validate structure/CLI behavior only: they do not establish semantic support, source authenticity, provenance, evidentiary independence, or material depth. None of this establishes source truth, canon, rights, or game mechanics.

## GO / NO-GO

**GO** for the pinned baseline inventory and the specified post-candidate regression procedure. **NO-GO to claim candidate replay, depth improvement, or corroboration from this report:** no candidate has been replayed, and a newly authored fictional attribution is not independent authenticated corroboration. Regression preservation alone cannot establish the hypothesis’s materiality or justify admission. Limits: evidence is confined to the shipped 132 fixture invocations and archived corpus at the named pin; it says nothing about other inputs or factual status of fictional events.

I edited only this report. No corpus/LOG/checker edits, commits, push, or merge.
