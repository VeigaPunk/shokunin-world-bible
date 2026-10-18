# V04 — c1-negative-rerun (round-97)

**Seat:** V04 · **Role:** c1-negative-rerun — re-run the accumulated **nine-class** negative
matrix (unmapped claim, duplicate, phantom, source-ID mismatch, malformed JSON, invalid
path, `schema_drift`, `inventory_mismatch`, `dual_pointer`) on scratch copies under the
**r97 tool**, twice each, and check exit codes + finding-ID stability against the C1 claim
text.
**Subject (delivered):** `corpus/tools/map_obligations.py` sha256
`86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9` (R1 §"Delivered
revision"); snapshot `.ufo/waves/round-97/seats/V04-scratch/map_obligations_r97.py`
sha-identical. Contract `corpus/tools/map-obligations-contract.json` sha256
`2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41` (25 cases, R2).
**Baseline (before):** r96 tool `2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8`
(snapshot `V04-scratch/map_obligations_r96.py`, sha-identical to the r96-closure revision).
**Base subject:** byte copy of `corpus/fixtures/r93-m2-kojiki-cluster` → `V04-scratch/base`
(sorted per-file sha256 tree hash `9de74566782802755a5260a5f02c5c88c389d839ad6ef7a1ce0759aa171ad5d5`),
the same fixture r94 F11, r95 V04 and r96 V06 used, so any finding-ID delta is the tool's,
not the harness's.
**Producer report polled:** `.ufo/waves/round-97/seats/R1-map-pinning.md` (POLL_HIT try=20).

---

## 1. Poll-wait record

Poller `V04-scratch/poll-r1.sh` (20 s cadence, 40-try budget) required **all** of: an
`R1-*.md` report in the seats dir, the tool file, and the contract file; then a 3-consecutive
combined-sha stability gate.

```
POLL_CHECK try=1 t=20s report=none tool=yes
… (tries 2–19, report=none) …
POLL_HIT try=20 report=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats/R1-map-pinning.md
STAB_CHECK i=1 sha=275c2e35b47fc32131be9d5c75c72cc2d353e3eb86169329f14bed185335097c stable=0
STAB_CHECK i=2 sha=275c2e35b47fc32131be9d5c75c72cc2d353e3eb86169329f14bed185335097c stable=1
STAB_CHECK i=3 sha=275c2e35b47fc32131be9d5c75c72cc2d353e3eb86169329f14bed185335097c stable=2
STAB_CHECK i=4 sha=275c2e35b47fc32131be9d5c75c72cc2d353e3eb86169329f14bed185335097c stable=3
POLL_STABLE sha=275c2e35b47fc32131be9d5c75c72cc2d353e3eb86169329f14bed185335097c
```

`275c2e35…` is the sha256 over the concatenated sha256 lines of tool+contract
(`86b52949…` / `2142b991…`). The tool sha moved through three revisions while polling
(`2b0ba815…` r96 → `7079515093da…` → `86b52949…`); **no final run was taken before the
report existed and the sha had been stable for 80 s**.

Observed intermediate revision (context only, no final run taken): `7079515093da…` declared
25 self-test cases but the contract still held 24 and the pre-tightening loader was still in
place — `python3 corpus/tools/map_obligations.py --self-test` → `SELF-TEST CASES 24/25
pinned` … `RESULT PASS` exit 0. That is the r96 tolerance state mid-iteration; the delivered
revision closes it (25/25).

## 2. Method

Harness ported from the r96 V06 seat: `build-cases.py` is a verbatim copy;
`run-cases.sh` / `determinism.sh` have only the scratch path rewritten; `compare.py` is the
verbatim copy **plus** three added boundary expectations (`i5`–`i7`, all exit 1
`dual_pointer`) — noted so no row below is mistaken for a byte-identical inheritor:

| file | sha256 (first 16) | role |
|---|---|---|
| `build-cases.py` | `f6fffdc74251c294` | builds base + 25 case dirs from the r93 byte copy; a–f replicate F11/V04 one-for-one |
| `run-cases.sh` | `ecb67eb3ca91a415` | runs every case **twice**, captures stdout+stderr+exit, prints byte-stability + ID table |
| `compare.py` | `dba667ba1fcdd269` | encodes the expectation table (C1 claim text) and reports MATCH/CHANGED + honest extras |
| `determinism.sh` | `b8fea7eb0121468a` | third pass per case under `PYTHONHASHSEED=0,1,2` |
| `map_obligations_r96.py` | `2b0ba815326b1cb3` | baseline tool (before) |
| `map_obligations_r97.py` | `86b529496214493f` | delivered tool snapshot (after) |
| `map-obligations-contract-r97.json` | `2142b9917694dbec` | delivered contract snapshot |

Case set (26): `base`; `a` unmapped raw claim; `b` duplicate row; `c` phantom pointer;
`d` source-ID mismatch; `e` malformed JSON; `f1`–`f4` invalid path (`map_missing`,
`foreign_path`, traversal `unsafe_path`, map-is-directory `map_missing`); `g1`/`g2`
`schema_drift`; `h1`/`h2` `inventory_mismatch` deletion class; `i1`–`i4` `dual_pointer`
forms; `i5`–`i7` dual-pointer boundary probes; five controls.

Commands (from the lane repo root, after POLL_STABLE):

```
$ python3 .ufo/waves/round-97/seats/V04-scratch/build-cases.py
$ cp corpus/tools/map_obligations.py .ufo/waves/round-97/seats/V04-scratch/map_obligations_r97.py
$ bash .ufo/waves/round-97/seats/V04-scratch/run-cases.sh <abs>/map_obligations_r97.py r97
$ python3 .ufo/waves/round-97/seats/V04-scratch/compare.py r97
$ bash .ufo/waves/round-97/seats/V04-scratch/determinism.sh <abs>/map_obligations_r97.py r97
```

Harness-faithfulness pre-check (before the final runs): the same 26-case harness was run
against the **r96** tool bytes (`label precheck-r96`) and reproduced the r96 V06 §4 table
one-for-one (`VERDICT: ALL-MATCH`), so the ported harness is faithful to the seat it
inherits from.

## 3. Final matrix — nine classes, twice each (label `r97`)

run1 == run2 **byte-identical for all 26 cases** (`grep -c IDENTICAL runs-r97-table.txt` →
`26`). `python3 compare.py r97` → **`VERDICT: ALL-MATCH`** (52/52 pass rows). Required
expectations, exits and IDs:

```
base                   exit=0 findings=[none]
a                      exit=1 findings=[missing_obligation]                  # unmapped raw claim
b                      exit=1 findings=[duplicate_mapping,inventory_mismatch] # duplicate row (+ gate co-fire)
c                      exit=1 findings=[inventory_mismatch,phantom_obligation] # phantom pointer (+ gate co-fire)
d                      exit=1 findings=[source_id_mismatch]
e                      exit=2 findings=[malformed_json]
f1                     exit=2 findings=[map_missing]     # --map missing-map.md
f2                     exit=2 findings=[foreign_path]    # --map outside cluster
f3                     exit=2 findings=[unsafe_path]     # --map ../outside-map/...
f4                     exit=2 findings=[map_missing]     # --map . (directory)
g1                     exit=1 findings=[inventory_mismatch,schema_drift]
g2                     exit=1 findings=[phantom_obligation,schema_drift]
h1                     exit=1 findings=[inventory_mismatch]
h2                     exit=1 findings=[inventory_mismatch]
i1                     exit=1 findings=[dual_pointer]
i2                     exit=1 findings=[dual_pointer]
i3                     exit=1 findings=[dual_pointer]
i4                     exit=1 findings=[dual_pointer,missing_obligation]
i5                     exit=1 findings=[dual_pointer]     # boundary: bare second token, no backticks
i6                     exit=1 findings=[dual_pointer]     # boundary: parenthetical repeats same pointer
i7                     exit=1 findings=[dual_pointer]     # boundary: malformed second token
ctrl-legacy-note       exit=0 findings=[none]
ctrl-legacy-prose      exit=0 findings=[none]
ctrl-canonical-note    exit=2 findings=[unsupported_map]
ctrl-inv-declared-wrong exit=1 findings=[inventory_mismatch]
ctrl-inv-malformed     exit=1 findings=[inventory_mismatch]
```

Representative raw output (run1; run2 identical):

```
$ python3 …/map_obligations_r97.py …/case-a
OBLIGATIONS raw=13 mapped=12
INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15
FINDING missing_obligation: entities.json#/0/claims/1 has no map row
RESULT FAIL
EXIT=1

$ python3 …/map_obligations_r97.py …/case-i1
OBLIGATIONS raw=3 mapped=3
FINDING dual_pointer: row P1 (line 7) names a second pointer token 'relations.json#/0' alongside entities.json#/0/first_appearance
RESULT FAIL
EXIT=1

$ python3 …/map_obligations_r97.py …/case-h1
OBLIGATIONS raw=11 mapped=11
INVENTORY JSON-FACTS 11/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 14/15 MISMATCH
FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 12/3/15; observed 11/3/14
RESULT FAIL
EXIT=1

$ python3 …/map_obligations_r97.py …/case-e
FINDING malformed_json: cannot parse entities.json: Unterminated string starting at: line 27 column 11 (char 558)
RESULT ERROR
EXIT=2
```

Every required class exits exactly as the C1 claim requires (finding classes 1, unparsable /
unsafe inputs 2) with stable FINDING IDs; co-firing `inventory_mismatch` on b/c/g1 and
`missing_obligation` on i4 are the documented r96 interactions (the mutation itself makes
observed rows differ from the declared count, or the second pointer is genuinely unmapped) —
recorded as extras, not failures.

## 4. Stability evidence

**(a) Twice each.** 26/26 cases `IDENTICAL` (byte diff run1 vs run2).

**(b) No behavioural drift vs the r96 tool.** Stripping only the recorded tool-path header
line (`tail -n +2`) from both run trees: **0 / 52 outputs differ** between
`runs-precheck-r96` and `runs-r97`. The nine classes' bodies are byte-identical across the
tool revision — R1's change (self-test case registration + loader tightening) is confined to
`--self-test` behaviour and does not perturb any map-verification path.

**(c) Seed sweep.** `determinism.sh` → 19 classes swept under `PYTHONHASHSEED=0,1,2`,
**19 STABLE, 0 VARIED** (`determinism-r97.txt`), e.g. `b STABLE exit=1
findings=[duplicate_mapping,inventory_mismatch] (seeds 0,1,2)`.

## 5. Relation to the C1 claim (context only — pinning is other seats' scope)

On the delivered revision: `python3 corpus/tools/map_obligations.py --self-test` →
`SELF-TEST CASES 25/25 pinned`, `SELF-TEST PASS dual_pointer exit=1
findings=['dual_pointer']`, `RESULT PASS`, exit 0 (captured `V04-scratch/selftest-r97.out`).
So the `dual_pointer` class my matrix exercises is now also a persisted self-test pin. I do
not adjudicate the loader-tightening or load-bearing probes (R1 §3) — only note that the
delivered revision's nine-class CLI behaviour matches the r96 pins exactly.

**Draft disclosure:** one exploratory run labelled `draft1` was taken against revision
`86b52949…` *before* R1's report landed (same bytes as the delivered revision, by sha). All
numbers quoted above are from the post-POLL_STABLE `r97` runs; `draft1` is retained in
scratch but is not evidence.

## 6. Hygiene / scope

- All writes confined to `.ufo/waves/round-97/seats/V04-scratch/` and this report (absolute
  paths under the lane repo). No commits, no pushes, no network, no nested agents.
- Live shas re-checked **after** all runs: tool `86b52949…`, contract `2142b991…` —
  unchanged from snapshot time.
- No `map-obligations-self-test-*` residue at the repo root after my runs (`ls -d` → none).
- Non-claims: I verified the nine-class CLI matrix, twice each, plus determinism and
  r96-vs-r97 byte-identity on my scratch. I do not judge C2 (`dependency_freeze`), C3
  (fixture content), the self-test contract wording, or any canon/entailment question.

**Bottom line: PASS** — all nine accumulated negative-control classes (unmapped claim,
duplicate, phantom, source-ID mismatch, malformed JSON, invalid path, `schema_drift`,
`inventory_mismatch`, `dual_pointer`) re-run twice each on the delivered r97 revision
(`86b52949…`) exit exactly as the C1 claim requires (1 for finding classes, 2 for
unparsable/invalid) with stable FINDING IDs, byte-identical across runs, across
`PYTHONHASHSEED` 0/1/2, and byte-identical (bodies) to the r96 baseline tool across all 52
outputs.
