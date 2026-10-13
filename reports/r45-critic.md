# Round 45 critic — faction occupancy exemption

## Verdict: NO-GO on the proposed faction exemption

The motivating premise is plausible but not established by this model. A faction may maintain distributed outposts, but that does not mean a timeline row's faction `entity_id` denotes the collective's distributed presence rather than a singular representative, unit, or attributed event subject. The newly authored in-world report would only assert the interpretation it was written to assert; it cannot independently authenticate the ontology or make the fixture a calibration oracle. Therefore skipping occupancy whenever `kind == "faction"` risks suppressing a legitimate same-tick contradiction, including records whose faction subject is intended as a singular actor. The character double-booking control protects only characters; it does not bound this loss for factions.

## Evidence (path:line)

- `.shokunin/lore/LOG.md:754-756`: r45 itself calls distributed faction events a hypothesis, not a rule; proposed evidence is a newly authored report and a paired character control. The proposal explicitly acknowledges uncertainty about singular location semantics.
- `.shokunin/lore/corpus/fixtures/check_bible.py:228-252`: occupancy is keyed by `(entity_id, tick)` and compares distinct valid places after unique actor resolution; no kind distinction is made. A faction exemption would remove this check for every faction row, not just the proposed outpost example.
- `.shokunin/lore/corpus/fixtures/README.md:29-34`: the stated rule is specifically that a **character** cannot occupy different places; simultaneous same-place records are allowed. This grounds character double-booking, not an exemption for every non-character kind.
- `.shokunin/lore/corpus/fixtures/README.md:19-27`: faction is an explicit entity kind in the alliance convention, but that convention says nothing about faction presence or occupancy semantics.
- `.shokunin/lore/corpus/knowledge/2026-10-12-lore-decision-table.md:25-36`: faction-kind checks support a specific alliance rule, and explicitly do not establish faction ontology beyond `kind` or semantic truth.
- `.shokunin/lore/corpus/fixtures/README.md:256-265, 279-287`: prior occupancy rules frame outcomes as definite same-actor inference under ID assumptions, not source truth; unique citations resolve source identity only. This reinforces that a fictional source excerpt cannot certify a general kind-level exception.
- `.shokunin/lore/LOG.md:750-752`: immediately preceding actor-kind proposal was rejected because generic actor IDs and the character-specific prose did not justify universal semantics. Round 45's faction exemption has the symmetric risk: kind alone does not prove distributed presence.

## Narrower alternative

Do not change occupancy behavior by entity kind. Keep the existing same-ID/same-tick/different-place diagnostic and allow an explicitly documented, case-specific editorial interpretation outside the checker (for example, mark the apparent conflict as unresolved when the source actually describes concurrent outposts). If a future input-level exception is needed, require an explicit schema field or relation that represents distributed presence, with a defined validation contract; do not infer it from `kind=faction` or prose/source citation alone. No such field/contract is evidenced here, so this alternative is a future design direction, not an implementation recommendation for this round.

## Falsifiable gate

**GO only if** independent, pre-existing project evidence (not a round-authored source or checker output) establishes that faction-subject timeline events denote the collective's location/presence and that simultaneous distinct-place rows for that subject are valid; and a paired control demonstrates the proposed exemption does not suppress a legitimate faction double-booking case under that same contract. Retain the character conflict diagnostic. **NO-GO** if support is only an invented report, if the meaning of faction rows remains ambiguous, or if any valid singular-faction occupancy conflict loses its finding. Current evidence meets NO-GO conditions; recommend no implementation, fixture admission, or claim of calibration improvement.
