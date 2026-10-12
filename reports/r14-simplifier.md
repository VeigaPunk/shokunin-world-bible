# Round 14 simplifier — excerpt minimum and manual map

## Observed baseline (raw paths)

- `.shokunin/lore/corpus/fixtures/r10-registry-witness/entities.json` has five entity rows: `mira`, `harbor`, `tower`, `seal`, and `sella`, with the first-appearance and claim statements listed below.
- `relations.json` has `mira carries seal` sourced to `courier-log`, and `sella records_departure mira` sourced to `registrar-copy`.
- `timeline.json` has `departure` and `arrival` attributed to `courier-log`, plus `registry-entry` attributed to `registrar-copy`.
- `sources.json` lists `archive-ledger`, `courier-log`, and `registrar-copy`. Only `registrar-copy-excerpt.md` currently supplies excerpt prose. It says Sella records seeing Mira leave, leaves the destination blank at Mira's request, and keeps the carbon. The two other source IDs currently have metadata, not supplied source wording.

These are observations of the fixture's rows and text, not claims about any real or independently recovered source. `check_bible.py` checks structural/source-ID consistency; it does not establish prose-to-claim support.

## Minimal proposed additions (recommendations, not existing facts)

If the declared round-14 edit proceeds, add only the following clearly marked fictional fixture text at `courier-log-excerpt.md` and `archive-ledger-excerpt.md`. These are proposed lines, not observed source text or independent corroboration.

`courier-log-excerpt.md`:
> Year 12, route note: I, Mira, left Lantern Harbor at tick 1 carrying the blue seal. At tick 2 I reached North Tower.

`archive-ledger-excerpt.md`:
> Year 12, registry and watch-bell ledger: Lantern Harbor has a registry. North Tower has a watch bell.

The proposed text is deliberately limited to claims already present in the JSON. It does not identify Sella as author/witness of either source, fill the registry's blank destination, or resolve the route by appeal to independent corroboration.

## Complete manual source-to-assertion map

“Supported” below means the proposed/observed wording contains a direct textual match for the JSON assertion. It does not mean the assertion is true in-world, nor that separate sources independently corroborate it. `registrar-copy` wording is observed; the two proposed excerpts above are recommendations only.

| JSON row / assertion (raw file) | Source ID | Exact relevant wording | Assessment |
|---|---|---|---|
| `mira`: first appearance (entities.json) | `courier-log` | Proposed: “I, Mira, left Lantern Harbor at tick 1” | Directly names Mira and the departure; first-appearance is a fixture organizational label, not proof of her literal first appearance in the world. |
| `mira` claim “Mira carried the blue seal.” (entities.json) | `courier-log` | Proposed: “I, Mira, … carrying the blue seal.” | Direct match. |
| `harbor`: first appearance (entities.json) | `archive-ledger` | Proposed: “Lantern Harbor has a registry.” | Names the place; does not establish that this is the place's first historical appearance. |
| `harbor` claim “Lantern Harbor has a registry.” (entities.json) | `archive-ledger` | Proposed: “Lantern Harbor has a registry.” | Direct match. |
| `tower`: first appearance (entities.json) | `archive-ledger` | Proposed: “North Tower has a watch bell.” | Names the place; does not establish that this is the place's first historical appearance. |
| `tower` claim “North Tower has a watch bell.” (entities.json) | `archive-ledger` | Proposed: “North Tower has a watch bell.” | Direct match. |
| `seal`: first appearance (entities.json) | `courier-log` | Proposed: “carrying the blue seal.” | Names the item; does not establish its first historical appearance. |
| `seal` claim “The seal accompanied Mira.” (entities.json) | `courier-log` | Proposed: “I, Mira, … carrying the blue seal.” | Direct textual support for Mira carrying the seal; does not imply later custody or provenance. |
| `sella`: first appearance (entities.json) | `registrar-copy` | Observed: “I, Sella, registrar there” | Names Sella. “First appearance” remains a fixture label, not a historical completeness claim. |
| `sella` claim “Sella is a registrar at Lantern Harbor.” (entities.json) | `registrar-copy` | Observed: “At first bell at Lantern Harbor, I, Sella, registrar there…” | Direct match. |
| relation `mira` `carries` `seal` (relations.json) | `courier-log` | Proposed: “I, Mira, … carrying the blue seal.” | Directly supports the stated relation in this bounded passage. |
| relation `sella` `records_departure` `mira` (relations.json) | `registrar-copy` | Observed: “I, Sella, … recorded seeing Mira leave.” | Direct support for Sella recording a departure observation. |
| event `departure`: Mira, tick 1, Lantern Harbor; “Mira departs the harbor.” (timeline.json) | `courier-log` | Proposed: “left Lantern Harbor at tick 1” | Direct match for place, tick, and departure wording. |
| event `arrival`: Mira, tick 2, North Tower; “Mira reaches the tower.” (timeline.json) | `courier-log` | Proposed: “At tick 2 I reached North Tower.” | Direct match for place, tick, and arrival wording. |
| event `registry-entry`: Sella, tick 1, Lantern Harbor; description records seeing Mira leave, leaves destination blank at Mira's request, keeps carbon (timeline.json) | `registrar-copy` | Observed: “At first bell at Lantern Harbor, I, Sella, registrar there, recorded seeing Mira leave. At Mira’s request, I left the registry destination blank and kept the carbon.” | Direct support for the described acts and place. The row's tick value `1` is only supported if the fixture equates “first bell” to tick 1; no such tick mapping is stated in this excerpt. Avoid claiming full support for that numeric tick absent a stated convention. |

### Boundary / minimality note

The `registry-entry` row combines prose details that its excerpt states with a numeric tick that the excerpt does not explicitly equate to `1`; preserve that distinction in any integrated map, or recommend an explicitly fictional “first bell (tick 1)” wording if the intended fixture convention permits it. Do not silently infer the tick equivalence. No other entity/relation/event JSON row is omitted from the map. The map is a manual editorial aid, not a checker result.
