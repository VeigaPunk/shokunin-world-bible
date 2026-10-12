# Round 15 scribe — bounded source-to-claim / README draft

Scope: documentation proposal only, based on the round-15 LOG declaration and the currently active `r10-registry-witness` fixture. This report does not author or assert that the proposed round-15 fixture exists. It does not establish source-text truth, canon truth, or game mechanics.

## Raw observations (as inspected)

- The LOG declares the active r10 baseline has Sella’s first-bell excerpt: she left a registry destination blank and kept the carbon. It expressly says there is no later observation of that carbon and no claim about a mark or its origin.
- In active `r10-registry-witness/registrar-copy-excerpt.md`, the invented excerpt says: “At first bell at Lantern Harbor, I, Sella, registrar there, recorded seeing Mira leave. At Mira’s request, I left the registry destination blank and kept the carbon.” Its header calls it fictional fixture text, not recovered evidence.
- The active r10 timeline has `registry-entry` at tick 1, with the description about first bell, the blank destination, and keeping the carbon, cited to `registrar-copy`. The prose’s “first bell” alone does not numerically establish tick 1; the LOG also warns against converting first bell to verified numeric time.
- The r10 `sources.json` labels `registrar-copy` as invented in-world text and notes its bounded reliability. The active excerpt does not mention a blue mark, blurred or otherwise, nor attribute anything to the Blue Seal.
- The LOG’s round-15 proposal is a *separate* fictional micro-bible preserving r10 rows and adding one later cited Sella follow-up event and short authored note: Sella looks again at the kept carbon at Lantern Harbor and records a blurred blue oval mark, with its origin unidentified, explicitly not attributing it to Mira’s Blue Seal. This is a declared proposal, not an observed result.

## Proposed source-to-claim table (for the proposed new fixture)

| Source / evidence | Proposed bounded statement | Claim mapping / permitted reading | Not established |
|---|---|---|---|
| Existing `registrar-copy` excerpt (invented) | Sella reports seeing Mira leave at first bell; leaves the destination blank at Mira’s request and keeps the carbon. | Existing r10 registry-entry description / Sella’s report. | Numeric tick from “first bell”; actual destination; truth or independence of Sella’s report. |
| Proposed new follow-up source ID (use the exact ID chosen in the fixture) and newly authored note | Sella later looks again at the carbon she kept, at Lantern Harbor; she records a blurred blue oval mark. | A new follow-up event at the chosen local tick, with dependency on `registry-entry` only if its tick is strictly later; claim narrowly limited to Sella’s later observation/report. The prose, event description and source ID must agree clause-for-clause. | Mark’s cause, author, age, meaning, whether it was present earlier, or relation to Mira/the seal. |
| Same proposed follow-up note | Sella cannot identify the mark’s origin and does not attribute it to Mira’s Blue Seal. | Explicitly preserves uncertainty; report the absence of attribution as a boundary on this authored account. | That the seal did not cause it; that the mark is or is not the Blue Seal; corroboration or objective source truth. |

The follow-up source should be labeled explicitly as newly authored fictional in-world text, not recovered evidence. Keep the new event’s tick/dependency consistent with actual fixture rows; do not infer a numeric first-bell conversion. Preserve every existing r10 JSON row. If the new source is not independently witnessed, do not call it corroboration.

## README wording proposal (conditional on implementation and review)

> ### Round 15: a later look at Sella’s carbon (separate fictional fixture)
>
> This separate micro-bible preserves the r10 rows and adds a later, explicitly authored fictional follow-up: Sella says she looked again at the carbon she kept and recorded a blurred blue oval mark whose origin she could not identify. The account does **not** attribute the mark to Mira’s Blue Seal. It does not establish who made the mark, when it appeared, or what it means. The follow-up is newly authored fixture text, not recovered evidence or independent corroboration. Its event/source citation records the fixture’s assertion; compare the wording with the cited note manually. The checker validates structure and source-ID resolution only; it does not read the prose or verify the account. “First bell” in the earlier excerpt is not converted into a verified numeric time.

Before including this wording, replace “separate micro-bible” with the implemented fixture path, confirm the exact source ID and event tick/dependency, and have a non-author verify every table row against the final raw artifacts. If no implementation exists, keep this README paragraph as a draft, not active fixture documentation.

## Documentation guardrails

- Distinguish raw fixture observations from the proposed authored follow-up; do not describe proposal as completed evidence.
- Say “Sella reports/records” rather than asserting the mark objectively exists.
- “Origin unidentified” means unidentified in the account, not proof that origin is unknowable.
- The blue color/oval shape is not evidence of a Blue Seal connection. Do not use “seal mark,” “Mira’s mark,” or causal phrasing.
- A clean checker result would establish structural validity and source-ID resolution only, not clause support or source truth. Manual clause review is traceability, not independent corroboration.
