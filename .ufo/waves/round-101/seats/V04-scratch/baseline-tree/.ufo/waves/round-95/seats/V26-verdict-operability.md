# V26 — verdict-operability (round 95, per-axis verdict)

**Seat:** V26 `verdict-operability`. Role: exactly one independent OPERABILITY verdict for the r95 delivered revision — new gate surfaces runnable, every documented command replays as written, 0/1/2 exit contract honored live — with bounds.
**Report path (only file written by this seat):** this file. No product file written, no commit, no push, no network, no nested agents.
**Baseline:** r94 closure `fb118c4` (`git rev-parse HEAD` → `fb118c42038ed27a747eec704b9aab41bb4b2ebe`, verified at report time).
**Seats read as instructed:** `V02-c1-selftest.md`, `V21-operability.md` — both landed inside the poll window; both bottom-line PASS; every operative point below is independently reproduced by me, not carried over.
**Scratch:** `/tmp/v26-scratch`, `/tmp/v26-sw`, `/tmp/v26-p2` only (mutation copies, sweep fixtures). No repo scratch dir. Nothing outside this report path was written in the repo.

## 0. Frozen revision (hash-pinned; re-verified at report time)

```
d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108  corpus/tools/map_obligations.py        (P1)
8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db  corpus/tools/map-obligations-contract.json (P2)
5d033c9db8a72801c9b8d5e609e01cddf1ace668711e24d0476b8cbd6879a264  corpus/tools/README.md                 (P2 addendum)
9d27af4ac9644210d3ee1df26938a4a5592b8cbcfdb5d6fb880de6ccdb1bdd0b  corpus/fixtures/r95-crossing-aftermath/README.md          (P4)
30281ff1a497bbe66f23cbd8a49befb3319595f20990718a0ffe8050741a874a  corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md (P4)
f87ed42ad4d42143bb84f13539f2db8ca0d5f221aaf4eaffdbd6874b5ef1ab9a  corpus/knowledge/r95-aftermath-scope-note.md (P5)
```

Hashes identical before and after every run below (re-checked at the end); tool `d1c239cc…` and contract `8173bb97…` match the revisions pinned independently by P1's, V02's and V21's reports. Python 3.14.7, all commands from the repo root unless stated.

**Mid-flight states were not verified and are not evidence of the delivered revision** (disclosed, not smoothed):
- At 16:22–16:25 the in-progress tool against the still-20-case contract gave `FINDING self_test_contract: contract self-test cases do not match the implemented cases` / `RESULT ERROR` / exit 2 (reproduced by me, also recorded by P1 §6, V02 §0, V21 §5.4). Superseded by `d1c239cc`+`8173bb97`.
- P5's note documents its own receipts at in-flight tool revision `9224a684…` and records an intermediate revision (`ca05159e…`) raising an uncaught `ValueError`; P5 asks for a re-run before citing. I re-ran all three P5-documented commands on the delivered revision — all pass (§2).

## 1. `--self-test` — runnable, 22/22, expectation-driven, discriminating

