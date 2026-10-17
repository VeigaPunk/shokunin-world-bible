# V25 — verdict-calibration (round 95)

- Seat: V25 `verdict-calibration` (leaf verifier). Scope: one CALIBRATION verdict on the
  declared **C1** (schema_drift class closed; 22-case self-test; zero regressions) with named
  bounds, after reading V01–V04 and V16 and running my own BR-02 before/after demo.
- Baseline: r94 closure `fb118c4`. Round: r95, 64-seat single wave, lore-shokunin.
- Frozen verified revision (identical before and after every command below):
  `corpus/tools/map_obligations.py` sha256
  `d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108`,
  `corpus/tools/map-obligations-contract.json` sha256
  `8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db`.
- Scratch: `/tmp/v25-scratch/` (no repo scratch dir declared for this seat); the only repo
  path this seat wrote is this report. No commits, no pushes, no network, no nested agents.
- Poll-wait: P1's tool landed mid-round (9+ intermediate shas while writing; P1 report
  `P1-tool-code.md` + sha stability required before any receipt). V01–V04, V16 were read as
  they landed; V02 (`V02-c1-selftest.md`) landed last and is also read and cross-checked.

## 1. Required reads — V01–V04, V16 (+V02)

| Report | Focus | Frozen revision | Verdict | Key evidence I cross-checked |
|---|---|---|---|---|
| V01 `c1-before-after` | BR-02 on entity 4 (r94), control mutations, fixture sweep | tool `cc1df4dc` (before) / pending after at read time | Phase-1 evidence matches my demo exactly (old tool: rename+drop-row = `raw=13 mapped=13` PASS exit 0; rename-only = phantom exit 1; row-only = missing exit 1) | same before-state on my entity-0 variant |
| V02 `c1-selftest` | self-test 22/22, persisted-vs-printed cross-check, corpus hash invariance | `d1c239cc`/`8173bb97` | PASS, with caveats: `schema_drift` **not** pinned by any persisted case; r88 "12/12" is total rows | I independently reproduced both caveats (§3, §4) |
| V03 `c1-regression` | full regression battery + negative controls | `d1c239cc`/`8173bb97` | PASS; NEG-2 (record *deleted* + row removed) still exit 0 with `INVENTORY … MISMATCH` receipt | my variant D reproduces this bound exactly |
| V04 `c1-negative-rerun` | r94's six negative classes re-run under new tool | `d1c239cc` | PASS: no finding ID changed; only added `INVENTORY` line | my sweep and bounds agree |
| V16 `preservation-mutations` | r95-fixture mutations: span break, row drop, source_id change, rename | `d1c239cc`/`8173bb97` | PASS; old tool silent exit 0 vs delivered `schema_drift` exit 1 on the r95 fixture | my mutA-r95 reproduces this on a different entity |

No contradictions between the five reports and my own receipts; the two nuances they raise
(drift not self-test-pinned; r88 denominator) are confirmed and carried into my bounds.

## 2. My own BR-02 before/after demo (independent scratch)

