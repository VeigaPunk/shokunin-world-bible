# JCAL1 — Calibration judge #1 (census + delta classification), round 88 follow-up

Judged tree: **delivered** HEAD `2ea9ef13a928475b13fd578740ea521bed4bd649`, working tree
verified clean (`git status --porcelain` empty) before and after every measurement.
Baseline: `dfd1fbc3711f2b28597d74444819aca91fe6bc31`. Python 3.14.7.
All probes ran under `/tmp/jcal1`; the only repo writes are
`.ufo/waves/round-88/followup/JCAL1.md` and `JCAL1-delta.json`.

**Verdict for calibration: improved.**

## Work performed

1. **Independent baseline regeneration** (not a read of seat-authored artifacts):

   ```text
   git archive dfd1fbc3711f2b28597d74444819aca91fe6bc31 | tar -x -C /tmp/jcal1/base
   ```

   145 fixture dirs extracted; baseline `check_bible.py` md5 `e088ac108b7f1e2dda8f1630d72cc161`
   vs delivered `1e93baa475f628c575f4569200abc799`.

2. **Full census on both trees**, command template run once per directory with the
   repo root as cwd (`PYTHONDONTWRITEBYTECODE=1`):

   ```text
   python3 corpus/fixtures/check_bible.py corpus/fixtures/<dir>
   ```

   Baseline census → `/tmp/jcal1/base-tuples.json`; delivered census →
   `/tmp/jcal1/delivered-tuples.json`; full stdout/stderr captured per dir.

3. **Baseline reproduction check**: my regenerated baseline was compared field-by-field
   (`exit`, `stdout_sha256`, `violation_count`) against
   `.ufo/waves/round-88/patches/B1-tuples.json` — **145/145 entries, 0 mismatches**.
   The diff baseline is therefore trustworthy; no seat-authored tuple artifact was used
   as verdict evidence.

4. **Delta enumeration**: tuple diff delivered vs B1; per-fixture line diff
   (`difflib.SequenceMatcher` on complete stdout) with every changed line classified.

5. **Invariant probes** (controls, run on the delivered tree):
   - disclosure grammar: every line matching
     `^VIOLATION: entities[N].provenance[M]: provenance continuity and tick-order comparisons remain unassessed \(input-structural finding, not sourced-canon\); first stop: <cause> at <origin>$`;
   - per-entity coverage: every provenance record at/after the first stop of its entity
     carries a disclosure, and all disclosures in a group name one origin and one cause;
   - legacy-grammar survivors: lines containing `unassessed` that do not match the new grammar.

6. **Determinism control**: delivered census rerun → 149/149 tuples byte-identical.

7. **Code read**: `corpus/fixtures/check_bible.py:183-303` (the `first_stop` /
   `record_stop_cause` machinery) to check reachability of each first-cause branch and
   to confirm no false-stop path.

## Before → after measurements

### Census

```text
baseline  (dfd1fbc, 145 dirs): exit 0=30  1=115  violation lines=331  stderr_nonempty=0
delivered (2ea9ef1, 149 dirs): exit 0=31  1=118  violation lines=367  stderr_nonempty=0
```

### Delta shape — confirms the claim exactly

| Quantity | Claimed | Observed |
|---|---|---|
| changed dirs | 9 | **9** |
| new dirs | 4 | **4** |
| total dirs | 149 | **149** |
| exit changes | 0 | **0** |
| unchanged tuples | — | 136/145 |
| pre-r87 changed paths | 2 (`r61-*`), both additive | **2, both additive** |

New dirs: `r88-m3-maya-cluster` (exit 0), `r88-mixed-stop` (exit 1, 6),
`r88-nonholder-stop` (exit 1, 4), `r88-shape-ambiguous-armed` (exit 1, 5) — all added
by `2ea9ef1` (`git log --diff-filter=A`). Violation-line arithmetic reconciles:
+21 from the 9 changed, +15 from the 4 new, 331 + 36 = 367.

### Line classification — every changed line of the 9

| Fixture | added | removed | added disclosure | reworded disclosure | field finding | count footer | **OTHER** |
|---|---|---|---|---|---|---|---|
| r61-independent-empty | 2 | 1 | 1 | 0 | 0 | 1 | 0 |
| r61-independent-unavailable | 2 | 1 | 1 | 0 | 0 | 1 | 0 |
| r87-masked-break-from-ambiguous | 4 | 5 | 0 | 3 | 0 | 1 | 0 |
| r87-masked-break-to-ambiguous | 4 | 5 | 0 | 3 | 0 | 1 | 0 |
| r87-probe-entry-shape | 7 | 1 | 6 | 0 | 0 | 1 | 0 |
| r87-probe-multi-invalid | 3 | 4 | 0 | 2 | 0 | 1 | 0 |
| r87-probe-nonitem-kinds | 5 | 4 | 2 | 2 | 0 | 1 | 0 |
| r87-probe-record-and-chain | 18 | 6 | 14 | 3 | 0 | 1 | 0 |
| r87-probe-shape-ambiguous | 4 | 1 | 2 | 0 | 1 | 1 | 0 |
| **totals** | **49** | **28** | **26** | **13** | **1** | **9** | **0** |

