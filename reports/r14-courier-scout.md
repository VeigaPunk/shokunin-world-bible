# Round 14 courier excerpt scout

## Observed baseline (facts about the files)

- `.shokunin/lore/corpus/fixtures/r10-registry-witness/sources.json` defines source ID `courier-log` as “Courier Mira’s Route Log, year 12,” a fictional personal log, and labels it an in-world first-person account. Its metadata row does not itself supply excerpt wording.
- In `.../entities.json`, `mira` has first appearance `courier-log` and claim “Mira carried the blue seal.” `seal` has first appearance `courier-log` and claim “The seal accompanied Mira.”
- `.../relations.json` has `mira` → `seal`, type `carries`, source `courier-log`.
- `.../timeline.json` has `departure` (tick 1, Mira, harbor; “Mira departs the harbor.”) and `arrival` (tick 2, Mira, tower; “Mira reaches the tower.”), both sourced to `courier-log`. The corresponding entity names in `.../entities.json` are Lantern Harbor and North Tower.
- These are observed fixture assertions and metadata only; they do not establish real-world events or verify the fictional account. `.../registrar-copy-excerpt.md` is separate invented fixture text and does not provide courier-log wording.

## Bounded proposed excerpt (recommendation; not written to the fixture)

> **Fictional source excerpt — newly authored fixture text, not recovered evidence**  
> Source ID: `courier-log`  
>  
> At tick 1, I left Lantern Harbor. I carried the blue seal with me. At tick 2, I reached North Tower.

## Proposed source-to-assertion map (recommendation)

| Existing row / assertion | Phrase in proposed excerpt | Scope |
|---|---|---|
| `entities.json`: `mira.first_appearance = courier-log` | Source ID plus “I”; source title identifies this as Mira’s log | Fictional attribution only; not proof of the narrator’s identity |
| `entities.json`: Mira claim “Mira carried the blue seal”; `relations.json`: `mira` carries `seal` | “I carried the blue seal with me.” | Covers carry/accompaniment, without adding custody before departure or after arrival |
| `entities.json`: `seal.first_appearance = courier-log` | “the blue seal” | Names the item as already identified by the existing row; no origin or provenance claim |
| `timeline.json`: `departure`, tick 1, Mira at harbor | “At tick 1, I left Lantern Harbor.” | Covers the stated departure endpoint; no route between endpoints is invented |
| `timeline.json`: `arrival`, tick 2, Mira at tower | “At tick 2, I reached North Tower.” | Covers the stated arrival endpoint; no claim about how or when between ticks |

The relevant raw files are `.shokunin/lore/corpus/fixtures/r10-registry-witness/entities.json`, `relations.json`, `timeline.json`, and `sources.json` (all under that fixture directory); the separate excerpt observed was `.shokunin/lore/corpus/fixtures/r10-registry-witness/registrar-copy-excerpt.md`.

This is a drafting recommendation for a new fictional excerpt, not a report that the excerpt exists or that its sentences are true. It deliberately does not claim a direct route, intermediate stops, seal ownership/origin, an exact clock time, or independent corroboration. The checker cannot infer prose-to-row support from this proposal.
