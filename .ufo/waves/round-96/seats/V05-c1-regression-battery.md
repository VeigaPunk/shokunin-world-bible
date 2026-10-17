# V05 — c1-regression-battery (round 96)

- Seat: V05 c1-regression-battery. Report path (exclusive): `.ufo/waves/round-96/seats/V05-c1-regression-battery.md`.
- Lane: lore-shokunin, round-96 single wave (64 seats). Baseline: r95 closure `dcb2d92` (HEAD `60dba0c`).
- Task: full regression battery over Q1's delivered `corpus/tools/map_obligations.py` — r87–r96 exits unchanged vs the r95 pins (r88 10/10 TOTAL 12/12; r93 12/12; r94 14/14; r95 15/15; r87/r89 exit 2; r96 16/16 once Q5 lands), `--frozen` r93 replay, usage exit 2, support_check receipts r87–r96 unchanged. Read-only everywhere except this report plus `.ufo/waves/round-96/seats/V05-scratch/` (absolute paths under the lane repo for every write). No commits, no pushes, no network, no nested agents.
- Verified revision (frozen bytes): `corpus/tools/map_obligations.py` sha256 `2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8` (mtime `2026-10-17 17:47:24 -0300`), identical at poll hit (try 29), after a 15 s stability recheck, immediately after the delivered battery, and at final re-read after the self-test rerun. Pre-Q1 baseline revision: same file at sha256 `d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108` (extracted via `git show dcb2d92:corpus/tools/map_obligations.py`, re-hashed to confirm). `corpus/tools/map-obligations-contract.json` sha256 `97b76bb8b1fea97f166ef7586eba69c427ec15bbe7b34eb5345ec65c936493b6` (Q2's 24-case contract, mtime `17:50:17`, landed before my delivered capture at `17:50:27`); `corpus/tools/support_check.py` byte-frozen at `55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c`.

## 0. Poll-wait evidence (Q1 + Q5)

Poll loop `.ufo/waves/round-96/seats/V05-scratch/poll.sh` (20 s cadence, 40 tries), log `poll.log`. Condition: Q1 report exists AND tool sha ≠ `d1c239cc…`.

- tries 1–8: `tool_sha=d1c239cc… q1_report=absent q5_map=absent`
- try 9: Q5's map appears (`corpus/fixtures/r96-crossing-response/claim-excerpt-map.md`)
- tries 12–21: tool mid-flight, transient shas `99c7d764…`, `965c1ec4…`, `db924c64…`, `8cbcdb51…`, `44a6ffd4…`, `c2c284c0…`, `6634e176…` — **not treated as deliverables** (r95 showed transient broken revisions)
- tries 22–28: `tool_sha=2b0ba815… q1_report=absent`
- **`POLL_HIT tries=29 tool_sha=2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8 report=.ufo/waves/round-96/seats/Q1-tool-hardening.md q5_map=corpus/fixtures/r96-crossing-response/claim-excerpt-map.md`**

All verification below ran only after the hit, against the stable `2b0ba815…` revision.

## 1. Pre-Q1 baseline (r95 revision `d1c239cc…`, before Q1's first write)

Captured 17:4x via `V05-scratch/capture.sh` into `V05-scratch/baseline/` (verbatim):

```text
map-r87:   FINDING unsupported_map: pointer cells must contain one canonical inline-code pointer | RESULT ERROR | EXIT=2
map-r88:   OBLIGATIONS raw=10 mapped=10 / INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12 / RESULT PASS | EXIT=0
map-r89:   FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column | RESULT ERROR | EXIT=2
map-r93:   OBLIGATIONS raw=12 mapped=12 / INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15 / RESULT PASS | EXIT=0
map-r94:   OBLIGATIONS raw=14 mapped=14 / INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16 / RESULT PASS | EXIT=0
map-r95:   OBLIGATIONS raw=15 mapped=15 / INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17 / RESULT PASS | EXIT=0
map-r96:   FINDING map_missing: expected exactly one conventional claim-to-excerpt map | RESULT ERROR | EXIT=2   (Q5 map not yet landed)
map-frozen: SNAPSHOT inputs=4 digests=verified / OBLIGATIONS raw=12 mapped=12 / INVENTORY … 15/15 / FROZEN expected=PASS/0 findings=none matched / RESULT PASS | EXIT=0
usage:     no-args → invalid_arguments: cluster directory is required | EXIT=2
           missing  → cluster_missing: cannot resolve cluster: [Errno 2] …does-not-exist-r96 | EXIT=2
           --bogus-flag → invalid_arguments: unrecognized arguments: --bogus-flag | EXIT=2
self-test: 22 SELF-TEST PASS lines / RESULT PASS | EXIT=0   (no `SELF-TEST CASES` header line pre-Q1)
support r87/r88/r93/r94/r95: all RESULT PASS | EXIT=0 (see §5); support r96: FAIL: claim-to-excerpt map not found | EXIT=2
```

The r95-revision baseline reproduces every r95 pin (r88 10/10 + 12/12, r93 12/12, r94 14/14, r95 15/15, r87/r89 exit 2), confirming the pins against the frozen tool revision that produced them.

## 2. Delivered battery (tool `2b0ba815…`, same commands, `V05-scratch/delivered/`)

`bash V05-scratch/capture.sh …/delivered` at 17:50:27–28; verbatim terminal lines and exits:

```text
=== map-r87 ===
FINDING unsupported_map: pointer cells must contain one canonical inline-code pointer
RESULT ERROR
EXIT=2

=== map-r88 ===
OBLIGATIONS raw=10 mapped=10
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12
RESULT PASS
EXIT=0

=== map-r89 ===
FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column
RESULT ERROR
EXIT=2

=== map-r93 ===
OBLIGATIONS raw=12 mapped=12
INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15
RESULT PASS
EXIT=0

=== map-r94 ===
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16
RESULT PASS
EXIT=0

=== map-r95 ===
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS
EXIT=0

=== map-r96 (Q4 tables + Q5 map) ===
OBLIGATIONS raw=16 mapped=16
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
RESULT PASS
EXIT=0

=== map-frozen (r93 snapshot) ===
SNAPSHOT inputs=4 digests=verified
OBLIGATIONS raw=12 mapped=12
INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15
FROZEN expected=PASS/0 findings=none matched
RESULT PASS
EXIT=0

=== usage probes ===
no-args:      FINDING invalid_arguments: cluster directory is required | RESULT ERROR | EXIT=2
missing:      FINDING cluster_missing: cannot resolve cluster: [Errno 2] No such file or directory: '/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/does-not-exist-r96' | RESULT ERROR | EXIT=2
--bogus-flag: FINDING invalid_arguments: unrecognized arguments: --bogus-flag | RESULT ERROR | EXIT=2
```

### Byte-diff baseline vs delivered (`cmp -s` per captured file)

```text
SAME map-frozen.out      SAME map-r87.out   SAME map-r88.out   SAME map-r89.out
SAME map-r93.out         SAME map-r94.out   SAME map-r95.out
DIFF map-r96.out         DIFF map-selftest.out
SAME map-usage-bogus.out SAME map-usage-missing.out SAME map-usage-noargs.out
SAME support-r87.out     SAME support-r88.out  SAME support-r93.out
SAME support-r94.out     SAME support-r95.out
DIFF support-r96-crossing-response.out
```

Every r87–r95 map run, the frozen replay, and all three usage probes are **byte-identical** pre/post Q1. The only diffs are the two new-content surfaces (r96: `map_missing` → 16/16; self-test: 22 → 24 cases) and the new r96 support receipt.

## 3. r95-pin comparison table

| fixture | r95 pin (seat brief) | delivered | exit | verdict |
|---|---|---|---|---|
| r88-m3-maya-cluster | 10/10, TOTAL 12/12, 0 | `raw=10 mapped=10`; `10/10; 2/2; 12/12`; `RESULT PASS` | 0 | ✓ unchanged |
| r93-m2-kojiki-cluster | 12/12, 0 | `raw=12 mapped=12`; `12/12; 3/3; 15/15`; `RESULT PASS` | 0 | ✓ unchanged |
| r94-paired-crossing | 14/14, 0 | `raw=14 mapped=14`; `14/14; 2/2; 16/16`; `RESULT PASS` | 0 | ✓ unchanged |
| r95-crossing-aftermath | 15/15, 0 | `raw=15 mapped=15`; `15/15; 2/2; 17/17`; `RESULT PASS` | 0 | ✓ unchanged |
| r87-myth-cluster | exit 2 | `unsupported_map: pointer cells must contain one canonical inline-code pointer`; `RESULT ERROR` | 2 | ✓ unchanged |
| r89-inspiration-paraphrase | exit 2 | `unsupported_map: table needs one JSON fact pointer and one source-ID column`; `RESULT ERROR` | 2 | ✓ unchanged |
| r96-crossing-response | 16/16 once Q5 lands | `raw=16 mapped=16`; `16/16; 2/2; 18/18`; `RESULT PASS` | 0 | ✓ landed, as declared |

Cross-check that r96's 16/16 is tool-independent: the extracted r95-revision tool run on the same completed fixture gives the identical `raw=16 mapped=16` / `18/18` / PASS / exit 0. Q5's map declares `**Expected inventory:** 16 JSON facts; 2 editorial rows; 18 total mapped rows; 14 distinct excerpt anchors.`

## 4. `--frozen` r93 replay + independent digest verification

Delivered run: `SNAPSHOT inputs=4 digests=verified` / `FROZEN expected=PASS/0 findings=none matched` / `RESULT PASS` / exit 0 — byte-identical to baseline. I re-hashed all four pinned inputs against `.ufo/waves/round-94/frozen/map-obligations-r93/expected.json` myself:

```text
MATCH entities.json        19f75678dae1b59e6704d1be903a5cecf1b070dd44165e3047bc47efdb8e2d1d
MATCH relations.json       32b79cd4d02793ce4c1f600522fb3810ffdbbad173b5707975fe9197ebf6e46d
MATCH timeline.json        69da079eb29104cf4da04942ec3df79155569aa61d64fec00cb4aa7ffe2417e2
MATCH claim-excerpt-map.md 17f0e8123f26e4f7c534c01a6fe843fe0e8e1278858c0b0ce74623cb7291f7d6
```

`expected.json` pins `exit_code: 0`, `result: PASS`, `finding_ids: []`; the delivered run matched all three.

## 5. support_check receipts r87–r96

Command per fixture: `python3 corpus/tools/support_check.py corpus/fixtures/<dir>`.

Delivered terminal receipt lines (all `RESULT PASS`, exit 0):

```text
r87-myth-cluster      INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 8/8; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 22/22
                      RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 8; TOTAL-ROWS 22
                      SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 8/8; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22; VALIDATED-ROWS 22/22
r88-m3-maya-cluster   INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12; DISTINCT-ANCHORS 8/8
                      SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 2/2; … MODES 12/12; VALIDATED-ROWS 12/12
r93-m2-kojiki-cluster INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15; DISTINCT-ANCHORS 15/15
                      SOURCE-SUPPORT 12/12; EDITORIAL-ANCHORS 3/3; … MODES 15/15; VALIDATED-ROWS 15/15
r94-paired-crossing   INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16; DISTINCT-ANCHORS 12/12
                      SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; … MODES 16/16; VALIDATED-ROWS 16/16
r95-crossing-aftermath INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; DISTINCT-ANCHORS 13/13
                      SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; … MODES 17/17; VALIDATED-ROWS 17/17
r96-crossing-response INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18; DISTINCT-ANCHORS 14/14
                      RECEIPT JSON-FACTS 16; EDITORIAL-ROWS 2; TOTAL-ROWS 18
                      SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; … MODES 18/18; VALIDATED-ROWS 18/18
```

- r87–r95 receipts are **byte-identical** baseline vs delivered (`cmp -s` SAME), and their stdout sha256 values match the r93-era published pins exactly:

```text
r87 952354ac759646a2ee4b0f6c14c8ddf8202bb311d12aff11db8309a23e991b95  (= F17 pin)
r88 b5c4075d65284f3d73cde11bc09b6f3678010474a291705ed3fd7be6830e2e3b  (= F17 pin)
r93 63f90ea53c14708882932dba8eb3c2ced411ea96008d127a86300abc90e7e6da  (= F17 pin)
r94 d0ff69820d619bc5a5350efa96522effcb991f6243588ff3db16a4383ba17e15  (= F17 pin)
r95 efae7be25d213fea277cc1457413e65deb2720a56c20c594aa2a8b40673b9420  (baseline == delivered)
r96 ca7a6815077f87e8e415588a312e3644ccaa44c5fbafb8ed3405a4b53aaf6be1  (new receipt)
```

- r96's receipt (`J16: … 37:> Tick 12: I was at Salt Court through the same agreed bell.` → `MODES 18/18`) is a new receipt, PASS exit 0; nothing was skipped or dropped from the inherited J01–J15/S01–S02 rows.
- `support_check.py` itself is byte-frozen (`git diff dcb2d92 -- corpus/tools/support_check.py` empty; sha256 `55a5eb27…`), so the receipts are a function of frozen checker + frozen fixtures (r87–r95) and the new r96 fixture.

## 6. Supplementary checks (same frozen revision)

- **Self-test 22 → 24.** Delivered (and rerun at 17:51:28 after Q2's contract landed):

```text
SELF-TEST CASES 24/24 pinned
… 24 SELF-TEST PASS lines …
SELF-TEST PASS schema_drift exit=1 findings=['schema_drift']
SELF-TEST PASS inventory_mismatch exit=1 findings=['inventory_mismatch']
RESULT PASS
EXIT=0
```

  Q2's live contract (`97b76bb8…`) holds 24 cases; the delivered capture at 17:50:27 already ran against it (contract mtime 17:50:17). This is C1(b)'s declared change, not a regression; the 22 inherited case IDs all still PASS with the same exits/findings.
- **Determinism.** Two consecutive runs byte-identical: r96 `442f0d1d…` ×2, r88 `8d98f0e6…` ×2.
- **Fixture/tool freeze.** `git diff --stat dcb2d92 -- corpus/fixtures/ corpus/tools/support_check.py` → empty: no tracked fixture byte changed, so the r87–r95 pins run against unmodified inputs. The only tracked tool change is Q1's `map_obligations.py` (plus Q2's contract/README and Q3's new files, untracked/owned by them).
- **No residue/strays.** No `map-obligations-self-test-*` residue at repo root; no V05 writes outside the lane repo (parent tree contains no V05 artifacts).

## 7. Bounds, scope, and non-claims

- I verified only the regression surface: exits/counts/bytes on the seven map fixtures, the frozen r93 replay, usage probes, and support receipts. I did **not** verify C1's new behaviors (deletion-class gating, `dual_pointer`, schema_drift pinning) on their own — those are other seats' claims; my battery only confirms they do not disturb the pins. Q1's declared bounded residuals (§7 of `Q1-tool-hardening.md`: anchor counts receipt-only, dual_pointer bounded to legacy dialect, loose declaration parsing, subset-tolerant self-test, BR-05 scratch location) are consistent with everything I observed.
- The r96 map declares 14 distinct anchors and the frozen `support_check` independently reports `DISTINCT-ANCHORS 14/14`; anchor counting remains support_check's scope.
- Transient Q1 revisions (tries 12–21) were observed and deliberately not treated as deliverables; all results above are on `2b0ba815…` only, re-checked after every phase.
- Nothing in this battery judges entailment, source authenticity, chronology, rights, permission, or canon.

## Bottom line

**PASS** — on the frozen delivered revision (`map_obligations.py` `2b0ba815…`, contract `97b76bb8…`) the full regression battery is green: r88 10/10 + TOTAL 12/12, r93 12/12, r94 14/14, r95 15/15 all `RESULT PASS` exit 0 and byte-identical pre/post Q1; r87/r89 still exit 2 `unsupported_map`; the new r96 fixture lands at `raw=16 mapped=16` / `TOTAL-ROWS 18/18` / PASS exit 0 exactly as declared; `--frozen` r93 replays `digests=verified` + `FROZEN expected=PASS/0 findings=none matched` exit 0 with all 4 pins independently re-hashed; all three usage probes exit 2; all six `support_check` receipts r87–r96 PASS exit 0 with r87–r95 byte-identical (stdout hashes match the r93-era pins `952354ac…`/`b5c4075d…`/`63f90ea5…`/`d0ff6982…`); supplementary self-test is 24/24 pinned exit 0 against the live 24-case contract, with determinism confirmed and zero fixture-byte drift vs `dcb2d92`.
