# F27 — final all-axis adjudicator (round-94 FOLLOW-UP, lore-shokunin)

**Seat:** F27, final all-axis adjudicator. Role: read every FOLLOW-UP report that exists at run time, spot-replay anything load-bearing, reconcile conflicting seat findings explicitly, apply the admission rule (admit ONLY if C1 and C2 verify on the delivered revision AND no axis is harmed), produce the per-axis verdict table for all six axes, the ADMIT/REJECT recommendation, and the exact conditions of admission. No re-roll of a harmed finding.

**Delivered revision judged:** HEAD `65a93298cb100fdbf5732ac6de55f01a683c02d8`; corpus bytes byte-identical to WORK checkpoint `abbc3e0` (`git diff --name-status abbc3e0 65a9329` → `M LOG.md`, `M README.md` only, and those two come from merge `b8b50c8` + the declaration commit; no corpus path). Baseline `9c2eea3`. Read cutoff ~15:50 local, 2026-10-17. Writes: this report only; no corpus edits, no commits, no nested agents, no network.

**Peer reports read:** all 39 reports present at cutoff — F01–F26, F28–F40 (F27 is this seat), listed by `ls .ufo/waves/round-94/followup/F*.md | wc -l` → `39` before this file was written. F29 (debt ledger) was compiled before F21/F40 landed and says so (`F29-debt.md:7`); its CC-14 "no depth verdict observed" is superseded by F21. F40 is defective (see §4.6).

## 1. My own replays (raw observed output; the basis for the verdicts below)

```
python3 <json.load comparison>          → counts r88: 4 0 2 | r94: 5 1 3; entities[0:4] equal True;
                                          timeline[0:2] equal True; new event depends_on == both tick9 ids True
python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing   → CLEAN ... 0 violations, exit 0
python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-m3-maya-cluster   → CLEAN ... 0 violations, exit 0
python3 corpus/tools/support_check.py corpus/fixtures/r94-paired-crossing    → RESULT PASS, exit 0
                                          (INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; MODES 16/16; VALIDATED-ROWS 16/16)
python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing  → OBLIGATIONS raw=14 mapped=14 / RESULT PASS, exit 0
python3 corpus/tools/map_obligations.py corpus/fixtures/r93-m2-kojiki-cluster→ OBLIGATIONS raw=12 mapped=12 / RESULT PASS, exit 0
python3 corpus/tools/map_obligations.py corpus/fixtures/r88-m3-maya-cluster  → FINDING unsupported_map ... / RESULT ERROR, exit 2
python3 corpus/tools/map_obligations.py --self-test                          → 20/20 SELF-TEST PASS / RESULT PASS, exit 0
python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93
                                          → SNAPSHOT inputs=4 digests=verified; FROZEN expected=PASS/0 findings=none matched; exit 0
# my own counterexample on a /tmp copy (extra raw claim, no map row):
support_check → RESULT PASS exit 0   |   map_obligations → raw=15 mapped=14, FINDING missing_obligation, exit 1
# my own F15-mutation-(a) replay on a /tmp copy (drop evin-ninth-bell from tick-10 depends_on):
check_bible → CLEAN exit 0           |   map_obligations → raw=14 mapped=14 PASS exit 0
# census loop over corpus/fixtures/*/: dirs=168 clean=34 neg=134 other=0 violation_lines=421
sha256sum -c .ufo/waves/round-94/work/W05-baseline-corpus.sha256 → 984 lines, 0 mismatches
git diff --name-status 9c2eea3..abbc3e0 -- corpus/ → 13 A, 0 M/D;  tool sha256 cc1df4dc…, checker ff9fd2aa…, contract 349a1956…
```

Citation spot-checks: `r87/inspiration-note.md:5,21-23`, `r88/source-excerpt.md:3-7`, `r93/kojiki-chamberlain-excerpt.md:3-16`, `r88/symbolism-clause-map.md:7-8`, `r93/claim-excerpt-map.md:33-41` all resolve to the content the r94 knowledge doc cites.

## 2. C1 — verifies on the delivered revision

Every declared C1 element is demonstrated, most by multiple independent seats plus my replays:

