# P4 — SHONEN block + proposed round-88 report SHONEN section

Seat: P4 (follow-up wave, world-bible lane). Judged revision: `2ea9ef1`
(`lore r88: C1 stop-cause repair + C2 Maya cluster + C3 inspiration table — work wave`),
tree clean at start of this seat (`git status --short` → empty). Baseline: `dfd1fbc`.
Every measurement below is on the DELIVERED tree at `2ea9ef1`, never on a patch or a
seat report's intent. Scratch used for probes only: `/tmp/p4/`.

## Work performed

- Read the delivered `SHONEN.md` (10 lines; four boxes at `:5`, `:6`, `:8`, `:9`) and
  checked its revision state: `git diff --stat dfd1fbc 2ea9ef1 -- SHONEN.md PROVINCE.md`
  → empty, i.e. both files are byte-unchanged by the round-88 work commit.
- Established the delivered facts each box asserts:
  - box 1 subject (`SKILL.md`), box 2's two pointers (`LOG.md` round-1 section,
    `reports/round-1/baseline-probes.json`) and the LOG clause, box 3's instruction
    surfaces (`corpus/knowledge/holder-assessment-boundary.md`,
    `corpus/knowledge/r87-provenance-chain-decision-table.md`, and the new
    `corpus/knowledge/r88-sourced-inspiration-decision-table.md`), box 4's pointer
    (`PROVINCE.md:3-11`) and the changed-path set.
- Replayed the delivered checker myself: a full 149-directory census (baseline checker
  extracted with `git show dfd1fbc:corpus/fixtures/check_bible.py` vs delivered), the
  three new r88 probe dirs, the new Maya cluster, and the boundary doc's own documented
  five-probe loop.
- Executed the new D1 table's own verification rule (`grep -nF -- '<anchor>' <excerpt>`)
  against the delivered Maya cluster to test whether the table is executable.
- Read the round-87 record (`LOG.md:1699`ff) to decide whether box 2's "logged in LOG.md"
  clause is satisfied at this revision, and `patches/W1-log-r88.proposal.md` for r88's
  own (unlanded) entry.
- Drafted the SHONEN section for the round-88 report below. No tracked file was written;
  this file is the only deliverable.

## Before → after measurements

All commands run from the lane root (`/home/vgpnk/Projects/shokunin/lore-shokunin`).

### Revision / file state

```sh
git rev-parse HEAD                 # 2ea9ef1...  (work commit; tree clean)
git diff --stat dfd1fbc 2ea9ef1 -- SHONEN.md PROVINCE.md   # (empty)
git diff --name-only dfd1fbc 2ea9ef1 -- LOG.md SCORECARD.md # (empty)
test -e SKILL.md && echo PRESENT || echo ABSENT             # ABSENT
git ls-files | grep -Ei 'skill'                             # (no matches)
```

### Census (box 2 end-to-end evidence) — 149 fixture dirs

`/tmp/p4/census.py`: for every immediate `corpus/fixtures/*` dir, run the baseline
checker (`git show dfd1fbc:corpus/fixtures/check_bible.py`) and the delivered checker,
compare `(returncode, stdout, stderr)`:

```text
dirs: 149
changed tuples: 12
  CH r61-independent-empty            rc 1 -> 1 findings 17 -> 18
  CH r61-independent-unavailable      rc 1 -> 1 findings  6 ->  7
  CH r87-masked-break-from-ambiguous  rc 1 -> 1 findings  6 ->  5
  CH r87-masked-break-to-ambiguous    rc 1 -> 1 findings  6 ->  5
  CH r87-probe-entry-shape            rc 1 -> 1 findings  2 ->  8
  CH r87-probe-multi-invalid          rc 1 -> 1 findings  6 ->  5
  CH r87-probe-nonitem-kinds          rc 1 -> 1 findings  8 ->  9
  CH r87-probe-record-and-chain       rc 1 -> 1 findings 34 -> 46
  CH r87-probe-shape-ambiguous        rc 1 -> 1 findings  2 ->  5
  CH r88-mixed-stop                   rc 1 -> 1 findings  6 ->  6
  CH r88-nonholder-stop               rc 1 -> 1 findings  1 ->  4
  CH r88-shape-ambiguous-armed        rc 1 -> 1 findings  2 ->  5
exit pairs: {(1, 1): 118, (0, 0): 31}
totals: baseline (340 findings, {0:31, 1:118}) -> delivered (367 findings, {0:31, 1:118})
```

Fixture-dir count `145 → 149` (+3 new `r88-*-stop`/`-armed` probes and
`r88-m3-maya-cluster`; the Maya cluster is `CLEAN` under both checkers, so it does not
appear in the changed set). 0 exit changes; +27 findings net over the changed set.

Delivered probe outputs (the three stop classes now each carry a first-cause line):

