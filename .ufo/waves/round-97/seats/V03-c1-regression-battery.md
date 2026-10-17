# V03 — c1-regression-battery (round 97)

- Seat: V03 c1-regression-battery. Report path (exclusive): `.ufo/waves/round-97/seats/V03-c1-regression-battery.md`.
- Lane: lore-shokunin, round-97 single wave (64 seats). Baseline: r96 closure `f3e09f9` (HEAD `2393934`).
- Task: full r87–r97 `map_obligations` battery — exits unchanged vs the r96 pins plus r97 17/17, `--frozen` r93 replay, usage probes exit 2, r87/r89 fail-closed. Quote actual commands and observed outputs.
- Writes: only this report and `.ufo/waves/round-97/seats/V03-scratch/` (absolute paths under the lane repo for every write; the lane repo root is `/home/vgpnk/Projects/shokunin/lore-shokunin`). No commits, no pushes, no network, no nested agents.
- Verified revision (frozen bytes, identical at poll hit, before the delivered capture, after it, and at final re-read): `corpus/tools/map_obligations.py` sha256 `86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9`; `corpus/tools/map-obligations-contract.json` `2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41` (25 cases); `corpus/tools/support_check.py` `55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c` (byte-frozen, `git diff f3e09f9 -- corpus/tools/support_check.py` empty); `corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md` `49d4834e124fa6cfaa1a73cd5d1a7bc2cb59711c6233b418fe7485a17eedc94f`; `corpus/fixtures/r96-crossing-response/claim-excerpt-map.md` `e851f068cfd7ed02c97054df18729c4c5a9b8bf60d99d7c9116f427d765440de` (post-repair). Pre-R1 baseline revision: same tool at `2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8` (r96 delivery, re-extracted via `git show f3e09f9:corpus/tools/map_obligations.py` and re-hashed), contract `97b76bb8b1fea97f166ef7586eba69c427ec15bbe7b34eb5345ec65c936493b6` (24 cases).

## 0. Poll-wait evidence (R1)

Poll loop `.ufo/waves/round-97/seats/V03-scratch/poll.sh` (20 s cadence, 40 tries), log `poll.log`. Condition: R1 report present AND tool sha ≠ r96 baseline `2b0ba815…`. Verbatim tail:

```text
POLL_CHECK try=1  tool_sha=2b0ba815… q1_report=absent  r97_map=absent  t=2026-10-17T18:42:51-03:00
POLL_CHECK try=6  tool_sha=2b0ba815… q1_report=absent  r97_map=present t=2026-10-17T18:44:31-03:00
POLL_CHECK try=8  tool_sha=7079515093daf598584d188f1fb27244b6b2c17ca2c51604913dadd122c7af2d  q1_report=absent t=2026-10-17T18:45:11-03:00
POLL_CHECK try=9  tool_sha=61685f3ffa66ba620ae61c48ba231d183b31934932535756664a68ee14e4401a  q1_report=absent t=2026-10-17T18:45:31-03:00
POLL_CHECK try=10 tool_sha=86b52949… q1_report=absent  t=2026-10-17T18:45:51-03:00
POLL_CHECK try=19 tool_sha=86b52949… q1_report=present r97_map=present t=2026-10-17T18:48:51-03:00
POLL_HIT try=19 tool_sha=86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9 report=.ufo/waves/round-97/seats/R1-map-pinning.md r97_map=present
```

Tries 8–9 are transient mid-flight revisions (`70795150…`, `61685f3f…`) and were deliberately **not** treated as deliverables (r95/r96 precedent). All results below are on `86b52949…` only, re-checked at final re-read.

Note on the r97 surface: the r97 fixture directory appeared at try 6, but its map was still a byte copy of the r96 map (title `# r96 crossing-response…`, `**Expected inventory:** 16 JSON facts`) until ~18:48. My delivered capture ran at 18:49:02 against the updated map `49d4834e…` (title `# r97 crossing-acknowledgment`, `17 JSON facts; 2 editorial rows; 19 total mapped rows; 15 distinct excerpt anchors`), sha-verified immediately before and after the capture. The stale r96-copy state is recorded here only as an observation of mid-flight producer state, not as a verified deliverable.

## 1. Pre-R1 baseline (r96 revision `2b0ba815…`), captured 18:42:50 before R1's first write

Full transcript `.ufo/waves/round-97/seats/V03-scratch/baseline/battery.txt`; per-section files in `baseline/sections/`. Verbatim map lines:

