# V20-verdict-calibration — round-101 seat report (verifier, calibration verdict)

- lane: lore-shokunin; round 101; seat V20 (verdict-calibration); model zai-coding-plan/glm-5.3-flash-low; date 2026-10-18
- baseline: r100 closure `6f86bf2`; tree HEAD at seat start `ebec6bb` (r101 declaration commit, touches LOG.md only); wave tree uncommitted per round convention; no commits, no pushes, no network, no nested agents
- assignment: read the C1/C3 seats; own a repointed-edge demonstration; issue ONE calibration verdict with bounds
- writes: this report + declared scratch `.ufo/waves/round-101/seats/V20-scratch/` only; everything else read-only (all repo invocations were read-only `verify`/`--self-test`-in-scratch; no `--freeze` ever run by this seat)

## Snapshot identity

Delivered bytes as verified by this seat (recomputed, match V03/V05's recorded values):

```
60a78bc39440917202488e4f6366a26540aeb494a089e5793864c1a4992fe3bf  corpus/tools/dependency_freeze.py
b8fc63c3500d626df8d5c34b28327c10716610512a3c72ef56a19f3b46de36ca  corpus/tools/dependency-freeze-contract.json
```

My scratch mirrors hash identically (byte-faithful copies), so every scratch result below is evidence about exactly these delivered bytes. Contract delta vs HEAD: 3 hunks (`@@ -32,7 +32,7 @@` revision refresh `b5fe4729…`→`ebec6bb…`; `@@ -677,6 +677,139 @@` r100-docket-review pin; `@@ -806,6 +939,14 @@` the new `repointed_edge` expectation) — `git diff HEAD -- corpus/tools/dependency-freeze-contract.json | grep -c '^@@'` → `3`. Since `ebec6bb` touched only LOG.md, diff-vs-HEAD equals diff-vs-`6f86bf2` for the contract, agreeing with V01/V04's baseline-scoped diffs.

## Poll record (poll-wait protocol)

- 00:02 — `.ufo/waves/round-101/` existed; `seats/` absent (first `ls` exited 2). Tools README/SKILL/contract greps for `repoint` returned nothing (pre-delivery bytes). While waiting, built the scratch mirror and the demo (below); observed delivery landing live (contract gained the 8-pin list incl. `r100-docket-review` mid-session; `git status` went from clean to U1's four owned `M` files between two reads).
- 00:10 — `seats/` appeared; polls at 20 s interval. U1 report found at loop try 2 (~40 s): `U1-chain-eight.md`. C1/C3 seat reports: my first claim-seat poll used a `C1*/C3*` name pattern — wrong guess; the claim seats are named `V01-c1-*`… `V06-c1-code-review`. Corrected on inspection; bounded harness note, not a stall (reports were landing throughout: 5 → 21 reports across my polling window).
- Seats read for this verdict: `U1-chain-eight.md` (producer), `V01-c1-chain.md`, `V02-c1-discharge.md`, `V03-c1-repointed.md`, `V04-c1-selftest.md`, `V05-c1-negative.md` — the C1 (chain pin) and C3 (persisted case) evidence seats. No contradictions found among them or against my own runs. V02's recorded gap (producer report ABSENT at its 40-try budget; README/SKILL not yet in tree) was later discharged: U1 landed at 00:21 and the docs were in the tree at 00:20:06/00:20:30 per V01/V04 — recorded by V02 as a bounded escape, resolved by later evidence, not adjudicated by me.
- ENDGAME CONVENTION: report counts in my poll lines never included SELF (this report did not exist while polling).

## Own demonstration — repointed-edge class (mandated)

Setup (scratch only): per-scenario mirror roots, each containing copies of the delivered tool + contract and the r95 base fixture under its pinned name (the pin is name-bound; my first attempt used renamed fixture copies and correctly tripped `UNPINNED-FIXTURE` exit 2 — the guard working as designed, and incidentally confirming pin-name binding).

Baseline (untampered mirror):

```
$ python3 $S/demo/corpus/tools/dependency_freeze.py $S/demo/corpus/fixtures/r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
RESULT PASS
baseline exit=0
```

Repoint (the C3 class): `aftermath-missing-evin` (tick 11) `depends_on ['paired-crossing-decision']` (its correct predecessor, tick 10) → `['aru-ninth-bell']` (a different valid earlier event in the same fixture, tick 9 < 11). Pre-swap assertion `depends_on == ['paired-crossing-decision']` passed in the edit script. Ran twice for stability:

```
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
FINDING ADDITION-DETECTED: event aftermath-missing-evin gained depends_on ['aru-ninth-bell']
FINDING REDUCTION-DETECTED: event aftermath-missing-evin lost depends_on ['paired-crossing-decision']
RESULT FAIL
run1 exit=1 / run2 exit=1 ; diff of the two outputs → OUTPUTS-IDENTICAL
```

BOTH findings in a single run, exit 1, stable IDs across repeats — the persisted class, reproduced outside the self-test harness through my own mirror construction.

Class-boundary controls (same target event, same new edge id, isolation of the two components):

- drop-only (`depends_on: []`): `FINDING REDUCTION-DETECTED … lost depends_on ['paired-crossing-decision']`, `RESULT FAIL`, exit=1 — REDUCTION only.
- add-only (`['paired-crossing-decision', 'aru-ninth-bell']`): `FINDING ADDITION-DETECTED … gained depends_on ['aru-ninth-bell']`, `RESULT FAIL`, exit=1 — ADDITION only.

So the repoint case is exactly the conjunction of the two pre-existing single-finding classes, now pinned as one case; a repoint can no longer be green under any expectation set that only covered the components.

Delivered self-test replayed in my scratch mirror (copies of the delivered tool + contract + base; the mirror `ROOT` keeps tempdirs inside my scratch):

```
CASE repointed_edge: exit=1 expected=1 findings=['ADDITION-DETECTED', 'REDUCTION-DETECTED'] ok
SELF-TEST 19/19
RESULT PASS
self-test exit=0
```

All 19 `CASE … ok` lines observed; the 18 inherited case ids ran with unchanged exits and finding sets in the same replay — the 18→19 growth added a case without disturbing the inherited expectations.

Chain spot-check (read-only, delivered tree, repository root), one line per fixture: all eight `RESULT PASS` exit=0 — r88 `acf677a7…`, r94 `048b8ff3…`, r95 `97cffd7b…`, r96 `43911900…`, r97 `a28b9ea0…`, r98 `5ecf84e1…`, r99 `7fe7e3b0…`, r100 `77debadf5c0f6e2c27f18902f0710278eb4305c633ff73158df7082936325c19` — the seven inherited digests exactly the Round-99/Round-100 values (none re-frozen), r100 matching U1's freeze receipt. Contract `self_test.expected` parsed: 19 entries; `repointed_edge = {"exit": 1, "finding_ids": ["ADDITION-DETECTED", "REDUCTION-DETECTED"], "forbid_traceback": true}`.

## Cross-seat consistency (C1/C3 seats read)

- U1 (producer): PASS C1+C3, receipts quoted (freeze output, 8/8 digests, 3-hunk diff, 19/19, own independent scratch probe). Consistent with my recomputations on every overlap.
- V01-c1-chain: PASS; independently recomputed the r100 pin's ten per-file digests + aggregate and the semantic inventory; inherited pins byte-identical vs `6f86bf2`. Also flags the seat-brief typo `6f86bf6` (nonexistent hash) for `6f86bf2` — I confirm `6f86bf2` is the named baseline and `6f86bf6` does not resolve.
- V02-c1-discharge: PASS on the pin-liveness discharge (tick-16 edge drop → `REDUCTION-DETECTED` exit 1 on a scratch mirror of r100); recorded producer-report ABSENT at its poll budget and not-yet-landed docs — later resolved (U1 00:21; docs 00:20); recorded, not re-adjudicated here.
- V03-c1-repointed: PASS; the same class demonstrated on the r100 base (`clerk-review-first-passage` → `acknowledgment-aru-records`, tick 13 < 16), twice, byte-stable; fail-closed in BOTH directions (contract missing the case, or `FROZEN_CASES` missing the case, each → exit 2 `CONTRACT-INVALID`) — no silent-pass path if tool and contract disagree about the case set.
- V04-c1-selftest: PASS; baseline `SELF-TEST 18/18` established from `git show 6f86bf2:` before-picture; delivered 19/19; 18 inherited expectations byte-identical (3-hunk diff, sole removed line = the disclosed revision refresh); corpus hash-stable around its runs.
- V05-c1-negative: PASS; 75/75 battery cases × 2 runs, 14/14 documented finding IDs, zero undocumented; wrong-but-earlier direction tick-asserted on both r95 and r100 bases; freeze refusals write nothing.

## CALIBRATION VERDICT (one, with bounds)

**Calibration: IMPROVED — bounded.** The blind-spot decision table's "wrong-but-earlier dependency edge" row (demonstrated at r99 by V16 P8 as a one-time probe) is now persisted as self-test case `repointed_edge` (18→19) in the delivered gate with expectations in the contract, closing that row with regression protection rather than a single demonstration. The persisted case pins the exact conjunction class — one event's `depends_on` swapped from its correct predecessor to a different valid earlier event yields BOTH `REDUCTION-DETECTED` and `ADDITION-DETECTED` in a single run, exit 1 — which I reproduced independently (twice, byte-identical), with controls showing each component class alone fires only its own single finding, and the untampered base passing exit 0. The fail-closed semantics around the case set (exit 2 `CONTRACT-INVALID` if either side drops the case) is verified by V03 in both directions and is consistent with the tool source I read. No calibration regression witnessed: the 18 inherited cases ran green with unchanged expectations in my own replay, and the seven inherited digests reproduced their Round-99/Round-100 values in my own 8/8 run. Bounded claim: this is detector-output calibration on the delivered bytes (snapshot SHAs above); it is not a new dependency-semantics or chronology-truth claim, matching the delivered README/SKILL wording.

Bounds (explicit):

1. **Directionality is construction-borne, not finding-borne.** The exit-1 + {REDUCTION, ADDITION} pair is direction-agnostic (V05's disclosure: a wrong-but-later swap fires the same IDs; consistent with `compare()` in the source, which reports lost/gained sets without tick reasoning). What is persisted is "a repoint cannot pass silently"; "wrong-but-earlier" lives in the case's tick facts (9 < 10 < 11) and in V05's tick-asserted probes, not in a distinct finding ID. A future gate that wished to detect earlier-vs-later as such would need new finding surface; today's calibration does not claim it.
2. **My own runs exercised the r95 base only.** The r100-base variant of the class is covered by V03 (twice, stable) and V05 (tick-verified) — corroborated, not self-observed by this seat.
3. **The guarded `--freeze` writer path was not exercised by me** (integration-time, run-once per U1, respected by V01/V04/V05 too). C1's pin is verified through the delivered pin payload, the reproduced digests, and the 8/8 clean chain — not through a rerun of the freeze.
4. **Snapshot-scoped.** All claims pinned to tool `60a78bc3…` / contract `b8fc63c3…`; bytes could in principle change after my window (none observed: hashes at first and last read identical).
5. **Adjacent gates out of scope.** `map_obligations.py`, `support_check.py`, `boundary_doc_check.py` untouched and unexercised by this seat (operability/boundary are other seats' axes; their unmodified state is witnessed via `git status` = exactly U1's four owned `M` files, agreeing with U1/V01/V04/V05).
6. **C2 witnessed only.** U2's `corpus/knowledge/r101-r10-register-first-entry.md` exists (untracked, per `git status` and the seats-dir listing); its depth claim belongs to the depth verdict seat, not here.
7. **Poll-harness note.** My initial claim-seat poll used a `C1*/C3*` filename pattern that cannot match this round's seat naming (`V01-c1-*` etc.); corrected after inspection. Recorded as a bounded harness error; no seat was judged ABSENT on its basis.

Writes by this seat: this report and `V20-scratch/` (demo mirrors, run outputs `repoint-run1/2.txt`). No delivered byte written; no `--freeze`; no commit; no network.

## Bottom line

PASS — calibration improved (bounded): the repointed-edge class is persisted as `dependency_freeze` self-test case 19/19 with contract-pinned expectations, independently reproduced by this seat (REDUCTION-DETECTED + ADDITION-DETECTED in one run, exit 1, twice byte-identical) with drop-only/add-only controls pinning the class boundary and a green baseline; chain verifies 8/8 clean with inherited digests unchanged; C1/C3 seat reports (U1, V01–V05) read and consistent with my own evidence, no contradictions; bounds as listed, chief among them that earlier-vs-later directionality is carried by case construction, not by a distinct finding ID.