```text
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-mixed-stop   # rc=1, 6 findings
VIOLATION: entities[5].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: unknown source 'f1-mixed-missing-source' at entities[5].provenance[0]
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-nonholder-stop   # rc=1, 4 findings
VIOLATION: entities[3].provenance[0]: ... first stop: unknown source 'f1-nonholder-missing-source' at entities[3].provenance[0]
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-shape-ambiguous-armed   # rc=1, 5 findings
VIOLATION: entities[4].provenance[0]: ... first stop: malformed record (unexpected field set); ambiguous holder identity to_holder 'f1-shape-dup' at entities[4].provenance[0]
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-m3-maya-cluster   # rc=0
CLEAN: schema, citations, relations, timeline; 0 violations
```

### Box 2 — the "logged in LOG.md" clause at the delivered revision

```sh
grep -n "Round 87 — 2026-10-17" LOG.md   # 1699:## Round 87 — 2026-10-17 (calibration repair + coverage cluster; ...)
grep -n "Fleet round 1 — calibration declaration" LOG.md   # 1574
grep -n -i "round 88" LOG.md             # 1906: (only, inside the r87 closure paragraph: "a named process debt for r88's wave design")
ls reports/round-1/baseline-probes.json  # present
```

At `dfd1fbc`/`2ea9ef1` the r87 record exists in `LOG.md` and logs an end-to-end domain
task (C1 checker repair + four fixtures + measurement replay, `LOG.md:1723-1738`). r88's
own entry is **not** appended; it exists only as `patches/W1-log-r88.proposal.md`
(self-labelled "PROPOSAL ONLY … not an append to LOG.md").

### Box 3 — executability of the delivered instruction surfaces

Positive (new this round): the D1 table's own rule executes against the delivered corpus.

```sh
grep -nF -- "He called out" corpus/fixtures/r88-m3-maya-cluster/source-excerpt.md        # 5:> ... He called out “Earth,” and the solid land appeared.
grep -nF -- "solid land appeared" corpus/fixtures/r88-m3-maya-cluster/source-excerpt.md  # 5: (same line)
grep -nF -- "carried the north lantern" corpus/fixtures/r88-m3-maya-cluster/fictional-excerpts.md  # 10:> Tick 9: Aru carried the north lantern at Quiet Rise.
grep -nF -- "held the south bell" corpus/fixtures/r88-m3-maya-cluster/fictional-excerpts.md       # 11:> Tick 9: Evin held the south bell at Salt Court.
```

Both passages and both in-world claim anchors resolve; the delivered ledger carries the
four-column format the table prescribes (`corpus/knowledge/reference-ledger.md`, 4 data
rows including the ETCSL row).

Counter-evidence (unchanged, now stronger): the boundary doc's documented replay no longer
reproduces. Its `Commands` block pastes 5 / 4 / 7 findings for
`r85-masked-ambiguous` / `r85-isolated-ambiguous` / `r85-harbor-repro`; the delivered
checker emits 4 / 3 / 6 with entirely different wording:

```sh
for case in r85-control r85-unique-break-control r85-masked-ambiguous r85-isolated-ambiguous r85-harbor-repro; do
  echo "=== $case ==="; python3 corpus/fixtures/check_bible.py corpus/live/runs/round-85/probe-inputs/"$case"; echo "[rc=$?]"
done
# r85-control CLEAN rc=0; r85-unique-break-control 1 finding rc=1 (unchanged)
# r85-masked-ambiguous   4 findings rc=1  (doc pastes 5)
# r85-isolated-ambiguous 3 findings rc=1  (doc pastes 4)
# r85-harbor-repro       6 findings rc=1  (doc pastes 7)
# delivered line form: "…comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity to_holder 'vault' at entities[3].provenance[1]"
```

The doc's contract text (`holder-assessment-boundary.md:61-75`, `:104-105`) describes an
item-level notice "…unassessed at this and all later records…" plus a per-record
"…first occurred at…" disclosure; neither string appears in any delivered output any more.
Its own decision-table row 5 states the per-record disclosure "names only the
holder-ambiguity origin, not the earlier cause" — exactly the behavior C1 replaced
(`r88-mixed-stop` now names `first stop: unknown source …`).