```
$ python3 corpus/tools/map_obligations.py --self-test
SELF-TEST PASS complete exit=0 findings=none
SELF-TEST PASS missing exit=1 findings=['missing_obligation']
SELF-TEST PASS duplicate exit=1 findings=['duplicate_mapping']
SELF-TEST PASS phantom exit=1 findings=['phantom_obligation']
SELF-TEST PASS source_id_mismatch exit=1 findings=['source_id_mismatch']
SELF-TEST PASS malformed_json exit=2 findings=['malformed_json']
SELF-TEST PASS map_missing exit=2 findings=['map_missing']
SELF-TEST PASS co_mapped_grammar exit=2 findings=['unsupported_map']
SELF-TEST PASS legacy_grammar exit=2 findings=['unsupported_map']
SELF-TEST PASS invalid_pointer exit=2 findings=['invalid_pointer']
SELF-TEST PASS empty_segment exit=2 findings=['invalid_pointer']
SELF-TEST PASS noncanonical_index exit=2 findings=['invalid_pointer']
SELF-TEST PASS noncanonical_claim_index exit=2 findings=['invalid_pointer']
SELF-TEST PASS foreign_path exit=2 findings=['foreign_path']
SELF-TEST PASS traversal_path exit=2 findings=['unsafe_path']
SELF-TEST PASS symlink_path exit=2 findings=['unsafe_path']
SELF-TEST PASS invalid_arguments exit=2 findings=['invalid_arguments']
SELF-TEST PASS frozen_complete exit=0 findings=none
SELF-TEST PASS frozen_tampered exit=2 findings=['snapshot_tampered']
SELF-TEST PASS frozen_missing_digests exit=2 findings=['unpinned']
SELF-TEST PASS frozen_expected_failure exit=1 findings=['missing_obligation']
SELF-TEST PASS frozen_verdict_mismatch exit=2 findings=['frozen_verdict_mismatch']
RESULT PASS
exit=0
```

Re-run at freeze: 22 `SELF-TEST PASS` lines, exit 0. 20→22 as declared; `map_missing` and `invalid_arguments` both present, exit 2 each. The delivered contract lists 22 cases; the tool's case-set guard (`self_test_contract`) was observed to bite on the mismatched mid-flight pair, so the persisted expectations cannot silently drift (V02 §1/§6 reproduced the negative control: a tampered expectation gives `self_test_mismatch` exit 2 — I did not re-run that control, it is V02's evidence).

## 2. Documented commands — every one replays as written

**P4's fixture README block (`corpus/fixtures/r95-crossing-aftermath/README.md:26–28`), run exactly as written:**

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
CLEAN: schema, citations, relations, timeline; 0 violations          exit=0

$ python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath
RECEIPT JSON-FACTS 15; EDITORIAL-ROWS 2; TOTAL-ROWS 17
SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 17/17; VALIDATED-ROWS 17/17
RESULT PASS                                                          exit=0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS                                                          exit=0
```

Counts match the fixture's declared shape (`entities 5 / relations 1 / timeline 4 / sources 4`, contradictions `[]`, read by `json.load`). The r95 README's claim "15 source-attributed JSON pointer obligations" is exactly `raw=15 mapped=15`.

**P5's note receipts block (`corpus/knowledge/r95-aftermath-scope-note.md:42–48`), same three commands:** all three reproduce the note's quoted results and exit 0 on the delivered revision (re-established after P5's in-flight `9224a684…` receipts; no documented command fails as written).

**Tools README Round-95 addendum (`corpus/tools/README.md`):**

| Documented command / claim | Observed |
|---|---|
| `... map_obligations.py corpus/fixtures/r88-m3-maya-cluster` → exit 0, `raw=10 mapped=10`, `INVENTORY ... 12/12` | `OBLIGATIONS raw=10 mapped=10` / `INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12` / `RESULT PASS`, exit 0 (before, at `cc1df4dc`: exit 2 `unsupported_map`) |
| `... corpus/fixtures/r87-myth-cluster` fail-closed | exit 2, `FINDING unsupported_map: pointer cells must contain one canonical inline-code pointer` |
| `... corpus/fixtures/r89-inspiration-paraphrase` fail-closed | exit 2, `FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column` |
| r93 example 12/12, r94 example 14/14, `--frozen` replay | all exit 0, `RESULT PASS`; each now prints one additional `INVENTORY` line (disclosed in the addendum) |
| "Keeping the map row while renaming the key reports `phantom_obligation` and `schema_drift` together, still exit 1" (scratch copy) | `raw=13 mapped=14`, `FINDING phantom_obligation: entities.json#/0/claims/0 is not a raw source-attributed obligation` + `FINDING schema_drift: entities.json#/0: 1 sourced-claim-shaped record(s) under unexpected key 'assertions'`, `RESULT FAIL`, exit 1 |
| "a declared count that disagrees ... appends ` MISMATCH` ... but does not by itself change the exit code" (scratch copy, `14→13 JSON facts`) | `INVENTORY JSON-FACTS 14/13; ... MISMATCH` / `RESULT PASS`, exit 0 |

