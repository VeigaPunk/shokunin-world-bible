# F27 — Round-93 SCORECARD proposal (scribe draft; NOT an admission record)

Status: scribe proposal for L1. Do **not** land as the round record until the full fresh
`opencode-go/deepseek-v4.1-flash` follow-up is received and recorded and L1 rules the
per-axis verdicts. No pre-admission, no promotion finding, no numeric score, no saturation.
Measured candidate: `4780cf088ab338f42b85739517aa237c968c4aea`; original work commit
`65838f867d6ece8e7b8bdcc4ffc667a08a1b785e`; pre-round baseline `87779a0`.
The candidate does not itself update `SCORECARD.md`/`LOG.md`/`SHONEN.md`
(`git diff --name-only 87779a0..4780cf0 -- SCORECARD.md LOG.md SHONEN.md` → empty); this
proposal is the SCORECARD material; the LOG entry and SHONEN re-file remain lane/L1 acts.

## Round 93 — luna round 7 of 12 (2026-10-17)

Two-wave regimen round: WORK wave (31 dispatched of 32 declared, `openai-codex/gpt-6-luna-max`;
one seat below declaration, parent strengthening is not a seat — `recovery/R29-record-errata.md`,
`recovery/work-dispatch.json`), then a corrective batch (`R01–R32`), then the fresh required
DeepSeek FOLLOW-UP (this wave). Work commit `65838f8`; corrective/freeze commit `4780cf0`
(candidate). All repairs committed; verdicts below are scribe recommendations from
same-lane re-execution at `4780cf0` — not external non-author verification, not admission.
Scores remain unmeasured (no 0–10 rubric); every row is a claim carrying its counting command
and measured commit.

| LIVE axis | r93 verdict (recommended) | Evidence and limit |
|---|---|---|
| depth | improved (bounded) | **C1** `65838f8` + `4780cf0`. Before (`87779a0`): `git show 87779a0:corpus/knowledge/r88-sourced-inspiration-decision-table.md \| python3 -c "…"` → `gate inside R9 appendix: False`; a 14-clause sample of the required R9 literals present inside the pre-round appendix slice: 4/14; `git cat-file -e 87779a0:corpus/knowledge/r93-r8-worked-example.md` → absent; `git cat-file -e 87779a0:corpus/tools/boundary_doc_check.py` → absent. After (run from lane root at `4780cf0`): the same venue one-liner → `True`; the decision table's LAST shell block (R9 delivered-appendix completeness) → exit 0, `36/36 requirements`, `36/36` clause-removal controls each failing exactly its own finding; the dossier's `### Corrected replay` block → exit 0, `record cells: 12/12`, canonical digest `da934a7e…`; `python3 corpus/tools/boundary_doc_check.py` → exit 0 `CERTIFIED`, receipts 3/3, cases 14/14, anchors 2/2; `--self-test` → exit 0, 8/8 controls; pin-drift control (`--doc` on a mutated copy) → `FINDING document_drift`, exit 1. Frozen bytes unchanged vs `65838f8`: checker `ff9fd2aa…` and boundary doc `7f815a93…` (2/2 byte-identical). Bounds: `CERTIFIED` = frozen-document drift + receipts + explicit numeric anchor ranges + structure only (no semantic/AST/prose validation); the R8 dossier is an illustrative model record, not an observed submission; the R9 check is textual completeness, never translation/source/rights review; the earlier 5/5 substring replay is superseded and was not used. |
| coverage | improved (bounded) | **C2** `65838f8` + `4780cf0`. Before: 166 fixture dirs (`git ls-tree 87779a0:corpus/fixtures/ \| grep -c '^040000'`), no Kojiki cluster (`git cat-file -e 87779a0:corpus/fixtures/r93-m2-kojiki-cluster/entities.json` → absent), ledger without the Chamberlain row. After: 167 dirs; `python3 corpus/fixtures/check_bible.py corpus/fixtures/r93-m2-kojiki-cluster` → exit 0 `CLEAN`, 0 violations; `python3 corpus/tools/support_check.py corpus/fixtures/r93-m2-kojiki-cluster` → exit 0, `SOURCE-SUPPORT 12/12; EDITORIAL-ANCHORS 3/3; TOTAL-ROWS 15/15; DISTINCT-ANCHORS 15/15; MODES 15/15; VALIDATED-ROWS 15/15`; independent census sweep: 167 dirs / 33 exit-0 / 134 exit-1 / 421 violation lines / no stderr / no unexpected exit; R10 `R10-key-scan.py` re-run → all normalized-key intersections empty vs both prior clusters (`2/2`) and all recorded input hashes match (`599d2507…`, `99747217…`, `0bb9084f…`); ledger +1 Chamberlain/Kojiki row; `contradictions.json` `[]`. The work-commit message's "10 JSON" is superseded by committed errata (`R29`): receipt is 12 JSON + 3 editorial. Bounds: the three translation rows are editorial comparisons only (no R9 manual PASS, no R5 support, rights/permission open); "zero shared referents" is a normalized-key scan + same-lane manual review (R10), not external verification; `R10-key-scan.json` `measured_revision=65838f8` is a historical capture (input-hash checks still true at HEAD); whole-claim review is `recovery/R12.md` (same-lane), which names the tick/`depends_on` normalization caveat. |
| calibration | improved (bounded) | **C3** `65838f8` + `4780cf0`. Before: `corpus/knowledge/r91-c9-watch.md` had 1 check-log row; `corpus/tools/discriminate_check.py` absent. After: 2 rows (row 2 `2026-10-17 (r93)` `DISCRIMINATION HELD`, gate 3 not met, trigger unsatisfied, ruling retained, next re-check r94) plus an append-only r93 clarification that replaces the row's imprecise abbreviation and the ambiguous "all four gates reproduce" phrase; `python3 corpus/tools/discriminate_check.py` → exit 0 `DISCRIMINATION HELD` (checker hash matches pin, both fixtures `pinned_semantic_gate=PASS`); negative control `--checker e97613c` → exit 2 `REGRESSION-DETECTED` (expected control, not a delivered pass); fixture negatives `r91-c1-null-chain`/`r91-c1-tick-unresolved` → exit 1 with their recorded findings. Bounds: no external non-author verification; the four-gate falsification trigger remains unsatisfied (gate 3 unmet); R24's historical debts (SHONEN box-3 record mismatch, r89 regression record, r91 missing SHONEN heading) await L1's correction record; the discriminator covers only its two pinned fixtures. |

