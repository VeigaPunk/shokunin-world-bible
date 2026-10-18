# PROPOSAL ONLY — Round 90 SCORECARD section (P2, follow-up wave)

Follow-up proposal. This supersedes the phase-1 draft
`.ufo/waves/round-90/patches/W2-scorecard-r90.proposal.md` as the candidate section
text, because W2 measured only the baseline; this draft measures the **delivered tree
at `ca7f9ef`** (tree clean, `HEAD=ca7f9ef1646cf3fcbe58747785a8cb2e9075ae13`). Do not
append without L1 ruling. All three verdicts are **PENDING-L1**; scores remain
unassigned (no rubric exists). Evidence references the follow-up judge seats that
landed during this run (JCAL/JDEP/JCOV/H/CB1/Q2 under `followup/`); their
reproductions are corroboration, not L1 verdicts.

Draft section text (for `SCORECARD.md`) begins below.

---

## Round 90 — luna round 4 of 12 (2026-10-17)

Two-wave regimen round: work wave (33 seats — 29 roster rows + the 4-seat
supplementary batch M5/C9/W3/SE3; `openai-codex/gpt-6-luna-max`), follow-up wave
(`opencode-go/deepseek-v4.1-flash`; `lane_requested=hyper/deepseek-v4.1-flash`,
failover `hyper-402`). Spec `.ufo/waves/round-90/wave-spec.md` (+ landing record and
closure amendments: roster correction 32→29 declared vs 33 delivered, C9 integer-only
tick-gating ruling). Baseline `e97613c` (r89 closure); work commit `ca7f9ef`; closure
= this section's commit. Scores remain unmeasured (no rubric); rows below are claims
with counting commands and measured commits. Freeze-then-verify (r88-I1): delivered
`corpus/fixtures/check_bible.py` = X2-null-gate + X3-tick-gating composed on
`e97613c`, sha256 `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`
(baseline `e2bb9639…`) — PASS, no blocking finding; independently composed by
JCAL1/JCAL2/JCAL4/JDEP3/H2/H4/CB1/Q2 with the same hash.

