# Round 49 source scout — bounded same-carbon handoff wording

## Finding

Conditional narrative proposal only: Sella may report that she handed the retained carbon to Jorin. First-person wording can support *Sella’s account of an action*, not Jorin’s receipt. Do not include a receipt confirmation, identify the blurred oval, or treat the document as authentication. This would add a reported custody transition beyond r10’s keeping and r15’s later inspection, but whether that is material depth remains for independent review; r6 provenance mechanics are not themselves narrative evidence.

## Proposed exact excerpt (newly authored fictional note; not recovered)

> I, Sella, mean the carbon I kept after Mira’s departure—the same carbon I looked at again later at Lantern Harbor, where I saw the blurred blue oval mark. I handed that carbon to Jorin, the registrar at Lantern Harbor. This is my account of handing it to him; I did not witness what he did with it afterward.

The last sentence deliberately stops short of Jorin acknowledging receipt. “The same carbon” is Sella’s asserted identity link between the retained sheet and the sheet she says she handed over, not an externally verified object identity. “Jorin, the registrar” is only Sella’s in-world identification; it does not authenticate his identity or office. The prior note’s unknown-origin oval remains unknown and is not assigned to any person or seal.

## Evidence and exact bounds

- `.shokunin/lore/LOG.md:827-828` defines the candidate as Sella’s first-person handoff of “the carbon I kept after Mira’s departure” to named registrar Jorin, expressly excluding objective receipt, mark attribution, destination, canon and rights. The wording above retains those limits.
- `.shokunin/lore/corpus/fixtures/r10-registry-witness/registrar-copy-excerpt.md:1-5` labels the text invented, and line 5 says Sella recorded Mira’s departure, left the registry destination blank at Mira’s request, and kept the carbon. This supports what that fictional excerpt reports, not actual departure, destination, or later chain of custody.
- `.shokunin/lore/corpus/fixtures/r15-carbon-followup/sella-carbon-followup-excerpt.md:1-5` labels the note newly authored fiction (not recovered); line 5 reports Sella later looking again at “the carbon I had kept,” seeing a blurred blue oval, not identifying its origin, and not attributing it to Mira’s Blue Seal. It supplies the first-person antecedent for a same-carbon assertion, but does not report a handoff or recipient.
- `.shokunin/lore/reports/r6-provenance-scout.md` (“Recommendation”) proposes an optional item `provenance` list with `{tick, from_holder, to_holder, source_id}` and explicitly distinguishes initial holding from later transfer. That is a recommendation, not evidence that any transfer occurred; the proposed wording must not be stretched into receipt or an objective chain.
- `.shokunin/lore/corpus/fixtures/r10-registry-witness/sources.json:11-17` describes `registrar-copy` as invented and limited to Sella’s report, not omniscient truth or Mira’s destination. Citation IDs link claims to authored sources; they do not authenticate them.

## Source-to-claim map and risks

| Exact phrase | Narrowly supportable interpretation | Must not claim |
|---|---|---|
| “I, Sella” | Note attributes the account to a fictional first-person speaker | Actual authorship, verified identity, independent witness |
| “the carbon I kept after Mira’s departure” | Sella refers back to her own r10-reported retention and labels it the same item | Independently established identity of a physical carbon; actual departure or destination |
| “looked at again later … saw the blurred blue oval mark” | Summary of the bounded r15 account, with unknown origin preserved | Mark maker, timing, authenticity, or identity with Mira’s Blue Seal |
| “I handed that carbon to Jorin” | Sella reports an act of handing to a person she identifies as Jorin | Jorin’s acknowledgment, receipt, possession afterward, or subsequent custody |
| “the registrar at Lantern Harbor” | Sella’s in-world description of Jorin | Verified office/identity or institutional authentication |
| “I did not witness what he did with it afterward” | Explicit limit on Sella’s observation | Any claim that Jorin retained, inspected, altered, or confirmed receipt of it |

Do not make a provenance chain say Jorin is an established holder if the record schema’s `to_holder` means actual receipt/possession rather than reported handoff. At most, represent the action as a Sella-attributed event with its new note citation; omit provenance rows if their holder semantics outrun the text. Never backfill an “acquisition” as fact. Keep the r10 and r15 source texts unchanged. No oval-mark identity, receipt, destination, clock conversion, canon, or real-world rights inference follows.

## Falsifiable go/no-go and distinct depth assessment

**Go only conditionally** if a distinct new Sella note can be cited and mapped clause-by-clause, and a non-author reviewer agrees it adds a meaningful reported custody action beyond (a) r10’s account of keeping the carbon and (b) r15’s account of looking again at it. Reviewer must be able to answer “no” to whether the text/rows establish Jorin’s receipt, possession after the handoff, oval-mark origin, Blue Seal identity, or actual transfer independent of Sella’s report. If any structured row encodes an unqualified transfer/holder change or receipt, the mapping fails: omit that representation or reject. If the reviewer judges the handoff sentence merely another unsubstantiated assertion or insufficiently distinct depth, no-go; do not count added rows, source files, or r6-style schema mechanics as depth.

**Distinct depth assessment:** Potential narrow depth gain is a new *reported custody transition* following the prior retained-carbon and inspection accounts. It is distinct in narrative function from r6’s generic data model and r10/r15’s retention/inspection, but the only proposed evidence is newly authored Sella narration, not independent corroboration. Depth therefore remains unproven until non-author review; coverage and calibration should remain unchanged. Checker cleanliness, if later measured, would only establish structure/reference integrity, not text truth or receipt.