Old tool extracted from git (not copied from any seat's scratch):

```
$ git show HEAD:corpus/tools/map_obligations.py > /tmp/v25-scratch/map_obligations_OLD.py
$ sha256sum /tmp/v25-scratch/map_obligations_OLD.py
cc1df4dc406870b6fc4ddbc3291e3690cf87dfb061f76ec3b4fec5cfcfbab790
```

Mutation A (the declared class): on a scratch copy, entity 0's `claims` key renamed to
`claimz` with record content preserved, plus removal of its map row `entities.json#/0/claims/0`
(r94 copy row J06; r95 copy same pointer).

```
$ python3 /tmp/v25-scratch/map_obligations_OLD.py /tmp/v25-scratch/mutA          # r94 copy
OBLIGATIONS raw=13 mapped=13
RESULT PASS                                                                     exit=0

$ python3 corpus/tools/map_obligations.py /tmp/v25-scratch/mutA                 # delivered
OBLIGATIONS raw=13 mapped=13
INVENTORY JSON-FACTS 13/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 15/16 MISMATCH
FINDING schema_drift: entities.json#/0: 1 sourced-claim-shaped record(s) under unexpected key 'claimz'
RESULT FAIL                                                                     exit=1

$ python3 /tmp/v25-scratch/map_obligations_OLD.py /tmp/v25-scratch/mutA-r95     # r95 fixture copy
OBLIGATIONS raw=14 mapped=14
RESULT PASS                                                                     exit=0

$ python3 corpus/tools/map_obligations.py /tmp/v25-scratch/mutA-r95             # delivered, run twice
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/17 MISMATCH
FINDING schema_drift: entities.json#/0: 1 sourced-claim-shaped record(s) under unexpected key 'claimz'
RESULT FAIL                                                                     exit=1   (second run byte-identical)
```

So the declared before→after obligation is reproduced on both the r94 and the delivered r95
fixture, with a stable finding ID and deterministic output. Independent reproductions of the
same class by other seats used different entities/keys (P1 `assertions` entity 0; V01
`assertions` entity 4; V02 `claim_rows` entity 0; V16 `assertions` entity 4 on r95).

## 3. Self-test and contract calibration

```
$ python3 corpus/tools/map_obligations.py --self-test
… 22 SELF-TEST PASS lines, 0 FAIL …
SELF-TEST PASS map_missing exit=2 findings=['map_missing']
SELF-TEST PASS invalid_arguments exit=2 findings=['invalid_arguments']
RESULT PASS                                                                     exit=0
```

Contract (22 cases; ids exactly the 22 implemented ones; two new entries):
`{"id": "map_missing", "exit": 2, "finding_ids": ["map_missing"]}` and
`{"id": "invalid_arguments", "exit": 2, "finding_ids": ["invalid_arguments"]}`; AST count of
`SELF_TEST_CASES` = 22.

**Load-bearing check (my own negative control, both new cases).** Copy tool + contract to
`/tmp/v25-scratch/toolcopy2/`, tamper one persisted expectation, run `--self-test`:

```
PERTURB-1: map_missing exit 2 -> 0
  SELF-TEST FAIL map_missing exit=2 findings=['map_missing']
  FINDING self_test_mismatch: isolated CLI outcomes differ from persisted expectations
  exit=2
PERTURB-2: invalid_arguments finding_ids ['invalid_arguments'] -> ['bogus_id']
  SELF-TEST FAIL invalid_arguments exit=2 findings=['invalid_arguments']
  FINDING self_test_mismatch: isolated CLI outcomes differ from persisted expectations
  exit=2
```

Both new expectations are consumed, not regenerated. Same technique as V02 §6; my variant
perturbs the other case and the finding-id field.

**Named bound (B4):** `grep -c schema_drift corpus/tools/map-obligations-contract.json` → `0`.
The headline BR-02 behavior has **no** persisted self-test case (BR-03 is closed for
`map_missing`/`invalid_arguments` only); a regression that removed the drift check would still
print 22/22. The class closure rests on the mutation demo + fixture invariance (V02 §3 agrees).

## 4. Regression evidence on the frozen revision

Fixture sweep (map-bearing fixtures; old tool from git vs delivered):

```
r87-myth-cluster        old exit=2 unsupported_map  → new exit=2 unsupported_map
r88-m3-maya-cluster     old exit=2 unsupported_map  → new exit=0  raw=10 mapped=10, TOTAL-ROWS 12/12
r89-inspiration-paraphrase old exit=2 unsupported_map → new exit=2 unsupported_map
r93-m2-kojiki-cluster   old exit=0 raw=12 mapped=12 → new exit=0 raw=12 mapped=12
r94-paired-crossing     old exit=0 raw=14 mapped=14 → new exit=0 raw=14 mapped=14
r95-crossing-aftermath  (new fixture)                → new exit=0 raw=15 mapped=15
```

Full-corpus old-vs-new diff over **all 169** `corpus/fixtures/*` directories comparing
`(exit code, sorted finding-id list)`: **exactly 1 fixture changed** —
`r88-m3-maya-cluster old=(2, ('unsupported_map',)) new=(0, ())` — the declared C3 improvement.
No other fixture changed, so no fixture trips `schema_drift`.

```
$ python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93
SNAPSHOT inputs=4 digests=verified
OBLIGATIONS raw=12 mapped=12
INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15
FROZEN expected=PASS/0 findings=none matched
RESULT PASS                                                                     exit=0
```

`support_check` receipts unchanged: r93 `SOURCE-SUPPORT 12/12; … MODES 15/15` PASS exit 0;
r94 `14/14; … MODES 16/16` PASS exit 0; r95 `15/15; … MODES 17/17` PASS exit 0; r88
`10/10; … MODES 12/12` PASS exit 0.

**Named bound (B5):** r87 fail-closed holds at the contract level (same ID `unsupported_map`,
same exit 2) but the reason string changed from `table needs one JSON fact pointer and one
source-ID column` to `pointer cells must contain one canonical inline-code pointer` (rejected
one layer deeper by the new dialect gate; V03 §2[4] documented the same).

## 5. Bounds probe matrix (old tool vs delivered, my scratch variants)

| # | Mutation (single class each) | OLD | DELIVERED |
|---|---|---|---|
| A | `claims`→`claimz`, content kept, row removed (**declared BR-02**) | PASS exit 0 silent | **FAIL exit 1 `schema_drift`** |
| A′ | same on r95 fixture copy | PASS exit 0 silent | FAIL exit 1 `schema_drift` |
| B | rename only, map row kept | FAIL exit 1 `phantom_obligation` | FAIL exit 1 `phantom_obligation` + `schema_drift` |
| C | extra claims-shaped key `claims_backup` added, nothing removed | PASS exit 0 | FAIL exit 1 `schema_drift` (over-detection; conservative) |
| D | `claims` key **deleted** + row removed | PASS exit 0 silent | **PASS exit 0** + `INVENTORY … MISMATCH` receipt (not gated) |
| E | `claims`→`Claims` (case rename) + row removed | PASS exit 0 silent | FAIL exit 1 `schema_drift` |
| F | claim `source_id`→`source` | ERROR exit 2 `invalid_raw_data` | ERROR exit 2 `invalid_raw_data` (unchanged) |
| G | timeline `source_id`→`source` | ERROR exit 2 `invalid_raw_data` | ERROR exit 2 `invalid_raw_data` (unchanged) |
| H | renamed key, records lack `statement` (source_id + note only), row removed | PASS exit 0 silent | PASS exit 0 + `INVENTORY … MISMATCH` |
| J | `claims` nested under `entity["meta"]` (dict), top-level key removed, row removed | PASS exit 0 silent | PASS exit 0 + `INVENTORY … MISMATCH` |

End-to-end context on the same mutants: `check_bible` catches the rename regardless
(`VIOLATION: entities[0].claims: required nonempty list` + dangling-entity cascade, exit 1 on
both mutA and mutA-r95); `support_check` catches the dropped row when the map inventory is
left un-restated (exit 1, `inventory total mapped rows mismatch`), but V16 §4 showed a
consistently restated inventory makes `support_check` blind again — the BR-02 blind spot was
map_obligations-specific, and that is the gate this round closes.

## 6. THE CALIBRATION VERDICT (one verdict, on C1)

**CALIBRATION: PASS (bounded).** On the frozen revision `d1c239cc`/`8173bb97`, all three
declared C1 sub-claims verify on my own independent evidence, and every bound below is
evidenced, not inferred:

1. **schema_drift class closed** for the declared mutation class (rename with content
   preserved + row removed): old tool silent `RESULT PASS` exit 0 → delivered exit 1 with the
   stable FINDING ID `schema_drift`, deterministic across runs, on both the r94 and r95
   fixture copies (§2).
2. **22-case self-test** verifies: 22/22 PASS, exit 0, persisted contract with exactly the 22
   implemented ids including `map_missing` and `invalid_arguments`, and both new expectations
   proven load-bearing by my two perturbations (§3).
3. **Zero regressions**: full-corpus diff over 169 fixtures shows exactly the one declared
   r88 change; r87/r89 remain exit 2; r93/r94/r95 and the frozen r93 digest replay remain
   exit 0 with unchanged obligation counts; `support_check` receipts unchanged (§4).

**Named bounds (the calibration does not extend beyond these):**

- **B1 — drift rule scope:** fires only on entities.json top-level entity keys other than
  `claims` whose value is a non-empty list containing records with a non-empty string
  `statement` *and* `source_id`. Not scanned: `relations.json`/`timeline.json` records, nested
  containers, keys whose records lack either field, or an absent `claims` key. Variants H/J/D
  are therefore still silent PASSes (with the `INVENTORY … MISMATCH` receipt visible).
- **B2 — over-detection direction:** any unexpected claims-shaped list fires even when nothing
  is missing (variant C). Conservative by design; no current fixture is affected (169-fixture
  sweep), but a future fixture storing claim-shaped records under another key would exit 1.
- **B3 — residual deletion class (BR-01-adjacent) remains open:** deleting the `claims` key
  and its row (variant D / V03 NEG-2) exits 0; the shortfall is only visible in the
  informational `INVENTORY … MISMATCH` line. Disclosed by P1 §6.3–6.4, V03 §5, V02 §8.4.
- **B4 — the drift class is not pinned by the persisted self-test** (§3); 22/22 does not by
  itself guard against drift-check removal.
- **B5 — r87 reason-string change** under unchanged ID/exit (§4).
- **B6 — r88 "12/12" denominator:** the r88 run reports `OBLIGATIONS raw=10 mapped=10` plus
  `TOTAL-ROWS 12/12`; "12/12" is the map's total row count (10 JSON facts + 2 editorial),
  not an obligation count. Traceable and correctly labeled (C3-level note; agrees with
  V02 §8.1, V03 §3[13], P1 §6.1).
- **B7 — end-to-end scope:** other gates partially overlap this class (`check_bible` catches
  the rename; `support_check` catches an un-restated inventory), so the round's improvement is
  specifically the map-obligation gate no longer passing silently.

No axis is harmed by these bounds; the residuals B3/B4 were disclosed by the producers and by
V02/V03 before this verdict, and are reported, not waived. Mid-flight P1 revisions (crashed
intermediates) were sampled by V03/V04/V16 and are not credited; all receipts above were taken
on the frozen shas, re-verified unchanged after the battery (`d1c239cc…`, `8173bb97…`).

Bottom line: **PASS** — C1 calibration verifies on the frozen revision (BR-02 closed at exit 1
`schema_drift` on my own r94/r95 mutation demos; 22/22 self-test with load-bearing persisted
expectations; 169-fixture diff shows only the declared r88 change), bounded as named: drift
rule covers claim-shaped records under unexpected entity keys only, deletion/nested/shape-lost
variants remain silent-PASS with an informational MISMATCH receipt, and the drift class itself
is not pinned by the persisted self-test.
