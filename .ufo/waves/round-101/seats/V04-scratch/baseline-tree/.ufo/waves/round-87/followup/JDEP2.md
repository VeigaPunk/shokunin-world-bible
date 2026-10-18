# JDEP2 — Depth judge #2 (D1 cross-reference audit)

Seat: JDEP2. Wave: round-87 follow-up (world-bible lane), fleet root
`/home/vgpnk/Projects/shokunin`, repo `lore-shokunin/`.
Mode: independent depth audit. Source under audit: `patches/D1-decision-table.md`
(the 23-row table draft). Question: does the **landed** C2 table subsume D1's
conditions? Any D1 condition absent from the landed table is a finding.
Measured tree: `2b48ca7` (work-wave evidence commit). No tracked file was written
by this seat; every output is under `.ufo/waves/round-87/followup/` or `/tmp/r87-JDEP2`.

Artifacts under audit (sha256):

| artifact | sha256 |
|---|---|
| `.ufo/waves/round-87/patches/D1-decision-table.md` | `64d83525b5a5ab08b53ca88032dc91321d3a31ed76cadd6d2326962a190840ae` |
| `.ufo/waves/round-87/patches/D2-decision-table.md` | `138450a4caa519044124282a577af70d1f6c1fb1681afae710fe9cdb7dc84788` |
| `corpus/knowledge/r87-provenance-chain-decision-table.md` (landed C2) | `6455dc14e74e7aab0588f14607dfcc4916d9b8ac39432d565c938625f02074c3` |
| `corpus/fixtures/check_bible.py` at `2b48ca7` | `3ae4134d1d7d0f4b72f5ed0b344de54e886b60ab7cacd8e8ab0008521efcb237` |
| `corpus/fixtures/check_bible.py` at D1's snapshot `28706dc` | `e8f241623aa84eb1dce192a03c9e70b8f4ba386344f0b22a99ba1ac0d4942132` |

D1's snapshot hash is confirmed exactly as D1 claims (`D1.md:4`); the delivered
checker differs, so D1's ambiguous-holder receipts are stale by construction.

## Wait-check receipt (seat dependency: I1)

I1's target was absent at HEAD through the first nine checks; it landed during the
tenth. The wait was a background poller (`test -f` on both proposed destinations,
30s spacing, run from the lane root):

```text
2026-10-17T01:40:22-03:00 JDEP2-WAITCHECK iter=1  r87-prefixed=absent unprefixed=absent I1report=absent
2026-10-17T01:40:52-03:00 JDEP2-WAITCHECK iter=2  r87-prefixed=absent unprefixed=absent I1report=absent
2026-10-17T01:41:22-03:00 JDEP2-WAITCHECK iter=3  r87-prefixed=absent unprefixed=absent I1report=absent
2026-10-17T01:41:52-03:00 JDEP2-WAITCHECK iter=4  r87-prefixed=absent unprefixed=absent I1report=absent
2026-10-17T01:42:22-03:00 JDEP2-WAITCHECK iter=5  r87-prefixed=absent unprefixed=absent I1report=absent
2026-10-17T01:42:52-03:00 JDEP2-WAITCHECK iter=6  r87-prefixed=absent unprefixed=absent I1report=absent
2026-10-17T01:43:22-03:00 JDEP2-WAITCHECK iter=7  r87-prefixed=absent unprefixed=absent I1report=absent
2026-10-17T01:43:52-03:00 JDEP2-WAITCHECK iter=8  r87-prefixed=absent unprefixed=absent I1report=absent
2026-10-17T01:44:22-03:00 JDEP2-WAITCHECK iter=9  r87-prefixed=absent unprefixed=absent I1report=absent
2026-10-17T01:44:52-03:00 JDEP2-WAITCHECK iter=10 r87-prefixed=present unprefixed=absent I1report=absent
LANDED
```

The landed file is `corpus/knowledge/r87-provenance-chain-decision-table.md`
(30 rows). The audit below is against that file, not against D1/D2 intent.

## 1. D1's 23 conditions, extracted and independently replayed

D1's table yields exactly 23 condition rows (extraction over the `|`-rows of
`patches/D1-decision-table.md`, excluding the header and separator). Because
D1's `r87-D1-*` probes are scratch-only (`D1-decision-table.md:5-10`), I rebuilt
equivalent probes under `/tmp/r87-JDEP2` from the delivered tree
(`git archive 2b48ca7 | tar -x -C /tmp/r87-JDEP2`) and replayed each against the
delivered checker. Generator + replay: `/tmp/r87-JDEP2/gen_d1_probes.py`
(23 probes); full output map: `/tmp/r87-JDEP2/d1-probe-replay.json`.

Result: **all 23 D1 conditions are real behaviors at `2b48ca7`.** 21 probes
reproduce D1's pasted stdout byte-for-byte. The two that do not are the
ambiguous-holder rows, and the difference is exactly the C1 addition:

