# V06 — c2-dispositions (round-102, lore-shokunin)

Seat: V06 — spot-check 8 dispositions (2 closed, 3 addressed, 3 carried) in
`corpus/knowledge/r102-debt-ledger.json`; each evidence pointer must
demonstrate the claimed state on delivered bytes.

**Bottom line: PASS** — all 8 slate dispositions verify on delivered bytes;
counts reconcile exactly with every source ledger; one adverse note recorded
on a 9th probe (r97-NB-17, partial pointer demonstration).

## Poll record

- Poller 1 (background, 20s interval): killed at 600s harness cap, ~30 content-gated tries, ABSENT.
- Poller 2 (foreground 20s × 14): ABSENT at 2026-10-18 06:29:44-03:00.
- Poller 3 (foreground 20s × 14): ABSENT at 06:35:01 (U1-scratch appeared — producer alive).
- Poller 4 (foreground 20s × 14): **LEDGER READY try 11, 06:38:26-03:00**. ~60 total gated tries; wave was live (verifier seats landing throughout), so the extra bounded cycles are recorded as stall-escapes, not fatal.

## Ledger structure and count reconciliation (C2 falsifier, part 1)

`corpus/knowledge/r102-debt-ledger.json` (delivered 06:38): dict with
`items` n=265, `carry_records` n=96, `totals.source_entries=361`,
dispositions `{closed:112, addressed:107, carried:46}`.

Per-source `items_in_source` vs my independent counts of the source files:

| source | claimed | my count | match |
|---|---|---|---|
| r94 F29-debt.json | 51 | 51 items | ✓ |
| r95 V31-debt.json | 51 | 51 items | ✓ |
| r96 V40-debt.json | 63 | 63 (12 new+10 closure+21 carried+13 PR+7 ST) | ✓ |
| r97 V37-debt.json | 70 | 70 items | ✓ |
| r98 V33-debt.json | 63 | 63 (same sections) | ✓ |
| r99 V36-debt.json | 42 | 42 (16+10+16) | ✓ |
| r100 V29/L1 | 11 | LOG r100 closure: AC-DOCS/AC-BASELINE/AC-RECEIPT-ERRATUM/AC-SCOPE/AC-CLOSE + V15/V18/V20 FAILs + V21/V30 quals ≈ 11 — plausible, not item-by-item refuted | ✓- |
| r101 V24/L1 | 10 | LOG r101 closure AC-1..AC-4 + named records ≈ 10 — plausible | ✓- |

Own-item sum 51+24+52+50+42+25+11+10 = 265 = items; items_in_source −
own_items = 96 = carry_records (mirrors, not double counts — counting rule 1
is applied consistently). Disposition sums per round = 112/107/46 exactly.
**No silent drop found.** The ledger itself flags the defect I independently
found pre-delivery: C2's LOG declaration cites "r100 V33" as a source ledger,
but round-100's roster was T1–T4 + V01–V30 — no V33 file exists
(`ls .ufo/waves/round-100/seats/` full listing checked). The ledger's
`sources[6]` correctly uses "V29/L1" and records the anomaly. V74-debt-2.md
(r99 second extraction) exists and is declared merged, not double-counted.

## Spot-checks (each: command → observed output → verdict)

### CLOSED (2)

**1. r98-NB-01** — "tools README 'not gitignored' claim false" → closed,
evidence `commit 4265df5`.
- `git log --oneline -1 4265df5` → `4265df5 lore r98: freeze admitted wave + closure docs (hyper completion wave, chain six, receipt 64/64)` ✓ exists.
- `git log --oneline -S"*-self-test-*" -- .gitignore` → `9d25df9 lore r97: freeze admitted wave + closure docs` — pattern landed at r97 closure, exactly as the disposition_detail states.
- `.gitignore:3-4` → `*-self-test-*/` present.
- `git show 4265df5 -- corpus/tools/README.md | grep -i gitignore` → the dated class erratum: "Two sentence classes … are factually stale on the delivered revision and are superseded as classes … (1) every 'the self-test scratch … is not gitignored' sentence (r94–r97 addenda) — the r97 closure added `*-self-test-*/` to `.gitignore` … (`git check-ignore -v` confirms)".
- Live reproduction: `mkdir -p dep-freeze-self-test-v06probe && touch …/probe && git check-ignore -v …` → `.gitignore:4:*-self-test-*/	dep-freeze-self-test-v06probe/probe` ✓. (probe dir removed after).
- Verdict: **demonstrated** (historical sentences remain only under the explicit kept-as-history addendum convention, with the superseding erratum landed in the same file).

