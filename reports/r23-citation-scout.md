# Round 23 citation scout — witnessed-absence note class

Scope: bound citation and canon claims for a **witnessed absence** note (a named speaker reports that a named thing was not present). This is a scout report only. It is not an authored fixture, not recovered evidence, and not a clause map of source prose. Baseline HEAD lacks `.shokunin/lore/corpus/fixtures/r23-note-class`. This class is distinct from round-15 mark observation (`sella-carbon-followup`: report of a blurred blue oval mark, origin unidentified, not attributed to Mira’s Blue Seal).

Checker `check_bible.py` validates schema, citations, relations, and timeline structure. It does **not** map source prose. Source-text truth is unverified. No canon claim follows from a green checker run.

## Reliability stance (from r15 pattern / PROVINCE)

PROVINCE refuses claiming canon without an in-world citation and refuses silently resolving contradictions. Fixture `sources.json` reliability notes (r15 pattern) treat private-note and register excerpts as invented in-world fiction: a speaker reports their own observation, not omniscient truth.

For a witnessed-absence note the same bounds apply, tightened to negation:

| Fixture field / practice | Bound meaning | Not meaning |
|---|---|---|
| `sources[].id` | Fixture identity string used by `source_id` links inside this micro-bible | Recovered archival ID, external evidence handle, or proof of provenance |
| Speaker reports absence (“I did not see X” / “X was not there”) | The authored text records that **report** | Proof that X was absent in-world as objective fact; proof X never existed; proof others would agree |
| `first_appearance` on entities | Index into which **fixture source id** first mentions the entity in this pack | Historical first appearance in a living world, publication order, or out-of-fixture chronology |
| Timeline `tick` / `depends_on` | Ordering inside the fixture graph | Calendar time, conversion from “first bell,” or game-clock mechanics |
| Event `description` citing the absence note | Paraphrase of the **reported** non-observation | Omniscient narration that the thing was absent |
| Green `check_bible.py` | Structural validity and ID resolution | Source-prose truth, canon lock, or contradiction resolution |

## What a witnessed-absence note may support

Bounded assertions only:

1. Named speaker **S** states, in the authored excerpt under source id **N**, that named thing **T** was not present (or not seen by S) at the situation the note describes.
2. Fixture rows may repeat that **report** with `source_id: N`, without upgrading it to world fact.
3. Explicit non-links already used elsewhere (e.g. r15 “do not attribute to Mira’s Blue Seal”) remain limits on **attribution language**, not proofs of non-causation.

## What it must not claim

- That absence-as-reported is absence-as-fact in the world bible.
- Blue Seal attribution, seal-mark identity, or Mira-authorship of any mark or gap (r15 already forbade Blue Seal attribution for the oval mark; do not smuggle it back via “absence of seal” wording).
- Chronology claims beyond fixture ticks/dependencies (no “after arrival,” no “before first bell” as history).
- Game-mechanics claims (detection rules, fog of war, inventory, quest flags).
- Restatement of existing r14/r15 rows as “new depth.”
- That `first_appearance` or source id constitutes recovered evidence.

## Forbidden phrasings (citation / canon surface)

Do not use these (or close paraphrases) in fixture claims, event descriptions, reliability notes, or round reports when describing witnessed absence:

- “canon”, “canonical”, “established fact”, “confirmed absent”, “proves that … was not there”
- “objectively missing”, “in fact gone”, “truly absent”, “never present”, “did not exist”
- “recovered evidence”, “primary source find”, “archival discovery”, “real excerpt”
- “first appeared historically”, “debut in the world”, “original introduction” (for `first_appearance`)
- “Blue Seal mark”, “Mira’s seal caused”, “attributed to the Blue Seal”, “seal-verified absence”
- “quest flag”, “mechanic”, “RNG”, “aggro”, “fog of war revealed”
- “therefore X never …”, “so we know X was …”, “omniscient record shows”
- “checker verified the story”, “schema proves the lore”
- Framing r15 mark text as this note class, or this class as proof about the mark’s origin

## Implementation/review recommendations (not observations)

- Label any new excerpt “fictional / invented fixture text (not recovered evidence)” and give it a **new** source id; do not overload `sella-carbon-followup` or `registrar-copy`.
- Map claims 1:1 to speaker-report wording; prefer “Sella reports that … was not …” over “… was not …”.
- Keep `first_appearance` values equal to fixture source ids only; document that index nature in reliability_note if touched.
- Separate structural checker results from any human clause-trace; neither is canon.

## Out of scope this scout

Authoring `r23-note-class` fixtures, editing checker/LOG/SCORECARD, commits, Blue Seal lore expansion, and chronology invention.