| LIVE axis | r90 verdict | Evidence and limit |
|---|---|---|
| calibration | PENDING-L1 | Delivered tree `ca7f9ef` (P2 receipts in `followup/P2.md`; all commands re-run post-freeze): census replay over 164 fixture dirs = the 160 prior tuples unchanged byte-identical (0 changed, 0 removed, 0 exit flips, stderr empty; 399→417 violation lines, the 18 new lines all from the four new fixtures) + 4 new durable fixtures — `r90-c1-rawpresent-from` (5 findings), `-to` (5), `-source` (4), `r90-c1-three-causes` (4; key-valid, three latching causes: invalid tick + absent holder + absent source). Repaired shapes on the delivered checker (P2 probes): null-from chain definite — `provenance chain break; expected from_holder 'mira', got None` (the vacuous `0 raw / 0 indexed` clause is gone corpus-wide; JCAL2 swept 0 occurrences); unrelated-identity tick definite; tick inversion under a genuinely unresolved compared holder definite (`provenance tick 1 must be greater than previous tick 3`) per the C9 integer-only ruling recorded in the spec's closure amendments. The genuinely unresolved non-null chain break keeps its exact r89 qualified wording (FN-2 pair tuple-stable 1→1/2→2; present in the canonical B1/B2 census manifests). Corroboration: five independent censuses (JCAL1/JCAL2/H2/H4 + JCOV2 for the C2 side) reproduce 160/160 identity and 0 exit changes; JCAL1 confirms both directions of the repair coexist with no over-correction; B1=B2 receipts byte-equal. Bounds (named, not netted): (a) the two repaired shapes are pinned only by wave-side receipts — all four new fixtures produce byte-identical output under baseline and delivered checkers (they pin FN-1 raw-present wording and the ≥3-cause record, both unchanged behavior), and no delivered fixture emits `got None`, so a regression of the repaired shapes would not be census-visible (JCAL2-D1, JCAL4-F3, H2 debt 2); r91 candidate: one durable fixture per repaired shape. (b) E1 conformance is incomplete on two sub-cases (JCAL4-F1/F2): a null-from chain whose previous holder is unresolved stays qualified (safe direction), and the first-record guard with an unresolved non-null id stays qualified with an internally inconsistent frame; the summary sentence "null chains and tick findings definite" needs those sub-case qualifiers (JCAL4-F4). (c) tick definiteness holds modulo the pre-existing ambiguous-source prefix gate (`r87-probe-source-prefix`; JCAL2-D2). (d) the integer-only reading is a ruling commissioned by C9's reasoning, not by a distinguishing case; the r91 falsification path (promote X1's gate if a tick finding ever needs identity context) stays recorded (C9; spec amendment). (e) documentation parity drifted and is unrepaired at `ca7f9ef`: `corpus/knowledge/holder-assessment-boundary.md` still describes the removed tick-qualification behavior and carries shifted checker line anchors (CB1 D1–D14; refresh proposal `followup/CB1-boundary-refresh.md`), and `corpus/fixtures/README.md` has no Round 90 section indexing the four new fixtures (JCAL1 finding 6; CB1-D12); r88/r89 precedent repairs this class in the closure commit — recorded, not netted. |
| coverage | PENDING-L1 | Delivered tree `ca7f9ef`: in-corpus claim→excerpt maps for both clusters plus one committed support command whose exit + `N/N` print is the receipt. `corpus/fixtures/r87-myth-cluster/claim-excerpt-map.md`: 22 rows (14 JSON-fact rows + 8 Low-Water Hymn clause rows), every row carrying fact pointer, excerpt path:line span, exact anchor, and R9 mode; the five excerpt files carry inline mode labels (the four r89 excerpts + hymn; 5/5). `corpus/fixtures/r88-m3-maya-cluster/claim-excerpt-map.md`: 10 source-attributed JSON facts + 2 symbolism comparisons declared separately; the Spence passage's mode is declared in-map (inline label absent on `source-excerpt.md` — JCOV2-D3). Receipts (P2): `python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster` → `SOURCE-SUPPORT 22/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22` / `RESULT PASS`, exit 0; r88-m3 → `SOURCE-SUPPORT 10/10; … MODES 10/10` / `RESULT PASS`, exit 0; `r89-inspiration-paraphrase` negative control → `SOURCE-SUPPORT 0/0; RETELLING-SUPPORT-ONLY 1 entries (1/1 anchors)`, exit 0 — paraphrase/summary counts zero source support. Span enforcement (the M4 attack's repair): a wrong-line mutation (E1 `:7`→`:6`) on a scratch copy fails closed — exit 1, `FAIL: E1: anchor hit outside declared line span 6 (hit lines: 7)`, `SOURCE-SUPPORT 21/22`; M4's D-M4-1 is closed and JCOV1/JCOV5 independently reproduce it. Delivered C2 files hash-match M1+M2+M3+M5 composed on `e97613c` (P2 check: 5/5 files identical; script `66a3c4bb…`), and W3's independent line-anchor wrapper reproduces 22/22 and 10/10. Corroboration: JCOV2 whole-claim spot audit 9/9 (pledge scope and the unresolved T3/T4 pair preserved); JCOV5 coverage improved (bounded), no sibling-province bleed. Bounds: (a) `22/22` counts rows, not JSON facts — 14 JSON rows + 8 editorial hymn rows, and two JSON obligations are folded into an H4 row by the map's own disclosure (JCOV2-D1, JCOV1-N1); quote it as rows unless the split is printed. (b) mode truthfulness is self-declared consistency, not evidence that a `verbatim` label is true (JCOV1-R1; `corpus/tools/README.md` disclaims). (c) one committed script, per-cluster receipts — no aggregate `32/32` (JCOV1 D-M4-2: spec wording satisfied, nothing demanded). (d) anchors are plain `grep -nF` substrings; mid-word occurrences pass (JCOV5 ND-2; no delivered anchor affected). (e) K1's two chousa cross-reference lines landed only in the wave artifact, not the governing table — Q89-047's delivered-governance half stays open (JCOV5 ND-1). (f) carried residues: `symbolism-clause-map.md:16`'s "the checker does not read this map" is now false for the new tool (JCOV2-D2); ledger row-5 text (Q89-015) and Spence row placement (Q89-020) unchanged; source-excerpt imprint unverified from the cited Gutenberg surface (JCOV2-D4); `keeps_watch_with` still semantics-free to the checker (JCOV2-D5, pre-existing). |
| depth | PENDING-L1 | Delivered tree `ca7f9ef`: the three JDEP2 sub-cases are DECIDED in delivered text as appendices to `corpus/knowledge/r88-sourced-inspiration-decision-table.md` (R8 `:28-38`, R9 `:40-47`, R10 `:49-59`), merged from seats D1/D2 per R1's recommendation with a provenance note. R8 — a dated neutral `possible influence: unverified` note records uncertainty, not influence; R2 (no source used) requires BOTH the creator's no-source account AND no contrary source-specific evidence AND only a commonplace motif; the `external-only / unverified inspiration` marker is reserved for established general-motif use with independent in-world support. R9 — translator name alone with an unverified source/version link FAILS R5; narrow exception only where a reliable bibliographic record ties the delivered passage and translator to a named source work, supporting only a claim about that identified translation. R10 — shared names/IDs are comparison keys, not identity; compared-and-dismissed overlaps go to the incoming cluster README under `## R10 comparison outcomes`; only a source-backed shared referent/field/occasion with incompatible assertions enters `corpus/knowledge/cross-cluster-contradictions.md`. Register: the live register is correctly absent; JDEP3 re-verified zero intersection between the clusters across entity/source/timeline/place ids, relation tuples, whole-word text, and anchor strings; the r89 demo file remains explicitly hypothetical; J3's collision checks show the r90 fixtures and maps manufactured no false referent, and the register holds no example names (JDEP3 F1–F4). Retroactivity: the r87 ETCSL marker, the r88-m3 Spence passage, and r87's local Hara/Sen contradiction are unaffected. Bounds: JDEP2's adversarial classification is partially covered per row — R8 leaves the failed-gate disposition, the parent-row-vs-appendix withhold-scope precedence, dispute routing, and the note-removal step unspecified; R9 leaves the reprint-vs-edition identity boundary and the "reliable" criterion undefined and notes the support command would count an unidentified-version `translation` row as full source support (zero exposure today: both clusters are `verbatim`-only, no translation rows); R10 does not scope the `source_id` namespace and defines no register/README schema (prospective; source-id sets disjoint). JDEP3 adds: the landed-clusters scoping rule exists only in wave text, not in the knowledge file; register/`## R10 comparison outcomes` conventions await a first real entry. Appendices carry owner/trigger/rule; worked examples remain wave-side (D1/D2/E2/R1/JDEP2 reports) rather than in-corpus. |

