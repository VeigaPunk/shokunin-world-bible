# JCOV1 — receipts judge (round-93 FOLLOW-UP)

Judgment surface: committed tree `65838f8` (baseline `87779a0`); tree clean at judgment
start. Axes named: (1) receipt fidelity — all four cluster receipts reproduce exactly;
(2) no-harm — pre-existing receipts byte-identical vs baseline, checker genuinely
unchanged; (3) attack resistance — the full failure-path battery against the current
support command, extended to the new cluster. All scratch under `/tmp/jcov1-r93`
(removed at end). Methods follow r92 followup JCOV1 (`c4d4823` seat) for continuity.

## Work performed

- Re-ran every receipt family named in the JCOV1 block on the committed tree, cwd
  `lore-shokunin/`:
  1. r87 receipt — `python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster`
  2. r88-m3 receipt — same command, `corpus/fixtures/r88-m3-maya-cluster`
  3. paraphrase demo — same command, `corpus/fixtures/r89-inspiration-paraphrase`
  4. r93-m2 receipt (NEW) — same command, `corpus/fixtures/r93-m2-kojiki-cluster`
  5. The new cluster's README-embedded replay:
     `python3 corpus/fixtures/check_bible.py corpus/fixtures/r93-m2-kojiki-cluster`
- Baseline controls from scratch only: `git show 87779a0:corpus/tools/support_check.py`
  (sha256 `55a5eb27…` — byte-identical to the delivered checker) plus baseline maps via
  `git show 87779a0:…` for r87/r88/r89. Byte-parity runs: baseline checker + baseline
  maps vs delivered checker + same maps, stdout+stderr diffed, on all three pre-existing
  clusters; plus the NEW r93-m2 cluster run under both checkers (delivered map).
- Pin census: `sha256sum` of all four `corpus/tools|fixtures` tools, `git show
  87779a0:<path> | sha256sum` per path, and full `git diff --stat 87779a0..65838f8 --
  corpus/` (18 files: 11 new `r93-m2-kojiki-cluster` files, 3 knowledge files, tools
  README, 2 NEW tools; zero changes to r87/r88/r89 fixture dirs, `check_bible.py`, or
  `support_check.py`).
- Attack battery: 20 observations (r92's 15-probe M2 contract battery reconstructed
  verbatim in intent, plus new-cluster probes P16–P18 and the P17A/P17B single-cell
  refinement) — committed maps mutated in `/tmp`, checker run against committed clusters,
  exit code + terminal `RESULT` line + stderr line-count captured per probe.
- Zero-shared-referent corroboration: JSON-level walk of `entities/relations/timeline`
  (id, entity_id, place_id, from, to, name, display_name) across the three clusters,
  pairwise intersections.
- Freeze check: 2×60 s re-verification that HEAD/tracked tree did not move during
  judgment.
- No repo writes except this file; no commit/push; no sibling repos touched.

## Before → after measurements

**Positive receipts (delivered tree; exit via `echo exit=$?`).**

```text
$ python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 8/8; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 22/22
ANCHORS repeated-references=0; DUPLICATE-ROWS 0
RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 8; TOTAL-ROWS 22
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 8/8; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS
exit=0
```

```text
$ python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12; DISTINCT-ANCHORS 8/8
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
RECEIPT JSON-FACTS 10; EDITORIAL-ROWS 2; TOTAL-ROWS 12
SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 12/12; VALIDATED-ROWS 12/12
RESULT PASS
exit=0
```

No `WARN` line (r90-era unreferenced-declaration WARN stays closed; S1/S2 both
`PASS … editorial-row; mode=verbatim; anchor=found`).