```text
map-r87:   FINDING unsupported_map: pointer cells must contain one canonical inline-code pointer | RESULT ERROR | EXIT=2
map-r88:   OBLIGATIONS raw=10 mapped=10 / INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12 / RESULT PASS | EXIT=0
map-r89:   FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column | RESULT ERROR | EXIT=2
map-r93:   OBLIGATIONS raw=12 mapped=12 / INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15 / RESULT PASS | EXIT=0
map-r94:   OBLIGATIONS raw=14 mapped=14 / INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16 / RESULT PASS | EXIT=0
map-r95:   OBLIGATIONS raw=15 mapped=15 / INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17 / RESULT PASS | EXIT=0
map-r96:   OBLIGATIONS raw=16 mapped=16 / INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18 / RESULT PASS | EXIT=0
map-r97:   FINDING cluster_missing: cannot resolve cluster … r97-crossing-acknowledgment | RESULT ERROR | EXIT=2   (fixture not yet landed)
map-frozen: SNAPSHOT inputs=4 digests=verified / OBLIGATIONS raw=12 mapped=12 / INVENTORY … 15/15 / FROZEN expected=PASS/0 findings=none matched / RESULT PASS | EXIT=0
usage:     no-args → invalid_arguments | missing → cluster_missing | --bogus-flag → invalid_arguments | all EXIT=2
self-test: SELF-TEST CASES 24/24 pinned / 24 PASS / RESULT PASS | EXIT=0
```

The r96-revision baseline reproduces every r96 pin exactly (r88 10/10 + 12/12, r93 12/12, r94 14/14, r95 15/15, r96 16/16, r87/r89 exit 2, frozen replay PASS), so the pins are confirmed against the frozen tool revision that produced them before any r97 change.

## 2. Delivered battery (tool `86b52949…`, contract `2142b991…`), captured 18:49:02–04

Full transcript `.ufo/waves/round-97/seats/V03-scratch/delivered/battery.txt`; per-section files in `delivered/sections/`. Command per fixture: `python3 corpus/tools/map_obligations.py corpus/fixtures/<dir>`.

```text
=== map-r87-myth-cluster ===
FINDING unsupported_map: pointer cells must contain one canonical inline-code pointer
RESULT ERROR
EXIT=2

=== map-r88-m3-maya-cluster ===
OBLIGATIONS raw=10 mapped=10
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12
RESULT PASS
EXIT=0

=== map-r89-inspiration-paraphrase ===
FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column
RESULT ERROR
EXIT=2

=== map-r93-m2-kojiki-cluster ===
OBLIGATIONS raw=12 mapped=12
INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15
RESULT PASS
EXIT=0

=== map-r94-paired-crossing ===
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16
RESULT PASS
EXIT=0

=== map-r95-crossing-aftermath ===
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS
EXIT=0

=== map-r96-crossing-response ===
OBLIGATIONS raw=16 mapped=16
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
RESULT PASS
EXIT=0

=== map-r97-crossing-acknowledgment ===
OBLIGATIONS raw=17 mapped=17
INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19
RESULT PASS
EXIT=0
```

### 2.1 Byte-diff baseline vs delivered (`delivered/sections.sha256`, `compare.py`)

```text
SAME  map-frozen-r93.out               exit 0->0  sha 673f7511b9e3 -> 673f7511b9e3
SAME  map-r87-myth-cluster.out         exit 2->2  sha fafe776fcbe5 -> fafe776fcbe5
SAME  map-r88-m3-maya-cluster.out      exit 0->0  sha 8d98f0e6888d -> 8d98f0e6888d
SAME  map-r89-inspiration-paraphrase.out exit 2->2 sha a675c1e7e742 -> a675c1e7e742
SAME  map-r93-m2-kojiki-cluster.out    exit 0->0  sha fd989983414f -> fd989983414f
SAME  map-r94-paired-crossing.out      exit 0->0  sha 099987f28617 -> 099987f28617
SAME  map-r95-crossing-aftermath.out   exit 0->0  sha 4c645d634a5d -> 4c645d634a5d
SAME  map-r96-crossing-response.out    exit 0->0  sha 442f0d1db017 -> 442f0d1db017
DIFF  map-r97-crossing-acknowledgment.out exit 2->0  sha 89eae1a47748 -> 8b387d9a2ffd   (absent -> landed)
DIFF  self-test.out                    exit 0->0  sha 4b9fbb347a2d -> 851fa47f0a21   (24 -> 25 cases)
SAME  support-r87-myth-cluster.out     exit 0->0  sha 952354ac7596 -> 952354ac7596
SAME  support-r88-m3-maya-cluster.out  exit 0->0  sha b5c4075d6528 -> b5c4075d6528
SAME  support-r93-m2-kojiki-cluster.out exit 0->0 sha 63f90ea53c14 -> 63f90ea53c14
SAME  support-r94-paired-crossing.out  exit 0->0  sha d0ff69820d61 -> d0ff69820d61
SAME  support-r95-crossing-aftermath.out exit 0->0 sha efae7be25d21 -> efae7be25d21
SAME  support-r96-crossing-response.out exit 0->0 sha ca7a6815077f -> ca7a6815077f
DIFF  support-r97-crossing-acknowledgment.out  (cluster missing -> landed)
SAME  usage-bogus.out / usage-missing.out / usage-noargs.out  exit 2->2
```

