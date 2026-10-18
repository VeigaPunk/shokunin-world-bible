# P2 — Round-91 SCORECARD section proposal (follow-up wave)

Seat: P2. Deliverable: the `## Round 91` section for `SCORECARD.md`, plus the capabilities-table
pointer edit it requires. Status: **proposal — verdict words are P2's measured proposal from the
delivered tree; L1 rules them at closure.** Scores remain unmeasured (no 0–10 rubric exists).
Machine-readable companion: `.ufo/waves/round-91/followup/P2-verdicts.json`.

Note on the r91 wave: this seat ran in the follow-up wave without an explicit 60 s poll loop (the seat
block did not require one); sibling follow-up artifacts were observed arriving during the run (the
`followup/` directory grew from empty to ~45 files, incl. H4/JCAL5/H2/H3/JDEP3/K1/V2/P3). Nothing below
rests on a sibling artifact; every receipt was re-run by this seat on the delivered tree at `c2ab3d0`.

## Work performed

- **Axes measured:** calibration (C1 discriminating fixtures + census + revert control + C9 watch),
  coverage (C2 hardened support command + five negative controls + contract-deviation documentation),
  depth (C3 R8/R9/R10 decisions + boundary-doc reconstruction fidelity and residue).
- **Delivered-tree evidence only for verdicts** (`c2ab3d0`, tracked tree clean; only untracked path is
  `.ufo/waves/round-91/followup/`). Scratch under `/tmp/p2` for probes/controls: the `e97613c` checker
  (`git show`-extracted, hash-stamped), three census scripts, four boundary-doc revisions extracted with
  `git show`, and five mutated copies of the r87/r89 clusters. `df -i /tmp` was checked before and after;
  the 164-directory baseline extraction was deleted as soon as its census was recorded; 79 scratch files
  remain (`/tmp/p2/ctl/*` plus scripts and JSON), `df -i /tmp` free inodes recovered from 1914 to 15484.
- **Commands run (all from `lore-shokunin/`):** `sha256sum corpus/fixtures/check_bible.py`; per-directory
  checker census over `corpus/fixtures/*/` with `cwd` = repo root (two independent scripts, plus one
  same-tree revert run with the `e97613c` checker); the two new fixture README expectation blocks replayed
  on both checkers; `python3 corpus/tools/support_check.py` for `r87-myth-cluster`, `r88-m3-maya-cluster`,
  `r89-inspiration-paraphrase` and five mutated copies; the boundary doc's three pasted command/output
  pairs replayed via a block-extraction harness; the doc's own R9 completeness command; the R9 patch-vs-doc
  keyword check; presence checks of every added line of the M2/M6 candidate patches in the delivered files;
  `git show`/`git diff`/`git log` inventory of the doc lineage (r89-landed, r90-closure, delivered).
- **Write boundary:** this file and `P2-verdicts.json` were the only writes in the repository. No commit, no
  push, no tracked-file edit, no sibling-repo access, no `l0-questions.md` append (not authorized for P2).

## Before → after measurements

### C1 calibration — durable discriminating fixtures, census, revert control, watch

```sh
sha256sum corpus/fixtures/check_bible.py
git show e97613c:corpus/fixtures/check_bible.py | sha256sum   # extracted to /tmp for probes
python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-null-chain
python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-tick-unresolved
```

Observed (delivered checker `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`; identical
to the `a7c6a17` blob, i.e. the r91 checker is unchanged):

```text
r91-c1-null-chain  (exit 1): VIOLATION: entities[3].provenance[1]: provenance chain break; expected from_holder 'mira', got None
                            1 violation(s); no canon changed
r91-c1-tick-unresolved (exit 1): VIOLATION: entities[1].first_appearance: required nonempty str
                            VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3
                            VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
                            3 violation(s); no canon changed
```

Same two directories under the `e97613c` checker (`e2bb9639…`): the null-chain record is the hedged
`… possible provenance chain break, not a definite identity mismatch: …; from_holder None is not uniquely
resolvable (0 raw entity rows carry this id, but only 0 is in the resolved index)`; the tick line is the
identity-qualified `… holder identity is not uniquely resolvable: …; provenance tick 1 must be greater than
previous tick 3`; the chain-break line is byte-identical to the delivered run. Both README expected blocks
(delivered and `e97613c`) match the observed stdout byte-for-byte (4/4 blocks compared mechanically with a
block-extraction harness, exit 1 and stderr empty in all four runs).

Census, per directory, `cwd` = tree root so the path echo is identical across trees:

```sh
python3 /tmp/p2/census2.py "$PWD"          # delivered tree
python3 /tmp/p2/census2.py /tmp/p2/baseline   # git archive a7c6a17 extraction (deleted after use)
python3 /tmp/p2/census3.py "$PWD" /tmp/p2/revert-check.py   # same 166 dirs, e97613c checker
```

Observed: delivered = 166 dirs, exits `{0: 32, 1: 134}`, 421 violation lines, stderr empty in all 166;
baseline `a7c6a17` = 164 dirs, exits `{0: 32, 1: 132}`, 417 violation lines; delta = **2 added
(`r91-c1-null-chain`, `r91-c1-tick-unresolved`), 0 changed, 0 removed, 0 exit changes**. Revert control:
the `e97613c` checker over the same 166 directories changes stdout on exactly those two directories
(stdout SHA-256 `615dc056…` vs `3a337ba4…`; `d754e96f…` vs `71b4ea43…`) and on no other directory; exit
codes and stderr unchanged everywhere. Earlier path-echo differences on five missing-file fixtures
(`r5-missing-file`, `r62-missing`, three `r67-claim-source-unavailable-*`) were reproduced as an artifact
of invoking the checker with different path prefixes (the diagnostic embeds the argument path) and
disappear with the `cwd`-normalized invocation.

Watch: `corpus/knowledge/r91-c9-watch.md` (43 lines) pins the hash above, restates the C9 ruling, and
gives a four-gate falsification trigger + owner. Measured gap: its probe block keeps the placeholder
paths `corpus/fixtures/<counterexample>` / `<uniquely-resolved-control>` (E1 proposed explicit prospective
names; neither watch text is integrated).

### C2 coverage — hardened support command and its negative controls

| command (delivered tree) | observed tail | exit |
|---|---|---|
| `python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster` | `INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 8/8; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 22/22` / `RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 8; TOTAL-ROWS 22` / `SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 8/8; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors)` / `RESULT PASS` | 0 |
| `… corpus/fixtures/r88-m3-maya-cluster` | `INVENTORY JSON-FACTS 10/10; … TOTAL-ROWS 10/10; DISTINCT-ANCHORS 6/6` / `ANCHORS repeated-references=4; DUPLICATE-ROWS 0` / `WARN: unreferenced excerpt declaration: source-excerpt.md (mode=verbatim)` / `RESULT PASS WITH WARNINGS` | 0 |
| `… corpus/fixtures/r89-inspiration-paraphrase` | `SOURCE-SUPPORT 0/0` / `RETELLING-SUPPORT-ONLY 1 entries (1/1 anchors)` / `RESULT PASS` | 0 |

Negative controls on scratch copies of the r87 cluster (probes; the delivered command is the one run):

| mutation | observed diagnostic | exit |
|---|---|---|
| `## JSON facts` renamed to `## Facts` | `FAIL: fact table must be under a JSON facts or Editorial rows heading` | 2 |
| one complete row duplicated | `FAIL: inventory JSON facts mismatch: expected=14 parsed=15` + `FAIL: inventory total mapped rows mismatch: expected=22 parsed=23` + `FAIL: duplicate mapped row E1 appears 2 times` | 1 |
| one anchor corrupted | `FAIL E1: source-support; mode=verbatim; anchor=not-found` + `FAIL: E1: source-support anchor missing`; `SOURCE-SUPPORT 13/14` | 1 |
| one declaration flipped `verbatim`→`summary` | `FAIL: E1: delivery mode missing or mismatched` (×3 rows); `MODES 19/22` | 1 |
| retelling anchor corrupted (r89 demo copy) | `WARN … retelling-support-only; anchor=not-found` + `WARN: retelling anchor not found …`; `RESULT PASS WITH WARNINGS` | 0 |

Freeze: every added line of `M2-hardening-alt.patch` and `M6-reconcile.patch` is present in the delivered
`corpus/tools/support_check.py`, `corpus/tools/README.md`, and the three maps (0 missing per file). M3's
alternative map wording is *not* in the delivered tree (7 lines absent) — candidate rejected, not a defect.
`corpus/tools/README.md:16-21` documents M2's two contract deviations (missing inventory exits 2 instead of
1 + `RESULT FAIL`; no terminal failure summaries) as named debt.

### C3 depth — R8/R9/R10 decisions, register, boundary-doc reconstruction

