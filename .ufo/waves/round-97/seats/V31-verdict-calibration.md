# V31 — verdict-calibration (round 97, single-wave swarm)

**Seat:** V31 verdict-calibration — read the C1 seats; own the dual-pin + loader demos;
one CALIBRATION verdict with bounds. C1 subject: `corpus/tools/map_obligations.py` (R1)
+ `corpus/tools/map-obligations-contract.json` (R2).

**Repo root for every command:** `/home/vgpnk/Projects/shokunin/lore-shokunin`
(session cwd is the parent repo; all writes used absolute paths under the lane repo
and were verified there). **Baseline:** r96 closure `f3e09f9`.

**Frozen revisions under test** (copied to `V31-scratch/frozen-r97/` before any demo;
all runs below use these copies, never the live files):

```
86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  map_obligations.py        (R1)
2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41  map-obligations-contract.json (R2)
```

Both hashes equal the producers' own reported revisions (R1 §"Delivered revision";
R2 §"Delivered revision under test"). Baseline copies (pre-R1/R2, `git show f3e09f9`-era
live bytes at seat start): tool `2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8`,
contract `97b76bb8b1fea97f166ef7586eba69c427ec15bbe7b34eb5345ec65c936493b6`.

---

## 1. Poll-wait record (protocol compliance)

`V31-scratch/poll.sh` — 20 s cadence, condition: tool changed vs `f3e09f9` **AND** contract
≥25 cases with `dual_pointer` **AND** R1+R2 `.md` reports present. Log `V31-scratch/poll.log`:

```
poll 4 18:44:57 tool_changed=0 contract25=0 r1rep=0 r2rep=0
poll 5 18:45:17 tool_changed=1 contract25=0 r1rep=0 r2rep=0
poll 8 18:46:17 tool_changed=1 contract25=1 r1rep=0 r2rep=0
poll 14 18:48:17 tool_changed=1 contract25=1 r1rep=0 r2rep=1
poll 16 18:48:57 tool_changed=1 contract25=1 r1rep=1 r2rep=1
READY after 16 polls
```

No verification run was taken against a plan or an unreported revision; every delivered-revision
run below postdates READY and ran on the frozen copies. R1 (`R1-map-pinning.md`) and R2
(`R2-contract-docs.md`) were read in full before the demos.

## 2. C1(a) — `dual_pointer` pinned, contract 24→25

```
$ python3 V31-scratch/demos.py V31-scratch/frozen-r97/map_obligations.py \
      V31-scratch/frozen-r97/map-obligations-contract.json V31-scratch/delivered
DELIVERED map_obligations.py sha256=86b52949…
DELIVERED contract sha256=2142b991…
CONTRACT cases n=25 ids=[…, 'map_missing', 'invalid_arguments', 'dual_pointer']
dual_pointer pinned: True
A pristine: 0 ['SELF-TEST CASES 25/25 pinned', 'RESULT PASS'] stderr:
A dual_pointer line: ["SELF-TEST PASS dual_pointer exit=1 findings=['dual_pointer']"]
```

`python3 -m json.tool` on the frozen contract → valid JSON. Diff vs baseline is exactly the
one added line (`git diff --numstat f3e09f9 -- corpus/tools/` → contract `2 1`), the pin being
`{"id": "dual_pointer", "exit": 1, "finding_ids": ["dual_pointer"]}`. The self-test executes the
real CLI per case (subprocess), so the pin is executed, not just parsed.

## 3. C1(b) — loader tightening: ANY missing pinned case now fails

**Baseline (r96 tool `2b0ba815…`, scratch contract copies — reproduces the r96 bound):**

```
$ python3 V31-scratch/drop-inventory/map_obligations.py --self-test | head -2
SELF-TEST CASES 23/24 pinned
SELF-TEST PASS complete exit=0 findings=none
$ python3 V31-scratch/drop-inventory/map_obligations.py --self-test >/dev/null; echo exit=$?
exit=0                      # dropped inventory_mismatch — still green
$ (same with schema_drift dropped)                     → "SELF-TEST CASES 23/24 pinned", exit=0
$ (both r96-added pins dropped, 22/24)                 → "SELF-TEST CASES 22/24 pinned", exit=0
```