Every r87–r96 map run, the frozen replay, and all three usage probes are **byte-identical** pre/post the round's changes. The only diffs are the new-content surfaces (r97, self-test 24→25) and the two r97 receipts that had no pre-landing counterpart. The r87–r96 support receipts are byte-identical, and their stdout sha256 values match the previously published pins exactly: `952354ac…` (r87), `b5c4075d…` (r88), `63f90ea5…` (r93), `d0ff6982…` (r94), `efae7be2…` (r95), `ca7a6815…` (r96, matches the r96 V05 pin).

### 2.2 r96-pin comparison table

| fixture | r96 pin | delivered | exit | verdict |
|---|---|---|---|---|
| r88-m3-maya-cluster | 10/10, TOTAL 12/12, 0 | `raw=10 mapped=10`; `10/10; 2/2; 12/12`; `RESULT PASS` | 0 | unchanged, byte-identical |
| r93-m2-kojiki-cluster | 12/12, 0 | `raw=12 mapped=12`; `12/12; 3/3; 15/15`; PASS | 0 | unchanged, byte-identical |
| r94-paired-crossing | 14/14, 0 | `raw=14 mapped=14`; `14/14; 2/2; 16/16`; PASS | 0 | unchanged, byte-identical |
| r95-crossing-aftermath | 15/15, 0 | `raw=15 mapped=15`; `15/15; 2/2; 17/17`; PASS | 0 | unchanged, byte-identical |
| r96-crossing-response | 16/16, 0 | `raw=16 mapped=16`; `16/16; 2/2; 18/18`; PASS | 0 | unchanged, byte-identical |
| r97-crossing-acknowledgment | 17/17 declared | `raw=17 mapped=17`; `17/17; 2/2; 19/19`; PASS | 0 | landed as declared |
| r87-myth-cluster | exit 2 | `unsupported_map: pointer cells must contain one canonical inline-code pointer` | 2 | fail-closed, unchanged |
| r89-inspiration-paraphrase | exit 2 | `unsupported_map: table needs one JSON fact pointer and one source-ID column` | 2 | fail-closed, unchanged |

## 3. `--frozen` r93 replay + independent digest verification

Delivered run (byte-identical to baseline):

```text
$ python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93
SNAPSHOT inputs=4 digests=verified
OBLIGATIONS raw=12 mapped=12
INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15
FROZEN expected=PASS/0 findings=none matched
RESULT PASS
EXIT=0
```