| Element | Evidence |
|---|---|
| New fixture, explicit r88 continuation, r88 untouched | F06, F21, F36; `git diff --name-status 9c2eea3..abbc3e0 -- corpus/` → 13 A / 0 M-D |
| Counts 4/0/2 → 5/1/3 | F01 §2, F21 Replay B, my json.load; F04's independent census 14 = 5+5+1+3 |
| Inherited records parsed-value identical (entities, events, sources) | F01 §4 (0 field-level diffs, key order identical), F06, F13/F14/F31/F36; my equality check True |
| Tick-10 event depends on BOTH named tick-9 entries; no dangling refs | F01 §3, F21 Replay C; my set-equality True |
| New authored minute supplies place/agreement/actors/ordering | `fictional-excerpts.md:17-20`; F04 proposition trace |
| 14 canonical map obligations + 2 separate editorial rows | F03, F09, F34, F39; `map_obligations raw=14 mapped=14`, `support_check 14/14 + 2/2` |
| Exact in-span anchors, R9 modes | F34 (16/16 in-span, negative controls), F02, F03; my support_check PASS |
| Relation bounded to the agreement ("for this crossing only") | F02 §J11, F04, F06; `relations.json#/0`, three in-place disclaimers |
| Tick/ID/dependency encodings distinguished from excerpt words | F04 O1–O4, F06, F39 C1-13 |
| Cross-myth comparison record (ETCSL/Spence/Kojiki, status, stops) | F05 PASS, F38 PASS, F39 C1-17..21; my citation spot-checks |
| check_bible CLEAN; support_check PASS | my runs + F01/F02/F33 |
| Independent manual whole-claim AND comparison review in FOLLOW-UP | F04 PASS (whole-claim), F05 PASS (comparison) — this closes F39's V4/V7 which were written before F04/F05 landed |

No C1 check failed in any seat. **C1 verifies.**

## 3. C2 — verifies on the delivered revision

| Element | Evidence |
|---|---|
| Bounded stdlib CLI + persisted contract | F07, F12, F24 §0, F39 C2-1/2; imports stdlib-only; tool sha256 `cc1df4dc…` matches HEAD blob |
| r93 canonical map 12/12; r94 map 14/14 | F08, F09, F10; my runs |
| Before/after blind spot demonstrated without touching live fixtures | F23 §1 (both fixtures), F15 §4 (mut-b/b2: support_check PASS while map_obligations FAILs `missing_obligation`), F24, W02 demo; my own /tmp counterexample |
| Duplicate / phantom / source-ID mismatch with stable finding IDs | F11 (six controls ×2 byte-identical), F09 §6, F39 C2-8 |
| Unsupported grammar / malformed JSON / invalid paths → exit 2, never empty success | F11, F23 §2 (19 probes), F35, F39 C2-9; my r88 run exit 2 `unsupported_map` |
| CLI contract 0/1/2, one terminal RESULT line, stable IDs | F35 (20 operational invocations), F24 §4; my runs |
| `--self-test` isolated, persisted expectations, real CLI subprocesses | F07, F12, F24 §2 (positive control: flipped expectation → exit 2 `self_test_mismatch`) |
| No network, no live-tree writes, no regeneration, no dependencies | F12, F24 §5, F36 §7, F39 §F (pre/post hashes unchanged); code census shows writes only inside the self-test temp dir |

No C2 check failed. **C2 verifies.** Bounds recorded (BR-01…BR-04 in F29; §5 below).

## 4. Conflict reconciliation (explicit; nothing smoothed)

