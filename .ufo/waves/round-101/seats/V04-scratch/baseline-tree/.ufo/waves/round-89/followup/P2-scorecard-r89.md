# PROPOSAL — Round 89 SCORECARD section (seat P2, follow-up wave)

Do not append before L1 adjudication. Every verdict below is **PENDING-L1**;
scores remain unmeasured (no rubric); every number is a measurement on the
DELIVERED tree at `1b09f3f` (baseline `51b286b`), never a score. The per-claim
rows carry their counting commands and commits; seat readings are inputs, not
rulings. Full receipts are in the appendix and in `followup/P2.md`.

## Round 89 — luna round 3 of 12 (2026-10-17)

Two-wave regimen round: work wave (32 seats, `openai-codex/gpt-6-luna-max`);
follow-up wave (judging/integration; 23 seat artifact sets landed by proposal
time). Spec `.ufo/waves/round-89/wave-spec.md` (roster-as-data + landing
record). Baseline `51b286b`; work commit `1b09f3f` (136 files, +12330/−15;
33 wave-root reports + 27 patch artifacts); closure commit = this section's
commit. Tree at judgment: tracked-clean apart from the authorized uncommitted
`l0-questions.md` append (K1) and the untracked `followup/`. Scores remain
unmeasured; the rows below are claims with counting commands and measured
commits.

### Per-claim rows

