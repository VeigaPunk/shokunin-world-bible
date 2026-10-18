# JDEP4 — Depth judge #4: checker-semantics drift check (round 88 follow-up)

Judged tree: `2ea9ef13a928475b13fd578740ea521bed4bd649` (`2ea9ef1`), baseline `dfd1fbc`.
Delivered checker: `corpus/fixtures/check_bible.py`, SHA-256
`dcacffd6981e1af5f60b31bed20c6eccce25970444088e4ee2e30e3249411911`, 395 lines
(r87 snapshot was `3ae4134d…`, 356 lines). All commands run from the lane root
`/home/vgpnk/Projects/shokunin/lore-shokunin`. No tracked file was written; the
only writes are this file and `JDEP4-drift.json` in `followup/`.

**Axis verdict — depth: harmed** (bounded; scope = checker-semantics fidelity of
the `corpus/knowledge` doc set). The r88 C1 commit replaced the checker's entire
disclosure family and did not update the two knowledge docs that are the fleet's
behavioral reference for the provenance branch. Both docs still present the
superseded r87 wording as current delivered behavior. Gain on the same axis
(the new `r88-sourced-inspiration-decision-table.md`) is named under Findings and
is not netted against the harm — a trade is not an improvement.

## Work performed

1. Confirmed the delivered tree and clean status (`git log --oneline -3`,
   `git status --porcelain`).
2. Diffed the checker between baseline and delivered
   (`git diff dfd1fbc 2ea9ef1 -- corpus/fixtures/check_bible.py`, +59/−20) and
   read the delivered provenance block in full (`:180–312`).
3. Replayed the five recorded r85 probes and the two r87 direction fixtures on
   the delivered checker.
4. Swept the whole repo for the two superseded r87 disclosure strings and the
   new r88 template (grep over `*.md|*.py|*.json`, `.git` excluded), separating
   tracked corpus docs from historical wave evidence.
5. Verified the D1 table's OBS-1 row and its closing checker paragraph claim by
   claim against the delivered checker and the delivered `r87-myth-cluster`.
6. Re-measured the boundary doc's fixture census (provenance-bearing dirs) and
   helper existence at `2ea9ef1`.

## Before → after measurements

### The r88 disclosure family (the drift root)

Delivered checker, `:192–194` and `:198–200`:

```python
def report_unassessed(record_label):
    cause, origin_label = first_stop
    errors.append(f'{record_label}: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: {cause} at {origin_label}')
...
disclosure_emitted = first_stop is not None
if disclosure_emitted:
    report_unassessed(record_label)
```

One template, emitted for **every** record at/after the stop. The r87 design's
two strings are gone:

```sh
grep -c "unassessed at this and all later records because holder identity is ambiguous" corpus/fixtures/check_bible.py   # 0
grep -c "unassessed because ambiguous holder identity" corpus/fixtures/check_bible.py                                   # 0
```

`first_stop` is now armed by the *first* stopping condition in document order
(`:183–189`, `:205`, `:227–232`, `:298–301`), from a cause set that now includes
non-holder causes: `source table unavailable`, `provenance attached to a
non-item entity`, `duplicate item id {id!r}`, four `malformed record (…)` forms,
`malformed record (unexpected field set); ambiguous holder identity {cause}`,
`dangling holder to_holder/from_holder {id!r}`, `unknown source {id!r}`, and
`ambiguous holder identity {cause}`. The r87 `can_check_chain` latch is gone;
the gate is `if first_stop is None:` at `:303`.

### Probe replay — counts changed, not only wording

```sh
for case in r85-control r85-unique-break-control r85-masked-ambiguous r85-isolated-ambiguous r85-harbor-repro; do
  echo "=== $case ==="; python3 corpus/fixtures/check_bible.py corpus/live/runs/round-85/probe-inputs/"$case"; echo "[rc=$?]"
done
```

