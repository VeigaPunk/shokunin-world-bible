# V55 — verdict-crosscheck-calibration (round 95)

Seat: V55 `verdict-crosscheck-calibration`. Scope per seat spec: after V25
lands, independently derive the calibration verdict (round claim C1) from
evidence and compare with V25's verdict. This report was derived from
independent runs on the delivered revision; the V25 comparison section is
filled only from V25's own written report (never from its plan).

Baseline: r94 closure `fb118c4`. Seat scratch declared here:
`.ufo/waves/round-95/seats/V55-scratch/` (extracted baseline tool, mutation
copies, run logs). No writes outside scratch + this report.

## 0. Artifact identities (sha256, all observed)

| Artifact | sha256 |
|---|---|
| `corpus/tools/map_obligations.py` @ `fb118c4` (git-extracted) | `cc1df4dc406870b6fc4ddbc3291e3690cf87dfb061f76ec3b4fec5cfcfbab790` |
| delivered `corpus/tools/map_obligations.py` | `d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108` |
| `corpus/tools/map-obligations-contract.json` @ `fb118c4` | `349a1956714c4496bbd17a00be00e3cd66a173edac015b88fdf10809e8fc7a50` |
| delivered contract | `8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db` |

Delivered-tool hash was stable across a 75 s pre-batch window (`i=13..17`
of my stability loop, 16:26:36–16:27:36) before I ran anything.
`git diff --stat fb118c4` for the two files: tool `142 +--` (138 insertions,
13 deletions incl. hunks), contract `9 +-`. The baseline tool hash matches
V38's independently recorded `cc1df4dc…` and the baseline contract hash
matches V38's `349a1956…`.

## 1. Independent derivation method

Mutation copies built by `.ufo/waves/round-95/seats/V55-scratch/mutate.py`
(plus mut5 inline) from `corpus/fixtures/r94-paired-crossing/`:

- `mut1-rename0-removerow` — entity 0 `claims` → `claim_list` (value content
  preserved by `pop`/reassign), map row ``entities.json#/0/claims/0`` removed
  (the exact BR-02 class).
- `mut2-rename2-removerow` — entity 2 `claims` → `assertions`, row
  ``entities.json#/2/claims/0`` removed (same class, different entity/key —
  for finding-ID stability).
- `mut3-rename0-keeprow` — entity 0 rename, row kept (the r94 mitigation
  direction).
- `mut4-benign-extrakey` — entity 0 gains `"notes": "editorial margin note"`,
  map unchanged (false-positive probe).
- `mut5-rename-firstappearance` — entity 0 `first_appearance` → `first_seen`,
  row ``entities.json#/0/first_appearance`` removed (breadth probe).
- `control-pristine` — unmodified copy.

Old tool extracted with `git show fb118c4:corpus/tools/map_obligations.py`
and run with a sibling copy of the baseline contract
(`.ufo/waves/round-95/seats/V55-scratch/old-tool/`). Delivered tool run from
the repo working tree.

## 2. BEFORE (baseline tool, git bytes) — BR-02 reproduces exactly

```
$ python3 .../old-tool/map_obligations.py .../control-pristine
OBLIGATIONS raw=14 mapped=14 / RESULT PASS / exit=0

$ ... mut1-rename0-removerow
OBLIGATIONS raw=13 mapped=13 / RESULT PASS / exit=0        <- silent PASS

$ ... mut2-rename2-removerow
OBLIGATIONS raw=13 mapped=13 / RESULT PASS / exit=0        <- silent PASS

$ ... mut3-rename0-keeprow
OBLIGATIONS raw=13 mapped=14
FINDING phantom_obligation: entities.json#/0/claims/0 is not a raw source-attributed obligation
RESULT FAIL / exit=1

$ ... mut4-benign-extrakey
OBLIGATIONS raw=14 mapped=14 / RESULT PASS / exit=0

$ ... mut5-rename-firstappearance
FINDING invalid_raw_data: entities.json#/0/first_appearance must contain a non-empty source ID
RESULT ERROR / exit=2
```

