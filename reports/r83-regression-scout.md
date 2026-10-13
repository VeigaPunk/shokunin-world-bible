# Round 83 regression scout — pinned corpus and raw CLI baseline

## Pin and scope

Declared baseline pin: `e9324f6e4657ad2cdddbe3f38e4749d51cc30cb1`; `git rev-parse HEAD` matched. I used `git archive` to extract only `.shokunin/lore/corpus` to `/tmp/r83-regression-e9324f6/`. The pre-existing worktree modification to `.shokunin/lore/LOG.md` was left untouched. This is baseline-only: no Round 83 candidate was created or tested. No checker, corpus, configuration, or LOG edits; no commit, push, or merge.

## Corpus bytes

Compared every root-relative corpus path and raw file bytes from the pinned archive with the working tree:

- Pinned archive: **1,356 files**; worktree: **1,356 files**.
- Identical paths and bytes: **1,356/1,356**; changed, missing, or extra paths: **0**.
- Checker SHA-256 at the pin: `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81`.
- Sorted root-relative path/content-hash manifest SHA-256 (manifest rows are `path NUL sha256(file bytes)`, newline-delimited): `fae9bd1a5972cf3d54addbb827f3f71bd1400e0c4c810ed0f353bd8392399a59`.

## 132 root-relative raw CLI tuples

Enumerated all **132** fixture directories from the archive. For each, ran the same command, once from the archive root and once from the working-tree root:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture-directory>
```

Compared unnormalized `(exit status, stdout bytes, stderr bytes)` tuples: **132/132 exact matches**, **27 exit 0**, **105 exit 1**, zero mismatches. No tuple was normalized or interpreted as a semantic verdict. SHA-256 of the serialized pinned tuple ledger (fixture name, exit code, stdout hex and stderr hex, JSON compact separators): `bdd1ed6253070e583b3631fd52d9af71ae6a05f85b83ea60474d707f442f8f7e`.

## What this does and does not establish

This verifies baseline byte preservation and root-relative CLI replay parity only. Exit codes describe the checker’s structural behavior, not whether its rule is editorially or narratively correct. In particular, replaying a structured fixture cannot authenticate authored fictional prose, prove source reliability or truth, settle fictional-world canon, or establish any real-world rights/permission. Nor does it establish game mechanics. I make no claim about Round 83 candidate quality or about the proposed negation reading.