**Delivered (frozen tool `86b52949…`) — full sweep, one drop per case, all 25 ids:**

```
$ python3 V31-scratch/demos.py …   # section B
B drop-complete: exit=2 first='FINDING self_test_contract: contract drops implemented self-test cases: complete' names_dropped_case=True
B drop-dual_pointer: exit=2 first='FINDING self_test_contract: contract drops implemented self-test cases: dual_pointer' names_dropped_case=True
… (23 more rows, identical shape; both r96-added pins included)
B sweep: 25 drops, still-green=0 -> []
```

Every drop fails closed with exit 2 **before any case is exercised**, and the finding names the
dropped case. Complementary half of the loader contract (pre-existing, re-probed on the frozen
copy): a contract pinning an unimplemented case also fails closed —

```
$ python3 V31-scratch/add-unknown/map_obligations.py --self-test
FINDING self_test_contract: contract pins unimplemented self-test cases: not_a_case
RESULT ERROR        # exit=2
```

## 4. C1(c) — the pin is load-bearing

Two independent single-sided falsifications of the frozen pair, both using **my own** perturbation
methods (distinct from R1's `if False:` and R2's short-circuit):

**C — neutralized emission** (`second_pointer_mention()`'s return replaced by `return None` in a
tool copy; neutralized sha `21ab92beb9d6b125da2291eded5778263146453d91678c3c4afcd991936d3ebb`):

```
C neutralized (function-body replace): exit=2
   SELF-TEST FAIL dual_pointer exit=0 findings=none
   FINDING self_test_mismatch: isolated CLI outcomes differ from persisted expectations
   RESULT ERROR
```

**D — expectation-flip** (pin kept, `exit` 1→0 and `finding_ids` → `[]` in a contract copy):

```
D flip-dual-pointer: exit=2
   SELF-TEST FAIL dual_pointer exit=1 findings=['dual_pointer']
   FINDING self_test_mismatch: isolated CLI outcomes differ from persisted expectations
   RESULT ERROR
```

Removing the behavior turns the pin red; falsifying the pin turns the run red.

## 5. Independent end-to-end probe (my fixture, not R1's)

My own mutation of the delivered `r88-m3-maya-cluster` legacy map (anchor asserted before
replacement, so no silent no-op), run against the frozen tool:

```
tool sha256: 86b52949…
control:            exit=0 RESULT PASS findings=[]
m1-second-pointer:  exit=1 FINDING dual_pointer: row P1 (line 23) names a second pointer token
                    'entities[0].claims[0]' alongside entities.json#/0/first_appearance
m2-prose:           exit=0 RESULT PASS findings=[]      # "Aru's first mention" — no false positive
```

The pinned expectation (`exit 1`, exactly `['dual_pointer']`) matches real CLI behavior on a
fixture neither producer built, and legitimate prose does not false-fire.

## 6. Non-regression spot battery (frozen tool)

| run | observed |
|---|---|
| `r87-myth-cluster` | exit 2 `unsupported_map` (unchanged) |
| `r88-m3-maya-cluster` | exit 0 `raw=10 mapped=10` / `10/10; 2/2; 12/12` |
| `r89-inspiration-paraphrase` | exit 2 `unsupported_map` (unchanged) |
| `r93-m2-kojiki-cluster` | exit 0 `raw=12 mapped=12` / `12/12; 3/3; 15/15` |
| `r94-paired-crossing` | exit 0 `raw=14 mapped=14` / `14/14; 2/2; 16/16` |
| `r95-crossing-aftermath` | exit 0 `raw=15 mapped=15` / `15/15; 2/2; 17/17` |
| `r96-crossing-response` | exit 0 `raw=16 mapped=16` / `16/16; 2/2; 18/18` |
| `r97-crossing-acknowledgment` | exit 0 `raw=17 mapped=17` / `17/17; 2/2; 19/19` (R5's row landed; R1's first observation of `17/16 missing_obligation` was mid-flight, since resolved) |
| `--frozen .ufo/waves/round-94/frozen/map-obligations-r93` | exit 0, `SNAPSHOT inputs=4 digests=verified` / `FROZEN expected=PASS/0 findings=none matched`; tool sha unchanged pre/post (`86b52949…`) |
| no-args / `--bogus-flag` | exit 2 each (0/1/2 contract intact) |