Learning trends: expansion improved (164 fixture dirs; `corpus/tools/` added — the
lane's first in-corpus tooling; 36 files changed in `ca7f9ef`); quality improved
(checker hedges repaired with the whole prior census byte-stable; both clusters mapped
with R9 modes and one reproducible span-enforced support command; three governance
sub-cases decided); discernment improved (53-row debt ledger
`followup/Q1-r90-debt.json`; claim-text corrections named and recorded: `22/22` =
rows incl. 8 editorial hymn rows; the null-chain sub-case qualifier; C9's ruling vs
its falsification path; the follow-up wave independently reproduced and bounded every
claim — JCAL1/JCAL2/JCAL4/JDEP2/JDEP3/JCOV1/JCOV2/JCOV5/H2/H4/CB1/Q2/Q1).

Capabilities: r90 adds its **third row** to the repertoire table (recommended;
see below). Alternative for L1: merge the row's content into the r89 row's evidence
pointer (a durability upgrade over the wave-side S2 map) and keep two rows — either
reading is defensible, but the content should not be dropped: it is r90's strongest
demonstrated capability.

| Capability | What it can now do | Evidence pointer | First-working round |
|---|---|---|---|
| R9-aware span-enforced support receipt | Run one committed in-corpus command that validates every mapped claim→excerpt anchor inside its declared line span and counts only `verbatim`/`translation` entries as source support; paraphrase/summary entries count zero and mode mismatch or an out-of-span hit fails closed | `PYTHONDONTWRITEBYTECODE=1 python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster` → `SOURCE-SUPPORT 22/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22` / `RESULT PASS`, exit 0; same script on `r88-m3-maya-cluster` → `10/10 …` exit 0; `r89-inspiration-paraphrase` → `SOURCE-SUPPORT 0/0 … RETELLING-SUPPORT-ONLY 1 entries (1/1 anchors)` exit 0; wrong-line mutation → exit 1 with an out-of-span failure | r90 |

planned (r91, from Q1 with L1 adoption; craft selection conditional on the ruled
lowest axis): phase-0 gate first — hash-stamped landing/freeze manifest, machine-
readable roster, requested/served lane + failover fields, and any integrator amendment
with before/after hashes, confirmed by a non-author verifier (Q1; Q2-P2 proposes a
`wave-spec.json` + validator whose negative control is r90's own 32/29/33 counts and
composition-without-artifact). Then the ruled axis: (1) calibration — durable fixtures
for the two repaired shapes (later-record `from_holder: null` definite line; tick
inversion under an unresolved compared holder), decide E1's two unresolved sub-cases
(extend the fix or qualify the claim text), keep the ambiguous-source prefix bound;
(2) coverage — a Round 90 section in `corpus/fixtures/README.md` indexing the four new
fixtures, the receipt-label split (`rows` vs JSON facts), the stale tool note fix, the
source-excerpt inline label, decide K1's chousa cross-references (land or reject with
rationale), ledger residues; (3) depth — R8 failed-gate disposition + withhold-scope
precedence + removal step, R9 reprint/edition identity + "reliable" criterion + the
support-command-vs-appendix translation boundary, R10 `source_id` namespace scoping +
register/README schema, move the landed-clusters scoping rule into the knowledge file.
Process: Q2's three improvements (committed poll helper with margin + TERM trap;
roster-as-data + validator; scratch budget + closure sweep). Exploratory: Q89-046
expectation-parity harness with the named operator acceptance path (deferred
acceptance if unavailable).
saturation: not declared (no rubric; nudge not triggered). retired: none.