| case | baseline `5eb9451` | r87 `2b48ca7` | delivered `2ea9ef1` |
|---|---|---|---|
| r85-control | 0 (`CLEAN`) | 0 (`CLEAN`) | 0 (`CLEAN`) |
| r85-unique-break-control | 1 | 1 | 1 (identical line) |
| r85-masked-ambiguous | 1 | 5 | **4** |
| r85-isolated-ambiguous | 1 | 4 | **3** |
| r85-harbor-repro | 2 | 7 | **6** |

Delivered `r85-masked-ambiguous` output (verbatim, rc=1):

```text
VIOLATION: entities[5].id: duplicate entities id 'vault'
VIOLATION: entities[3].provenance[1].to_holder: ambiguous entity 'vault'
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity to_holder 'vault' at entities[3].provenance[1]
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity to_holder 'vault' at entities[3].provenance[1]
4 violation(s); no canon changed
```

The two r87 direction fixtures also drop 6 → 5:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-masked-break-to-ambiguous    # 5 violation(s), rc=1
python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-masked-break-from-ambiguous  # 5 violation(s), rc=1
```

New behavior confirmed on the three r88 fixtures:

- `r88-shape-ambiguous-armed` → 5 findings; the shape-invalid dict record now
  arms the stop: `first stop: malformed record (unexpected field set); ambiguous
  holder identity to_holder 'f1-shape-dup' at entities[4].provenance[0]`, and
  the tail `[1]` is disclosed.
- `r88-mixed-stop` → 6 findings; the disclosure names the **earlier non-holder**
  cause: `first stop: unknown source 'f1-mixed-missing-source' at
  entities[5].provenance[0]`, while `[1]` still gets its own
  `ambiguous entity 'f1-mixed-dup'` line.
- `r88-nonholder-stop` → 4 findings; an unknown-source-only item discloses.

A live counterexample to the superseded "suppression is silent" claim:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r61-independent-unavailable
```

```text
VIOLATION: entities[0].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: source table unavailable at entities[0].provenance
```

`r61-independent-empty` likewise emits `first stop: provenance attached to a
non-item entity at entities[0].provenance`.

### D1 table's OBS-1 row and closing paragraph — claim-by-claim

Source: `corpus/knowledge/r88-sourced-inspiration-decision-table.md` (row 5,
"An in-world claim is attributed to a delivered excerpt"; closing paragraph).

