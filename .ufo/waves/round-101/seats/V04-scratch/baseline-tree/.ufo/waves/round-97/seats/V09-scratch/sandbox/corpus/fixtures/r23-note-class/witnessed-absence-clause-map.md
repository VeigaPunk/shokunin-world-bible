# Clause map — witnessed absence (manual; checker does not read this file)

Note class: **witnessed absence**. A named speaker reports that a named thing was not present at a named place. This is not the r15 mark observation (a present blurred blue oval, origin unknown, not attributed to Mira’s Blue Seal). Source-text truth is unverified. The checker does not map prose.

Excerpt (`sella-absence-note-excerpt.md`):

> Later at Lantern Harbor, I, Sella, looked for Mira’s outbound route strip on the registry hook rack. I did not find it there.

| clause | fixture field | status |
|---|---|---|
| Later | `timeline[2]` (`strip-absence-note`) tick 3, `depends_on: ["departure"]` | mapped as fixture order only; not a clock fact and not a duration |
| at Lantern Harbor | `timeline[2].place_id` = `harbor` (kind place) | mapped |
| I, Sella | `timeline[2].entity_id` = `sella`; entity `sella` name Sella | mapped as speaker identity in the authored note, not independently established |
| looked for Mira’s outbound route strip on the registry hook rack | `entities[sella].claims[0].statement` and `timeline[2].description` | mapped as the search the speaker reports; the strip is not an entity row |
| I did not find it there | same claim and description | mapped as the witnessed-absence predicate: speaker reports non-finding at that rack |
| (no cause) | none | deliberately unmapped; must-not-imply theft, removal, or motive |
| (no proof of world-absence) | `sources[sella-absence-note].reliability_note` | deliberately unmapped as fact; report ≠ proof the strip was absent |
| (no Blue Seal link) | none | deliberately unmapped; must-not-imply the strip is the seal, a mark, or a carbon |
| (no mark / carbon) | none | deliberately unmapped; this class is not the r15 presence observation |

`first_appearance` on `sella` is the fixture source id `sella-absence-note`. It is an index into this pack, not a historical first appearance.