```text
$ python3 corpus/tools/support_check.py corpus/fixtures/r89-inspiration-paraphrase
INVENTORY JSON-FACTS 1/1; EDITORIAL-ROWS 0/0; TOTAL-ROWS 1/1; DISTINCT-ANCHORS 1/1
ANCHORS repeated-references=0; DUPLICATE-ROWS 0
PASS entities.json#/0/claims/0: retelling-support-only; anchor=found; mode=paraphrase; 9:A modern paraphrase says …
RECEIPT JSON-FACTS 1; EDITORIAL-ROWS 0; TOTAL-ROWS 1
SOURCE-SUPPORT 0/0; EDITORIAL-ANCHORS 0/0; RETELLING-SUPPORT-ONLY 1 entries (1/1 anchors); MODES 1/1; VALIDATED-ROWS 1/1
RESULT PASS
exit=0
```

Retelling-only semantics hold: the paraphrase row never counts toward SOURCE-SUPPORT.

```text
$ python3 corpus/tools/support_check.py corpus/fixtures/r93-m2-kojiki-cluster
INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15; DISTINCT-ANCHORS 15/15
ANCHORS repeated-references=0; DUPLICATE-ROWS 0
PASS E1 … PASS E12: source-support; mode=verbatim; anchor=found   (12 rows)
PASS S1/S2/S3: editorial-row; mode=translation; anchor=found      (3 Chamberlain rows)
RECEIPT JSON-FACTS 12; EDITORIAL-ROWS 3; TOTAL-ROWS 15
SOURCE-SUPPORT 12/12; EDITORIAL-ANCHORS 3/3; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 15/15; VALIDATED-ROWS 15/15
RESULT PASS
exit=0
```

```text
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r93-m2-kojiki-cluster
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

The README-embedded replay block (both lines) reproduces exactly.

**Baseline parity (controls).**

- `git show 87779a0:corpus/tools/support_check.py | sha256sum` = `55a5eb27…` — identical
  to the delivered checker's hash, so r93 introduces ZERO checker delta (first round
  since the r92 delivery with no `support_check.py` change).
- Baseline checker + baseline maps vs delivered checker + same maps on r87 / r88-m3 /
  r89: `base_exit=0 deliv_exit=0 PARITY diff_lines=0` for all three (stdout and stderr).
- New cluster under BOTH checkers (delivered map): `base_exit=0`, `deliv_exit=0`,
  outputs identical — the new receipt needs no checker change; pure coverage addition.

**Checker pins (working tree == HEAD 65838f8 throughout).**

| file | sha256 (HEAD) | at 87779a0 | delta |
|---|---|---|---|
| `corpus/fixtures/check_bible.py` | `ff9fd2aa6811…` | same | UNCHANGED (since r90) |
| `corpus/tools/support_check.py` | `55a5eb275390…` | same | UNCHANGED (since r92) |
| `corpus/tools/boundary_doc_check.py` | `8e439b5129d0…` | absent | NEW in r93 |
| `corpus/tools/discriminate_check.py` | `6c7b7cd8b667…` | absent | NEW in r93 |

**Attack battery (20 observations; maps mutated in /tmp, cluster committed).** Observed
`exit=`, terminal-`RESULT` line count, and stderr line count:

| probe | mutation | exit | terminal | stderr lines |
|---|---|---|---|---|
| P1 | no args | 2 | RESULT ERROR (1 line) | 2 |
| P2 | cluster dir missing | 2 | RESULT ERROR | 1 |
| P3 | `--map` missing | 2 | RESULT ERROR | 1 |
| P4 | `--map` is a directory | 2 | RESULT ERROR | 1 |
| P5 | inventory line deleted (r87) | 1 | RESULT FAIL | 1 |
| P6 | inventory malformed (`14`→`fourteen`) | 1 | RESULT FAIL | 1 |
| P7 | inventory duplicated (`sed '7p'`) | 1 | RESULT FAIL | 1 |
| P8 | totals inconsistent (22→21) | 1 | RESULT FAIL | 1 |
| P9 | row cell-count mismatch (extra cell, r88 P1 row) | 2 | RESULT ERROR | 1 |
| P10 | fact row with empty anchor (handcrafted map) | 2 | RESULT ERROR | 1 |
| P11 | fact table under non-fact heading | 2 | RESULT ERROR | 1 |
| P12 | source anchor missing (r88, sentinel) | 1 | RESULT FAIL | 0 |
| P13 | excerpt path missing (r87 → `missing-excerpt-r93.md:7`) | 1 | RESULT FAIL | 0 |
| P14 | map unreadable (chmod 000) | 2 | RESULT ERROR | 1 |
| P15 | map invalid UTF-8 (`\xff`) | 2 | RESULT ERROR | 1 |
| P16 | r93 exact duplicate mapped row (E1 ×2) | 1 | RESULT FAIL | 0 |
| P17A | r93 single fact-row mode `verbatim`→`paraphrase` | 1 | RESULT FAIL | 0 |
| P17B | r93 map-level declaration `verbatim`→`paraphrase`, rows untouched | 1 | RESULT FAIL | 0 |
| P18 | r93 E1 span `5`→`99` (out-of-span hit) | 1 | RESULT FAIL | 0 |

All 20 printed exactly one terminal `RESULT` line. Representative details:
P5 stderr `FAIL: map must contain exactly one expected inventory declaration`; P9 stderr
`FAIL: map table row has a different number of cells than its header`; P15 stderr
`FAIL: 'utf-8' codec can't decode byte 0xff…`; P12 stdout `FAIL E1: … anchor=not-found`
+ `FAIL: E1: source-support anchor missing`; P16 stdout `FAIL: inventory JSON facts
mismatch: expected=12 parsed=13` + `FAIL: duplicate mapped row E1 appears 2 times`; P18
stdout `FAIL: E1: anchor hit outside declared line span 99 (hit lines: 5)`.