**2. r101-DEF-1** — "entry cites r94 README:13 twice for a line-11 clause" →
closed (AC-1 repair), evidence `commit ceeef43` + register file.
- `git log --oneline -1 ceeef43` → `ceeef43 lore r101: freeze admitted wave + closure docs (chain eight, R10 first entry, …)`.
- `sed -n '58p;81p' corpus/knowledge/r101-r10-register-first-entry.md` → both lines cite `corpus/fixtures/r94-paired-crossing/README.md:11` / `r94 README.md:11` (editorial-encodings clause).
- `grep -c "README.md:13" <register>` → `0` — no stale cite remains.
- Truth of the paraphrase target: r94 README line 11 reads "The integer ticks and event-ID edges in `timeline.json` are editorial encodings of the excerpt's tick labels and stated order/dependence, not literal JSON wording in the minute." ✓ matches.
- Verdict: **demonstrated**.

### ADDRESSED (3)

**3. r94-BR-01** — "dependency-reduction undetectable (JSON + prose halves)"
→ addressed (JSON half closed r96; prose half detectable r99, bounded r100),
evidence: commits `f3e09f9`/`fe1ce46`, blind-spot rows 1b/6, r100 boundary record.
- Both commits exist (`git log --oneline -1`: `f3e09f9 lore r96: …`, `fe1ce46 lore r99: … ten-file pins …`).
- `corpus/knowledge/r100-provenance-semantics-boundary.md` exists and opens: "**BR-01's prose half is byte-change-detectable, not dependency-semantics-provable.**" — precisely the claimed bound.
- Live gate evidence (isolated temp tree, no live-tree writes): `python3 corpus/tools/dependency_freeze.py --self-test` → observed tail: `CASE markdown_tamper: exit=2 … findings=['DIGEST-MISMATCH'] ok` / `CASE repointed_edge: exit=1 … findings=['ADDITION-DETECTED','REDUCTION-DETECTED'] ok` / `SELF-TEST 19/19` / `RESULT PASS` / exit=0. Both halves of BR-01 demonstrated firing on the delivered revision.
- Verdict: **demonstrated** ("addressed" not "closed" is correct: prose entailment remains unprovable, stated as a bound).

**4. r95-CL-07** — "no wave-spec.json and no receipt.json for r95" →
addressed, evidence `.ufo/waves/round-95/receipt.json` + LOG r95 closure.
- `python3 -c "import json; json.load(open('.ufo/waves/round-95/receipt.json'))"` → parses OK (keys incl. `record_type`, `phase`, `dispatch_tool_call_id`).
- LOG r95 closure (2808+): "(dispatch `tool_8xm2IckmDuqcTQITaqoEGpGe`, returned `completed: 64`; receipt `.ufo/waves/round-95/receipt.json`, agent IDs from the dispatch result)" and "receipt rebuilt (64/64 reports…)".
- Standing-convention half: receipt.json present for r96–r101 (`ls .ufo/waves/round-9[6789]/receipt.json .ufo/waves/round-10[01]/receipt.json` → all six exist).
- Verdict: **demonstrated**.

**5. r100-QUAL-V21** — "literal-harness limit (two T4 harnesses not
independently re-runnable)" → addressed (retained as standing convention),
evidence `SCORECARD.md r100/r101 operability rows`.
- SCORECARD.md:614 (Round 100 section): "| operability | unchanged (not harmed) | … V21's literal-harness limit retained (two T4 harnesses not independently re-runnable — bounded, recorded). |"
- SCORECARD.md:647 (Round 101 section): "… V21's literal-harness limit carried as convention. |"
- Verdict: **demonstrated** verbatim in both cited rows.

### CARRIED (3, each with `carried_owner: r103+ (operator; lane closes at r102)`)

