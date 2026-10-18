# V34 — verdict-calibration: C1 (`map_obligations` hardening bundle)

Seat: V34, round 96, lore-shokunin lane. Scope: one CALIBRATION verdict on C1 —
(a) gating inventory mismatch (deletion class), (b) persisted self-test pinning of
`schema_drift` + `inventory_mismatch` (contract 22→24), (c) V37-D1 closed
(dual pointer in legacy-dialect cell → exit 1 `dual_pointer`) — with bounds
(drift scope unchanged).

All commands run from `/home/vgpnk/Projects/shokunin/lore-shokunin`; scratch under
`.ufo/waves/round-96/seats/V34-scratch/` (absolute path). Every mutation ran on scratch
copies; no corpus byte was written by this seat.

**Delivered revision pins (verified, match both producer reports):**

| artifact | sha256 |
|---|---|
| `corpus/tools/map_obligations.py` (Q1) | `2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8` |
| `corpus/tools/map-obligations-contract.json` (Q2) | `97b76bb8b1fea97f166ef7586eba69c427ec15bbe7b34eb5345ec65c936493b6` |
| `corpus/tools/README.md` (Q2) | `965b29cd41a8af14293eb2e1948f58f310e58c6e752b8fe322c5445b20a91f24` |

Baseline for the "before" half: r95 closure `dcb2d92` — tool
`d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108`, contract
`8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db`. Producers Q1
(`Q1-tool-hardening.md`) and Q2 (`Q2-contract-docs.md`) landed complete at 17:47/17:50;
poll-wait observed the tool hash settle at `2b0ba815…` for 15 consecutive 20 s tries before
Q2's contract reached 24 cases (transcript: `V34-scratch/poll.sh` log, tries 21–35).

## VERDICT: PASS (calibration improved, bounded)

C1(a) **improved**: the deletion class now exits 1 with the stable `inventory_mismatch`
FINDING on the identical scratch input that exited 0 at r95, the `INVENTORY` receipt line is
byte-unchanged, and clean/corrected-declaration controls still exit 0 (the gate compares
declaration against observation, it does not punish deletion as such).
C1(b) **improved**: the contract persists 24 expectations including `schema_drift` and
`inventory_mismatch`; `--self-test` runs 24 isolated CLI cases → 24 PASS, 0 FAIL, `RESULT PASS`,
exit 0; flipping either new expectation makes the self-test FAIL exit 2, so both pins are
load-bearing.
C1(c) **improved**: the legacy-dialect hidden-second-pointer cell that exited 0 at r95 now exits
1 with the stable `dual_pointer` FINDING naming row, line, second token, and the token actually
read; all canonical-header and legacy fail-closed forms keep their r95 exits.
Bounds: **drift scope unchanged** — the `claim_shaped`→drift-loop code region is byte-identical
to baseline, and all three functional drift pins reproduce baseline exits/finding text.
No calibration harm found: 7/7 fixture runs, frozen-r93 replay, r87/r89 fail-closed exits, the
0/1/2 exit contract, and the receipts are unchanged; re-runs are byte-identical.

## 1. C1(a) — gating inventory mismatch

Deletion class, exactly as carried: scratch copy of `corpus/fixtures/r95-crossing-aftermath`,
`entities[4].claims` key removed from `entities.json` + map row
`| J10 | … entities.json#/4/claims/0 …` removed.

Baseline `d1c239cc…` (before): `OBLIGATIONS raw=14 mapped=14` / `INVENTORY JSON-FACTS 14/15;
EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/17 MISMATCH` / `RESULT PASS` / exit 0.

Delivered `2b0ba815…`:

```
$ python3 corpus/tools/map_obligations.py .ufo/waves/round-96/seats/V34-scratch/del-demo/cluster
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/17 MISMATCH
FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 15/2/17; observed 14/2/16
RESULT FAIL
EXIT=1
```

Controls and generalization (same revision):

| probe | observed | exit |
|---|---|---|
| untouched fixture copy (control) | `raw=15 mapped=15` / `15/15; 2/2; 17/17` / `RESULT PASS` | 0 |
| deletion **with declaration corrected** 15/2/17→14/2/16 | `raw=14 mapped=14` / `14/14; 2/2; 16/16` / `RESULT PASS` | 0 |
| timeline-event deletion + its row (J15) | `FINDING inventory_mismatch … 15/2/17; observed 14/2/16` / `RESULT FAIL` | 1 |
| editorial-only over-declaration (2→3 rows) | `INVENTORY … EDITORIAL-ROWS 2/3; TOTAL-ROWS 17/18 MISMATCH` / `FINDING inventory_mismatch … 15/3/18; observed 15/2/17` / `RESULT FAIL` | 1 |
| declaration deleted along with the claim+row | `raw=14 mapped=14` / `RESULT PASS` (no declaration → no gate) | 0 |

