# Provenance-chain decision table (round 87, C2)

Snapshot: `2b48ca72033dfd1060b6f81c4cf27ad83deae57f` (HEAD of the round-87
work wave), checker `corpus/fixtures/check_bible.py` (SHA-256
`3ae4134d1d7d0f4b72f5ed0b344de54e886b60ab7cacd8e8ab0008521efcb237`).
This table describes the checker's output for input conditions, in lifecycle
order: entry gate → holder/record validation → source resolution → chain
comparison → post-stop. It is not a statement of fictional-world truth.

All commands below are run from the repository root as
`python3 corpus/fixtures/check_bible.py <fixture>`. Every row's observed
output is pasted from a rerun on this tree; the full, unelided outputs for
every cited fixture are in "Receipts" at the end. `VIOLATION:` lines are
printed one per finding; a run with findings exits 1 and ends with
`N violation(s); no canon changed`, a clean run exits 0 with
`CLEAN: schema, citations, relations, timeline; 0 violations`.

Line anchors are `corpus/fixtures/check_bible.py:<line>` at this snapshot.
Rows 31-35 (boundary gate, combination classes) were added at round
closure from follow-up attack probes (`.ufo/waves/round-87/followup/JDEP3.md`,
fixes U-1, U-2, U-3, U-4, U-5, U-6, U-8, U-9) and re-measured on the closure tree.
This table supersedes the pre-C1 snapshot in
`.ufo/waves/round-87/patches/D2-decision-table.md`: every ambiguous-holder
row is refreshed to the C1 after-state (per-record unassessed disclosure),
and every row is re-pointed at a durable fixture that ships in this tree.

## Entry gate and initial eligibility

| # | Condition | Code anchor | Emitted signature (verbatim) | Verifying fixture | Observed output |
|---|---|---|---|---|---|
| 1 | Entity has no `provenance` member | `:171-173` | none — the block is skipped; absence asserts no chain, not a failed one | `consistent` | `CLEAN: schema, citations, relations, timeline; 0 violations` (exit 0) |
| 2 | `provenance` present as an empty list | `:178-180` (list accepted), `:187` (loop runs zero times) | none — valid, no records to assess | `r87-probe-entry-shape` (`seal`) | no `seal` line in the 2-finding output (see Receipts) |
| 3 | `provenance` on a non-item entity | `:176-177` | `entities[0].provenance: only valid on item entities` | `r61-independent-empty` (`mira`, character) | `VIOLATION: entities[0].provenance: only valid on item entities` |
| 4 | `provenance` value is not an array | `:178-180` | `entities[4].provenance: expected array` | `r87-probe-entry-shape` (`lamp`) | `VIOLATION: entities[4].provenance: expected array` |
| 5 | Item ID is not unique | `:183` (`entity_id_counts[item['id']] == 1` false) | `entities[6].id: duplicate entities id 'rope'`; chain eligibility is false, so no comparison is made for that item | `r87-probe-entry-shape` | `VIOLATION: entities[6].id: duplicate entities id 'rope'` — and no chain-break line for either `rope` row despite the injected record-2 break |
| 6 | Source table unavailable (cannot load) | `:97-99` (`unavailable`), `:183` | `sources.json: cannot load JSON: …`; `source_status()` is `unavailable`, so no per-reference `source_id` finding is emitted | `r61-independent-unavailable` | `VIOLATION: sources.json: cannot load JSON: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)` — and no `entities[0].provenance[0].source_id:` line |

## Holder resolution and record validation

A record must be an object with exactly `tick`, `from_holder`, `to_holder`,
and `source_id` (`:201-203`). An invalid record sets
`can_check_chain = False` from that point on (`:260-263`); its own local
checks still run and still report.