Removed lines: 19 legacy disclosure lines + 9 count footers. Removals exceed reworded
records because the retired grammar emitted two lines for the first-stop record
(`at this and all later records…` plus the `first occurred at…` line); the new grammar
emits one line per record.

**Zero OTHER lines** — every added/removed line is a disclosure (added or reworded), the
one field finding, or a count footer.

The single field finding is
`VIOLATION: entities[5].provenance[0].to_holder: ambiguous entity 'dup'` in
`r87-probe-shape-ambiguous`: the shape-invalid record's holder is now checked once the
record arms the stop, so a finding class that the record previously suppressed appears.
This is the intended consequence of "shape-invalid dict records with ambiguous holder
ids arm the stop", not an OTHER.

### C1 sub-claims, verbatim receipts

**(i) arm from shape-invalid dict record.**

```text
baseline  r87-probe-shape-ambiguous  exit 1, 2 findings
  VIOLATION: entities[1].id: duplicate entities id 'dup'
  VIOLATION: entities[5].provenance[0]: expected exactly tick, from_holder, to_holder, source_id
delivered r87-probe-shape-ambiguous  exit 1, 5 findings
  VIOLATION: entities[1].id: duplicate entities id 'dup'
  VIOLATION: entities[5].provenance[0]: expected exactly tick, from_holder, to_holder, source_id
  VIOLATION: entities[5].provenance[0].to_holder: ambiguous entity 'dup'
  VIOLATION: entities[5].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity to_holder 'dup' at entities[5].provenance[0]
  VIOLATION: entities[5].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity to_holder 'dup' at entities[5].provenance[0]
  5 violation(s); no canon changed
```

New durable fixture `r88-shape-ambiguous-armed` pins the **combined same-record cause
summary**:

```text
VIOLATION: entities[4].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (unexpected field set); ambiguous holder identity to_holder 'f1-shape-dup' at entities[4].provenance[0]
```

**(ii) over-attribution removed.** `r87-probe-multi-invalid` before named the ambiguity
for the tail; delivered names the actual first cause (unknown source at `provenance[0]`)
on `[1]` and `[2]`. The new `r88-mixed-stop` pins the discriminating case — a *later*
`to_holder` ambiguity must not become the named cause:

```text
VIOLATION: entities[5].provenance[1].to_holder: ambiguous entity 'f1-mixed-dup'
VIOLATION: entities[5].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (…); first stop: unknown source 'f1-mixed-missing-source' at entities[5].provenance[0]
VIOLATION: entities[5].provenance[2]: provenance continuity and tick-order comparisons remain unassessed (…); first stop: unknown source 'f1-mixed-missing-source' at entities[5].provenance[0]
```

**(iii) non-holder stop causes disclose.** `r88-nonholder-stop` (unknown source, 3
disclosures), `r87-probe-nonitem-kinds` (non-item entity), `r61-independent-empty`
(non-item provenance) and `r61-independent-unavailable` (source table unavailable) all
gained disclosures where the baseline emitted none.

**(iv) qualifier carried and grammar uniform.**

```text
delivered disclosure lines:                        47
lines matching the exact new grammar:              47
legacy-grammar survivors ('unassessed', old shape): 0
stop groups (entity, first-stop index):            17
groups with exactly one origin and one cause:      17
coverage violations (record at/after stop w/o disclosure): 0
```

First-cause taxonomy observed across the delivered tree (13 distinct causes):

```text
11 malformed record (expected object)          6 duplicate item id 'rope'
 5 provenance attached to a non-item entity     4 unknown source 'ghost-source'
 3 ambiguous holder identity from_holder 'dup'  3 ambiguous holder identity to_holder 'dup'
 3 unknown source 'f1-mixed-missing-source'     3 unknown source 'f1-nonholder-missing-source'
 2 ambiguous holder identity from_holder 'vault'
 2 ambiguous holder identity to_holder 'dup', from_holder 'dup'
 2 malformed record (unexpected field set); ambiguous holder identity to_holder 'dup'
 2 malformed record (unexpected field set); ambiguous holder identity to_holder 'f1-shape-dup'
 1 source table unavailable
```

**(v) pre-r87 discipline.** `git ls-tree -d 28706dc:corpus/fixtures` = 133 dirs (r87's
pre-wave state). Exactly two of the nine changed paths are pre-r87:
`r61-independent-empty` and `r61-independent-unavailable`. Both are **pure additions**:
one disclosure line plus a count-footer bump (17→18, 6→7); no other baseline line changed.
The other seven changed paths are all `r87-*` fixtures introduced by r87.

### Control

Delivered census rerun: `149/149` tuples byte-identical; `git status --porcelain` empty
afterwards (the checker writes nothing). `python3 census.py DELIVERED_RERUN …` output
`exit_counts: {0: 31, 1: 118} total_violations: 367` again.

## Findings & named debt

