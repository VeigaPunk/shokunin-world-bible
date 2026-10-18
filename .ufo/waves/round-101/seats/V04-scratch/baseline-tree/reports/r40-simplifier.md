# Round 40 simplifier — minimum auditory account

## Minimal fixture and rows

Use a separate fixture copied from `.shokunin/lore/corpus/fixtures/r35-bell7-conflict/` (baseline files: `sources.json`, `entities.json`, `relations.json`, `timeline.json`, `contradictions.json`, two excerpts and maps). Preserve all inherited bytes. The existing conflict is explicitly attributed: Tarin’s excerpt reports seeing Sella place an envelope during Bell-7 (`.shokunin/lore/corpus/fixtures/r35-bell7-conflict/tarin-note-excerpt.md:1`); Sella’s excerpt reports her presence at Tower and absence from Harbor during that same ringing (`.../sella-bell7-note-excerpt.md:1`). These are reported claims, not established events.

Add one fictional Vela source row and its separate short excerpt; one Vela entity row with a sourced report claim only if needed to represent the speaker; one timeline event for Vela at `harbor`, local tick 3, with actor `vela`, source ID matching the new note, and no dependency on either existing event. Minimal excerpt: “I, Vela, stood on the Lantern Harbor east steps and heard two strokes I took to be the registry bell during Bell-7, the sole seventh-watch registry-bell sounding on the seventh day of Embermonth, year 12. I did not see Sella or an envelope.” Mirror only those statements in the event description. Add a brief manual clause map linking the hearing, Vela’s tentative identification, occasion label, and non-sighting to the prose; it is editorial, not machine verification. Do not alter existing rows, excerpts, ledger, maps, checker, or README. No new contradiction-ledger row is warranted: Vela does not report a competing place for Sella.

Path evidence: existing source/event pattern and actor/place attribution are visible in `.shokunin/lore/corpus/fixtures/r35-bell7-conflict/sources.json:1-` and `timeline.json:17-36`; the two existing excerpts and their event text provide the Bell-7 phrase (`tarin-note-excerpt.md:1`, `sella-bell7-note-excerpt.md:1`, `timeline.json:17-36`). The precise line spans may shift if formatting changes; keep evidence anchored to these file rows.

## Risks and limits

The only plausible depth delta is a third, distinct sensory account plus an explicit limit on what Vela did not see. This may still be arbitrary added detail rather than useful narrative depth; a new name/source alone is not a gain. “I took [the strokes] to be the registry bell” is Vela’s interpretation only. Do not claim an objective bell, identify its cause, authenticate Bell-7, reconcile timeline ticks, or treat Vela as corroborating or disproving either other report. Vela’s failure to see Sella or an envelope is not proof of their absence. Other reports remain attributed and conditional; no claim about their truth or canon follows. A structurally clean checker result establishes neither excerpt support nor world truth.

## Falsifiable check

A non-author must map each new Vela claim to the exact excerpt and confirm the source/event IDs resolve, actor/place match, and inherited r35 files remain byte-identical. They must find no wording that upgrades Vela’s interpretation into an objective bell or turns non-sighting into proof of absence; they must also state that the added account neither corroborates nor contradicts the other reports. If the excerpt does not explicitly support any event claim, if any inherited file changes, or if reviewers cannot identify a distinct useful sensory/report detail beyond gratuitous accumulation, reject the depth claim. Run the existing checker for structural consistency only; exit 0 is not evidence of prose truth or canon.

Scope: report only; no fixture, checker, README, LOG, or commit changes.
