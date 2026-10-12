# Round 15 independent reviewer — carbon follow-up

## Scope and raw replay

Read the round-15 declaration and clarification in `.shokunin/lore/LOG.md`, the active `r10-registry-witness` JSON/excerpt, the separate `r15-carbon-followup` fixture, and the saved raw CLI run records. This is a read-only review; no lore source, fixture, checker, or shared documentation was changed.

Replayed the checker from the repository root using the repo-relative CLI for every one of the 29 active fixture directories. Compared each exact command/exit/stdout record with `corpus/live/runs/20261012T181828Z/<fixture>.txt`: **29/29 matched**, including the old 28. The new fixture exits 0 with `CLEAN: schema, citations, relations, timeline; 0 violations`. This verifies structural checker behavior, not excerpt semantics or truth. In the new fixture, the five inherited JSON files preserve every r10 row: source/entity/relation/timeline inherited prefixes compare equal, and `contradictions.json` is unchanged and empty. The one added source and event are the only rows.

## Clause-level review (verbatim artifact evidence)

The new excerpt labels itself “Fictional private-note excerpt — newly authored for this fixture (not recovered evidence)” and identifies `Source ID: sella-carbon-followup`. Its exact quoted text is:

> Later, at Lantern Harbor, I looked again at the carbon I had kept. I saw a blurred blue oval mark on it. I cannot identify where the mark came from, and I do not attribute it to Mira’s Blue Seal.

The corresponding added `timeline.json` row is `id: carbon-followup`, `tick: 3`, `entity_id: sella`, `place_id: harbor`, `depends_on: ["registry-entry"]`, and `source_id: sella-carbon-followup`. Its exact description: “Sella reports looking again at the carbon she kept and observing a blurred blue oval mark whose origin she cannot identify; she does not attribute it to Mira’s Blue Seal.” The added source metadata calls it a “fictional private note” and says: “Newly authored fictional text for this fixture, not recovered; Sella reports her own later observation and uncertainty, not omniscient truth.”

| Added assertion/clause | Exact support in the cited new note / event | Boundary |
|---|---|---|
| Sella looks again at the carbon she kept | “I looked again at the carbon I had kept”; event says “Sella reports looking again at the carbon she kept.” | One authored first-person report; not independently verified custody, identity, or observation. “Again” links to the r10 excerpt’s “kept the carbon,” but matching scene/text is not corroboration. |
| Location is Lantern Harbor | “Later, at Lantern Harbor”; event `place_id` is `harbor` (entity name “Lantern Harbor”). | Reported location only, not independent location proof. |
| Mark is on the carbon, and is blurred, blue, oval | “I saw a blurred blue oval mark on it”; “it” refers to the carbon in the preceding sentence; event repeats those properties. | Does not establish who made it, when it appeared, whether it was previously present, its significance, or objective existence beyond this fictional account. |
| Origin is unknown to Sella | “I cannot identify where the mark came from”; event says origin she cannot identify. | Her stated epistemic limit, not proof the origin is unknowable to everyone. |
| No attribution to Mira’s Blue Seal | “I do not attribute it to Mira’s Blue Seal”; event repeats the non-attribution. | It is a non-attribution, not an explicit denial of contact, causation, or relation. It does not prove or disprove that the seal made the mark. |
| A later event follows the registry entry | Event is tick 3 and depends on `registry-entry` (tick 1); checker accepts the strict ordering. Note begins “Later”. | Establishes fixture ordering after the registry entry, not a bell/time conversion or elapsed duration. The tick-3 choice is also later than the existing tick-2 `arrival` in the fixture’s ordering, although there is no dependency or causal claim connecting those events. Do not write as though it is after arrival for a story reason or caused by it. |

The original excerpt in r10 says “At first bell at Lantern Harbor, I, Sella, registrar there, recorded seeing Mira leave. At Mira’s request, I left the registry destination blank and kept the carbon.” Neither this wording nor the new note converts “first bell” into a numeric clock time; tick 1 is a fixture value. The new text says “Later” only relative to the earlier kept-carbon account; tick 3 is a local sequencing choice, not proof of a duration. The new source’s “not recovered” label precludes presenting this as found historical evidence.

## Narrative depth and calibration judgment

Unlike the rejected r14 prose, which only rephrased assertions already in the r10 JSON, the new note adds an actual new fictional beat and observation: a second look at a retained object and an imperfect mark with an unresolved origin. It attaches a concrete trace to the existing blank-destination/carbon setup without filling the destination or explaining the mark. That is a bounded, uncertainty-bearing story detail rather than merely a more legible restatement. The claim is narrative depth in the invented micro-bible, **not** evidential support, independent corroboration, source truth, or a checker-validated semantic fact.

There is nevertheless a real associative risk: “blurred blue oval” is placed in the same note that expressly names “Mira’s Blue Seal,” against a fixture where Mira carries that seal. A reader could infer seal provenance despite the words “I do not attribute it.” The text does not state a provenance claim, and the explicit uncertainty/non-attribution materially limits it; however, non-attribution does not erase the suggestive resemblance. Do not call this a seal trace, clue, contact, or evidence about Mira’s route. If future presentation frames the resemblance as an answer or hint, that would exceed the source and harm calibration. On the present raw wording, I judge calibration **unchanged, with a noted implication risk**, rather than harmed: the tempting association is left unresolved, and the assertion itself is calibrated. Coverage is unchanged.

## Independent verdict

- **Depth: improved** — one new bounded observation/event, not r14 restatement; gain is fictional narrative detail only.
- **Calibration: unchanged, watch the implication risk** — attribution and origin remain explicitly unknown; the visual resemblance may still invite an unsupported inference, which must not be promoted.
- **Coverage: unchanged** — no rule class or checker coverage is added.

No structural or clause mismatch found. The “later” event is ordered after the entry; it is not numerically anchored to first bell. The result supports only the narrow declared depth move. Do not claim the blue mark belongs to, came from, or was caused by the Blue Seal. No source edit or commit was made.
