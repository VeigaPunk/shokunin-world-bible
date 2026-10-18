# V01 — c1-deletion-demo (round 96)

Seat: V01 `c1-deletion-demo`. Scope: prove the r95-carried deletion class on the
baseline tool — deleting an entity's `claims` key AND its map row exits 0 with the
shortfall visible only in the non-gating `INVENTORY … MISMATCH` receipt — then prove
the delivered tool makes that inventory mismatch GATING (exit 1, stable
`inventory_mismatch` FINDING), plus single-sided controls (row only / key only) with
each exit reported. Leaf seat: no nested agents, no commits, no pushes, no network.
Writes: this report + declared scratch `.ufo/waves/round-96/seats/V01-scratch/` only.

Baseline: r95 closure `dcb2d92`. All commands run from repo root
`/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3` (2026-10-17).

## Poll outcome

- Target: Q1's `corpus/tools/map_obligations.py` + producer report, per poll-wait
  protocol (20 s cadence, 40 tries). Poller 1 (17:38→17:45, 25 tries) false-fired on
  the directory name `Q1-scratch`; poller 2 with a report-only condition
  (`ls .ufo/waves/round-96/seats/ | grep -E '^Q1.*\.md$'`) reported
  `REPORT-READY attempt=9 hash=2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8 report=Q1-tool-hardening.md`
  at ~17:53. Tool hash `2b0ba815…` observed stable from poller-2 attempt 2 through
  attempt 9 (~2.5 min) before the report landed.
- Q1 report: `.ufo/waves/round-96/seats/Q1-tool-hardening.md`, sha256
  `631b2a6e16b05f1d62d7b8389ff897d2f2ce249864191aa1aca497bf5a8ffdea`, declares the
  same delivered hash `2b0ba815…`, 900 lines, `git diff --numstat` = `115 24`.
- Delivered tool hash re-verified unchanged at the end of every run below (final
  check: `2b0ba815…`); working tree tool at seat start was the baseline
  `d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108` (byte-equal to
  `git show dcb2d92:corpus/tools/map_obligations.py`, the r95-pinned revision).

## Mutation build (scratch only)

Pristine base extracted with
`git archive dcb2d92 corpus/fixtures/r95-crossing-aftermath | tar -x -C …/V01-scratch/old`.
Three variants built by a `python3` heredoc on byte-copies; unified diffs saved as
`V01-scratch/diff-<variant>.txt`:

- `key+row` — `entities.json` entity index 4 (`chalk-stair`): `claims` key deleted;
  map row J10 (`entities.json#/4/claims/0`, `claim-excerpt-map.md` line 31) removed —
  28-line diff, exactly two hunks.
- `row-only` — J10 row removed only (11-line diff).
- `key-only` — `claims` key deleted only (17-line diff).

Key+row second hunk (from `diff-key+row.txt`):

```
@@ -51,12 +51,6 @@
     "id": "chalk-stair",
     "kind": "place",
     "name": "Chalk Stair",
-    "first_appearance": "crossing-minute",
-    "claims": [
-      {
-        "statement": "The crossing minute places Aru and Evin together at the Chalk Stair after both tick-9 entries.",
-        "source_id": "crossing-minute"
-      }
-    ]
+    "first_appearance": "crossing-minute"
```

Note this uses entity 4 / row J10 — a different entity and row than Q1's own demo
(entities[0] / J06), so the two verifications are independent.

## Phase 1 — OLD tool (baseline dcb2d92, sha256 `d1c239cc…`)

Old copy: `git show dcb2d92:corpus/tools/map_obligations.py > V01-scratch/old/map_obligations.py`
(sha256 equal to the working-tree tool at seat start). Raw outputs saved
`V01-scratch/old-<variant>.out` + `.exit`:

```
$ python3 …/V01-scratch/old/map_obligations.py …/old/corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS
exit=0

$ …/old/map_obligations.py …/mutations/key+row
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/17 MISMATCH
RESULT PASS
exit=0

$ …/old/map_obligations.py …/mutations/row-only
OBLIGATIONS raw=15 mapped=14
INVENTORY JSON-FACTS 14/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/17 MISMATCH
FINDING missing_obligation: entities.json#/4/claims/0 has no map row
RESULT FAIL
exit=1

$ …/old/map_obligations.py …/mutations/key-only
OBLIGATIONS raw=14 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
FINDING phantom_obligation: entities.json#/4/claims/0 is not a raw source-attributed obligation
RESULT FAIL
exit=1
```

→ Deletion class reproduced exactly as carried: only the pair (key + row removed) is
silent, exit 0, with the shortfall visible only in the non-gating `INVENTORY … MISMATCH`
receipt line (`JSON-FACTS 14/15`, `TOTAL-ROWS 16/17`). Neither edit alone is silent.

