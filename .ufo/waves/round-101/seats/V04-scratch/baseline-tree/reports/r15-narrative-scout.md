# Round 15 narrative scout — carbon mark and uncertain origin

## Scope

Narrative assessment of the declared proposed detail for a separate fictional micro-bible: Sella later examines the carbon she kept and notes a blurred blue oval mark whose origin she cannot identify, without attributing it to Mira’s Blue Seal. This is an assessment of the proposal, not a claim that a new fixture or excerpt exists.

## Raw observations

- In the active `.shokunin/lore/corpus/fixtures/r10-registry-witness/registrar-copy-excerpt.md`, the invented fictional excerpt says: “At first bell at Lantern Harbor, I, Sella, registrar there, recorded seeing Mira leave. At Mira’s request, I left the registry destination blank and kept the carbon.”
- The active `timeline.json` has a `registry-entry` at tick 1, sourced to `registrar-copy`, whose description repeats that Sella saw Mira leave, left the destination blank, and kept the carbon. Its wording says “At first bell”; it does not establish a conversion from first bell to numeric tick 1.
- The active source/entity rows identify a Blue Seal accompanying Mira and a `carries` relation sourced to `courier-log`. The registrar excerpt does not say the seal was at the registry or on the carbon.
- The active registrar excerpt and timeline entry contain no later inspection, colored mark, or account of a mark’s origin. The excerpt is explicitly invented fixture text, not recovered evidence.
- The declared proposed follow-up adds a later observation: a blurred blue oval on that retained carbon, with Sella unable to identify its origin and explicitly not identifying it as Mira’s Blue Seal. Those clauses are proposed additions, not present-file observations.

## Assessment and recommendations (not raw observations)

This is a **specific story detail rather than retrospective restatement**, if implemented as declared. The extant account ends with a particular retained object and a deliberately blank public destination; a later, visibly imperfect mark on that same object gives the blank record a physical trace and gives Sella a bounded new observation. Neither the mark’s shape/color nor Sella’s uncertainty merely paraphrases the existing entry. The uncertainty has narrative content: the trace is observable, but its maker or cause is not. That can deepen the story without resolving the omission or inventing evidence for Mira’s destination.

The blue color creates a tempting connection to the Blue Seal, but resemblance alone is not provenance. Preserve the explicit uncertainty and non-attribution. Do not imply that the seal touched the carbon, that Mira made the mark, or that the mark proves a hidden destination, tampering, or a particular chronology. The detail is more than decorative only insofar as it remains attached to the kept carbon and the missing destination; avoid adding unsupported interpretation around it.

For implementation, make the follow-up a distinct later event with a source ID that matches its short, explicitly authored fictional note. Keep “first bell” as written rather than converting it into a verified numeric time; any event ordering should be represented as fixture ordering/dependency, not as a newly proven historical clock reading. A non-author reader should be able to point to clauses for (1) Sella looking again at the retained carbon, (2) the blurred blue oval, and (3) her inability to identify its origin and refusal to identify it as the Blue Seal. If any of those clauses are absent or the added prose only repeats the blank-entry passage, the proposed depth gain is not established.

This narrative judgment does not establish the fictional account as true, independent corroboration, checker support for prose semantics, or real-world/game-mechanics facts. It recommends a plausible bounded addition; final depth admission still depends on the declared clean checker, clause review, and baseline replay/hash evidence.