| # | axis / claim | verdict | measured before → after | evidence and limit |
|---|---|---|---|---|
| C1 `1b09f3f` | calibration — six first-cause branches pinned; valid-key combined-cause summary; FN-1 two-sided wording; FN-2 qualification | **PENDING-L1** | **Before `51b286b`:** 149 dirs, exits 0=31/1=118, 367 violation lines, 0 stderr; a valid-key multi-defect record named only the first defect; a chain break against a non-uniquely-resolvable holder printed as definite; `r89-f2-*` disclosures read `dangling holder …` / `unknown source …`. **After `1b09f3f`:** 160 dirs, exits 0=32/1=128, 399 lines, 0 stderr; delta **4 changed + 11 new, 0 removed, 0 exit changes, 0 violation-count changes** on shared paths; all 12 changed disclosure lines sit inside existing `first stop:` lines (2 combined-cause + 10 FN-1 wording); `r89-c1-multi-cause-valid` names both causes; FN-2 pair qualifies / control stays plain. | Counting commands in the appendix (§Receipts 1–3). Checker `+54/−14` (`git diff --numstat 51b286b 1b09f3f -- corpus/fixtures/check_bible.py`), SHA-256 `e2bb9639…`, byte-identical to `patches/X1-c1.patch` applied to `51b286b` (V2; JCAL1). Corroboration: JCAL1 (delta classified line-by-line), JCAL3 (10-fixture replay + 9-mutation matrix — every non-control fixture catches at least one wrong implementation), H1/H2 (independent censuses: 399−367=32 = the added dirs' sum), V2 (freeze + 8/11 READMEs byte-match). Bounds: (a) FN-1's `present in raw … but absent from the resolved index` branch has **0 durable fixtures** (string occurrence 0/0 across all 160 dirs; scratch-only per H5/C6/P3); (b) 3 `r89-f2-*` READMEs quote the pre-FN-1 cause strings (V2 8/11; JCAL3 Debt 1; H2 F3; H5 item 1); (c) the "current contract" doc `holder-assessment-boundary.md` is stale — its "only the shape-invalid branch combines two cause phrases" precedence claim is contradicted by the delivered valid-key combined summary, its replay block no longer reproduces, code anchors shifted (H2 F5; H5 item 2; JCAL3 Debt 2); (d) FN-2 predicate is a conservative superset — a definite tick-order violation and a schema-valid `None` observed holder can be over-qualified (C6; P3 probes); (e) 4 of 8 cause-family fixtures are byte-identical on the baseline checker — mutation-discriminating, not delta-discriminating (JCAL3 Debt 4); (f) `r89-c1-malformed-source-id` is integrator-authored with no patch artifact (disclosed in its README; JCAL1; Q2). |
| C2 `1b09f3f` | coverage — r87 cluster to 22/22 under the D1 support rule + ETCSL delivery marker | **PENDING-L1** | **Before:** `r87-myth-cluster/` held 1 delivered excerpt (9 files); anchors 0/14; pointers with a delivered excerpt 1/7; D1-rule supported facts 8/22; ledger row without delivery status. **After:** 5 excerpts (4 added — `gate-witness`, `dune-register`, `shell-charter`, `tide-bell-tally`); anchors **14/14** at their recorded lines; pointers **7/7**; facts **22/22** (7 pointers + 7 claims + 4 relation edges + 4 timeline events); cluster `CLEAN` exit 0 (both sides); ledger `external-only / text not delivered at lore…`; corpus-wide 0 exit changes. | Counting commands in appendix §Receipts 4. Corroboration: JCOV1 (0/14→14/14, 1/7→7/7, 8→22, exit-neutral; verdict improved (bounded)), JCOV4 (fresh-eyes: 14/14; denominator resolves; PROVINCE refusals respected), JCOV3 (R9/R10 demo sub-scope), JDEP4 (32/32 across r87+r88), P4 (two demonstrated applications). Bounds: (a) `M4-verify.json`'s `after.facts_supported: 22` is a hand-composed 8+14 — its own stored probe prints `OK=8` on the delivered tree; cite the per-fact map/composition, not that block (JCOV1-D1; P3; H1 F1); (b) no in-corpus claim→excerpt map in the cluster — path/line evidence is wave-resident (`patches/S2-fact-map.json`), so 22/22 is not certifiable from the corpus alone (JCOV4-D1; P4 D1; JDEP4 F5); (c) `r87-myth-cluster/README.md` unchanged, lists none of the four new excerpts (JCOV1-D2; JCOV4 D3); (d) the four new excerpts declare no R9 delivery mode although r89 is a content touch (JCOV4 D2; P4 D2; JDEP2-4); (e) decision-table row-5 evidence cell stale (JCOV1-D3); (f) ETCSL marker omits the literal `unverified` token (JCOV4 D4); (g) the r88 Maya map is a replay, not a delivered map (JDEP4 M3/F5). |
| C3 `1b09f3f` | depth — R8/R9/R10 governance rows + R9 demo fixture + R10 worked example | **PENDING-L1** | **Before:** table 7 rows; no R8/R9/R10; demo/example absent. **After:** 3 rows × 6 columns at `:22-24`; R9 negative demo `r89-inspiration-paraphrase` (CLEAN exit 0; `**Delivery mode:** paraphrase` in excerpt and map; map cell `Fails:`; anchor at `ash-ledger-excerpt.md:9`); R10 worked example `corpus/knowledge/r89-cross-cluster-contradiction.md` (32 lines; 2× `Status: unresolved`; second cluster hypothetical; live register absent); integration notes scope R8–R10 **prospective**. | Counting commands in appendix §Receipts 5. Corroboration: JDEP1 (row commands replayed; shapes), JDEP4 (depth improved (bounded); second capabilities row FOR), JCOV3 (R9 rule statements 7/7; R10 elements 17/17; pointers resolve; checker silent), V2 (6-column shape preserved; no existing row modified; append = D2's draft + owner clause). Bounds: (a) no mechanical layer reads the rows (checker grep for excerpt/delivery/knowledge terms → none), so all three are normative text; JDEP2's constructed probes show each row leaves one sub-case undecided — R8 unrecorded-but-plausible influence (who raises it; where the element marker lives with no note/map; the landed r87 ETCSL motif carries 0 `external-only` markers) = uncovered; R9 translation with named translator but unrecorded version (declaration vs eligibility clauses pull opposite) = uncovered; R10 referent-name overlap with different occasions (register defined only for supported incompatible pairs; dismissed overlaps leave no record; D1's name-identity guard dropped) = uncovered (partial); (b) no R8 demo fixture (JDEP2-3); (c) three coexisting `external-only / …` marker strings (JDEP2-2); (d) R9's demonstrated path is declarative-only — a scratch verbatim twin is not discriminated by the checker (JCOV3 P2; D2). |

### Documentation/expectation parity condition (cross-cutting; L1 decision owed at closure)

The r89 checker/disclosure changes landed without every quoting surface being
updated; `H2` states the parity cost must count against the move, not be netted
silently. Open items: (a) three `r89-f2-*` fixture READMEs quote the retired
cause strings; (b) `holder-assessment-boundary.md` — including a behavior
statement now contradicted by the delivered checker and a replay block that no
longer reproduces; (c) no `## Round 89` section in `corpus/fixtures/README.md`
(11 dirs, 4 excerpts, the R9 demo unindexed — third round running for this
file); (d) `r87-probe-source-prefix/README.md` cites three stale code lines;
(e) `r87-myth-cluster/README.md` silent on the four new excerpts; (f) the two
FN-2 READMEs still say "integration verification pending" (now resolved); (g)
the Spence ledger row renders outside the table; (h) `S2-fact-map.json`'s
`anchor_basis` misnames M3 while the delivered bytes are M4's. Precedent: r88
recorded the same class as `depth: harmed (bounded)` and repaired it in the
closure commit. L1 decides: repair inside the r89 closure (all one-clause /
one-section edits; the checker needs no change) and state the condition closed,
or record the harm as unresolved. Neither path is a score.

### LIVE verdict table (PENDING-L1)

| LIVE axis | r89 verdict | Evidence and limit |
|---|---|---|
| calibration | **PENDING-L1** | C1 row above. Seat readings (non-binding inputs): JCAL1 `improved`; JCAL3 `improved (bounded)`; P3 `improved (bounded)` — not clean because H2/H5 parity harm is not netted. Limits: FN-1 raw-present branch unfixtured; stale F2 READMEs; stale/contradicted contract doc; FN-2 superset; 4/8 non-delta-discriminating fixtures. |
| coverage | **PENDING-L1** | C2 row above. Seat readings: JCOV1/JCOV3/JCOV4 `improved (bounded)`; JDEP4 `improved (bounded)`; P4 box-3 `[ ]`→`[~]` proposed. Limits: receipt reproducibility (M4 block), no in-corpus map, README/excerpt-mode parity, decision-table row-5 cell. |
| depth | **PENDING-L1** | C3 row above. Seat readings: JDEP4 `improved (bounded)` + second capabilities row FOR; JDEP2 reports the three uncovered sub-cases; JCOV3 `improved (bounded)` on the demo sub-scope; P3 `improved (bounded) on the artifact surface; a documentation harm is recorded, not netted`. Limits: rows unread by any mechanical layer; each row leaves one sub-case undecided; no R8 demo. |

No axis was read as `unchanged`; no `unprovable-but-better` reading was issued;
no axis verdict is ruled here — admission and verdicts are L1's.

### Capabilities — proposed update (second row)

Delivered state: the structured `## Capabilities` table still reads
`| — none yet — |` (line 76) although the r88 section records row 1 in
narrative only (line 146). Proposed single repair edit (JDEP4 F3 condition):
write **both** rows into the table at once —

| Capability | What it can now do | Evidence pointer | First-working round |
|---|---|---|---|
| provenance stop-cause assessment | For any provenance-chain stop the checker latches, emit at the stop record and every later record a disclosure naming the cause that actually latched, never a later ambiguity. | `for d in r88-shape-ambiguous-armed r88-mixed-stop r88-nonholder-stop; do python3 corpus/fixtures/check_bible.py corpus/fixtures/$d; done` → 5/6/4 findings, exit 1. | r88 |
| in-world excerpt support verification | For an in-world claim attributed to a source: resolve the `source_id`, locate the delivered excerpt, run a fixed-string anchor preflight over the recorded anchors, and return a support verdict — including refusal when the delivered representation is a paraphrase/summary or the source text is undelivered. | Appendix §Receipts 6 (r87 `facts=22 OK=22`; R9 demo `CLEAN` + anchor hit + support withheld). | r89 |

Bounds to record verbatim with row 2: procedure-shaped, the whole-claim review
is human (JDEP4 F2); the r87 anchor map is wave-resident, not corpus-resident
(F5); the R9 positive mode path is unexercised — only the paraphrase-failure
class is demonstrated (F6). If the table is not repaired this closure, defer
row 2 one round rather than entering it into a table that still denies row 1.

### planned (r90, proposal — L1 to adopt or amend)

1. calibration — FN-1 raw-present fixture pair (entity + source side); reconcile
   the three F2 READMEs and refresh `holder-assessment-boundary.md` (cause table,
   precedence paragraph, replay block) or record the parity harm; optionally
   restrict the FN-2 predicate (schema-valid `None` observed holder; tick-order
   non-causation — C6/P3 bounds).
2. coverage — land an in-corpus claim-to-excerpt map in `r87-myth-cluster/`
   (fact → excerpt path:line → delivery mode) so 22/22 is certifiable from the
   tree; declare R9 modes on the four r89-added excerpts (or record the
   exemption); optionally the r88 map; align the ETCSL literal if wanted.
3. depth — close JDEP2's sub-cases: R8 unrecorded-influence trigger + marker
   home; R9 unknown-version disposition; R10 dismissed-overlap record +
   name-identity guard; add an R8 demo fixture. The checker stays silent; these
   are normative rows.
4. process (Q2's three improvements) — poll loops of ≤9 checks or a background
   loop with a closing `POLLS n SPAN … GAPS n` line (the 25×60 s loop cannot
   complete under the 600 s tool cap; 10 seats hit it); a hash-stamped landing
   freeze so cutoff state survives in-place rewrites (23 of 32 seats wrote after
   the cutoff; two overwrote pre-cutoff artifacts); `wave-spec.json` roster +
   `amendments[]` (r89's three integrator edits: the new fixture, the composed
   table, the S2 R3 anchor rewrite) with declared==delivered validation; one
   wave-wide deadline instant.

saturation: not declared (no rubric; the stagnation nudge is not triggered).
retired: none.

Learning trends: expansion improved (149 → 160 fixture dirs; 4 freshly authored
in-world excerpts; 2 knowledge documents added/touched); quality improved
(first-cause disclosure accuracy with 8 durable cause-family fixtures, the
valid-key combined summary, and a negative demo that refuses support); discernment
improved (five independent censuses agree to the tuple — P2/JCAL1/H2/H1/P4 — and
fresh-eyes, attack, capability, and process-audit seats each named their bounds;
Q2 turned the round's own conduct into three adoptable improvements) — with one
recurring failure mode named: **documentation/expectation parity lagged the
checker change for the third consecutive round** (r87 drift repaired at r88
closure; r88 drift repaired at r88 closure; r89 set is carried above). Recommend
adding an expectation-update step to every checker-wording round.

SHONEN: per P4 — `SHONEN.md` byte-unchanged; boxes `[ ]`/`[~]`; box 3 can move
`[ ]` → `[~]` (two demonstrated D1 applications; the r88 drift blocker cleared);
no `[x]` (no named non-author verifier executed the lane's instructions cold).
The SHONEN block lands in the round report, not here.

---

## Appendix — P2 receipts (not part of the drop-in text)

All commands from the repo root; delivered = `1b09f3f`, baseline checker
extracted from `51b286b` (read via stdin pipe because `/tmp` was inode-full).

**Receipts 1 — census + delta (P2 replay).**

```sh
for d in corpus/fixtures/*/; do python3 corpus/fixtures/check_bible.py "$d"; done
# DELIVERED: 160 dirs, exits 0=32/1=128, 399 violations, stderr 0
# BASELINE (git show 51b286b:corpus/fixtures/check_bible.py, stdin): 149 dirs,
#   exits 0=31/1=118, 367 violations, stderr 0; reproduces B1-tuples.json with 0 mismatches
# FULL_TUPLE_CHANGED 4 ['r87-probe-multi-invalid','r87-probe-record-and-chain',
#   'r88-mixed-stop','r88-nonholder-stop']; EXIT_CHANGES []; VIOLCOUNT_CHANGES []
# ADDED 11 (5 r89-c1-*, 3 r89-f2-*, r89-fn2-control, r89-fn2-unresolved-chain-break,
#   r89-inspiration-paraphrase)
```

**Receipts 2 — C1 fixture first stops (delivered → baseline).**

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/<dir>
# r89-c1-invalid-tick         rc=1 4 findings  malformed record (invalid tick)  (baseline identical)
# r89-c1-invalid-from-holder  rc=1 3          malformed record (invalid from_holder)  (identical)
# r89-c1-invalid-to-holder    rc=1 3          malformed record (invalid to_holder)    (identical)
# r89-c1-malformed-source-id  rc=1 3          malformed record (invalid source_id)    (identical)
# r89-c1-multi-cause-valid    rc=1 4          "malformed record (invalid tick);
#     ambiguous holder identity to_holder '…'"  (baseline: tick only)  ← combined summary
# r89-f2-dangling-to          rc=1 4          "holder reference to_holder '…' absent from raw
#     entities and absent from the resolved index"  (baseline: "dangling holder …")
# r89-f2-dangling-from        rc=1 4          same for from_holder  (baseline: "dangling holder …")
# r89-f2-invalid-source-id    rc=1 4          "source reference '…' absent from raw sources and
#     absent from the resolved index"  (baseline: "unknown source '…'")
# r89-fn2-control             rc=1 1          unqualified chain break  (baseline identical)
# r89-fn2-unresolved-chain-break rc=1 2       "possible provenance chain break, not a definite identity
#     mismatch: … not uniquely resolvable (2 raw entity rows …, but only 1 …)"  (baseline unqualified)
# r89-inspiration-paraphrase  rc=0 0          CLEAN
```

FN-1/FN-2 string coverage over all 160 dirs (P2):

```text
  6  2 absent from raw entities and absent from the resolved index
  0  0 present in raw entities but
 15  5 absent from raw sources and absent from the resolved index
  0  0 present in raw sources but
  1  1 possible provenance chain break, not a definite identity mismatch
  1  1 is not uniquely resolvable (
```

**Receipts 3 — checker + tree.**

```sh
git diff --numstat 51b286b 1b09f3f -- corpus/fixtures/check_bible.py   # 54  14
git diff --shortstat 51b286b 1b09f3f                                   # 136 files, +12330/-15
```

**Receipts 4 — C2.**

```sh
# anchor sweep: every row of patches/S2-fact-map.json, grep -nF against
#   corpus/fixtures/r87-myth-cluster/<source_id>-excerpt.md  →  ANCHORS 14/14
# pointers: entities.first_appearance resolved in sources.json  →  POINTERS 7/7
# composition: 7 ptrs + 7 claims + 4 relations + 4 events       →  D1_FACTS 22
python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster   # CLEAN, rc=0
grep -n 'external-only' corpus/knowledge/reference-ledger.md
# 8:| … | external-only / text not delivered at lore; citation is a research lead …
git ls-tree -r --name-only 51b286b -- corpus/fixtures/r87-myth-cluster | grep -c excerpt   # 1
```

**Receipts 5 — C3.**

```sh
grep -c '^| R8 —' corpus/knowledge/r88-sourced-inspiration-decision-table.md   # (sum over R8/R9/R10) = 3
python3 corpus/fixtures/check_bible.py corpus/fixtures/r89-inspiration-paraphrase  # CLEAN, rc=0
grep -nF -- 'moved to the west stair' corpus/fixtures/r89-inspiration-paraphrase/ash-ledger-excerpt.md
# 9:A modern paraphrase says … the tide-mark had been moved to the west stair.
grep -n 'Fails' corpus/fixtures/r89-inspiration-paraphrase/claim-to-excerpt-map.md
# 5:| … | `paraphrase`; fixture writer (R9 demonstration) | `moved to the west stair` | Fails: …
wc -l < corpus/knowledge/r89-cross-cluster-contradiction.md   # 32
grep -c 'Status: `unresolved`' corpus/knowledge/r89-cross-cluster-contradiction.md   # 2
git ls-tree -r --name-only 51b286b -- corpus/knowledge/r89-cross-cluster-contradiction.md \
  corpus/fixtures/r89-inspiration-paraphrase | wc -l   # 0 (both new)
```

**Receipts 6 — capabilities row-2 evidence (observed; same values as JDEP4).**

```text
r87 D1 support: facts=22 OK=22 not-OK=0 (pointers 7/7, hymn 1/1, anchored 14/14)
python3 corpus/fixtures/check_bible.py corpus/fixtures/r89-inspiration-paraphrase → CLEAN, rc=0
grep -nF -- 'moved to the west stair' …/ash-ledger-excerpt.md → line 9 hit
(… while claim-to-excerpt-map.md records the claim as Fails — support withheld)
```

Working-tree state at proposal time: `M l0-questions.md` (K1's authorized
append), `?? .ufo/waves/round-89/followup/`; nothing else. No commit, no push.