| # | Condition | Code anchor | Emitted signature (verbatim) | Verifying fixture | Observed output |
|---|---|---|---|---|---|
| 7 | Record is not an object | `:196-197` | `entities[3].provenance[0]: expected object` | `r87-probe-record-and-chain` (`lamp` r0) | `VIOLATION: entities[3].provenance[0]: expected object` |
| 8 | Record key set is not exactly the four keys (missing or extra) | `:201-203` | `entities[3].provenance[1]: expected exactly tick, from_holder, to_holder, source_id` | `r87-probe-record-and-chain` (`lamp` r1 missing `source_id`; r10 extra `extra`) | `VIOLATION: entities[3].provenance[1]: expected exactly tick, from_holder, to_holder, source_id` and `VIOLATION: entities[3].provenance[10]: expected exactly tick, from_holder, to_holder, source_id` |
| 9 | `tick` is not a nonnegative exact `int` (boolean or negative) | `:214-216` | `entities[3].provenance[2].tick: required nonnegative integer` | `r87-probe-record-and-chain` (`lamp` r2 boolean, r3 negative) | `VIOLATION: entities[3].provenance[2].tick: required nonnegative integer` and `VIOLATION: entities[3].provenance[3].tick: required nonnegative integer` |
| 10 | `from_holder` is neither null nor a nonempty string | `:217-219` | `entities[3].provenance[4].from_holder: required null or nonempty entity id` | `r87-probe-record-and-chain` (`lamp` r4 whitespace) | `VIOLATION: entities[3].provenance[4].from_holder: required null or nonempty entity id` |
| 11 | `to_holder` is not a nonempty string | `:220-222` | `entities[3].provenance[5].to_holder: required nonempty entity id` | `r87-probe-record-and-chain` (`lamp` r5 integer) | `VIOLATION: entities[3].provenance[5].to_holder: required nonempty entity id` |
| 12 | Holder ID dangles (no such entity) | `:223-225` (`to_holder`), `:234-236` (`from_holder`) | `…to_holder: dangling entity 'ghost'` / `…from_holder: dangling entity 'ghost2'` | `r87-probe-record-and-chain` (`lamp` r6/r7); also `r61-independent-empty` | `VIOLATION: entities[3].provenance[6].to_holder: dangling entity 'ghost'` and `VIOLATION: entities[3].provenance[7].from_holder: dangling entity 'ghost2'` |
| 13 | Holder ID is ambiguous (duplicate entity ID) | `:226-230` (`to_holder`), `:237-241` (`from_holder`) | `…to_holder: ambiguous entity 'dup'` and/or `…from_holder: ambiguous entity 'dup'` | `r87-probe-record-and-chain` (`bell` r0, both fields); `r87-masked-break-to-ambiguous` (to); `r87-masked-break-from-ambiguous` (from) | `VIOLATION: entities[5].provenance[0].to_holder: ambiguous entity 'dup'` + `VIOLATION: entities[5].provenance[0].from_holder: ambiguous entity 'dup'` |
| 14 | First ambiguous-holder record emits exactly one item-level notice | `:242-245` | `entities[5].provenance[0]: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous` | `r87-probe-record-and-chain` (`bell`); `r87-masked-break-to-ambiguous`; `r87-masked-break-from-ambiguous` | emitted once at the origin record; no second copy at later records (see row 15 receipts) |
| 15 | **C1 after-state:** every record at/after the stop carries a per-record disclosure | `:246-250` (origin record), `:189-195` (later records) | `entities[5].provenance[1]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'dup', from_holder 'dup' first occurred at entities[5].provenance[0]` | `r87-probe-record-and-chain` (`bell` r0→r1, `chime` r1); `r87-masked-break-to-ambiguous`; `r87-masked-break-from-ambiguous` | origin record gets the row-14 notice **and** a self-referential disclosure; each later record gets the disclosure naming the origin record (see Receipts) |

## Source resolution

Source lookup yields `unavailable`, `unknown`, `unique`, or `ambiguous`
(`:97-101`). A malformed, unknown, or unavailable `source_id` invalidates
the record; an ambiguous source does **not** — the chain gate stays open and
later structural comparison findings carry the
`input-structural finding, not sourced-canon; ` prefix (`:258-259`,
`:267-271`).

