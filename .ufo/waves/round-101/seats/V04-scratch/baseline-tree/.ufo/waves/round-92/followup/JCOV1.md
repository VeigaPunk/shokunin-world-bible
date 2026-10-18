# JCOV1 — receipts judge (round-92 FOLLOW-UP)

Judgment surface: committed tree `c4d4823` (baseline `396c568`); tree clean at judgment
start. Axes named: (1) receipt fidelity — stated numbers reproduce exactly; (2) contract
behavior — exit codes and terminal summaries on failure paths; (3) no-harm — positive
receipts unchanged vs baseline. All scratch under `/tmp/jcov1` (removed; `ls` → "No such
file or directory"; `df -i /tmp` was 99% full, ≤3 probe files live at once).

## Work performed

- Re-ran every receipt family named in the JCOV1 block on the committed tree, cwd `lore-shokunin/`:
  1. r87 regression receipt — `python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster`
  2. r88-m3 coverage receipt (Spence rows + WARN closure) — same command, r88-m3 cluster
  3. paraphrase demo — same command, r89 cluster
  4. M2 contract — 15-probe failure-path battery (all exit codes + terminal `RESULT`
     lines captured; stdout/stderr separated)
- Baseline controls from scratch only: `git show 396c568:corpus/tools/support_check.py`
  (sha256 `9da149b8…`, vs delivered `55a5eb27…`) plus `git show 396c568:…claim-excerpt-map.md`
  for r87/r88 as control maps. Controls: B1 baseline checker+baseline map; B2 delivered
  checker+baseline map; B3 baseline checker+missing-inventory map; B4 baseline checker+missing
  cluster; plus byte-parity diff of baseline vs delivered checker output on all three fixtures.
- Checker-pin re-verification: `sha256sum` of `corpus/fixtures/check_bible.py` and
  `corpus/tools/support_check.py`, `git log` per path, and `git show 396c568:<path> | sha256sum`.
- Freeze check: 2×60 s re-verification that HEAD/tracked tree did not move during judgment.
- No repo writes except this file; no commit/push; no sibling repos touched.

## Before → after measurements

**Positive receipts (delivered tree, exit codes via `echo exit=$?` after each run).**

```text
$ python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 8/8; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 22/22
RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 8; TOTAL-ROWS 22
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 8/8; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS
exit=0
```

```text
$ python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12; DISTINCT-ANCHORS 8/8
RECEIPT JSON-FACTS 10; EDITORIAL-ROWS 2; TOTAL-ROWS 12
SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 12/12; VALIDATED-ROWS 12/12
RESULT PASS
exit=0
```

No `WARN` line in the r88-m3 output (the row lines S1/S2 both `PASS … editorial-row; mode=verbatim; anchor=found; 5:> …`).

```text
$ python3 corpus/tools/support_check.py corpus/fixtures/r89-inspiration-paraphrase
INVENTORY JSON-FACTS 1/1; EDITORIAL-ROWS 0/0; TOTAL-ROWS 1/1; DISTINCT-ANCHORS 1/1
PASS entities.json#/0/claims/0: retelling-support-only; anchor=found; mode=paraphrase; 9:A modern paraphrase says …
SOURCE-SUPPORT 0/0; EDITORIAL-ANCHORS 0/0; RETELLING-SUPPORT-ONLY 1 entries (1/1 anchors); MODES 1/1; VALIDATED-ROWS 1/1
RESULT PASS
exit=0
```

**WARN closure before → after (controls).**

- B1 baseline checker + baseline r88 map: `RESULT PASS WITH WARNINGS`,
  `WARN: unreferenced excerpt declaration: source-excerpt.md (mode=verbatim)`, exit 0.
- B2 delivered checker + baseline r88 map: same WARN, exit 0 → the WARN machinery is
  intact; the closure is map-side (the committed map gained the two Spence rows).
- After (delivered checker + delivered map): no WARN, `RESULT PASS`, exit 0 (above).
- Byte-parity of baseline vs delivered checker stdout on all three fixtures:
  `PARITY r87…/r88…/r89… baseline_exit=0 delivered_exit=0 diff_lines=0` (three runs).

**M2 contract battery (15 probes; each from committed maps, mutated in /tmp, checker run
against the committed cluster).** Observed `exit=` and terminal line:

| probe | mutation | exit | terminal |
|---|---|---|---|
| P1 | no args | 2 | RESULT ERROR |
| P2 | cluster dir missing | 2 | RESULT ERROR |
| P3 | `--map` missing | 2 | RESULT ERROR |
| P4 | `--map` is a directory | 2 | RESULT ERROR |
| P5 | inventory line deleted (`sed '7d'`, r87 map) | 1 | RESULT FAIL |
| P6 | inventory line malformed (`14` → `fourteen`) | 1 | RESULT FAIL |
| P7 | inventory line duplicated (`sed '7p'`) | 1 | RESULT FAIL |
| P8 | totals inconsistent (`22` → `21` total rows) | 1 | RESULT FAIL |
| P9 | table row cell-count mismatch (`\| S1 \| malformed \|`, r88 map) | 2 | RESULT ERROR |
| P10 | fact row with empty anchor (1-row handcrafted map) | 2 | RESULT ERROR |
| P11 | fact table outside JSON-facts/Editorial heading | 2 | RESULT ERROR |
| P12 | source anchor missing (`I am Hara…` → sentinel) | 1 | RESULT FAIL |
| P13 | excerpt path missing (`gate-witness-excerpt.md:7` → `missing-excerpt.md:7`) | 1 | RESULT FAIL |
| P14 | map unreadable (`chmod 000`) | 2 | RESULT ERROR |
| P15 | map invalid UTF-8 | 2 | RESULT ERROR |

All 15 printed exactly one terminal `RESULT` line (stdout). Representative stderr details:
P5 `FAIL: map must contain exactly one expected inventory declaration`; P9 `FAIL: map table
row has a different number of cells than its header`; P14 `FAIL: [Errno 13] Permission
denied`; P15 `FAIL: 'utf-8' codec can't decode byte 0xff…`. P12/P13 (row-level failures)
leave stderr empty — their `FAIL:` detail lines are on stdout, with `RESULT FAIL`.

**Exit alignment vs baseline (controls).** B3 baseline checker + missing-inventory map:
`exit=2`, no `RESULT` line. B4 baseline checker + missing cluster: `exit=2`, no `RESULT`.
Delivered: missing inventory → `exit=1` + `RESULT FAIL` (P5); map errors → `exit=2` +
`RESULT ERROR` (P9–P11, P14, P15). The baseline quotes in M2.md reproduce exactly.

**Checker pins.**

- `corpus/fixtures/check_bible.py`: working-tree sha256 `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`;
  `git show 396c568:corpus/fixtures/check_bible.py | sha256sum` identical; last commit
  touching it is `ca7f9ef` (r90); `c4d4823` does not touch it → "r92 checker UNCHANGED
  (ff9fd2aa)" holds for this file.
- `corpus/tools/support_check.py`: `9da149b8…` at `396c568` → `55a5eb27…` at `c4d4823`.
  Diff hunks are exactly: `InventoryError(ValueError)`; the four inventory raise sites
  reclassified; `RESULT FAIL` added to `run()`'s failure branch; `main()` restructured so
  argparse/cluster/map/parse failures print `RESULT ERROR`/`RESULT FAIL` with exits 2/1/1.

**Freeze check** (own task, `cd lore-shokunin`, two 60 s checks):

```text
FREEZE_CHECK t=60s head=c4d4823b9a8165a88e8199af136e62d6e961b6b9 dirty=0
FREEZE_CHECK t=120s head=c4d4823b9a8165a88e8199af136e62d6e961b6b9 dirty=3
FREEZE_TERMINAL status=0 checks=2
```

The dirty entries are untracked concurrent follow-up seat artifacts (by ~10:26:
`followup/H4-census.json`, `H4-lineage.json`, `H4-probes.json`, `JCAL1-delta.json`,
`JCAL3-evidence.json`, `JCAL3.md` — all within the permitted `<SEAT>*` naming);
`git diff --stat` and `git diff --cached --stat` were empty, HEAD constant → zero tracked
modifications during judgment.

## Findings & named debt

- All four receipt families reproduce exactly on the committed tree; every number in the
  seat block (14+8; 10+2 with no WARN; retelling-only; contract exits/summaries) was
  observed as stated. No fabricated-receipt discrepancy found. The M2.md baseline quotes
  also match the reproduced controls.
- Pin attribution (record hygiene): `ff9fd2aa` is `check_bible.py` (the boundary-doc
  replay checker), not `support_check.py`. The round record should keep the two pins
  distinct — "checker UNCHANGED" is true for `ff9fd2aa` and deliberately false for
  `support_check.py` (`9da149b8` → `55a5eb27`).
- Stream nuance (minor, not a contract breach): row-level failures (`P12`/`P13`) print
  their `FAIL:` detail on stdout with empty stderr, while parse/CLI/IO failures print the
  detail on stderr. The terminal-summary claim holds on every path tested; if S2's
  contract wanted stream discipline for row details too, this is the one asymmetry left.
- Exit taxonomy verified as two families: inventory-declaration family → `RESULT FAIL`/1;
  map structure/CLI/IO family → `RESULT ERROR`/2; collected row failures → `RESULT
  FAIL`/1. Consistent with the delivered `main()` restructure.
- Not in this seat's scope (other blocks): C1 boundary-doc certification and C3 watch
  re-check receipts — not judged here, no gap claimed from this seat.
- Scratch hygiene: all probes removed; `/tmp/jcov1` no longer exists.

**Verdict recommendation** (per axis, judged only on the committed tree `c4d4823`):

- C2 coverage axis: **improved** — r88-m3 returns PASS with inventory 10+2 and zero WARN,
  against a reproduced baseline showing the WARN; the M2 contract conforms on all 15
  designed failure paths, with the missing-inventory exit moved 2→1 per the S2 contract;
  positive-path output is byte-identical to baseline (no trade).
- Regression axis (r87 + paraphrase receipts): **unchanged** (still PASS; byte-parity).
- Checker-pin axis: **unchanged** for `check_bible.py` `ff9fd2aa…`; `support_check.py`
  changed by design (C2 delivery).

## Handoff

- Report: `.ufo/waves/round-92/followup/JCOV1.md` (this file). No other repo writes, no
  commits, scratch removed. Judgment surface stayed `c4d4823` throughout (freeze above).
- Recommend the round record carry C2-coverage as improved with these receipts, and keep
  the checker pins distinct (`check_bible.py ff9fd2aa…` vs `support_check.py 55a5eb27…`).
- Replay: every command and observed output needed is inline above; controls are
  reconstructible via `git show 396c568:<path>`.