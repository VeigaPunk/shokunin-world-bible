# V01-c1-chain — round-101 seat report (verifier, C1 chain)

- lane: lore-shokunin; round 101; seat V01 (c1-chain); model zai-coding-plan/glm-5.3-flash-low; date 2026-10-18
- baseline: r100 closure `6f86bf2`; tree HEAD `ebec6bb` (r101 declaration); wave tree uncommitted as expected
- verifies: U1's C1 — pin `r100-docket-review` into the frozen chain via guarded `--freeze`; eight fixtures 8/8 clean; ten-file digests match delivered bytes; contract pins exactly eight; six+one inherited pins' fields byte-identical vs baseline
- producer report polled and read: `.ufo/waves/round-101/seats/U1-chain-eight.md` (9758 bytes, mtime 00:21)

## Poll record

- tries 1–13 (~00:13–00:17): artifacts present (`dependency_freeze.py` 00:07:59, contract 00:08:32 — freeze already landed), no U1 report.
- try 23 (~00:21): FOUND `.ufo/waves/round-101/seats/U1-chain-eight.md`. Within the 40-try budget; no stall-escape needed.

## C1.1 — eight fixtures, 8/8 clean

Command (repository root, per fixture): `python3 corpus/tools/dependency_freeze.py corpus/fixtures/<name>` — final re-run on settled bytes. Full receipts, every one quoted:

```
r88-m3-maya-cluster         FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0 | DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae | RESULT PASS | exit=0
r94-paired-crossing         FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1 | DIGEST 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef | RESULT PASS | exit=0
r95-crossing-aftermath      FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1 | DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710 | RESULT PASS | exit=0
r96-crossing-response       FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1 | DIGEST 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c | RESULT PASS | exit=0
r97-crossing-acknowledgment FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1 | DIGEST a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54 | RESULT PASS | exit=0
r98-clerk-filing            FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1 | DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0 | RESULT PASS | exit=0
r99-window-lapse            FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1 | DIGEST 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e | RESULT PASS | exit=0
r100-docket-review          FREEZE r100-docket-review: events 9/9; dependency-edges 8/8; relations 1/1 | DIGEST 77debadf5c0f6e2c27f18902f0710278eb4305c633ff73158df7082936325c19 | RESULT PASS | exit=0
```