The r87 provenance decision table has the same problem in its pasted receipts:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-probe-shape-ambiguous
# delivered: 5 findings rc=1, including two "…remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (unexpected field set); ambiguous holder identity to_holder 'dup' …" lines
# r87 table row 32 pastes: "key-set finding only; … zero `unassessed` lines; pre-existing, unchanged by C1"
python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-probe-record-and-chain
# delivered: 46 findings rc=1; r87 table rows 14/15/27 receipts paste a 34-finding output with the retired wording
```

One further wart: the delivered D1 table's row 6 evidence cell still says "D3's patch adds
the ETCSL row" (proposal framing) although the delivered `reference-ledger.md` already
carries that row.

### Box 4 — cross-domain bleed at the delivered revision

```sh
git diff --name-only dfd1fbc 2ea9ef1 | grep -v '^corpus/' | grep -v '^\.ufo/'   # (none)
git diff --name-only dfd1fbc 2ea9ef1 -- l0-questions.md                          # (empty)
git diff --stat dfd1fbc 2ea9ef1 -- PROVINCE.md                                   # (empty)
wc -l PROVINCE.md                                                                # 11 PROVINCE.md
```

Every changed path is under `corpus/` or `.ufo/waves/round-88/`. The new artifacts keep
attribution / rights / AI-training as three separate open questions
(`r88-sourced-inspiration-decision-table.md` rows 1–3; ledger ETCSL row asserts no rights
conclusion), and no game-dev/kotodama surface is touched.

## Findings & named debt

Per-box verdicts at `2ea9ef1` (glyph in the delivered file in parentheses):

- **Box 1 — `SHONEN.md:5` `[ ]` "SKILL.md contains real decision tables, error patterns,
  checklists, cited sources" — unchanged.** `SKILL.md` is still absent (`test -e` →
  ABSENT; `git ls-files | grep -Ei 'skill'` → no matches), so the box's subject does not
  exist and cannot be asserted. The substance lives at other paths and grew this round
  (`corpus/knowledge/r88-sourced-inspiration-decision-table.md`, plus the existing
  decision tables / `2026-10-12-malformed-error-patterns.md` /
  `2026-10-12-lore-consistency-checklist.md`), but not in a `SKILL.md`.
- **Box 2 — `SHONEN.md:6` `[~]` end-to-end task logged in LOG.md — evidence improved this
  round; glyph retained.** Two independent end-to-end artifact sets now exist at the
  delivered revision: the r87 record logged at `LOG.md:1699` (absent at r87's own
  measurement point, so the "logged in LOG.md" clause is satisfied at this tree) and this
  round's 149-dir census + three new stop-class probes + Maya cluster + D1 table. The box's
  evidence pointer is stale (points only at `LOG.md:1574` / round-1); recommend adding
  `LOG.md:1699`. No external promotion verification exists → no `[x]`.
- **Box 3 — `SHONEN.md:8` `[ ]` instructions executable by an agent without oral context —
  unchanged; counter-evidence persists.** The new D1 table is executable and I ran its
  rule successfully against the delivered cluster, but the lane's other two instruction
  surfaces (`holder-assessment-boundary.md`, `r87-provenance-chain-decision-table.md`) paste
  output that no longer reproduces and describe retired strings/behavior. An agent
  following them cold at `2ea9ef1` gets contradictions with no in-file pointer to the r88
  change. Note: the seat block refers to this box as `[~]`; the delivered glyph is `[ ]`.
- **Box 4 — `SHONEN.md:9` `[~]` no cross-domain bleed (PROVINCE.md still accurate) —
  unchanged; evidence strengthened.** Zero changed paths outside `corpus/` and `.ufo/`;
  `PROVINCE.md` byte-unchanged and its `:3-11` pointer still resolves (file is 11 lines).

Named debt carried (all for the integrator / L1, not this seat):

- **No `[x]` and no promotion.** No named non-author verifier has executed the lane's
  instructions cold; dispatched reviewers do not qualify. `SHONEN.md` itself is unchanged
  this round (`git diff --stat dfd1fbc 2ea9ef1 -- SHONEN.md` → empty), so its evidence
  lines (esp. box 2's round-1-only pointer) are stale relative to the delivered tree.
  Editing `SHONEN.md` is a tracked-file write outside this seat's scope — recommendation
  only.
- **Instruction-surface drift (box 3's blocker).** `corpus/knowledge/holder-assessment-boundary.md`
  and `corpus/knowledge/r87-provenance-chain-decision-table.md` were pinned to `2b48ca7`
  and now describe superseded C1 behavior; the D1 table's row 6 still frames the landed
  ETCSL ledger row as a pending patch. Refresh is a knowledge-file write, not authorized
  for P4.
- **r88's LOG entry is unlanded.** Only `patches/W1-log-r88.proposal.md` exists; box 2's
  LOG clause is satisfied only via the r87 entry at this revision.

## Proposed SHONEN section for the round-88 report

Text to be placed in the report's `## SHONEN` section (report copy only — do **not** edit
`SHONEN.md` from this draft). One line per box, in file order:

> `SHONEN.md` is unchanged this round (`git diff --stat dfd1fbc 2ea9ef1 -- SHONEN.md` →
> empty); four boxes at `SHONEN.md:5,6,8,9`. No `[x]` is claimed — no named non-author
> verifier has executed the lane's instructions cold. Drafted by follow-up seat `P4`
> (`followup/P4-shonen.md`).

