# Round 49 critic — same-carbon handoff falsification

## Verdict: NO-GO for the proposed provenance chain; conditional GO only for a carefully attributed narrative report without claiming chain validation

The proposal has a plausible distinct story beat—Sella says she handed the retained carbon to Jorin—but source wording and the current schema do not justify representing an actual transfer/recipient as fact. A newly authored Sella note can report her claimed handoff; it cannot authenticate transfer or Jorin's receipt. The chain would likely make the semantic claim stronger than its evidence. If the round needs a depth gain dependent on a recorded chain, reject rather than treat structural CLEAN as support.

## Evidence and falsification

- LOG explicitly describes the proposed identity/handoff and limits Jorin to a source-claimed recipient: `.shokunin/lore/LOG.md:827-828`. This is a candidate, not evidence that the note exists or transfer occurred.
- The original fictional registrar excerpt says Sella “kept the carbon,” but identifies neither a later transfer nor the sheet by persistent identifier: `.shokunin/lore/corpus/fixtures/r10-registry-witness/registrar-copy-excerpt.md:1-5` (especially line 5).
- R15 Sella's authored follow-up says “the carbon I had kept” and reports a blurred blue oval mark of unknown origin; it does not mention Jorin, transfer, or a unique carbon identifier: `.shokunin/lore/corpus/fixtures/r15-carbon-followup/sella-carbon-followup-excerpt.md:1-5` (especially line 5). The r15 timeline reports the same bounded observation and its dependency only on registry-entry: `.shokunin/lore/corpus/fixtures/r15-carbon-followup/timeline.json:13-21`.
- The r6 valid chain describes an initial acquisition and later explicit holder transfers. Its source citations are accepted by ID; the checker does not inspect source text: `.shokunin/lore/corpus/fixtures/README.md:98-103,110-119`. In particular, local ticks are not automatically linked to timeline events, holder IDs need not imply legal ownership, and a citation does not prove a transfer (`README.md:114-119`).
- The schema's example chain is for the unrelated `seal` item and uses archive-ledger citations for the harbor/tower transitions: `.shokunin/lore/corpus/fixtures/item-chain-valid/entities.json:38-62`. Reusing its shape for carbon can pass structural holder-chain checks while failing the substantive question: does Sella's note identify this same physical carbon and attest actual transfer to Jorin?

Falsifiers: (1) If the proposed note says only “I handed a carbon to Jorin,” the identity link to Sella's previously kept carbon is unsupported absent explicit referential wording. (2) If it says “the carbon I kept” but says she left it for/with Jorin, this supports Sella's report of an intended or attempted handoff, not proof Jorin received it. (3) If a provenance row records `to_holder: jorin`, readers can reasonably interpret that as a completed transfer, while the only warranted conclusion is that Sella authored that report. (4) A distinct Jorin acknowledgment would still be a fictional, source-claimed account, not authentication or independent real-world evidence; absent that, do not imply recipient receipt. (5) The blue oval is not identified as Mira's Blue Seal, and this handoff supplies no bridge to it.

## Novelty / distinct depth

R6 already demonstrates item holder chains as mechanics; r10 reports initial retention; r15 adds a later inspection and unresolved mark. A reported transfer to a named person could add a new relational development, not merely another file/voice, **if** the source clearly states that Sella reports handing the same retained carbon to Jorin. But generic provenance rows or a source-ID citation do not add verified custody history. Any gain is a bounded narrative claim of Sella's reported action, not the chain's objective state. Distinct depth is therefore **unproven as proposed**; no-go for a provenance-chain assertion. A prose-only observation may be worth testing, conditional on exact clause mapping and a non-author rejecting any inference of receipt, authentication, oval-mark identity, chronology beyond local ordering, canon, or rights.

## Axis assessment and testable gate

- **Depth:** not established for an asserted same-carbon transfer/recipient chain; conditionally testable only as Sella's attributed report of a claimed handoff.
- **Coverage:** unchanged by the candidate; no checker/schema capability is implicated.
- **Calibration:** unchanged only if claims stay explicitly attributed and uncertain. It is harmed if provenance notation upgrades report to verified transfer/receipt or links oval to seal.

**Go** only if a non-author can map the exact newly authored clause to every new row and concludes it supports no more than “Sella reports handing the same carbon to Jorin”; any chain must be clearly interpreted as a representation of that report, not authenticated custody. Otherwise **no-go**: omit the chain or reject the candidate. Preserve all baseline outputs/JSON and checker; a CLEAN result is structural only. The note must remain labeled newly authored fictional material, not recovered evidence. Do not claim canon or real-world reuse rights.
