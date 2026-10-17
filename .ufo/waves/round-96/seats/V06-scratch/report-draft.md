# V06 — c1-negative-rerun (round-96) [DRAFT SKELETON — scratch only]

Seat V06, report path `.ufo/waves/round-96/seats/V06-c1-negative-rerun.md`.
Subject: `corpus/tools/map_obligations.py` at the delivered r96 revision
(sha256 TBD), baseline r95 tool sha
`d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108`.

## Poll record
- Target: Q1 tool revision + `.ufo/waves/round-96/seats/Q1-tool-code.md`.
- Poller `V06-scratch/poll-q1.sh`, 20 s cadence, 40 tries. Result: TBD.

## Method
- Base = byte copy of `corpus/fixtures/r93-m2-kojiki-cluster` (same subject as
  r94 F11 / r95 V04). Cases a–f replicate F11/V04 one-for-one; g/h/i add
  schema_drift, inventory deletion class, dual_pointer; ctrl-* are no-false-fire
  controls.
- Builder `V06-scratch/build-cases.py`; runner `V06-scratch/run-cases.sh`
  (each case twice, stdout+stderr+exit captured); comparator
  `V06-scratch/compare.py` (post-r96 expectation table from the C1 claim text).
- Baseline before-picture: `runs-baseline` under the r95 tool (sha d1c239cc…).

## Before picture (r95 tool, runs-baseline, both passes byte-identical)
TBD table (filled).

## After picture (r96 tool, runs-new)
TBD.

## Verdict
TBD.

**Bottom line: TBD.**
