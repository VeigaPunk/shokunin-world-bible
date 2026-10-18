# U1-chain-eight — round-101 seat report (producer)

- lane: lore-shokunin; round 101; seat U1; model zai-coding-plan/glm-5.3-flash-low; date 2026-10-18
- baseline: r100 closure `6f86bf2`; tree HEAD at seat start `ebec6bb` (round declaration); wave tree left uncommitted per round convention; no commits, no pushes, no network
- owned bytes written: `corpus/tools/dependency_freeze.py`, `corpus/tools/dependency-freeze-contract.json`, `corpus/tools/README.md`, `SKILL.md` (freeze row only). Declared scratch: `.ufo/waves/round-101/seats/U1-chain-eight-scratch/`. No other tracked file touched (`git status`: exactly these four `M`).

## Per-claim verdicts

- **C3 / calibration: PASS** — `repointed_edge` persisted, self-test 18→19, `SELF-TEST 19/19`, both findings in one run, exit 1.
- **C1 / coverage: PASS** — `r100-docket-review` pinned through the guarded `--freeze`; chain verifies 8/8 clean; contract diff vs `6f86bf2` = 3 hunks only (pin + case + writer-managed revision refresh); every inherited pin field-identical.
- **Collateral harm: none observed** — the 18 inherited case expectations are byte-identical; the 7 inherited digests reproduce their Round-99/Round-100 values exactly; `map_obligations.py`, `support_check.py`, `boundary_doc_check.py` untouched.

## C3 — persisted repointed-edge case (18→19)

Edit 1 — `corpus/tools/dependency_freeze.py`: appended `"repointed_edge"` to `FROZEN_CASES`; added the case body after `markdown_tamper` (isolated mirror of `r95-crossing-aftermath`; for `aftermath-missing-evin`, `depends_on` entry `paired-crossing-decision` replaced by `aru-ninth-bell`); Round-101 docstring paragraph. Edit 2 — contract `self_test.expected.repointed_edge = {exit: 1, finding_ids: [ADDITION-DETECTED, REDUCTION-DETECTED], forbid_traceback: true}` (direct edit; the only hand edit to contract bytes).

Hand derivation: frozen `aftermath-missing-evin` (tick 11) has `depends_on ["paired-crossing-decision"]` (tick 10, its correct predecessor). After the swap it has `["aru-ninth-bell"]` — a valid event pinned in the same fixture, tick 9 < 11, i.e. wrong-but-earlier. `compare()` sees lost `['paired-crossing-decision']` → `REDUCTION-DETECTED` and gained `['aru-ninth-bell']` → `ADDITION-DETECTED` on the same event in one run; no endpoint or relation change → `RESULT FAIL`, exit 1.

Command and observed output (delivered bytes, post-freeze):

```
$ python3 corpus/tools/dependency_freeze.py --self-test
...
CASE repointed_edge: exit=1 expected=1 findings=['ADDITION-DETECTED', 'REDUCTION-DETECTED'] ok
SELF-TEST 19/19
RESULT PASS
exit=0
```

All 19 `CASE … ok` lines printed; the 18 prior expectations unchanged. Independent cross-check outside the harness (declared scratch mirror of the delivered tool + contract + r95 fixture, swap applied by hand; assertion `depends_on == ['paired-crossing-decision']` pre-swap passed, printed `swapped -> ['aru-ninth-bell']`):

```
$ python3 $S/corpus/tools/dependency_freeze.py $S/corpus/fixtures/r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
FINDING ADDITION-DETECTED: event aftermath-missing-evin gained depends_on ['aru-ninth-bell']
FINDING REDUCTION-DETECTED: event aftermath-missing-evin lost depends_on ['paired-crossing-decision']
RESULT FAIL
manual probe exit=1
```

This persists blind-spot table row 2 ("wrong-but-earlier dependency edge", `corpus/knowledge/r99-gate-blind-spot-table.md`, demonstrated at r99 by verifier probe V16 P8) in the delivered gate.

## C1 — guarded r100 pin + eight-fixture chain

