# Round 45 checker scout — faction occupancy

## Finding

The candidate branch is real and the baseline probe reproduces faction double-booking, but this is **not enough to authorize a calibration change**. The existing checker can be said to enforce occupancy for every uniquely indexed actor kind; the README only documents the character rule. That difference is a testable gap, not evidence that the rule is semantically wrong for factions. **Go/no-go: NO-GO for changing checker behavior on this evidence.** Keep the probe as a baseline observation and request domain evidence / independent review before any guard.

## Path:line evidence

- `corpus/fixtures/check_bible.py:7` allows the entity kinds `character`, `place`, `faction`, and `item`; there is no character-only timeline actor schema.
- `corpus/fixtures/check_bible.py:12-13` types `timeline.entity_id` only as `str`, not as a character reference.
- `corpus/fixtures/check_bible.py:228-252` resolves actor/place IDs, checks unique actor IDs and a uniquely resolved `place`, and uses `(row['entity_id'], row['tick'])` as the occupancy key at lines 245-252. The block has no actor-kind condition. Its `double-booked` diagnostic is generated at line 250.
- `corpus/fixtures/README.md:19-27` explicitly recognizes fictional faction entities in relation fixtures but limits that discussion to the alliance convention; it does not say factions are distributed or have simultaneous locations.
- `corpus/fixtures/README.md:29-34` defines tick as a local sequence, allows same-place simultaneous records, and states only “A character cannot occupy different places at the same tick.” It does not define whether a faction event's `place_id` means a member, outpost, whole faction, or scene.
- `.shokunin/lore/LOG.md:750-752` records r44's rejection: generic `entity_id` does not prove a character-only input rule; a clean structurally altered probe is not proof of semantic invalidity. `.shokunin/lore/LOG.md:755-757` sets r45's falsifiable premise and requires prior-art review, distinct-place faction pair, character control, and no assumed faction ontology.
- Precedent `corpus/fixtures/README.md:12-27` establishes factions and a narrow relation rule, not faction location semantics. The occupancy precedents are `corpus/fixtures/README.md:~` (round descriptions in the same README) and checker lines 228-252: actor ambiguity, missing/wrong/ambiguous place, negative tick, and malformed dependency guards do not authorize broadening the actor-kind interpretation. In particular r12/r13 fixtures preserve unique/missing/ambiguous actor identity behavior; r16-r21 concern resolved place/time/input eligibility, not faction distribution. R24 is relation-endpoint identity only.

## Temporary reproduction (outside repo)

Created temporary clones under `/tmp/lore-r45-*`; no repository fixture or checker file was edited. Starting with `consistent/`, changed the two events to tick 7 at `harbor` and `tower`, and changed the uniquely indexed `mira` row's kind to `faction` (then ran an otherwise paired `character` control). The checker emits for **both**:

`VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'`

Both also emit the unrelated existing equal-tick dependency inversion because the copied second event depends on the first; this probe therefore demonstrates the occupancy branch but is not a clean isolated pair. Character double-booking is preserved in the observed output. The test says nothing about any source text, faction outposts, membership, or canon. The entity ID/name staying `mira` is a fixture-construction artifact, not a faction model.

## Risks and falsifiable disposition

A faction might be a collective represented at two sites, but a row could instead denote a singular headquarters, a specific delegation, or an editorial actor for which the event place is intended to be exclusive. Faction-kind alone does not discriminate these meanings. Applying a blanket faction exception could suppress real contradictions; applying an exception only after source prose says “outposts” would make source-text parsing/editorial judgment a separate unimplemented requirement. Do not generalize this candidate to all noncharacters or introduce a generic “distributed entity” category without a schema contract.

**Falsifiable go condition:** independently establish that this timeline convention allows one uniquely indexed faction subject to have distinct simultaneous place assignments (not merely that a faction may own or maintain multiple places), then test a valid faction multi-site pair and a contradictory/singular faction pair under that same convention. Any future narrow change must still report the paired unique-character conflict and preserve all existing outputs. If that convention cannot be established, or if the checker is intended to represent a single location per subject regardless of kind, the proposal remains no-go. Current evidence establishes only that the implementation reports the pair and the prose contract expressly names characters; it does not establish which interpretation is correct.