1. **F15 "FAIL for mutation (a)" vs everything else green.** Sustained as an observed fact, but it is not a C1/C2 claim failure and not an axis harm. The wave spec never claims `check_bible` detects a *reduction* of `depends_on`; the checker is byte-frozen (`ff9fd2aa…`, unchanged by r94) and only validates edges that remain (`check_bible.py:397-414` behavior). My own replay reproduced F15 exactly (drop one dependency → CLEAN + PASS). F15's other mutations (a2 dangling ref, b/b2 dropped map rows, b3 stale inventory, c span break, d source-id) all behave as specified. Recorded as BR-01; no re-roll is warranted because no axis is harmed.
2. **F17 FAIL + F25 FAIL (freshness) vs F24 PASS (operability) and F22 PASS (coverage).** Not contradictory: F17/F25 judge pin/document currency (four findings reproduce, plus two carried stale records), F24 judges the delivered gate's runnable behavior, F22 judges the delivered surface. F25 itself states the axis is "unimproved by r94 rather than newly harmed" (`F25-debt…` bottom line). I adopt freshness = **unchanged (no improvement, no harm)** and carry the findings as admission conditions (C-1/C-2).
3. **F37 "FAIL (bounded)" (doc currency).** Same class as (2): `corpus/fixtures/README.md` still at the r93 167-dir census and the W25 appends absent — all declared pending in `work-receipt.json` `checkpoint_limits` and `SCORECARD.md:379`. A condition, not a harm.
4. **F39's two NOT-demonstrated items (V4/V7) vs F04/F05 PASS.** Superseded: F39 ran before F04/F05 landed and said "no report on disk has yet performed it". At my cutoff both reviews exist and PASS. F29 BR-25 records the same supersession; the integrator must use the latest receipts.
5. **F29 CC-14 (no depth verdict) vs F21 IMPROVED.** Superseded by F21, which landed after F29 compiled.
6. **F40 defective output (reported exactly as observed).** `F40-receipt.md` claims "Receipt skeleton written. `.ufo/waves/round-94/followup-receipt.json`" but no such file exists anywhere (`find . -name followup-receipt.json` at lane root and fleet root → nothing; `ls .ufo/waves/round-94/` → no receipt), and the report still contains unsubstituted placeholders (`SNAPSHOT_TIME`, `SNAPSHOT_COUNT`, `MISSING_LIST`, `FINAL_AUDIT_SUMMARY`, `BOTTOM_LINE` at `F40-receipt.md:36,43,44,86,100`). Its collision audit (35 reports, no duplicate prefixes, no header mismatches at 15:45:30) is historical and was independently superseded by the final count of 39 before this seat. F40's bookkeeping must not be credited; the integrator must produce the real FOLLOW-UP receipt from the dispatch result (C-3).
7. **Trivial miscounts, no verdict impact.** F01's "(11 files listed)" for the r94 directory vs the actual 10 files (`ls -la` → 10); F19's self-test quote "(21 cases)" vs 20 (F29 BR-23). Both are transcription slips in otherwise reproduced evidence.
8. **Stale declaration field (CC-01).** `wave-spec.json:15` still says `requested_seats: 32` / `status: "not-dispatched"` while `LOG.md:2687` declares a 40-seat dispatched FOLLOW-UP (within the 32–64 authorization). F18, F25, F29, F40 all flag it. Declaration-accuracy item → C-3.
9. **Low-severity items that assert no harm.** F20-1…F20-7 (anti-overclaim critic: sole new unbounded phrase is the interpretive label "their near-miss", `README.md:9`); F23 §3 residual (renamed `claims` key + removed map row → silent PASS, out of declared canonical scope); F35 §5 `--help` exits 0 with zero RESULT lines; F11 notes 1–3; F22's coverage bounds. All recorded as bounds (C-5/C-6), none contradicts a claim.

## 5. Per-axis verdict table (all six axes; verdict words only, no scalars)

| Axis | Verdict | Primary evidence | Bounds (recorded, not hidden) |
|---|---|---|---|
| **depth** | **improved** | F21 IMPROVED with 3 spot replays; my replays (counts, equality, both-deps, CLEAN, 14/14 support, 14/14 map); F01–F06, F20, F34 | One authored-minute fixture; support = mapped minute + F04's bounded whole-claim review, not authentication; relation scoped "for this crossing only"; dependency-reduction undetectable (BR-01) |
| **coverage** | **improved (bounded)** | F22: first positive-path two-parent dependency, first agreement-type relation, first explicit cross-fixture continuation, first raw-JSON↔map tool surface; my census 168 dirs; 0 corpus modifications | One fixture + one tool; no new checker finding template; legacy maps exit 2 (`unsupported_map`); relation `type` not gate-enforced; docs/index not yet updated |
| **calibration** | **improved (bounded)** | F23 PASS/improved with 19 probes; my counterexample, self-test 20/20, frozen replay, negatives; F07–F12, F24, F35 | Canonical one-obligation-per-row scope only; renamed-`claims`-key residual; mapping completeness + source-ID agreement only — no entailment/fidelity/chronology/rights/permission/canon |
| **operability** | **improved (bounded)** | F24 PASS + F18 PASS; my replays of every documented command and the 0/1/2 contract | `--help` exit 0 / zero RESULT lines; self-test scratch under the repo root survives `kill -9` and is not gitignored; tool not relocatable for `--self-test`; README/registry entry pending (C-1) |
| **freshness** | **unchanged (no improvement; no harm)** | F17 FAIL + F25 FAIL sustained (S1–S4 reproduce; CC-03…CC-07); live pins all fresh (checker/boundary/frozen digests verified — F17 F-e/F-h, F25 "live pins"; r94 knowledge metadata fresh — F17 F-a, F38); C9 r94 append pending (`LOG.md:2671`) | 4 unrepaired docs items + 2 carried stale records (`LOG.md:2312-2314`, `wave-spec.json` followup) + `r91-c9-watch.md:54` stale HEAD line; no r94-introduced staleness |
| **adjacency** | **unchanged (PASS)** | F26 PASS + F19 PASS; `PROVINCE.md` byte-identical (blob `7c599c3`); no sibling writes; mythology stays editorial; rights/mechanics refused | Sibling check is a bounded mtime sweep + string-leak grep; transient scratch note |

## 6. Admission-rule application