SHONEN: unchanged at `ca7f9ef` (`git diff --stat e97613c ca7f9ef -- SHONEN.md`
empty). Box 1 `[ ]` (no SKILL.md); box 2 `[~]` (the r90 census/support/judge receipts
are the end-to-end task; the closure LOG entry completes the clause); box 3 `[~]`
(instruction surfaces are tree-true except the pending boundary-doc refresh; still no
external verifier — judge seats are lane-internal, not the named non-author operator);
box 4 `[~]` (province-clean per JCOV5; kotodama contract acknowledgement untriggered).
No `[x]`.

Draft section text ends.

---

## P2 receipts (delivered tree `ca7f9ef`; run 2026-10-17, scratch under `/tmp/p2-r90`)

**1. Freeze-then-verify (blocking check).** Command: extract `e97613c` checker,
compose X2+X3 with `patch -s`, hash-compare with the delivered commit and working
tree. Observed:

```text
composed_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
delivered_commit_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
delivered_tree_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
baseline_sha256=e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556
CMP=IDENTICAL
```

**2. Census replay.** Command (from repo root; bytecode writes disabled):
per-directory run of `corpus/fixtures/check_bible.py` over `corpus/fixtures/*/`,
comparing `(exit, stdout_sha256, violation_count)` against
`patches/B1-tuples.json`/`B2-tuples.json`. Observed:

