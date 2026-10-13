# r33 clause scout — bounded observation clause

## Precedent and fit
- `.shokunin/lore/LOG.md:515` sets the proposed event: Tarin reports seeing Sella place an unlabeled paper envelope on the Lantern Harbor registry desk; it explicitly excludes contents, recipient, destination, Blue Seal and causation.
- `.shokunin/lore/LOG.md:514` says the checker validates structure/reference IDs, not source-text truth. Treat any clause map as manual editorial alignment, not validation.
- `.shokunin/lore/corpus/fixtures/r23-note-class/witnessed-absence-clause-map.md:1-4` defines a bounded witness report; `.shokunin/lore/corpus/fixtures/r23-note-class/witnessed-absence-clause-map.md:11-17` deliberately separates reported observation from world fact and excludes cause/Blue Seal. Reuse this discipline, not its absence predicate.
- `.shokunin/lore/corpus/fixtures/r10-registry-witness/timeline.json:14-23` records Sella's registry account and its local tick; `.shokunin/lore/LOG.md:139-147` (Round 10 post-scout clarification, reviewer caveat, and closure) explicitly says tick 1 is a fixture-author local beat, not proven simultaneity/clock conversion. Round 10's safe pattern is source claims limited to what the fictional excerpt states.

## Proposed literal clause (fictional, newly authored)
> I, Tarin, stood at Lantern Harbor’s registry desk. I saw Sella place an unlabeled paper envelope on the desk.

Manual map only: “I, Tarin” → event actor `tarin` (editorial speaker-ID alignment); “at Lantern Harbor’s registry desk” → event place `harbor` plus desk as description only (desk is not a new place/entity unless separately modeled); “I saw” → Tarin’s reported perception, not independent confirmation; “Sella place” → event action and subject `sella`; “an unlabeled paper envelope” → object description only, not envelope identity, owner, recipient, contents, destination, significance, or seal. Encoding a single timeline event may collapse observer and observed actor: preserve Tarin as actor only if schema permits; otherwise event actor `sella` loses the reporting perspective, so keep Tarin’s first-person report in description and do not imply event verification.

## Risks / bounds
1. **Actor semantics:** timeline `entity_id` may denote event participant rather than narrator. A row with `entity_id=tarin` should not be read as Tarin placing the envelope; include the explicit report wording in description and map it as Tarin's claim. Do not add a `placed_by` relation absent lexical/schema need.
2. **Overclaim:** “saw” is a character's statement, not proof Sella did it. No claim that this is the same paper/envelope in any other record, no motive, transfer, transaction, concealment, or causal link.
3. **Object drift:** keep “unlabeled paper envelope” literal; do not upgrade to sealed, addressed, official, carbon, route strip, record, evidence, or known owner. Do not infer its contents or destination.
4. **Time drift:** any tick/dependency is fixture ordering only. Do not synchronize to first bell, Mira's departure/arrival, or Sella's other account; equal ticks do not establish simultaneity.
5. **Scope:** no envelope contents, recipient, destination, Blue Seal/mark/carbon, canon truth, real-world provenance/rights, or source reliability conclusion. Source is invented for the fixture.

## Falsifiable check
A non-author can compare the exact excerpt against the new event/map: each mapped proposition must be directly stated (Tarin says he stood at the desk; reports seeing Sella place an unlabeled paper envelope there). Reject if any fixture field or prose asserts contents/owner/recipient/destination, sealing, Blue Seal connection, causal motive, verified world fact, or cross-record identity; reject if event wording drops the reporting attribution and presents the placement as independently established. Also confirm no mapping extends beyond this single event, and the timeline's order/tick is not described as an external clock fact. This check is falsified by even one unsupported implication.
