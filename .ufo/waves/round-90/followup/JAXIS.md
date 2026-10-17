# JAXIS — Axis-verdict synthesizer (round 90 follow-up, world-bible lane)

Seat JAXIS. Judged tree: **delivered** `ca7f9ef1646cf3fcbe58747785a8cb2e9075ae13`
(`ca7f9ef`), baseline `e97613cc276f5fa9cac49ff1900798cf6863c020`. Every verdict below rests on the
delivered tree's artifacts: my own re-runs are pasted under "Before → after measurements", and each
seat-cited number names the follow-up report that carries its receipt. Scratch was `/tmp/jaxis-r90/`
only; no commit, no push.

**This file is a RECOMMENDATION to the L1, not the round's verdict.** The L1 owns the admission
decision and the SCORECARD wording. It is written against the lane's standing rule: per-axis
verdicts are `improved / harmed / unchanged / unprovable-but-better`, and a trade anywhere is NOT an
improvement.

## Work performed

- Read all fourteen `followup/J*.md` present — `JCAL1`–`JCAL5`, `JCOV1`–`JCOV5`,
  `JDEP1`–`JDEP4` — plus the J-seat JSON receipts where they carry the numbers (`JCAL1-delta`,
  `JCAL2-receipts`, `JCAL3-census-after`, `JCAL4-probes`, `JCAL5-delta`, `JCOV3-denominators`,
  `JCOV5-probes`, `JDEP1-receipts`, `JDEP2-probes`, `JDEP3-probes`, `JDEP4-evidence`). Also read the
  non-J follow-up seats whose findings bear on the verdicts: `CB1` + `CB1-boundary-refresh.md`
  (boundary-doc drift audit + draft refresh), `E1` + `E1-drift.json` (independent drift inventory),
  `H2` (harm sweep), `H3`/`H4` receipts, `H5-drift.json` (doc falsification sweep), `V2`
  (delivered-revision verifier), `SE2` (sentinel), `Q1` + `Q1-r90-debt.json` (53-row ledger +
  r91 proposal), `Q2` (process audit).
- Wait-checks per the wave protocol: three timestamped 60 s polls
  (`2026-10-17T06:55:01-03:00 → 06:56:01 → 06:57:01`; only `Q1-r90-debt.json` present), then
  extended polling `06:58:31 → 07:03:31` that observed the J-lane landing live (`H2`/`H4`/`JCAL5`
  JSONs at 06:57–06:58; the J `*.md` batch 06:59–07:00; `JDEP1` last at ~07:01). All fourteen
  `J*.md` were present and stable before this report was written; **no gap is owed**.
- Independent re-runs on the delivered tree (never on scratch patches): the freeze-then-verify
  composition; the 164-dir census with per-directory baseline-vs-delivered comparison; the four
  C5/C9 semantic probes; both support-command receipts; a span-enforcement attack and an R9
  paraphrase control; the boundary-doc source-level check; the census-manifest greps;
  `.gitignore`/pycache hygiene.

## Before → after measurements

All commands run from the repository root unless stated.

**Tree identity and freeze-then-verify (r88-I1).**

```sh
git rev-parse HEAD
git status --porcelain | head          # untracked followup/* artifacts + corpus/tools/__pycache__/ only
sha256sum corpus/fixtures/check_bible.py
# compose: e97613c checker + X2 + X3 (patch --fuzz=0, in /tmp/jaxis-r90/compose)
sha256sum /tmp/jaxis-r90/compose/corpus/fixtures/check_bible.py
```

```text
ca7f9ef1646cf3fcbe58747785a8cb2e9075ae13
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  /tmp/jaxis-r90/compose/.../check_bible.py
COMPOSITION_IDENTICAL
```

The delivered checker (428 lines, `ff9fd2aa…`) is byte-identical to X2+X3 composed on `e97613c`
(`e2bb9639…`, 435 lines) — **no mismatch; no blocking finding on the freeze rule.** Independently
reproduced by every J seat and by CB1, E1, H2, H5, V2, SE2, Q1 (JCAL5 records the composition as
order-independent: X2X3 = X3X2 = delivered).

**Census (my re-run, one fresh process per fixture directory).**

```sh
python3 - <<'PY'   # for every dir under corpus/fixtures/: python3 corpus/fixtures/check_bible.py <dir>
PY
```

```text
dirs 164 exits {0: 32, 1: 132} violations 417
shared 160 dirs: changed_stdout 0, exit_flips 0, shared_viol_delta 0
new fixtures (rc, violations): rawpresent-from (1,5), rawpresent-to (1,5), rawpresent-source (1,4), three-causes (1,4)
```