- C1 verifies on the delivered revision: **YES** (§2; F39's acceptance table with V4/V7 now demonstrated by F04/F05).
- C2 verifies on the delivered revision: **YES** (§3).
- No axis is harmed: **YES** — depth improved; coverage improved (bounded); calibration improved (bounded); operability improved (bounded); freshness unchanged (no improvement, no harm — F25's own wording); adjacency unchanged. The FAIL-class seats (F15, F17, F25, F37) are bounded findings, none a regression introduced by this round (F15's non-detection is pre-existing checker scope; the freshness/doc items are unrepaired pre-existing or declared-pending, not r94-created).

**Recommendation: ADMIT round 94 (C1 depth + C2 calibration), conditional on C-1…C-6.** This is an admission recommendation, not an admission act: no capability row, no `[x]`, no promotion, no saturation, no fleet report or MANIFEST entry is made here, and r95 must not start before L1 records the closure.

## 7. Exact conditions of admission

- **C-1 (docs/registry integration, before closure).** Apply the W25 proposals now that products exist and run: `SKILL.md` gate-registry row for `map_obligations` (entry `python3 corpus/tools/map_obligations.py <cluster-directory>`, verdict map 0/1/2, `--self-test` citing the 20 persisted cases, pinned values = the contract + the frozen `expected.json`); `corpus/tools/README.md` addendum; `corpus/fixtures/README.md` Round-94 section with the census re-declared as measured at the candidate revision (168 dirs / 34 clean / 134 negative / 421 violation lines) plus a dated note that this file's W05 baseline pin `a13d1af3…` changes (F30 P3); `corpus/README.md` index update. (F30 P1–P4; F17/F25 CC-03…CC-05; F37.)
- **C-2 (C9 watch).** Append the due r94 re-check row to `corpus/knowledge/r91-c9-watch.md` and repair or dated-erratum the stale HEAD-bound line at `:54` (R10-erratum pattern), keeping the checker pin `ff9fd2aa…`. (F17 S4; F25; CC-06; CR-04.)
- **C-3 (declaration/receipt reconciliation).** Reconcile `wave-spec.json` `followup` with the actual dispatch (40 seats per `LOG.md:2687`, status dispatched) or record the divergence; record the actual FOLLOW-UP receipt (seat outcomes, agent IDs) after the dispatch returns; **do not credit F40's claimed-but-absent `followup-receipt.json`** — produce it from the real result. Also decide durability for F02's fleet-root copy (F29 CC-11). (CC-01/CC-10/CC-11.)
- **C-4 (failed-output gaps).** Record the W20 gap (31/32 usable; `work-receipt.json:56-57`) and the F40 defect (claimed receipt absent; placeholders unfilled) as failed-output gaps; neither is usable seat output.
- **C-5 (sustained findings recorded, not dropped).** The closure record must carry F15 mutation (a) (BR-01), F17/F25 freshness findings (CC-03…CC-07), F37 doc-map failure, F23 §3 residual, F35 `--help` caveat, and the self-test scratch residual (BR-05) as bounded findings/conditions — and must state that no axis was harmed, so nothing is re-rolled.
- **C-6 (capability decision).** `map_obligations` may be registered as a gate only with the declared scope (canonical one-obligation-per-row mapping completeness + source-ID agreement; no entailment/fidelity/authenticity/chronology/rights/permission/canon) and the named bounds (BR-01…BR-04, BR-16, BR-24, legacy maps exit 2). No numerical rubric, no saturation line, no promotion.
- **C-7 (carried, r95 candidates; not admission blockers).** BR-01 dependency-reduction detection; BR-02 schema-drift class; BR-05 scratch relocation; BR-07/08/09 map/README/schema polish; BR-19/20 wording; CR-01 AST anchors; CR-02/05/06/07 r93-carried debts.

## 8. Limits of this adjudication

- Same-lane review: this is not outside non-author verification; no external authentication, no source-text truth, no rights finding is made or implied.
- F29's ledger (compiled before F21/F40) and F39 (before F04/F05) are superseded where noted; all other reports were read in full at the cutoff. I did not re-run every seat's probes — I replayed the load-bearing ones (counts/equality/deps, checker, support, map positives + negatives + self-test + frozen, census, W05 pins, counterexample, mutation (a), diff/blob scope, citation spot-checks).
- No numeric axis scores are invented; verdict words only.

**Bottom line: PASS — ADMIT round 94 recommended: C1 (depth) and C2 (calibration) both verify on the delivered revision `abbc3e0`/HEAD `65a9329` with no axis harmed (depth/coverage/calibration/operability improved, freshness and adjacency unchanged), conditional on C-1…C-6, with F15/F17/F25/F37 sustained as bounded findings and F40's absent receipt JSON not credited.**