The declared before-state is reproduced exactly: the rename+row-removal pair
is silent (exit 0), the kept-row rename is caught only as `phantom_obligation`,
and the `first_appearance` rename was already non-silent (exit 2) — the silent
channel is specific to the `claims` container.

Baseline unchanged-clause receipts (same old-tool run):
`r93 12/12 exit=0`; `r94 14/14 exit=0`; `r87-myth-cluster exit=2
unsupported_map`; `r89-inspiration-paraphrase exit=2 unsupported_map`;
`--self-test` = 20 `SELF-TEST PASS` lines, exit 0, no scratch leftover.

## 3. AFTER (delivered tool) — batch log `V55-scratch/delivered-check.log`

```
mut1: OBLIGATIONS raw=13 mapped=13
      INVENTORY JSON-FACTS 13/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 15/16 MISMATCH
      FINDING schema_drift: entities.json#/0: 1 sourced-claim-shaped record(s) under unexpected key 'claim_list'
      RESULT FAIL / exit=1
mut2: FINDING schema_drift: entities.json#/2: 1 sourced-claim-shaped record(s) under unexpected key 'assertions'
      RESULT FAIL / exit=1
mut3: FINDING phantom_obligation … + FINDING schema_drift …  / RESULT FAIL / exit=1
mut4: RESULT PASS / exit=0      (no false positive on a non-claim-shaped extra key)
mut5: RESULT ERROR / exit=2     (unchanged from baseline)
control-pristine: 14/14, INVENTORY 14/14;2/2;16/16, RESULT PASS / exit=0
```

Stability: mut1 run twice → byte-identical stdout
(`17a8bf6e68f7e010c5b8b9a38f282dd3f6a0c06adf3476aba872606c9b9ec7a1` both
runs); the finding ID `schema_drift` is identical across mut1/mut2 (different
entity, different unexpected key). Exit class is 1 (FAIL), as claimed, not 2.

## 4. Unchanged clauses (delivered tool)

```
r93-m2-kojiki-cluster        12/12  RESULT PASS  exit=0
r94-paired-crossing          14/14  RESULT PASS  exit=0
r87-myth-cluster             FINDING unsupported_map: pointer cells must contain one canonical inline-code pointer
                             RESULT ERROR  exit=2
r89-inspiration-paraphrase   FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column
                             RESULT ERROR  exit=2
r88-m3-maya-cluster          10/10, INVENTORY 10/10;2/2;12/12, RESULT PASS  exit=0  (C3's declared flip)
--frozen .ufo/waves/round-94/frozen/map-obligations-r93
                             SNAPSHOT inputs=4 digests=verified
                             FROZEN expected=PASS/0 findings=none matched
                             RESULT PASS  exit=0
```

Extra fail-closed fixtures (old vs delivered, identical):
`r87-probe-source-prefix` and `r89-c1-multi-cause-valid` both `FINDING
map_missing: expected exactly one conventional claim-to-excerpt map`,
`RESULT ERROR`, exit=2 on both tools.

I independently confirmed the frozen snapshot pins before running it: the
four sha256 values in `.ufo/waves/round-94/frozen/map-obligations-r93/expected.json`
match both the snapshot's own input copies and the live
`corpus/fixtures/r93-m2-kojiki-cluster/` bytes (all four compared, all equal).

