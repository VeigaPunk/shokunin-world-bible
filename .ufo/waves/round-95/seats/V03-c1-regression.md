# V03 — c1-regression seat report (round 95)

- Seat: V03 c1-regression. Report path (exclusive): `.ufo/waves/round-95/seats/V03-c1-regression.md`.
- Lane: lore-shokunin, round-95 single wave (64 seats). Baseline: r94 closure `fb118c4`.
- Task: regression battery over P1's delivered `corpus/tools/map_obligations.py`. Read-only everywhere except this report; scratch work under `/tmp/r95-v03/` (no repo scratch dir declared for this seat). No commits, no pushes, no network, no nested agents.
- Verified revision (frozen bytes): `corpus/tools/map_obligations.py` sha256 `d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108` (809 lines); `corpus/tools/map-obligations-contract.json` sha256 `8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db` (22 self-test cases). Both shas were identical immediately before and after every command in §2 and §3.

## 0. Poll-wait evidence (P1)

Baseline pre-P1 tool sha: `cc1df4dc406870b6fc4ddbc3291e3690cf87dfb061f76ec3b4fec5cfcfbab790`. I polled on 20 s cadence for the tool sha to change **and** a `seats/P1*` report to exist.

- 16:18–16:21: `tool_changed=no p1_report=absent` (P3, P4, P5 reports landed meanwhile).
- 16:23:02 tool sha `85c237c3…`, then `ca05159e…` (16:23:09), `9224a684…` (16:24:43), `d1c239cc…` (16:26:27) — P1 was mid-refactor. The first three revisions were **transient and broken** (evidence in §4); I did not treat them as deliverables.
- Poll hit at try 26: `POLL_HIT tries=26 tool_sha=d1c239cc… contract_sha=8173bb97… report=.ufo/waves/round-95/seats/P1-tool-code.md`. The sha then held stable through every subsequent command (re-checked at the end of §2 and §3).

## 1. Pre-P1 baseline (same commands, baseline revision `fb118c4`)

```
python3 corpus/tools/map_obligations.py corpus/fixtures/r93-m2-kojiki-cluster
OBLIGATIONS raw=12 mapped=12
RESULT PASS                                   EXIT=0

python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing
OBLIGATIONS raw=14 mapped=14
RESULT PASS                                   EXIT=0

python3 corpus/tools/map_obligations.py corpus/fixtures/r87-myth-cluster
FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column
RESULT ERROR                                  EXIT=2

python3 corpus/tools/map_obligations.py corpus/fixtures/r89-inspiration-paraphrase
FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column
RESULT ERROR                                  EXIT=2

python3 corpus/tools/map_obligations.py --self-test
… 20 SELF-TEST PASS lines …
RESULT PASS                                   EXIT=0

python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93
SNAPSHOT inputs=4 digests=verified
OBLIGATIONS raw=12 mapped=12
FROZEN expected=PASS/0 findings=none matched
RESULT PASS                                   EXIT=0
```

Usage probes at baseline: no args → `FINDING invalid_arguments: cluster directory is required` EXIT=2; nonexistent fixture → `FINDING cluster_missing: cannot resolve cluster: [Errno 2] …does-not-exist-r95` EXIT=2; unknown flag → `FINDING invalid_arguments: unrecognized arguments: --bogus-flag` EXIT=2.

## 2. Delivered regression battery (sha `d1c239cc…`, bracketed)

Commands run from repo root; every output below is verbatim.

**[1] r93-m2 — required 12/12 PASS**
```
python3 corpus/tools/map_obligations.py corpus/fixtures/r93-m2-kojiki-cluster
OBLIGATIONS raw=12 mapped=12
INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15
RESULT PASS
EXIT=0
```
PASS. Counts identical to baseline; one new additive receipt line (`INVENTORY`), one `RESULT` line, same exit.

**[2] r94-paired-crossing — required 14/14 PASS**
```
python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16
RESULT PASS
EXIT=0
```
PASS. Counts identical to baseline.

**[3] frozen r93 snapshot — digests verified + expected PASS/0 matched**
```
python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93
SNAPSHOT inputs=4 digests=verified
OBLIGATIONS raw=12 mapped=12
INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15
FROZEN expected=PASS/0 findings=none matched
RESULT PASS
EXIT=0
```
PASS. The `digests=verified` claim is independently confirmed — I re-hashed all four pinned inputs against `expected.json` myself:
```
entities.json           MATCH 19f75678dae1b59e6704d1be903a5cecf1b070dd44165e3047bc47efdb8e2d1d
relations.json          MATCH 32b79cd4d02793ce4c1f600522fb3810ffdbbad173b5707975fe9197ebf6e46d
timeline.json           MATCH 69da079eb29104cf4da04942ec3df79155569aa61d64fec00cb4aa7ffe2417e2
claim-excerpt-map.md    MATCH 17f0e8123f26e4f7c534c01a6fe843fe0e8e1278858c0b0ce74623cb7291f7d6
ALL_DIGESTS_VERIFIED
```
`expected.json` pins `exit_code: 0`, `result: PASS`, `finding_ids: []`; the delivered run matched all three.