| claim | verdict at `2ea9ef1` |
|---|---|
| "the structural checker still returns `CLEAN`" for the Gate-attributed hymn | **verified true**: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster` → `CLEAN: schema, citations, relations, timeline; 0 violations`, rc=0 |
| "`corpus/fixtures/check_bible.py` … does not read inspiration notes, excerpts, or symbolism maps" | **verified true**: the loader reads exactly `directory / (section + '.json')` for `sources, entities, relations, timeline, contradictions` (`:41–45`); no `.md` path is constructed or opened anywhere in the file |
| "validates JSON structure, source-ID resolution, relations, and timeline rules" | **understated, not false**: it also validates the contradictions ledger (`:112–143`), `allied_with` reciprocity, and timeline occupancy/double-booking |
| "The r87 replay returned `CLEAN: schema, citations, relations, timeline; 0 violations` while OBS-1 remained undetected" | **verified true**, and the CLEAN string is an exact byte match to the delivered checker's clean line (`:395`) |
| "r87's `entities.json:33` attributes a Gate claim to a hymn with no matching place/threshold terms" | **stale present tense**: the line is the same at `2ea9ef1`, but the excerpt was repaired by M4, so the defect no longer exists. Measured: `lowwater-hymn-excerpt.md` now has `Mother-Tide:1, gate:1` (was 0/0 at `dfd1fbc`); `threshold:0, shore:0, basin:0, vow:0` unchanged. |

The row's own column is "r87 / round-88 evidence", and it does name "M4's
excerpt patch adds the Gate and matches 8/8 map clauses", so the sequence is
recoverable — but the leading clause reads as a live defect on the delivered
tree when OBS-1 is in fact **repaired at `2ea9ef1`**. This is a tense/scoping
defect in the D1 row, not a checker-semantics error: every behavioral claim it
makes about the checker is correct.

### The two drifted docs — precise inventory

```sh
grep -rn "unassessed at this and all later records because holder identity is ambiguous" --include='*.md' . | grep -v '^./.git/'
grep -rn "unassessed because ambiguous holder identity" --include='*.md' . | grep -v '^./.git/'
```

Excluding historical `.ufo/waves/**`, `reports/round-1/**` and `LOG.md` (all
append-only historical evidence), the dead strings survive only in two tracked
corpus docs:

| doc | dead-notice hits | dead-disclosure hits | last modified |
|---|---|---|---|
| `corpus/knowledge/holder-assessment-boundary.md` | 5 | 8 | `dfd1fbc` (r87) |
| `corpus/knowledge/r87-provenance-chain-decision-table.md` | 9 | 16 | `dfd1fbc` (r87) |

The seat block predicted the boundary doc. The **second drifted doc was not
predicted** and is the more load-bearing one: it is the r87 C2 decision table,
the fleet's row-by-row reference for the whole provenance branch.

#### `corpus/knowledge/holder-assessment-boundary.md`

Its own `recheck:` line reads "Re-verify whenever the provenance branch of
`corpus/fixtures/check_bible.py` changes, either notice string or format
changes" — the r88 commit changed both, so the trigger fired and was not
honored. Drift items:

1. `:54` "The delivered checker (`2b48ca7`) adds disclosure only" — `2b48ca7` is
   no longer the delivered tree, and the behavior it introduces is gone.
2. `:62–66` contract item 2, item-level notice `…unassessed at this and all
   later records because holder identity is ambiguous` — string absent from the
   delivered checker. There is no separate item-level notice; the origin record
   gets the same per-record template as later records.
3. `:67–72` contract item 3, per-record disclosure `…unassessed because
   ambiguous holder identity {field} {id!r} first occurred at {origin_label}` —
   string absent; replaced by the `remain unassessed (…) first stop:` template.
4. `:104` decision-table row "Ambiguous holder, either field" — describes the
   two-form output and cites "4 findings vs 5"; delivered counts are masked 4 /
   isolated 3.
5. `:105` decision-table row "Ambiguity after an earlier invalid record" — states
   "the per-record disclosure names only the holder-ambiguity origin, not the
   earlier cause". **Inverted at `2ea9ef1`**: naming the earlier cause is exactly
   the C1 first-stop fix (receipt: `r88-mixed-stop` → `first stop: unknown source
   'f1-mixed-missing-source' at entities[5].provenance[0]` while the ambiguity
   sits at `[1]`).
6. `:106` row "Later valid records in an item whose chain is already unassessed" —
   "PLUS the per-record disclosure on each of them" carries the dead wording.
7. `:145` "delivered latch `:260-263`, gate `:264-271`" — stale refs; the
   `can_check_chain` latch no longer exists, the gate is `if first_stop is None:`
   at `:303`, and the no-resume previous-value update is `:311–312`.
8. `:146` "Two notice forms, one boundary" — now one form.
9. `:164–168` "Chain eligibility upstream of this contract is unchanged (baseline
   `:183`; delivered `:183`)" — `:183–189` now arms `first_stop` instead of
   computing `can_check_chain`. The sub-claim "the disclosures are NOT gated by
   it" remains true.
10. `:188–224` Commands block, the pasted five-probe output — wrong at
    `2ea9ef1` (masked 5→4, isolated 4→3, harbor 7→6, and every `unassessed` line
    text differs). `r85-control` and `r85-unique-break-control` still match.
11. `:225–226` "1 → 5 … 1 → 4 … 2 → 7" — now 1 → 4, 1 → 3, 2 → 6.
12. `:228–231` "the two in-tree direction fixtures added by C1 … gives
    `6 violation(s)`" — now 5, with dead wording quoted.
13. `:261–267` "Checker at delivered `2b48ca7` (…, 356 lines)" — delivered is 395
    lines, SHA `dcacffd6…`; every line ref in that bullet is stale.
14. `:316–318` "UNKNOWN / UNMEASURED: whether any in-tree fixture outside the r85
    probes and the four `r87-masked-*`/`r87-chain-*` additions combines
    `provenance` with a duplicated holder id. Measured at `2b48ca7`: of the nine
    fixture directories containing `provenance`, none does" — **now resolved and
    the count is wrong**: 19 fixture dirs contain `provenance` at `2ea9ef1`, and
    8 of them combine it with a duplicated holder id (`r87-masked-break-from-ambiguous`,
    `r87-masked-break-to-ambiguous`, `r87-probe-multi-invalid`,
    `r87-probe-nonitem-kinds`, `r87-probe-record-and-chain`,
    `r87-probe-shape-ambiguous`, `r88-mixed-stop`, `r88-shape-ambiguous-armed`).
    The sub-claim "`r61-*` are dangling holders" still holds.
15. `:18–19` `verified-at:` and the doc's whole present-tense framing point at
    `2b48ca7` as "the delivered tree" — two commits stale.

Still **correct** at `2ea9ef1` (not drift, recorded to bound the repair):
`:33–35` the helper `corpus/fixtures/measure_holder_disclosure.py` is still
absent (`ls` → `No such file or directory`); item 1's local
`{record_label}.{field}: ambiguous entity {id!r}` line still fires for both
fields (now also on shape-invalid records, `:218`); "the disclosure repeats the
ORIGIN cause on every later record" is still true and now generalized; "emitted
at the top of the record loop, so it also appears on later records that are not
objects or lack the required keys" is still true (`:198–200` precedes the
`isinstance` check at `:201`); "emission does not depend on chain eligibility"
is still true and broader; relation-endpoint ambiguity precedent is still `:168`.

#### `corpus/knowledge/r87-provenance-chain-decision-table.md` (unpredicted)

Snapshot header `:3–5` pins `2b48ca7` / checker SHA `3ae4134d…`, and `:23–25`
states the table supersedes the pre-C1 draft — but nothing marks the table
itself as superseded, and it is still the live row-by-row reference. Drift items:

- Row 14 (`:54`) "First ambiguous-holder record emits exactly one item-level
  notice", signature `…unassessed at this and all later records because holder
  identity is ambiguous` — **removed**; there is no item-level notice.
- Row 15 (`:55`) "**C1 after-state:** every record at/after the stop carries a
  per-record disclosure", signature `…unassessed because ambiguous holder
  identity to_holder 'dup', from_holder 'dup' first occurred at …` — the
  every-record property survives, the signature does not.
- Row 27 (`:93`) "Ambiguity notice/disclosure after an earlier invalid record",
  receipts quoting both dead strings — the mechanism changed; the earlier cause
  is now named.
- Row 32 (`:97`) "Shape-invalid record carrying the ambiguous holder id … key-set
  finding only; the holder stop is never armed, and the tail is neither reported
  nor disclosed … pre-existing, unchanged by C1" — **false at `2ea9ef1`**:
  `r88-shape-ambiguous-armed` shows the shape-invalid record arming the stop and
  the tail disclosed. This is the C1-intended change the row predates.
- Row 35 (`:100`) "Non-item entity carrying an ambiguous holder … the disclosure
  family fires even though the chain was never eligible" — conclusion survives,
  wording/anchors do not.
- Receipts block (`:120–284`) pastes the dead r87 outputs for
  `r87-masked-break-{to,from}-ambiguous`, `r87-probe-record-and-chain`,
  `r85-masked-ambiguous`, `r87-probe-multi-invalid`, `r87-probe-nonitem-kinds` —
  every one of those replays now differs.
- `:113–115` "If `sources.json` cannot be loaded, every provenance comparison is
  suppressed for the whole run with no notice or disclosure of any kind — the
  `unassessed` disclosure family exists only for holder ambiguity" — **false**:
  `r61-independent-unavailable` now emits `first stop: source table unavailable
  at entities[0].provenance`.

## Findings & named debt

**F1 — depth harmed (primary).** The r88 C1 commit is a semantic replacement of
the checker's disclosure family with no accompanying knowledge-doc update. Two
tracked docs in `corpus/knowledge/` describe the superseded r87 wording as
current delivered behavior: `holder-assessment-boundary.md` and
`r87-provenance-chain-decision-table.md`. Both carry explicit recheck triggers
keyed to the provenance branch / notice strings, and both triggers fired at
`2ea9ef1`. Row-level inventory above; I did not edit either file (seat block:
"do NOT edit it" for the boundary doc, and the sibling `r87-…` doc is outside
the drift-check scope it named).

**F2 — the unpredicted doc.** The seat block expected only the boundary doc. The
r87 provenance-chain decision table is the larger carrier (9 + 16 dead-string
occurrences vs 5 + 8) and is the row-by-row reference. Any repair plan that
touches only the boundary doc leaves the decision table wrong.

**F3 — D1 OBS-1 row staleness (minor, non-checker).** The OBS-1 row's leading
clause reads as a live defect; OBS-1 is repaired at `2ea9ef1`. Every behavioral
claim the row makes about the checker is correct, so this is a tense/scoping
defect, not a semantics error.

**F4 — D1 closing paragraph understatement (minor).** "validates JSON structure,
source-ID resolution, relations, and timeline rules" omits contradictions,
`allied_with` reciprocity, and timeline occupancy. Not false; the load-bearing
claim ("does not read inspiration notes, excerpts, or symbolism maps") is
verified true.

**F5 — the boundary doc's fixture census is now wrong, not merely stale.** It
states nine provenance-bearing dirs and "none" combining with a duplicated
holder id. Delivered: 19 dirs, 8 combining. This is the one boundary-doc line
whose falsity changes an editor's action (it would under-report the regression
surface for any future disclosure-family change).

**Named debt (carry to the round record).** D-JDEP4-1: two tracked knowledge
docs describe a superseded checker; repair is a follow-up round item, not a
r88 work item (the work phase is closed and the tree is clean at `2ea9ef1`).
D-JDEP4-2: the D1 OBS-1 row's present-tense defect framing needs a
repaired-as-of marker. D-JDEP4-3: no measurement helper exists for the five-gate
sample at `2ea9ef1` either — unchanged from r87, still unmeasured.

**Not judged here.** Calibration (C1 tuple deltas, first-cause correctness) and
coverage (C2 clusters) are sibling seats' axes; I measured the probe counts only
as drift evidence for the two docs, not as a calibration verdict. I did not
judge whether the r88 template itself is a better or worse disclosure design —
only whether the docs describe it.

## Handoff

- Deliverables: `.ufo/waves/round-88/followup/JDEP4.md` (this file) and
  `.ufo/waves/round-88/followup/JDEP4-drift.json` (machine-readable inventory:
  dead strings, live template, probe count table, census, stop-cause list,
  per-doc drift flags).
- Reproduce in one pass:
  `python3 corpus/fixtures/check_bible.py corpus/live/runs/round-85/probe-inputs/r85-masked-ambiguous`
  → 4 findings, rc=1; `… corpus/fixtures/r88-mixed-stop` → 6 findings, rc=1;
  `grep -c "first occurred at" corpus/fixtures/check_bible.py` → 0.
- Blocker for a repair seat: the boundary doc is ~15 distinct drifted items
  (strings, counts, line refs, census) and the decision table ~7 rows plus its
  whole Receipts block. Both need re-derivation from a fresh replay at
  `2ea9ef1`, not a find-and-replace of the two notice strings.
- Nothing is committed or pushed; the only repo writes are the two files above.
  No gap in the wait-checks affected this seat: every input I needed
  (checker, both docs, D1 table, the r85 probe inputs, the r88 fixtures) is
  present on the delivered tree.
