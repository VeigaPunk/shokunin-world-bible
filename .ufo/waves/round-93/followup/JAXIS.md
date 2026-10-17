# JAXIS — Synthesizer (round-93 follow-up, world-bible lane)

Seat JAXIS, round-93 follow-up wave. Mission: read all `followup/J*.md` (the judge
seats JCAL1–JCAL5, JCOV1–JCOV2, JDEP2, JDEP4) plus every other follow-up report
present, rule the per-axis verdict table (depth / coverage / calibration), reconcile
cross-seat disagreements, and recommend the admission path.

Judgment surface: the committed tree at `65838f867d6ece8e7b8bdcc4ffc667a08a1b785e`
(the r93 WORK commit; baseline `87779a0`). The tracked tree was clean at every check —
the only untracked path all run was `.ufo/waves/round-93/followup/`. Peer reports are
testimony; every verdict below rests on committed-tree measurements — mine (next
section) or a named seat's with exact command + observed output. No commit, no push;
repo writes are this report and `followup/JAXIS-verdicts.json` only. Scratch was one
`/tmp` file (`jaxis-mutated-doc.md`, the cert-tool mutation control), removed.

## Work performed

- **Read all 22 follow-up `.md` reports**: E1, H4, H5, JCAL1, JCAL2, JCAL3, JCAL4,
  JCAL5, JCOV1, JCOV2, JDEP2, JDEP4, P1, P2, P3, P4, Q1, Q1-r94-proposal, SE2, V2,
  X1, X2. Of the 11 machine artifacts, `JCAL1-delta.json` was read in full; the other
  10 are receipt payloads (`*-tuples/census/probes/evidence/debt/receipts/manifest`)
  whose load-bearing numbers I consumed through their parent reports' embedded
  commands and outputs and through my own re-runs. No report landed after my read
  pass began (last arrival `JCOV2.md` 12:40; my read pass started 12:43).
- **Dependency receipts** (block contract: two 60 s wait-checks; batch landed late):

```text
CHECK t=0s   2026-10-17T12:07:14-03:00 HEAD=65838f8 files=0
CHECK t=60s  2026-10-17T12:08:14-03:00 HEAD=65838f8 files=1   (JCAL1-delta.json)
CHECK t=120s 2026-10-17T12:09:14-03:00 HEAD=65838f8 files=1
TERMINAL status=0 checks=2
CHECK3.1 t=+60m 2026-10-17T12:42:55-03:00 md_files=22 all_files=33   (early-exit poll)
```

  Per the contract I then worked with what existed: my verification battery (below)
  ran during the landing window, and the full batch was read once present.
- **Ran my own first-hand battery on the committed tree before reading any verdict**
  (next section), so the table in §F1 is anchored on every claim family directly, not
  only on testimony.
- **Reconciled four cross-seat disagreements** (§F2). None survived as a data
  conflict; one genuine classification item is handed to L1 open.
