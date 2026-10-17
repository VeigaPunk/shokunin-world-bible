# P1 — tool-code seat report (round 95)

- Seat: P1 tool-code. Owned file: `corpus/tools/map_obligations.py` (alone; no other file written).
- Baseline: r94 closure `fb118c4`. Round: r95, 64-seat single wave, lore-shokunin.
- Deliverable: two bounded stdlib-only extensions to `map_obligations.py` — (a) BR-02 `schema_drift` detection (exit 1), (b) r88-m3 map-dialect coverage. 0/1/2 exit contract and the single terminal `RESULT` line preserved.
- Work footprint: `git status --porcelain` shows ` M corpus/tools/map_obligations.py` as my only write; `git diff --numstat` = `130 12 corpus/tools/map_obligations.py`. All scratch work was done under `/tmp` (no repo scratch dir declared for this seat). No commits, no pushes, no network.

## 1. What changed (file:line on the delivered revision)

| Change | Location |
|---|---|
| Legacy-dialect pointer translation `entities[0].first_appearance` / `entities[0].claims[0]` / `timeline[0]` / `relations[0]` → canonical pointers | `corpus/tools/map_obligations.py:154` (`legacy_pointer`), `:19-25` (constants) |
| Dialect gate: bracket cells are accepted only when the table's pointer column is the legacy `JSON fact and fields` column | `:173` (`parse_pointer_cell(cell, legacy=False)`), `:292-303` |
| `schema_drift` detection + claim-shape predicate | `:357` (`claim_shaped`), `:377-388` |
| Drift returned as an exit-1 finding (not a `ToolError`), merged with comparison findings | `:365`, `:435` (`run_cluster`), `:525` (`run_frozen`) |
| Inventory receipt echo (`INVENTORY JSON-FACTS x/x; EDITORIAL-ROWS x/x; TOTAL-ROWS x/x`, plus ` MISMATCH` suffix) | `:223`, `:238`, `:258` |
| New persisted self-test cases `map_missing`, `invalid_arguments` | `:31` (`SELF_TEST_CASES`), `:638`, `:651`, `:728` |

`claim_shaped(record)` requires a non-empty string `statement` **and** a non-empty string `source_id`, so the check cannot fire on the r87–r91 `provenance` lists (`from_holder`/`to_holder`/`tick`/`source_id`, ~30 fixtures) — see probe 3 below. `schema_drift` is emitted as `FINDING schema_drift: entities.json#/<i>: <n> sourced-claim-shaped record(s) under unexpected key '<key>'` and exits **1** (comparison-class finding, not exit 2).

## 2. Declared gates — commands and observed outputs

`python3 corpus/tools/map_obligations.py corpus/fixtures/r93-m2-kojiki-cluster` → exit 0
```
OBLIGATIONS raw=12 mapped=12
INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15
RESULT PASS
```

`... corpus/fixtures/r94-paired-crossing` → exit 0
```
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16
RESULT PASS
```

`... corpus/fixtures/r88-m3-maya-cluster` (before: exit 2 `unsupported_map`) → exit 0
```
OBLIGATIONS raw=10 mapped=10
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12
RESULT PASS
```

`... --frozen .ufo/waves/round-94/frozen/map-obligations-r93` → exit 0
```
SNAPSHOT inputs=4 digests=verified
OBLIGATIONS raw=12 mapped=12
INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15
FROZEN expected=PASS/0 findings=none matched
RESULT PASS
```

Fail-closed controls (all exit 2, unchanged):
```
corpus/fixtures/r87-myth-cluster         FINDING unsupported_map: pointer cells must contain one canonical inline-code pointer
corpus/fixtures/r89-inspiration-paraphrase FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column
corpus/fixtures/r87-probe-source-prefix   FINDING map_missing: expected exactly one conventional claim-to-excerpt map
corpus/fixtures/r89-c1-multi-cause-valid  FINDING map_missing: expected exactly one conventional claim-to-excerpt map
```

CLI contract paths (one terminal RESULT line, zero stderr in every case):
```
no args            FINDING invalid_arguments: cluster directory is required          exit 2
--self-test + dir  FINDING invalid_arguments: --self-test cannot be combined with cluster, --map, or --frozen   exit 2
--frozen + dir     FINDING invalid_arguments: --frozen cannot be combined with cluster or --map                 exit 2
--bogus + dir      FINDING invalid_arguments: unrecognized arguments: --bogus        exit 2  stderr_bytes=0
--help             exit 0, RESULT lines=0 (unchanged)
```