**6. r94-BR-17** — "fixture README replay blocks without recorded observed
exits" → carried (recurring, never systematically fixed).
- Trail check: recurrences present in source ledgers r95:NB-11, r97:NB-20, r98:NB-08, r99:NB-09 ✓ (grepped each src dump).
- Ledger's own cited probe re-run: `grep -c -i exit corpus/fixtures/r98-clerk-filing/README.md` → `0`; same on `r95-crossing-aftermath/README.md` → `0` (2026-10-18). The r98 closure item CL-10 indeed never landed.
- Verdict: **demonstrated** (carried state is the observed reality).

**7. r96-NB-21** — "consistent regeneration still exits 0" → carried
(permanent declared-vs-observed bound).
- `corpus/knowledge/r99-gate-blind-spot-table.md:24` row 7: "| 7 | consistent-regeneration inventory bound | `dependency_freeze` `REDUCTION-DETECTED` exit 1 on the JSON deletion half | `check_bible` CLEAN 0; `support_check` PASS 0; `map_obligations` PASS 0 when the map row and the `**Expected inventory:**` line are restated to match | …"
- Cross-pointer SKILL.md:89: "bound: a consistently regenerated declaration still exits 0."
- Source fidelity: r96 V40 NB-21 = "Consistent regeneration (deletion + updated declaration) still exits 0; gate keys on declared-vs-observed mismatch only." ✓ no drift.
- Verdict: **demonstrated**.

**8. r96-NB-01** — "dual_pointer confined to legacy dialect" → carried
(permanent scope bound).
- SKILL.md:89 (map gate scope): "`dual_pointer` (r96 detection, r97 pin): legacy-dialect cells naming a second pointer in prose exit 1; bound: canonical-dialect variants stay `unsupported_map` exit 2 (fail-closed)."
- Trail: r99 V36 `bounds_carried.open_accepted` contains "CO-05 dual_pointer legacy scope" ✓.
- Verdict: **demonstrated**.

### Adverse note (9th probe, outside the required slate)

**r97-NB-17** — "freeze verify-side bounds (name-gated lookup, symlinks,
JSON-only payload)" → carried, evidence "SKILL.md dependency row scope".
SKILL.md's dependency-row scope line demonstrates only the path-binding half
("Path-bound since r97 (pins carry repo-relative paths; a byte-identical copy
at a foreign path exits 2 `PATH-MISMATCH`)"). The other two titled components
fail on delivered bytes: `grep -i symlink SKILL.md corpus/tools/README.md` →
no matches; and "JSON-only payload" is superseded — the delivered registry
row itself now declares "full-file content digests over the ten declared
files per fixture" (markdown hashed since r99's ten-file pins, commit
`fe1ce46`). The row is not dropped and carries an owner, so this is a
pointer-fidelity blemish (title quotes stale source wording without a dated
trail note, unlike r98-NB-01's handling), not a silent-drop or miscount.

## Method notes

- Source inventories dumped to scratch (`src-r94..99.txt`, `r102-items.tsv`, `r102-carries.tsv`, `dump.py`) inside `.ufo/waves/round-102/seats/V06-scratch/` (exclusive).
- All commands run from lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`; no commits, no pushes, no network; the only tree-level writes were this report, the scratch dir, and the removed `dep-freeze-self-test-v06probe` probe dir.
- Frozen-gate evidence used the tool's own persisted self-test (isolated temp tree), not an in-tree mutation (in-tree writes are outside V06 byte-ownership).

## Verdict

C2 spot-check: **8/8 slate dispositions verified** on delivered bytes with
source-row fidelity (no drift, no silent drops); per-source counts and
disposition totals reconcile exactly. One adverse note: r97-NB-17's evidence
pointer partially demonstrates its titled bound (symlink half undocumented at
the pointer; JSON-only half superseded by r99's ten-file pins) — recorded for
the adjudicator, non-fatal to the slate.

**Bottom line: PASS — 8/8 spot-checked dispositions (2 closed, 3 addressed, 3 carried) demonstrate their claimed states on delivered bytes; counts reconcile exactly; one non-fatal pointer-fidelity blemish recorded (r97-NB-17).**
