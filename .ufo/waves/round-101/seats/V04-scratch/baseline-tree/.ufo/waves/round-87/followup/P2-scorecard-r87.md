# PROPOSAL ONLY — Round 87 SCORECARD section (P2)

Do not copy into `SCORECARD.md` unedited. Scores remain unassigned: no bounded
0–10 rubric exists, so counts, exit codes and verdicts below are measurements
and judgments, not scores. Every figure was measured on the delivered tree at
`2b48ca72033dfd1060b6f81c4cf27ad83deae57f` (tree clean apart from untracked
`.ufo/waves/round-87/followup/`), never on a scratch patch. The per-claim rows
are additive to the `axes` table above; the LIVE table is the round verdict
block in the voice of the r86 section.

## Round 87 — per-claim before → after

| # | claim (axis) | measured commit | before → after | counting command / observed |
|---|---|---|---|---|
| C1 | calibration — per-record unassessed disclosure for ambiguous provenance holders | `03c6746` (delivered; +17 lines in `corpus/fixtures/check_bible.py`, +4 fixture dirs) | Before (`28706dc`): the ambiguous-holder stop emits one item-global notice only; records after the stop carry no local disclosure, so an encoded later holder mismatch is unreported. After: every record at/after the stop emits a local disclosure naming the ambiguous field, the holder id, and the origin record; the original notice is retained; assessment never resumes and no duplicate identity is chosen. | `sha256sum corpus/fixtures/check_bible.py` → `3ae4134d1d7d0f4b72f5ed0b344de54e886b60ab7cacd8e8ab0008521efcb237` (baseline `28706dc`: `e8f241623aa84eb1dce192a03c9e70b8f4ba386344f0b22a99ba1ac0d4942132`). Full before/after tuple replay over every `corpus/**` dir holding `entities.json` (147 dirs): `changed=5` — 133 inherited `corpus/fixtures` dirs **0 changed**; 3 changed inherited probes `r85-masked-ambiguous` (3→5 findings), `r85-isolated-ambiguous` (3→4), `r85-harbor-repro` (5→7); 2 new `r87-masked-break-{to,from}-ambiguous` fixtures (6 findings each). 5 added finding tuples, 0 removed, all exit codes unchanged. Independent delivered-tree harm sweep (`followup/H3.md`, checker sha256 pinned to the same `3ae4134d…`): 8/8 provenance mutations exit 1 with either an independent report or a per-record disclosure, `0 silent passes`; corpus-wide `146` dirs compared pre-C1 vs delivered → `exit-code changes: none`, `fixtures losing a reported finding: none` (gains only). |
| C2 | depth — provenance-chain decision table | **TBD-by-parent** | Before: no decision-table knowledge file at either proposed destination. After: **still not measured at `2b48ca7`** — `corpus/knowledge/r87-provenance-chain-decision-table.md` and `corpus/knowledge/provenance-chain-decision-table.md` are both absent. | `ls corpus/knowledge/` → no decision-table file (only `2026-10-12-lore-decision-table.md`, `r74-slate-wording-decision-table.md`, `holder-assessment-boundary.md`, others). Drafts exist as evidence only: `patches/D1-decision-table.md` (23 rows), `patches/D2-decision-table.md` (30 replay blocks); `R2`/`T2`/`SE1` replayed 30/30 outputs. **Not a claim until a consolidated file lands and is replayed.** Post-measurement note: I1's two authorized probe dirs `corpus/fixtures/r87-probe-entry-shape/` and `corpus/fixtures/r87-probe-record-and-chain/` appeared in the working tree after `2b48ca7` (fixture count 138→140), but the knowledge file itself was still absent at P2's last check — the C2 row stays a placeholder until it lands. |
| C3 | coverage — `r87-myth-cluster` world-bible fixture | `e4708cb` (delivered; +1 fixture dir, 9 files) | Before (`28706dc`): directory absent; `check_bible.py corpus/fixtures/r87-myth-cluster` fails with 5 "No such file" violations (M4 replay). After: `CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0; structurally 7 entities / 2 factions / 4 relations / reciprocal alliance true / 4 events / 3 `depends_on` edges / 1 reported-not-resolved contradiction / 5 sources / 4 prose files. | `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster` → `CLEAN: schema, citations, relations, timeline; 0 violations` (exit 0). Structural count command (parses the four JSON tables): `entities=7 factions=2 relations=4 allied_with=2 reciprocal_alliance=True events=4 dependency_edges=3 contradictions=1 sources=5`. |
| ext | census extension (measurement, not an axis claim) | `2b48ca7` + `followup/I3.md` | 133 fixture dirs / exits `{0:28,1:105}` / 259 violations / 705 corpus JSON → 138 dirs / exits `{0:30,1:108}` / 272 violations / 730 corpus JSON (685 under `corpus/fixtures`). 0 non-empty stderr before and after; 0 inherited JSON bytes changed. | `python3 - <<PY` … replaying every immediate `corpus/fixtures/*` dir → `fixture_dirs=138 exit_counts={0:30,1:108} stderr_nonempty=0 total_violations=272 corpus_json_paths=730 fixture_json_paths=685`. Independently reproduced by `followup/I3.md` (`133 + 5 = 138`; S4's `134` arithmetic superseded) and consistent with `patches/B1.md` baseline. |

### C1 detail — exact added tuples (delivered checker, `03c6746`)

Added lines are findings-only; no pre-existing line was reworded or removed, and
only the terminal count line changes. Verbatim additions:

```text
# corpus/live/runs/round-85/probe-inputs/r85-masked-ambiguous  (3 -> 5)
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'vault' first occurred at entities[3].provenance[1]
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'vault' first occurred at entities[3].provenance[1]

# corpus/live/runs/round-85/probe-inputs/r85-isolated-ambiguous  (3 -> 4)
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'vault' first occurred at entities[3].provenance[2]

# corpus/live/runs/round-85/probe-inputs/r85-harbor-repro  (5 -> 7)
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'harbor' first occurred at entities[3].provenance[1]
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'harbor' first occurred at entities[3].provenance[1]
```

The delivered wording is the **X1** variant (`patches/X1-c1.patch`), not the X3
minimal tail-only variant that `R1` ranked first: the checker sha256 above equals
the X1 candidate hash recorded in `patches/C6.md:22`, and the added-line text
matches `patches/X1.md:15-24` verbatim. `V1`/`V3`/`V4` therefore verified
scratch patches of a *different* wording than the one shipped; the delivered
behavior is evidenced by this replay, by `patches/C6.md` (142-input X1 census:
`unchanged=139 changed=3 added_findings=5 removed_findings=0`), by `followup/I3.md`,
and by `followup/E2-strings.json` (6 findings per masked fixture, both directions
and both-fields). `C5`'s standing caveat applies to the shipped text: the
disclosure names a *later additional* ambiguity, so if an unknown source latched
the gate first, the line is not the sole stop cause. The mixed-cause case is not
covered by any delivered fixture.

Two boundaries the round record must keep:

- **Disclosed, not reported.** `H3` shows the delivered checker *discloses* the
  tick-inversion and holder-swap mutations as unassessed but does not
  independently report them (`followup/H3.md` D2). Any claim must use "reported
  or disclosed-as-unassessed", never "reported".
- **The `input-structural finding, not sourced-canon` qualifier is unreachable in
  the delivered corpus.** `followup/E2-contrast.json` sweeps all 138 fixture
  dirs: `fixtures_emitting_qualifier: 0`. It is reachable only from scratch
  inputs. Do not cite a delivered fixture as exercising that branch.

### C3 detail — structural counts (delivered tree)

```text
entities=7 factions=2 relations=4 allied_with=2 reciprocal_alliance=True events=4 dependency_edges=3 contradictions=1 sources=5
md files: README.md, inspiration-note.md, lowwater-hymn-excerpt.md, symbolism-clause-map.md
```

`contradictions.json` records one place disagreement (Moon-Basin Vow: gate-witness
vs dune-register) with no resolution field. `JCOV4` re-derived the same counts on
the delivered tree and matched `C7`/`M4`'s M3 numbers field-for-field, so the
delivered cluster is the M3 candidate and the C7/M4 PASSes cover the shipped
content. `JCOV2` verified all four PROVINCE invariants on the delivered tree
(three separate attribution/rights/AI-training questions; no rights claim; every
reference resolves, `0` unresolved of 5 source ids; the contradiction is reported,
not resolved) and re-fetched the ETCSL page, confirming lines 122–163 match the
note's description. Two support gaps are named, neither a checker violation and
neither repaired: (a) `entities.json` attributes `mother-tide-gate.first_appearance`
and one claim to `lowwater-hymn`, but the delivered excerpt contains no proper
place name (`grep -c "Mother-Tide" lowwater-hymn-excerpt.md` → `0`); (b)
`relations.json` `shellweavers keeps_watch_with reed-bell` cites `shell-charter`,
which has no excerpt in the fixture. The round record must carry both if C3 claims
"in-world texts delivered and auditable".

## Round 87 — LIVE axis verdicts

Verdicts are **PENDING-L1**: P2 measures and reports, L1 adjudicates. The
evidence column states what the delivered tree shows; the verdict cell is not
P2's to assign.

| LIVE axis | r87 verdict | Evidence and limit |
|---|---|---|
| depth | PENDING-L1 | C2 not delivered: no decision-table knowledge file at `2b48ca7` (drafts only). C1 changed the checker's disclosure contract — a behavior change, not new depth documentation; no new checker rule was added by C1 or C3. Follow-up judge recommendation: `followup/JCOV2.md` → depth **unchanged**. Limit: the shipped C1 wording diverges from every verified scratch patch, so its own verifier receipts do not cover the delivered text. |
| coverage | PENDING-L1 | C3 delivered one clean cluster (7 entities / 2 factions / 4 relations / 4 events / 1 reported contradiction) and the census moved 133→138 fixture dirs; `S2` found no prior mythology/folklore citation precedent. Follow-up judge recommendation: `followup/JCOV2.md` → coverage **improved (bounded)**, with the documentation sub-axis **unchanged/partial**. Limit: 1 of the 5 new dirs is C3's; the other 4 are C1's chain/masked controls, so the surface grew by one topic cluster. `S1` lists many provenance branch classes still without an active fixture; no `## Round 87` section exists in `corpus/fixtures/README.md`; two new fixture READMEs declare no expected exit. |
| calibration | PENDING-L1 | C1's local disclosure is a real observability gain over the single global notice, reproduced on the delivered tree (5 additions / 0 removals / 0 exit changes) and corroborated by `followup/H3.md` (8/8 mutations, 0 silent passes) and `followup/JCOV2.md` (calibration **improved**, observed). Limit: `C5`'s mixed-stop-cause caveat; the tick-inversion and holder-swap defects are disclosed, not reported; and the delivered wording was never independently verified *as shipped* — the V1/V3/V4 receipts measured other patches. |
| adjacency (not a lore-owned axis; reported for the fleet) | PENDING-L1 | `followup/JCOV2.md` → adjacency **unchanged, no harm**; the cluster stays inside `PROVINCE.md:3,5-9` and no sibling's scope is silently absorbed. Named debt: the C3/chousa source-method line is a wording gap (refine `PROVINCE.md:5-8` → becomes `unprovable-but-better`); `kotodama-shokunin` is a newly minted, unaddressed C3 adjacency (`followup/K2.md`); `art-east-asian-design`, named in `PROVINCE.md:9`, does not exist at the fleet root. |

Scores remain unmeasured. Calibration remains the existing falsifiability
tie-break among unmeasured axes, not a numerical lowest-axis claim; that is
unchanged from r86 and is not re-argued here. **No axis is recorded as harmed**:
every measured delta is additive (findings gained, none lost; exit codes and
inherited JSON bytes unchanged), and the documentation, boundary-doc and
citation-registration gaps are reported as debt rather than folded into any gain.

Measurement: full-census replay and before/after tuple diff on the delivered tree
(commands and outputs in the per-claim table), checker
`sha256 3ae4134d1d7d0f4b72f5ed0b344de54e886b60ab7cacd8e8ab0008521efcb237`,
plus `followup/I3.md`, `followup/E2-strings.json`, `followup/E2-contrast.json`,
`followup/H3.md`, `followup/JCOV2.md`, `followup/JCOV4.md`, `patches/C6.md`.
138 fixture tuples, exits `{0:30,1:108}`, 272 violations, 0 non-empty stderr,
0 inherited JSON bytes changed.

Learning trends: expansion changed (coverage 133→138 fixture dirs, one new topic
cluster; `S2` measured a previously absent citation class); quality unchanged (no
depth documentation landed; the C2 table is still absent, and the checker gained
no new rule); discernment improved on evidence, pending L1 (the follow-up wave
caught the delivered-vs-verified wording divergence, the mixed-stop-cause
attribution gap, the hymn-attribution support gap, the F2 fixture-base divergence,
and the stale boundary doc — none of which the author seats reported). No outside
admit/reject spot-check or promotion is claimed.

### Contract-field updates (AXES.md §SCORECARD.md contract)

planned: (1) **C2 — depth**: land one consolidated
`corpus/knowledge/r87-provenance-chain-decision-table.md` from `D1` + `D2`
(destination contested; `R2`/`T2` converge on the unprefixed path), add the
`item-chain-valid` clean control, narrow the ambiguous-source wording, make the
tail probes reproducible, and replay every ambiguous-holder row against the
delivered C1 output — not the `28706dc` snapshot. (2) **C1 follow-through**:
re-verify the *shipped* X1 wording (the verified V1/V3/V4 receipts cover
scratch variants) and add a mixed-stop-cause fixture, or make the disclosure
non-causal. (3) **calibration**: refresh
`corpus/knowledge/holder-assessment-boundary.md` to the delivered behavior and
replace its stale "STATIC PENDING PARENT RUNTIME" status with an as-of revision
(`patches/CB1-drift.json` carries the draft replacements); the referenced
`corpus/fixtures/measure_holder_disclosure.py` is absent from HEAD, so no
five-gate score may be claimed. (4) **coverage documentation**: append a
`## Round 87` section to `corpus/fixtures/README.md` (its own convention; absent
per `followup/JCOV2.md`) and give `r87-masked-break-{to,from}-ambiguous/README.md`
and `r87-myth-cluster/README.md` a declared expected exit, per S4 step 2.
(5) **citation registration**: decide whether the ETCSL inspiration belongs in
`corpus/knowledge/reference-ledger.md`, which `seed.md:26-29` names as the
real-world entry point but which does not list it (`grep -c etcsl` → 0).

saturation: **not declared — the lane cannot set a saturation line without the
bounded 0–10 rubric the round's plan required but did not establish**; scores are
still unmeasured, so "every owned axis at or above the line" is not evaluable.
Stagnation window N: the `capabilities` table is still empty, so the count of
rounds since the last capability row is unbounded; N is not declarable from the
current table. The stagnation nudge is therefore **not** triggered and the
lowest-axis obligation is not waived. Proposed declaration for L1: set the
saturation line only after a rubric exists, and start N at the first round that
lands a capability row (r87 delivered a candidate — see below).

retired: none added. No axis is retired or split this round; no saturation-based
retirement is claimed, and the historical duplicate-name rejection
(`SCORECARD.md:14`) remains in force.

## Capabilities — candidate row for L1 (not entered by P2)

| Capability | What it can now do | Evidence pointer | First-working round |
|---|---|---|---|
| per-record holder-disclosure replay | Disclose, at every provenance record at/after an ambiguous-holder stop, which holder field and id stopped the chain and where it first occurred — without resuming comparisons or selecting an identity | `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-masked-break-to-ambiguous` → 6 findings incl. three `... first occurred at entities[3].provenance[0]` lines (delivered tree `2b48ca7`); corroborated by `followup/H3.md` (8/8 mutations, 0 silent passes), `followup/E2-strings.json`, `patches/C6.md` | r87 |

Per AXES.md a capability row requires a passing demonstration in the round report
and the lane's sign-off; P2 supplies the demonstration, L1 decides admission.
The row is **not** entered in this proposal. Note the wording bound: the
capability is *disclosure*, not detection — H3's tick-inversion and holder-swap
cases are disclosed, not reported.

## Open evidence gaps P2 could not close

- C2 has no commit and no delivered knowledge file; the per-claim row is a
  placeholder by design (`TBD-by-parent`).
- The boundary-knowledge refresh (I2 target) and the C2 decision table (I1 target)
  were not present in `followup/` at either of P2's two 60-second-spaced checks
  (01:40:49 and 01:41:47 `-03:00`; a third listing at 01:42:17 showed the same
  absence, plus the later `H3`/`JCOV2`/`E2-contrast` artifacts). This section is
  built from the wave evidence and the `followup/` artifacts that did exist
  (`I3`, `K2`, `Q1`, `JCOV4`, `JCOV2`, `H3`, `E2`).
- **Post-measurement sibling arrivals (after `2b48ca7`, not in this section's
  measurements).** At P2's final check the working tree had gained
  `corpus/knowledge/holder-assessment-boundary.md` (modified, `186 insertions(+)
  / 71 deletions(-)` — I2's authorized refresh) and the two untracked I1 probe
  dirs `corpus/fixtures/r87-probe-entry-shape/` and
  `corpus/fixtures/r87-probe-record-and-chain/`, taking the fixture count to
  `140`. The decision-table knowledge file was still absent. Every count and
  verdict above is measured at the committed tree `2b48ca7` and is unchanged by
  those arrivals; the census row's `138` must be re-measured if the probes are
  committed, and the boundary-doc staleness item is closed by I2's edit.
- `followup/H3.md` D1: `V4`'s two F2-derived mutation cases were defined against a
  fixture (`r87-f2-masked-break-from-ambiguous`, 4 records, `aster` at `[1]`) that
  is **not** the one that landed (`r87-masked-break-from-ambiguous`, 3 records,
  `dup` at `[0]`). No seat should cite `V4`'s F2 output as delivered-tree evidence.
- No file was written to `SCORECARD.md`; no score, verdict, or retirement was
  asserted.
