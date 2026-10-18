# V05 — c1-code-review (round 97)

**Seat:** V05 `c1-code-review` (verifier) · **Wave:** round-97, 64-seat single-wave swarm · **Lane:** lore-shokunin
**Baseline:** r96 closure `f3e09f9` · **Report written:** 2026-10-17 (session date)
**Scope:** after R1 lands, line-by-line review of `git diff f3e09f9 -- corpus/tools/map_obligations.py`:
loader tightening soundness (no case silently skipped; error paths exit 2), `dual_pointer` exposure
matching r96 behavior exactly (no semantic drift), stdlib-only, no live-tree writes; defects by
severity. No other claim (C2/C3, R2 contract wording, fixture content) is verified here.

## 0. Target revision, poll record, freeze

Poll (20 s / 40 tries, `.ufo/waves/round-97/seats/V05-scratch/poll-r1.sh`, condition = tool diff
vs `f3e09f9` **and** R1 report present):

```
poll 5/40  tool_changed=1 r1_report=0 contract_changed=0 18:45:09
poll 16/40 tool_changed=1 r1_report=1 contract_changed=1 18:48:49
READY: R1 tool diff + R1 report present
```

R1's report `.ufo/waves/round-97/seats/R1-map-pinning.md` was present before review began; its
declared hashes verify against the bytes.

| revision | sha256 | note |
|---|---|---|
| reviewed `corpus/tools/map_obligations.py` | `86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9` | md5 `1674d5f28e0a1c3c21f5cf10296515c3`, blob `9509c849db222867896b32bbece568c92086bcba`, 922 lines, mtime 18:45:37, re-hashed unchanged at 18:52 |
| baseline `git show f3e09f9:corpus/tools/map_obligations.py` | `2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8` | equals R1's cited baseline and my frozen copy |
| R2 contract (peer input, not my gate) | `2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41` | 25 cases; `dual_pointer` → exit 1, `["dual_pointer"]` |

```
$ git diff --numstat f3e09f9 -- corpus/tools/map_obligations.py
26	4	corpus/tools/map_obligations.py          (900 → 922 lines, one file)
```

Frozen copies: `V05-scratch/map_obligations_reviewed.py`, `V05-scratch/diff-reviewed.patch`
(76 lines). No commits, no pushes, no network; writes only under `.ufo/waves/round-97/seats/V05-scratch/`
and this report.

## 1. The diff, line-by-line (delivered line numbers)

Six hunks, all confined to test scaffolding, the case list, the loader, and the module docstring:

1. **Docstring (lines 8–11):** documents the fail-closed rule — the contract must pin every
   implemented case, else `--self-test` exits 2 "rather than passing on a subset". Accurate; see §2A.
2. **Line 76:** `ADDED_SELF_TEST_CASES = ("schema_drift", "inventory_mismatch", "dual_pointer")` →
   `SELF_TEST_CASES` (line 77) now holds 25 implemented cases.
3. **Lines 639–646:** `legacy_test_rows()` — the same four obligations as `test_rows()` but as r88
   legacy field-path tokens (`entities[0].first_appearance`, `entities[0].claims[0]`, `relations[0]`,
   `timeline[0]`). Required because `dual_pointer` is only reachable in the legacy dialect.
4. **Line 649:** `DUAL_POINTER_CELL = "`entities[0].first_appearance` (also named
   `entities[1].first_appearance`)"` — first token backticked, second pointer in the prose tail
   (the form r96 V04 established).
5. **Line 652 / 682–683:** `write_test_fixture(..., legacy=False)`; header becomes
   `JSON fact and fields` when `legacy=True`, else the unchanged `JSON fact pointer and fields`.
6. **Lines 732–734:** `prepare_test_case` branch: `dual_pointer` writes the legacy fixture with
   `{0: DUAL_POINTER_CELL}` and returns early.
7. **Line 820:** `missing = sorted(set(SELF_TEST_CASES) - set(expected))` (was
   `set(CORE_SELF_TEST_CASES)`) — the C1(b) tightening.

Emission code is untouched: no hunk intersects `parse_map_text` (326–377 baseline / ~348–399
delivered), `parse_pointer_cell`, `second_pointer_mention`, `compare`, `inventory_*`, `emit`, or the
`--frozen` path. The only runtime-behavior delta is the loader rule and the case list.

## 2. Checklist results

### A. Loader tightening sound — no case silently skipped; error paths exit 2