| # | Condition | Code anchor | Emitted signature (verbatim) | Verifying fixture | Observed output |
|---|---|---|---|---|---|
| 16 | `source_id` is not a nonempty string | `:251-253` | `entities[3].provenance[8].source_id: required nonempty source id` | `r87-probe-record-and-chain` (`lamp` r8 blank) | `VIOLATION: entities[3].provenance[8].source_id: required nonempty source id` |
| 17 | `source_id` is unknown (no such source row) | `:254-257`, `:103-106` | `entities[3].provenance[9].source_id: unknown in-world source 'ghost-source'` | `r87-probe-record-and-chain` (`lamp` r9, `rope` r7) | `VIOLATION: entities[3].provenance[9].source_id: unknown in-world source 'ghost-source'` |
| 18 | `source_id` is ambiguous (duplicate source row); record stays valid | `:258-259`, `:107-108` | `entities[7].provenance[1].source_id: ambiguous in-world source 'ambig-source'` | `r87-probe-record-and-chain` (`anvil` r1, r2); `r7-item-ambiguous` | `VIOLATION: entities[7].provenance[1].source_id: ambiguous in-world source 'ambig-source'` — no chain-gate latch; `anvil` r2 is still compared |
| 19 | Ambiguous source prefixes a later comparison finding | `:267`, `:269`, `:271` | `entities[7].provenance[2]: input-structural finding, not sourced-canon; provenance chain break; expected from_holder 'harbor', got 'mira'` | `r87-probe-record-and-chain` (`anvil` r2, the `:269` chain-break prefix); `r87-probe-source-prefix` (`:267` tick prefix, `:271` first-record prefix, both at one record) | `VIOLATION: entities[7].provenance[2]: input-structural finding, not sourced-canon; provenance chain break; expected from_holder 'harbor', got 'mira'` |

## Chain comparison

Only valid records are compared while the eligibility gate remains open
(`:264-273`). The first valid record must have null `from_holder`; later
valid records independently test strict tick increase and holder continuity.

| # | Condition | Code anchor | Emitted signature (verbatim) | Verifying fixture | Observed output |
|---|---|---|---|---|---|
| 20 | First valid record has non-null `from_holder` | `:270-271` | `entities[4].provenance[0]: provenance chain break; first record must have from_holder null` | `r87-probe-record-and-chain` (`rope` r0) | `VIOLATION: entities[4].provenance[0]: provenance chain break; first record must have from_holder null` |
| 21 | Tick equal to previous (holders continuous) | `:265-267` | `entities[4].provenance[1].tick: provenance tick 0 must be greater than previous tick 0` | `r87-probe-record-and-chain` (`rope` r1) | `VIOLATION: entities[4].provenance[1].tick: provenance tick 0 must be greater than previous tick 0` |
| 22 | Tick reversed (holders continuous) | `:265-267` | `entities[4].provenance[3].tick: provenance tick 1 must be greater than previous tick 2` | `r87-probe-record-and-chain` (`rope` r3) | `VIOLATION: entities[4].provenance[3].tick: provenance tick 1 must be greater than previous tick 2` |
| 23 | Holder discontinuity | `:268-269` | `entities[4].provenance[4]: provenance chain break; expected from_holder 'tower', got 'mira'` | `r87-probe-record-and-chain` (`rope` r4); `item-chain-broken`; `r87-chain-unique-broken` | `VIOLATION: entities[4].provenance[4]: provenance chain break; expected from_holder 'tower', got 'mira'` |
| 24 | Both comparisons fail on one record | `:265-269` | tick line **and** break line at the same `record_label` | `r87-probe-record-and-chain` (`rope` r6) | `VIOLATION: entities[4].provenance[6].tick: provenance tick 3 must be greater than previous tick 5` and `VIOLATION: entities[4].provenance[6]: provenance chain break; expected from_holder 'harbor', got 'tower'` |
| 25 | A comparison finding does not latch the chain | `:264-273` (state advances) | a second, independent comparison finding on a later record | `r87-probe-record-and-chain` (`rope` r4 then r5) | `VIOLATION: entities[4].provenance[4]: provenance chain break; expected from_holder 'tower', got 'mira'` followed by `VIOLATION: entities[4].provenance[5]: provenance chain break; expected from_holder 'tower', got 'mira'` |

