# r88-m3 Maya cluster: claim-to-excerpt map

Scope: 10 source-attributed in-world JSON facts (4 `first_appearance` pointers, 4 entity claims, and 2 timeline events), plus 2 separate Spence comparison rows. Every JSON fact and editorial row has an exact anchor and repeats the R9 mode.

## Inventory

**Expected inventory:** 10 JSON facts; 2 editorial rows; 12 total mapped rows; 8 distinct excerpt anchors.

## R9 excerpt declarations

| Excerpt | Source / reference | Delivery mode | Status |
|---|---|---|---|
| `fictional-excerpts.md:7–8` | `veil-verse` | `verbatim` | Newly authored fictional verse; no JSON fact points to this source. |
| `fictional-excerpts.md:12–13` | `paired-clock` | `verbatim` | Newly authored fictional register; all ten JSON facts below point to this source. |
| `source-excerpt.md:5` | Lewis Spence, *The Myths of Mexico & Peru* (1913), English prose | `verbatim` | Delivered in-tree, verbatim from Spence's English prose; external comparison, not an in-world source. The underlying K'iche primary text is not reproduced (`external-only`). |

## JSON facts (10 source-attributed rows)

The `source_id` for each fact resolves to `paired-clock` in `sources.json`. Anchors are lexical preflight only; review the whole claim and its scope, not just a matching phrase.

| ID | JSON fact and fields | `source_id` | Excerpt path:line | R9 mode | Exact anchor |
|---|---|---|---|---|---|
| P1 | `entities[0].first_appearance` (Aru) | `paired-clock` | `fictional-excerpts.md:12` | `verbatim` | `Aru carried the north lantern at Quiet Rise` |
| P3 | `entities[2].first_appearance` (Quiet Rise) | `paired-clock` | `fictional-excerpts.md:12` | `verbatim` | `Aru carried the north lantern at Quiet Rise` |
| P4 | `entities[3].first_appearance` (Salt Court) | `paired-clock` | `fictional-excerpts.md:13` | `verbatim` | `Evin held the south bell at Salt Court` |
| E1 | `entities[0].claims[0]`: Aru carries the north lantern at Quiet Rise at tick 9 | `paired-clock` | `fictional-excerpts.md:12` | `verbatim` | `Tick 9: Aru carried the north lantern at Quiet Rise.` |
| E2 | `entities[1].claims[0]`: Evin holds the south bell at Salt Court at tick 9 | `paired-clock` | `fictional-excerpts.md:13` | `verbatim` | `Tick 9: Evin held the south bell at Salt Court.` |
| E3 | `entities[2].claims[0]`: the register locates Aru's north-lantern entry at Quiet Rise | `paired-clock` | `fictional-excerpts.md:12` | `verbatim` | `north lantern at Quiet Rise` |
| E4 | `entities[3].claims[0]`: the register locates Evin's south-bell entry at Salt Court | `paired-clock` | `fictional-excerpts.md:13` | `verbatim` | `south bell at Salt Court` |
| T1 | `timeline[0]` (`description`, `source_id`): Aru carries the north lantern at Quiet Rise | `paired-clock` | `fictional-excerpts.md:12` | `verbatim` | `Tick 9: Aru carried the north lantern at Quiet Rise.` |
| T2 | `timeline[1]` (`description`, `source_id`): Evin holds the south bell at Salt Court | `paired-clock` | `fictional-excerpts.md:13` | `verbatim` | `Tick 9: Evin held the south bell at Salt Court.` |

## Editorial rows (2 Spence comparisons; not extra JSON facts)

Each cited clause is located in the delivered Spence English prose at `source-excerpt.md:5` (`verbatim`); each authored comparison is in `fictional-excerpts.md` (`verbatim`). The underlying K'iche primary text is not reproduced (`external-only`). These are bounded editorial readings, not claims about K'iche symbolism or extra in-world canon.

| ID | Editorial comparison | Excerpt path:line | R9 mode | Exact anchor |
|---|---|---|---|---|
| S1 | `symbolism-clause-map.md:7`: `He called out “Earth,”` → `We leave its name unowned in the rain.` | `source-excerpt.md:5` | `verbatim` | `He called out “Earth,”` |
| S2 | `symbolism-clause-map.md:8`: `and the solid land appeared.` → `The chalk stair stays a crossing, never a map.` | `source-excerpt.md:5` | `verbatim` | `and the solid land appeared.` |

## Scope and review notes

- The ten JSON facts are four first-appearance pointers, four entity claims, and two timeline events. The two editorial rows index the Spence clauses cited by the symbolism comparisons; they are not in-world JSON facts. `relations.json` and `contradictions.json` are empty; `veil-verse` has no source-attributed JSON fact.
- The delivered English passage at `source-excerpt.md:5` is verbatim of Spence's English prose (R9 mode: `verbatim`). `external-only` applies to the underlying K'iche primary text, which is not reproduced here. The Spence passage remains an external comparison, not an in-world `source_id` or a mapped in-world JSON source.
- `check_bible.py` checks structure and source-ID resolution, not excerpt support or R9 delivery modes; a clean run is not a claim-support receipt.
