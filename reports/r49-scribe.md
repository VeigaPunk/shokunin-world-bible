# Round 49 scribe — clause/source/provenance map

## Evidence and mapping (manual; checker does not read this)

| Clause / assertion | Source and exact support | Fixture representation | Boundary |
|---|---|---|---|
| “I, Sella, registrar there, recorded seeing Mira leave” | `corpus/fixtures/r10-registry-witness/registrar-copy-excerpt.md:5` | `r10-registry-witness/relations.json:10-14` (`sella` → `mira`, `records_departure`, `registrar-copy`); `timeline.json:34-40` records Sella’s report | Supports what this invented Sella text says she recorded/saw, not independently established departure. |
| “At Mira’s request, I left the registry destination blank and kept the carbon.” | `registrar-copy-excerpt.md:5` | `r10-registry-witness/timeline.json:34-40` | Sella’s report supports retained carbon at this point; does not provide object serial/unique identifier. |
| “Later … I looked again at the carbon I had kept.” | `r15-carbon-followup/sella-carbon-followup-excerpt.md:5` | `r15-carbon-followup/timeline.json:42-48` (`carbon-followup`, source `sella-carbon-followup`) | Linguistically connects this note’s “the carbon” to Sella’s earlier kept carbon, as her report; does not authenticate continuity of physical object. |
| Blurred blue oval; origin unknown; not attributed to Mira’s Blue Seal | `sella-carbon-followup-excerpt.md:5` | `r15-carbon-followup/timeline.json:42-48` | Explicitly disclaims identity with Blue Seal. Color/shape do not establish mark identity. |
| Proposed later handoff to Jorin | No existing clause in r10/r15 says handoff, transfer, Jorin, receipt, or when it occurred. | No currently supported mapping. | A newly authored Sella sentence could create only a fictional *report of a handoff*. It cannot authenticate actual transfer, Jorin’s receipt, or when/how it happened. |
| Optional item provenance chain | `corpus/fixtures/item-chain-valid/entities.json:43-64` shows item-local records `{tick, from_holder, to_holder, source_id}`; `item-chain-broken/entities.json:43-64` illustrates predecessor mismatch | The convention is structural; r10/r15 do not assert a transfer. | Schema acceptance and linked holder IDs do not establish clause entailment or real custody. Existing item model cannot turn a reported assertion into verified fact. |

## Falsifiable support test / go-no-go

**Go only** if the new authored note contains an explicit, unambiguous first-person clause identifying the transferred object as “the carbon I kept” (or equally explicit anaphora to Sella’s r10 carbon), names the handoff to Jorin as Sella’s reported act, and the proposed item/provenance fields cite that exact note. A non-author must quote-map each field and confirm that the source distinguishes *Sella says she handed it over* from *Jorin actually received it*. Keep time as an ordinal/local tick only when the note supports ordering; do not invent a calendar time. The check is falsifiable: remove the explicit same-carbon anaphora or handoff verb and the item identity/transfer row loses support; weaken the prose to “a carbon” and identity is no-go.

**No-go** for any claim that the note authenticates actual transfer, receipt by Jorin, oval-mark identity, canon, or real-world rights. No-go also if provenance implies those claims as fact rather than recording a source-attributed assertion. A newly authored note repeating the proposed detail is not independent corroboration. Without this explicit wording and independent clause-to-field review, omit the item/provenance chain; clean checker status is not evidence of support.

## Axis assessment (distinct)

- **Depth: not yet demonstrated / conditional.** A first-person Sella account of passing the retained carbon to a named registrar could add a connected custodial beat beyond r10’s retention and r15’s later observation, but only as authored narrative attribution. With the proposed material still absent, this report cannot call depth improved; mere schema rows or a self-authored note repeating the premise add no evidential depth.
- **Coverage: unchanged.** No checker or fixture rule is evaluated here; r6 already covers structural item-chain consistency. A new source-specific example is not a new coverage class.
- **Calibration: unchanged.** The boundary is explicit, but no before/after prediction or independent validation yet demonstrates improved calibration.

No fixture/checker/README/LOG edits made. No statement here authenticates transfer, recipient, oval mark, canon, or rights.