Pre-state proof that the pin was absent:

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r100-docket-review
FINDING UNPINNED-FIXTURE: no pin for 'r100-docket-review' in corpus/tools/dependency-freeze-contract.json (pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing', 'r99-window-lapse'])
RESULT ERROR
r100 verify exit=2
```

Integration-time operation, run once (not a verification command; must not be rerun to check a delivery):

```
$ python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/r100-docket-review
FROZEN r100-docket-review: events 9; dependency-edges 8; relations 1
DIGEST 77debadf5c0f6e2c27f18902f0710278eb4305c633ff73158df7082936325c19
FREEZE r100-docket-review: events 9/9; dependency-edges 8/8; relations 1/1
DIGEST 77debadf5c0f6e2c27f18902f0710278eb4305c633ff73158df7082936325c19
RESULT PASS
freeze exit=0
```

Eight-fixture verification, full receipts (each command `python3 corpus/tools/dependency_freeze.py corpus/fixtures/<name>`, repository root):

```
r88-m3-maya-cluster        FREEZE … events 2/2; dependency-edges 0/0; relations 0/0; DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae; RESULT PASS; exit=0
r94-paired-crossing        FREEZE … events 3/3; dependency-edges 2/2; relations 1/1; DIGEST 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef; RESULT PASS; exit=0
r95-crossing-aftermath     FREEZE … events 4/4; dependency-edges 3/3; relations 1/1; DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710; RESULT PASS; exit=0
r96-crossing-response      FREEZE … events 5/5; dependency-edges 4/4; relations 1/1; DIGEST 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c; RESULT PASS; exit=0
r97-crossing-acknowledgment FREEZE … events 6/6; dependency-edges 5/5; relations 1/1; DIGEST a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54; RESULT PASS; exit=0
r98-clerk-filing           FREEZE … events 7/7; dependency-edges 6/6; relations 1/1; DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0; RESULT PASS; exit=0
r99-window-lapse           FREEZE … events 8/8; dependency-edges 7/7; relations 1/1; DIGEST 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; RESULT PASS; exit=0
r100-docket-review         FREEZE … events 9/9; dependency-edges 8/8; relations 1/1; DIGEST 77debadf5c0f6e2c27f18902f0710278eb4305c633ff73158df7082936325c19; RESULT PASS; exit=0
```

8/8 clean; the seven inherited digests are exactly the Round-99/Round-100 values (none re-frozen).

Contract diff vs `6f86bf2` — exactly three hunks (`git diff 6f86bf2 -- corpus/tools/dependency-freeze-contract.json | grep '^@@'`):

- `@@ -32,7 +32,7 @@` — writer-managed top-level `revision` refresh: `b5fe472957ab1e4e9c90f5613acc14cd24a288ae` → `ebec6bbdeb1d919c9eb19e7fdd5b9c6dd14db026` (the r101 round-declaration commit, tree HEAD at freeze time);
- `@@ -677,6 +677,139 @@` — the new `r100-docket-review` pin (fixture `corpus/fixtures/r100-docket-review`, revision `ebec6bb…`, payload_schema_version 2, all ten declared files with per-file SHA-256, `content_sha256 77debadf…`, 9 events / 8 edges / 1 relation, counts entities 6 / sources 9, tick-16 edge `clerk-review-first-passage` → `clerk-lapse-recorded`);
- `@@ -806,6 +939,14 @@` — the new `self_test.expected.repointed_edge` case.

No other hunk; `provenance_note` and every inherited pin field byte-unchanged. `git diff --stat 6f86bf2 -- corpus/tools/` = contract +143/−1, `dependency_freeze.py` +18. (LOG.md/SCORECARD.md also appear in a full diffstat vs `6f86bf2`, but those landed in commit `ebec6bb` before this seat started — not my writes; `git status` shows my working-tree modifications as exactly the four owned files.)

## Docs (dated supersession)

- `corpus/tools/README.md` — new "Round-101 addendum: r100 pinned, eight-fixture chain, wrong-but-earlier edge persisted as self-test case (2026-10-18)": supersession paragraph (Round-100's seven-fixture wording and its "`r100-docket-review` is not part of this seven-fixture frozen chain" sentence superseded as of 2026-10-18, round 101), the freeze receipt, the 19-case section with hand-derived expectation and the independent probe, the 8/8 verification, and the unchanged-surface paragraph.
- `SKILL.md` freeze row — chain list now includes `r100-docket-review`; "19 cases (…; r101 added `repointed_edge`, the wrong-but-earlier repointed dependency edge)"; "exactly the eight chain fixtures, verifying 8/8 clean"; "The seven inherited pins retain every field from r100 closure `6f86bf2`"; new `dated supersession (2026-10-18, round 101)` bullet; the round-100 bullet kept as delivered history.

## Disclosures / bounds

- `corpus/knowledge/r99-gate-blind-spot-table.md` row 2 was **not** edited: the knowledge table is outside r101 producer byte ownership. The dated record of that row's closure by the persisted case lives in the tools README addendum and the SKILL.md supersession bullet. C3's "dated row update" is delivered as documentation-of-record, not as an edit to the table itself.
- Contract `provenance_note` deliberately unchanged (seat diff constraint: pin + case + revision refresh only).
- The self-test scratch directories it creates at the repo root are gitignored (`*-self-test-*/`) and were cleaned by the tool's `TemporaryDirectory`; my declared scratch mirror remains under `.ufo/waves/round-101/seats/U1-chain-eight-scratch/`.
- Baseline self-test before any edit: `SELF-TEST 18/18` / `RESULT PASS`, exit 0 (quoted in transcript); baseline 7-fixture chain PASS quoted in transcript.

## Bottom line

PASS — C1: guarded `--freeze` pinned `r100-docket-review` (receipt quoted), chain verifies 8/8 clean, contract diff vs `6f86bf2` is exactly pin + case + writer-managed revision refresh; C3: `repointed_edge` persisted (18→19), `SELF-TEST 19/19` on the delivered bytes with both `ADDITION-DETECTED` and `REDUCTION-DETECTED` in one run, exit 1, independently reproduced; README + SKILL.md superseded with dates; no axis harmed; no commits.
