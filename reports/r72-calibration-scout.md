# Round 72 calibration scout — timeline removal and residual implications

## Scope and evidence

I read the Round 72 declaration in `.shokunin/lore/LOG.md`, the full five-table `r43-jorin-vela-sighting` fixture (especially `entities.json`, `sources.json`, `timeline.json`, `vela-note-excerpt.md`, `vela-clause-map.md`, and `jorin-note-excerpt.md`/`jorin-clause-map.md`), the Round 71 critic, reviewer, verifier and final adjudicator reports, and `corpus/fixtures/check_bible.py`. No r72 candidate fixture exists in the inspected checkout; this is a review of the declared representation, not an audit of unprovided wording or rows.

## Timeline harm

The declared change explicitly adds one Vela entity claim and no event, dependency, relation or contradiction. Thus it does not add a `timeline.json` row or a tick to the shared ordered event list. This avoids the specific R71 harm: R71's `tick: 4` placed its reading report after inherited tick-3 reports even though its excerpt did not say it happened later. As the R71 reviewer and adjudicator explain, a disclaimer cannot undo the ordering encoded by that integer; changing it to 3 or an earlier tick would still imply an unsupported relative position. The checker requires each timeline row to have an integer tick and checks dependency ordering, but does not require every entity claim to have a timeline event. R43 already has cited entity claims without a corresponding event for each claim.

This removes the identified *timeline-position* implication; it does not prove the proposed prose or JSON is free of every temporal implication. No event is a useful boundary, not a semantic validator.

## Residual calibration checks

The inherited Vela excerpt itself says she stood on the east steps and heard the bell “during Bell-7,” identified as a sole seventh-watch ringing on a stated year-12 date. Its map expressly treats that as Vela's fictional source claim, not authenticated chronology or proof of a shared occasion. Accordingly, a new reading report must not borrow that Bell-7/date as the slate-reading time merely because it is another Vela claim or is appended near the inherited claim. Avoid wording such as “then,” “after,” “at the same time,” “during Bell-7,” a date, or “contemporaneous” unless the new fictional report itself makes the attribution and uncertainty explicit; even then, it would be a fictional timing claim, not authenticated chronology. Appending an entity claim does not itself establish sequence.

For authorship, the R71 candidate and reviews provide a useful boundary: Vela may report a tentative inference about cramped lettering or a possible hurried maker, but must not convert that inference into who wrote the words, a verified maker identity, or an objective fact. Explicitly saying she did not see/know the writer would help. A source title or reliability note identifying this as a newly authored fictional, unverified Vela account likewise attributes the account; it does not authenticate the slate or its writer. The declared plan's phrase “tentative maker inference” is appropriately bounded in concept, but no exact r72 excerpt/source/claim is available to check whether its wording preserves that boundary.

## Judgment and limits

**Calibration: the declared no-timeline design avoids the R71 tick-order harm. No hidden chronology or authorship implication is apparent in the declaration itself**, which specifies no event/tick and frames maker inference as tentative. This is conditional, not candidate approval: actual text could still smuggle in a Bell-7/date relation, chronology, or maker assertion, and the entity-claim row plus clause map must be checked against exact source wording. Coverage is not assessed as improved here; the checker can establish structure/citations, not semantic support, authentication, chronology, authorship, or canon. No conclusion is made about source truth, canon, rights, or mechanics.
