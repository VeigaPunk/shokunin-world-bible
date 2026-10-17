# F10 — c2-frozen (r94 FOLLOW-UP verification seat)

Role: independent verification of the C2 frozen snapshot replay at
`.ufo/waves/round-94/frozen/map-obligations-r93`, including independent SHA-256
recomputation against the r93 pinned revision.

Scope of this seat: run the `--frozen` replay, recompute the frozen copies' digests
independently, and confirm they match the r93 live files at the pinned revision.
This is a verification of the snapshot/pin mechanism and the pinned verdict's
truthfulness; it is not a review of the C2 tool's design, of C1, or of r94 admission.

## E1 — Frozen replay: PASS, exit 0, four digests verified

Command (from repo root):

```
python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93
```

Observed output (verbatim, rerun twice with identical results; stderr empty, 0 bytes):

```
SNAPSHOT inputs=4 digests=verified
OBLIGATIONS raw=12 mapped=12
FROZEN expected=PASS/0 findings=none matched
RESULT PASS
EXIT=0
```

This matches the seat's expected outcome exactly: four digests verified,
`expected=PASS/0 findings=none matched`, exit 0.

Note on what the `SNAPSHOT ... digests=verified` line proves: it is emitted only
after `verify_frozen_inputs` has compared all four SHA-256 digests
(`corpus/tools/map_obligations.py:385-401`, comparison at `:399`; print at `:417`),
so the line is a post-check assertion, not a pre-emptive claim.

## E2 — Independent SHA-256 recomputation (frozen vs pins vs live vs pinned revision)

The frozen directory holds exactly five files (`find` output, no symlinks anywhere
under `frozen/`: `find .ufo/waves/round-94/frozen -type l | wc -l` → `0`):

```
claim-excerpt-map.md  entities.json  expected.json  relations.json  timeline.json
```

`sha256sum .ufo/waves/round-94/frozen/map-obligations-r93/*` and an independent
Python digest comparison against `expected.json` (`inputs`, lines 3-8):

```
17f0e8123f26e4f7c534c01a6fe843fe0e8e1278858c0b0ce74623cb7291f7d6  claim-excerpt-map.md
19f75678dae1b59e6704d1be903a5cecf1b070dd44165e3047bc47efdb8e2d1d  entities.json
32b79cd4d02793ce4c1f600522fb3810ffdbbad173b5707975fe9197ebf6e46d  relations.json
69da079eb29104cf4da04942ec3df79155569aa61d64fec00cb4aa7ffe2417e2  timeline.json
MATCH claim-excerpt-map.md 17f0e8123f... 17f0e8123f...
MATCH entities.json 19f75678da... 19f75678da...
MATCH relations.json 32b79cd4d0... 32b79cd4d0...
MATCH timeline.json 69da079eb2... 69da079eb2...
```

Triple comparison of each of the four inputs —
`git show 9c2eea3:corpus/fixtures/r93-m2-kojiki-cluster/<file>` vs the live working
tree file vs the frozen copy:

```
entities.json        TRIPLE-MATCH
relations.json       TRIPLE-MATCH
timeline.json        TRIPLE-MATCH
claim-excerpt-map.md TRIPLE-MATCH
```

Repeated against the HEAD revision `abbc3e0:corpus/fixtures/r93-m2-kojiki-cluster/<file>`:
all four `MATCH` as well. So frozen copy = live file = `9c2eea3` blob = `abbc3e0` blob
for every input, with identical hex digests, e.g. entities
`19f75678dae1b59e6704d1be903a5cecf1b070dd44165e3047bc47efdb8e2d1d`.

Supporting facts:

- `git diff --stat 9c2eea3 abbc3e0 -- corpus/fixtures/r93-m2-kojiki-cluster/` → empty:
  the WORK round did not modify the r93 fixture (spec invariant "no existing fixture
  modified" holds for this fixture).
- `git ls-files .ufo/waves/round-94/frozen/` lists all five files; the only commit
  touching the path is `abbc3e0` (`git log --diff-filter=A` on `expected.json`), i.e.
  the snapshot is committed content, not an untracked working-tree copy.
- Only one r93 fixture directory exists (`corpus/fixtures/r93-m2-kojiki-cluster`), so
  there is no ambiguity about which live tree the snapshot claims to pin.

## E3 — Pinned verdict is truthful, checked without the tool

The frozen `expected.json` pins `exit_code: 0, result: "PASS", finding_ids: []`
(lines 9-13). To test that this pin is a real expectation rather than a rubber stamp,
I recounted the obligations and map rows with an independent script (no import of
`map_obligations.py`), reading the frozen bytes directly:

```
header cells: ['ID', 'JSON fact pointer and fields', 'In-world source ID', 'Excerpt path', 'R9 delivery mode', 'Exact anchor']
data row count: 12
raw obligations: 12 | mapped pointers: 12
missing: []
phantom: []
source-id mismatch: []
INDEPENDENT VERDICT: PASS
```

Independent count derivation: 5 entity `first_appearance` + 5 entity claims + 1
relation + 1 timeline record = 12 raw obligations, matching `OBLIGATIONS raw=12
mapped=12` and the pinned `PASS/0/[]`. The pin therefore describes the true result of
the frozen bytes.

## E4 — Frozen failure modes exercised (tool's own isolated controls)

`python3 corpus/tools/map_obligations.py --self-test` → exit 0, all 20 cases `SELF-TEST
PASS`, including the five frozen controls:

```
SELF-TEST PASS frozen_complete exit=0 findings=none
SELF-TEST PASS frozen_tampered exit=2 findings=['snapshot_tampered']
SELF-TEST PASS frozen_missing_digests exit=2 findings=['unpinned']
SELF-TEST PASS frozen_expected_failure exit=1 findings=['missing_obligation']
SELF-TEST PASS frozen_verdict_mismatch exit=2 findings=['frozen_verdict_mismatch']
RESULT PASS
```

The self-test creates and removes its own temporary directory under the repo root
(`tempfile.TemporaryDirectory(..., dir=ROOT)`); no repo files were written by me, and
`git status --porcelain` before and after showed no changes to tracked files.

I deliberately did **not** run `.ufo/waves/round-94/work/W02-frozen-demo.py`: it copies
the snapshot into a transient directory under `.ufo/waves/round-94/work/`, which is
outside this leaf's write scope. The equivalent end-to-end tamper evidence is covered
by `frozen_tampered` above (real CLI, real tampered copy, exit 2 `snapshot_tampered`).
The LOG.md claim that this demo exits 0 is a WORK-wave claim I did not independently
reproduce.

## Observations and limits

- Transient environmental observation (not a tool defect): during the follow-up run a
  `map-obligations-self-test-*/` directory briefly appeared at repo root in a
  `git status --porcelain` snapshot and had disappeared in the next check ~seconds
  later (`ls` → `No such file or directory`, no `map_obligations` process running).
  This is consistent with a concurrent follow-up seat running `--self-test` at that
  moment. Final `git status --porcelain` shows only the expected untracked
  `.ufo/waves/round-94/followup/` directory. Flagged so the integrator is not
  surprised by a transient untracked path in a parallel status probe.
- What this seat does **not** establish: that the map rows' excerpts entail their
  claims (the tool's own declared scope excludes entailment/fidelity/chronology/
  rights/permission/canon, `corpus/tools/map-obligations-contract.json:3`), nor
  anything about C1, nor r94 admission. `--frozen` also rejects snapshots outside the
  repository (`map_obligations.py:348`), which bounds the replay to in-repo content.
- One documentation cross-check: `LOG.md:2669` states the `--frozen` invocation "exits
  0 after verifying all four input digests and the committed literal expected PASS/0/[]
  record" — the observed run above matches that statement exactly.

## Bottom line

PASS — `--frozen` replays the r93 snapshot with exit 0, four digests verified and the
pinned `PASS/0/[]` verdict matched; the four frozen copies independently hash-match
both the live r93 fixture and its `9c2eea3`/`abbc3e0` blobs, and an independent
non-tool recount confirms the pinned verdict is truthful.
