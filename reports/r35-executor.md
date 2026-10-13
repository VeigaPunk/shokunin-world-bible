.shokunin/lore/corpus/fixtures/r35-bell7-conflict/

# Round 35 executor — Bell-7 paired reports

## Work and checker result

Cloned `r33-tarin-envelope/` to `r35-bell7-conflict/`. Added `sella-bell7-note` and its fictional first-person excerpt; added event `sella-bell7-presence` for actor `sella`, place `tower`, tick 3, cited to that source. Tarin's excerpt now explicitly places the reported sighting during Bell-7, defined in both excerpts as the sole seventh-watch registry-bell sounding on the seventh day of Embermonth, year 12; the date and sole-ringing status are fictional source claims, not authenticated chronology. The inherited Sella-attributed Tarin claim retains its original “Tarin reports that Sella placed...” wording and receives only the Bell-7 occasion append; the Tarin timeline description receives the same occasion append. Updated inherited `clause-map.md` now traces the full Bell-7 excerpt, with explicit tick/clock limits. All remaining inherited JSON rows were retained.

Exact checker command (repository root):

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r35-bell7-conflict
```

Exact result: exit **0**; stdout `CLEAN: schema, citations, relations, timeline; 0 violations
`; stderr empty.

## Manual map and interpretation boundary

`manual-clause-pointer-map.md` traces each added or amended clause to its excerpt/record, both ledger pointers, and limits. `contradictions.json` points Tarin event `tarin-envelope-observation.place_id` and Sella event `sella-bell7-presence.place_id`. Its rationale says why an apparent location conflict follows only if the speaker/place ID alignments and shared unique ringing are assumed. Crucially, Tarin's Harbor `place_id` is the scene of Tarin's observation report, not a claim that Tarin himself is Sella or the Sella location side of the dispute. Sella's event is explicitly her own reported location.

Both excerpts identify Bell-7 as one single ringing. Tarin reports the placement during it; Sella reports being physically at North Tower throughout it and not at Lantern Harbor at any point. Bell-7 is not a clock/tick conversion: the inherited/equal tick 3 is only an editorial local sequence value. Reports remain attributed and unresolved. Checker exit 0 is structural only and does not prove semantic incompatibility, source-text support, either account's truth, or canon. No envelope contents, ownership, recipient, motive, or Blue Seal/carbon/route-strip connection is asserted.

## JSON diff from r33

Exact unified diff of the four changed JSON files (`sources.json`, `entities.json`, `timeline.json`, `contradictions.json`); unlisted inherited JSON tables/files are byte-identical:

```diff
--- r33/sources.json
+++ r35/sources.json
@@ -16,5 +16,11 @@
     "title": "Tarin’s harbor note, year 12",
     "kind": "fictional first-person note",
     "reliability_note": "Newly authored fictional excerpt; reports Tarin’s observation, not omniscient truth."
+  },
+  {
+    "id": "sella-bell7-note",
+    "title": "Sella’s North Tower note, year 12",
+    "kind": "fictional first-person note",
+    "reliability_note": "Newly authored fictional account; reports Sella’s claimed presence, not omniscient truth."
   }
 ]

--- r33/entities.json
+++ r35/entities.json
@@ -66,7 +66,7 @@
     "first_appearance": "tarin-note",
     "claims": [
       {
-        "statement": "Tarin reports that Sella placed an unlabeled paper envelope on the Lantern Harbor registry desk.",
+        "statement": "Tarin reports that Sella placed an unlabeled paper envelope on the Lantern Harbor registry desk during Bell-7, the sole seventh-watch registry-bell sounding on the seventh day of Embermonth, year 12.",
         "source_id": "tarin-note"
       }
     ]

--- r33/timeline.json
+++ r35/timeline.json
@@ -25,7 +25,16 @@
     "entity_id": "tarin",
     "place_id": "harbor",
     "depends_on": [],
-    "description": "Tarin reports seeing Sella place an unlabeled paper envelope on the Lantern Harbor registry desk.",
+    "description": "Tarin reports seeing Sella place an unlabeled paper envelope on the Lantern Harbor registry desk during Bell-7, the sole seventh-watch registry-bell sounding on the seventh day of Embermonth, year 12.",
     "source_id": "tarin-note"
+  },
+  {
+    "id": "sella-bell7-presence",
+    "tick": 3,
+    "entity_id": "sella",
+    "place_id": "tower",
+    "depends_on": [],
+    "description": "Sella reports she was physically at North Tower throughout that same Bell-7 ringing and was not at Lantern Harbor at any point during it; Bell-7 is the sole seventh-watch registry-bell sounding on the seventh day of Embermonth, year 12.",
+    "source_id": "sella-bell7-note"
   }
 ]

--- r33/contradictions.json
+++ r35/contradictions.json
@@ -1 +1,14 @@
-[]
+[
+  {
+    "id": "bell7-location-reports",
+    "claim_a": {
+      "event_id": "tarin-envelope-observation",
+      "field": "place_id"
+    },
+    "claim_b": {
+      "event_id": "sella-bell7-presence",
+      "field": "place_id"
+    },
+    "why": "If the names Sella and the place IDs harbor/North Tower align, and both fictional reports refer to the sole Bell-7 ringing on the seventh day of Embermonth, year 12, Tarin reports observing Sella at Lantern Harbor during it, while Sella reports her own physical presence at North Tower throughout it and no presence at Lantern Harbor at any point. The date and sole-ringing description are claims in the fictional notes, not authenticated chronology. Tarin event.place_id records the observation scene for Tarin’s reported sighting; it is not a claim that Tarin himself is Sella or that Tarin’s location is the conflicting Sella location. Both reports are retained unresolved; this is an editorial apparent conflict, not a checker-proven contradiction or a canon verdict."
+  }
+]
```