| D1 row | probe | D1 pasted (28706dc) | observed (2b48ca7) | cause |
|---|---|---|---|---|
| 17 holder duplicated, either field | `r87-JDEP2-holder-ambiguous-both` | 4 findings, one item-level notice | **7 findings** | C1 adds per-record disclosure at the origin record and at each later record |
| 18 ambiguous after an earlier invalid stop | `r87-JDEP2-ambiguous-after-stop` | 4 findings, one notice | **6 findings** | same C1 addition |

Exact observed for row 17 (delivered tree, lane root):

```text
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-JDEP2-holder-ambiguous-both
VIOLATION: entities[5].id: duplicate entities id 'r87-double'
VIOLATION: entities[3].provenance[0].to_holder: ambiguous entity 'r87-double'
VIOLATION: entities[3].provenance[0]: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous
VIOLATION: entities[3].provenance[0]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'r87-double' first occurred at entities[3].provenance[0]
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'r87-double' first occurred at entities[3].provenance[0]
VIOLATION: entities[3].provenance[1].from_holder: ambiguous entity 'r87-double'
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'r87-double' first occurred at entities[3].provenance[0]
7 violation(s); no canon changed
```

So D1's condition inventory is sound, but its pasted outputs for rows 17-18 are
the pre-C1 state and must not be landed as-is. Two further D1 reconstruction
notes, not condition gaps: D1 row 8's pasted output is `1 violation`, while
duplicating `seal` in the shipped `item-chain-valid` base also trips the
`mira → seal` relation (`relations[0].to: ambiguous entity 'seal'`), giving 2 —
D1's probe evidently dropped that relation; and D1 row 21's pasted output is
reproducible only if the later record's `source_id` is unique, which is the point
of that row (see finding F2).

## 2. Subsumption: D1's 23 conditions vs the landed 30-row table

The landed table states at `:19-22` that it supersedes the D2 draft and refreshes
every ambiguous-holder row to the C1 after-state. Mapping each D1 condition to
the landed row(s) that carry it:

| D1 # | D1 condition | landed row(s) | status |
|---|---|---|---|
| 1 | Unique, continuous item chain (control) | 30 | covered (positive control present; D2 omitted it) |
| 2 | Wrong `from_holder` in a later record | 23 | covered |
| 3 | First record has non-null `from_holder` | 20 | covered |
| 4 | Tick not strictly greater than preceding | 21, 22 | covered |
| 5 | Comparison finding does not stop later comparisons | 25 | covered |
| 6 | Initial eligibility: `sources.json` unavailable | 6 | covered |
| 7 | Initial eligibility: provenance on a non-item | 3 | covered |
| 8 | Initial eligibility: item entity ID duplicated | 5 | covered |
| 9 | `provenance` is not a list | 4 | covered |
| 10 | Record is not an object | 7 | covered |
| 11 | Record key set not exactly the four keys | 8 | covered |
| 12 | `tick` not a nonnegative exact `int` | 9 | covered |
| 13 | `to_holder` blank / not a nonempty string | 11 | covered |
| 14 | non-null `from_holder` blank / not nonempty | 10 | covered |
| 15 | `to_holder` dangling | 12 | covered |
| 16 | non-null `from_holder` dangling | 12 | covered |
| 17 | Holder ID duplicated, either field | 13, 14, 15 | covered (C1 after-state) |
| 18 | Holder ambiguous after an earlier invalid stop | 27 | covered (C1 after-state) |
| 19 | `source_id` blank / not a nonempty string | 16 | covered |
| 20 | `source_id` unknown | 17 | covered |
| 21 | `source_id` ambiguous; findings marked input-only; **prefix persists on later unique-source records** | 18, 19 | **partly covered** — see F2 |
| 22 | Chain stop is permanent (later break unreported) | 26 | covered (representative is an unknown source, not an invalid tick; the latch is the same `:260-263` path) |
| 23 | `allied_with` faction holder interplay | — | **MISSING** — see F1 |

Result: **21 of 23 D1 conditions are fully covered; 1 is partly covered; 1 is
missing.**

The landed table also carries conditions D1 lacks (rows 1 no-provenance member,
2 empty list, 24 both comparisons on one record, 28 record-local checks after the
stop, and 29 the masked-break control pair), so it is a superset in the other
direction. Coverage is therefore not a one-way loss — only D1 row 23 and the F2
sub-clause are unsupported.

## 3. Findings

**F1 (primary, missing condition).** D1 row 23 (`allied_with` faction holder
interplay) has no counterpart anywhere in the landed table. The landed file
contains no `allied`/`faction`/`reciprocal` token (verified: `grep -n -i
"allied\|faction\|reciprocal" corpus/knowledge/r87-provenance-chain-decision-table.md`
→ no output, rc 1). The condition is real and clean at `2b48ca7`: an item whose
unique provenance holder is a faction, alongside a valid sourced reciprocal
`allied_with` edge, produces no provenance finding —