8/8 PASS, exit 0 on each. These DIGEST values are byte-identical to the receipts quoted in U1-chain-eight.md (no drift between U1's run and mine). The seven inherited digests are the Round-99/Round-100 values (none re-frozen). I did not re-run `--freeze` (U1 marks it integration-time, run-once; correct).

## C1.2 — r100 pin's ten-file digests match delivered bytes (independent recompute)

My own recompute (not the tool's word): `hashlib.sha256` per file over `corpus/fixtures/r100-docket-review/`, compared to `pins['r100-docket-review']['files']`, plus an independent replication of the aggregate `content_digest` (sha256 of `json.dumps({name: sha256}, sort_keys=True, separators=(",",":"))`):

```
OK  README.md:              a312a364d4d9476e98c0fae3f62b23bf72e73a06c508aac04ffe48cf9cf4c5fa
OK  claim-excerpt-map.md:   16981162f8476a8fcc1bd892ac0b1b9e6cb916e1d45e6f2ea392a5eeca769244
OK  contradictions.json:    37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
OK  entities.json:          db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984
OK  fictional-excerpts.md:  d01825a7e3c8f4af549b7acdde7eb8e1b9074a6eccb8ce6d12401cea19745705
OK  inspiration-note.md:    58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37
OK  relations.json:         c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9
OK  source-excerpt.md:      b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd
OK  sources.json:           effa5160eb7a6b228d52a972bf52beeffc1544d3cb1f6c5edb2850f88bd2d22e
OK  timeline.json:          008a1ff8dbef63e552e271f1be8eb536b1361c5a0fe83f008423b06d505ab7f8
content_sha256 recomputed == pin: 77debadf5c0f6e2c27f18902f0710278eb4305c633ff73158df7082936325c19
ALL TEN + AGGREGATE OK: True
```

10/10 per-file + aggregate match. Semantic spot-checks, also independent of the tool: pin `events` == inventory rebuilt from `timeline.json` (9 events, all `depends_on` sorted); pin `relations` == `[('aru','evin','agreed_co_stewardship_for_this_crossing')]` from `relations.json`; pin `counts` == fixture JSONs (events 9, dependency_edges 8, relations 1, entities 6, sources 9). Pin `revision` = `ebec6bbdeb1d919c9eb19e7fdd5b9c6dd14db026` == `git rev-parse HEAD` (full hash match).

## C1.3 — contract pins exactly eight

`json.load` of the delivered contract: `pins` has exactly 8 keys — r88-m3-maya-cluster, r94, r95, r96, r97, r98, r99, r100-docket-review (each mapping to its `corpus/fixtures/...` path). Baseline had 7; the only addition is `r100-docket-review`; nothing removed.

## C1.4 — six+one inherited pins byte-identical vs 6f86bf2 (git diff scoped)

Reference commit: the seat brief said "6f86bf6…" — `git cat-file -t 6f86bf6` → `fatal: Not a valid object name 6f86bf6`; that hash does not exist. I used `6f86bf2`, the named r100-closure baseline (round claims and LOG.md both name it). The "six+one" split is real in the baseline: six pins at revision `337f0fa52b02…` (r88-m3, r94–r98) + one at `b5fe472957ab…` (r99, repointed at r100 declare).

Method: (a) canonical-JSON comparison of each inherited pin dict between `git show 6f86bf2:corpus/tools/dependency-freeze-contract.json` and the delivered file — all 7 `dict_equal=True canonical_bytes_equal=True`, `ALL INHERITED IDENTICAL: True`; (b) scoped `git diff 6f86bf2 -- corpus/tools/dependency-freeze-contract.json` shows exactly three hunks:

```
@@ -32,7 +32,7 @@     top-level revision b5fe472957ab… → ebec6bbdeb1d… (writer-managed refresh, disclosed since r100)
@@ -677,6 +677,139 @@ the new r100-docket-review pin block only
@@ -806,6 +939,14 @@  the new self_test.expected.repointed_edge case (C3's deliverable)
```

No hunk touches any inherited pin; `provenance_note` unchanged. Both methods agree: every inherited pin field is byte-identical to baseline.

## Witnessed (not verdict-bearing for this seat)

- `git status --porcelain` final state: exactly `M SKILL.md`, `M corpus/tools/README.md`, `M corpus/tools/dependency-freeze-contract.json`, `M corpus/tools/dependency_freeze.py` + untracked `corpus/knowledge/r101-r10-register-first-entry.md` (U2's) — matches U1's "exactly these four M" claim and the byte-ownership rules. Process note: my first two status reads (~00:07, ~00:23) showed fewer modified files; SKILL.md/README.md were last written at 00:20:06/00:20:30 — the tree was mid-write while I polled. All C1 checks above were (re)run after 00:20 on settled bytes; contract bytes were stable throughout (mtime 00:08:32, unchanged across both chain runs).
- SKILL.md and tools README now carry the r101 dated-supersession wording (freeze row lists r100-docket-review; "19 cases … r101 added `repointed_edge`"); their content adequacy belongs to the C3/docs seat, not this one.
- The contract diff contains C3's `repointed_edge` case (hunk 3); I verified only its presence/location as part of scoping — its behavioral verification is the C3 seat's claim.

## Bottom line

PASS — eight fixtures verify 8/8 clean (all receipts quoted, matching U1's); the r100 pin's ten file digests + aggregate content digest recompute exactly against delivered bytes; the contract pins exactly eight; all six+one inherited pins' fields are byte-identical to baseline 6f86bf2 (canonical-JSON and scoped-diff agreement, only pin + case + disclosed revision refresh changed); "6f86bf6" in the brief is a nonexistent-hash typo for 6f86bf2.