Matches JCAL1 (`164 / {0:32,1:132} / 417`), JCAL2, JCAL3 (`JCAL3-census-after.json`), JCAL5, H2
(`417 − 399 = 18 = 5+5+4+4`), Q1, V2, SE2. The claim — **0 changed + 4 new of 164, 0 exit
changes** — reproduces exactly, at stdout-byte level, in my run and in five seats.

**Four C5/C9 semantic probes against the delivered checker** (built from
`r89-fn2-unresolved-chain-break`, ancillary JSON symlinked; scratch only):

```sh
python3 corpus/fixtures/check_bible.py /tmp/jaxis-r90/probes/<case>
```

```text
chain-unresolved            → qualified: "possible provenance chain break, not a definite identity mismatch: … 'f3-dup' is not uniquely resolvable (2 raw …1 …); got 'mira'"
tick-relevant-unresolved    → definite: "provenance tick 1 must be greater than previous tick 3"   (no identity note)
null-from-chain             → definite: "provenance chain break; expected from_holder 'mira', got None"
unrelated-duplicate-tick    → definite: "provenance tick 1 must be greater than previous tick 3"
```

This is C9's ruled composition exactly: null chains and tick findings definite; a genuinely
unresolved non-null holder **chain break** stays qualified; the tick comparison is integer-only.
Corroborated by JCAL1/2/3/4/5, V2, H5 (each with its own harness).

**Support command (C2 receipts) and enforcement attacks.**

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster; echo "r87_exit=$?"
python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster; echo "r88m3_exit=$?"
```

```text
SOURCE-SUPPORT 22/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22
RESULT PASS
r87_exit=0
SOURCE-SUPPORT 10/10; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 10/10
RESULT PASS
r88m3_exit=0
```

Span enforcement (scratch copy of r87, E1 locator `:7` → `:8`):

```text
FAIL E1: source-support; mode=verbatim; anchor=found; 7:> I am Hara, keeper of the Mother-Tide Gate.; span=8; outside-span=7
SOURCE-SUPPORT 21/22; … MODES 22/22 ; exit=1
```

R9 non-counting (minimal one-row scratch cluster; same bytes, mode flipped):

```text
paraphrase:  PASS F1: retelling-support-only; anchor=found; mode=paraphrase; 2:> the ring was set.
             SOURCE-SUPPORT 0/0; RETELLING-SUPPORT-ONLY 1 entries (1/1 anchors); MODES 1/1 ; RESULT PASS ; exit=0
verbatim:    PASS F1: source-support; anchor=found; mode=verbatim; 2:> the ring was set.
             SOURCE-SUPPORT 1/1; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 1/1 ; RESULT PASS ; exit=0