```text
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-JDEP2-allied-faction-holder
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

D1's row-23 claim (alliance is checked outside the provenance block; a faction
holder is not special-cased) is therefore accurate and uncovered by the landed
table. This is a documentation-coverage gap on the depth axis, not a checker
defect.

**F2 (narrow, sub-clause not isolated).** D1 row 21 asserts the ambiguous-source
prefix "persists on later unique-source records". The landed rows 18-19 test the
prefix on a later comparison finding, but in the landed fixture `anvil` **both**
records 1 and 2 cite the ambiguous `ambig-source` (verified by reading
`corpus/fixtures/r87-probe-record-and-chain/entities.json`), so the receipt
(`…provenance[2].source_id: ambiguous in-world source 'ambig-source'` immediately
before the prefixed break line) cannot distinguish "flag persisted from record 1"
from "flag set again at record 2". D1's probe did isolate it (its output carried
only the record-1 source-ambiguity line before the prefixed record-2 break). The
landed table states the persistence claim in prose but does not demonstrate it.

**F3 (D1 must not be landed verbatim).** D1's pasted outputs for rows 17-18 are
the pre-C1 state (`4` findings each); at `2b48ca7` the same inputs give `7` and
`6`. The landed table correctly refreshed these (rows 13-15, 27). Any future
consolidation that copies D1's receipts would regress the table to a state that
contradicts the delivered checker.

**F4 (D1 internal accuracy, minor).** D1 row 8's pasted output under-counts by one
finding relative to the shipped `item-chain-valid` base (see §1). The landed row 5
is accurate for its own `r87-probe-entry-shape` fixture.

## 4. Receipts for the landed table (independent)

The landed table's two new probes reproduce its pasted receipts exactly:

```text
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-probe-entry-shape
VIOLATION: entities[6].id: duplicate entities id 'rope'
VIOLATION: entities[4].provenance: expected array
2 violation(s); no canon changed
exit=1

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-probe-record-and-chain
… (35 lines) …
35 violation(s); no canon changed
exit=1
```

Both match `corpus/knowledge/r87-provenance-chain-decision-table.md:168-211`
verbatim, including the 35-finding count. The landed table's ambiguous-holder
receipts also match the delivered C1 after-state (each `r87-masked-break-*` gives
6 findings; `r85-masked-ambiguous` gives 5).

## 5. Depth verdict recommendation

- **As delivered at `2b48ca7` (including the landed C2 file): `improved` — with
  one named condition gap.** Before the round there was no provenance decision
  table at either destination (`R2.md:33`; `P2-scorecard-r87.md:16`). Now a
  30-row table ships, is re-pointed at durable in-tree fixtures, is refreshed to
  the C1 after-state, and its receipts reproduce. That is a real depth gain, and
  it is a superset of D2 (adds the clean positive control D2 lacked). It does not
  fully subsume D1: row 23 (F1) is absent and row 21's persistence sub-clause
  (F2) is asserted but not isolated.
- **Recommended verdict string for the depth axis: `improved`**, recorded with
  F1 as the outstanding condition gap (and F2 as a narrow wording/receipt gap).
  I do not recommend `unchanged` — a landed, replayed table is a landed artifact,
  not intent.
- **Conditional:** if the round's depth claim is scored as "C2 subsumes D1's
  conditions", then it is **not** met until an `allied_with`/faction-holder row is
  added (a one-fixture addition; my probe construction is a working recipe) and
  the F2 record is changed so the later record cites a unique source. Both are
  small and local.
- **Anti-recommendation:** do not land D1's table verbatim (F3); its rows 17-18
  contradict the delivered checker.

## 6. Method notes and gaps

- Measured revision `2b48ca7`; `git rev-parse HEAD` → `2b48ca72033dfd1060b6f81c4cf27ad83deae57f`.
  The worktree is no longer clean because sibling follow-up seats are mid-write
  (` M corpus/knowledge/holder-assessment-boundary.md`, ` M l0-questions.md`,
  `?? .ufo/waves/round-87/followup/`, `?? corpus/fixtures/r87-probe-entry-shape/`,
  `?? corpus/fixtures/r87-probe-record-and-chain/`,
  `?? corpus/knowledge/r87-provenance-chain-decision-table.md`); none of those
  files was touched by this seat.
- All checker replays were read-only; the checker contains no write calls.
- Not done: byte-identity check of my reconstructed D1 probes against D1's
  originals (they are not delivered, and D1 itself says so) — output agreement is
  the strongest available check, matching T2's approach for D2.
- Not done: full re-verification of every landed row (this seat verified the two
  new probe receipts, the C1 masked receipts, and the positive control; a
  row-by-row replay of all 30 is the other depth judge's / a verifier's job).
- No commit, no push, no registry write.
