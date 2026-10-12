# Round 15 executor report — carbon follow-up fixture

## Artifacts and structural check

Created only `corpus/fixtures/r15-carbon-followup/` and this report. The fixture contains the five JSON tables copied from `r10-registry-witness/` plus `registrar-copy-excerpt.md` copied byte-identically, and the newly authored `sella-carbon-followup-excerpt.md`. In `sources.json`, appended exactly one source, `sella-carbon-followup`, described as a fictional private note and explicitly newly authored, not recovered. In `timeline.json`, appended exactly one event, `carbon-followup`: Sella (`sella`) at Lantern Harbor (`harbor`), tick 3, depends only on `registry-entry`, cited to `sella-carbon-followup`. All inherited rows remain unchanged; the other three JSON tables are value-identical to r10.

New note, verbatim: “Later, at Lantern Harbor, I looked again at the carbon I had kept. I saw a blurred blue oval mark on it. I cannot identify where the mark came from, and I do not attribute it to Mira’s Blue Seal.” The event description says Sella **reports** looking again and observing the mark, cannot identify its origin, and does not attribute it to Mira’s Blue Seal. It does not assert objective seal-mark identity or causal truth.

CLI: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r15-carbon-followup` exited 0: `CLEAN: schema, citations, relations, timeline; 0 violations`. This confirms structural checks and reference resolution only, not textual entailment, source truth, canon truth, or game mechanics.

## Exact clause map and limits

| Exact excerpt clause | Corresponding event/source assertion | Limits |
|---|---|---|
| “Later, at Lantern Harbor, I looked again at the carbon I had kept.” | `carbon-followup` locates Sella at `harbor` and reports looking again at the carbon she kept; source is `sella-carbon-followup`. Dependency on `registry-entry` supports ordering after the earlier record. | Sella’s authored report only; no independent verification of custody or observation. “Later” is relative sequencing, not elapsed time. Tick 3 is local fixture order, not a first-bell conversion. |
| “I saw a blurred blue oval mark on it.” | Event reports Sella observed a blurred blue oval mark on the carbon. | Does not establish objective fact beyond her report, who made it, when it first appeared, destination, any contact with a seal, or corroboration. |
| “I cannot identify where the mark came from” | Event says she cannot identify the mark’s origin. | Her uncertainty, not proof origin is unknowable or no one could identify it. |
| “I do not attribute it to Mira’s Blue Seal.” | Event explicitly preserves Sella’s non-attribution. | Does not prove or disprove any causal relation. Do not call it a seal mark or Mira’s mark. |

The note and event are one fictional authored account, not independent corroboration. No motive, mark-maker, appearance time, destination, or first-bell-to-tick conversion is asserted. “Blurred blue oval” may invite association with the existing Blue Seal motif; the explicit non-attribution is retained, and the mark is not presented as evidence of that seal.

## Baseline replay and integrity

Replayed all **28** pre-existing fixture CLI cases from repo-relative paths against saved baseline outputs in `corpus/live/runs/20261012T180109Z/`: stdout, stderr, and exit code matched for **28/28**. Old fixtures had 6 exit-0 and 22 exit-1 outcomes. Hashed all 139 old fixture JSON inputs before and after; the sorted path/hash maps matched, manifest SHA-256 `87ee35628b6d81c4a2291abfe21412b18e01ab3eabf529ba28562e55567ec8da`. Checker SHA-256 unchanged: `eaa2f1178c4571d8a911cb3d880068216614766d8f35922cb78d6584179dad80`. The original `registrar-copy-excerpt.md` bytes are identical in the new fixture.

This is executor evidence, not a non-author review or axis verdict.