- Did not re-run the full 167-fixture census or the 14-case cert replay beyond the
  spot runs below: five independent census receipts agree (B1=B2 byte-identical at
  `185ce02d`; JCAL1=JCAL5=H4 on shared fields; V2's tuple replay), and the cert-tool
  positive run is byte-identical across ≥6 executions (CERT patch-stage, H5, JCAL2,
  JDEP4, V2, SE2, mine).

## Before → after measurements

All commands from `lore-shokunin/` at HEAD `65838f8`; outputs verbatim.

**1. Identities and the unchanged-checker claim.**

```sh
git rev-parse HEAD && git status --porcelain | head -3
sha256sum corpus/fixtures/check_bible.py
git diff 87779a0..65838f8 -- corpus/fixtures/check_bible.py | wc -l
git ls-tree -d -r -t 87779a0 -- corpus | wc -l && git ls-tree -d -r -t 65838f8 -- corpus | wc -l
```

```text
65838f867d6ece8e7b8bdcc4ffc667a08a1b785e
?? .ufo/waves/round-93/followup/
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
0
207
208
```

Checker byte-identical across the round (claim upheld first-hand); corpus tree
207 → 208 dirs, the +1 being `r93-m2-kojiki-cluster` (consistent with "167 direct
fixture dirs, 0 changed + 1 new"; JCAL1/JCAL5/H4/V2 agree at tuple level).

**2. Cert tool — positive and mutation control.**

```sh
python3 corpus/tools/boundary_doc_check.py; echo "EXIT=$?"
# /tmp copy with one anchor range mutated (check_bible.py:NNN → 9NNN), then:
python3 corpus/tools/boundary_doc_check.py --doc /tmp/jaxis-mutated-doc.md; echo "EXIT=$?"
```

```text
CHECK receipt replay: PASS / CHECK code anchors: PASS / CHECK document structure: PASS
replay_receipts=3/3  replay_cases=14/14  anchors=2/2
h1_count=1  duplicate_headings=0  instruction_markers=0
CERTIFIED                       EXIT=0
FAIL: unresolved anchor check_bible.py:9212-224: checker has 428 lines
CERTIFICATION FAIL              EXIT=1
```

**3. Discrimination harness — both documented modes.**

```sh
python3 corpus/tools/discriminate_check.py; echo "EXIT=$?"
python3 corpus/tools/discriminate_check.py --checker e97613c; echo "EXIT=$?"
```

```text
RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression   EXIT=0
REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — …         EXIT=2
```

Exactly the semantics the new `corpus/tools/README.md` section documents.

**4. Third cluster — support receipt and shape.**

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r93-m2-kojiki-cluster; echo "EXIT=$?"
ls corpus/fixtures/r93-m2-kojiki-cluster/*.json | wc -l   # 5
ls corpus/fixtures/r93-m2-kojiki-cluster/*.md  | wc -l    # 6
```

```text
INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15; DISTINCT-ANCHORS 15/15
SOURCE-SUPPORT 12/12; EDITORIAL-ANCHORS 3/3; … RESULT PASS   EXIT=0
```

The claim's "12 JSON + 3 editorial" counts **facts and rows, not files** — the dir is
11 files (5 JSON + 6 md); the map inventories 12 source-attributed JSON facts and 3
editorial comparison rows, all PASS (JCOV1 and X1 re-derived byte-identically from a
path-limited archive; JCOV2 replayed all 15 anchors checker-free).

**5. Watch row 2, ledger row, and the venue repair — diffs vs baseline.**

```sh
git diff 87779a0..65838f8 -- corpus/knowledge/r91-c9-watch.md corpus/knowledge/reference-ledger.md corpus/knowledge/r88-sourced-inspiration-decision-table.md
```

Observed: watch gains exactly one row — `| 2026-10-17 (r93) | ff9fd2aa…d1421 |
**DISCRIMINATION HELD** — re-check 2 (seat X1, r93) … Next re-check: r94. |` (two
distinct dated rows, first-hand); ledger gains the Chamberlain row (rights and
AI-training both "Open question — not assessed"; narrow editorial comparison only);
decision-table diff shows the Manual R9 gate / Required record / Receipt boundary /
worked-example blocks moved INSIDE the R9 appendix, the R9 row gaining the
manual-review-receipt sentence, the doubled "Failed-gate disposition (clarified
r92):" label reduced to one, and the R8 appendix's worked example replaced by the
seven-threshold-names case. `git diff 87779a0..65838f8 --
corpus/knowledge/holder-assessment-boundary.md` → empty: the r92 gate-C repairs
(tail/dups/range/pin/label, K1 README patch, post-repair re-certification) are in the
**baseline** `87779a0` closure commit, so r93 judges a clean doc.

**6. R8 dossier replay.**

```sh
D2_DOSSIER=corpus/knowledge/r93-r8-worked-example.md python3 - <<'PY' … PY   # dossier :41-61
```

```text
gate_result: PASS / contrary_evidence: PASS / separability_rationale: PASS /
scope: PASS / next_action: PASS / R8 record fields: 5/5     EXIT=0
```

## Findings & named debt

### F1 — Per-axis verdict table

Verdicts are per axis, never scalars, never netted across axes; sub-harm is named
inside the axis that carries it. Every seat that scanned for trades found none
(JCAL1, JCAL3, JCAL4, JCOV1, JDEP4, SE2, V2 state this explicitly); "unchanged"
entries below are the desired no-regression property, not trades.

| Axis | Verdict | Positive evidence (measuring seats; ✓ = my own run) | Named bounds (within this axis) |
|---|---|---|---|
| **depth** (C1) | **improved (bounded)** | Q92-002 closed on the delivered tree: all four defect counts flipped (dup label 2→1, Kesh example 0→1, gate/record/receipt 0/0/0→1/1/1, old example 1→0) — JCAL4 B2, V2, H5, P2, SE2, Q1; R9 manual-gate wording internally consistent, no over-claim (JCAL4 B3); dossier committed with 5 required record fields, replay 5/5 ✓ (JCAL4 B1, X2 22-probe field audit, V2); cert tool committed, `CERTIFIED` exit 0 ✓, byte-identical across ≥6 independent executions; fails closed with named failures on tampered checker / `{expected}` contradiction / receipt drift / anchor-beyond-range / pin drift (JCAL2 A2/A3, JDEP4 M3, SE2, ✓ my mutation) — the patch-only candidate CB-audit falsified had exit 0 on two of these | (a) anchor census covers **2 of ~127** colon-refs; an in-range wrong-anchor mutation certifies (SE2 live probe; JDEP2 2/127 sizing + `:322→:325` drift demo) — AST/content-signature debt real, r94; (b) C9 gate is needle-narrow: CB-audit's verbatim `{details}` contradiction **certifies** (JDEP4 M4) — the historical harm's phrasing; (c) doc:78's full-form baseline anchor is range-checked against the wrong revision (JDEP2); (d) `corpus/tools/README.md` has **no** certifier section — the "AST debt named r94" sub-claim is half-landed (JCAL2 A4 NOT CONFIRMED, E1, H5, JDEP4 F2(v)), and `CERTIFIED` is unbounded in docs (E1); (e) unguarded `--doc`/`--checker` reads crash unnamed (fail-closed; JCAL2, JDEP2, SE2); (f) dossier omits the integration-editor owner role and the `element map` recording target (X2, bounded — not decision-required fields); (g) pin is a constant, not Gate A's CLI argument (Q1) |
| **coverage** (C2) | **improved (bounded)** | Third sourced-mythology family lands: CLEAN census tuple (exit 0, 0 violations, `afe570fc…`) inside a zero-drift census 166→167 (JCAL1, JCAL5 method-varied double census, H4, V2, ✓); support receipt 12/12+3/3 `RESULT PASS` ✓, byte-identical archive vs live vs recorded (JCOV1, X1 ×4, V2, JDEP4 M6); 15/15 anchors independently replayed (JCOV2); zero shared referents **lexically** corroborated by three independent scans — JCOV1 JSON-level, JCOV2 normalized-key, V2 8 referent families, all pairwise intersections empty incl. the r87∩r88 control; attribution verified against the live Terebess page incl. Part III locator and verbatim clauses (JCAL4 B4, JCOV2); ledger row + three-question discipline + bounded symbolism verified (JCOV2); both support-path checkers byte-unchanged (JCOV1: `ff9fd2aa` + `55a5eb27`) | (a) the **integrated** zero-referent conclusion is author-side + lexical only: the cluster README itself defers M6's M2-specific semantic review (R93-N2) — do not promote the claim's strength until it lands (JCOV1, JCOV2, Q1); (b) commit message says "10 JSON" — measured 12 (V2, JDEP4 M6, X1, SE2; 10 was M1's losing candidate's count); (c) fixtures README indexes neither Round 91 nor the new cluster (two rounds deep; H5, Q1 Q92-005); (d) rights/AI-training/edition identity open by design (correctly) |
| **calibration** (C3) | **improved (bounded)** | Watch row 2 landed: two distinct dated rows, ruling retained, gate 3 unmet, **next-recheck r94 pointer present** (closes Q92-010's pointer debt) ✓ (JCAL3, V2, JDEP4 F5); discrimination harness promoted to `corpus/tools/discriminate_check.py`, both documented modes verified ✓ and by JCAL3/V2/SE2/P2/JDEP4 (exit 0 HELD / exit 2 REGRESSION-DETECTED via `--checker e97613c`, pin `matches_pin=True`); census behavior zero-drift under four methods (sorted / reverse / seeded-shuffle / git-archive — JCAL5), 421 = 421 violation lines; baseline receipts proven faithful (JCAL5 regenerated-base == B1, 0 mismatches); receipts byte-parity vs baseline on all pre-existing clusters (JCOV1 PARITY ×3, X1) | (a) row 2 abbreviates the hash and shares row 1's calendar date (distinct only by the `(r93)` suffix — JCAL3); (b) watch residuals: no pointer to the promoted tool, E3's stable-checkout wording absent (Q1 Q92-010 residuals); (c) `discriminate_check` depends on `e97613c` staying reachable (JCAL3, Q1 R93-N6); (d) trigger gate 3 remains unmet — correctly retained, not a defect; (e) census proves behavior-identity, not byte-identity, of pre-existing fixtures (JCAL1/JCAL5, R93-N7) |

### F2 — Reconciliations (no surviving data conflict)

1. **JCAL2 finding 1 vs JDEP4 M4 (C9 contradiction class).** JCAL2's A3 injected the
   `{expected}` phrasing → named FAIL exit 1 (correct measurement); JDEP4 re-ran
   CB-audit's verbatim `{details}` sentence → **CERTIFIED exit 0** (also correct).
   Resolution: JCAL2's data stands; its conclusion ("directly closes the holes
   CB-audit falsified") and the commit message's "both adversarial probes exit 1"
   overclaim the contradiction class. Closure text must say: pin class closed;
   contradiction class **not** closed for the `{details}` phrasing (the form the
   historical `c2ab3d0` harm actually used).
2. **Q1's "adversarial probes unre-probed by any follow-up seat" vs JCAL2/JDEP4.**
   Landing-order artifact: Q1 audited before those seats wrote. The probes now exist
   (JCAL2 A2/A3, JDEP4 M3/M4, SE2, my mutation run); Q1's flag is superseded — with
   the JDEP4 sharpening above.
3. **JCAL5's "per its README" (AST debt) vs JCAL2 A4.** JCAL2 measured `git grep` →
   zero hits: the README names no such debt. JCAL5's aside is a mis-citation, not a
   competing measurement; JCAL2's finding stands.
4. **Capabilities fourth row: JDEP4 FOR (bounded) vs P3/P4/W2 "unchanged".** A
   classification judgment, not a measurement conflict — JDEP4 F4 lays out both
   readings and the r91 precedent for resolving it. **Handed to L1 open** (§F3
   condition 3). The one forbidden state is entering a row that reads as semantic
   certification (JDEP4 F2 bounds are mandatory under the FOR reading).

### F3 — Admission recommendation

**Admit.** All three axes are improved (bounded); no seat found a harmed axis or a
trade; the checker and both support-path tools are byte-unchanged, so nothing
pre-existing moved (166/166 census tuples identical; receipts byte-parity). Unlike
r92, there is **no content repair list**: every bound above is either correct-as-
delivered-with-named-debt or record wording. The closure commit (LOG/SCORECARD are
unwritten at `65838f8` — Q1 R93-N10, P3/P4 proposals pending) must:

1. Record the Kojiki receipt as **JSON-FACTS 12** + 3 editorial (R93-N5; the commit
   message's "10" is the losing candidate's count).
2. Word certification as **lexical certification only** (receipt replay + 2 strict
   anchors + structure + pin + C9 needles) and state that CB-audit's `{details}`
   contradiction probe still certifies — "both adversarial probes exit 1" must not
   carry into the record.
3. Rule the capabilities classification explicitly: adopt JDEP4's fourth row
   `boundary-document certification` (r93) **with F2's six bounds**, or record
   "table unchanged" — either is honest; silence is not.
4. Keep the zero-shared-referents claim qualified (lexical, author-side + follow-up
   corroboration; M6's M2-specific semantic review pending — in-tree disclaimer).
5. Carry the r94 queue: AST/content-signature anchors (Gate C) + revision-qualified
   anchor grammar; contradiction-class C9 gate or documented tripwire status; cert
   README section with bounds + r94 debt naming; guarded input reads; CLI hash
   argument (Gate A); dossier owner-role/map-target sentence + discoverability link;
   LOG/SCORECARD receipt-number refresh; fixtures README Round-91/93 sections;
   watch row-3 conventions (full hash, date-cell suffix, tool pointer) + E3 wording;
   `e97613c` reachability note. Q1-r94-proposal.md's selection gate (weakest axis by
   L1's ruled words; tie-break open-row counts depth 5 > coverage 3 > calibration 2)
   is the ready ranking input.

### F4 — Named debt rollup (owner-ready)

`D-r93-ast-anchors` (SE2/JDEP2/JCAL2; demonstrated live) · `D-r93-c9-contradiction`
(JDEP4 M4) · `D-r93-cert-readme` + `CERTIFIED` scope sentence (JCAL2 A4/E1) ·
`D-r93-cert-guarded-reads` (JCAL2/JDEP2/SE2) · `D-r93-pin-constant` (Q1) ·
`D-r93-cert-wrong-revision-anchor` doc:78 (JDEP2) · `D-r93-dossier-owner` (X2) ·
`D-r93-dossier-links` (Q1 R93-N3) · `D-r93-zero-referent-semantic` (R93-N2; README/
JCOV1/JCOV2) · `D-r93-record-refresh` (X1/JDEP4 F6) · `D-r93-commit-msg-12`
(R93-N5) · `D-r93-fixtures-readme-index` (H5/Q92-005, two rounds deep) ·
`D-r93-watch-row2-cosmetics` + tool pointer + E3 wording (JCAL3/Q1) ·
`D-r93-e97613c-reachability` (JCAL3/Q1 R93-N6) · `D-r93-silent-venue-repair`
(JCAL4 F1) · `D-r93-capabilities-classification` (L1) · `D-r93-boundary-doc-header`
(stale round-90 provenance; JDEP4 F6(iv)) · `D-r93-behavior-not-byte`
(JCAL1/JCAL5). Carried unchanged: Q92-004, Q92-008 residual, Q92-006/007/009
(process), R93-N9 (rights/training, open by design), C5-001, stream-asymmetry note.
Machine-readable rollup: `followup/JAXIS-verdicts.json`.

### Agreements

Checker unchanged (✓, H4 lineage, JCOV1, JCAL1/3/5, V2, E1, SE2, P2); census
166→167 zero-drift (five receipts + ✓); cert tool positive + fail-closed (✓ + 6
seats); discrimination 0/2 both modes (✓ + 5 seats); Q92-002 closed (JCAL4/V2/H5/
P2/SE2/Q1 + ✓ diff); cluster receipts 12+3 PASS (✓ + 4 seats, byte-identical);
venue/dossier/cluster/wording all improved with no over-claim found (JCAL4's
adversarial sweep); SHONEN unchanged, no promotion (P4, P3).

## Handoff

- **Deliverables:** `followup/JAXIS.md` (this report) and
  `followup/JAXIS-verdicts.json` (machine-readable: per-axis verdicts,
  reconciliations, admission conditions, debt rollup, agreements, gaps, receipts).
  No other tracked write; no commit; no push; scratch removed.
- **The ruling in one paragraph:** r93 delivers all three claimed axes and every
  load-bearing claim reproduces from the committed tree — depth improved (bounded)
  on a genuinely closed Q92-002, a replayable dossier, and a committed fail-closed
  certifier whose named limits (2/127 anchor census, needle-narrow C9 gate,
  undocumented surface) are r94 debt, not defects in what landed; coverage improved
  (bounded) on a third sourced family whose receipts are byte-stable and whose
  zero-referent claim is correctly qualified pending M6's semantic review;
  calibration improved (bounded) on watch row 2 with the r94 pointer and a promoted,
  doubly-verified discriminator. Nothing regressed anywhere measured. **Admit**, with
  the five record conditions in §F3; the only open classification (capabilities row
  FOR vs unchanged) is L1's, with JDEP4 F4 as the decision frame.
- **Gaps:** the two contract wait-checks saw only `JCAL1-delta.json` (batch landed
  12:07–12:40; contract discharged, full batch read before writing); I read the 10
  non-JCAL1 `.json` artifacts through their parents rather than byte-for-byte;
  JDEP2's ~119-ref content audit was probe-side (script deleted per file-frugality —
  its negative result "no wrong-content anchor" rests on that one seat's eyeball
  pass, corroborated only by the doc's r92-closure repair provenance); no closure
  commit existed at write time, so all record-wording conditions are forward
  obligations on the scribe.
