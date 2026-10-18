# Provenance-chain decision table — D2

Snapshot: `28706dc73a9b7667851fd82adb71e905ae5eb896` (`corpus/fixtures/check_bible.py:171-255`). This table follows the lifecycle phases entry validation → holder resolution → source resolution → chain comparison → post-stop. It describes checker output, not fictional-world truth.

All replay commands below were run from `/tmp/r87-D2-28706dc` against the checker archived from that revision. Existing fixture commands use committed fixture names. `r87-d2-*` probe fixtures were generated only under that scratch archive from `consistent/`, `item-chain-valid/`, or `item-chain-broken/`; they are not delivered by this table patch. Their commands and complete observed CLI output are retained below. `VIOLATION:` prefixes and final count lines are included as printed. Commands returning violations exit 1.

## Entry validation and initial eligibility

- **No `provenance` member:** the block skips the entity; absence does not assert a failed chain. Fixture `consistent` has an item without provenance.

  Replay: `python3 corpus/fixtures/check_bible.py corpus/fixtures/consistent`
  ```text
  CLEAN: schema, citations, relations, timeline; 0 violations
  ```

- **Present empty list:** valid, with no records to assess.

  Replay: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-d2-empty-list`
  ```text
  CLEAN: schema, citations, relations, timeline; 0 violations
  ```

- **Provenance on a non-item:** emits the block-level kind finding; initial chain eligibility is false (`item['kind'] == 'item'` is required), so no chain comparison is made.

  Replay: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-d2-kind-gate`
  ```text
  VIOLATION: entities[3].provenance: only valid on item entities
  1 violation(s); no canon changed
  ```

- **Present non-list value:** emits the array-shape finding and skips record iteration.

  Replay: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-d2-provenance-nonarray`
  ```text
  VIOLATION: entities[3].provenance: expected array
  1 violation(s); no canon changed
  ```

- **Item ID not unique:** duplicate item identity disables chain eligibility for the item. The duplicate-ID and any other reference diagnostics remain independent.

  Replay: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-d2-duplicate-item`
  ```text
  VIOLATION: entities[4].id: duplicate entities id 'seal'
  VIOLATION: relations[0].to: ambiguous entity 'seal'
  2 violation(s); no canon changed
  ```

- **Source table unavailable:** initial eligibility is false (`sources_available`); `source_status()` is `unavailable`, not `unknown`, so no per-reference source-ID finding is emitted for otherwise well-shaped provenance citations. The input-table load finding remains.

  Replay: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-d2-sources-unavailable`
  ```text
  VIOLATION: sources.json: cannot load JSON: [Errno 2] No such file or directory: 'corpus/fixtures/r87-d2-sources-unavailable/sources.json'
  1 violation(s); no canon changed
  ```

## Holder resolution and record validation

A record must be an object with exactly `tick`, `from_holder`, `to_holder`, and `source_id` (`:186-203`). Any invalid record makes the chain ineligible from that point onward (`:243-246`); its local record checks continue to report their findings.

- **Non-object record:**

  Replay: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-d2-record-object`
  ```text
  VIOLATION: entities[3].provenance[1]: expected object
  1 violation(s); no canon changed
  ```

- **Missing or extra key:** the key-set mismatch has its own signature; member-specific validators do not run for that record.

  Replay: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-d2-record-keys`
  ```text
  VIOLATION: entities[3].provenance[1]: expected exactly tick, from_holder, to_holder, source_id
  1 violation(s); no canon changed
  ```

- **Tick not a nonnegative exact `int`:** both a boolean (`type(True) is not int`) and a negative integer use the same finding signature.

  Replay: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-d2-tick-bool`
  ```text
  VIOLATION: entities[3].provenance[1].tick: required nonnegative integer
  1 violation(s); no canon changed
  ```
  Replay: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-d2-tick-negative`
  ```text
  VIOLATION: entities[3].provenance[1].tick: required nonnegative integer
  1 violation(s); no canon changed
  ```

- **Holder field shape:** `from_holder` permits null or a nonempty string; `to_holder` requires a nonempty string. Whitespace-only and wrong-type examples:

  Replay: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-d2-from-shape`
  ```text
  VIOLATION: entities[3].provenance[1].from_holder: required null or nonempty entity id
  1 violation(s); no canon changed
  ```
  Replay: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-d2-to-shape`
  ```text
  VIOLATION: entities[3].provenance[1].to_holder: required nonempty entity id
  1 violation(s); no canon changed
  ```

- **Dangling holder ID:** either field gets its own local dangling finding. It is not holder ambiguity and emits no ambiguity notice.

  Replay: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-d2-from-dangling`
  ```text
  VIOLATION: entities[3].provenance[1].from_holder: dangling entity 'ghost-holder'
  1 violation(s); no canon changed
  ```
  Replay: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-d2-to-dangling`
  ```text
  VIOLATION: entities[3].provenance[1].to_holder: dangling entity 'ghost-holder'
  1 violation(s); no canon changed
  ```

- **Ambiguous holder ID:** either/both holder fields get local ambiguity findings; the global duplicate entity finding remains. At the first ambiguous-holder record, exactly one item-level notice is emitted. That record is invalid and permanently latches chain comparison off (`:217-233`, `:243-246`).

  Replay: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-d2-holder-ambiguous-both`
  ```text
  VIOLATION: entities[5].id: duplicate entities id 'vault'
  VIOLATION: entities[3].provenance[1].to_holder: ambiguous entity 'vault'
  VIOLATION: entities[3].provenance[1].from_holder: ambiguous entity 'vault'
  VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous
  4 violation(s); no canon changed
  ```