Paraphrase-injection probes in detail (both fail closed):

- P17A — downgrading one fact row to `paraphrase` does NOT smuggle it past validation:
  `FAIL E1: retelling-support-only; … mode=paraphrase; excerpt-mode=verbatim`, E1 is
  excluded from source support (`SOURCE-SUPPORT 11/11` — the tampered row counts in
  neither column of support), `MODES 14/15; VALIDATED-ROWS 14/15`, `RESULT FAIL`.
- P17B — flipping the map-level declaration breaks mode agreement for every row on that
  excerpt (all 12 `archive-record-excerpt.md` rows FAIL), `RESULT FAIL`. (First run of
  this probe accidentally applied both mutations at once — same verdict, exit 1; redone
  as single-cell P17A/P17B above.)

**Zero-shared-referent corroboration** (JSON id/name-level, this seat's independent
scan): `r87 keys=14 r88 keys=8 r93 keys=8`; `r93∩r87: EMPTY`; `r93∩r88: EMPTY`;
`r87∩r88: EMPTY`.

**Freeze check** (two 60 s checks, `cd lore-shokunin`):

```text
FREEZE_CHECK t=60s head=65838f8 tracked_dirty=0 untracked_total=1
FREEZE_CHECK t=120s head=65838f8 tracked_dirty=0 untracked_total=1
FREEZE_TERMINAL
```

