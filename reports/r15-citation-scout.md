# Round 15 citation scout — Sella follow-up

Scope: source-text-to-assertion mapping for the declared round-15 move. This is a scout report, not an authored fixture or evidence that the proposed follow-up exists. I inspected the active r10 fixture and the round-15 declaration; no r15 fixture was present at inspection time.

## Raw observations

- `.shokunin/lore/LOG.md`, Round 15 declaration: active `corpus/fixtures/r10-registry-witness/` has Sella’s first-bell excerpt; she reports leaving the destination blank and keeping the carbon. The declaration says there is no later observation of the carbon and no claim about a mark or its origin.
- `corpus/fixtures/r10-registry-witness/registrar-copy-excerpt.md` is headed “Fictional source excerpt — invented fixture text (not recovered evidence).” It says: “At first bell at Lantern Harbor, I, Sella, registrar there, recorded seeing Mira leave. At Mira’s request, I left the registry destination blank and kept the carbon.” It contains no later look, mark, or origin claim.
- `corpus/fixtures/r10-registry-witness/timeline.json` has `registry-entry` at tick 1 and `arrival` at tick 2. The registry-entry description cites `registrar-copy` and says Sella kept the carbon. `first bell` in the prose does not itself establish a numeric time.
- `corpus/fixtures/r10-registry-witness/sources.json` describes `registrar-copy` as invented in-world text with bounded reliability; the excerpt is a report by Sella, not omniscient truth.
- The declaration calls for a separate fictional micro-bible preserving the r10 rows and adding a later Sella follow-up at Lantern Harbor: a blurred blue oval mark, origin unidentified, specifically not attributed to Mira’s Blue Seal. That is a planned change, not an observed artifact/result.

## Proposed exact follow-up wording and mapping

Suggested newly authored excerpt (under a new source ID, explicitly labeled invented/not recovered):

> Later, at Lantern Harbor, I looked again at the carbon I had kept. I saw a blurred blue oval mark on it. I cannot identify where the mark came from, and I do not attribute it to Mira’s Blue Seal.

| Clause in proposed note | Bounded assertion it can support in the fixture | Not supported / boundary |
|---|---|---|
| “Later, at Lantern Harbor, I looked again at the carbon I had kept.” | Sella reports a later second look at the same carbon she says she kept in `registrar-copy`; the report locates this observation at Lantern Harbor. | Does not verify the first-bell numeric time, the carbon’s custody independently, or the objective truth of her account. “Later” must be reflected by a tick greater than prior events; do not infer a conversion from first bell. |
| “I saw a blurred blue oval mark on it.” | Sella reports observing a mark on the carbon, with the stated appearance. A matching new event may describe this reported observation. | Does not establish who made it, when it was made/appeared, its meaning, whether anyone else saw it, or whether the mark objectively exists beyond the authored account. |
| “I cannot identify where the mark came from” | Sella reports that the origin is unidentified to her. | Not proof that its origin is unknowable or that no origin can be inferred by others. |
| “I do not attribute it to Mira’s Blue Seal.” | The authored account makes no attribution of the mark to Mira’s Blue Seal; retain this as an explicit limit. | Does not establish that the Blue Seal did not cause, leave, or relate to the mark. Do not label it a seal mark or Mira’s mark. |

## Implementation/review recommendations (not raw observations)

- Use a distinct source ID for this follow-up, with metadata identifying it as newly authored fictional text, not recovered evidence. Do not alter `registrar-copy` or retroactively place the follow-up in the original excerpt.
- Match each event description only to the reported observation (Sella looks again at the kept carbon and reports the mark); avoid making the event text assert objective mark origin or a Blue Seal connection. Cite the new event to the new source ID.
- For chronology, choose a tick strictly later than the active maximum tick (currently 2) and make the follow-up depend on `registry-entry` if the schema permits. This expresses later-than the keeping event without making “first bell” a numeric conversion; do not imply it is after `arrival` unless dependency/order explicitly says so.
- A clean checker run can establish structural validity/source-ID resolution only. A non-author clause review can establish wording traceability, not source truth or independent corroboration. Keep these conclusions separate.
