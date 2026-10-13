# Round 82 regression scout — pinned baseline replay

## Scope

Baseline-only audit of the declared archive pin `7876a15fb4784e77e2a4062758d65bdafbacc8b7`. Archived `.shokunin/lore/corpus` with `git archive` to `/tmp/lore-r82-7876a15/`; raw archive and replay data remain outside the repository. No candidate was tested. I did not edit corpus, checker, config, or LOG, and did not commit, push, or merge. The pre-existing worktree modification to `.shokunin/lore/LOG.md` was left untouched.

## Corpus path and byte parity

Compared sorted root-relative corpus paths and raw bytes between the pinned archive and worktree:

- Pinned files: **1,356**; worktree files: **1,356**.
- Byte-identical same paths: **1,356/1,356**; changed, missing, or extra paths: **0**.
- Pinned checker SHA-256: `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81`.
- SHA-256 of sorted `path + space + file-SHA256 + newline` manifest: `6893c5f5a7cff5534a48833e503ffbdf1c4b76ac54e59d2b066c8f06fb22b0dc`.

## 132 raw root-relative CLI tuples

Enumerated all **132** fixture directories at the archive pin and ran each from the archive root and checkout root using the same command and root-relative argument:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture-directory>
```

Compared raw `(exit status, stdout bytes, stderr bytes)` tuples without normalization: **132/132 exact**, comprising **27 exit 0** and **105 exit 1**, with no mismatches. The pinned raw tuples are archived outside the repo at `/tmp/lore-r82-7876a15-tuples.json` (SHA-256 `c279637b4370cf8575bdbcc6c048fe8766594a13ee297cc912fb4b5f046d3578`). Archive/extraction and replay script files are also outside the repository (`/tmp/lore_r82_replay.py`, `/tmp/lore_r82_save.py`).

## Limits and attribution

This is a baseline preservation and CLI-behavior check, not candidate evaluation or an editorial-axis finding. Exit status and checker structure do not authenticate a source, establish that an attributed fictional account is true, settle fictional-world canon, establish real-world rights or permissions, or establish game mechanics. In particular, r35's Tarin excerpt is a fictional account reporting that Tarin saw Sella place an unlabeled envelope at the Lantern Harbor registry desk during the claimed Bell-7; Sella's separately authored fictional account says she was at North Tower throughout that same claimed ringing and not at Harbor. The map distinguishes Tarin's reported observation scene from a claim about Sella's own location. The fixture's shared Bell-7/date wording is not independent time authentication, and local `tick: 3` does not encode a clock or occasion. These are attributed story statements and explicit limitations, not facts verified by this replay.

Conditional requests for later, independently attributable evidence (such as unique occasion/person/place identification or source/capture provenance) are hypothetical editorial investigation steps only: no such evidence is shown to exist here, and finding it would not by itself authenticate either account, determine canon, establish rights, or establish mechanics. r36's eighth-day near-miss shows the date mismatch can withdraw support for treating the accounts as the same occasion; it does not decide truth or prove either account false. r74's evidence table concerns slate reports and is not itself evidence about Bell-7. No source authenticity, canon, rights, or mechanics finding is made.