## 3. BR-02 before→after (mutation demo, /tmp scratch copies)

Mutation on a copy of `r94-paired-crossing`: entity 0's `claims` key renamed to `assertions` with content preserved, and the map row `entities.json#/0/claims/0` removed.

```
OLD tool (git fb118c4)   OBLIGATIONS raw=13 mapped=13 / RESULT PASS          exit=0   <- silent, the r94 BR-02 defect
DELIVERED tool           OBLIGATIONS raw=13 mapped=13
                         INVENTORY JSON-FACTS 13/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 15/16 MISMATCH
                         FINDING schema_drift: entities.json#/0: 1 sourced-claim-shaped record(s) under unexpected key 'assertions'
                         RESULT FAIL                                          exit=1
```

## 4. Full-corpus regression (old tool from `fb118c4` vs delivered, every `corpus/fixtures/*`)

Compared `(exit code, sorted finding-id list)` per fixture: **exactly one fixture changed** — `r88-m3-maya-cluster` `old_rc=2 old=[unsupported_map]` → `new_rc=0 new=[]`, the declared C3 improvement. All other 150 fixtures identical (r93/r94 unchanged at exit 0; every mapless fixture `map_missing` exit 2; r87-myth-cluster and r89-inspiration-paraphrase `unsupported_map` exit 2).

`check_bible` (untouched by this seat) on the named fixtures — all `exit=0`, `CLEAN: schema, citations, relations, timeline; 0 violations`: r87-myth-cluster, r88-m3-maya-cluster, r89-inspiration-paraphrase, r93-m2-kojiki-cluster, r94-paired-crossing, r95-crossing-aftermath.

`support_check` receipts unchanged (tool not touched): r88 `RECEIPT JSON-FACTS 10; EDITORIAL-ROWS 2; TOTAL-ROWS 12` / `MODES 12/12` PASS; r93 `SOURCE-SUPPORT 12/12` PASS; r94 `SOURCE-SUPPORT 14/14` PASS.

Cross-check of a sibling artifact (not mine): `map_obligations corpus/fixtures/r95-crossing-aftermath` → `OBLIGATIONS raw=15 mapped=15`, `INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17`, PASS exit 0 — consistent with C2's declared 15 obligations.

## 5. Adversarial probes (scratch copies under /tmp)

| Probe | Observed |
|---|---|
| BR-02 rename with the map row **kept** | exit 1, findings `phantom_obligation`, `schema_drift` |
| Renamed key + `claims` removed + records **not** claim-shaped (no `statement`) + row removed | exit 0, **no** `schema_drift` — documented bound (see §6) |
| `provenance`-list fixture (`r87-probe-record-and-chain`) + a valid map | 24 findings, **no** `schema_drift` — drift does not fire on chain-shape records |
| Empty list / string under an unexpected key | exit 0, no drift |
| Drift on two entities under `assertions` and `claims_v2` | two `schema_drift` findings, deterministically sorted |
| r88 map with a co-mapped legacy cell (`` `entities[0].first_appearance`, `entities[0].claims[0]` ``) | exit 2 `unsupported_map` |
| r88 map with the header rewritten to `JSON fact pointer and fields` (bracket cells) | exit 2 `unsupported_map` (dialect gate holds; same class as self-test `legacy_grammar`) |
| r88 dropped claim row | exit 1 `missing_obligation` (`raw=10 mapped=9`) |
| r88 row bound to a wrong source ID | exit 1 `source_id_mismatch` |
| r88 phantom index `entities[9].claims[0]` | exit 1 `missing_obligation` + `phantom_obligation` |

r88 dialect parse dump: 10 obligation rows with canonical pointers `entities.json#/0..3/first_appearance`, `entities.json#/0..3/claims/0`, `timeline.json#/0`, `timeline.json#/1`, all bound to `paired-clock`; declared inventory `(10, 2, 12, 8)`, editorial rows parsed `2`. This is the same 12-row set `support_check` validates on r88 (`MODES 12/12`).

## 6. Findings, bounds, and a contradiction to record

