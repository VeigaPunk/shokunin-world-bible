# Round 71 narrative scout — Vela/Jorin prose and slate-text limits

## Scope and finding

This is a report-only comparison of the declaration in `.shokunin/lore/LOG.md` (Round 71, 2026-10-13T07:58:34.200125+00:00) with the r43 source excerpts/maps and relevant prior reports. I did not edit fixtures, checker, LOG, or corpus data.

The declaration proposes a Vela first-person report distinguishing what she could read on an east-step registry slate from what she inferred about its maker. I found **no existing slate or maker wording** in the r43 fixture files, nor any matching `slate`/`maker` prose in the corpus files searched. However, the declaration supplies no literal proposed excerpt or quoted slate text. Therefore I can say the *subject* is not a duplication of existing prose, but cannot perform exact phrase-level duplication or entailment review of the proposed text. The new distinction could add a different partial-witness perspective; that alone does not prove material depth gain.

## Existing prose and its scope

- `.shokunin/lore/corpus/fixtures/r43-jorin-vela-sighting/vela-note-excerpt.md` is Vela’s attributed first-person account: she stood on Lantern Harbor’s east steps, heard the registry bell strike twice during her named Bell-7 occasion, and did not see Sella or an envelope. It says nothing about a slate, reading text, or identifying/inferencing its maker.
- `.shokunin/lore/corpus/fixtures/r43-jorin-vela-sighting/vela-clause-map.md` treats this as an unverified source report. It maps east steps only to broad `harbor`, not the registry desk; the Bell-7/date language is not authenticated chronology; and the non-sighting does not establish absence. Its structured character and timeline descriptions are existing attributed summaries, not independent verification.
- `.shokunin/lore/corpus/fixtures/r43-jorin-vela-sighting/jorin-note-excerpt.md` has Jorin at the registry doorway, reporting that he saw Vela on the east steps during what he called Bell-7, and that he did not see who, if anyone, struck a bell. It contains no slate observation and gives no evidence about what Vela read or who made anything.
- `.shokunin/lore/corpus/fixtures/r43-jorin-vela-sighting/jorin-clause-map.md` explicitly limits Jorin’s visual report to Vela’s reported location; it does not establish a shared occasion. It cannot be used to imply that Jorin saw the slate, witnessed Vela reading it, or independently confirms her account.
- `.shokunin/lore/corpus/fixtures/r43-jorin-vela-sighting/strength-contrast-map.md` documents the difference between Vela’s r40 tentative bell identification and r41 direct identification, and warns that the stronger first-person claim is not objective proof. It provides no slate or authorship support.

For comparison, `.shokunin/lore/corpus/fixtures/r40-vela-listener/vela-note-excerpt.md` contains the earlier “two strokes I took to be” wording; `.shokunin/lore/corpus/fixtures/r41-vela-direct-bell/vela-note-excerpt.md` contains the direct bell-identification wording inherited by r43. These are revisions of Vela’s auditory account, not prior slate prose. The `r43-prior-scout.md`, `r43-source-scout.md`, and `r43-reviewer.md` reports likewise describe the bounded location/auditory/non-sighting and Jorin’s conditional location comparison; none supplies a slate episode. The Round 71 declaration itself notes no separately authored contemporaneous Vela response about the slate wording.

## Duplication and overclaim risks

The proposed perspective is distinguishable from existing content **if** it is a new, explicitly attributed report about legible marks/words and Vela’s own inference. It would be duplicative if it merely restates her east-step location, the bell event, Bell-7, or the existing Sella/envelope non-sighting without adding an inspectable slate-reading distinction. Exact judgment awaits the literal excerpt and the exact quoted words.

The proposed distinction can remain calibrated only if the prose separates (a) what Vela says she could read from (b) what she guesses or infers about a maker. A legible name, signature, handwriting, or mark does not itself establish the maker’s identity or authorship. The report must not turn the slate into an authenticated record, prove who wrote it, assign the slate to Jorin/Sella/another person, connect it to the bell or existing envelope/Blue Seal material, establish a verified time or shared occasion, or resolve any inherited disagreement. Nothing in Jorin’s doorway account supports such additions. Vela’s existing line “I did not see Sella or an envelope” limits that stated sighting; it neither proves absence nor forbids a carefully bounded new report, but any apparent tension about what she saw must be represented as her account (not silently harmonized or treated as objective contradiction).

## Checker and citation limits

`.shokunin/lore/corpus/fixtures/check_bible.py` validates JSON shape, source/entity/event references, and selected input dependencies. It does not read excerpts or clause maps and cannot verify that a slate quotation matches a source, that Vela could read it, or that an inference about its maker is warranted. A `source_id` would make an in-world attribution traceable within the fixture, not authenticate the text or its claims. A clause map can make the author’s intended boundaries reviewable but cannot establish them as fact. No factual canon, rights, ownership, or game-mechanics conclusion follows from these materials.

## Scout judgment

**Existing-prose duplication:** no slate/maker content found in the inspected r43 excerpts/maps; the exact new wording is absent from the declaration, so exact duplication remains unassessed. **Depth:** a reading-versus-maker-inference perspective is potentially distinct from Vela’s auditory/non-sighting report and Jorin’s visual location report, but material gain is unproven until literal prose is compared and its rows map without overclaim. **Coverage/calibration:** no improvement claim; preserve explicit attribution and the limits above. This scout does not validate a candidate or make canon claims.