```

Both facts are independently enforced by JCOV1 (M4's wrong-line attack closed 8/8; live paraphrase
fixture `0/0`), JCOV2 (controls A/B), JCOV3 (three controls), JCOV4 (12 probes), JCOV5 (four
controls), JDEP4 (M1/M2).

**Boundary doc vs the delivered checker (my source-level reproduction of the drift).**

```sh
grep -c "holder identity is not uniquely resolvable" corpus/fixtures/check_bible.py   # rc=1 → 0 hits
git diff --stat e97613c..ca7f9ef -- corpus/knowledge/   # only the decision table, +37
sed -n '188p;266,272p' corpus/knowledge/holder-assessment-boundary.md
```

The delivered checker **cannot emit** `holder identity is not uniquely resolvable:` anywhere (the
string is absent from the 428-line file; the r88 format strings are restored at `:326`/`:337`/`:343`).
The boundary doc asserts it twice for ticks — decision-table row 3 (`:188`: "…and for ticks
`{record_label}.tick: input-structural finding, not sourced-canon; holder identity is not uniquely
resolvable: {details}; …` (`:327-333`, `:334-344`, `:345-350`)") and the limits bullet (`:266-272`:
"…or, for ticks, carries `holder identity is not uniquely resolvable: …`. Both the expected and the
observed side are tested"). The doc was true at `e97613c` (the baseline emits that form — my
tick probe's before-output in B3/C9 receipts); the work commit changed the behavior (X3) without
updating the doc. This is drift **introduced by `ca7f9ef`**, not inherited.

Independent corroboration, four seats: **CB1** (drift inventory D1–D14: D1/D2 behavioral, D3–D5
revision pins / unhonored recheck trigger, D6–D9 anchor remaps, D10–D14 inventories/status; full
replacement text in `CB1-boundary-refresh.md`, proposal only), **H5** (`boundary_doc: harm
(bounded, doc-parity class): two falsified behavioral claims, one removed FN-2 sub-branch, ~60
stale anchors, stale revision pins, unhonored recheck trigger`), **V2** (F2: "the boundary contract
doc is now false and mis-anchored … the delivered revision introduced this falsification"),
**E1** (`E1-drift.json` inventory). CB1's doc's pasted `=== case ===` blocks themselves still
replay 14/14 byte-exact (CB1); the harm is in prose claims, anchors, and provenance stamps.

**Census-manifest wording (C1(iii)) and hygiene.**

```sh
grep -o "r89-fn2[^\"]*" .ufo/waves/round-90/patches/B1-tuples.json | sort -u   # both pair dirs present
git diff --stat e97613c..ca7f9ef -- corpus/fixtures/README.md                  # empty
git check-ignore -v corpus/tools/__pycache__/                                  # rc=1 (not ignored)
```

The FN-2 pair is a row of both 160-row baseline manifests (and of the delivered census); there is
**no textual manifest delta** in `ca7f9ef` — the pair was already in the manifest at `e97613c`
(H2 named debt 1). `.gitignore` (unchanged, only `.ufo/interactive-sessions/`) does not ignore
`__pycache__`; an untracked `corpus/tools/__pycache__/` appeared during the wave from sibling seats
importing `support_check` as a module (JCAL1 removed it once; it reappeared; Q89-044 open).

## Findings & named debt

### Per-axis verdict table (recommendation to the L1)

| axis | verdict at `ca7f9ef` | verdict after the R1–R3 repairs | one-line evidence pointer |
|---|---|---|---|
| **calibration** | **improved (bounded)** | **improved (bounded)** | Freeze hash-match (my run + 15 seats); census 0 changed + 4 new of 164, 0 exit flips (my run + JCAL1/2/3/5, H2, Q1, V2, SE2); both r89 hedged shapes repaired and the genuine-uncertainty case preserved character-for-character (my four probes + JCAL1/2/3/4/5, V2, H5); vacuous clause 0/164 (JCAL2); four new fixtures byte-exact vs their READMEs (JCAL3, H2, V2, H5). Bounds: repaired shapes have no durable fixture (see CAL-D1); C9 is a ruling, not a case (CAL-D2); E1's sub-case templates diverge in the safe direction (CAL-D3). |
| **coverage** | **improved (bounded)** | **improved (bounded)** | Receipts reproduce: r87 22/22, r88-m3 10/10, exit 0 (my run + all JCOV seats + JDEP4); R9 non-counting of paraphrase and span enforcement proven by independent negative controls (my two attacks; JCOV1 8/8 M4 attack; JCOV2 A/B; JCOV3 3 controls; JCOV4 12 probes; JCOV5 4 controls); all 42+10 map pointers resolve, 0 disagreements (JCOV3); maps are in-corpus and the command is committed (JDEP4 M1; JCOV5). Bounds: receipt counts rows, not JSON facts (COV-D1); header-role silent row-drop (COV-D2); unreferenced excerpt labels unenforced (COV-D3); translation/version tie outside the tool (COV-D4). |
| **depth** | **harmed (bounded)** | **improved (bounded)** | The C3 gains are real and verified (JDEP1/2/3/4: appendices append-only +37/0, owner+trigger+decided phrases present, retroactivity byte-proven, register correctly absent, no false referent). But the work commit left the boundary contract doc (**D1–D14**, CB1/H5/V2/E1) false on exactly the behavior C1 changed and mis-anchored throughout; a trade anywhere is NOT an improvement, so depth cannot be recorded improved while D1/D2 stand. Repair is a doc edit (`CB1-boundary-refresh.md`), no checker change. |

No other axis harmed: H2/H3/H4/H5, V2, SE2, Q1, Q2 find no exit/stderr, coverage, corpus, or
process harm beyond the doc-parity surface above; all four r90 fixture READMEs reproduce their
own fenced blocks byte-exactly (H5, JCAL3, V2).

### Attribution note (for the L1's wording)

V2's F2 charges the doc harm to the **calibration** verdict ("must be repaired or recorded as a
bounded harm before any 'improved' calibration verdict is admitted"); H5 calls it a doc-parity
harm without assigning an axis; r88/r89 assigned the identical condition (a knowledge/contract
doc contradicting the shipped checker on exactly what the round's C1 changed) to **depth**
(r88 follow-up ruling; r89 JAXIS note). I assign it to depth. Under V2's attribution, calibration
would instead be `harmed (bounded)` and depth `improved (bounded)`. Under either attribution the
substantive instruction is identical: the cost is real, bounded to one file, and must be repaired
(or explicitly recorded) before "improved" is written anywhere it is charged — and the C3 gains
must not be netted against it.

### Claim-verification notes (C1 / C2 / C3 vs the delivered tree)

1. **C1 verifies, with four wording scopes for the round record.** (a) "Null chains and tick
   findings definite" holds for tick findings and for null-from chains whose expected side is
   resolved or null; the mixed case (null observed side, **unresolved non-null expected side**)
   stays qualified — X2's narrower bound, diverging from E1's panel template (JCAL4-F1/F4, CB1 F1
   probe, V2 probe table). Safe direction (over-hedge), but the claim sentence needs the sub-case
   qualifier. (b) The tick-definite reading keeps the independent `ambiguous-source` prefix
   (`r87-probe-source-prefix` unchanged; JCAL2-D2, JCAL5 §6). (c) "The FN-2 pair joins the
   canonical census manifest" holds in the **runtime** sense (census membership + regression
   visibility, JCAL1); there is no textual manifest delta — the pair was already in the 160-row
   baseline manifest (H2 named debt 1). (d) The repaired shapes are pinned only by scratch probe
   receipts (B3/C5/C9 + J-seat re-runs); no durable fixture exercises either (CAL-D1).
2. **C2 verifies under its own rule, but "22/22" must name its denominator.** The r87 receipt
   counts rows: 14 JSON rows co-carrying 20 obligations + 8 editorial hymn rows; 2 obligations
   (`entities[2].first_appearance`, `entities[2].claims[0]`) are covered only by the map's prose
   crosswalk at `:56` (JCOV1-N1, JCOV2-D1, JCOV3-F2, JCOV4-F3). r88-m3's 10/10 is an exact
   bijection with its 10 JSON obligations. "One command" = the committed script; its two
   invocations are two receipts (JCOV1 D-M4-2, adjudicated satisfied). Only exit 0 + `RESULT PASS`
   should be read as support evidence.
3. **C3 verifies in substance as delivered** — three appendices, each with an owner clause and a
   trigger sentence, no deletions, provenance line recorded (JDEP1; JDEP3's register screen;
   JDEP4's M3). Residual edges are named debt (DEP-D2/D3/D4). Per JDEP4, **do not** enter a third
   capabilities row this round; update row 2's evidence pointer to the corpus-resident command
   set at closure instead (DEP-D5).

### Named debt (consolidated; receipts in the named seats)

**Calibration-side:**
- **CAL-D1 Repaired shapes are census-invisible; no durable fixture pins them** (JCAL2-D1,
  JCAL3-3, JCAL4-F3, JCAL5-1, H2-2, CB1 FN-2 list). r91 candidate: one durable fixture per shape
  (later `from_holder: null` break; unresolved-compared-holder tick inversion), or a committed
  harness that runs against the delivered checker; fold the 4 new fixture rows into the canonical
  manifest (JCAL5-2).
- **CAL-D2 C9's integer-only tick ruling remains a ruling** — open to r91 falsification as C9
  named it (C9.md; JCAL1-5, JCAL5-3).
- **CAL-D3 E1-vs-delivered sub-case divergence** — mixed null/unresolved-expected chain stays
  qualified; first-record guard with unresolved non-null id stays qualified and voice-inconsistent
  (JCAL4-F1/F2/F4; CB1 adjacent note; E1). Adjudication for the L1: doc describes delivered
  behavior (as CB1's refresh does) or r91 adopts E1's definite template.
- **CAL-D4 Claim-text precision** — C1 summary needs the null-sub-case qualifier and the
  ambiguous-source qualifier (JCAL4-F4, JCAL2-D2).
- **CAL-D5 `r90-c1-three-causes/README.md:21` precision** ("occur nowhere in their corresponding
  raw tables" — each occurs once as its own provenance reference; V2-F4).

**Coverage-side:**
- **COV-D1 Receipt denominator wording** — print rows vs JSON facts separately (JCOV1-N1,
  JCOV2-D1, JCOV3-F2, JCOV4-F3; one-line fix at `support_check.py:276-281`).
- **COV-D2 Silent row-drop** — a fact table whose header loses its `id` role leaves the receipt
  with `RESULT PASS`, exit 0 (JCOV4-F1; r91 inventory assertion `--expect-rows`).
- **COV-D3 Unreferenced excerpt labels are not enforced** (r88 Spence `source-excerpt.md`);
  benign today, no fact row targets it (JCOV2-D3, JCOV4-F2, JCOV3-F5).
- **COV-D4 `translation` is support-eligible with no translator/version tie** (JDEP2-D5, JDEP4-F2
  /M2, JCOV4-F5; README:14 disclaims).
- **COV-D5 Substring anchors** — mid-word occurrences pass; chousa's token-boundary hardening
  cited but unlanded (JCOV5-ND2).
- **COV-D6 Stale tool note** — `symbolism-clause-map.md:16` "the checker does not read this map"
  is false for the new `support_check.py`; name `check_bible.py` (JCOV2-D2).
- **COV-D7 K1's chousa cross-references landed only in the wave artifact**, not the governing
  table (JCOV5-ND1; Q89-047 delivered half stays open).
- **COV-D8 Retelling rows tolerate absent anchors; no de-duplication in N/N** (JCOV4-F4);
  r88-m3 imprint publisher unverified from the cited source (JCOV2-D4, minor).

**Depth-side:**
- **DEP-H1 (blocking-class repair) Boundary doc drift D1–D14** — behavioral claims (tick note,
  both-sides sentence), FN-2 sub-branch list, revision stamps (`1b09f3f`/`e2bb9639`), ~60 anchors,
  inventories, unhonored recheck trigger. Repair: apply `CB1-boundary-refresh.md` (or equivalent)
  with the `ca7f9ef`/`ff9fd2aa` re-verification stamps; re-verify every anchor against the
  delivered checker before applying (CB1 D6–D9 remap table); no checker change → cannot re-open
  the census.
- **DEP-D2 Delivered appendices have no own executable check** (JDEP1-F1; zero commands cited
  in-appendix).
- **DEP-D3 Governance edges** — R8 failed-gate disposition + note lifecycle + withhold-scope
  reconciliation; R9 reprint/"reliable" criterion; R10 `source_id` namespace scoping (JDEP2
  D-JDEP2r90-1…-5; JDEP3 scoping-rule debt).
- **DEP-D4 Register conventions** — file/header/ordering/ID conventions unstated; scoping to
  landed clusters vs fixture dirs (JDEP3; JDEP2-D4).
- **DEP-D5 Capabilities** — **against** a third row as phrased; update row 2's evidence pointer
  to the corpus-resident command set at closure; first-working stays r89 (JDEP4-F2/F3; F4 = the
  r91 candidate test for a third row).
- **DEP-D6 `r87-probe-source-prefix/README.md` re-anchor** — cites `:350`/`:333`/`:344`; delivered
  `:343`/`:326`/`:337` (Q89-032; CB1 adjacent, V2 anchor table).
- **DEP-D7 r87 note "four excerpts" wording drift** (five exist; pre-existing, byte-unchanged —
  JDEP1-F4).
- **DEP-D8 R10 row exit-code wording is form-dependent** (split argv → exit 2 matches; space-joined
  → exit 1; JDEP1-F3).

**Closure/process:**
- **PROC-1 `## Round 90` section for `corpus/fixtures/README.md`** + retire the now-misleading
  "(r89 refresh)" contract label (V2-F3; JCAL1-6, JCAL3-2, H2-1, CB1-D12 — closure-scope by
  precedent: r87/r88/r89 sections were added at closure).
