# Round 83 fixture scout — candidate and preservation map

## Candidate: isolated Vela excerpt near-miss (proposal only)

The smallest plausible source fixture is a new sibling cloned from `.shokunin/lore/corpus/fixtures/r40-vela-listener/` (call it `r83-vela-negation-scope` if admitted). It already contains the exact first-person Vela sentence and all five required JSON tables. Keep the r40 control untouched. The only intended source-prose delta in the candidate is:

- Control, `vela-note-excerpt.md`: `I did not see Sella or an envelope.`
- Candidate: `I did not see Sella with an envelope.`

Keep the preceding sentence byte-for-byte: `I, Vela, stood on the Lantern Harbor east steps and heard two strokes I took to be the registry bell during Bell-7, the sole seventh-watch registry-bell sounding on the seventh day of Embermonth, year 12.` Do not alter punctuation or any other excerpt words. This exact mutation changes a reported non-sighting of each item (ordinary “or” reading) into a non-sighting of the joint scene/person-object configuration. It does **not** license saying Vela saw Sella separately, saw an envelope separately, or that either was actually present/absent. The useful editorial consequence, if a non-author confirms the contrast, is to withhold or qualify the JSON wording that says Vela reported not seeing Sella **or** an envelope: the candidate prose alone does not support an envelope-alone non-sighting. If readers find “or” itself scope-ambiguous, or no meaningful repair difference, this is not a demonstrated calibration gain.

## Five JSON tables to inherit exactly

Copy these from r40 unchanged, byte-for-byte, including formatting, row order, all inherited records, and all pointers:

1. `sources.json` — `vela-note` remains the source ID; its unverified fictional attribution note remains unchanged.
2. `entities.json` — preserve all rows. In the appended `vela` character row, retain `first_appearance: "vela-note"`, the claim statement `Vela reports hearing two strokes she took to be the registry bell during Bell-7 and reports not seeing Sella or an envelope.`, and `source_id: "vela-note"` exactly. This is the structured assertion whose envelope-alone scope may need qualification against the changed excerpt.
3. `relations.json` — unchanged, including its sole Mira/seal row.
4. `timeline.json` — preserve all rows. In `vela-listening-report`, retain actor `vela`, place `harbor`, tick `3`, `depends_on: []`, source `vela-note`, and description `Vela reports hearing two strokes she took to be the registry bell during Bell-7; she reports that she did not see Sella or an envelope.` exactly. This event description repeats the broad non-sighting.
5. `contradictions.json` — unchanged, retaining the inherited unresolved `bell7-location-reports` record and pointers to `tarin-envelope-observation` and `sella-bell7-presence`.

The relevant preexisting source pointers are therefore the Vela claim and event to `vela-note`; do not add, remove, or redirect any source/entity/event/ledger pointer. The event's `tick: 3` is only the fixture-local sequence label. No new relation, contradiction, event, or factual absence assertion is justified by this mutation.

The existing `vela-clause-map.md` quotes the old sentence and maps “I did not see Sella or an envelope.” A cloned candidate must not leave that quotation stale: in the candidate copy, update only the quoted excerpt and its clause-map row to accurately identify the joint-scope wording and its limit. Otherwise keep inherited prose/maps byte-identical. The five JSON tables remain exact; excerpt/map are the only proposed authored-text delta needed for a usable paired fixture. Preserve the original r40 control and all source-pointer structure.

## Bounds and no-edit status

Both versions are expected to pass the existing checker structurally because it reads the five JSON tables, not the Markdown excerpt or clause map. That would establish only schema and resolvable ID structure, not prose entailment. The excerpt and attribution are newly authored fiction, not authenticated source material. This comparison cannot establish fictional-world truth or canon, real-world source authenticity or rights, game mechanics, objective presence/absence, a Bell-7 occurrence, or a shared occasion. It does not extend checker behavior. This is a fixture-scout proposal, not an admission or implementation; no corpus, checker, config, LOG, or other file was edited.