## Phase 2 — NEW tool (delivered, sha256 `2b0ba815…`)

Tool + live contract copied byte-identically into `V01-scratch/new/tool/`
(sha256 checked: tool `2b0ba815…` = delivered; contract copy at that moment
`8173bb97…` = r95's 22-case contract — see self-test note). Runner
`V01-scratch/run-new.sh`; each variant run twice; outputs `new-<variant>-run<1,2>.out`.

```
$ python3 …/new/tool/map_obligations.py …/old/corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS
exit=0

$ …/new/tool/map_obligations.py …/mutations/key+row
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/17 MISMATCH
FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 15/2/17; observed 14/2/16
RESULT FAIL
exit=1

$ …/new/tool/map_obligations.py …/mutations/row-only
OBLIGATIONS raw=15 mapped=14
INVENTORY JSON-FACTS 14/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/17 MISMATCH
FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 15/2/17; observed 14/2/16
FINDING missing_obligation: entities.json#/4/claims/0 has no map row
RESULT FAIL
exit=1

$ …/new/tool/map_obligations.py …/mutations/key-only
OBLIGATIONS raw=14 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
FINDING phantom_obligation: entities.json#/4/claims/0 is not a raw source-attributed obligation
RESULT FAIL
exit=1
```

Exit matrix (both tools, all runs):

| variant | OLD exit | OLD findings | NEW exit | NEW findings |
|---|---:|---|---:|---|
| pristine | 0 | none | 0 | none |
| key+row | 0 | none (receipt MISMATCH only) | 1 | `inventory_mismatch` |
| row-only | 1 | `missing_obligation` | 1 | `inventory_mismatch`, `missing_obligation` |
| key-only | 1 | `phantom_obligation` | 1 | `phantom_obligation` |

Stability and cross-checks (all observed):

- key+row run twice: stdout byte-identical, sha256 `9ff203f6f0abca2e294a300c3a2d7c5f6d8af03aeb3c2b8e859ad6c65b963c2a`
  for both runs; exits 1/1. All four variants: `diff -q run1 run2` empty, identical
  exits. FINDING IDs stable across runs.
- In-place cross-check: `python3 corpus/tools/map_obligations.py …/mutations/key+row`
  → `diff` vs scratch-copy stdout empty, exit 1. The verdict does not depend on the copy.
- Pristine non-regression: NEW pristine stdout byte-identical to OLD pristine stdout
  (both sha256 `4c645d63…`), exit 0 — the gate adds no output on a clean input.
- Live fixture: `python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath`
  → `OBLIGATIONS raw=15 mapped=15` / `INVENTORY … 17/17` / `RESULT PASS`, exit 0.
- Delivered tool hash re-checked after all runs: `2b0ba815…` unchanged.

Self-test (supporting evidence for C1(b), quoted as context — contract is Q2-owned):

- Before Q2's new contract landed (contract then `8173bb97…`, 22 cases):
  `--self-test` → `SELF-TEST CASES 22/24 pinned`, 22 PASS lines, `RESULT PASS`, exit 0
  (subset-tolerant by Q1's design; the two unpinned cases were `schema_drift`,
  `inventory_mismatch`).
- After Q2's 24-case contract landed mid-verification (live sha256 `97b76bb8…`):
  `--self-test` → `SELF-TEST CASES 24/24 pinned`, `SELF-TEST PASS schema_drift exit=1 findings=['schema_drift']`,
  `SELF-TEST PASS inventory_mismatch exit=1 findings=['inventory_mismatch']`,
  24 PASS lines, 0 FAIL, `RESULT PASS`, exit 0. This independently closes Q1's §8
  pending item.

## Boundary notes

- The `key-only` NEW run shows no `inventory_mismatch`: the gate compares the declared
  inventory against observed **map rows** (`15/2/17` observed vs declared), which still
  agree in that variant; the raw-side shortfall surfaces as `phantom_obligation` via the
  unchanged comparison. Reported as observed, not as a defect.
- No corpus file was written by this seat; all writes are under
  `.ufo/waves/round-96/seats/V01-scratch/` plus this report. No commits, no pushes.

## Bottom line

**PASS** — the deletion class reproduces on baseline `d1c239cc…` (key+row → exit 0,
shortfall only in the non-gating `INVENTORY JSON-FACTS 14/15 … TOTAL-ROWS 16/17 MISMATCH`
receipt), and the delivered revision `2b0ba815…` turns the identical mutation into
exit 1 with the stable `FINDING inventory_mismatch` (byte-identical across two runs,
stable ID, in-place == scratch copy); single-sided controls exit 1 under both tools
(row-only additionally gains `inventory_mismatch` on NEW; key-only stays
`phantom_obligation`), the clean input is byte-unchanged (exit 0), and the delivered
revision passes `--self-test` 24/24 pinned against the live contract.
