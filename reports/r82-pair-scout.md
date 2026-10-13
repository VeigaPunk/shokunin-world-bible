# Round 82 pair scout — r35 Tarin/Sella clause and pointer map

## Scope

Read-only map of the fictional r35 Bell-7 pair, its structured source/event/contradiction pointers, the r36 date near-miss, and the r74 slate decision table. This report identifies what the repository text says and where it is represented. It does not determine whether any account is true, whether the fictional sources are authentic, or what is canon.

## r35 exact source clauses

Both fixture excerpts are explicitly newly authored fictional first-person reports (`corpus/fixtures/r35-bell7-conflict/sources.json`, IDs `tarin-note` and `sella-bell7-note`). The excerpts and clause maps are under `corpus/fixtures/r35-bell7-conflict/`.

| Source clause | Fixture-local alignment / structured pointer | Exact scope and limit |
|---|---|---|
| Tarin: “I, Tarin” | `tarin-note-excerpt.md`; entity `entities.json` `/4` (`tarin`); event `timeline.json` `/2` (`tarin-envelope-observation`, `entity_id: tarin`, `source_id: tarin-note`) | First-person reporter. The character ID is an editorial fixture alignment, not independent identity verification. |
| Tarin: “saw” | Same excerpt; `timeline.json` `/2` description, source `tarin-note` | Tarin reports an observation; wording does not independently verify the event. |
| Tarin: “Sella” | Same excerpt; entity `entities.json` `/5` (`sella`) and Sella `claims[0]`, sourced to `tarin-note` | Named person is editorially aligned to `sella`; the claim remains Tarin-attributed, not a first-person statement by Sella. |
| Tarin: “place an unlabeled paper envelope” | Same excerpt; `entities.json` `/5/claims/0`; `timeline.json` `/2` description | Reported placement and an envelope described only as unlabeled paper. No contents, ownership, sender, recipient, or motive is stated. |
| Tarin: “on the Lantern Harbor registry desk” | Same excerpt; place entity `entities.json` `/1` (`harbor`); `timeline.json` `/2` has `place_id: harbor` | The event's Harbor place is the **scene of Tarin's reported observation**. It is not itself an assertion that Tarin is Sella or that Tarin's own whereabouts are the disputed Sella-location claim. |
| Tarin: “during Bell-7, the sole seventh-watch registry-bell sounding on the seventh day of Embermonth, year 12” | Same excerpt; `entities.json` `/5/claims/0`; `timeline.json` `/2` description | A fictional claim identifying the reported occasion and date. It is not authenticated chronology, clock time, or an independent synchronization signal. |
| Sella: “I, Sella” | `sella-bell7-note-excerpt.md`; entity `entities.json` `/5`; event `timeline.json` `/3` (`sella-bell7-presence`, `entity_id: sella`, `source_id: sella-bell7-note`) | Sella's first-person attribution in this fictional account; the fixture alignment/source citation does not authenticate identity or source. |
| Sella: “was physically at North Tower throughout that same Bell-7 ringing” | Same excerpt; place entity `entities.json` `/2` (`tower`); `timeline.json` `/3` has `place_id: tower` | Her account reports Tower presence over the named ringing. “Same” is the source's wording, not external proof that the occasion is shared with Tarin's account. |
| Sella: “was not at Lantern Harbor at any point during it” | Same excerpt; `timeline.json` `/3` description; compare Tarin's Harbor scene at `/2` | Explicit absence claim in Sella's report. The apparent incompatibility depends on linking Tarin's observed person to Sella and aligning the occasions/places. |
| Sella: “Bell-7 is the sole seventh-watch registry-bell sounding on the seventh day of Embermonth, year 12” | Same excerpt; `timeline.json` `/3` description; `contradictions.json` `/0/why` repeats the shared-occasion premise | Fictional date/uniqueness assertion, not authenticated chronology. The excerpt's second paragraph explicitly disclaims authenticated chronology, clock time, and timeline tick. |

The `tick: 3` values on `timeline.json` `/2` and `/3` are local sequence labels. They do not encode Bell-7, the calendar date, exact simultaneity, or synchronized time (`clause-map.md`; `manual-clause-pointer-map.md`). The source rows' `reliability_note` fields likewise label the materials fictional and non-omniscient; a resolving source ID proves structural attribution only, not authenticity, support, honesty, or truth.

## Contradiction ledger pointers

`corpus/fixtures/r35-bell7-conflict/contradictions.json` row `/0` is `bell7-location-reports`:

- `claim_a` → `event_id: tarin-envelope-observation`, `field: place_id` → `timeline.json` `/2`, Harbor observation scene.
- `claim_b` → `event_id: sella-bell7-presence`, `field: place_id` → `timeline.json` `/3`, Sella's reported Tower location.
- `why` conditionally frames the accounts as an apparent incompatible location pair **if** the Sella/person and Harbor/Tower alignments hold and both fictional reports refer to the sole Bell-7 on the stated date. It explicitly distinguishes Tarin's observation scene from a claim about Tarin's own location, retains both accounts unresolved, and says this is not a checker-proven contradiction or canon verdict.

These are structured event-field pointers, not direct quotations or a semantic proof. The checker can validate structure/references; it does not establish that the excerpts support the structured descriptions, the identity/place assumptions, shared occasion, source authenticity, truth, or canon. The manual pointer map is editorial documentation, not a checker guarantee.

## r36 date near-miss and r74 distinction

In `corpus/fixtures/r36-bell7-wrong-date/`, Tarin's excerpt still names the seventh day, but Sella's changed excerpt says the eighth day while retaining “that same Bell-7.” The five JSON files—including Sella's event description and ledger `why`—remain the r35 seventh-day version. `date-contrast-map.md` therefore treats the explicit source dates as failing to establish a shared occasion and flags the inherited structured wording as stale relative to the changed excerpt. This near-miss does not prove either report false or locate Sella on Tarin's day; matching Bell-7 labels or `tick: 3` do not bridge the date difference.

The r74 artifact, `corpus/knowledge/r74-slate-wording-decision-table.md`, concerns fictional Vela/Jorin reports of different slate wording. Its conditional evidence requests distinguish possible separate surfaces, one surface read at unknown times, and inaccurate reporting. It is a decision-table precedent for slate-specific uncertainty, not evidence about Bell-7 and not a solution to the r35 identity/place/occasion questions. Avoid treating its hypotheses or proposed evidence as Bell-7 facts.

## Boundary

Every named note, place, person, bell, registry, and event above is part of the **invented fixture**. Conditional requests for independent evidence would be hypothetical editor questions only; no such corroboration is established here. Nothing in this map authenticates a real-world source, determines fictional canon or truth, grants or assesses rights, or asserts game/story mechanics. No winner is selected and no envelope/Blue Seal/carbon/route-strip link is implied.