- R8 failed-gate disposition + withhold precedence: `corpus/knowledge/r88-sourced-inspiration-decision-table.md:40-47`.
- R9 reprint boundary: same file `:49-91` (owner, trigger, decision, worked example, completeness command).
  Delivered doc's own command → `R9 reprint decision completeness: 11/11`, exit 0.
- R10 `source_id` namespace scoping: same file `:105-108`.
- Register: `test ! -e corpus/knowledge/cross-cluster-contradictions.md` → exit 0 (absent ≠ empty; correctly
  absent — no shared referent between the landed clusters).
- Coverage of the *form* the claim promised (owner + trigger + worked example): R9 has all three; R8 and R10
  are decision paragraphs that inherit an owner and carry no trigger/worked-example/verification command.

Boundary-doc lineage and repair:

```sh
git show a7c6a17:corpus/knowledge/holder-assessment-boundary.md | head -3
git show ca7f9ef:corpus/knowledge/holder-assessment-boundary.md | sha256sum
cmp corpus/knowledge/holder-assessment-boundary.md .ufo/waves/round-90/followup/CB1-boundary-refresh.md
```

Observed: the baseline tracked doc at `a7c6a17` is byte-identical to CB1's r90 **instruction sheet**
(`sha256 0d42c988…`, 316 lines, title `# CB1 — Boundary-doc refresh proposal (for the round-90 closure)`) —
the r90 closure's own repair never landed; `ca7f9ef`'s doc is identical to `e97613c`'s (`a4b1b331…`, 630
lines), i.e. the r90 refresh was never applied anywhere. The delivered doc is the reconstruction (549 lines,
`c0c59daf…`) with a repair banner naming the defect and one skipped item (D1 — decision-table row 2 code refs).
Its three pasted command/output pairs replay byte-identically through the delivered checker (14/14 pasted case
blocks, exit 0, stderr empty), and all 22 referenced repository paths resolve.

Measured residue in the reconstruction (all on the delivered doc):