- **PROC-2 Closure prose must use delivered figures** — W2's proposals carry pre-integration
  numbers (`X1-unchanged=160`, patch `c3573aa0…`); delivered: `X1-tuple-delta.json` = 159/1, patch
  `6d37eccf…`, census 164/0+4 (JCAL3-4; W2 patches).
- **PROC-3 Hygiene** — remove `corpus/tools/__pycache__/` before freeze; decide the `.gitignore`
  entry (Q89-044 open; JCAL1-7, JCAL2/JCOV5/JDEP1/V2/H2 observations).
- **PROC-4 Environment fact** — `/tmp` inode exhaustion (100% during the wave; several seats
  moved to `/dev/shm`/memfd) belongs in r91 planning (JCOV1, JCAL1/2/4/5, JDEP2/3/4, CB1, E1, H2).
- **PROC-5 Q1 ledger** — 53 rows re-verdict at the delivered tree (verified 8 / partial 7 /
  open 16 / bound 8 / carried 4 / not claimed 10) with the r91 proposal Q89-046 (exploratory;
  operator cold-run acceptance, not dispatchable).

### Admission recommendation to the L1

**Do not admit as-is; repair, then admit (recommended).** The round's rule is "admit only if
every claim verifies and no axis harmed; a trade is NOT an improvement". Calibration and coverage
verify with named bounds; depth carries an independently corroborated (CB1, H5, V2, E1 + my
re-run) doc-parity harm introduced by the work commit — the same condition the r88 follow-up
ruled harmed and the r88/r89 closures repaired. The repair set is small, documentation-only, and
partly drafted:

1. **R1 (blocking-class):** apply a refreshed `holder-assessment-boundary.md` (CB1's
   `CB1-boundary-refresh.md` is a ready-to-paste replacement carrying D1–D14 + the anchor-remap
   table; re-verify its anchors before applying; drop the "(r89 refresh)" label issue with
   PROC-1) — no checker change, so the C1 census cannot re-open.
2. **R2 (closure-scope by precedent):** add the `## Round 90` section to
   `corpus/fixtures/README.md` naming the four new fixtures; re-anchor
   `r87-probe-source-prefix/README.md` (DEP-D6); fix the `r90-c1-three-causes` README sentence
   (CAL-D5).
3. **R3 (cheap, non-blocking):** `symbolism-clause-map.md:16` tool name (COV-D6); receipt
   denominator wording if wanted now (COV-D1); pycache cleanup (PROC-3).

Then record: **calibration improved (bounded), coverage improved (bounded), depth improved
(bounded)**, with CAL-D1…D5, COV-D1…D8, DEP-D2…D8, PROC-1…5 carried as named debt. This is the
r88/r89 resolution sequence verbatim, and every repair diagnostic is already in the wave evidence.

**Alternative — admit with recorded harm:** if the L1 prefers not to reopen the round, record
depth **harmed (bounded)** explicitly (contract doc contradicts the shipped checker on exactly
what C1 changed, plus stale anchors/pins across the file) with R1–R3 as the first closure/r91
items. Acceptable only as stated; do not record depth as improved while D1/D2 stand, and do not
net the C3 gains against the harm. If the L1 follows V2's attribution, the same recorded-harm
sentence moves to calibration instead.

