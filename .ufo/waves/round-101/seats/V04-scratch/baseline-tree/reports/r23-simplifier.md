# Round 23 simplifier — WITNESSED ABSENCE note class (depth)

## Axes this round
depth (single axis-move), coverage, calibration. This report only names the smallest depth addition.

## Baseline observations (not new depth)
- `HEAD` lacks `.shokunin/lore/corpus/fixtures/r23-note-class` (`git cat-file -e` absence).
- r15 already maps a **presence** private-note class: Sella reports a blurred blue oval mark, origin unknown, not Mira’s Blue Seal (`.shokunin/lore/corpus/fixtures/r15-carbon-followup/`). That is not this class.
- r14 depth that only restated existing rows was rejected. Do not restate r15 mark text or registry-entry wording as new depth.
- `check_bible.py` validates schema, citations, relations, timeline structure. It does **not** map source prose. Source-text truth is unverified. No canon claim.

## Note class (definition)
**WITNESSED ABSENCE:** one named speaker reports that one named thing was **not** present. Clause-by-clause map is new; it is not the r15 mark observation.

## Smallest change that still counts (recommendation only)

One new fixture directory only: `.shokunin/lore/corpus/fixtures/r23-note-class/`.

**Files (minimum):**
1. Copy JSON skeleton from r15 (or r10-registry-witness) so inherited entities/places/relations/sources stay valid for the checker: `entities.json`, `relations.json`, `contradictions.json` (empty array), plus extended `sources.json` and `timeline.json`.
2. One new excerpt file only, e.g. `sella-absence-note-excerpt.md`.
3. No `check_bible.py` edit. No LOG/SCORECARD/other-report edits from this scout. No commit.

**One new source id:** `sella-absence-note`  
- title/kind/reliability_note as fictional private note authored for the fixture (not recovered evidence).

**One new timeline event:** `seal-absence-note`  
- tick after existing r15/r10 ticks (e.g. tick 4 if copying r15’s tick-3 carbon-followup, else tick 3 if copying r10 only); entity `sella`; place `harbor`; `depends_on` the prior Sella registry event only (`registry-entry`); `source_id` `sella-absence-note`.
- description must paraphrase the same four clauses as the excerpt (no extra facts).

**Prose ceiling (excerpt ≤ one short paragraph, ≤ four clauses):**  
> Later at Lantern Harbor, I, Sella, looked for Mira’s Blue Seal on the carbon I had kept. I did not find the Blue Seal there.

Four clauses max: (1) time/place frame, (2) named speaker, (3) named thing sought, (4) reported absence. Optional tighten to three clauses if “I, Sella” merges with the look-for clause—still one speaker, one named absent thing.

**JSON copies:** add only the one source row and one timeline row above; leave every inherited entity/relation/claim untouched. No new entity, no new relation type, no new claim statements on Mira/seal/Sella beyond what inheritance already has.

## What NOT to add
- No second witness.
- No cause, motive, theft, removal, or timing of when the seal left.
- No new place.
- No seal identification of any mark; do not mention the r15 blue oval.
- No assertion that the seal is destroyed, elsewhere, or never existed—only that **this speaker did not find that named thing on the carbon**.
- No checker change, no second excerpt, no second event, no contradiction ledger row “resolving” presence vs absence.

## Depth rationale (calibration)
This is new mapped depth because the corpus has no fixture whose excerpt+event pair is a speaker-reported **non-presence** of a named item. r15 is speaker-reported **presence** of an unidentified mark. Schema pass alone is not prose support and is not canon.

## Out of scope for this report
Implementing the fixture; critic/adjudicator verdict; any live run of the checker.