Static path (`load_test_expectations`, lines 805–821): duplicate IDs, malformed expectations,
unknown IDs (`set(expected) - set(SELF_TEST_CASES)`) and now missing IDs
(`set(SELF_TEST_CASES) - set(expected)`, line 820) all `fail("self_test_contract", …)` →
`ToolError` → caught in `run_self_test` (line 880) → `FINDING self_test_contract` + `RESULT ERROR`
+ return 2. The replay loop's `pinned` list (line 833) is built **after** both set checks, so it
can only ever equal the full 25-case set — no silent subset is reachable.

Dynamic (delivered tool + contract copies, one case dropped/appended per variant;
`V05-scratch/post_checks.py`, outputs in `V05-scratch/post/`):

```
[minus-dual-pointer]        exit=2  FINDING self_test_contract: contract drops implemented self-test cases: dual_pointer        RESULT ERROR
[minus-schema-drift]        exit=2  FINDING self_test_contract: contract drops implemented self-test cases: schema_drift        RESULT ERROR
[minus-inventory-mismatch]  exit=2  FINDING self_test_contract: contract drops implemented self-test cases: inventory_mismatch  RESULT ERROR
[minus-complete-core]       exit=2  FINDING self_test_contract: contract drops implemented self-test cases: complete            RESULT ERROR
[plus-unknown]              exit=2  FINDING self_test_contract: contract pins unimplemented self-test cases: unknown_case        RESULT ERROR
```

Baseline contrast (pre-change gap reproduced on r96 tool + r96 contract copies):

```
$ python3 loader-baseline/one-drop/map_obligations.py --self-test     # contract minus schema_drift
SELF-TEST CASES 23/24 pinned … RESULT PASS                             EXIT=0
$ python3 loader-baseline/tool/map_obligations.py --self-test         # minus schema_drift+inventory_mismatch
SELF-TEST CASES 22/24 pinned … RESULT PASS                             EXIT=0
```

### B. `dual_pointer` exposure matches r96 behavior exactly — no semantic drift

Byte-compare, baseline tool vs delivered tool, on frozen fixture copies (identical bytes fed to
both; `V05-scratch/drift_compare.sh`, `DRIFT_EXIT=0`):

```
IDENTICAL exit=1  frozen-fixtures/dual-ref            (parenthetical dual cell)
IDENTICAL exit=1  frozen-fixtures/dual-ref-colon      (colon-prose dual cell)
IDENTICAL exit=2  frozen-fixtures/r87-myth-cluster
IDENTICAL exit=0  frozen-fixtures/r88-m3-maya-cluster (real legacy-dialect map)
IDENTICAL exit=0  frozen-fixtures/r96-crossing-response
```

Reference emission (baseline, reproduced byte-identically by delivered):

```
$ python3 …/baseline/map_obligations.py dual-ref
OBLIGATIONS raw=4 mapped=4
FINDING dual_pointer: row E2 (line 8) names a second pointer token 'relations[0]' alongside entities.json#/0/claims/0
RESULT FAIL    EXIT=1
```

Self-test output diff, baseline (24-case contract) vs delivered (25-case contract):

```
1c1
< SELF-TEST CASES 24/24 pinned
---
> SELF-TEST CASES 25/25 pinned
25a26
> SELF-TEST PASS dual_pointer exit=1 findings=['dual_pointer']
```

Only the header line and the new case line differ — all 24 inherited cases keep their exits and
finding IDs. Default-path fixture generation is byte-identical too (module-level check importing
both revisions: `entities.json`, `relations.json`, `timeline.json`, `claim-excerpt-map.md` all
IDENTICAL; `test_rows()` equal).

### C. Stdlib-only

AST import sets identical between revisions:
`['argparse','collections','hashlib','json','os','pathlib','re','subprocess','sys','tempfile']`;
no import added by the diff. `python3 -m py_compile corpus/tools/map_obligations.py` → COMPILE OK.

### D. No live-tree writes

```
$ strace -f -e trace=openat,open,unlink,unlinkat,rename,renameat,mkdir,mkdirat \
    -o V05-scratch/strace-self-test.log python3 corpus/tools/map_obligations.py --self-test
EXIT=0 / RESULT PASS
$ grep -E "O_WRONLY|O_RDWR|O_CREAT|O_TRUNC|O_APPEND" strace-self-test.log | grep -v "map-obligations-self-test-"
(no output — 169/169 write-mode opens are under the TemporaryDirectory)
```