Path-depth note: the same frozen replay run from the frozen copy's own directory exits 2
`unsafe_path: frozen snapshot must be inside the owning repository` — correct fail-closed behavior
for a copy at a foreign depth, not a regression; relocating the frozen tool to a matching-depth
scratch root reproduces exit 0 with the same receipts.

## 7. Cross-read of the C1 seats

- **R1 (`R1-map-pinning.md`)** and **R2 (`R2-contract-docs.md`)** both report PASS; my independent
  runs agree on every point I re-derived: 25/25 self-test, both r96-added pins now mandatory, the
  new pin load-bearing, battery + frozen replay unchanged. R1's §4.3 pending r97 observation is
  resolved in my §6 (17/17). No contradiction found between the two reports and my evidence.
- R2's hand-derivation (scratch cluster, clean twin exit 0) and R1's fixture both match my §5
  probe's behavior; R2's flag that `SKILL.md`/`corpus/README.md` still say "24 cases" is outside
  C1's byte-ownership and remains an L1 closure-doc item.
- V44 (`c1-negative-2`) was still an unfilled template (10 `__` placeholders) at write time and
  was not used as evidence; V09 (`c2-selftest`) is C2/R3, out of my scope.

## 8. Calibration verdict (with bounds)

**C1 verdict: calibration improved (bounded).** All three sub-claims verify on the delivered
revision, independently of the producers' own demos: (a) `dual_pointer` is persisted case 25 and
executes green (`exit=1 findings=['dual_pointer']`); (b) the subset-tolerant loader is gone — all
25 single-case drops fail closed exit 2 naming the case, where the r96 tool still passed 22–23/24
green; (c) the pin is load-bearing under both a tool-side neutralization and a contract-side
expectation flip. Non-regression: 8 fixtures + frozen replay + usage exits match the r96 pins.

Bounds (named, not netted):

1. **Self-test binds consistency, not truth.** C and D each show a *single-sided* falsification
   fails; a tool+contract edited together consistently (behavior and pin moved in tandem) would
   stay green — inherent to any persisted self-test, not closable by this mechanism.
2. **`dual_pointer` coverage is legacy-dialect-scoped** (documented scope). Probed on the frozen
   tool with asserted anchors on a canonical fixture (`r94-paired-crossing`, cell J01):
   a second **bare field-path token** in the canonical parenthetical passes **silently**
   (`exit=0 RESULT PASS`); a second **`.json#` pointer** exits 2 `unsupported_map` — fail-closed,
   but a different class. The new pin records the legacy emission only; this canonical-dialect
   acceptance is a feature-scope residual, not a C1 regression.
3. **Surviving r96 calibration bound, untouched by C1:** a *consistently regenerated* inventory
   declaration still exits 0 (the gate compares declared vs observed; carried in SCORECARD's r97
   debt list and restated in R2's README addendum).
4. **BR-05 residual (pre-existing, documented as unchanged in r97):** self-test scratch lives under
   the repo root and is not gitignored. Observed live: a transient `map-obligations-self-test-…/`
   entry in `git status` at ~21:50:20Z during concurrent self-test runs, gone on the next check —
   race-window residue of `TemporaryDirectory`, not a stray write by this seat.
5. **Sweep scope:** the 25-drop sweep covers every id in `SELF_TEST_CASES`; loader additions
   (unknown id, repeated id, invalid expectation) were spot-checked, not exhaustively re-derived.

## 9. Hygiene

Writes confined to `V31-scratch/` (frozen copies, poll/demo scripts, logs, probe trees) and this
report; producer files read-only throughout (frozen copies used for every delivered-revision run);
no commits, no pushes, no network, no nested agents. Delivered tool/contract hashes re-checked
after the run batch: unchanged (`86b52949…` / `2142b991…`).

**Bottom line: PASS — C1's three sub-claims verify independently on the frozen delivered revision (`map_obligations.py` `86b52949…` + contract `2142b991…`): `dual_pointer` pinned as case 25, all-25-case drop sweep fails closed where the r96 tool passed 23/24, and the pin is load-bearing under two independent falsifications; bounds recorded (self-test binds consistency not truth; legacy-dialect scope; surviving regenerated-declaration bound; BR-05 scratch residual).**