| residue | receipt |
|---|---|
| pre-r90 row kept beside its superseding row | `:179` still says checks incl. ticks are qualified under an unresolved holder; `:184` (pasted r90 row) says `Tick findings are NOT qualified` — one state, contradictory guidance |
| r89 decision row lost | r89-landed `:193` “Two or more causes in one record that passes the key-set check” does not exist in the delivered table; the pasted row occupies its slot (content survives only in the first-stop-causes section and the pasted r89 case) |
| r90 provenance banner + one Limits bullet not applied | delivered doc still reads `Landed at round-89 closure`; CB1's `Refreshed at round-90 closure` banner block and the `- The two r89 hedged shapes are repaired at ca7f9ef …` limits bullet are absent |
| cosmetic | duplicated H1 (`:1`, `:8`); stitched revision sentence at `:40` (`… (…/round-90/followup/CB1.md) delivered checker at 1b09f3f …`) |
| index gap | no `## Round 91` section in `corpus/fixtures/README.md` (last is `## Round 90`, `:1016`) for the two new fixtures; their own READMEs are byte-exact |
| code anchors partially stale | spot-check against the delivered checker: `:169-170` (null guard) and `:323-326` (tick order) are correct; the first-stop-causes text still cites the cause join at `:313-316` although the join is at `:318` (the doc's own evidence section cites `:249-312`/`:313-319`), and decision-table row 2's `:349-350` lands in the allied-relations loop — those row-2 refs are the banner's named skipped item (D1) |

## Findings & named debt

Corroboration (not evidence — this seat's receipts above stand alone): the follow-up seat CB1's doc-state
audit (`.ufo/waves/round-91/followup/CB1.md:97,147,158-161,226-228,267-269,302`) independently reports the
same `:179`/`:184` contradiction, the duplicate H1, the splice fragment, and the named skip — and adds items
beyond this seat's check: three r89 headings not restored, an incomplete 35+13 anchor remap, and stale counts.

### Proposed `SCORECARD.md` text (append after the r90 section, verbatim)

```markdown
## Round 91 — luna round 5 of 12 (2026-10-17)

Two-wave regimen round: work wave (spec declares 32 seats, names 30; `openai-codex/gpt-6-luna-max`,
one unrostered seat `CB1` delivering the boundary-doc audit), follow-up wave on
`alibaba-token-plan/deepseek-v4.1-flash` (operator-directed; fallback alibaba-tp-1 → tp-2 → tp-3 →
opencode-go → zai-glm; hyper exhausted since r89). Spec `.ufo/waves/round-91/wave-spec.md` (W1's
landing record appended) + `wave-spec.json`. Baseline `a7c6a17` (r90 closure); work commits `6332115`
+ `c2ab3d0`; closure = this section's commit. **The r91 checker is unchanged**
(`corpus/fixtures/check_bible.py` = `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`,
byte-identical to `a7c6a17`), so C1 lands regression pins only. Scores remain unmeasured (no rubric);
each row is a claim carrying its counting command and measured commit.

| LIVE axis | r91 verdict | Evidence and limit |
|---|---|---|
| calibration | improved (bounded) | C1 `6332115`: two durable DISCRIMINATING fixtures pin the r90-repaired shapes where the baseline had none (Q90-001 open: a silent revert was invisible to the census). `r91-c1-null-chain` → definite `provenance chain break; expected from_holder 'mira', got None` (1 violation, exit 1) where the `e97613c` checker hedges the same record (`… possible provenance chain break …; from_holder None is not uniquely resolvable (0 raw entity rows carry this id, but only 0 is in the resolved index)`); `r91-c1-tick-unresolved` → integer-only `entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3` (3 violations, exit 1) while its chain-break line stays byte-identically qualified. Counting: fixture census over every `corpus/fixtures/*/` directory at `cwd` = repo root — delivered 166 dirs `{0: 32, 1: 134}` vs `a7c6a17` 164 dirs `{0: 32, 1: 132}`, **0 changed + 2 new + 0 removed, 0 exit changes, stderr empty on all 166**; a simulated revert (the `e97613c` checker over the same 166 dirs) changes stdout on exactly those two directories and nowhere else. Both fixture README expected blocks replay byte-for-byte on both checkers (4/4 mechanically compared). `corpus/knowledge/r91-c9-watch.md` pins the shipped hash, the C9 ruling (tick order is an integer comparison; unresolved non-null holders still qualify chain continuity), and a four-gate falsification trigger with owner. Bounds: the watch's probe keeps placeholder paths (`<counterexample>`/`<uniquely-resolved-control>`) — E1's explicit names are unintegrated (debt); the pin constrains reverts, not new behavior; discrimination covers the two repaired shapes only. |
| coverage | improved (bounded) | C2 `6332115` (M2 stack + M6 reconcile; every candidate added line present in the delivered files, M3's alternative map wording was not applied): the support command asserts the map's declared inventory, reports distinct anchors, fails duplicate rows, and warns on retelling misses. Receipts (exit + print): `python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster` → `INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 8/8; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 22/22`, `RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 8; TOTAL-ROWS 22`, `SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 8/8`, `RESULT PASS`, exit 0; `… r88-m3-maya-cluster` → `10/10`, `WARN: unreferenced excerpt declaration: source-excerpt.md (mode=verbatim)`, `RESULT PASS WITH WARNINGS`, exit 0; `… r89-inspiration-paraphrase` → `SOURCE-SUPPORT 0/0`, `RETELLING-SUPPORT-ONLY 1 entries (1/1 anchors)`, exit 0. Negative controls on scratch copies (probes; delivered command): renamed section heading → `FAIL: fact table must be under a JSON facts or Editorial rows heading`, exit 2; duplicated complete row → `FAIL: inventory JSON facts mismatch: expected=14 parsed=15` + `FAIL: duplicate mapped row E1 appears 2 times`, exit 1; corrupted anchor → `FAIL: E1: source-support anchor missing`, exit 1, `SOURCE-SUPPORT 13/14`; mode flip `verbatim`→`summary` → `FAIL: E1: delivery mode missing or mismatched`, exit 1, `MODES 19/22`; retelling-anchor miss → `WARN … retelling anchor not found`, exit 0. `corpus/tools/README.md:16-21` records M2's two contract deviations (missing inventory exits 2 where S2 required 1 + `RESULT FAIL`; no terminal failure summaries) as named debt. Bounds: those deviations stand (callers read exit code + diagnostic text); `22/22` is rows (14 JSON + 8 editorial), not facts — the split landed in the map and tool README, while `corpus/fixtures/README.md:1018` keeps the older `r87 22/22` shorthand (wording debt); lexical preflight only — whole claim, translation fidelity, and rights remain human decisions; mode truthfulness is self-declared. |
| depth | improved (bounded) | C3 `6332115` + `c2ab3d0`: JDEP2's three prospective edges are decided in `corpus/knowledge/r88-sourced-inspiration-decision-table.md` — R8 failed-gate disposition + detail-over-element withhold precedence (`:40-47`), R9 later-reprint boundary with tie-reliability criterion + worked example + completeness command (`:49-91`; `R9 reprint decision completeness: 11/11`, exit 0), R10 `source_id` namespace scoping (`:105-108`). Register correctly absent (`test ! -e corpus/knowledge/cross-cluster-contradictions.md` → exit 0; no shared referent between the landed clusters — JDEP3/J3). **Boundary-doc repair (inherited defect, found and repaired in-round):** at `a7c6a17` the tracked boundary doc WAS CB1's r90 instruction sheet (byte-identical to `.ufo/waves/round-90/followup/CB1-boundary-refresh.md`; 316 lines; title `# CB1 — Boundary-doc refresh proposal`) — the r90 closure's own repair never landed (Q1 `closure_regression`); the r91 integration rebuilt the contract from CB1's r90 sections against the r89-landed contract (549 lines). The rebuilt contract replays its three pasted command/output pairs byte-identically on the delivered checker (14/14 pasted case blocks) and all 22 referenced repo paths resolve. Bounds / residue (measured, not netted): the table keeps the pre-r90 row at `:179` (checks incl. ticks “qualified” under an unresolved holder) that the pasted row at `:184` (“Tick findings are NOT qualified”) supersedes — one state, contradictory guidance read in order; the r89 row “Two or more causes in one record that passes the key-set check” was overwritten by that paste instead of being kept; CB1's r90 provenance banner and one Limits bullet are not applied (the doc still reads `Landed at round-89 closure`); duplicated H1 (`:1`, `:8`) and one stitched revision sentence (`:40`) are cosmetic; the repair banner names one skipped item (D1 — decision-table row 2 code refs); R8/R10's r91 decisions carry no trigger/worked-example/verification form (R9 carries all three); no `## Round 91` entry in `corpus/fixtures/README.md`. |

Learning trends: expansion improved (164 → 166 fixture dirs; the census itself now discriminates, since a
revert flips exactly the two new fixtures); quality improved (a real contract replaces an instruction sheet
and replays 14/14 pasted outputs; support receipts carry inventory/distinct-anchor/split rows); discernment
improved (the round found and repaired an inherited integration defect instead of inheriting it silently,
and the reconstruction residue is measured and named as debt rather than netted against the repair).

Capabilities: no third row — C1 is regression coverage and C2 is hardening of the existing capability, not
new repertoire. The repertoire table's row 2 evidence pointer is updated to the hardened receipt
(see the pointer edit below) and its bounds gain the two documented contract deviations.

planned (r92, from Q1 with L1 adoption; Q1's proposal is explicitly conditional on calibration ranking
lowest under the severity rule): (1) calibration — close Q90-001's remaining item (a tracked, executable
C9 falsification probe in place of the placeholder paths, E1's names) and keep the two fixtures as the
revert tripwire; (2) depth — repair the decision-table residue (supersede the `:179` row instead of
duplicating it; restore the r89 multi-cause row), apply the r90 replacement set's banner/limits blocks,
and give R8/R10 the trigger/worked-example form; (3) coverage — extend the rows-not-facts wording to
`corpus/fixtures/README.md:1018`, add the `## Round 91` fixture-README section, and reconcile or re-scope
the `RESULT FAIL` contract deviation. Process: commit the poll helper and a roster/wave-spec validator
(P1/P2 remain unlanded; `wave-spec.json` landed without one), set a numeric scratch budget (P3), and
resolve the 32-declared/30-named roster mismatch.
saturation: not declared (no rubric; the stagnation nudge is not triggered). retired: none.

SHONEN: box 1 `[ ]` (no SKILL.md); box 2 `[~]` (LOG evidence improves again — the r91 trailing record);
box 3 `[~]` (the instruction surfaces are delivered-tree-true again — the boundary doc's pasted outputs
replay 14/14 and the support command is reproducible with fail-closed controls — but the reconstruction
residue above and the absent external verifier keep `[x]` withheld); box 4 `[~]` (province-clean;
kotodama acknowledgement untriggered; no new cross-domain bleed).
```

### Proposed capabilities-table pointer edit (row 2, `in-world excerpt support verification`)

Replace the evidence cell

```text
`python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster` → 22/22 exit 0; `... r88-m3-maya-cluster` → 10/10 exit 0; paraphrase demo retelling-only
```

with

```text
`python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster` → `INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 8/8; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 22/22` … `RESULT PASS`, exit 0; `... r88-m3-maya-cluster` → 10/10 + `WARN: unreferenced excerpt declaration`, exit 0; `... r89-inspiration-paraphrase` → retelling-only, `SOURCE-SUPPORT 0/0`, exit 0
```

and append to the row's bounds: `22/22` counts rows (14 JSON + 8 editorial), not facts; the map inventory
is asserted, duplicate rows fail, retelling misses WARN; the two M2 contract deviations (missing inventory
exits 2; no terminal `RESULT FAIL`) are named debt in `corpus/tools/README.md:16-21`.

### Named debt created or carried by r91 (for planner/L1)

1. C9 watch probe is a placeholder path pair; no tracked, executable counterexample/control names.
2. Boundary-doc residue: pre-r90 `:179` row superseded-not-removed (contradicts the C9 ruling on one state);
   r89 multi-cause row lost from the table; r90 banner + Limits bullet unapplied; duplicated H1; stitched
   sentence at `:40`; banner names one skipped item (D1) although three replacement blocks are absent.
3. R8 and R10 r91 decisions lack the trigger/worked-example/verification form the C3 claim promised.
4. `corpus/fixtures/README.md` has no `## Round 91` section (the two new fixtures are documented only in
   their own READMEs).
5. Coverage wording: `corpus/fixtures/README.md:1018` still says `r87 22/22` without the JSON/editorial split.
6. Support-command contract: two documented deviations vs the S2 terminal-status contract (exit 2 on missing
   inventory; no `RESULT FAIL`/`RESULT ERROR` summaries) — reconcile or re-scope.
7. Process: no committed poll helper (P1), no roster/wave-spec validator (P2 partial), no numeric scratch
   budget (P3); roster declares 32 seats but names 30.

### Process observations (not axis verdicts)

- The follow-up wave's artifact set was still arriving during this seat's run; nothing here depends on a
  sibling artifact, and no sibling verdict was copied. Sibling receipts I happened to see (`H4-census.json`,
  `JCAL5-delta.json`) report the same census deltas this seat measured independently (166 vs 164 dirs,
  0 changed / 2 added, 0 exit changes; `changed_under_old_checker` = the two new fixtures).
- The r91 wave left `.ufo/waves/round-91/wave-spec.md` and `wave-spec.json` in the work commit, but the two
  r90 process items (poll helper, validator) remain unlanded; the scorecard's process sentence states this.

## Handoff

- **Baseline:** `a7c6a17` (r90 closure). **Delivered revision measured:** `c2ab3d0` (tracked tree clean; only
  untracked path `.ufo/waves/round-91/followup/`). Work commits `6332115` + `c2ab3d0`; **no commit/push by
  this seat**.
- **Deliverable:** this file's `### Proposed SCORECARD.md text` block is the section to append to
  `SCORECARD.md` after the r90 section, plus the capabilities row-2 pointer replacement above. The proposed
  verdicts are `improved (bounded)` on all three axes with the bounds stated; L1 rules the words at closure.
  Machine-readable companion: `.ufo/waves/round-91/followup/P2-verdicts.json`.
- **Key receipts (all re-runnable on the delivered tree):** `sha256sum corpus/fixtures/check_bible.py`
  (`ff9fd2aa…`); the two fixture commands with their README-expected stdout; the 166-directory census with
  the `e97613c` revert control (exactly two changing stdout tuples); the three support-check receipts and
  the five negative controls; the boundary doc's three pasted command/output pairs and its own R9
  completeness command; `git show a7c6a17:…` proving the mis-landed instruction sheet.
- **Scratch:** `/tmp/p2` (three census scripts, both checker copies, four doc revisions, five mutation
  controls, control outputs); the 164-dir baseline extraction was deleted after its census. Nothing under
  `/tmp/p2` is needed to re-verify — every command above runs against the delivered tree and, for the
  `e97613c` control, `git show e97613c:corpus/fixtures/check_bible.py`.
- **Left undone / for follow-up:** the residue list above is measured but not repaired (repairing tracked
  docs was outside this seat's write boundary). No explicit 60 s poll loop was run by this seat; sibling
  follow-up seats were mid-flight throughout, so an integration-time cross-check against their verdicts
  (esp. V2's freeze receipt, CB1's doc-state audit, and the H4/JCAL5 censuses) is advisable before closure —
  CB1's audit already corroborates the `:179`/`:184` residue and adds items (three unrestored headings,
  incomplete anchor remap, stale counts). No l0-questions entry was written (P2 is not authorized);
  if the boundary-doc residue or the support-command contract deviation needs an operator decision, that
  append is L1/K1's call.