I re-hashed all four pinned inputs myself at the final state (not trusting the tool's own `digests=verified` line):

```text
MATCH entities.json        19f75678dae1b59e6704d1be903a5cecf1b070dd44165e3047bc47efdb8e2d1d
MATCH relations.json       32b79cd4d02793ce4c1f600522fb3810ffdbbad173b5707975fe9197ebf6e46d
MATCH timeline.json        69da079eb29104cf4da04942ec3df79155569aa61d64fec00cb4aa7ffe2417e2
MATCH claim-excerpt-map.md 17f0e8123f26e4f7c534c01a6fe843fe0e8e1278858c0b0ce74623cb7291f7d6
```

`expected.json` pins `exit_code: 0`, `result: PASS`, `finding_ids: []`; the delivered run matched all three.

## 4. Usage probes — all exit 2 (byte-identical to baseline)

```text
$ python3 corpus/tools/map_obligations.py
FINDING invalid_arguments: cluster directory is required
RESULT ERROR
EXIT=2

$ python3 corpus/tools/map_obligations.py corpus/fixtures/does-not-exist-r97
FINDING cluster_missing: cannot resolve cluster: [Errno 2] No such file or directory: '…/corpus/fixtures/does-not-exist-r97'
RESULT ERROR
EXIT=2

$ python3 corpus/tools/map_obligations.py --bogus-flag
FINDING invalid_arguments: unrecognized arguments: --bogus-flag
RESULT ERROR
EXIT=2
```

## 5. r87 / r89 fail-closed (unchanged, and shown to be refusals, not path failures)

Both fixtures are **resolvable** clusters — the frozen `support_check.py` reads them fully (control runs at final state):

```text
$ python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 8/8; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS   (exit 0)

$ python3 corpus/tools/support_check.py corpus/fixtures/r89-inspiration-paraphrase
PASS entities.json#/0/claims/0: retelling-support-only; anchor=found; mode=paraphrase; 9:…
RECEIPT JSON-FACTS 1; EDITORIAL-ROWS 0; TOTAL-ROWS 1
RESULT PASS   (exit 0)
```

`map_obligations` nevertheless refuses both with `unsupported_map` (exit 2) and emits **no** `OBLIGATIONS`/`INVENTORY`/`RESULT PASS` line — i.e. it fails closed on map grammars it cannot validate, rather than resolving the path and silently passing. The refusal reasons are visible in the fixtures' own maps: r87's rows pack multiple pointer tokens into one cell (`entities[0].claims[0].statement`, `entities[0].claims[0].source_id`, co-map `entities[0].first_appearance`), which the one-pointer-per-row rule rejects; r89's table header is `Claim pointer | In-world source | …`, which supplies neither a recognized pointer column nor a source-ID column. Both messages and both exit-2 codes are byte-identical to the pre-R1 baseline.

## 6. r97 17/17 — independent cross-check (not the tool's own count)

`V03-scratch/count_obligations.py` counts raw obligations directly from the JSON tables without importing `map_obligations.py` (one per `entities[i].first_appearance`, `entities[i].claims[j]`, `relations[k]`, `timeline[l]`). Sanity: it reproduces the known pins r93=12, r94=14, r95=15, r96=16. On r97:

```text
$ python3 V03-scratch/count_obligations.py corpus/fixtures/r97-crossing-acknowledgment | tail -1
TOTAL=17
```

Extracting the canonical pointer from each JSON-facts row of the delivered r97 map (`49d4834e…`) and comparing with that independent list:

```text
independent obligations: 17
map rows: 17
map pointers == independent set: True
missing from map: [] | extra in map: []
new row: [('J17', 'timeline.json#/5')]
```

So the delivered r97 map's pointer set is exactly the 17 raw obligations (16 inherited + the new `timeline.json#/5` event), and the new event row is `J17`. Supplementary facts on the r97 tables (read-only): `entities=5 relations=1 timeline=6 sources=6`; `entities.json`/`relations.json`/`contradictions.json` byte-identical to r96; the only added source id is `aru-acknowledgment-note`; inherited sources and the first 5 timeline records are byte-identical to r96 (dict-compare `True`).

Receipts for r97:

```text
map_obligations:  OBLIGATIONS raw=17 mapped=17 / INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19 / RESULT PASS / exit 0
support_check:    INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19; DISTINCT-ANCHORS 15/15
                  RECEIPT JSON-FACTS 17; EDITORIAL-ROWS 2; TOTAL-ROWS 19
                  SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 19/19; VALIDATED-ROWS 19/19
                  RESULT PASS / exit 0
```

The map's declared `**Expected inventory:** 17 JSON facts; 2 editorial rows; 19 total mapped rows; 15 distinct excerpt anchors.` agrees with both receipts (anchor counting is `support_check`'s scope and its `DISTINCT-ANCHORS 15/15` line is quoted, not re-derived here).

Determinism (two consecutive runs byte-identical): r97 `8b387d9a2ffdb8b0d9a0b63ee3fffc163b23ad22a6c6a18d294bf9badc0f3fe9` ×2, r88 `8d98f0e6888d875ff52f3690e3415472d8e1c39a22b54f7699409242aa480a77` ×2.

## 7. r96 cosmetic repair is receipt-neutral (C3 repair half, map surface)

`git diff` of the repair (working tree vs `f3e09f9`): exactly 2 insertions / 2 deletions — the editorial-table delimiter row `|---|---|---|---|---|---:|---|---|` → `|---|---|---|---|---:|---|---|`, and the sentence `The new relation encodes only the agreement for this crossing…` → `The new tick-12 event encodes only Evin's second account of the same crossing occasion; it asserts no reconciliation, selects no winner between the accounts, and adds no duty beyond this crossing…`. The 18 data rows (`| J…`, `| S…`) are byte-identical pre/post repair (`DATA ROWS IDENTICAL`; checked by extracting the rows from `git show f3e09f9:…` vs the working tree).