**[4] r87-myth-cluster — must stay fail-closed**
```
python3 corpus/tools/map_obligations.py corpus/fixtures/r87-myth-cluster
FINDING unsupported_map: pointer cells must contain one canonical inline-code pointer
RESULT ERROR
EXIT=2
```
PASS (fail-closed held). Observation: the *reason text* changed versus baseline. Because the new dialect gate accepts the legacy header `JSON fact and fields` + `source_id`, r87 now gets past the header-role check and is rejected one layer deeper — its cells pack three co-mapped pointers into one cell. Same finding ID, same exit 2; the failure is still deterministic across repeated runs.

**[5] r89-inspiration-paraphrase — must stay fail-closed**
```
python3 corpus/tools/map_obligations.py corpus/fixtures/r89-inspiration-paraphrase
FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column
RESULT ERROR
EXIT=2
```
PASS. Unchanged message and exit (`Claim pointer` / `In-world source` header roles remain unsupported).

**[6][7][8] usage probes — all exit 2**
```
python3 corpus/tools/map_obligations.py
FINDING invalid_arguments: cluster directory is required
RESULT ERROR                                  EXIT=2

python3 corpus/tools/map_obligations.py corpus/fixtures/does-not-exist-r95
FINDING cluster_missing: cannot resolve cluster: [Errno 2] No such file or directory: '/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/does-not-exist-r95'
RESULT ERROR                                  EXIT=2

python3 corpus/tools/map_obligations.py --bogus-flag corpus/fixtures/r94-paired-crossing
FINDING invalid_arguments: unrecognized arguments: --bogus-flag
RESULT ERROR                                  EXIT=2
```
PASS. Byte-identical to baseline.

## 3. Supplementary checks (same frozen bytes)

**[9] `--self-test` — 22 cases, all PASS**
```
python3 corpus/tools/map_obligations.py --self-test
SELF-TEST PASS complete exit=0 findings=none
… (20 r94-era cases unchanged) …
SELF-TEST PASS map_missing exit=2 findings=['map_missing']
SELF-TEST PASS invalid_arguments exit=2 findings=['invalid_arguments']
SELF-TEST PASS frozen_complete exit=0 findings=none
SELF-TEST PASS frozen_tampered exit=2 findings=['snapshot_tampered']
SELF-TEST PASS frozen_missing_digests exit=2 findings=['unpinned']
SELF-TEST PASS frozen_expected_failure exit=1 findings=['missing_obligation']
SELF-TEST PASS frozen_verdict_mismatch exit=2 findings=['frozen_verdict_mismatch']
RESULT PASS
EXIT=0
```
22/22, exit 0. The live contract holds exactly the same 22 ids (including `map_missing`, `invalid_arguments`) — C1's 20→22 self-test claim verifies.

**[10][11] BR-02 renamed-key mutation — exit 1, stable `schema_drift`, deterministic**

Scratch copy `/tmp/r95-v03/mut-br02` = byte copy of `corpus/fixtures/r94-paired-crossing` with `entities[0].claims` renamed to `assertions` (claim content preserved verbatim) and map row `entities.json#/0/claims/0` removed. Same mutation on the **old** tool (from git) gave silent `OBLIGATIONS raw=13 mapped=13 / RESULT PASS / EXIT=0`. Delivered tool, two consecutive runs:
```
python3 corpus/tools/map_obligations.py /tmp/r95-v03/mut-br02     # run A and run B identical
OBLIGATIONS raw=13 mapped=13
INVENTORY JSON-FACTS 13/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 15/16 MISMATCH
FINDING schema_drift: entities.json#/0: 1 sourced-claim-shaped record(s) under unexpected key 'assertions'
RESULT FAIL
EXIT=1
```
**[12] control (key renamed, map row KEPT)** → `FINDING phantom_obligation …` + `FINDING schema_drift …`, `RESULT FAIL`, EXIT=1. The silent-PASS class is closed in both variants.

