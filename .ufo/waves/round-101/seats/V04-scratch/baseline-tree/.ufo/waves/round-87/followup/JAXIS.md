# JAXIS — Axis-verdict synthesizer (round-87 follow-up)

Seat: JAXIS. Wave: round-87 follow-up (world-bible lane), fleet root
`/home/vgpnk/Projects/shokunin`, repo `lore-shokunin/`.

**Measured tree:** `2b48ca72033dfd1060b6f81c4cf27ad83deae57f` (`2b48ca7`, work-wave
evidence commit). All verdicts below are measured on that committed revision, never on
intent and never on the now-dirty working tree (I1/I2 in-flight writes, see §6).

**Deliverable:** this file only. No tracked file written, nothing committed, no push, no
registry write. This is a **recommendation to the L1**, not the verdict itself.

---

## 1. Wait-check and J-seat inventory

Wait-check for `followup/J*.md`, 60s spacing, three observations:

| check | time | `followup/` contents |
|---|---|---|
| 1 | ~01:39 | empty |
| 2 | ~01:41 | `I3.md`, `JCOV4.md`, `Q1.md`, + I3 JSON |
| 3 | ~01:44 | `JCAL1.md`, `JCAL4.md`, `JCOV1.md`, `JCOV2.md`, `JCOV4.md`, `JDEP1-replay.json`, plus E2/H1–H4/I2/K2/P2/P4/Q2/Q4 |