## Post-stop behavior

| # | Condition | Code anchor | Emitted signature (verbatim) | Verifying fixture | Observed output |
|---|---|---|---|---|---|
| 26 | Invalid record latches the tail (unknown source) | `:254-257` (invalidate), `:260-263` (latch) | only the invalid record's own finding; no comparison findings for later valid records | `r87-probe-record-and-chain` (`rope` r7 invalid, r8 valid-but-would-break) | `VIOLATION: entities[4].provenance[7].source_id: unknown in-world source 'ghost-source'` — and no break at r8 |
| 27 | Ambiguity notice/disclosure after an earlier invalid record | `:242-250` | notice + per-record disclosure still emitted on the first ambiguous-holder record even though the gate already stopped | `r87-probe-record-and-chain` (`chime` r0 invalid, r1 ambiguous); `r85-masked-ambiguous` | `VIOLATION: entities[6].provenance[1]: … unassessed at this and all later records because holder identity is ambiguous` and the paired `… first occurred at entities[6].provenance[1]` line |
| 28 | Record-local checks continue after the stop | `:251-259` (record-local checks run before the latch is tested) | a later record's holder-identity findings are still reported even though comparisons are unassessed | `r87-probe-record-and-chain` (`bell` r1 `from_holder` ambiguous after r0 armed the stop) | `VIOLATION: entities[5].provenance[1].from_holder: ambiguous entity 'dup'` |
| 29 | Masked-break control pair: unique vs duplicated holder | `:242-250` | unique control reports the downstream break; the duplicated-holder variant reports ambiguity + disclosure instead of a guessed break | `r85-unique-break-control` vs `r87-masked-break-to-ambiguous` | `VIOLATION: entities[3].provenance[2]: provenance chain break; expected from_holder 'vault', got 'harbor'` (control) vs the 6-line ambiguous output (variant) |
| 31 | Boundary, above the block: entity row rejected by the schema gate never reaches the provenance block | `:65-76` (row dropped), block `:171-273` never runs | `entities[i].<field>: required nonempty …` for the malformed member; every provenance diagnostic for that item is silently absent — no notice, no disclosure | `r87-probe-rowshape-rejected` | `VIOLATION: entities[0].name: required nonempty str` and `VIOLATION: relations[0].to: dangling entity 'seal'` — no provenance line of any kind |
| 32 | Shape-invalid record carrying the ambiguous holder id | `:196-206` (`continue` precedes the holder check) | key-set finding only; the holder stop is never armed, and the tail is neither reported nor disclosed | `r87-probe-shape-ambiguous` | `VIOLATION: entities[5].provenance[0]: expected exactly tick, from_holder, to_holder, source_id` — zero `unassessed` lines; pre-existing, unchanged by C1 |
| 33 | One record carrying both an ambiguous holder and an unknown source | `:226-230`/`:237-241` + `:254-257` | both findings on the same record; disclosure and unknown-source line co-occur; tail disclosed | `r87-probe-multi-invalid` | six findings, in order: duplicate `vault` id; ambiguous `from_holder`; item-level notice; disclosure at [1]; unknown source at [1]; disclosure at [2] |
| 34 | `kind` outside `KINDS` with `provenance` | `:145-147` + `:176-177` | kind finding plus only-valid-on-item finding on the same entity | `r87-probe-nonitem-kinds` (`relic-x`) | `VIOLATION: entities[0].kind: unknown kind 'relic'` and `VIOLATION: entities[0].provenance: only valid on item entities` |
| 35 | Non-item entity carrying an ambiguous holder | `:176-177` + `:226-250` | the disclosure family fires even though the chain was never eligible; disclosure emission does not depend on chain eligibility | `r87-probe-nonitem-kinds` (`chalice`) | `VIOLATION: entities[5].provenance: only valid on item entities`; then ambiguous `from_holder`, item-level notice, per-record disclosures at [1] and [2] |
| 30 | Positive control: clean, nonempty, continuous chain | `:264-273` (no finding) | `CLEAN: schema, citations, relations, timeline; 0 violations` | `item-chain-valid`; `r87-chain-unique-valid` | `CLEAN: schema, citations, relations, timeline; 0 violations` (exit 0) |

