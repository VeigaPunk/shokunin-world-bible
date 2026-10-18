# Round 45 independent verifier report

## Baseline and method

Pinned baseline: `7ef761d639c18f3a09a61477956b234042a91ebf`. Extracted with `git archive` into an independent temporary root (`/tmp/lore-r45-baseline-g1hcaijr`); compared against the working lore root at that revision. This is a read-only verification except for this report.

Both roots contain 95 active immediate fixture directories and 474 JSON paths, with identical path sets and byte-identical JSON contents. The checker path is byte-identical. Fixture README is byte-identical. No active fixture directory with `r45` in its name exists in the current root.

## Reproduction

From each root, ran the same root-relative argv, with `python3`, for both commands:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/consistent
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/contradictions
```

Exact observations (raw stdout/stderr byte equality):

| Argument fixture | Baseline exit | Current exit | stdout equal | stderr equal |
|---|---:|---:|---|---|
| `consistent` | 0 | 0 | yes (60 bytes) | yes (0 bytes) |
| `contradictions` | 1 | 1 | yes (281 bytes) | yes (0 bytes) |

Thus the initial narrow replay finds no baseline/current checker-output difference for these two documented controls. It is not the full regression matrix; full 95-fixture replay is separately recorded below.

## Scope and interpretation

No checker, README, or active fixture JSON changes were found relative to the pinned baseline; no r45 fixture exists. Existing unrelated workspace changes/reports were not modified. Scout temporary faction-pair material or any checker result is not source truth and does not by itself establish a calibration bug. This verifier makes no claim about prose support, source authenticity, canon, or untested inputs.


## Full pinned fixture replay (follow-up)

Separately from the regression scout, enumerated all **95** immediate fixture directories in the archived baseline and ran, for every directory, the identical root-relative command from both roots:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture-directory>
```

Compared each raw `(exit status, stdout bytes, stderr bytes)` triple. **95/95 triples matched exactly; 0 differences.** Baseline and current exit distributions were 24 exit-0 and 71 exit-1 runs each. The full replay produced 14,270 total stdout bytes in the baseline and 0 stderr bytes; this is an aggregate, not a semantic pass/fail assessment. The same 95 baseline fixture names are present in current. This establishes exact replay equivalence only, not semantic validity or calibration.