**[13] r88-m3 dialect (C3, supplementary — C3 is another seat's claim)**
```
python3 corpus/tools/map_obligations.py corpus/fixtures/r88-m3-maya-cluster
OBLIGATIONS raw=10 mapped=10
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12
RESULT PASS
EXIT=0
```
Exit 2 `unsupported_map` before, exit 0 after. Denominator note: the r88 map holds **10** JSON-fact obligation rows (4 `first_appearance` + 4 claims + 2 timeline; raw obligations = 10) and 2 editorial rows that the map itself labels "not extra JSON facts". The round's "12/12" is the *total row* count, which the tool prints as `TOTAL-ROWS 12/12`; the obligation receipt is 10/10. P1's own report reads it the same way. No corpus file was modified for this (fixture untouched: `git status` shows no r88 change).

**[14] `--help`** → EXIT=0 with **0** `RESULT` lines (unchanged from the documented r94 contract; exit 0 alone is not a PASS).

**[15] `--self-test` combined with a cluster** → `FINDING invalid_arguments: --self-test cannot be combined with cluster, --map, or --frozen`, `RESULT ERROR`, EXIT=2.

## 4. Mid-flight revisions (transient — recorded as process evidence, not as the deliverable)

While P1 was still writing, three sampled revisions were internally inconsistent and crashed on every operational path, e.g. on `d1c239cc`'s predecessors:
```
File "corpus/tools/map_obligations.py", line 400, in compare
    counts = Counter(pointer for pointer, _ in rows)
ValueError: too many values to unpack (expected 2, got 12)
EXIT=1
```
and `--self-test` reported `FINDING self_test_contract: contract self-test cases do not match the implemented cases` EXIT=2 until P2's 22-case contract landed. Both conditions were resolved in the frozen revision `d1c239cc` / `8173bb97`. Recording it because it shows the contract/implementation guard (`self_test_contract`) and the exit contract both bite during partial delivery — but it is **not** a finding against the delivered revision.

## 5. Negative controls I added (dialect gate + detector scope)

- **NEG-1 — bracket pointer injected into the canonical r94 dialect** (`entities.json#/0/first_appearance` → `entities[0].first_appearance` in the `JSON fact pointer and fields` column): `FINDING unsupported_map: co-mapped or unsupported pointer grammar`, `RESULT ERROR`, EXIT=2. The legacy dialect acceptance did **not** loosen the canonical dialect. Harm-none confirmed.
- **NEG-2 — claim record DELETED (not renamed) plus its map row removed** (`/tmp/r95-v03/neg-delete`), deterministic across two runs:
```
OBLIGATIONS raw=13 mapped=13
INVENTORY JSON-FACTS 13/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 15/16 MISMATCH
RESULT PASS
EXIT=0
```
  Bounded residual (outside C1's declared renamed-key scope, so not a claim failure): the map's own `**Expected inventory:** 14 JSON facts …` declaration is parsed, the receipt correctly prints ` MISMATCH`, but `print_inventory_receipt` is informational only (`map_obligations.py:258-270`) and the verdict stays `PASS` exit 0 because raw count (13) equals mapped count (13). This is the BR-01-adjacent deletion/dependency-reduction class still open after r95; the r94→r95 improvement is that the shortfall is now visible in the receipt line even though it does not move the exit code.

## 6. Scope, limits, and non-claims

- I verified only P1's tool file and the two self-test/contract receipts that my battery touches. I did not verify the r95 fixture (`r95-crossing-aftermath`), the README addendum, or C2/C3 acceptance — those are other seats' claims.
- `--frozen` refuses snapshots outside the repository root; all frozen runs here used the in-repo r94 snapshot.
- Nothing in this battery judges entailment, source authenticity, chronology, rights, permission, or canon.

## Bottom line

PASS — on the frozen delivered bytes (tool `d1c239cc…`, contract `8173bb97…`) the required regression battery is green: r93-m2 12/12 `RESULT PASS` exit 0, r94 14/14 `RESULT PASS` exit 0, `--frozen` `digests=verified` + `FROZEN expected=PASS/0 findings=none matched` exit 0 (all 4 pins independently re-hashed), r87 and r89 still exit 2 `unsupported_map`, and all three usage probes exit 2; additionally the BR-02 rename-and-drop-row mutation now yields a deterministic `FINDING schema_drift` exit 1 (was silent PASS exit 0), the canonical dialect still rejects bracket pointers (exit 2), and `--self-test` is 22/22 exit 0 against the live 22-case contract — with one bounded residual recorded in §5 (record *deletion* still exits 0 while printing an `INVENTORY … MISMATCH` receipt).
