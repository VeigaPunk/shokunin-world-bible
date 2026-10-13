# Round 45 simplifier — occupancy guard or no-go

## Recommendation: no-go on current evidence

The smallest proposed change would be to skip the existing occupancy comparison/store only when the uniquely resolved `entity_id` has `kind == 'faction'` (at `check_bible.py:243-252`), while retaining the same-ID/same-tick conflict for characters and other kinds. That is mechanically narrow, but the evidence supplied so far does not ground the semantic exception. Do not implement it merely because factions can be distributed in ordinary language or because a fictional report says so: the checker validates structural rules, not the truth of invented source text.

## Evidence and scope

- `check_bible.py:7-13` permits four entity kinds; timeline `entity_id` is a generic string field. `:228-252` resolves actor ambiguity and applies occupancy by raw unique actor ID/tick, with no kind branch. `:245-252` requires a uniquely resolved place and nonnegative tick, then flags different places for the same actor/tick.
- Fixture `README.md:29-34` defines local ticks and says, “A character cannot occupy different places at the same tick.” This establishes a character rule, not a converse that factions are distributed, nor an explicit exception for factions. It also does not specify whether a faction-subject event records the location of an indivisible represented actor, a membership/outpost presence, or something else.
- Round 44 rejected reading a generic `entity_id` as character-only; that rejection does not establish that every noncharacter avoids occupancy constraints. The r21 README material (`README.md:443-468`) concerns malformed dependency handling and preservation of occupancy checks, not faction semantics. Check cited r12/r22/r24 precedent reports before treating them as resolving the new class; generic actor identity, dependency, or entity-resolution behavior is not itself evidence of a faction occupancy contract.
- A source excerpt authored for a test can demonstrate that a proposed input shape is representable, but cannot authenticate itself or establish fictional canon. A checker CLEAN/finding is likewise structural evidence only.

## Risks

A faction-kind exemption could suppress a useful inconsistency if the timeline convention treats each faction ID as one actor/location. Conversely, retaining the current universal same-ID occupancy comparison may overstate a contradiction if the record explicitly represents simultaneous separate outposts. Neither interpretation follows solely from the `faction` label. Do not generalize to all noncharacters, infer all factions are distributed, create a generic “entity actor” ontology, or alter source-authentication expectations. Preserve the existing character double-booking behavior in any future candidate.

## Falsifiable go/no-go test

**No-go now.** Reconsider only with an explicit project-level event/occupancy convention that says what a faction actor's location means, or a grounded event subtype/field that identifies distributed-presence events without inferring it from prose. Then test a narrowly scoped faction case with two distinct valid places at one tick, a faction single-location control, and a character double-booking control. Go only if independent review confirms the scoped case is valid under that convention, the checker currently reports the targeted false positive, the proposed condition removes only that finding, and the character conflict remains. No-go if the convention is absent/ambiguous, if it treats faction IDs as singular locations, if the proposed exception suppresses a legitimate conflict, or if the only support is a newly authored fictional excerpt. Preserve/replay the prior 95 fixtures and 474 JSON paths if implementation is later authorized; this recommendation itself claims no axis improvement and licenses no checker/fixture/README/LOG edit.
