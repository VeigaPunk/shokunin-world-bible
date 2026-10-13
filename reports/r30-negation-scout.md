# Round 30 negation scout report

## Evidence and semantics

- The r28 excerpt says “I, Mira, carried the blue seal” (`.shokunin/lore/corpus/fixtures/r28-courier-excerpt/courier-log-excerpt.md:3`). Its map calls “carried” the lexical basis for `type=carries`, while treating name-to-ID mapping as editorial (`.shokunin/lore/corpus/fixtures/r28-courier-excerpt/relation-clause-map.md:9,13`).
- The r29 clause is “The blue seal was near Mira” (`.shokunin/lore/corpus/fixtures/r29-near-miss/courier-log-excerpt.md:3`). Its map labels `relations[0].type=carries` unsupported—not contradicted or false—because proximity says neither that she carried nor did not carry it (`.shokunin/lore/corpus/fixtures/r29-near-miss/negative-clause-map.md:9`).
- Round 28 closure admits only a narrow clause map and says it does not support other JSON claims or canon (`.shokunin/lore/LOG.md:438-441`); round 29 closure admits an explicit negative-control interpretation without relation falsity or canon (`.shokunin/lore/LOG.md:455-457`).

## Negation distinction and temporal caveat

For the proposed r30 sentence “I, Mira, did not carry the blue seal,” the explicit negation denies the carrying event in that constructed clause. Conditional on the fixture-local editorial identity alignments, this is a textual conflict with the unchanged positive `relations[0].type=carries` claim—not merely unsupported evidence as in r29. It is not a finding that the relation is canonically false, nor a resolution of the JSON record: the fixture juxtaposes a prose assertion and a record claim, and the checker does not read Markdown. The existing r28/r29 maps already warn that checker output is structural only (`relation-clause-map.md:17`; `negative-clause-map.md:15`).

Temporal caveat: “did not carry” negates the described event in the clause’s temporal scope; absent a specified interval or exhaustive-time claim, it does not establish that Mira never carried the seal, that no carrying occurred at another time, or that the relation is globally false. Explicit negation is at most a local textual conflict, never canon falsity.

## Risk and falsifiable check

**Risk:** treating a locally negated clause as global negation would overstate its time scope and convert a prose/record mismatch into canon adjudication; conflating it with r29 would also erase the meaningful distinction between unsupported proximity and explicit contrary wording.

**Check:** keep the five JSON tables and selected relation byte-identical to r28/r29; create only the fictional explicit-negation clause/map, with editorial ID alignment stated as conditional. A non-author reviewer must classify r28 “carried” as lexical support, r29 “near” as unsupported, and r30 “did not carry” as local textual conflict (not false/canon-resolving), and must reject any inference of “never” beyond the clause’s unstated temporal scope. Falsify this calibration claim if the reviewer accepts the temporal/global overreach, fails to distinguish r29 from r30, or treats a clean structural checker result as validating prose or canon.
