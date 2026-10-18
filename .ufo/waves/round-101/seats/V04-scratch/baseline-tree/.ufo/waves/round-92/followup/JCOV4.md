# JCOV4 — Fresh-eyes province audit (maps, hardened script, watch, governance text)

Seat JCOV4, round-92 FOLLOW-UP wave, world-bible lane. Judgment surface: committed tree
`c4d4823` (baseline `396c568`); `git diff --name-only HEAD` = 0 at start and at report time;
only untracked sibling artifacts moved. Fresh-eyes sequence: every gate/probe below was run
before reading any sibling follow-up verdict; SF1/SF2 were read first only as dispatch context,
and JDEP/JCAL/JCOV/H3/H4 verdicts were read afterwards for the comparison list in Findings.
Scratch under `/tmp`, removed in-command (`df -i /tmp` was 99% in use throughout; ≤6 probe files
live at once). Repo writes: this file only. No commit or push.

## Work performed

- Audited, on the committed tree only: (1) `corpus/knowledge/holder-assessment-boundary.md`
  (the C1 re-derivation) against B3's certification contract; (2) `corpus/tools/support_check.py`
  + its contract text `corpus/tools/README.md` + the three maps; (3) `corpus/knowledge/r91-c9-watch.md`
  (the C3 re-check) by rebuilding its probes; (4) the R8/R9 governance insert in
  `corpus/knowledge/r88-sourced-inspiration-decision-table.md`; (5) the 166-dir census and the
  README path-convention claims; (6) the certification artifacts (`patches/T1-certification.json`,
  commit message) against their own claims.
- Dependency waits (two 60 s checks, own task, receipt shape matching `poll_wait.sh`): the
  dependency was sibling follow-up artifacts, and several landed during the window:

  ```text
  POLL_CHECK t=60s followup_new=H4-census.json,H4-probes.json,JCAL1-delta.json,
  POLL_CHECK t=120s followup_new=H3-r92-discrimination.json,H3-r92-replay.json,H3-r92-scan.json,H4-census.json,H4-lineage.json,H4.md,H4-probes.json,JCAL1-delta.json,JCAL3-evidence.json,JCAL3.md,JCAL5-delta.json,JCOV1.md,JCOV2.md,JCOV3-census.json,
  POLL_TERMINAL status=0 reason=deadline elapsed=120s checks=2
  ```

  (JDEP1/JDEP4/K1/JCAL2/JCAL4 landed after the window; read for comparison only.) The committed
  work tree itself was present before the first check, so no work-phase wait was consumed.
- Gate/probe inventory: my own B3-gate run (A pin, B replay, C anchor census, D structure, E C9);
  a 12-probe support-contract battery plus a lowercase-malformed edge probe; watch probes
  re-derived from `.ufo/waves/round-90/patches/C9-rerun-probes.sh` mutations; census replay vs
  the committed `patches/B1-tuples.json`; relative-vs-absolute argv census on all 166 dirs;
  governance-text greps; artifact-consistency checks on T1/K1.

## Before → after measurements

All commands from `/home/vgpnk/Projects/shokunin/lore-shokunin`; every number observed in this
seat's own runs unless attributed to a named seat.

**1. State pins.**

```sh
sha256sum corpus/fixtures/check_bible.py corpus/knowledge/holder-assessment-boundary.md corpus/tools/support_check.py
```

```text
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
8e1fe8774a70f06c31efd783b4313a1639c1da4bcfd830be92134e8964536728  corpus/knowledge/holder-assessment-boundary.md
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py
```

The delivered doc hash equals the D2 candidate text that the pre-integration audit seat CB
measured (`CB.md` line 148: `D2: sha256=8e1fe877… lines=671`): the candidate was applied
verbatim; no reconciliation edit is present. `check_bible.py` is untouched by `c4d4823`
(commit touches 6 corpus files, none of them the checker).

**2. C1 boundary doc — my fresh B3 run.**