## Source resolution

Source lookup yields `unavailable`, `unknown`, `unique`, or `ambiguous` (`:97-109`). A malformed/missing `source_id` or unknown/unavailable citation invalidates the record. An ambiguous source does **not** invalidate it: the chain remains assessable, while later structural comparison findings carry a scope prefix (`:234-242`, `:247-254`).

- **Malformed and unknown source ID:**

  Replay: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-d2-source-shape`
  ```text
  VIOLATION: entities[3].provenance[1].source_id: required nonempty source id
  1 violation(s); no canon changed
  ```
  Replay: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-d2-source-unknown`
  ```text
  VIOLATION: entities[3].provenance[1].source_id: unknown in-world source 'ghost-source'
  1 violation(s); no canon changed
  ```

- **Ambiguous source ID:** reports duplicate and local source ambiguity; the later holder discontinuity is still compared and explicitly labeled input-structural, not sourced-canon.

  Replay: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-d2-source-ambiguous-prefix`
  ```text
  VIOLATION: sources[3].id: duplicate sources id 'ambig-source'
  VIOLATION: entities[3].provenance[1].source_id: ambiguous in-world source 'ambig-source'
  VIOLATION: entities[3].provenance[2]: input-structural finding, not sourced-canon; provenance chain break; expected from_holder 'harbor', got 'mira'
  3 violation(s); no canon changed
  ```

## Chain comparison

Only valid records are compared while the initial eligibility gate remains true (`:247-255`). The first valid record must have null `from_holder`; later valid records independently test strict tick increase and holder continuity.

- **First record has non-null `from_holder`:**

  Replay: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-d2-first-from-nonnull`
  ```text
  VIOLATION: entities[3].provenance[0]: provenance chain break; first record must have from_holder null
  1 violation(s); no canon changed
  ```

- **Equal or reversed later tick:** both violate strict increase and use the same tick-finding signature. The equal-tick probe retains continuous holders; the reversed-tick probe does too, isolating the tick comparison.

  Replay: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-d2-tick-equal`
  ```text
  VIOLATION: entities[3].provenance[2].tick: provenance tick 3 must be greater than previous tick 3
  1 violation(s); no canon changed
  ```
  Replay: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-d2-tick-reversed`
  ```text
  VIOLATION: entities[3].provenance[2].tick: provenance tick 2 must be greater than previous tick 3
  1 violation(s); no canon changed
  ```

- **Holder discontinuity:**

  Replay: `python3 corpus/fixtures/check_bible.py corpus/fixtures/item-chain-broken`
  ```text
  VIOLATION: entities[3].provenance[2]: provenance chain break; expected from_holder 'harbor', got 'mira'
  1 violation(s); no canon changed
  ```

- **Both comparisons fail on one record:** both findings are emitted; neither is collapsed into the other.

  Replay: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-d2-both-comparisons`
  ```text
  VIOLATION: entities[3].provenance[2].tick: provenance tick 3 must be greater than previous tick 3
  VIOLATION: entities[3].provenance[2]: provenance chain break; expected from_holder 'harbor', got 'mira'
  2 violation(s); no canon changed
  ```

- **A comparison finding does not latch the chain:** checker state advances after a comparison finding; later records are still checked. This fixture has comparison findings at records 2 and 3.

  Replay: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-d2-comparison-does-not-latch`
  ```text
  VIOLATION: entities[3].provenance[2].tick: provenance tick 3 must be greater than previous tick 3
  VIOLATION: entities[3].provenance[2]: provenance chain break; expected from_holder 'harbor', got 'mira'
  VIOLATION: entities[3].provenance[3]: provenance chain break; expected from_holder 'tower', got 'mira'
  3 violation(s); no canon changed
  ```