```text
B1_B2_equal= True B1_count= 160
fn2_manifest_entry r89-fn2-unresolved-chain-break: present=True
fn2_manifest_entry r89-fn2-control: present=True
fixtures=164 baseline=160 unchanged=160 changed=0 new=4 exit_changes=0
new_dirs= [('r90-c1-rawpresent-from', 1, 5), ('r90-c1-rawpresent-source', 1, 4),
           ('r90-c1-rawpresent-to', 1, 5), ('r90-c1-three-causes', 1, 4)]
changed_dirs= []   exit_changes= []
violation_lines=417   (exits: 32 clean / 132 violation)
```

**3. Hedged-shape probes against the delivered checker** (C9-style reconstruction of
the four semantic probes from `r89-fn2-unresolved-chain-break`, built under
`/tmp/p2-r90/probes`, symlinked ancillary JSON). Observed:

```text
=== chain-unresolved (genuinely unresolved non-null expected holder) ===
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
2 violation(s); no canon changed    exit=1

=== tick-relevant-unresolved ===
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3
2 violation(s); no canon changed    exit=1

=== null-from-chain ===
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1]: provenance chain break; expected from_holder 'mira', got None
2 violation(s); no canon changed    exit=1

=== unrelated-duplicate-tick ===
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3
2 violation(s); no canon changed    exit=1
```

**4. Support command and span attack.** `python3 corpus/tools/support_check.py
<cluster>` run on r87, r88-m3, r89-paraphrase → `22/22`, `10/10`, `0/0
retelling-only` respectively, all `RESULT PASS`, exit 0. Wrong-line attack on a
scratch copy of the r87 cluster (E1 `gate-witness-excerpt.md:7` → `:6`): exit 1,
`FAIL E1: … ; span=6; outside-span=7`, `SOURCE-SUPPORT 21/22; … MODES 22/22`,
`FAIL: E1: anchor hit outside declared line span 6 (hit lines: 7)`.

**5. C2/C3 composition check.** Applying `M1-r87-map.patch`,
`M2-r88m3-map.patch`, `M3-support-script.patch`, `M5-span-fix.patch` to a
path-limited `e97613c` archive yields files byte-identical to the delivered tree
(5/5: both `claim-excerpt-map.md`, `fictional-excerpts.md`, `support_check.py`,
`tools/README.md`).

**6. Doc-parity and state probes.** `grep -n "Round 90" corpus/fixtures/README.md`
→ empty; `corpus/knowledge/cross-cluster-contradictions.md` → absent;
`holder-assessment-boundary.md:188` still carries the removed tick-qualification
claim and pre-r90 line cites; `git diff --stat e97613c ca7f9ef -- SHONEN.md` → empty;
`git status` tracked-clean.

## Integration checklist for L1 / closure

1. Rule the three `PENDING-L1` verdicts (proposal only; no scores exist without a
   rubric) and decide the capabilities reading (third row recommended vs merge into
   the r89 row).
2. Closure-repair the doc-parity class found (not netted): adopt/replace
   `followup/CB1-boundary-refresh.md` into
   `corpus/knowledge/holder-assessment-boundary.md`; add the Round 90 section to
   `corpus/fixtures/README.md` (JCAL1 finding 6).
3. Housekeeping named by the junta: sweep or `.gitignore` `corpus/tools/__pycache__/`
   (Q89-044/JCAL1/JCAL2/JCOV5/H2/H4 observations); Q2's process improvements for r91.
