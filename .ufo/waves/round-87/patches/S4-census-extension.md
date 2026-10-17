# Round 87 inherited-census extension procedure (S4)

Axes: census accuracy, reproducibility, and preservation of prior observations.

## Canonical definition from round 86

The r86 diagnostic is an inherited-work measurement, not an admission result. Its baseline is commit `5eb9451baff217c19d5786405f9b2aa500b7c1b7`; it archives that commit's `corpus/` and runs the candidate checker from the candidate tree (`.ufo/rounds/r86/diagnose.py:14-16,39-57`).

There are two separate inventories:

- **Fixture tuples:** one run for every sorted immediate child directory of the baseline `corpus/fixtures/`. Each recorded tuple is `(returncode, stdout, stderr)`; the command is retained alongside it but is not part of tuple equality (`diagnose.py:26-34,52-57`).
- **Inherited JSON inputs:** every `*.json` recursively below the archived baseline `corpus/`, not just JSON in fixture directories. The diagnostic compares each such path with the candidate copy and reports missing or byte-different inputs (`diagnose.py:47-50`).

The r86 observation is 133 fixture runs, all 133 tuples equal, with baseline exits 28×0 and 105×1; it counted 705 inherited corpus JSON files and found no changed inherited JSON (`diagnostic.stdout.json:7-19`). `same_fixture_tuples` means candidate versus baseline tuple equality for these inputs; it is not a count of JSON files, individual records, probes, or new fixtures.

## Round 87 extension protocol

1. **Name fixture directories stably.** Use lowercase kebab case with an `r87-` prefix and a topic/case suffix, e.g. `r87-myth-cluster`. A single fixture directory is one census case regardless of its number of entities, relations, events, JSON tables, or Markdown notes. The census only enumerates immediate fixture subdirectories; nesting additional cases will not add census rows.
2. **Declare the expected exit before replay.** Keep the fixture contract separate from the observed result. A clean cluster required by C3 declares expected exit `0`; an intentionally negative fixture declares `1` and names its intended findings. For each new case, record its exact command, declared expected exit, observed return code, full stdout and stderr. Reject any exit mismatch, unexpected finding, missing expected finding, or stderr output. Do not infer the expected exit from the run itself.
3. **Append new cases; do not rewrite inherited evidence.** Treat the 133 original baseline tuple records as immutable. Preserve `.ufo/rounds/r86/diagnostic.stdout.json` unchanged (its pinned-copy SHA-256 is `471054be46458c3116201fa487b5c8fa343be0a18a203f5b8c8a44dbffa5e405`) and record r87 additions in a separate extension artifact. Include the prior artifact path/hash and append only new named cases there. Do not regenerate, reorder, normalize, or replace the old tuple records to make the extension fit a new output.
4. **Handle intended changes to old cases as explicit deltas.** Replay all inherited cases against the target checker. For every changed tuple, retain the old baseline tuple exactly and record a separate old→new tuple delta keyed by fixture name, including the exact new return code/stdout/stderr and the reason the output is allowed to change. For C1's disclosure additions, enumerate every affected existing fixture tuple; all unlisted tuples must remain equal. This preserves the inherited expected observations while making intentional checker changes auditable.
5. **Keep the JSON preservation check independent.** Recompute the inherited JSON set from the pinned baseline corpus and compare each inherited path's bytes with the candidate. The old-input changed/missing list must stay empty; list new JSON paths/counts separately. The 705-file number covers all corpus JSON, including 45 files outside `corpus/fixtures/` in the inspected copy. It must not be conflated with the fixture tuple count.
6. **Record the run and arithmetic.** For each new fixture, use the repository-root command form `python3 corpus/fixtures/check_bible.py corpus/fixtures/<fixture-name>` and capture its observed exit/stdout/stderr exactly. With one newly added directory and no removals, the census becomes `133 + 1 = 134` fixture runs. The JSON inventory becomes `705 + N`, where `N` is the count of newly added `*.json` files under `corpus/`; do not assume `N` from the number of entities or from Markdown files.

The existing r86 harness compares stdout/stderr as decoded text because it invokes `subprocess.run(..., text=True)` (`diagnose.py:26-34`). Therefore its equality check is exact on return code and captured text, not a raw-process-byte comparison. The stronger preservation rule above is achieved by keeping the original diagnostic artifact byte-for-byte intact and hash-checking it, while storing new observations separately.

## Application to the inspected round-87 base

The pinned copy at `28706dc` contains 133 immediate fixture directories and 705 corpus JSON files. It does not yet contain `corpus/fixtures/r87-myth-cluster/`; no checker replay or observed exit for that new fixture is claimed here. After that directory lands, run the command above, require exit 0 as specified by C3, record its actual stdout/stderr, and expect 134 total fixture directories/runs if no other fixture directories are added.