```text
Gate A (pin): checker ff9fd2aa…, 428 lines — PASS.
Gate B (replay, T1's grammar): fence_blocks=7; replay_receipts=3; replay_cases=14; mismatches=[]. PASS.
Gate C (anchors): 140 bare `:NNN` sites extracted outside fences.
  orphan r89 tail (doc:545-556): 21 sites, 14 stale vs the delivered checker —
    :168-173 (function is :168-175), :182 (delivered :182 is the dangling append; the
    ambiguity precedent is :184), :185-352 (loop is :187-345), :191 (check is :193),
    :192-194 (is :194-196), :198-203 (is :200-205), :206-208 (is :208-210),
    :212-214 (is :214-216), :215-221 (is :217-223), :222-248 (is :224-250),
    :249-312 (is :251-314), :313-319 (is :315-321), :320-352 (is :322-345),
    :425-435 (is :418-428; :429-435 is past EOF).
    The other 7 sites (:38-39, :72-76, :82-83, :85-91, :93, :97, :164-166) coincide.
  delivered-context stale: doc:330 `:198-203` for the item-level first-stop tests; the
    delivered span is :200-205 (doc:331 in the same bullet already gives the correct range).
  => 15 stale sites total; Gate C FAIL.
Gate D (structure): h1_count=1; duplicate_headings=[]; instruction_markers=[] — PASS.
Gate E (C9): c9_positive_clauses=5/5; c9_legacy_tick_conflict=False; AST tick 324-326
  (no holder_identity_detail, prefix chain_has_ambiguous_source True) and null guard 169-170 — PASS.
```

The r91 interlude is genuinely gone: T1's baseline control recorded, at `396c568`,
`h1_count=2` plus markers `(5, 'instruction sheet')`, `(6, 'Skipped as named debt')`
(`T1.md` observed block); the delivered doc scans clean, and its first H1 is now the only one.
The doc also contains no `r92`/`round-92` string: the provenance line still reads
"Refreshed at round-90 closure … verified-at: RUNTIME REPLAYED … round-90 seat CB1" (doc:3-9,
:39) — CB's named seam "explicit r92 provenance/skip receipt reconciled" (CB.md:269 item 3) is
still unreconciled.

**3. Certification record vs the commit message.** `patches/T1-certification.json` (committed,
written pre-integration at 09:40) states `"overall": "FAIL"`, `candidate_selection.status =
FAIL` ("No selected, integrated round-92 document is present … remains the r91 baseline"), and
records 3/3 + 14/14 only as the *baseline control* (`"Baseline-only control replay passed …
this is not a candidate pass"`). The commit message's "certified by T1: 3/3 receipts, 14/14
replay cases" therefore (a) cites numbers that are T1's r91-baseline controls, not a delivered-tree
certification, and (b) attributes a certification that no committed artifact records. My own
Gate-B replay reproduces 3/3 and 14/14 for the delivered doc, so the numbers are true for
Gate B — but "certified" against B3 requires Gate C too, which fails.

**4. C2 support script — contract battery (committed tree).**

```text
r87-myth-cluster           RESULT PASS  rc=0  (14/14 JSON, 8/8 editorial, 22/22 total, 22 anchors)
r88-m3-maya-cluster        RESULT PASS  rc=0  (10/10, 2/2, 12/12, 8 anchors; no WARN)
r89-inspiration-paraphrase RESULT PASS  rc=0  (1/1 retelling-support-only)
missing cluster            rc=2  stdout [RESULT ERROR]  stderr [FAIL: cluster directory not found: …]
missing map                rc=2  stdout [RESULT ERROR]  stderr [FAIL: claim-to-excerpt map not found]
inventory absent           rc=1  stdout [RESULT FAIL]   stderr [FAIL: map must contain exactly one …]
inventory malformed (upper)rc=1  stdout [RESULT FAIL]   stderr [FAIL: expected inventory declaration is malformed]
inventory duplicated       rc=1  stdout [RESULT FAIL]
inventory sum mismatch     rc=1  stdout [RESULT FAIL]   stderr [FAIL: expected JSON facts and editorial rows …]
row cell-count mismatch    rc=2  stdout [RESULT ERROR]  stderr [FAIL: map table row has a different number of cells …]
header drift (mode col renamed) rc=1  stdout ends [RESULT FAIL]  (declared inventory vs 0 parsed)
argparse error             rc=2  stdout [RESULT ERROR]
--help                     rc=0  (no RESULT ERROR line)
```

Every S2-contract family (inventory → FAIL/1; operational/structural → ERROR/2; collected
failures → FAIL/1) is conformant on these paths. Fresh-eyes edge probe (not covered by any
sibling battery I found): a *lowercase* malformed declaration —

```
**expected inventory:** ten json facts; not a number.
```