The single untracked entry is the round-93 `followup/` dir (this report's parent);
`git diff --stat` and `git diff --cached --stat` empty, HEAD constant → zero tracked
modifications during judgment.

## Findings & named debt

- All four receipt families reproduce exactly on the committed tree; every number in the
  seat block was observed as stated: r87 14+8 PASS; r88-m3 10+2 PASS with zero WARN;
  paraphrase demo retelling-only (SOURCE-SUPPORT 0/0, RETELLING 1/1); r93-m2 12+3 PASS
  with 15/15 distinct anchors, plus its README replay (`check_bible.py` CLEAN, exit 0).
  No fabricated-receipt discrepancy found.
- Pin attribution (record hygiene, carried from r92): `ff9fd2aa` is `check_bible.py`.
  This round the claim "checker UNCHANGED (ff9fd2aa)" is true AND understated —
  `support_check.py` (`55a5eb27`) is byte-identical to baseline too; the only new
  checker bytes are the two NEW tools (`8e439b51`, `6c7b7cd8`). The round record can say
  both support-path checkers are unchanged in r93.
- Attack resistance: 20/20 observations on-contract. Exit taxonomy holds in two families
  (inventory/row-level collected failures → `RESULT FAIL`/1; CLI/IO/map-structure →
  `RESULT ERROR`/2). The new cluster is not a soft target: duplicate rows, mode
  tampering (both directions), and span tampering all fail closed.
- Stream asymmetry (named in r92, persists verbatim — same delivered checker): row-level
  `FAIL:` details print on stdout with empty stderr (P12, P13, P16–P18), while
  InventoryError/parse/IO details print on stderr. Terminal-summary claim holds on every
  path tested; still the one asymmetry if stream discipline is ever wanted for row
  details.
- Zero-shared-referents: corroborated at the JSON id/name level by this seat's
  independent scan (all three pairwise intersections EMPTY, including r87∩r88 as a
  control). The cluster README itself still flags M6's M2-specific independent scan and
  semantic review as pending — the integrated zero-referent conclusion remains named
  debt owned by the M6/J3 lane, not closed by this seat's lexical corroboration.
- P17B serendipity (behavior note, not debt): the checker validates map-declaration ↔
  inline-excerpt-declaration agreement per row (support_check.py:275), so a tampered
  declaration row poisons every row of that excerpt — stricter than the README's
  one-line description implies. Worth one sentence in the tools README if the lane ever
  touches it; no change requested this round.
- Not in this seat's scope (other blocks): boundary-doc certification receipts (CERT/
  CB-audit surface), the C9 watch re-check rows, and `boundary_doc_check.py`/
  `discriminate_check.py` behavior — no gap claimed from this seat.
- Scratch hygiene: all probes removed; `/tmp/jcov1-r93` no longer exists.

**Verdict recommendation** (per axis, judged only on the committed tree `65838f8`):

- C2-coverage axis (new Kojiki-family cluster receipts): **improved** — a third sourced
  cluster lands with a full 12+3 receipt PASS (plus `check_bible.py` CLEAN) under a
  checker that needed no change, zero WARN, 15/15 distinct anchors, and battery probes
  specific to it all fail closed; no trade observed on any pre-existing receipt.
- No-harm / regression axis (r87 + r88-m3 + paraphrase receipts): **unchanged** —
  fixture dirs zero-diff vs `87779a0`, checker byte-identical, outputs byte-identical
  (PARITY diff_lines=0 ×3, plus the new cluster identical under both checkers).
- Attack-resistance axis: **unchanged** (contract holds on all 20 probes), positively
  re-exercised on the new cluster with three new failure classes (duplicate row, mode
  tamper, span tamper) all caught.
- Checker-pin axis: **unchanged** for both `check_bible.py` (`ff9fd2aa…`) and
  `support_check.py` (`55a5eb27…`); `boundary_doc_check.py` / `discriminate_check.py`
  are new files with no prior pin (certification lane's surface, not judged here).

## Handoff

- Report: `.ufo/waves/round-93/followup/JCOV1.md` (this file). No other repo writes, no
  commits, scratch removed. Judgment surface stayed `65838f8` throughout (freeze above).
- Recommend the round record carry: C2-coverage improved on the strength of the r93-m2
  receipts (12+3 PASS + CLEAN replay + fail-closed battery), with r87/r88/r89 receipts
  unchanged at byte parity, and BOTH support-path checker pins unchanged this round
  (`check_bible.py ff9fd2aa…`, `support_check.py 55a5eb27…`).
- Keep the standing debt lines: M6's M2-specific zero-referent scan/semantic review
  (integrated conclusion pending), and the row-detail stream asymmetry in
  `support_check.py` (cosmetic, unchanged since r92).
- Replay: every command and observed output needed is inline above; baseline controls
  reconstructible via `git show 87779a0:<path>`.
