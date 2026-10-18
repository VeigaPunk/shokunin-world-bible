# V52 — support-hardening-regression (round 95)

**Seat role:** leaf verifier. Re-run `corpus/tools/support_check.py` on r87 (14+8), r88-m3 (10+2), r93 (12+3), r94 (14+2); confirm the two named silent-failure vectors still fail/warn on scratch demos (header-rename drops rows; unreferenced-row mode flip); demonstrate that the r91-hardening behavior survives the r95 tool work. Report-only on the live tree; all scratch under `.ufo/waves/round-95/seats/V52-scratch/`. No commits, no network.

**Revision under test:** HEAD `fb118c4` (r94 closure). Working tree at final run 16:28–16:29: `M LOG.md`, `M corpus/tools/README.md` (P2, 16:28:26), `M corpus/tools/map-obligations-contract.json` (P2, 16:27:02), `M corpus/tools/map_obligations.py` (P1, 16:26:27); untracked `.ufo/waves/round-95/`, `corpus/fixtures/r95-crossing-aftermath/` (P3/P4), `corpus/knowledge/r95-aftermath-scope-note.md` (P5). Producer reports present at final check (16:29:45): P1, P2, P3, P4, P5.

## 1. Precondition — support_check.py is byte-identical to the r94 baseline

```
$ sha256sum corpus/tools/support_check.py
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py
$ git show fb118c4:corpus/tools/support_check.py | sha256sum
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  -
$ git hash-object corpus/tools/support_check.py ; git rev-parse fb118c4:corpus/tools/support_check.py
a69ae9d27ad1e848c3188fa832352d00b7c0ffc7
a69ae9d27ad1e848c3188fa832352d00b7c0ffc7
```

`git diff --stat -- corpus/fixtures/r87-myth-cluster corpus/fixtures/r88-m3-maya-cluster corpus/fixtures/r93-m2-kojiki-cluster corpus/fixtures/r94-paired-crossing corpus/tools/support_check.py` → **empty**. So the r95 tool work (P1/P2: `map_obligations.py` sha256 `d1c239cc…`, contract `8173bb97…`, README `5d033c9d…`) touched no support_check byte and no pre-existing fixture byte; the survival question is about behavior, demonstrated below. V49's report was not present in `.ufo/waves/round-95/seats/` at my final check (16:29:45); the byte-identity above is my own independent check, not a citation of V49.

## 2. Four required receipts — all PASS, exit 0

Command (cwd = repo root), one per cluster: `python3 corpus/tools/support_check.py corpus/fixtures/<cluster>`

| Cluster | INVENTORY (JSON/editorial/total/anchors) | RECEIPT | Support line | Result | Exit |
|---|---|---|---|---|---|
| r87-myth-cluster | 14/14; 8/8; 22/22; 22/22 | 14 / 8 / 22 | `SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 8/8; … MODES 22/22; VALIDATED-ROWS 22/22` | `RESULT PASS` | 0 |
| r88-m3-maya-cluster | 10/10; 2/2; 12/12; 8/8 | 10 / 2 / 12 | `SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 2/2; … MODES 12/12; VALIDATED-ROWS 12/12` | `RESULT PASS` | 0 |
| r93-m2-kojiki-cluster | 12/12; 3/3; 15/15; 15/15 | 12 / 3 / 15 | `SOURCE-SUPPORT 12/12; EDITORIAL-ANCHORS 3/3; … MODES 15/15; VALIDATED-ROWS 15/15` | `RESULT PASS` | 0 |
| r94-paired-crossing | 14/14; 2/2; 16/16; 12/12 | 14 / 2 / 16 | `SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; … MODES 16/16; VALIDATED-ROWS 16/16` | `RESULT PASS` | 0 |

All match the seat's expected 14+8 / 10+2 / 12+3 / 14+2 exactly; r88 and r94 also report `ANCHORS repeated-references=4` (unchanged from the r94 F33 receipt). Exit codes captured immediately after each python3 invocation (`echo "EXIT=$?"`). Full transcripts: `.ufo/waves/round-95/seats/V52-scratch/receipts/*.out`. These four outputs are byte-identical across three separate runs spanning the producer landing window (sha256 e.g. r87 `952354ac…`, r88 `b5c4075d…`, r93 `63f90ea5…`, r94 `d0ff6982…` in all manifests; final re-run after P2's README landed).

## 3. Silent-failure vector demos (scratch copies)

Builder: `python3 .ufo/waves/round-95/seats/V52-scratch/make_demos.py` (copies the live fixture read-only, asserts each replacement occurs exactly once). Old-tool control: `git show a7c6a17:corpus/tools/support_check.py` → `V52-scratch/support_check_r90.py` (r90-closure tool, sha256 `66a3c4bb…`), run identically.

### 3a. Header-rename drops rows (r87 `| ID | JSON fact and fields |` → `| Row | JSON fact and fields |`, 1 occurrence)

| Tool | Observed | Exit |
|---|---|---|
| r90 baseline tool | `SOURCE-SUPPORT 8/8; … MODES 8/8` / `RESULT PASS` — the 14 JSON rows silently dropped, 8 editorial rows still green | **0** |
| delivered r95 tool | `INVENTORY JSON-FACTS 0/14; EDITORIAL-ROWS 8/8; TOTAL-ROWS 8/22; DISTINCT-ANCHORS 8/22`; 4 `WARN: unreferenced excerpt declaration: …`; `FAIL: inventory JSON facts mismatch: expected=14 parsed=0`; `FAIL: inventory total mapped rows mismatch: expected=22 parsed=8`; `FAIL: inventory distinct excerpt anchors mismatch: expected=22 parsed=8`; `RESULT FAIL` | **1** |

