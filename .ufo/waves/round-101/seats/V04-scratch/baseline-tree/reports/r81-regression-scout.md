# Round 81 regression scout — pinned corpus and raw CLI baseline

## Pin and scope

Report-only baseline audit for Round 81. The declared pin is `c683e507469a4edef4407bb7467d2715b94221b7`; `git rev-parse HEAD` matched this hash during the audit. I archived only `.shokunin/lore/corpus` from that commit with `git archive` and extracted it to `/tmp/lore-r81-c683e50/`. This is baseline-only: no candidate was replayed or evaluated.

The worktree already had a modification to `.shokunin/lore/LOG.md`; I did not change it. The raw archive and replay outputs are outside the repository. I made no corpus, checker, or LOG edits.

## Corpus path and byte comparison

Compared every corpus file by root-relative path and raw bytes between the pinned archive and current worktree:

- Pinned corpus files: **1,356**; worktree corpus files: **1,356**.
- Same path and byte-identical: **1,356/1,356**.
- Missing, changed, or additional paths: **0**.
- Checker SHA-256 at both pin and worktree: `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81`.
- SHA-256 of a sorted path/content-hash manifest for the pinned archive: `d94c6c3a1cd6f24b60dc231646dc63ff923d5bd1e3e1b55b2ee7b01b9ad3bbf4`.

## 132 root-relative checker tuples

Enumerated the 132 fixture directories in the pinned corpus and invoked each checker from both the archive root and working-tree root with the identical root-relative command and arguments:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture-directory>
```

Compared unnormalized `(exit status, stdout bytes, stderr bytes)` tuples. Result: **132/132 exact matches**, with **27 exit 0** and **105 exit 1** in the pinned run; no mismatches. The pinned raw tuple data is stored outside the repository at `/tmp/lore-r81-c683e50-tuples.json` (SHA-256 `03566593ccae06b2f6c8687edf6642d5712afe6088e7126855ee0b3ac5123859`). Replay script: `/tmp/lore_r81_replay.py`.

## Limits

This establishes path/byte parity and the pinned checker's present root-relative CLI behavior for these fixtures. It does not establish that exit-1 results are intended, that checker rules are semantically correct, or that any candidate improves an editorial axis. No candidate was tested. Structural checker output does not establish source authenticity, prose truth, fictional-world truth or canon; this report makes no rights or game-mechanics finding.

I did not commit, push, merge, change Git configuration, or modify the LOG, corpus, or checker.