**J-seat reports read in full:** `JCAL1.md`, `JCAL4.md`, `JCOV1.md`, `JCOV2.md`,
`JCOV4.md`, and the machine receipt `JDEP1-replay.json`.
**Gaps (recorded, not blocked on):** `JDEP1.md` (depth judge's prose report) is **absent** —
only its 30-block replay receipt exists, so the depth verdict below is derived from that
receipt plus `JCOV2.md`'s depth row, not from a depth judge's own statement. No `JCAL2/3`,
`JCOV3`, `JDEP2+` appeared. Corroborating non-J seats also read: `I2.md`, `I3.md`,
`Q1.md`, `Q2-debt.json`, `K2.md`, `H1–H4` verdicts, `S1.md`.

---

## 2. My own independent measurements (delivered tree)

Every command run from `/home/vgpnk/Projects/shokunin/lore-shokunin`; base extracted with
`git archive 28706dc | tar -x -C /tmp/jaxis-base`.

**M1 — identity of the landed C1 artifact.** Each candidate patch applied to a fresh
`28706dc` archive, checker hashed, compared to `git show HEAD:corpus/fixtures/check_bible.py`:

```text
HEAD checker sha256=3ae4134d1d7d0f4b72f5ed0b344de54e886b60ab7cacd8e8ab0008521efcb237
X1-c1: MATCHES-HEAD
X2-c1-alt: differs sha=2150c51e30e1a8389cb994f704764f35cdfd13ecf1ccbc80d1b82c8f241620ee
X3-c1-min: differs sha=a2eec1c90205179c7c2c9c229da23da0db7933f5addb5eb622f33485935eb104
X4-c1-fsm: differs sha=d0b3d7535ff808a087547a9430d97e1b24e285f78b77ba5f29e313b07638ab75
```

→ **the landed checker is byte-identical to `28706dc` + `X1-c1.patch`**, not to the minimal
`X3-c1-min` that `R1.md:50` ranked #1 and `V3.md:43` issued its PASS against. `V1`/`V4`
verified X1; `V3`'s PASS covers X3. This is Q2's `D-C1-001`, independently reproduced.

**M2 — full checker-input census and before→after delta** (147 dirs under `corpus`
containing any checker table; 138 immediate `corpus/fixtures/*/`):

```text
TOTAL_CHECKER_DIRS=147
HEAD_EXIT_COUNTS={1: 113, 0: 34}
STDERR_NONEMPTY=0
CHANGED_VS_BASE=3
  corpus/live/runs/round-85/probe-inputs/r85-harbor-repro         rc 1->1  added=3 removed=1
  corpus/live/runs/round-85/probe-inputs/r85-isolated-ambiguous   rc 1->1  added=2 removed=1
  corpus/live/runs/round-85/probe-inputs/r85-masked-ambiguous     rc 1->1  added=3 removed=1
```

The only "removed" line in each case is the summary footer (`5→7`, `3→4`, `3→5`); zero
finding lines were removed. Restricted to the fixture corpus:

```text
inherited_fixture_dirs=133 tuple_changed=0
```

and `for d in corpus/fixtures/*/; do python3 corpus/fixtures/check_bible.py "$d"; done` →
`exit0=30 exit_nonzero=108` over 138 dirs.

**M3 — C3 cluster, delivered tree.**

```text
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster
CLEAN: schema, citations, relations, timeline; 0 violations      exit=0
entities=7 factions=2 relations=4 reciprocal=True events=4 depends_on_edges=3 contradictions=1
```

**M4 — integration state at `2b48ca7`.** `ls corpus/knowledge/` contains **no**
`*provenance-chain-decision-table.md`. `corpus/knowledge/holder-assessment-boundary.md:52`
still reads "Exactly one notice per item, located at the FIRST ambiguous-holder record"
and `:14` still reads `verified-at: STATIC PENDING PARENT RUNTIME`.

*Post-measurement note:* I1's `corpus/knowledge/r87-provenance-chain-decision-table.md`
appeared **untracked after M4 was taken**; it is not in `2b48ca7`. See §6.9.

---

## 3. Per-axis verdict table (recommendation)

Vocabulary: improved / harmed / unchanged / unprovable-but-better. No scalars. A trade
anywhere is **not** an improvement.

| axis | verdict | one-line evidence pointer |
|---|---|---|
| **calibration** (C1, commit `03c6746`) | **improved, bounded** | Landed checker = base + `X1-c1.patch` (M1); per-record disclosure at every record at/after the holder-ambiguity stop, naming field+id+origin (`JCAL1.md:96-124`, `I2.md:63-96`, M2). 133/133 inherited fixture tuples byte-identical (M2; `JCAL1.md:65-91`); 5 added findings on 3 pre-existing live probes, 0 findings removed, 0 exit-code changes, 0 added lines outside the disclosure signature (`JCAL1.md:180-192`; `H1`/`H4` verdicts). |
| **calibration — bound 1** | — | Discloses only **holder-ambiguity** stops. An unknown-source (or other non-holder) latch produces **no** per-record disclosure at all, and the stop record carries two near-duplicate lines (`JCAL4.md:50-55,110`; `JCAL1.md:197`). The landed `X1` wording also frames the holder ambiguity as a *cause* ("because … first occurred at"), which is misleading when an earlier non-holder stop already latched the gate (`JCAL4.md:72-98`). Pre-existing semantics carried over from the pre-C1 global notice, **not a C1 regression**. |
| **calibration — bound 2** | — | Residual unclosed vector: a record that carries an ambiguous holder id **and** a shape violation never arms the stop, so a later real break stays silently unassessed and undisclosed. Identical in base and delivered checkers (`JCAL1.md:151`). Fixture-thin: only 2 of 138 census dirs exercise the new path (`JCAL1.md:198`). |
| **coverage** (C3, commit `e4708cb`) | **improved, bounded** | `r87-myth-cluster` CLEAN exit 0 (M3); 7 entities (2 factions), 4 relations incl. a sourced reciprocal `allied_with` pair, 4 events / 3 `depends_on` edges, 1 reported-not-resolved place contradiction; all 22 citations resolve to 5 uniquely-defined sources (`JCOV1.md:32-141`). Byte-identical to the `M3` candidate (`JCOV1.md:239-250`); every rule class the cluster satisfies fires under mutation (`JCOV1.md:143-164`); 4/4 PROVINCE refusals respected, each actively disclaimed (`JCOV4.md:207-223`). |
| **coverage — bound** | — | Clean input, so it adds **no new checker finding template** (65 templates unchanged) — positive-path surface, not error-path coverage (`JCOV1.md:236`). Documentation sub-axis **unchanged**: no `## Round 87` section in `corpus/fixtures/README.md`; two new fixture READMEs declare no expected exit (`JCOV2.md:264-265`, `JCOV1.md:280`). The ETCSL citation is not registered in `corpus/knowledge/reference-ledger.md` (`JCOV2.md:249`). Named content debt OBS-1: `entities.json` attributes a Mother-Tide-Gate claim to the hymn, but the delivered excerpt names no place (`JCOV4.md:183-199`, `Q1.md:100-133`). |
| **depth** (C2 decision table) | **unchanged** at `2b48ca7` | No C2 knowledge file exists in the delivered tree (M4); `JCOV2.md:268` records depth unchanged because no new checker rule was added. The `D2` draft is **stale against the delivered revision**: replaying its 30 blocks against the delivered checker gives 26 match / **4 mismatch**, and all 4 mismatches are exactly the ambiguous-holder rows C1 changed (`JDEP1-replay.json`). `D1`/`D2` both self-declare baseline-only (`D1.md:31`, `D2.md:32`). |
| **depth — conditional** | *unprovable-but-better if landed* | If I1 lands `corpus/knowledge/r87-provenance-chain-decision-table.md` with the **delivered** outputs, the `item-chain-valid` control, and reproducible probes, the move is documentation-only: no behavior change is measurable, so it cannot be called `improved`. It is not measurable at `2b48ca7` because the file is absent. I1's version landed untracked after M4 (§6.9); it needs its own re-verification before that verdict is issued. |

**No axis harmed.** Four independent harm sweeps on the delivered tree — `H1` (wide
delta), `H2` (tree-diff audit, CONFORMANT), `H3` (8/8 mutations, 0 silent passes), `H4`
(live probes, additions-only) — plus `JCAL1.md:180-192` and `JCOV1.md:166-190` all report
zero removed findings, zero exit-code changes, and zero added lines outside the disclosure
signature. `JCAL4`'s mixed-stop issue is pre-existing, not introduced.

---

## 4. Harm findings

1. **No regression harm found.** The only output deltas anywhere in the tree are the 5
   intended disclosure lines on 3 live probes (M2) and the 4 new fixture directories'
   own outputs.
2. **Pre-existing, unclosed (not a regression):** non-holder stops remain undisclosed
   (`JCAL4.md:110`); shape-violating ambiguous records never arm the stop
   (`JCAL1.md:151`); the `because …` causal framing is misleading in mixed-stop inputs
   (`JCAL4.md:80`). All three are identical in the pre-C1 checker, so C1 neither caused
   nor worsened them.
3. **Record-integrity harm: none.** `SE1.md` found no fabricated receipt, no seat commit,
   no worktree divergence, and one documented-and-reversed transient write by F1.
4. **Doc-drift (owed, not harm):** `holder-assessment-boundary.md` still describes the
   one-notice contract (M4). I2's refresh closes it (see §6).

---

## 5. Admission recommendation

Per the wave rule — *admit only if every claim verifies and no axis is harmed; a trade is
not an improvement*:

- **ADMIT calibration (C1) as a bounded improvement.** Every measured claim verifies
  (M1–M2; `V1`/`V4`/`JCAL1`/`I2`/`JCOV1`/`H1`/`H4`). **Condition:** the round record must
  pair the landed artifact with the correct receipt — the landed checker is `X1-c1.patch`,
  so cite `V1`/`V4`/`C6`/`X4`, **not** `V3` (which PASSed `X3`, an unlanded variant) and
  **not** `R1`'s #1 ranking. Carry bounds 1–2 and the mixed-stop debt as named debt, and
  do not let the commit-message phrase "every record at/after the stop" be read as
  covering non-holder stops.
- **ADMIT coverage (C3) as a bounded improvement.** Every measured claim verifies
  (M3; `M4`/`C7`/`JCOV1`/`JCOV2`/`JCOV4`). Carry the bounds: no new finding template,
  documentation sub-axis unchanged, OBS-1, unregistered ETCSL citation.
- **DO NOT record depth as improved at `2b48ca7`.** The C2 knowledge file is absent from the
  judged revision and the `D2` draft is measurably stale against the delivered checker
  (26/30 match). Record depth **unchanged**, with the C2 table as owed follow-up. If I1's
  table (late-landed, untracked — §6.9) is re-verified against the delivered outputs, the
  correct later verdict is `unprovable-but-better` (documentation-only), never `improved`.
- **No trade is recorded as an improvement.** The changed live-probe footers and the
  duplicated stop-record line are costs paid inside the calibration gain, not separate
  gains; the stale boundary doc and missing C2 table are debt, not credits.

**Overall recommendation:** admit C1 (calibration) and C3 (coverage) as two bounded axis
moves; depth unchanged; the round is admissible **only with** the four named-debt items
below carried into the record.

---

## 6. Named debt and gaps for the record

1. **Receipt/artifact mismatch (blocking for an honest record).** Landed = `X1-c1.patch`;
   `V3`'s PASS and `R1`'s top ranking refer to `X3-c1-min`. (`Q2-debt.json` `D-C1-001`.)
2. **Mixed-stop attribution debt.** Causal `because` wording over-claims the holder
   ambiguity as the operative stop cause; three resolution options proposed, cheapest is
   an additive wording (`JCAL4.md:100-108`).
3. **Boundary-doc refresh owed.** `holder-assessment-boundary.md:52-55,73-74` still states
   the one-notice contract. I2 has an in-flight rewrite (measured accurate against the
   delivered checker, `I2.md:238-266`), but at `2b48ca7` the tracked file is **unmodified**.
4. **C2 decision table not integrated at `2b48ca7`.** `corpus/knowledge/r87-provenance-chain-decision-table.md`
   absent from the judged revision (it landed untracked afterwards — §6.9); `D2` stale (4 rows);
   `D1`/`D2` probes are scratch-only and not reproducible from
   the delivered tree (`R2.md:34`, `T2.md:25`).
5. **Census arithmetic.** S4's `133 + 1 = 134` was superseded by `133 + 5 = 138`
   (`I3.md:53-55`, `JCOV1.md:191-196`). The C1 commit's own "133 → 137" is correct for its
   own commit; at `2b48ca7` the count is 138.
6. **`corpus/fixtures/README.md` has no Round 87 section**; the two `r87-masked-break-*`
   READMEs describe pre-C1 behavior and declare no expected exit (`JCOV2.md:265`).
7. **`art-east-asian-design`**, named as the rights recipient in `PROVINCE.md:9`, does not
   exist at the fleet root — a fleet-wide dangling reference (`JCOV2.md:132-142`, `K2.md:22`).
8. **Working tree is dirty at hand-off:** `corpus/knowledge/holder-assessment-boundary.md`
   modified (I2), `l0-questions.md` modified (K2, one authorized appended line), and
   `corpus/fixtures/r87-probe-entry-shape/` + `r87-probe-record-and-chain/` untracked (I1).
   None of these is part of the judged revision `2b48ca7`; a later census over the dirty
   tree will read 140 dirs (`H1`), not 138.
9. **Late-landed C2 table (after my measurement).** `corpus/knowledge/r87-provenance-chain-decision-table.md`
   (24,918 bytes, untracked) appeared *after* M4 was taken and is **not** in `2b48ca7`. Its
   own header claims snapshot `2b48ca7` with checker sha `3ae4134d…` (matching M1) and it
   does include the `item-chain-valid` control (2 references). It therefore plausibly closes
   §6.4 — but because it is untracked and post-dates the judged revision, the depth row in
   §3 stays **unchanged at `2b48ca7`** and the file needs its own re-verification (delivered
   outputs pasted, no stale baseline rows) before depth can be recorded as
   `unprovable-but-better`. I did not audit its 24 KB of rows.

## 7. Bounds of this synthesis

- Verdicts are bounded to the three owned axes (depth, coverage, calibration) on the
  delivered tree at `2b48ca7`. I did not score anything, did not re-derive the r86 tuple
  artifact, and did not re-fetch the external citation.
- The depth row rests on a **machine receipt without its prose report** (`JDEP1-replay.json`
  only) plus `JCOV2.md`'s depth row; if `JDEP1.md` lands with a different reading, that row
  should be re-checked.
- Sibling repos were read-only; no UFO registry write, no commit, no push was made.

## 8. Handoff

- Land `lore-shokunin/.ufo/waves/round-87/followup/JAXIS.md` as the axis-verdict synthesis.
  No other file from this seat.
- L1: use §3 as the verdict table and §5 as the admission recommendation; the four
  blocking items are §6.1 (receipt pairing), §6.2 (mixed-stop wording), §6.3 (boundary
  refresh), §6.4 (C2 table). Do not record depth as improved without §6.4 closed and
  re-verified.
