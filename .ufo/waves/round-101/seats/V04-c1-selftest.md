# V04-c1-selftest — round-101 seat report (verifier)

- lane: lore-shokunin; round 101; seat V04; model zai-coding-plan/glm-5.3-flash-low; date 2026-10-18
- target: U1 (`U1-chain-eight.md`); baseline `6f86bf2` (r100 closure); tree HEAD `ebec6bb` (declaration); no commits, no pushes, no network; only my report + `.ufo/waves/round-101/seats/V04-scratch/` written
- axes: (1) self-test 19/19 on delivered bytes; (2) 18 inherited case expectations byte-identical vs baseline; (3) corpus hash-stable around my runs

## Poll

Producer report absent at seat start; found at poll try 5 (~80 s of 20 s interval): `.ufo/waves/round-101/seats/U1-chain-eight.md`. Artifacts observed mid-flight (contract/script first caught between a clean `git status` at ~00:03 and my JSON dump at ~00:08 — U1 was writing live); all four owned files final by 00:20:30; `git status` at verification time: exactly `M` on `SKILL.md`, `corpus/tools/README.md`, `corpus/tools/dependency-freeze-contract.json`, `corpus/tools/dependency_freeze.py` plus untracked U2 file `corpus/knowledge/r101-r10-register-first-entry.md` (U2's, not my scope).

## Baseline establishment (pre-verification control)

`git show 6f86bf2:corpus/tools/dependency-freeze-contract.json` → 7 pins (`r88-m3-maya-cluster … r99-window-lapse`, no `r100-docket-review`), `self_test.expected` = 18 cases, `repointed_edge` absent. Baseline script + contract extracted to scratch; full baseline tree via `git archive 6f86bf2` into scratch; run there:

```
$ python3 corpus/tools/dependency_freeze.py --self-test   # in baseline tree
...
CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
SELF-TEST 18/18
RESULT PASS
EXIT=0
```

Note: an initial scan suggested the worktree contract (8 pins/19 cases) was committed at baseline; that was my misread of a live-edited worktree file against the commits. `git show 6f86bf2:` settles it — baseline is clean 7-pin/18-case. Also verified: pin `revision` values are git SHAs recording HEAD at pin-time (r99 pin → `b5fe472` = r100 declaration; r100 pin → `ebec6bb` = r101 declaration), so the r100 pin's `revision=ebec6bb…` follows the established convention, not an anomaly.

## Axis 1 — delivered self-test 19/19 PASS

```
$ python3 corpus/tools/dependency_freeze.py --self-test
CASE repointed_edge: exit=1 expected=1 findings=['ADDITION-DETECTED', 'REDUCTION-DETECTED'] ok
SELF-TEST 19/19
RESULT PASS
EXIT=0
```

19 `CASE … ok` lines counted (`grep -c "^CASE .* ok$"` → 19); exit 0; both findings in the single `repointed_edge` run as claimed; `forbid_traceback` expectation present in contract. Output preserved at `.ufo/waves/round-101/seats/V04-scratch/selftest-output.txt`.

## Axis 2 — 18 inherited expectations byte-identical

Parsed-JSON compare, baseline contract (scratch `baseline-contract.json`) vs delivered:

- cases: baseline 18, delivered 19; added `{repointed_edge}`, dropped `{}`, per-case canonical-JSON equality for all 18 inherited → changed: NONE; `base_fixture` `r95-crossing-aftermath` unchanged; delivered `repointed_edge` = `{exit:1, finding_ids:[ADDITION-DETECTED, REDUCTION-DETECTED], forbid_traceback:true}`.
- pins: baseline 7, delivered 8; added `{r100-docket-review}`, dropped `{}`, inherited pins changed: NONE.
- top-level: only `revision` refreshed `b5fe47295…` → `ebec6bbdeb1…` (the disclosed writer-managed refresh); every other top-level key unchanged.

Raw-byte proof stronger than the parse compare: `git diff 6f86bf2 -- corpus/tools/dependency-freeze-contract.json` has exactly 3 hunks and its only removed line is `-  "revision": "b5fe472957ab…",` — i.e. all inherited contract bytes are untouched; additions are the pin hunk and the case hunk. `git diff --stat 6f86bf2` on owned files: contract +143/−1, `dependency_freeze.py` +18, `README.md` +59, `SKILL.md` 7 lines — matching U1's disclosure.

## C1 support — eight-fixture chain verifies 8/8 clean (my runs)

`python3 corpus/tools/dependency_freeze.py corpus/fixtures/<name>` × 8, repository root — every one `RESULT PASS`, exit 0:

```
r88-m3-maya-cluster         DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
r94-paired-crossing         DIGEST 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef
r95-crossing-aftermath      DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
r96-crossing-response       DIGEST 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c
r97-crossing-acknowledgment DIGEST a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54
r98-clerk-filing            DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
r99-window-lapse            DIGEST 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e
r100-docket-review          DIGEST 77debadf5c0f6e2c27f18902f0710278eb4305c633ff73158df7082936325c19
```

All eight digests byte-match U1's quoted receipts; the seven inherited digests are the Round-99/Round-100 values (none re-frozen). I did **not** run `--freeze` (integration-time op; U1 flags it must not be rerun — respected).

## Axis 3 — corpus hash-stable around my runs

SHA-256 manifest over `corpus/` (1850 files, `__pycache__` excluded) before vs after my self-test + 8 fixture runs: identical (`diff` clean). Manifest vs session start differs in exactly two entries, both producer writes, neither mine: `corpus/tools/README.md` (U1's delivered rewrite) and added `corpus/knowledge/r101-r10-register-first-entry.md` (U2). Contract and script hashes unchanged from first post-edit capture to end.

## Docs spot-check (U1-owned, observed only)

`SKILL.md` freeze row now reads "19 cases (… r101 added `repointed_edge` …)", "exactly the eight chain fixtures, verifying 8/8 clean", "The seven inherited pins retain every field from r100 closure `6f86bf2`", plus a dated supersession bullet (2026-10-18, round 101). Baseline `6f86bf2` README contains zero "Round-101" text (`git show 6f86bf2:… | grep -c` → 0), so the README r101 addendum is delivered worktree bytes, not pre-committed baseline text.

## Bounds / not verified

- Guarded `--freeze` behavior itself (scope refusal on foreign paths) is exercised by the persisted `scope_refused` self-test case (passed above); I did not re-exercise the writer path, per U1's integration-time-only note.
- U2's C2 file present but outside my seat; not verified.
- Adversarial contract tamper re-detection (DIGEST/SELF-TEST-MISMATCH paths) is covered by the persisted cases, not independently re-probed beyond the self-test run.

## Bottom line

PASS — delivered `--self-test` 19/19 RESULT PASS exit 0 with `repointed_edge` = {ADDITION-DETECTED + REDUCTION-DETECTED, exit 1} in one run; the 18 inherited case expectations and 7 inherited pins raw-byte-identical vs `6f86bf2` (3-hunk diff, sole removal = disclosed revision refresh); chain verifies 8/8 clean with digests matching U1's receipts; corpus hash-stable across all my runs.
