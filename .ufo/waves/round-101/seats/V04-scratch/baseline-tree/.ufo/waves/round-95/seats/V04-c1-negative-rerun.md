# V04 — c1-negative-rerun (round-95)

**Seat:** V04 · **Role:** c1-negative-rerun — re-run the r94 round's six negative-control classes on scratch copies under the **new** r95 tool, twice each, and diff the observed finding IDs against r94's recorded baseline.
**Subject:** `corpus/tools/map_obligations.py` at the delivered r95 revision — sha256 `d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108` (byte-identical to the live file at report time; `cmp` → equal). Baseline commit `fb118c4`; r94 tool sha `cc1df4dc406870b6fc4ddbc3291e3690cf87dfb061f76ec3b4fec5cfcfbab790` (= `HEAD`).
**Verdict on the seat claim:** all six classes reproduce the r94 finding IDs exactly, byte-stable across four runs per case; **no finding ID changed**. The only stdout delta is one added `INVENTORY …` line on map-parsing cases, which P1's report discloses (§6.2). No undisclosed change found.

---

## 1. Poll-wait record (protocol compliance)

Targets: P1's tool revision + P1's report `.ufo/waves/round-95/seats/P1-tool-code.md`.
Poller: `.ufo/waves/round-95/seats/V04-scratch/poll-p1.sh` (20 s cadence, 40-try budget). Result: **`READY try=32`** at t≈640 s, `tool_sha=d1c239cc…`, `p1_report=P1-tool-code.md`. The tool sha changed 9 times while P1 iterated (9 distinct new shas: `c37f298b…`, `28d308be…`, `ca05159e…`, `74a88346…`, `8eb5051d…`, `feea13c9…`, `3f87fe8b…`, `9224a684…`, `d1c239cc…`), so no run was taken until the report landed. Live sha re-checked **after** all runs: still `d1c239cc…`.

## 2. Baseline IDs quoted from r94's F11 report

From `.ufo/waves/round-94/followup/F11-c2-negative.md` §3 ("Stability of finding IDs") and §2:

```
base  result=PASS  exit=0 findings=[none]
a     result=FAIL  exit=1 findings=[missing_obligation]     (raw claim, no map row)
b     result=FAIL  exit=1 findings=[duplicate_mapping]      (duplicate map row)
c     result=FAIL  exit=1 findings=[phantom_obligation]     (map row not a raw obligation)
d     result=FAIL  exit=1 findings=[source_id_mismatch]     (map source column differs from raw)
e     result=ERROR exit=2 findings=[malformed_json]         (truncated entities.json)
f1    result=ERROR exit=2 findings=[map_missing]            (nonexistent map file)
f2    result=ERROR exit=2 findings=[foreign_path]           (map outside the cluster)
f3    result=ERROR exit=2 findings=[unsafe_path]            (traversal in --map)
f4    result=ERROR exit=2 findings=[map_missing]            (map path is a directory; F11's extra variant)
```

## 3. Method

- **Base subject:** byte copy of `corpus/fixtures/r93-m2-kojiki-cluster` → `V04-scratch/base` (`diff -r` → `IDENTICAL`) — the same fixture+map F11 used.
- **Cases:** `V04-scratch/build-cases.py` (sha256 `3774c534…`) replicates F11's `build-cases.py` mutations one-for-one (a–f), so a delta would be the tool's, not the harness's.
- **Harness-fidelity control (important):** the same cases were first run with the **r94 tool** saved from `HEAD` (`V04-scratch/map_obligations_r94.py`, sha `cc1df4dc…`) via `run-cases.sh` (sha `25a85f44…`). Result: every ID/exit reproduced F11 exactly, f4 included → my harness is faithful.
- **New-tool runs:** `bash run-cases.sh <tool> <label>`, each case twice, back to back, stdout+stderr+exit captured in `runs-<label>/<case>-run{1,2}.out`.
  - `runs-new` = frozen snapshot taken mid-iteration whose content hash equals the delivered revision (`tool-snap-d1c239cc.py`, sha `d1c239cc…`; `cmp` vs live → equal).
  - `runs-final` = the **live** path `python3 corpus/tools/map_obligations.py <case> …` at the delivered revision.
- Comparison harness `compare.py` (sha `0a416e2b…`) encodes the F11 table above and reports MATCH/CHANGED per case per pass.

## 4. Observed output under the delivered tool (live path, `runs-final`)

