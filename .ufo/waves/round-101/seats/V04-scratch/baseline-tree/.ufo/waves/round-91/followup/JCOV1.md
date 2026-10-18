# JCOV1 — receipts judge (C2 support command)

Seat: JCOV1. Judged artifact: delivered tree at `c2ab3d07eaa86ce58f3f9c7fdff702f4b91ea7b7` (HEAD; tracked tree clean, only the untracked followup dir present). All commands run from `lore-shokunin/` unless stated. Scratch: `/tmp/JCOV1s/<case>` (unique per case) plus `/tmp/jcov1/delivered/` for the script copy. Every number below comes from a clean run in a unique scratch dir; an earlier probe batch that shared `/tmp/jcov1` with a concurrent process (foreign `ctrl-*`, `base.json`, `census.py` files present) was discarded rather than reported.

## Work performed

- Ran the delivered support command (`corpus/tools/support_check.py`, sha256 `9da149b8e51f5c6c39477f17b8b19d17da3568a1a7c72412079efccff1f330bf`, byte-identical in tree and scratch copy) on r87, r88-m3, and the r89 paraphrase demo.
- Reproduced the M2+M6 integration receipt: `git archive a7c6a17` of the five patch-touched files, applied `patches/M2-hardening-alt.patch` then `patches/M6-reconcile.patch` (both `git apply` = PASS); `cmp` reports all five files IDENTICAL to c2ab3d0, including the r89 map (the c2ab3d0 `+4` lines are byte-for-byte the M2 patch hunk for that file — the integration fixup restored the hunk the work commit missed).
- Extracted the baseline checker `a7c6a17:corpus/tools/support_check.py` (sha256 `66a3c4bb2ae7fc2049227e480864661606b65a629c64cbc3ce05e14589add472`) and ran it as a discriminating control on the delivered fixtures and on three mutants.
- Re-ran all five attack cases (header rename, dropped section, duplicate row, Spence mode flip, missing inventory) against the delivered script on fresh scratch copies, with exit codes captured immediately after each run.
- Corroborated the C9 pin: `sha256sum corpus/fixtures/check_bible.py` = `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` (matches `knowledge/r91-c9-watch.md`).
- No wait-checks were required: the work commits `6332115` + `c2ab3d0` were already landed, so all inputs existed.

## Before → after measurements

Positive receipts, delivered tree:

```text
$ python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster        # exit 0
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 8/8; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 22/22
RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 8; TOTAL-ROWS 22
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 8/8; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS

$ python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster     # exit 0
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 0/0; TOTAL-ROWS 10/10; DISTINCT-ANCHORS 6/6
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 0/0; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 10/10; VALIDATED-ROWS 10/10
WARN: unreferenced excerpt declaration: source-excerpt.md (mode=verbatim)
RESULT PASS WITH WARNINGS

$ python3 corpus/tools/support_check.py corpus/fixtures/r89-inspiration-paraphrase   # exit 0
PASS entities.json#/0/claims/0: retelling-support-only; anchor=found; mode=paraphrase; 9:A modern paraphrase says that the keeper later summarized the ledger for the court: the tide-mark had been moved to the west stair.
SOURCE-SUPPORT 0/0; EDITORIAL-ANCHORS 0/0; RETELLING-SUPPORT-ONLY 1 entries (1/1 anchors); MODES 1/1; VALIDATED-ROWS 1/1
RESULT PASS
```

Baseline (`66a3c4bb`) on the same fixtures, for contrast — aggregate receipts only, no category split, no warning:

```text
r87: SOURCE-SUPPORT 22/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22 / RESULT PASS (exit 0)
r88: SOURCE-SUPPORT 10/10; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 10/10 / RESULT PASS (exit 0)
r89: SOURCE-SUPPORT 0/0; RETELLING-SUPPORT-ONLY 1 entries (1/1 anchors); MODES 1/1 / RESULT PASS (exit 0)
```

The r89 retelling-only behavior predates this hardening; the delivered change adds the inventory/anchors/receipt split and the corroborating counts.

Attack cases, delivered script (each run in its own fresh scratch dir; the first shared-scratch batch was discarded and none of its numbers are reported):