**Finding 1 — six reachable first-cause branches have no fixture.** The delivered
checker can name these causes (`check_bible.py:246,250,254,258,270,285`) but no fixture
in the 149-dir corpus ever produces them as a first stop (0 occurrences each in a grep of
all delivered stdout):

```text
malformed record (invalid tick)
malformed record (invalid from_holder)
malformed record (invalid to_holder)
dangling holder to_holder <id>
dangling holder from_holder <id>
malformed record (invalid source_id)
```

The grammar and the stop semantics are verified, but the *cause content* is only pinned
for the causes the corpus happens to exercise. This is the one place where C1's
"every record at/after ANY stop discloses the actual first cause" is verified by
construction + 13 observed causes rather than exhaustively by fixture.

**Finding 2 — two first-cause branches are unreachable for the first-stop purpose.**
`check_bible.py:293` (record-level `source table unavailable`) is dead for `first_stop`
because the container gate at `:185` already sets it whenever `sources_available` is
false; the `'malformed record'` fallback at `:299` is unreachable because
`record_stop_cause` is assigned on every path where `valid` becomes False. Harmless, but
the code carries paths no input can select. No false-stop path exists: `first_stop` is
set only inside `if not valid:` (`:297-302`), so a clean record can never arm a stop.

**Finding 3 — the two knowledge docs that specify the disclosure contract were not
updated by `2ea9ef1` and now contradict the delivered checker.**

- `corpus/knowledge/holder-assessment-boundary.md` — header still says
  "verified-at: RUNTIME REPLAYED on the delivered tree at `2b48ca7`". Its contract
  item 3 (`:70`) quotes the retired disclosure text
  `…unassessed because ambiguous holder identity {field} {id!r} first occurred at {origin_label}`;
  its contract item 2 (`:63-68`) specifies "exactly one item-level notice per item"
  (`…unassessed at this and all later records because holder identity is ambiguous`),
  which the delivered checker no longer emits anywhere; its decision-table row for a
  dangling holder says "No `ambiguous entity` line or `unassessed` notice is owed",
  though `:258,270` now arm the stop on a dangling holder; and its row "Ambiguity after
  an earlier invalid record" still describes the over-attribution that C1(ii) removed.
- `corpus/knowledge/r87-provenance-chain-decision-table.md` — row 14 (item-level notice),
  row 15 (old grammar as the "C1 after-state"), row 27 (removed notice), row 32
  ("the holder stop is never armed, and the tail is neither reported nor disclosed …
  unchanged by C1" — now false), row 33 ("six findings" for `r87-probe-multi-invalid`;
  delivered is five), row 35 ("per-record disclosures at [1] and [2]" for
  `r87-probe-nonitem-kinds`; delivered is [0],[1],[2]), plus code anchors
  (`:226-230` etc.) that predate the +59/−20 line shift in `check_bible.py`.

  This is documentation-only drift: the delivered checker behaviour is correct and the
  C1 claim is about behaviour, so this does not harm the calibration axis. It is the
  largest named debt the delta exposes.

**Finding 4 — one new field-level line on a shape-invalid record.** See the
`r87-probe-shape-ambiguous` field finding above. Intended by the arm design, but a
record that previously produced only a shape error now also produces a holder finding;
worth an explicit note wherever the shape-invalid boundary is documented.

**Not observed:** no exit flips, no stderr changes, no `OTHER` changed line, no fixture
lost, no new stderr output, no scalar trade anywhere in the delta.

## Handoff

- `lore-shokunin/.ufo/waves/round-88/followup/JCAL1.md` — this report.
- `lore-shokunin/.ufo/waves/round-88/followup/JCAL1-delta.json` — machine-readable
  delta: baseline-reproduction check, census before/after, changed/new path lists,
  per-fixture added/removed lines with their class, disclosure-record sets
  (added / reworded / removed-legacy), first-cause taxonomy, branch coverage,
  doc-contract drift, and the verdict block.
- **Verdict recommendation for calibration: improved.** All three C1 sub-claims
  (arm-from-shape-invalid, first-cause tracking without over-attribution, disclosure for
  non-holder stops) are reproduced on the delivered tree; the qualifier is carried on
  47/47 disclosures; the coverage invariant holds with 0 violations across 17 stop
  groups; the tuple delta is exactly 9 changed + 4 new with 0 exit changes, and all 136
  remaining baseline tuples are byte-identical; the only pre-r87 changes are the two
  additive `r61-*` disclosures.
- **Debt to carry into the record artifacts** (in priority order): (1) doc-contract
  drift in `holder-assessment-boundary.md` and `r87-provenance-chain-decision-table.md`;
  (2) six unexercised first-cause branches; (3) the new field finding on shape-invalid
  records; (4) two unreachable first-cause branches.
- **Not in scope / not verified by this seat:** C2 coverage and C3 depth (other seats);
  the `r88-m3-maya-cluster` fixture was only censused here (exit 0, 0 violations) and
  its content was not judged.
- **Reproduction:** all commands are in `JCAL1-delta.json` → `method`; the census driver
  is `/tmp/jcal1/census.py` (scratch, not tracked).