Either way: the C1 record must carry the sub-case qualifiers (note 1), the C2 headline must name
the row denominator (note 2), and the capabilities table must not gain a third row this round
(JDEP4).

## Handoff

- Deliverable: `lore-shokunin/.ufo/waves/round-90/followup/JAXIS.md` (this file) and
  `lore-shokunin/.ufo/waves/round-90/followup/JAXIS-verdicts.json` (machine-readable verdict
  table, admission options, consolidated debt ids, seat inventory). No other repo write; no
  commit; no push. `corpus/tools/__pycache__/` is a sibling-seat side effect, not mine.
- Reproduce my four central measurements (cwd repository root): (1) compose X2+X3 on
  `e97613c:corpus/fixtures/check_bible.py` with `patch --fuzz=0` and `sha256sum` both (expect
  `ff9fd2aa…` twice); (2) loop the checker over `corpus/fixtures/*/` (expect 164 /
  `{0:32, 1:132}` / 417, and 0 changed stdout on the 160 shared dirs vs the baseline checker);
  (3) run `python3 corpus/tools/support_check.py` on both clusters (expect 22/22 and 10/10 with
  `RESULT PASS`, exit 0); (4) `grep -c "holder identity is not uniquely resolvable"
  corpus/fixtures/check_bible.py` (expect 0) vs `holder-assessment-boundary.md:188` and `:266-272`
  (expect the two claims) — the doc-parity drift, repair artifact in `CB1-boundary-refresh.md`.
- Claim status for the integrator: **C1 verifies (bounded, wording scopes 1a–1d); C2 verifies
  under the row-denominator rule; C3 verifies in substance; one bounded doc-parity harm (D1–D14)
  blocks a clean admission and has a drafted repair.**
- Not done here: I did not field-audit every J receipt JSON beyond its key numbers (the seat
  reports carry the full receipts), did not re-render the decision table with a GFM parser, did
  not independently re-fetch the Spence/ETCSL sources (JCOV2/JDEP1 receipts cited), and did not
  rule on the E1-vs-delivered adjudication beyond naming it (DEP/CAL-D3). All remediation is the
  L1's decision.
