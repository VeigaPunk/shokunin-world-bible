# Round 35 independent verifier — Bell-7 paired reports

## Scope and baseline replay

Baseline report commit: `0b2f4166377622aad45e86cd2204e765b7829e0c`. I enumerated its fixture tree with `git ls-tree -r`: 86 fixture directories and 429 JSON paths. I extracted the baseline with `git archive`, extracted the baseline checker with it, and replayed the same root-relative argv against both extracted baseline and current trees: `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture-dir>`. Compared `(returncode, raw stdout bytes, raw stderr bytes)` for every fixture. **86/86 exact matches.** Compared all 429 baseline JSON files byte-for-byte against current paths: **429/429 unchanged.**

A preliminary attempt reported 85/86: it used absolute checker/script paths for the extracted tree while comparing to relative paths in the working tree. The only mismatch was `r5-missing-file`, whose diagnostic embeds the path spelling (absolute versus relative). This was a test-harness argv/cwd artifact, not a fixture behavior regression; rerunning both sides with the same relative argv and corresponding repository-root cwd yielded exact 86/86 as above.

## Final r35 checker

Ran the documented command against the corrected final fixture:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r35-bell7-conflict
```

Exit **0**; stdout exactly `CLEAN: schema, citations, relations, timeline; 0 violations
`; stderr empty.

## r35 versus r33 JSON

Fixture pair: `r33-tarin-envelope/` → `r35-bell7-conflict/`.

- `relations.json`: byte-identical.
- `sources.json`: adds one `sella-bell7-note` source, described as a newly authored fictional first-person North Tower note, not omniscient truth.
- `entities.json`: one inherited Sella-attributed claim statement is minimally occasion-qualified; it remains attributed to Tarin and sourced to `tarin-note`. It says Tarin reports the placement during Bell-7, now identified as the sole seventh-watch registry-bell sounding on seventh day of Embermonth, year 12.
- `timeline.json`: inherited Tarin observation event description receives the same occasion/date qualification; a single `sella-bell7-presence` event is added (`entity_id=sella`, `place_id=tower`, `tick=3`, source `sella-bell7-note`) reporting Sella's claimed presence throughout that same ringing and absence from Harbor.
- `contradictions.json`: changes from `[]` to one ledger entry, `bell7-location-reports`, with `place_id` pointers to `tarin-envelope-observation` and `sella-bell7-presence`. Its rationale explicitly conditions the apparent conflict on the names/place IDs and the reports' same sole ringing/date; it clarifies Tarin's Harbor pointer is the scene of his reported sighting, not a claim that Tarin is Sella or a Sella-actor location event.

The first submitted version failed the non-author review: both notes said “on the day of this note,” so their dates did not independently establish the same occasion. The executor remediated both excerpts to name the same specific fictional date—seventh day of Embermonth, year 12—and updated the maps/ledger rationale to match. The corrected final artifacts were checked above; the earlier fail remains an important review finding, not a passing result. The exact date and unique ringing remain claims within fictional notes, not authenticated chronology.

## What validation does and does not establish

The checker exit 0 establishes schema and pointer/citation consistency only. It does **not** validate that two pointers encode semantic incompatibility, that the event actors/places align with real identities or locations, that the shared date or unique ringing is externally true, or that either source is reliable. The asserted report-level conflict is conditional on identity/place alignment and both accounts referring to the same uniquely described occasion. Both accounts remain unresolved; no winner, source truth, or canon is inferred. Equal local tick 3 is not a conversion to Bell-7. No envelope contents, owner, recipient, motive, or Blue Seal/carbon/route-strip relationship is established.