placed above a valid declaration — returns `rc=0`, `RESULT PASS`, empty stderr. The guard at
`support_check.py:89` (`line.lstrip().startswith("**Expected inventory:**")`) is case-sensitive
while `EXPECTED_INVENTORY` is `IGNORECASE`, so a lowercase malformed declaration is silently
ignored when a valid one is also present. Low severity, but it is an asymmetric edge in the
new fail-closed logic (uppercase variant → rc=1 RESULT FAIL).

**5. C2 doc-parity harm — `corpus/tools/README.md` still declares the old behavior live.**
`git diff 396c568 c4d4823 -- corpus/tools/README.md` is empty; the file still says at :18-21:

```
- **Missing inventory exits 2:** M2 reports … on stderr and returns 2, while S2 requires … 1 …
- **No terminal failure summaries:** … map/cluster errors return 2 without `RESULT ERROR` …
These are known contract deviations, not accepted equivalents; callers must use the diagnostic
text and process exit code until the checker is updated.
```

Both statements became false in this commit (probes above). `patches/K1-tools-readme.patch`
(sha256 `b4d7bd61…`; exactly the terminal-status replacement) passes `git apply --check`
cleanly but was not committed. So C2's code-side closure is real; its doc side now misstates
the delivered tool.

**6. Maps and census.**

```text
166 dirs vs committed patches/B1-tuples.json: missing=0 extra=0 tuple_mismatches=0;
exit_counts={0:32, 1:134}; violation_lines=421; b1_b2_identical=True.
rel vs abs invocation, all 166 dirs: stdout/exit differ for exactly 5 —
r5-missing-file, r62-missing, r67-claim-source-unavailable-control/-empty/-whitespace.
r88-m3 map: S1/S2 rows at claim-excerpt-map.md:40-41; both PASS; anchors hit
source-excerpt.md:5 inside the declared span; WARN (unreferenced source-excerpt.md) is gone.
```

**7. C3 watch.** `sha256sum corpus/knowledge/r91-c9-watch.md` → `a6b2b9db…`; check-log row 1
(2026-10-17, checker `ff9fd2aa…`) is consistent with the file. My reconstruction of the four
C5 probes (mutations from `C9-rerun-probes.sh` applied to `r89-fn2-unresolved-chain-break`) and
the two pinned fixtures replayed byte-identical to the watch's logged blocks (P1 2 violations
qualified chain; P2 definite tick; P3 definite null-side break; P4 definite tick; `r91-c1-null-chain`
1 violation; `r91-c1-tick-unresolved` 3 violations). The gate-count and sequence-scope commands
in the watch reproduce the logged output (`item=f3-seal admitted_matches=1 ticks=[3, 1] …`).
The watch's K1 composition check: `K1-watch-compose.patch` neither applies forward (:201) nor
reverse (:41) — my scratch rebuild shows the landed file = raw `X1-recheck.patch` + the two
hand-added census lines; content-equivalent to K1's composed proposal, but the composed patch
as such is not what landed.

**8. Governance insert.** `r88-sourced-inspiration-decision-table.md:40` carries the label
`**Failed-gate disposition (clarified r92):**` twice on one line (grep count of the doubled
pattern = 1; E1's `patches/E1-edges.md` and E2's wording each carry a single label — the
duplication was introduced at application). The R9 manual-gate block, receipt-boundary text
("necessary but not sufficient"), and R8 whole-element-hold text otherwise landed once each.

## Findings & named debt

**F1 — blocking: boundary-doc certification FAILS as delivered (Gate C), and the tree itself
says so.** Independently: 14 orphan-tail sites + 1 delivered-context site (doc:330) do not
resolve against the delivered checker; the orphan tail (doc:545-556) lost its r89 revision head,
so its citations are unqualified and, per B3, fail closed. The follow-up certifier JDEP1
(untracked artifact, ruled 10:29) reached the same ruling on its own census:
`(a) PASS · (b) FAIL (blocking) · (c) PASS · (d) PASS · (e) PARTIAL`, with the same 14/21
orphan mapping and the doc:330 stale. Repair is mechanical (delete the orphaned tail or restore
its head; re-anchor doc:330; add the r92 provenance line), then re-run Gate C.

**F2 — record integrity: "certified by T1" is unsupported by the committed artifacts.** The
committed `T1-certification.json` is `overall FAIL / candidate unavailable`, and its 3/3 + 14/14
are baseline controls (`T1.md`). The replay gates do pass on the delivered doc (my run), but
no committed artifact certifies it, and the first post-application certification (JDEP1) fails
Gate C. The round record should not carry C1's "certified" sub-claim.