**Other owned-axis check (observed scope).**

| axis | r93 recommendation | Observation and limit |
|---|---|---|
| operability | improved (bounded) | Two new committed runnable gates (`boundary_doc_check.py`, `discriminate_check.py`) with documented verdict maps, self-test/default instructions, and registry rows (`SKILL.md` Gate registry; `corpus/tools/README.md`); re-run commands produced the stated outcomes. Bound: `support_check.py` and `discriminate_check.py` still lack protocol self-test modes (named conformance debt, `SKILL.md:46`). |
| freshness | improved (bounded) | Persisted in-repo pins for the frozen boundary doc + checker (`corpus/tools/boundary-doc-contract.json`) with a runnable drift detector (default, self-test controls, live `document_drift` negative control); dated C9 re-check 2 with due round. Bounds: the contract manifest is colocated and not independently pinned against coordinated edits to both; R10 JSON `measured_revision` is a historical capture. |
| adjacency | unchanged | No cross-domain evidence newly encountered in scoped verification; no bleed found (Kojiki translation kept editorial; kotodama contract digest-change question routed to `l0-questions.md` round-93 lines as informational, not absorbed). R10 discipline demonstrated. |

Learning trends: expansion improved (166 → 167 fixture dirs; third mythology family landed
with a full 12+3 map and a separate ledger row); quality improved (R9 venue repaired and
replayable, R8 dossier now an exact-cell replay, two new fail-closed gates); discernment
improved (the corrective commit replaced a gameable 5/5 substring replay with a 12-cell
digest, fixed historical evidence cells, and the C9 watch's second check is dated with its
unsatisfied trigger stated honestly). No axis found harmed in scoped verification.

**Capabilities (proposed; enters only on L1 admission).** Proposed row — **bounded
frozen-document certification**: verify the boundary document and delivered checker against
persisted byte pins, replay recorded receipts, resolve explicit numeric anchor ranges, and
check limited structure, returning exit 0 `CERTIFIED` / exit 1 findings. Evidence:
`python3 corpus/tools/boundary_doc_check.py` → exit 0 `CERTIFIED` (receipts 3/3, cases 14/14,
anchors 2/2); `--self-test` → exit 0 (8/8 controls); mutated-copy `--doc` control → exit 1
`document_drift`. First-working round: r93. Bounds: no semantic/AST/general prose validation;
colocated manifest not independently pinned. No capability row is proposed for the Kojiki
cluster (instance-only coverage, not a capability). The two missing self-tests remain debt,
not implied capability.

planned (r94; scribe draft — L1 selects and admits): (1) **depth — an actual myth-content
move**: extend the mythology corpus with real content (candidate scopes for L1: deepen the
delivered clusters' in-world/passage-level material, or land the next sourced family); this
must not be another boundary-doc/tooling repair round — the r93 doc-repair lane is closed
pending only its named debts. (2) **calibration — the C9 watch re-check due r94** (small due
item; keep the ruling unless a source-backed counterexample satisfies all four gates).
(3) optional bounded debt — self-test modes for `support_check.py`/`discriminate_check.py`.
The conditional `patches/Q1-r94-proposal.md` exists but is unselected and predates the
corrective commit; it is not authorization.

saturation: not declared — no rubric exists; the stagnation nudge is not triggered.
retired: unchanged (none retired; the historical duplicate-name rejection remains in force).

SHONEN: box 1 `[ ]` in the file (SKILL.md now exists at `4780cf0` with decision table, error
signatures, checklist, gate registry — but no external non-author verifier, so no `[x]`);
box 2 `[~]`; box 3 `[ ]` in the file, which no longer matches the r89–r92 SCORECARD prose
`[~]` — the R24-recorded mismatch; L1 must re-file the checklist with the correction record
before the 12-round contract is called satisfied; box 4 `[~]`. No `[x]`; no named non-author
verifier this round; no promotion is claimed.

**Scribe limits.** Same-lane re-execution at `4780cf0` with a clean worktree; peer follow-up
reports were not read and no backend echo is asserted; this proposal recommends verdicts and
does not rule them. L1 owns admission; closure remains red until the fresh required follow-up
is received and recorded.