No `map-obligations-self-test-*` residue at the repo root after any run; contract sha256 unchanged
(`2142b991…`) after the full battery; the diff adds writes only through `write_test_fixture` into
the per-case scratch cluster (same mechanism as baseline).

### E. Supporting: pin is load-bearing (C1(c), independently reproduced)

Two independent neutralizations of the delivered revision, both re-run to exit 2:

- my variant (`second_pointer_mention` body → `return None`, `V05-scratch/post_checks.py`):
  `SELF-TEST FAIL dual_pointer exit=0 findings=none` … `FINDING self_test_mismatch` / `RESULT ERROR`, exit 2.
- R1's exact scratch copy (`probes/neutralized-live25/…`, `if mention is not None:` → `if False:`),
  re-run by me: 24 × `SELF-TEST PASS`, then `SELF-TEST FAIL dual_pointer exit=0 findings=none`
  (line 26 of `V05-scratch/neutralized-r1-rerun.txt`), `RESULT PASS` (line 28 — the failing case's
  own stdout, printed by the failure diagnostics), `FINDING self_test_mismatch` / `RESULT ERROR`, exit 2.

## 3. Defects by severity

- **BLOCKING / HIGH: none.** The diff is minimal, closes exactly the C1(b) gap, and introduces no
  new failure mode I could find.
- **MEDIUM: none.**
- **LOW-1 (R1 report quote, not the tool):** `R1-map-pinning.md` §3 quotes the neutralized run as
  `SELF-TEST FAIL dual_pointer exit=1 findings=[]`. The actual line is
  `SELF-TEST FAIL dual_pointer exit=0 findings=none` (a nonzero exit cannot carry an empty finding
  list in this tool). Re-run of R1's own scratch copy confirms exit=0/none and outer exit 2; the
  report's conclusion ("the pin is load-bearing") is correct — only the quoted line is wrong.
- **LOW-2 (same family, cosmetic):** `probes.txt` elides long outputs to `first 3 + "…" + last 3`,
  so the neutralized section visually ends `RESULT PASS / FINDING self_test_mismatch / RESULT ERROR`;
  the `RESULT PASS` is the failing case's stdout printed by `run_self_test` diagnostics. Readable
  with care, but easy to misquote — as LOW-1 shows.
- **NOTE-1:** `SELF-TEST CASES 25/25 pinned` is now structurally constant (any missing case fails
  before the print). By design; the counter can no longer surface a partial contract.
- **NOTE-2:** `DUAL_POINTER_CELL` names `entities[1].first_appearance`, an index absent from the
  fixture. Mentions are text-only (never resolved against the JSON), so the case is valid and
  minimal; no action.

## 4. Evidence index (all under `.ufo/waves/round-97/seats/V05-scratch/`)

`baseline/` (pristine f3e09f9 tool+contract), `loader-baseline/` (pre-change gap runs),
`dual-ref/` + `dual-ref-colon/` (emission references), `frozen-fixtures/` (drift inputs),
`post_checks.py` + `post/` (variant battery, `full.txt`), `drift_compare.sh`,
`strace-self-test.log` + `strace-stdout.txt`, `neutralized-r1-rerun.txt`,
`baseline-selftest.txt`, `diff-reviewed.patch`, `map_obligations_reviewed.py`, `poll-r1.sh`.

## 5. Non-claims

I verified the delivered tool revision (`86b52949…`) against the checklist above. I did not verify
R2's contract wording beyond pin presence/shape, R3's `dependency_freeze`, R4/R5/R6 deliverables,
or any entailment/canon/chronology question. The wave was still in flight (R4/R5/R6 artifacts
partially landed) at review time; the reviewed tool revision was stable from 18:45:37 through
report time.

## Bottom line

**PASS** — the R1 diff (26+/4−, `86b52949…`) tightens the loader to fail closed on any dropped
pin (all five drop/unknown variants exit 2; r96 tool still passed the same 23/24-case contract at
exit 0), exposes `dual_pointer` with byte-identical r96 emission on every probed fixture and
inherited case, stays stdlib-only, and performs zero write-mode opens outside its self-test temp
tree; the only defect found is a LOW quote error inside R1's own report (`exit=1 findings=[]` for
the neutralized run; actual `exit=0 findings=none`), which does not affect the tool or the claim.