```
base  pass1 result=PASS  exit=0 findings=[none]                     pass2 IDENTICAL
a     pass1 result=FAIL  exit=1 findings=[missing_obligation]       pass2 IDENTICAL
b     pass1 result=FAIL  exit=1 findings=[duplicate_mapping]        pass2 IDENTICAL
c     pass1 result=FAIL  exit=1 findings=[phantom_obligation]       pass2 IDENTICAL
d     pass1 result=FAIL  exit=1 findings=[source_id_mismatch]       pass2 IDENTICAL
e     pass1 result=ERROR exit=2 findings=[malformed_json]           pass2 IDENTICAL
f1    pass1 result=ERROR exit=2 findings=[map_missing]              pass2 IDENTICAL
f2    pass1 result=ERROR exit=2 findings=[foreign_path]             pass2 IDENTICAL
f3    pass1 result=ERROR exit=2 findings=[unsafe_path]              pass2 IDENTICAL
f4    pass1 result=ERROR exit=2 findings=[map_missing]              pass2 IDENTICAL
```

`python3 compare.py runs-final` → every line `MATCH`, every stability line `IDENTICAL`, **`VERDICT: ALL-MATCH`**. `runs-new` gives the same ALL-MATCH; snapshot-vs-live captures are byte-identical after dropping the (tool-path) command echo line, i.e. **4 runs per case, all identical**. Representative raw captures:

```
$ python3 corpus/tools/map_obligations.py …/case-a
OBLIGATIONS raw=13 mapped=12
INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15
FINDING missing_obligation: entities.json#/0/claims/1 has no map row
RESULT FAIL
EXIT=1
$ python3 corpus/tools/map_obligations.py …/case-f --map missing-map.md
FINDING map_missing: cannot resolve map: [Errno 2] No such file or directory: '…/case-f/missing-map.md'
RESULT ERROR
EXIT=2
```

Case (c) note: the r93-map phantom (`entities.json#/99/first_appearance`, out of range) still yields exactly `phantom_obligation` (`raw=12 mapped=13`), matching F11 §5.1's documented set-membership semantics — the r95 schema-drift check did not add a second finding here.

## 5. ID changes and disclosure status

**Finding IDs changed: none** (all ten cases, both runs, both subjects).

**Stdout delta vs r94 tool** (`diff <(sed 1d runs-r94control/<c>-run1.out) <(sed 1d runs-new/<c>-run1.out)`): exactly one added line on the five cases that parse a map, none on the four error cases (e, f1–f4):

```
base/a/d:  + INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15
b/c:       + INVENTORY JSON-FACTS 13/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 16/15 MISMATCH
```

**Disclosure:** P1's report discloses this — §1 lists the receipt echo at `corpus/tools/map_obligations.py:223,238,258` and §6.2 states "r93/r94 stdout gained one line … their obligation counts, findings and exits are unchanged"; §6.4 discloses that the declared inventory is echoed, never gated (`MISMATCH` suffix does not change the exit code) — consistent with case-b/c, where the added `MISMATCH` line accompanies unchanged `RESULT FAIL`/`EXIT=1`. **No undisclosed delta found.**

**Context observed (outside my seat's scope, recorded because it corroborates P1 §6.6/§7):** while P2's contract had not yet landed, the live `--self-test` failed closed with `FINDING self_test_contract: contract self-test cases do not match the implemented cases`, `RESULT ERROR`, exactly as P1 §6.6 documents; after P2's contract landed (sha `8173bb97…`), `python3 corpus/tools/map_obligations.py --self-test` → 22 `SELF-TEST` lines, `SELF-TEST PASS map_missing exit=2 findings=['map_missing']`, `SELF-TEST PASS invalid_arguments exit=2 findings=['invalid_arguments']`, `RESULT PASS` (exit 0). That is P1/P2's claim, not this seat's; I did not gate on it.

## 6. Live tree untouched

- All writes confined to `.ufo/waves/round-95/seats/V04-scratch/` (my seat scratch) and this report. No other path written; no commits, no pushes, no network.
- `git status --porcelain` after all runs shows only other seats' work: ` M LOG.md`, ` M corpus/tools/map-obligations-contract.json`, ` M corpus/tools/map_obligations.py`, `?? .ufo/waves/round-95/`, `?? corpus/fixtures/r95-crossing-aftermath/`, `?? corpus/knowledge/r95-aftermath-scope-note.md`. Nothing from V04.
- Delivered-revision sha re-checked after all runs (`d1c239cc…`) — the subject did not move under me.

**Bottom line: PASS — all six r94 negative-control classes (a–f, f4 extra) reproduce the exact F11 baseline finding IDs and exit codes on scratch copies under the delivered r95 tool, byte-stable across four runs each; the only stdout delta is the disclosed `INVENTORY` line, and no finding ID changed.**