The silent drop is closed exactly as the r91 receipts (JCOV1:50, JCOV4 T1) recorded for the delivered r91 tool.

### 3b. Unreferenced-row mode flip (r88 Spence declaration `verbatim` → `summary`)

The r90-era attack mutated the declaration of `source-excerpt.md`, which at that time no fact row referenced. The r92 map revision turned the Spence comparisons into editorial table rows (S1/S2) that **do** reference `source-excerpt.md`, so two variants were run:

- **Exact single mutation on the current r88 map** (declaration mode cell flipped, nothing else): delivered tool → `FAIL S1/S2: editorial-row; mode=verbatim; excerpt-mode=summary; anchor=found`, `EDITORIAL-ANCHORS 0/2`, `MODES 10/12`, `FAIL: S1/S2: delivery mode missing or mismatched`, `RESULT FAIL`, **exit 1**. No longer silent (the old r90 tool also exits 1 on this current-map shape).
- **r90-era shape reconstruction** (S1/S2 table rows removed, inventory restated `10 JSON facts; 0 editorial rows; 10 total mapped rows; 6 distinct excerpt anchors`, then the same flip): delivered tool → `WARN: unreferenced excerpt declaration: source-excerpt.md (mode=summary)` / `RESULT PASS WITH WARNINGS`, **exit 0**; old r90 tool on the same map → `SOURCE-SUPPORT 10/10; … MODES 10/10` / `RESULT PASS`, **exit 0** (the documented silent pass). Control without the flip: `WARN: unreferenced excerpt declaration: source-excerpt.md (mode=verbatim)` / `RESULT PASS WITH WARNINGS`, exit 0 — the warning fires for the unreferenced declaration and reports its mode, so the flip is visible in the WARN text.

Delivered behavior matches the r91 follow-up receipts exactly (JCOV1:53 `mode=paraphrase` variant; JCOV4 T5 `mode=summary` variant → WARN + `RESULT PASS WITH WARNINGS` exit 0).

Summary matrix (all commands replayable from `V52-scratch/`):

| Demo | r90 tool | delivered r95 tool |
|---|---|---|
| demo1-header-rename | PASS 8/8 exit 0 (silent) | FAIL exit 1 (inventory 0/14) |
| demo2a-mode-flip (current map) | FAIL exit 1 | FAIL exit 1 (S1/S2 mismatch) |
| demo2b-unreferenced-flip (r90 shape) | PASS 10/10 exit 0 (silent) | WARN + PASS WITH WARNINGS exit 0 |
| demo2b-control (no flip) | — | WARN (mode=verbatim) + PASS WITH WARNINGS exit 0 |

All demo outputs are byte-identical across three runs spanning the producer landing window (11/11 hashed outputs equal; manifests `demo-manifest-1/3.txt`). Live-tree protection: sha256 of `r87/…/claim-excerpt-map.md` `3ad4e810…`, `r88/…/claim-excerpt-map.md` `b3b79fe5…`, `support_check.py` `55a5eb27…` identical before and after all demo work.

## 4. Bonus — new r95 fixture receipt (cross-checks C2/C3 support claim)

`python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath` → `INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; DISTINCT-ANCHORS 13/13`; `RECEIPT JSON-FACTS 15; EDITORIAL-ROWS 2; TOTAL-ROWS 17`; `SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; … MODES 17/17; VALIDATED-ROWS 17/17`; `RESULT PASS`, exit 0 (map sha256 `30281ff1…`). P3 (`P3-fixture-json.md` §6b/6d) and P4 (`P4-fixture-docs.md`) report the same receipt independently.

## 5. Bounds and notes

- The r91-era expectation of a *clean WARN on r88* ("r88-m3 10/10 with the single expected unreferenced-declaration WARN", JCOV1:70) no longer applies at r92+: r88's current receipt is `RESULT PASS` with no WARN because the Spence declaration is now referenced by S1/S2. This is the documented r92 map evolution, not a hardening loss — the same flip now fails outright (§3b).
- The two vectors are the r90 attacks hardened by r91 (r91 M4:246 baseline table; JCOV1/JCOV4 delivered receipts); the r94 round re-confirmed only receipts (F33), so these demos are the r95 re-confirmation on the delivered revision.
- Transient observation, not a defect: an untracked `map-obligations-self-test-sxjitx92/` appeared at repo root during the P1/P2 landing window and was gone by 16:28:29 (producer scratch; not mine, not present in the final status).
- Everything else in the round was read-only from this seat; my only writes are this report plus `V52-scratch/`.

**Bottom line: PASS — all four required receipts reproduce exactly on the delivered r95 revision (r87 14+8, r88 10+2, r93 12+3, r94 14+2, all exit 0), both named silent-failure vectors still fail/warn on scratch demos (header-rename → exit 1 inventory FAIL vs r90 silent PASS 8/8; unreferenced flip → WARN `(mode=summary)` exit 0 vs r90 silent PASS 10/10), `support_check.py` is byte-identical to the r94 baseline (sha256 `55a5eb27…`), so the r91-hardening behavior survives the r95 tool work intact.**