**F3 — introduced harm: `corpus/tools/README.md:16-21` now misstates the delivered script.**
Its named-debt section (true before this commit) remained while `support_check.py` changed;
K1's ready patch (`b4d7bd61…`) was not integrated. Until it lands, readers are told to expect
exit 2 / no terminal summary for inventory failures that now yield exit 1 / `RESULT FAIL`.

**F4 — introduced defect: doubled R8 label at decision-table :40** (integration-application
defect; single in E1/E2 sources). JDEP4 independently charges it as its D-JDEP4r92-2.

**F5 — fresh edge: lowercase malformed inventory declaration silently ignored** (guard
case-sensitivity vs the IGNORECASE declaration regex). Low severity; no sibling probe covers it.

**F6 — carried/sibling-named debt (agreements, not new):** CB's three D2 seams remain unreconciled
(orphan e2bb9639 block = F1; duplicated README continuation doc:591-596 / doc:615-619; missing
r92 provenance). JDEP1 adds: census off-by-one doc:581-590 ("13 records across ten" at
`ca7f9ef`; measured 12/10) and README has no `## Round 91`/`r91-c1` mention. JCAL2 adds: the
watch has no next-recheck pointer (owner/due) and the e97613c checker hash + explicit
ambiguous-SOURCE wording from CB R3 remain absent. JDEP4 adds decisional gaps: R8 reviewer has
no independence requirement (R9's block does); R9 `PASS` has no sustainment/re-access clause;
R10 alias case still uncovered. JCOV1 adds a stream nuance: row-level `FAIL:` details go to
stdout while parse/CLI failures go to stderr (contract-preserving). All verified as present in
the committed tree by the cited seats; I reproduced the parts cited in my own sections.

**Verdict reads (per axis, committed tree only; no scalar, no trade counts as improvement).**
C1 depth: the anchor-based re-derivation and C9/replay/structure gates pass (interlude ended;
one heading set; replays byte-identical), but Gate C fails on 15 sites and the certification
record is absent/FAIL — as delivered, C1's certified-delivery claim is **not an improvement**;
the doc is improved vs the r91 interlude on structure/replay, with carried evidence-section
defects. C2 coverage: maps + script **improved** (WARN closure and contract conformance both
reproduced), but the same commit introduced the tools-README misstatement (F3) — a trade, so
C2 reads improved only once F3 lands. C3 calibration: **improved (bounded)** — my replay and
JCAL2's independent judge agree; the missing next-recheck pointer is named debt. Governance
text: **improved, bounded** (R8/R9 decided), with F4 and JDEP4's carried edges.

## Handoff

- Report: `.ufo/waves/round-92/followup/JCOV4.md` (this file). No other repo writes; no commits;
  scratch removed; judgment surface stayed `c4d4823` (`git diff --name-only HEAD` = 0).
- For the round record / r93: (1) carry JDEP1's Gate-C FAIL as the certification of record for
  the boundary doc until a repaired revision is re-certified; correct the commit-message
  "certified by T1" reading (F2). (2) Mechanical repairs: orphan tail doc:545-556, stale
  doc:330 `:198-203` → `:200-205`, doubled label decision-table :40, apply
  `K1-tools-readme.patch`, add the doc's r92 provenance line. (3) Consider hardening the
  inventory guard to match the IGNORECASE regex (F5). (4) Census and path-convention notes are
  confirmed exactly; no action needed there.
- Reproduce my headline receipts: B3-gate script (inline above), support battery commands
  (above), watch mutation script from `.ufo/waves/round-90/patches/C9-rerun-probes.sh` (run the
  delivered checker instead of the patched candidate), census driver as in `JCAL1.md`.
- Cross-seat comparison: agreements — JCOV1 (receipts + contract battery), JCOV2 (Spence rows +
  doubled label), JCOV3/JCAL1/H4 (census), JCAL2/H3/JCAL4 (watch), JCAL3 (path notes), H3/H4
  (probes/lineage), JDEP1 (Gate-C FAIL + splices), JDEP4 (governance edges). Unique to this
  seat: the certification-artifact/message mismatch analysis (F2), the tools-README + unlanded
  K1 patch finding (F3), the lowercase inventory edge (F5), and the X1+note composition check.