- **Header rename** (r87 `| ID |`→`| Row |` on the JSON-facts header line only): exit **1**; `INVENTORY JSON-FACTS 0/14; EDITORIAL-ROWS 8/8; TOTAL-ROWS 8/22; DISTINCT-ANCHORS 8/22`; `FAIL: inventory JSON facts mismatch: expected=14 parsed=0`; `FAIL: inventory total mapped rows mismatch: expected=22 parsed=8`; `FAIL: inventory distinct excerpt anchors mismatch: expected=22 parsed=8`; four unreferenced-declaration WARNs; no `RESULT FAIL` line.
- **Dropped section** (removed `## JSON facts` block, 19 lines): exit **1**; identical counts and the same three FAILs; no `RESULT FAIL`.
- **Duplicate row** (exact `| P1 |` row inserted once in r88): exit **1**; `INVENTORY JSON-FACTS 11/10; EDITORIAL-ROWS 0/0; TOTAL-ROWS 11/10; DISTINCT-ANCHORS 6/6`; `ANCHORS repeated-references=5; DUPLICATE-ROWS 1`; `FAIL: inventory JSON facts mismatch: expected=10 parsed=11`; `FAIL: inventory total mapped rows mismatch: expected=10 parsed=11`; `FAIL: duplicate mapped row P1 appears 2 times`.
- **Spence mode flip** (declaration-table row `source-excerpt.md:5`, `verbatim`→`paraphrase`): exit **0**; all counts unchanged (`10/10`, `6/6`, `SOURCE-SUPPORT 10/10`); `WARN: unreferenced excerpt declaration: source-excerpt.md (mode=paraphrase)`; `RESULT PASS WITH WARNINGS`.
- **Missing inventory** (r87 `**Expected inventory:**` line removed): exit **2**; stdout 0 bytes; stderr `FAIL: map must contain exactly one expected inventory declaration`.

Baseline discrimination control (same mutants, baseline then delivered):

```text
header-rename:   baseline exit 0  SOURCE-SUPPORT 8/8;  MODES 8/8  / RESULT PASS   | delivered exit 1
dropped-section: baseline exit 0  SOURCE-SUPPORT 8/8;  MODES 8/8  / RESULT PASS   | delivered exit 1
duplicate-row:   baseline exit 0  SOURCE-SUPPORT 11/11; MODES 11/11 / RESULT PASS | delivered exit 1
```

The baseline silently passed all three mutants with a green terminal line; the delivered command fails each one. The baseline r88 run also emitted no unreferenced-declaration warning where the delivered run does.

README documentation check (`corpus/tools/README.md`, delivered): the "Named debt — S2 terminal-status contract" section states the missing-inventory `FAIL:`/exit-2 behavior and the absent `RESULT FAIL`/`RESULT ERROR` summaries. Observed behavior in the five cases matches both named deviations exactly.

## Findings & named debt

- **C2 receipts reproduce exactly.** r87 14/14 + 8/8, r88-m3 10/10 with the single expected unreferenced-declaration WARN and `RESULT PASS WITH WARNINGS`, r89 retelling-only — all confirmed on the delivered tree with exit 0. The M2+M6 composition and the delivered bytes are identical, so the delivered artifact is exactly the verified stack.
- **Verdict recommendation: C2 coverage axis — improved, bounded.** The hardened command detects the three silent-pass mutants that the baseline passed green, splits JSON-fact from editorial support, and surfaces the r88 declaration drift as a warning. Bounds are the already-named debt: the inventory is self-attested (a coordinated row+declaration edit can still agree), warnings are non-blocking by design, and no terminal `RESULT FAIL`/`RESULT ERROR` summaries exist; missing inventory exits 2 rather than S2's 1.
- **Spence flip is warn-only and indirect:** the flipped declaration is *unreferenced* (the two Spence comparisons are prose bullets, not table rows — the r92 item), so the flip changes only the WARN text; counts and exit are unaffected. This matches the M6 record and is not silent-pass detection of a mapped row.
- **C9 pin corroborated:** `check_bible.py` = `ff9fd2aa…` in the delivered tree, matching the watch doc.
- Environmental caveat only: `/tmp/jcov1` is shared with a concurrent process; the first probe batch there raced and was discarded. No repo impact; all reported results are from unique-dir clean runs. Not repo debt.

## Handoff

- Deliverable: this file, `.ufo/waves/round-91/followup/JCOV1.md`. No other tracked writes; no commit or push. Scratch (`/tmp/JCOV1s`, `/tmp/jcov1/{base,delivered,logs}` — only my own files) removed after measurement.
- For closure: recommend C2 = improved (bounded) with no new debt; carry the two README-named S2 terminal-status deviations and the warning-only retelling semantics into r92 as already recorded. The Spence comparison rows (r92) remain the follow-up that would make the r88 declaration directly referenced rather than warn-only.