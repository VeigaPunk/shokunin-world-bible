# Round 84 regression scout — pinned corpus and raw CLI baseline

## Pin and scope

Declared baseline: `596f70e417c794f6d09279ee26cf9a03dd17eea9`; `git rev-parse HEAD` matched. I extracted only `.shokunin/lore/corpus` from that commit with `git archive` to `/tmp/r84-regression-596f70e/`. The pre-existing worktree changes to `.shokunin/lore/LOG.md` and other Round 84 reports were left untouched. This is a baseline-only measurement: no Round 84 candidate was created or tested. No corpus, checker, configuration, or LOG edits; no commit, push, or merge.

## Corpus bytes

Compared every root-relative corpus file path and raw bytes from the pinned archive with the working tree:

- Pinned archive: **1,368 files**; worktree: **1,368 files**.
- Identical paths and bytes: **1,368/1,368**; changed, missing, or extra paths: **0**.
- Active checker SHA-256 at the pin: `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81`.
- Sorted root-relative path/content-hash manifest SHA-256 (rows `path NUL sha256(file bytes)`, newline-delimited): `1da9dd1c19ee11443440f5416eca921bd6ff65d45cb3193aa84eae2996fb71c9`.

## 133 root-relative raw CLI tuples

Enumerated all **133** fixture directories in the pinned corpus. For each directory, ran this command from both the extracted archive root and working-tree root:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture-directory>
```

Compared unnormalized `(exit status, stdout bytes, stderr bytes)` tuples: **133/133 exact matches**, **28 exit 0**, **105 exit 1**, zero mismatches. The serialized pinned tuple ledger SHA-256 is `32a100b732a29bcac5f4b08aa72ddfea1e0547a28d5748506dcf4ced1f6d9bc7`; ledger rows contain fixture name, exit code, stdout hex and stderr hex, JSON compact separators. No tuple was normalized or interpreted as a semantic verdict.

## What this does and does not establish

This verifies pinned corpus byte preservation and root-relative CLI replay parity only. Exit codes and diagnostics describe checker behavior on structured inputs; they do not establish that a rule is editorially or narratively correct. In particular, replay cannot authenticate authored fictional prose, prove source reliability or truth, settle fictional-world canon, establish rights or permission, or establish game mechanics. I make no claim about the Round 84 hypothesis or candidate quality.
