# Round 28 source scout — fictional courier-log boundaries

## Located boundary

- `.shokunin/lore/corpus/fixtures/consistent/sources.json:9-12` identifies `courier-log` as “Courier Mira’s Route Log, year 12,” a fictional personal log; the reliability note explicitly says it is a first-person account.
- `.shokunin/lore/corpus/fixtures/consistent/relations.json:2-7` asserts only the structured `mira` → `seal` `carries` relation and cites `courier-log`. This is the target record, not source text.
- `.shokunin/lore/corpus/fixtures/consistent/entities.json:7-11` gives Mira’s claim “Mira carried the blue seal”; `:39-47` gives the seal claim “The seal accompanied Mira.” These are additional structured assertions, not an excerpt or independent corroboration.
- `.shokunin/lore/corpus/fixtures/consistent/timeline.json:1-23` cites the same source for departure/arrival events; it does not supply a quoted courier-log passage.
- `.shokunin/lore/corpus/fixtures/README.md:36-41` distinguishes in-world `source_id` citations from the real-world reference ledger and says entries are invented for the fixture. `.shokunin/lore/corpus/knowledge/reference-ledger.md:1-10` is expressly real-world method references, not fictional canon.
- Round 28’s declaration in `.shokunin/lore/LOG.md` records the prior `git ls-tree ... | grep excerpt` search as empty. Therefore there is no located committed courier-log excerpt to map clause-by-clause; only its fictional metadata and downstream assertions are present.

## Risks / limits

A source ID establishes a reference link, not source-text support, truth, or corroboration. Repeating the asserted content in entity claims cannot independently validate the relation. The source metadata describes a first-person log with an explicit limited-reliability note, so avoid upgrading an observation into omniscient or canon truth. Do not claim anything about any real source: the proposed prose is a constructed fictional excerpt only. Keep the proposed map limited to the one selected relation and mark unsupported implications out of scope.

## Proposed falsifiable check

For a separate fictional fixture, have a human reviewer trace each mapped subclaim for only `mira` → `seal` `carries` to an exact clause in the newly constructed excerpt. Record clause text/location and the corresponding structured record fields; flag any added implication (identity certainty, time/place, ownership, exclusive possession, or broader canon) as out of scope unless directly entailed. Falsify the mapping if any asserted component lacks a supporting clause or if a clause is paraphrased to add meaning. Separately verify the fixture checker’s structural exit and byte/stdio regression baseline; neither result should be presented as automated proof of prose entailment.