Nuance (observed, reported not smoothed): r87's diagnostic detail string
changed between tools (old: "table needs one JSON fact pointer and one
source-ID column"; delivered: "pointer cells must contain one canonical
inline-code pointer"). Exit code 2 and finding ID `unsupported_map` are
unchanged; r89's detail is byte-identical old vs delivered. The round claim
pins "fail-closed behavior", which holds at the exit/finding-ID level.

## 5. Persisted contract and self-test

`python3 corpus/tools/map_obligations.py --self-test` → 22 `SELF-TEST PASS`
lines, 22 PASS, `RESULT PASS`, exit 0, stderr 0 bytes; includes
`SELF-TEST PASS map_missing exit=2 findings=['map_missing']` and
`SELF-TEST PASS invalid_arguments exit=2 findings=['invalid_arguments']`.

Contract JSON: `case_count: 22`; the two new entries are exactly
`{"id": "map_missing", "exit": 2, "finding_ids": ["map_missing"]}` and
`{"id": "invalid_arguments", "exit": 2, "finding_ids": ["invalid_arguments"]}`
— matching the expectation I hand-derived from the baseline tool's code
(`resolve_map` fails with `map_missing`; usage errors emit `invalid_arguments`
via `emit(2, …)`) before reading the persisted values. The tool's
`SELF_TEST_CASES` tuple has the same 22 IDs, and `load_test_expectations`
enforces set-equality with the contract at runtime, so the exit-0 self-test
run itself proves tool/contract agreement. Contract diff vs baseline: only
the `legacy_pointer_dialect` block and the two case entries were added.

## 6. Observed bounds and side effects (evidence, not verdict inputs)

- Drift is bounded to full claim-shaped records (`statement` + `source_id`)
  under unexpected keys of `entities.json` only: mut4 (non-claim-shaped key)
  stays PASS; P1's report §6.3 documents the same bound. This is wider than
  the exact BR-02 class the round claims (rename + row removal), and the
  declared mutation class is fully covered.
- The delivered tool adds an `INVENTORY …` stdout line for maps declaring
  `**Expected inventory:**` (r93/r94/r88 outputs gained one line; counts,
  findings, exits unchanged). r88's round-claim figure "12/12" is the map's
  total row count (10 JSON facts + 2 editorial rows); the tool prints
  `OBLIGATIONS raw=10 mapped=10` and `TOTAL-ROWS 12/12` — both numbers
  labeled, exit 0. Consistent with P1 §6.1.
- BR-05 (scratch under repo root) remains: during concurrent seat runs a
  transient `map-obligations-self-test-*` directory is visible under the repo
  root (I observed two different names at different times). Isolated repeated
  delivered `--self-test` runs (2×, counted before/after) left no leftover,
  and the baseline tool left none; the observed dirs were another seat's
  in-flight scratch, consistent with BR-05's "visible during runs" wording,
  not a new leak.
- Repo footprint after my batch: `git status --short` shows exactly the
  declared producer files (`LOG.md`, tool, contract, README addendum,
  `r95-crossing-aftermath/`, knowledge note) plus `.ufo/waves/round-95/`;
  no unexpected writes.
- Independent full-corpus old-vs-new sweep (my own, not V25's): all 169
  `corpus/fixtures/*` dirs run under both tools comparing `(exit, sorted
  finding IDs)` → `fixture_dirs: 169, changed_count: 1`, the single change
  being `r88-m3-maya-cluster (2, ('unsupported_map',)) → (0, ())`. No fixture
  trips `schema_drift`.
- Independent boundary corroboration of V25's probe matrix: `claims_backup`
  added, nothing removed → old PASS exit 0 / delivered exit 1 `schema_drift`
  (over-detection, conservative); `claims` deleted + row removed → old PASS
  exit 0 / delivered PASS exit 0 + `INVENTORY … MISMATCH` (the residual
  deletion class); `Claims` case rename + row removed → old PASS exit 0 /
  delivered exit 1 `schema_drift`.
- `grep -c schema_drift corpus/tools/map-obligations-contract.json` → `0`:
  the headline behavior is not pinned by any persisted self-test case
  (BR-03 closed for `map_missing`/`invalid_arguments` only).
- The two new persisted expectations are load-bearing (my own perturbations on
  a scratch tool+contract copy): `map_missing` exit `2→0` → `SELF-TEST FAIL
  map_missing` + `FINDING self_test_mismatch`, exit 2; `invalid_arguments`
  finding id → `['bogus_id']` → `SELF-TEST FAIL invalid_arguments` +
  `self_test_mismatch`, exit 2. Expectations are consumed, not regenerated.

## 7. Independent calibration verdict (C1)

| C1 clause | Verdict | Evidence |
|---|---|---|
| Before: rename `claims` key + remove map row → silent PASS exit 0 | confirmed | §2 mut1/mut2 on git-bytes tool |
| After: same class → exit 1 with stable `schema_drift` FINDING | confirmed | §3, ID identical across mut1/mut2, byte-identical repeats |
| Contract persists 22 cases incl. `map_missing`, `invalid_arguments` (20→22) | confirmed | §5, values match pre-reading hand derivation |
| `--self-test` exit 0 | confirmed | §5, 22/22, stderr 0 |
| r93 12/12, r94 14/14 unchanged | confirmed | §4 |
| frozen-r93 digest replay unchanged | confirmed | §4 + independent digest re-verification |
| r87/r89 fail-closed unchanged | confirmed (exit 2 + `unsupported_map`; r87 detail string differs — §4 nuance) | §4 |

## 8. V25 comparison

V25 `verdict-calibration` report (`.ufo/waves/round-95/seats/V25-verdict-calibration.md`,
landed 16:33:24) states **CALIBRATION: PASS (bounded)** on frozen revision
`d1c239cc…`/`8173bb97…` — the same two shas I froze and used — with named
bounds B1–B7. My independent derivation reaches the same verdict on the same
revision. Point-by-point comparison:

| Item | V25 | V55 independent |
|---|---|---|
| Frozen revision | `d1c239cc` / `8173bb97` | same, recorded before running |
| Before: rename + row removal silent PASS exit 0 | entity 0 `claims`→`claimz`, r94 + r95 copies | entity 0 `claim_list`, entity 2 `assertions`, r94 copy |
| After: exit 1 `schema_drift`, stable + deterministic | confirmed | confirmed; byte-identical repeats, same ID across variants |
| 22/22 self-test; contract 22 cases; new entries load-bearing | confirmed; 2 perturbations (`map_missing` exit, `invalid_arguments` id) | confirmed; 2 independent perturbations, same results |
| Regression | 169-fixture sweep: exactly 1 change (r88) | independently reproduced: 169 dirs, exactly 1 change (r88) |
| r87/r89 fail-closed | exit 2 + `unsupported_map`; B5 r87 reason-string change | same; plus `r87-probe-source-prefix` / `r89-c1-multi-cause-valid` byte-identical old vs new |
| B1 drift scope / B2 over-detection | claim-shaped, entities.json only; conservative | corroborated (mut4 PASS; `claims_backup` → exit 1) |
| B3 deletion residual | `claims` deleted + row removed → PASS exit 0 + MISMATCH | corroborated independently |
| B4 drift not self-test-pinned | `grep -c schema_drift` contract = 0 | corroborated: `0` |
| B5 r87 string / B6 r88 denominator | named | observed independently (§4, §6) |
| Verdict | PASS (bounded) | PASS (bounded) |

Differences are additive only: V25 also re-ran `support_check` receipts and
read V01–V04/V16/V02 (outside my seat's scope); V25 did not run my two extra
fail-closed fixtures or the frozen-pin three-way digest check. No shared fact
contradicts between the two derivations; I found no overclaim in V25's report
and no underclaim in my own.

## 9. Bottom line

PASS — C1 calibration independently verified on frozen revision
`d1c239cc…`/`8173bb97…` (silent PASS reproduced on git bytes; delivered exit 1
with stable `schema_drift`; 22/22 self-test with load-bearing new
expectations; 169-fixture sweep shows only the declared r88 change), and the
cross-check against V25 `verdict-calibration` finds no discrepancy: both
derive PASS (bounded) with the same bounds (deletion-variant residual and
drift-not-self-test-pinned reported, not waived).

Bottom line: **PASS** — calibration verdict independently derived and
consistent with V25; all C1 clauses confirmed on the frozen revision with the
named bounds.
