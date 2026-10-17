# JCAL1 — Calibration judge #1 (census + delta classification)

Seat mission: rerun the full 160-directory census at the delivered tree; diff against
`.ufo/waves/round-89/patches/B1-tuples.json` (the 149-directory baseline at `51b286b`);
confirm exactly 4 changed + 11 new; classify every changed line
(combined-summary / qualification / FN-1 wording / footer / OTHER); confirm zero exit flips;
name the 4. Deliver `followup/JCAL1.md` + `followup/JCAL1-delta.json`.

Judged tree: `1b09f3f` (work commit; baseline `51b286b`). Repo writes limited to this
seat's two `followup/` artifacts; all scratch, probe fixtures and captures under
`/tmp/lore-r89-JCAL1/`. Sibling repos untouched. No commit/push performed.

## Work performed

- Verified the judged revision: `git rev-parse HEAD` → `1b09f3ff8016b26a2259e086f673d0112f4f54e5`;
  `git status --porcelain` → empty (tree clean at start; the only untracked path on the
  tree is the concurrent `followup/` directory written by this wave's seats).
- Re-derived the baseline independently instead of trusting the artifact: extracted
  `51b286b` with `git archive` into `/tmp/lore-r89-JCAL1/base` (read-only on the repo) and
  ran the checker there. The replay reproduced `patches/B1-tuples.json` exactly
  (149 keys, 0 tuple mismatches), so the baseline reference is sound.
- Ran the full census on the delivered tree over the scope "every direct child of
  `corpus/fixtures/` holding at least one of `contradictions.json`, `entities.json`,
  `relations.json`, `sources.json`, `timeline.json`" — 160 of 160 directories qualify
  (no directory is out of scope, so scope filter is a no-op this round).
- Diffed tuples and per-line stdout (difflib opcodes over the full stdout of each of the
  149 common directories) and classified every added line.
- Built two scratch control fixtures under `/tmp` to probe properties the delivered
  fixtures cannot demonstrate: a 4-simultaneous-cause valid-key record (completeness of
  the combined summary) and a raw-present-but-unindexed holder (the unexercised FN-1
  branch).
- Re-applied `patches/X1-c1.patch` to the baseline checker in scratch and diffed against
  the delivered file.

## Before → after measurements

Checker command, run from the repository root for every directory:

```text
python3 corpus/fixtures/check_bible.py corpus/fixtures/<dir>
```

**1. Census (delivered tree, `1b09f3f`).** Command: `python3 /tmp/lore-r89-JCAL1/census.py`

```text
dirs: 160
exit_counts: {1: 128, 0: 32}
total_violations: 399
stderr_nonempty: 0
```

**2. Baseline replay (`51b286b`, scratch archive).** Command: `python3 /tmp/lore-r89-JCAL1/census_base.py`

```text
BASELINE dirs: 149 exits: {1: 118, 0: 31} violations: 367 stderr_nonempty: 0
B1 artifact dirs: 149
B1-vs-replay key sets equal: True
B1-vs-replay tuple mismatches: 0 []
```

**3. Delta (delivered vs baseline).** Command: `python3 /tmp/lore-r89-JCAL1/diffcheck.py`

```text
baseline dirs: 149 head dirs: 160
added: 11 removed: 0 common: 149
changed tuples: 4 unchanged tuples: 145
exit_status_changes: 0 []
```

Confirmed as requested: **exactly 4 changed + 11 new, 0 removed, 0 exit flips.**

**4. The 4 changed directories** (all four are pre-existing baseline dirs; violation-line
counts unchanged, only the disclosure text moved):

| directory | exit before → after | violations before → after |
|---|---|---|
| `corpus/fixtures/r87-probe-multi-invalid` | 1 → 1 | 5 → 5 |
| `corpus/fixtures/r87-probe-record-and-chain` | 1 → 1 | 46 → 46 |
| `corpus/fixtures/r88-mixed-stop` | 1 → 1 | 6 → 6 |
| `corpus/fixtures/r88-nonholder-stop` | 1 → 1 | 4 → 4 |

**5. Every changed line classified.** Command: the bucket pass in
`/tmp/lore-r89-JCAL1/diffcheck.py` (opcode-level diff of complete stdout, 149 common dirs).

```text
changed-line buckets: {'combined-summary': 2, 'qualification': 0, 'FN-1 wording': 10, 'footer': 0, 'OTHER': 0} total: 12
per-dir: {'r87-probe-multi-invalid': 2, 'r87-probe-record-and-chain': 4, 'r88-mixed-stop': 3, 'r88-nonholder-stop': 3}
```

All 12 changed lines are `first stop:` disclosure lines. None is a finding line, a footer,
or a new/removed finding.

- **combined-summary (2 lines, `r87-probe-multi-invalid`)** — a second latching cause is
  now joined to the first with `'; '`:

  ```text
  VIOLATION: entities[5].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity from_holder 'vault'; source reference 'ghost-source' absent from raw sources and absent from the resolved index at entities[5].provenance[1]
  VIOLATION: entities[5].provenance[2]: ... first stop: ambiguous holder identity from_holder 'vault'; source reference 'ghost-source' absent from raw sources and absent from the resolved index at entities[5].provenance[1]
  ```

- **FN-1 wording (10 lines)** — the same three fixtures' single-cause source-reference
  disclosures, e.g. `r88-nonholder-stop`:

  ```text
  before: ... first stop: unknown source 'f1-nonholder-missing-source' at entities[3].provenance[0]
  after:  ... first stop: source reference 'f1-nonholder-missing-source' absent from raw sources and absent from the resolved index at entities[3].provenance[0]
  ```

- **qualification (0 lines on the 149-dir manifest), footer (0), OTHER (0).**

**6. Footer / clean-line and stderr invariance across all 160.** Command: the invariance
pass in `diffcheck.py`.

```text
footer/clean anomalies across 160: 0 []
stderr nonempty across 160: 0
```

Every exit-1 directory ends with the exact `N violation(s); no canon changed` footer, and
the single exit-0 directory (`r89-inspiration-paraphrase`) prints the exact
`CLEAN: schema, citations, relations, timeline; 0 violations` line.

**7. Violation-line arithmetic closes exactly.**

```text
baseline violations: 367 head: 399 growth: 32
new-dir violations: 32
changed-dir net delta: 0
exit counts base: {0: 31, 1: 118}  head: {0: 32, 1: 128}
new exit-1: 10 new exit-0: 1
```

All growth is attributable to the 11 new directories; the 4 changed directories contribute
net zero violation lines. Exit-count deltas (+10 exit-1, +1 exit-0) are exactly the new
directories' exits.

**8. Replay determinism.** Command: `python3 /tmp/lore-r89-JCAL1/census.py` re-run.

```text
REPLAY_DETERMINISM: dirs=160, identical=True
```

**9. Checker change is byte-reproducible from the archived patch.** Command:

```text
mkdir -p /tmp/lore-r89-JCAL1/patchcheck2/corpus/fixtures
cp /tmp/lore-r89-JCAL1/base/corpus/fixtures/check_bible.py /tmp/lore-r89-JCAL1/patchcheck2/corpus/fixtures/
cd /tmp/lore-r89-JCAL1/patchcheck2 && patch -p1 < .../patches/X1-c1.patch
diff corpus/fixtures/check_bible.py <delivered>/corpus/fixtures/check_bible.py
```

```text
IDENTICAL
```

(The delivered checker is exactly `51b286b` + `X1-c1.patch`; independently corroborates
seat V2's freeze check.)

**10. Scratch controls (probes only, no repo writes).**

Combined-summary completeness — a valid-key record with four simultaneous latching
defects (invalid tick, invalid `to_holder`, ambiguous `from_holder`, invalid `source_id`),
run against the delivered checker:

```text
VIOLATION: entities[2].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (invalid tick); malformed record (invalid to_holder); ambiguous holder identity from_holder 'dup'; malformed record (invalid source_id) at entities[2].provenance[0]
```

All four causes appear, in validation order, none dropped. The summary fires only on the
expected-key-set path (`check_bible.py:316`), matching the E1 "valid-key" scoping.

FN-1 second branch — a raw entity row present but schema-invalid (so absent from the
resolved index):

```text
VIOLATION: entities[1].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: holder reference to_holder 'ghost' present in raw entities but absent from the resolved index at entities[1].provenance[0]
```

The branch renders correctly, but see the debt below.

## Findings & named debt

- **Delta is fully enumerable and matches the claim: 4 changed + 11 new of 160, 0 exit
  flips, 145 unchanged tuples.** Every changed line is inside a `first stop:` disclosure;
  no finding was gained, lost, or reordered (per-directory violation counts are identical
  before/after, and the footer and CLEAN strings are invariant across all 160).
- **The combined-summary mechanism is only partly new.** Two unchanged baseline
  directories (`r87-probe-shape-ambiguous`, `r88-shape-ambiguous-armed`) already emitted a
  `'; '`-joined first stop from the *unexpected-field-set* branch
  (`malformed record (unexpected field set); ambiguous holder identity ...`). What C1 adds
  is the *valid-key* branch (`check_bible.py:316`). Any claim of "new combined summary"
  should be scoped to the valid-key path.
- **Named debt — FN-1's second branch is unexercised by delivered fixtures.** The string
  `present in raw` occurs **0 times** across all 160 delivered directories
  (`grep -R -F -- 'present in raw' /tmp/lore-r89-JCAL1/delivered-output | wc -l` → `0`).
  Every delivered fixture that hits FN-1 has the id genuinely absent from raw. The
  raw-present-but-unindexed rendering is therefore demonstrated only by this seat's
  scratch probe, not by durable delivered evidence. Half the FN-1 wording change has no
  fixture.
- **Named debt — FN-2 is invisible to the baseline manifest.** `grep -R -F -- 'not
  uniquely resolvable' delivered-output` matches exactly one file
  (`r89-fn2-unresolved-chain-break`), and the qualification wording produces **0** line
  changes on the 149 common directories. Re-running the 149-dir manifest cannot detect a
  regression in the FN-2 clause; only the two new `r89-fn2-*` fixtures can. Gating is
  nonetheless correct: the control (`r89-fn2-control`, one valid raw row) still emits the
  unqualified `provenance chain break; expected from_holder 'f3-dup', got 'mira'`, while
  the unresolved fixture (2 raw rows, 1 indexed) emits the qualified clause — so the
  qualification does not over-claim on the control.
- **Wording mismatch with the seat brief, not with the tree.** The brief quotes the FN-1
  phrase as `absent from the raw table and resolved index`; that exact string occurs
  nowhere in the tree (`grep -rn -F -- 'absent from the raw table' corpus/ .ufo/waves/round-89/`
  → no matches). The delivered form is `absent from raw sources and absent from the
  resolved index` (sources) / `absent from raw entities and absent from the resolved index`
  (holders), which matches the authoritative spec `patches/E1-r89-wording.md` verbatim.
  Recommend judging the FN-1 wording against the E1 spec, not the brief's paraphrase.
- **Minor provenance asymmetry.** 8 cause-branch fixtures are delivered (5 `r89-c1-*`,
  3 `r89-f2-*`). Seven are captured by patch artifacts (`F1-cause-fixtures.patch` covers
  4 of the 5 C1 dirs, `F2-cause-fixtures.patch` covers the 3 F2 dirs); the fifth C1 dir,
  `r89-c1-malformed-source-id`, has no patch artifact — its README records that it was
  authored directly by the L1 integrator to close X1's named debt, and it is referenced by
  `followup/H2-delta.json` and `followup/V2.md`. So it is documented, just not
  patch-docked. Not a correctness defect; a traceability gap if the wave's patches are
  treated as the complete change set.
- No trade was found: exit codes, violation counts, footers, CLEAN line and stderr are all
  invariant; the only changes are added accuracy inside existing disclosure lines.

## Verdict recommendation

**Calibration: improved.** The two delivered cause-text changes replace a
mis-description (labelling a raw-present id as `unknown`/`dangling`) with an accurate
two-sided lookup result, and complete the valid-key first-stop disclosure — with no
regression on any of the 149 baseline directories (0 exit flips, 0 violation-count
changes, 0 footer/stderr changes) and with the checker change byte-reproducible from the
archived patch. The improvement is bounded and should be recorded with the named debt
above: FN-1's raw-present branch and the FN-2 qualification are each supported by at most
one durable fixture, and FN-2 is entirely invisible to the 149-dir manifest.

## Handoff

- `lore-shokunin/.ufo/waves/round-89/followup/JCAL1.md` — this report.
- `lore-shokunin/.ufo/waves/round-89/followup/JCAL1-delta.json` — machine-readable delta:
  baseline/candidate commits, census counts, the 11 added and 4 changed directories, the
  12 changed lines with per-line category, exit-flip list, and the bucket totals.
- Scratch evidence retained under `/tmp/lore-r89-JCAL1/`: `census.py`, `census_base.py`,
  `diffcheck.py`, `head-tuples.json`, `head-raw.json`, `base-tuples.json`, `base-raw.json`,
  `delta-raw.json`, `delivered-output/` (160 stdout captures), `base/` (51b286b archive),
  `patchcheck2/` (X1 patch replay), `probe-4cause/`, `probe-rawpresent/`.
- No tracked file outside this seat's two `followup/` artifacts was written; no
  commit/push was performed.