**LOG r95 counting commands:** the BR-02 mutation demo (old tool from git `fb118c4` vs delivered, `/tmp` scratch copy of `r94-paired-crossing` with `claims`→`assertions` and the J06 map row deleted):

```
OLD tool (git fb118c4)   OBLIGATIONS raw=13 mapped=13 / RESULT PASS                          exit=0   <- silent pass
DELIVERED tool           OBLIGATIONS raw=13 mapped=13
                         INVENTORY JSON-FACTS 13/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 15/16 MISMATCH
                         FINDING schema_drift: entities.json#/0: 1 sourced-claim-shaped record(s) under unexpected key 'assertions'
                         RESULT FAIL                                                      exit=1
```

Reproduced exactly as declared (and as P1 §3 / V02 §5 report independently).

Additional documented forms verified: `--map claim-excerpt-map.md` explicit → exit 0; invocation from a non-repo cwd with absolute tool+cluster paths → exit 0; `--frozen` snapshot outside the repository → exit 2 `FINDING unsafe_path: frozen snapshot must be inside the owning repository`.

## 3. Exit contract 0/1/2 honored live (19 invocations)

| Path | exit | RESULT lines | FINDING lines | traceback | stderr bytes |
|---|---|---|---|---|---|
| r93 default / r94 default / r88 default / r95 default | 0 | 1 | 0 | 0 | 0 |
| `--self-test` / `--frozen` | 0 | 1 | 0 | 0 | 0 |
| `--help` | 0 | **0** | 0 | 0 | 0 |
| r87 fail-closed / r89 fail-closed | 2 | 1 | 1 | 0 | 0 |
| no-arg / missing cluster | 2 | 1 | 1 | 0 | 0 |
| live fail: missing row / duplicate row / source-ID mismatch / phantom pointer | 1 | 1 | 1 | 0 | 0 |
| live err: malformed JSON / legacy pointer under canonical header | 2 | 1 | 1 | 0 | 0 |
| misuse: `--self-test`+cluster / `--frozen`+cluster | 2 | 1 | 1 | 0 | 0 |

All four live exit-1 cases and both live exit-2 cases ran on `/tmp` copies of `r94-paired-crossing`; live fixtures untouched. `--help` exiting 0 with zero RESULT lines is the documented BR-06 caveat, unchanged — exit 0 alone is not a PASS. Terminal `RESULT` line exactly once on every operational path; empty stderr and no traceback everywhere.

## 4. No live-tree writes

```
find corpus -type f ! -path "*__pycache__*" | sort | xargs sha256sum | sha256sum
BEFORE 31f7360097bf401ed8f427280a9568e873279b8199db2025444f967538b69391
AFTER  31f7360097bf401ed8f427280a9568e873279b8199db2025444f967538b69391   (identical)
```

Whole-repo `git status --porcelain` unchanged across the run set: ` M LOG.md`, ` M corpus/tools/{README.md,map-obligations-contract.json,map_obligations.py}`, `?? .ufo/waves/round-95/`, `?? corpus/fixtures/r95-crossing-aftermath/`, `?? corpus/knowledge/r95-aftermath-scope-note.md` — producer edits only, nothing from tool runs.

Independent census replay (my own loop over `corpus/fixtures/*/`, `check_bible.py`): `dirs=169 clean=35 negative=134 violation_prefix_lines=421 summary_sum=421 stderr_nonempty=0` — reproduces V21 §5.7 exactly and the declared 168→169 delta (one new clean fixture).

## 5. OPERABILITY VERDICT — **improved (bounded)**