## Post-stop behavior

- **Representative invalid-record latch:** an unknown source invalidates record 1; record 2 contains a deliberately bad tick and discontinuous holder, but neither chain-comparison finding is emitted. This illustrates the common permanent `can_check_chain = False` path for invalid records (`:243-246`).

  Replay: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-d2-unknown-source-stops-tail`
  ```text
  VIOLATION: entities[3].provenance[1].source_id: unknown in-world source 'ghost-source'
  1 violation(s); no canon changed
  ```

- **Ambiguity after an earlier invalid record:** the holder notice is still emitted on the first ambiguous-holder record even though the comparison gate already stopped at record 1.

  Replay: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-d2-earlier-invalid-then-ambiguous`
  ```text
  VIOLATION: entities[5].id: duplicate entities id 'vault'
  VIOLATION: entities[3].provenance[1].source_id: unknown in-world source 'ghost-source'
  VIOLATION: entities[3].provenance[2].to_holder: ambiguous entity 'vault'
  VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous
  4 violation(s); no canon changed
  ```

- **Other record-local checks continue after a stop:** after record 1 has a dangling holder and unknown source, record 2's dangling holder is still reported; no later chain comparisons are emitted.

  Replay: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-d2-after-stop-local`
  ```text
  VIOLATION: entities[3].provenance[1].to_holder: dangling entity 'ghost-holder'
  VIOLATION: entities[3].provenance[1].source_id: unknown in-world source 'unknown-source'
  VIOLATION: entities[3].provenance[2].to_holder: dangling entity 'later-ghost'
  3 violation(s); no canon changed
  ```

- **Ambiguous-holder stop versus the masked-break control:** the unique-holder control reports its downstream chain break. Adding a duplicate holder at the prior record instead reports ambiguity and an unassessed notice, not a guessed break.

  Replay: `python3 corpus/fixtures/check_bible.py corpus/live/runs/round-85/probe-inputs/r85-unique-break-control`
  ```text
  VIOLATION: entities[3].provenance[2]: provenance chain break; expected from_holder 'vault', got 'harbor'
  1 violation(s); no canon changed
  ```
  Replay: `python3 corpus/fixtures/check_bible.py corpus/live/runs/round-85/probe-inputs/r85-masked-ambiguous`
  ```text
  VIOLATION: entities[5].id: duplicate entities id 'vault'
  VIOLATION: entities[3].provenance[1].to_holder: ambiguous entity 'vault'
  VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous
  3 violation(s); no canon changed
  ```

- **Only first ambiguous-holder record gets the snapshot notice:** later ambiguous references still get local findings, but no second notice is emitted and the chain remains unassessed.

  Replay: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-d2-two-ambiguous-records`
  ```text
  VIOLATION: entities[5].id: duplicate entities id 'vault'
  VIOLATION: entities[3].provenance[1].to_holder: ambiguous entity 'vault'
  VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous
  VIOLATION: entities[3].provenance[2].to_holder: ambiguous entity 'vault'
  VIOLATION: entities[3].provenance[2].from_holder: ambiguous entity 'vault'
  5 violation(s); no canon changed
  ```

  **Integration debt:** this is the checker snapshot's one-notice behavior (`holder_ambiguity_notice_emitted`, `:185`, `:231-233`). Round-87 C1 calls for an explicit disclosure on every record at/after the ambiguous-holder stop. If that C1 change is integrated, replay all ambiguous-holder cases in this table and update the pasted outputs/table rows to the delivered behavior; do not present this snapshot's once-only notice as the C1 after-state.

## Assessment limits

The provenance block checks input structure, holder-ID resolution, source-ID membership, ordered ticks, and explicit `from_holder`/`to_holder` continuity only. It does not choose among duplicate IDs, inspect source text, establish custody or canon, or infer missing history. A `CLEAN` replay is only this checker's structural result for that exact input. Source status is membership, not support (`corpus/fixtures/README.md:110-128`).