So the gate is a real declaration-vs-observation comparison (the corrected-declaration control
proves precision), generalizes beyond claims to events and to editorial counts, and its
fail-closed edge (an `**Expected inventory:**` line whose counts cannot be parsed gates with the
same ID, receipt `INVENTORY declaration-malformed`) reproduces exactly as documented:

```
$ python3 corpus/tools/map_obligations.py …/V34-scratch/bound/unparsable   # "see the table below."
INVENTORY declaration-malformed
FINDING inventory_mismatch: map declares an **Expected inventory:** line whose counts cannot be parsed
RESULT FAIL / EXIT=1
```

Off-form but parseable declarations (≥4 integers) compare positionally: matching off-form line →
exit 0; wrong off-form counts → `FINDING inventory_mismatch … 14/2/16; observed 15/2/17` exit 1.

## 2. C1(b) — persisted pinning, 22→24

```
$ python3 corpus/tools/map_obligations.py --self-test
SELF-TEST CASES 24/24 pinned
SELF-TEST PASS schema_drift exit=1 findings=['schema_drift']
SELF-TEST PASS inventory_mismatch exit=1 findings=['inventory_mismatch']
… 24 PASS lines, 0 FAIL …
RESULT PASS          (exit 0)
```

`grep -c '^SELF-TEST PASS'` = 24; `FAIL` = 0. Contract now lists 24 cases
(`97b76bb8…`), including `{"id": "schema_drift", "exit": 1, "finding_ids": ["schema_drift"]}`
and `{"id": "inventory_mismatch", "exit": 1, "finding_ids": ["inventory_mismatch"]}`.

Load-bearing proof (tamper, scratch copy of tool+contract, `V34-scratch/tamper2/`): setting
either new expectation to exit 0 / no findings makes the self-test FAIL both cases and exit 2
(`FINDING self_test_mismatch: isolated CLI outcomes differ from persisted expectations`).
Contract validation also holds: pinning an unimplemented case → exit 2
`FINDING self_test_contract: contract pins unimplemented self-test cases: bogus_case`.

Pinned mutations read from the delivered `prepare_test_case` (`map_obligations.py:713-722`):
`schema_drift` drops the `/claims/0` row and renames entity 0's `claims` container to
`assertions` (content preserved); `inventory_mismatch` runs the **intact** fixture with
`declared=(5, 0, 5, 5)` against 4 observed rows. This matches Q2's disclosed divergence from its
brief ("claims key + its map row removed"): the pinned case achieves the mismatch by
over-declaration, not deletion. I verify the divergence is real and that it is immaterial to
C1(b) as declared (the pinned behaviour is the gating `inventory_mismatch` exit 1 with exact
finding set); the deletion scenario itself is gated and demonstrated in §1.

## 3. C1(c) — V37-D1 closed

Legacy-dialect E4 cell of `corpus/fixtures/r88-m3-maya-cluster` mutated to name a second
pointer in colon-prose: `` `entities[3].claims[0]`: the register locates Evin's south-bell entry
at Salt Court; see also `entities[2].claims[0]` ``.

Baseline: `OBLIGATIONS raw=10 mapped=10` / `INVENTORY … 12/12` / `RESULT PASS` / exit 0
(silently ignored). Delivered:

```
OBLIGATIONS raw=10 mapped=10
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12
FINDING dual_pointer: row E4 (line 30) names a second pointer token 'entities[2].claims[0]' alongside entities.json#/3/claims/0
RESULT FAIL / EXIT=1
```

The row is still read by its first token (no cascading `missing_obligation`); the clean r88 run
is unchanged (`12/12`, `RESULT PASS`, exit 0), and the canonical-header fail-closed forms are
unchanged (r87 `unsupported_map` exit 2, r89 `unsupported_map` exit 2).

## 4. Bounds — drift scope unchanged

Code: the `def claim_shaped` … `def raw_obligations(cluster)` region of the delivered tool is
**byte-identical** to baseline (`V34-scratch/baseline_drift_region.txt` vs delivered extraction →
`IDENTICAL`). Function (baseline → delivered, same scratch inputs):

| probe | baseline | delivered |
|---|---|---|
| entity unexpected key `notes` with claim-shaped records | `FINDING schema_drift: entities.json#/0: 1 sourced-claim-shaped record(s) under unexpected key 'notes'` exit 1 | identical text, exit 1 |
| timeline unexpected key `extra_notes` with claim-shaped records | `RESULT PASS` exit 0 | `RESULT PASS` exit 0 |
| entity unexpected key `tags` with plain strings | `RESULT PASS` exit 0 | `RESULT PASS` exit 0 |