1. **Contradiction with the round declaration (evidence, not a defect of my seat).** C3 declares `12/12 PASS` for r88. The r88 fixture has **10** raw source-attributed obligations (4 `first_appearance` + 4 entity claims + 2 timeline events; `relations.json` is empty). "12" is the r88 map's declared **total row count** (10 JSON facts + 2 editorial rows = support_check's `MODES 12/12`), not an obligation count. The tool therefore reports `OBLIGATIONS raw=10 mapped=10` and, to make the declared figure traceable, prints `INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12` — both numbers appear, correctly labeled, on an exit-0 `RESULT PASS`. No implementation can honestly report `raw=12 mapped=12` here: the two editorial rows point at `source-excerpt.md`, not JSON pointers, and counting them as obligations would emit `phantom_obligation` and exit 1.
2. **New receipt line on r93/r94 output.** The `INVENTORY ...` line is printed for every map that declares `**Expected inventory:**`, so r93/r94 stdout gained one line. Their obligation counts (`12/12`, `14/14`), findings (`none`) and exits (0) are unchanged, as is the frozen replay. Disclosed here for adjudication.
3. **Bounded residual (schema-drift class).** Drift fires only on the declared mutation class: an unexpected key whose records are full claim-shaped (`statement` + `source_id`). A rename that also changes the inner record shape (e.g. `assertions: [{"source_id": ...}]`) is still a silent PASS (probe row 2). Also bounded to `entities.json` records; relations/timeline records are not drift-scanned.
4. **Bounded residual (inventory).** The declared inventory is echoed, never gated: a tampered `**Expected inventory:**` line prints ` MISMATCH` or `INVENTORY declaration-malformed` but does not change the exit code. No new failure modes were added beyond `schema_drift`.
5. **Dialect bound.** The bracket grammar is accepted only under the legacy `JSON fact and fields` column; r87's co-mapped multi-token cells, r89's map (no `source-ID` column) and any bracket cell under the canonical `JSON fact pointer and fields` header stay exit 2 `unsupported_map`.
6. **Coordination dependency.** The two new self-test cases are implemented in my file, but their expectations live in P2's `corpus/tools/map-obligations-contract.json`; `--self-test` fails closed with `self_test_contract` while that file still lists 20 cases (observed: `FINDING self_test_contract: contract self-test cases do not match the implemented cases`, exit 2). Verified independently against a scratch 22-case copy of the contract at `/tmp/p1-selfcheck/`: **22/22 SELF-TEST PASS**, `RESULT PASS`, exit 0 (including `map_missing exit=2 findings=['map_missing']` and `invalid_arguments exit=2 findings=['invalid_arguments']`). Against the live contract: see §7.

## 7. Self-test against the live contract

P2's `corpus/tools/map-obligations-contract.json` landed mid-round with 22 cases; its two new entries are exactly `{"id": "map_missing", "exit": 2, "finding_ids": ["map_missing"]}` and `{"id": "invalid_arguments", "exit": 2, "finding_ids": ["invalid_arguments"]}`.

`python3 corpus/tools/map_obligations.py --self-test` against the live contract → **22/22 SELF-TEST PASS**, `RESULT PASS`, exit 0:
```
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
```
Pre-landing behaviour of the same command (contract still at 20 cases) was the fail-closed `FINDING self_test_contract: contract self-test cases do not match the implemented cases`, exit 2 — the contract/implementation guard still bites.

Cross-seat observation (not my file, not edited): at my final check `corpus/tools/README.md` was unchanged by P2 and its line 95 still reads `# 20/20 SELF-TEST PASS / RESULT PASS, exit 0`, and it does not yet document `schema_drift`, the r88 dialect, or the `INVENTORY` line. The README addendum is P2's declared artifact.

## Bottom line

PASS (bounded) — `schema_drift` closes the BR-02 silent-PASS class at exit 1 with a stable finding id (old tool exit 0 / delivered exit 1 on the exact rename-`claims`-and-drop-row mutation), r88 flips from exit 2 `unsupported_map` to exit 0 over the same 12 mapped rows (10 obligations + 2 editorial, receipt-labeled), r87/r89 stay exit 2, `--self-test` is 22/22 exit 0 against the live 22-case contract, and the full-corpus before/after diff (old tool vs delivered, every fixture) shows exactly the one intended change; the round's `12/12` for r88 is the map's total row count, not an obligation count (§6.1).
