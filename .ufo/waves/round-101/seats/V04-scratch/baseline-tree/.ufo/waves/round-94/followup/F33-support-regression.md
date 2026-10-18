# F33 — support-hardening-regression

**Seat role:** Re-run `corpus/tools/support_check.py` on the two prior fixtures (`r87-myth-cluster`, `r88-m3-maya-cluster`) on the delivered r94 tree to confirm the r94 additions did not regress prior receipts. LEAF seat; report-only, no corpus edits.

**Tree under test:** HEAD `65a93298cb100fdbf5732ac6de55f01a683c02d8` (follow-up declaration commit; WORK candidate `abbc3e0`, baseline `9c2eea3`). `git status --porcelain` output was empty — working tree clean, so the fixture bytes run below are exactly the committed delivered tree.

---

## 1. r87-myth-cluster — PASS

Command (cwd = repo root):

```
python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster
```

Actual observed output (exact RESULT lines quoted):

```
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 8/8; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 22/22
ANCHORS repeated-references=0; DUPLICATE-ROWS 0
...
RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 8; TOTAL-ROWS 22
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 8/8; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS
```

Process exit code: `EXIT=0`. All 22 per-row checks (E1–E6, R1–R4, T1–T4, H1–H8) reported `PASS ... anchor=found`; the complete transcript was observed in the command output.

Expected counts for this seat were **14 JSON + 8 editorial, PASS** — receipt line `RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 8` and `RESULT PASS` match exactly.

## 2. r88-m3-maya-cluster — PASS

Command:

```
python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster
```

Actual observed output (exact RESULT lines quoted):

```
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12; DISTINCT-ANCHORS 8/8
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
...
RECEIPT JSON-FACTS 10; EDITORIAL-ROWS 2; TOTAL-ROWS 12
SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 12/12; VALIDATED-ROWS 12/12
RESULT PASS
```

Process exit code: `EXIT=0`. All 12 per-row checks (P1–P4, E1–E4, T1–T2, S1–S2) reported `PASS ... anchor=found`.

Expected counts for this seat were **10 + 2, PASS** — receipt line `RECEIPT JSON-FACTS 10; EDITORIAL-ROWS 2` and `RESULT PASS` match exactly.

## 3. Bonus check — r94-paired-crossing (new fixture, same tool) — PASS

Not required by the seat, run because it is free and closes the loop that the checker handles the new fixture too:

```
python3 corpus/tools/support_check.py corpus/fixtures/r94-paired-crossing
```

```
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16; DISTINCT-ANCHORS 12/12
RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 2; TOTAL-ROWS 16
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 16/16; VALIDATED-ROWS 16/16
RESULT PASS
```

Exit code `EXIT=0`; all 16 rows (J01–J14, S01–S02) `anchor=found`. This is consistent with the C1 claim of 14 JSON facts + 2 editorial rows for the new fixture as consumed by this checker.

## 4. Causality check — the r94 diff cannot have changed prior receipts

- `git diff --stat 9c2eea3 abbc3e0 -- corpus/fixtures/r87-myth-cluster corpus/fixtures/r88-m3-maya-cluster corpus/tools/support_check.py` → **empty output** (no changes to either prior fixture or the checker between baseline and checkpoint).
- `git hash-object corpus/tools/support_check.py` → `a69ae9d27ad1e848c3188fa832352d00b7c0ffc7`; `git rev-parse 9c2eea3:...` and `git rev-parse abbc3e0:...` for the same path → identical hash `a69ae9d2...`. The checker binary is byte-identical across baseline, checkpoint, and working tree.
- `git diff --name-status 9c2eea3 abbc3e0 | grep -c -E 'r87-myth-cluster|r88-m3-maya-cluster'` → `0` (no r87/r88 path appears anywhere in the r94 diff).
- All r94 `corpus/` additions are new files only: `A corpus/fixtures/r94-paired-crossing/*` (10 files), `A corpus/knowledge/r94-cross-myth-design-comparison.md`, `A corpus/tools/map-obligations-contract.json`, `A corpus/tools/map_obligations.py` — no deletions or modifications of prior corpus paths.
- `git diff --stat abbc3e0 65a9329` → only `LOG.md` and `README.md` changed (30 insertions), so the follow-up declaration commit itself also touched no fixture or tool bytes.

## Summary table

| Fixture | Expected (seat) | Observed receipt | RESULT | Exit |
|---|---|---|---|---|
| r87-myth-cluster | 14 JSON + 8 editorial, PASS | `RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 8; TOTAL-ROWS 22` | `RESULT PASS` | 0 |
| r88-m3-maya-cluster | 10 + 2, PASS | `RECEIPT JSON-FACTS 10; EDITORIAL-ROWS 2; TOTAL-ROWS 12` | `RESULT PASS` | 0 |
| r94-paired-crossing (bonus) | — | `RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 2; TOTAL-ROWS 16` | `RESULT PASS` | 0 |

**Bottom line: PASS — both prior receipts reproduce exactly on the delivered r94 tree (r87 14+8, r88 10+2, both `RESULT PASS` exit 0), and the diff/hash evidence shows r94 added only new files and left the prior fixtures and `support_check.py` byte-identical, so no regression is possible or observed.**