Scope remains entities-only and claim-shaped-only: unchanged, neither widened nor narrowed.

## 5. Non-regression, determinism, boundary

| command | observed | exit |
|---|---|---|
| `… corpus/fixtures/r87-myth-cluster` | `unsupported_map` | 2 |
| `… corpus/fixtures/r88-m3-maya-cluster` | `raw=10 mapped=10` / `12/12` / PASS | 0 |
| `… corpus/fixtures/r89-inspiration-paraphrase` | `unsupported_map` | 2 |
| `… corpus/fixtures/r93-m2-kojiki-cluster` | `raw=12 mapped=12` / `15/15` / PASS | 0 |
| `… corpus/fixtures/r94-paired-crossing` | `raw=14 mapped=14` / `16/16` / PASS | 0 |
| `… corpus/fixtures/r95-crossing-aftermath` | `raw=15 mapped=15` / `17/17` / PASS | 0 |
| `… corpus/fixtures/r96-crossing-response` | `raw=16 mapped=16` / `18/18` / PASS | 0 |
| `… --frozen .ufo/waves/round-94/frozen/map-obligations-r93` | `SNAPSHOT inputs=4 digests=verified` / `FROZEN expected=PASS/0 findings=none matched` / PASS | 0 |

Every line matches the baseline battery captured in this seat before the producers landed
(`V34-scratch/baseline-battery/`), including receipt text. Exit contract 0/1/2 unchanged across
all probes. Re-running the deletion demo and the dual-pointer demo twice each produces
byte-identical output. `git status --short` shows only the producers' declared files modified
(`M corpus/tools/map_obligations.py`, `M corpus/tools/map-obligations-contract.json`,
`M corpus/tools/README.md`, plus Q3/Q4/Q5/Q6 untracked artifacts and the wave-owned `M LOG.md`);
no stray writes from this seat.

Documentation: `corpus/tools/README.md` gained the Round-96 addendum (line 121) documenting both
new gates and the 24-case self-test with before/after quotes; the r95 sentence at line 119 is
retained as history and explicitly superseded at line 144. The documented commands replay as
written (the `--self-test` and fixture commands above).

## 6. Bounds and residuals (verified, not hidden)

1. **Anchor count stays receipt-only.** Declared `99 distinct excerpt anchors` with everything
   else correct → `RESULT PASS` exit 0. `inventory_finding` compares only facts/editorial/total.
2. **Absent declaration → no gate** (`no_declared` probe: exit 0). The gate needs a declaration to
   compare against; this is unchanged from r95 and documented.
3. **Self-test pinning is contract-carried, not self-enforcing against omission.** Removing the
   two new cases from a scratch contract yields `SELF-TEST CASES 22/24 pinned` / `RESULT PASS`
   exit 0 — omission is tolerated but *visible* in the receipt. (Q1 residual §7.4; deliberate
   window-tolerance design.) Flipping or bogusly extending the pins does fail (§2).
4. **`dual_pointer` is legacy-dialect-scoped**; canonical-header cells with a pointer in the note
   stay `unsupported_map` exit 2 (r87/r89 unchanged).
5. **Loose declaration parsing** (≥4 integers → positional compare; <4 → gate as unparsable) is a
   deliberate fail-closed extension beyond the literal "disagrees with observed rows" wording.
6. **BR-05 unchanged**: self-test scratch still under the repository root.
7. **Environment finding (reproduced independently)**: `/tmp` is inode-exhausted
   (`/tmp/v34-run1: No space left on device` on this seat's first determinism attempt; re-run
   under the seat scratch dir). Matches Q1 §7.6 and Q2 §5; closure seats should know.

## 7. Failures / contradictions

None found. The only report-vs-implementation divergence is Q2's self-disclosed
`inventory_mismatch` pinned-case mutation (over-declaration instead of deletion) — verified
accurate and immaterial to C1(b)'s declared behaviour. No claim in C1(a)/(b)/(c) failed
verification; no axis-harm evidence was observed within this seat's scope.

## Bottom line

**PASS** — on the delivered revision (`2b0ba815…` / `97b76bb8…` / `965b29cd…`, both producer
reports' pins matched), the r95 deletion class now exits 1 `inventory_mismatch` (baseline exit 0
on the same input) with the receipt unchanged and clean/corrected-declaration controls still
exit 0; the contract pins 24 cases and `--self-test` is 24/24 PASS exit 0 with both new pins
proven load-bearing by tamper; the V37-D1 legacy hidden-second-pointer cell now exits 1
`dual_pointer` with a stable ID and row/line/token detail; drift scope is code- and
function-identical to baseline, and all fixtures, frozen replay, fail-closed exits, and the
0/1/2 contract are unchanged.