## Assessment limits

The provenance block checks input structure, holder-ID resolution, source-ID
membership, ordered ticks, and explicit `from_holder`/`to_holder` continuity
only. It does not choose among duplicate IDs, inspect source text, establish
custody or canon, or infer missing history. Ambiguity of holder identity
never resumes assessment within a run and never infers a break; ambiguity of
source ID does not invalidate an otherwise-valid record and only prefixes
later structural findings. A `CLEAN` replay is only this checker's structural
result for that exact input. If `sources.json` cannot be loaded, every
provenance comparison is suppressed for the whole run with no notice or
disclosure of any kind — the `unassessed` disclosure family exists only for
holder ambiguity (follow-up probes `P5-unavailable-suppression`/`P5b`,
`.ufo/waves/round-87/followup/JDEP3-probes.json`). Source status is membership, not support
(`corpus/fixtures/README.md:110-128`); holder kind need not mean legal
ownership.

## Receipts

Full verbatim outputs from reruns on this tree (repository root
`/home/vgpnk/Projects/shokunin/lore-shokunin`). Exit codes are shown per
command. These are the raw receipts behind every row above.

```text
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/consistent
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/item-chain-valid
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-chain-unique-valid
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/item-chain-broken
VIOLATION: entities[3].provenance[2]: provenance chain break; expected from_holder 'harbor', got 'mira'
1 violation(s); no canon changed
exit=1

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-chain-unique-broken
VIOLATION: entities[3].provenance[2]: provenance chain break; expected from_holder 'harbor', got 'mira'
1 violation(s); no canon changed
exit=1

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r7-item-ambiguous
VIOLATION: sources[2].id: duplicate sources id 'archive-ledger'
VIOLATION: entities[1].first_appearance: ambiguous in-world source 'archive-ledger'
VIOLATION: entities[1].claims[0].source_id: ambiguous in-world source 'archive-ledger'
VIOLATION: entities[2].first_appearance: ambiguous in-world source 'archive-ledger'
VIOLATION: entities[2].claims[0].source_id: ambiguous in-world source 'archive-ledger'
VIOLATION: entities[3].provenance[1].source_id: ambiguous in-world source 'archive-ledger'
VIOLATION: entities[3].provenance[2].source_id: ambiguous in-world source 'archive-ledger'
7 violation(s); no canon changed
exit=1

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-masked-break-to-ambiguous
VIOLATION: entities[5].id: duplicate entities id 'dup'
VIOLATION: entities[3].provenance[0].to_holder: ambiguous entity 'dup'
VIOLATION: entities[3].provenance[0]: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous
VIOLATION: entities[3].provenance[0]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'dup' first occurred at entities[3].provenance[0]
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'dup' first occurred at entities[3].provenance[0]
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'dup' first occurred at entities[3].provenance[0]
6 violation(s); no canon changed
exit=1

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-masked-break-from-ambiguous
VIOLATION: entities[5].id: duplicate entities id 'dup'
VIOLATION: entities[3].provenance[0].from_holder: ambiguous entity 'dup'
VIOLATION: entities[3].provenance[0]: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous
VIOLATION: entities[3].provenance[0]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity from_holder 'dup' first occurred at entities[3].provenance[0]
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity from_holder 'dup' first occurred at entities[3].provenance[0]
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity from_holder 'dup' first occurred at entities[3].provenance[0]
6 violation(s); no canon changed
exit=1

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-probe-entry-shape
VIOLATION: entities[6].id: duplicate entities id 'rope'
VIOLATION: entities[4].provenance: expected array
2 violation(s); no canon changed
exit=1

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-probe-record-and-chain
VIOLATION: sources[3].id: duplicate sources id 'ambig-source'
VIOLATION: entities[9].id: duplicate entities id 'dup'
VIOLATION: entities[3].provenance[0]: expected object
VIOLATION: entities[3].provenance[1]: expected exactly tick, from_holder, to_holder, source_id
VIOLATION: entities[3].provenance[2].tick: required nonnegative integer
VIOLATION: entities[3].provenance[3].tick: required nonnegative integer
VIOLATION: entities[3].provenance[4].from_holder: required null or nonempty entity id
VIOLATION: entities[3].provenance[5].to_holder: required nonempty entity id
VIOLATION: entities[3].provenance[6].to_holder: dangling entity 'ghost'
VIOLATION: entities[3].provenance[7].from_holder: dangling entity 'ghost2'
VIOLATION: entities[3].provenance[8].source_id: required nonempty source id
VIOLATION: entities[3].provenance[9].source_id: unknown in-world source 'ghost-source'
VIOLATION: entities[3].provenance[10]: expected exactly tick, from_holder, to_holder, source_id
VIOLATION: entities[4].provenance[0]: provenance chain break; first record must have from_holder null
VIOLATION: entities[4].provenance[1].tick: provenance tick 0 must be greater than previous tick 0
VIOLATION: entities[4].provenance[3].tick: provenance tick 1 must be greater than previous tick 2
VIOLATION: entities[4].provenance[4]: provenance chain break; expected from_holder 'tower', got 'mira'
VIOLATION: entities[4].provenance[5]: provenance chain break; expected from_holder 'tower', got 'mira'
VIOLATION: entities[4].provenance[6].tick: provenance tick 3 must be greater than previous tick 5
VIOLATION: entities[4].provenance[6]: provenance chain break; expected from_holder 'harbor', got 'tower'
VIOLATION: entities[4].provenance[7].source_id: unknown in-world source 'ghost-source'
VIOLATION: entities[5].provenance[0].to_holder: ambiguous entity 'dup'
VIOLATION: entities[5].provenance[0].from_holder: ambiguous entity 'dup'
VIOLATION: entities[5].provenance[0]: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous
VIOLATION: entities[5].provenance[0]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'dup', from_holder 'dup' first occurred at entities[5].provenance[0]
VIOLATION: entities[5].provenance[1]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'dup', from_holder 'dup' first occurred at entities[5].provenance[0]
VIOLATION: entities[5].provenance[1].from_holder: ambiguous entity 'dup'
VIOLATION: entities[6].provenance[0].source_id: unknown in-world source 'ghost-source'
VIOLATION: entities[6].provenance[1].to_holder: ambiguous entity 'dup'
VIOLATION: entities[6].provenance[1]: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous
VIOLATION: entities[6].provenance[1]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'dup' first occurred at entities[6].provenance[1]
VIOLATION: entities[7].provenance[1].source_id: ambiguous in-world source 'ambig-source'
VIOLATION: entities[7].provenance[2].source_id: ambiguous in-world source 'ambig-source'
VIOLATION: entities[7].provenance[2]: input-structural finding, not sourced-canon; provenance chain break; expected from_holder 'harbor', got 'mira'
34 violation(s); no canon changed
exit=1

$ python3 corpus/fixtures/check_bible.py corpus/live/runs/round-85/probe-inputs/r85-unique-break-control
VIOLATION: entities[3].provenance[2]: provenance chain break; expected from_holder 'vault', got 'harbor'
1 violation(s); no canon changed
exit=1

$ python3 corpus/fixtures/check_bible.py corpus/live/runs/round-85/probe-inputs/r85-masked-ambiguous
VIOLATION: entities[5].id: duplicate entities id 'vault'
VIOLATION: entities[3].provenance[1].to_holder: ambiguous entity 'vault'
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'vault' first occurred at entities[3].provenance[1]
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'vault' first occurred at entities[3].provenance[1]
5 violation(s); no canon changed
exit=1

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-probe-source-prefix
VIOLATION: sources[2].id: duplicate sources id 'ambig-src'
VIOLATION: entities[3].provenance[0].source_id: ambiguous in-world source 'ambig-src'
VIOLATION: entities[3].provenance[0]: input-structural finding, not sourced-canon; provenance chain break; first record must have from_holder null
VIOLATION: entities[3].provenance[1].tick: input-structural finding, not sourced-canon; provenance tick 0 must be greater than previous tick 0
VIOLATION: entities[3].provenance[1]: input-structural finding, not sourced-canon; provenance chain break; expected from_holder 'harbor', got 'mira'
5 violation(s); no canon changed
exit=1

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-probe-rowshape-rejected
VIOLATION: entities[0].name: required nonempty str
VIOLATION: relations[0].to: dangling entity 'seal'
2 violation(s); no canon changed
exit=1

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-probe-shape-ambiguous
VIOLATION: entities[1].id: duplicate entities id 'dup'
VIOLATION: entities[5].provenance[0]: expected exactly tick, from_holder, to_holder, source_id
2 violation(s); no canon changed
exit=1

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-probe-multi-invalid
VIOLATION: entities[1].id: duplicate entities id 'vault'
VIOLATION: entities[5].provenance[1].from_holder: ambiguous entity 'vault'
VIOLATION: entities[5].provenance[1]: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous
VIOLATION: entities[5].provenance[1]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity from_holder 'vault' first occurred at entities[5].provenance[1]
VIOLATION: entities[5].provenance[1].source_id: unknown in-world source 'ghost-source'
VIOLATION: entities[5].provenance[2]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity from_holder 'vault' first occurred at entities[5].provenance[1]
6 violation(s); no canon changed
exit=1

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-probe-nonitem-kinds
VIOLATION: entities[2].id: duplicate entities id 'vault'
VIOLATION: entities[0].kind: unknown kind 'relic'
VIOLATION: entities[0].provenance: only valid on item entities
VIOLATION: entities[5].provenance: only valid on item entities
VIOLATION: entities[5].provenance[1].from_holder: ambiguous entity 'vault'
VIOLATION: entities[5].provenance[1]: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous
VIOLATION: entities[5].provenance[1]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity from_holder 'vault' first occurred at entities[5].provenance[1]
VIOLATION: entities[5].provenance[2]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity from_holder 'vault' first occurred at entities[5].provenance[1]
8 violation(s); no canon changed
exit=1
```