Receipt neutrality, isolated on the unchanged pre-R1 tool (repaired map + `2b0ba815…`) and re-confirmed on the delivered tool:

```text
map-r96     stdout sha256 442f0d1db017a6d3… pre-repair == post-repair (baseline tool), and delivered == baseline
support-r96 stdout sha256 ca7a6815077f87e8… pre-repair == post-repair, and delivered == baseline (= published r96 pin)
```

## 8. Self-test (delivered, live 25-case contract)

```text
SELF-TEST CASES 25/25 pinned
… 25 SELF-TEST PASS lines …
SELF-TEST PASS dual_pointer exit=1 findings=['dual_pointer']
RESULT PASS
EXIT=0
```

The 24 inherited case IDs all still PASS with the same exits/findings; `dual_pointer` is the 25th. C1(b)'s loader tightening (any missing pinned case fails the self-test) and C1(c)'s load-bearing demonstration are R1/R2's and other seats' claims; my battery only establishes that the delivered revision's self-test is green and that the r87–r97 surface it guards did not move.

## 9. Bounds, scope, and non-claims

- I verified only the regression surface: exits, counts, and stdout bytes on the eight map fixtures, the frozen r93 replay, the three usage probes, the self-test header/exit, and the seven support receipts; plus the r97 pointer-set cross-check and the r96 repair's receipt neutrality.
- I did **not** verify C1's or C2's new behaviors on their own (dual_pointer load-bearingness, contract-loader tightening, `dependency_freeze` scope guard / path binding), and I did not judge the r97 prose, anchors beyond `support_check`'s receipt, or any entailment, authenticity, chronology, rights, permission, or canon question.
- Mid-flight revisions (tries 8–9) and the stale r96-copied r97 map were observed and deliberately not treated as deliverables; every number above is on the shas listed in the header, re-checked at final re-read (tool `86b52949…`, contract `2142b991…`, r97 map `49d4834e…`, r96 map `e851f068…`).
- Environment note: `/tmp` is inode-exhausted (`df -i /tmp` → `1048576 1048576 0 100%`, matching the r96 note); two redirects to `/tmp` failed with `No space left on device`, so all capture output was redirected into my scratch dir under the lane repo.
- Writes stayed inside the lane repo: `git status --short` at battery time (18:51) showed `M LOG.md` (wave owner), `M corpus/fixtures/r96-crossing-response/claim-excerpt-map.md` (R4), `M corpus/tools/README.md` + `M corpus/tools/map-obligations-contract.json` (R2), `M corpus/tools/map_obligations.py` (R1), `?? .ufo/waves/round-97/`, `?? corpus/fixtures/r97-crossing-acknowledgment/`. At report time R3's `M corpus/tools/dependency_freeze.py` and R6's `?? corpus/knowledge/r97-acknowledgment-scope-note.md` have also landed (outside my battery's scope); no V03 artifact exists outside its scratch and this report, and a parent-repo sweep (`find /home/vgpnk/Projects/shokunin -maxdepth 2 -name 'V03*'` outside the lane repo) returned nothing.

## Bottom line

**PASS** — on the frozen delivered revision (`map_obligations.py` `86b52949…`, contract `2142b991…`) the full r87–r97 battery is green: r88 10/10 + TOTAL 12/12, r93 12/12, r94 14/14, r95 15/15, r96 16/16 all `RESULT PASS` exit 0 and byte-identical to the pre-R1 baseline; r97 lands at `raw=17 mapped=17` / `TOTAL-ROWS 19/19` / PASS exit 0 with the map's pointer set exactly equal to an independently counted 17 obligations (new row `J17 = timeline.json#/5`); r87/r89 still fail closed at exit 2 `unsupported_map` with no PASS line although both clusters resolve under the frozen `support_check`; `--frozen` r93 replays `digests=verified` + `FROZEN expected=PASS/0 findings=none matched` exit 0 with all four pins independently re-hashed MATCH; all three usage probes exit 2; all seven support receipts r87–r97 PASS exit 0 with r87–r96 byte-identical and matching the published pins; the r96 cosmetic repair is receipt-neutral (data rows byte-identical; map receipt `442f0d1d…` and support receipt `ca7a6815…` unchanged); determinism confirmed; the only diffs vs baseline are the two declared new-content surfaces (r97, self-test 24→25).