- `SHONEN.md:5` — `[ ]` *SKILL.md contains real decision tables, error patterns, checklists,
  cited sources* — **unchanged**. No `SKILL.md` exists in the lane (`test -e SKILL.md` →
  ABSENT; `git ls-files | grep -Ei 'skill'` → no matches), so the box's subject does not
  exist to assert. Round 88's decision-table material landed at
  `corpus/knowledge/r88-sourced-inspiration-decision-table.md` (C3), alongside the r87
  provenance table, `2026-10-12-malformed-error-patterns.md`, and
  `2026-10-12-lore-consistency-checklist.md` — not in a `SKILL.md`.
- `SHONEN.md:6` — `[~]` *At least one end-to-end domain task executed and logged in LOG.md*
  — **lane assertion retained; evidence improved this round**. The clause is satisfied at
  the delivered revision by the round-87 record (`LOG.md:1699`, C1 landed + measurements +
  reproduce commands), which was absent when r87's own follow-up measured the box; round 88
  adds a second end-to-end set (149-dir census, `340 → 367` findings, exits
  `{0:31, 1:118}` unchanged, `145 → 149` fixture dirs; three new stop-class probes; the
  Maya cluster; the D1 table). Round 88's own LOG entry is not appended — only
  `patches/W1-log-r88.proposal.md`. Pointers: `LOG.md:1574` (round-1 declaration),
  `LOG.md:1699` (round-87 record), `reports/round-1/baseline-probes.json`.
- `SHONEN.md:8` — `[ ]` *Instructions executable by an agent without oral context* —
  **unchanged; counter-evidence at `2ea9ef1`**. The new
  `corpus/knowledge/r88-sourced-inspiration-decision-table.md` is executable — its
  `grep -nF -- '<anchor>' <excerpt>` rule resolves on the delivered cluster
  (`source-excerpt.md:5`, `fictional-excerpts.md:10-11`), and the delivered ledger carries
  its four-column format. But `corpus/knowledge/holder-assessment-boundary.md` is pinned to
  `2b48ca7` and its own documented replay no longer reproduces: the doc pastes 5/4/7
  findings for `r85-masked-ambiguous`/`r85-isolated-ambiguous`/`r85-harbor-repro` while the
  delivered checker emits 4/3/6 with the retired "…unassessed at this and all later
  records…" / "…first occurred at…" wording gone, and its row 5 states the disclosure "names
  only the holder-ambiguity origin, not the earlier cause" — the behavior C1 replaced.
  `corpus/knowledge/r87-provenance-chain-decision-table.md` row 32 pastes "zero `unassessed`
  lines" for `r87-probe-shape-ambiguous` where the delivered checker emits two. The D1
  table's row 6 also still frames the landed ETCSL ledger row as "D3's patch".
- `SHONEN.md:9` — `[~]` *No cross-domain bleed (PROVINCE.md still accurate)* — lane
  assertion retained; evidence strengthened. `PROVINCE.md` bytes unchanged
  (`git diff --stat dfd1fbc 2ea9ef1 -- PROVINCE.md` → empty; `PROVINCE.md:3-11` still
  resolves, file is 11 lines); every changed path is under `corpus/` or
  `.ufo/waves/round-88/` (`git diff --name-only … | grep -v '^corpus/' | grep -v '^\.ufo/'`
  → none), and `l0-questions.md` is untouched. The new artifacts keep attribution, rights,
  and AI-training as three separate open questions and assert no rights conclusion
  (`r88-sourced-inspiration-decision-table.md` rows 1–3; ledger ETCSL row).

## Handoff

- **Deliverable:** this file, `.ufo/waves/round-88/followup/P4-shonen.md`. No tracked file
  was written; no commit, no push, no registry write, no sibling-repo write.
- **Judged revision:** `2ea9ef1` (baseline `dfd1fbc`), tree clean; scratch `/tmp/p4/`
  (`base_check.py`, `census.py`) is probe-only and not a deliverable.
- **Headline for L1:** at the delivered tree SHONEN.md is unchanged and all four boxes stay
  `[~]`/`[ ]`; box 2's evidence improved (LOG clause now satisfied by `LOG.md:1699` + the
  r88 census/probes); box 3 remains blocked by two knowledge files that now describe
  superseded checker behavior; boxes 1 and 4 are unchanged.
- **Follow-ups worth a seat next round:** refresh `holder-assessment-boundary.md` and
  `r87-provenance-chain-decision-table.md` receipts to the delivered C1 wording, and fix the
  D1 table's row-6 ETCSL framing; the integrator must decide whether the round-88 LOG entry
  (W1 proposal) is appended, which is the only remaining gap between the delivered tree and
  box 2's wording.
- **Block discrepancy noted:** the seat block calls box 3 `[~]`; the delivered
  `SHONEN.md:8` reads `[ ]`. I judged the delivered glyph.