`r61-independent-empty` and `r61-independent-unavailable` receipts (used for
rows 3, 6, and 12):

```text
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r61-independent-empty
VIOLATION: entities[0].first_appearance: unknown in-world source 'courier-log'
VIOLATION: entities[0].claims[0].source_id: unknown in-world source 'courier-log'
VIOLATION: entities[1].first_appearance: unknown in-world source 'archive-ledger'
VIOLATION: entities[1].claims[0].source_id: unknown in-world source 'archive-ledger'
VIOLATION: entities[2].first_appearance: unknown in-world source 'archive-ledger'
VIOLATION: entities[2].claims[0].source_id: unknown in-world source 'archive-ledger'
VIOLATION: entities[3].first_appearance: unknown in-world source 'courier-log'
VIOLATION: entities[3].claims[0].source_id: unknown in-world source 'courier-log'
VIOLATION: relations[0].source_id: unknown in-world source 'courier-log'
VIOLATION: entities[0].provenance: only valid on item entities
VIOLATION: entities[0].provenance[0].to_holder: dangling entity 'nobody'
VIOLATION: entities[0].provenance[0].from_holder: dangling entity 'ghost'
VIOLATION: entities[0].provenance[0].source_id: unknown in-world source 'courier-log'
VIOLATION: timeline[0].source_id: unknown in-world source 'courier-log'
VIOLATION: timeline[0].tick: must be nonnegative
VIOLATION: timeline[0].depends_on: unknown event 'missing-event'
VIOLATION: timeline[1].source_id: unknown in-world source 'courier-log'
17 violation(s); no canon changed
exit=1

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r61-independent-unavailable
VIOLATION: sources.json: cannot load JSON: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
VIOLATION: entities[0].provenance: only valid on item entities
VIOLATION: entities[0].provenance[0].to_holder: dangling entity 'nobody'
VIOLATION: entities[0].provenance[0].from_holder: dangling entity 'ghost'
VIOLATION: timeline[0].tick: must be nonnegative
VIOLATION: timeline[0].depends_on: unknown event 'missing-event'
6 violation(s); no canon changed
exit=1
```