On the frozen revision the round's operability surface grew in three runnable, documented ways, and no operability property was harmed:

- **Runnable new surfaces:** `map_obligations` now exits 0 on `r88-m3-maya-cluster` (previously exit 2 `unsupported_map`), so that cluster joins the runnable documented command set; `--self-test` is 22/22 exit 0 with the two new persisted cases; the BR-02 mutation class is demonstrated live (old exit 0 → delivered exit 1 `schema_drift`).
- **Documented commands replay:** every command in P4's fixture README, P5's note, and the tools README r94+r95 addenda runs as written with the recorded exit and result text. The r94 receipts gain one disclosed `INVENTORY` line while keeping their `OBLIGATIONS`/`RESULT` lines and exits.
- **Exit contract honored:** 0/1/2 with one terminal RESULT line, stable FINDING IDs, empty stderr, no traceback, on all 19 probed invocations; `--help` remains the documented RESULT-less exit-0 caveat.
- **No live-tree writes:** corpus manifest byte-identical around the runs; support_check receipts on r88/r93/r94 unchanged (10/10, 12/12, 14/14 PASS).

**Bounds (all disclosed, none waived):**

1. **BR-05 still open (witnessed live).** Self-test scratch is created under the repo root (`tempfile.TemporaryDirectory(prefix="map-obligations-self-test-", dir=ROOT)`) and is not gitignored. During a concurrent seat's run I observed `?? map-obligations-self-test-9t5f9gk5/` in `git status --porcelain`; it was gone within 25 s (transient), and my own runs left zero residue. Unchanged in r95; the addendum says so explicitly.
2. **`schema_drift` has no persisted self-test case.** `grep -c schema_drift corpus/tools/map-obligations-contract.json` → 0. The round's headline C1 behavior is pinned only by the mutation demo (and producer/verifier replay), so a future regression that removed the drift check would still show `--self-test` 22/22 exit 0. (Same finding as V02 §3; it bounds calibration/operability, not the delivered behavior.)
3. **`INVENTORY` is a receipt, never a gate.** A tampered declared count prints ` MISMATCH` and still exits 0 (reproduced). Documented as such; not a hidden pass.
4. **Stale prose outside producer write scope:** `corpus/README.md:35` still says `--self-test` "(20 persisted cases)"; SCORECARD r94 sections (`:374`, `:400`, `:416`) cite 20/20 as r94 history. These are doc-parity integration items for closure (V20-doc-parity's axis), not unfulfilled ownership claims — P2 owns only `corpus/tools/README.md` + the contract.
5. **Round-text reconciliation, not a defect:** C3's "12/12" is the r88 map's total row count (10 obligations + 2 editorial rows) — the tool prints both figures correctly labelled (`raw=10 mapped=10`, `TOTAL-ROWS 12/12`); the addendum's wording is accurate.
6. **Scope:** exit 0 means one-to-one mapping completeness and source-ID agreement only — nothing here is entailment, fidelity, chronology, rights, permission, or canon evidence. This verdict covers operability of the delivered artifacts only; it is not an admission, a capability row, or a whole-round verdict.

## Bottom line

**PASS / operability improved (bounded)** — on the frozen r95 revision (tool `d1c239cc…`, contract `8173bb97…`) `--self-test` is 22/22 exit 0, every command documented in the fixture README, the r95 note and the tools README r94/r95 addenda replays as written (r95 15/15, r88 12/12, r87/r89 exit-2 fail-closed, r93 12/12, r94 14/14, frozen replay, BR-02 mutation old-0→new-1 `schema_drift`), the 0/1/2 exit contract holds with one terminal RESULT line and empty stderr on all 19 probed invocations, and the corpus manifest is byte-identical around the runs; bounds are the still-open transient repo-root scratch (BR-05), the unpinned `schema_drift` self-test gap, the non-gating `INVENTORY` receipt, and stale `corpus/README.md:35` prose outside the producers' write scope.
