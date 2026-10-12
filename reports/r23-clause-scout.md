# Round 23 clause scout — witnessed-absence note class

## Scope and limits

Leaf clause map for lore round 23 depth axis-move. Baseline HEAD `d6ea676fa43549c85eba6ea9291399db1b970af4` has no `r23-note-class` fixture (`git cat-file -e HEAD:.shokunin/lore/corpus/fixtures/r23-note-class` fails). Checker `check_bible.py` validates schema, IDs, relations, and timeline structure only; it does **not** map source prose. Source-text truth and canon are unverified. This report designs a clause-by-clause map only; it does not edit fixtures, checker, LOG, or SCORECARD.

**Owned axis this round:** depth (single axis-move). Coverage and calibration are out of scope here.

**Class under design:** WITNESSED ABSENCE — a named speaker reports that a named thing was **not** present. This is **not** the r15 private-note mark observation (positive sensory report of a blurred blue oval on a kept carbon, origin unknown, non-attribution to the Blue Seal).

**r14 guard:** do not restate existing rows as new depth. Mapping must introduce a new observation class, not paraphrase `registry-entry`, `carbon-followup`, or entity/relation claims already present.

## Raw observations (r15 carbon-followup baseline)

### Excerpt `sella-carbon-followup-excerpt.md` (source ID `sella-carbon-followup`)

Prose (invented fixture text, not recovered evidence):

> Later, at Lantern Harbor, I looked again at the carbon I had kept. I saw a blurred blue oval mark on it. I cannot identify where the mark came from, and I do not attribute it to Mira’s Blue Seal.

### Timeline event `carbon-followup` (`timeline.json`)

| Field | Value |
|---|---|
| `id` | `carbon-followup` |
| `tick` | `3` |
| `entity_id` | `sella` |
| `place_id` | `harbor` |
| `depends_on` | `["registry-entry"]` |
| `description` | Sella reports looking again at the carbon she kept and observing a blurred blue oval mark whose origin she cannot identify; she does not attribute it to Mira’s Blue Seal. |
| `source_id` | `sella-carbon-followup` |

### Contrast: what r15 maps vs what witnessed absence needs

| Dimension | r15 carbon-followup (mapped mark observation) | Witnessed absence (new class) |
|---|---|---|
| Speech act | Positive observation (“I saw …”) | Negative report (“I did not see / was not present …”) |
| Object of report | Mark **on** retained carbon | Named thing **absent** from a named scene/object/place |
| Uncertainty | Origin unknown; non-attribution | Absence as reported; **no** inferred cause |
| Blue Seal | Explicit non-attribution clause | Must **not** invent Seal presence, absence-as-seal-proof, or Seal link |
| Depth novelty | New sensory detail + uncertainty | New **negation** observation class, clause-checked |

r15 is a useful structural neighbor (first-person private note → timeline row + source ID + entity/place), not a template to copy as restatement.

## Required clauses for a witnessed-absence note

A witnessed-absence note **must** carry these speaker-report clauses (as reported, not as omniscient fact):

1. **Speaker identity as reported** — who states the absence (first person or clearly named reporter in the note).
2. **Place (or locus) of the report/scene** — where the speaker situates the looking or the scene of absence (place name or bounded locus tied to a `place` entity when the fixture uses `place_id`).
3. **Thing absent** — a named thing (item, mark, person, seal impression, destination entry, etc.) reported as not present / not found / not seen.
4. **No cause** — the prose must **not** supply a cause for the absence; absence is the observation, not an explanation.

Minimal shape (illustrative only; not authored fixture text and not canon):

> At [place], I, [speaker], [looked at / checked] [locus]. [Named thing] was not [present / on it / there]. I do not know why.

Fixture wiring expected for a later executor (recommendation, not implemented here): one source row + excerpt; timeline event with `entity_id` = speaker, `place_id` = place, `source_id` = note source, `description` aligning only to mapped clauses; optional entity claim only if the note newly introduces the speaker (prefer reusing `sella` / `harbor` if the scene stays with them). No contradiction row required solely to encode absence.

## Must stay unmapped (must-not-imply)

These must **not** be written into fixture fields as established facts, even if adjacent lore tempts them:

| Forbidden implication | Why |
|---|---|
| **Cause of absence** | Class requires no cause; mapping a cause upgrades report to explanation |
| **Time-of-absence as clock fact** | Phrases like “later”, bells, or year labels are report framing; `tick` is fixture ordering only, not conversion of clock time (same discipline as r15 “first bell” / “Later”) |
| **Blue Seal link** | Presence, absence, touch, authorship, or proof-via-absence of/for Mira’s Blue Seal must not be implied; r15 already spent a non-attribution clause on a *positive* mark — absence must not silently re-open Seal provenance |
| Omniscient “really missing” | Fixture rows cite a speaker report; they do not establish world truth |
| Restatement of r15 mark / blank destination / keeps-carbon alone | Would fail the r14 depth-restatement guard |

## Clause map template

Status vocabulary:

- **mapped** — clause should correspond 1:1 to a named fixture field (or a bounded substring of `description` / claim `statement`).
- **deliberately unmapped** — clause may appear in prose for readability but must not become a typed fact field.
- **must-not-imply** — clause must not be present in prose *or* must be actively blocked from fixture inference (no field, no sneaky description upgrade).

### A. Illustrative witnessed-absence prose, split into clauses

*Illustrative target prose for the new class (design aid only; not a committed excerpt):*

> Later, at Lantern Harbor, I, Sella, looked again at the carbon I had kept. The registry destination was still blank; no destination mark was present on the carbon. I do not know why it remained blank.

| # | clause (prose) | fixture field | status |
|---|---|---|---|
| 1 | “Later” (sequence adverb) | *(none)* — optional narrative hinge only; ordering via `depends_on` / higher `tick` if needed | deliberately unmapped |
| 2 | “at Lantern Harbor” | `timeline.json` event `place_id` → `harbor`; place entity `name` | mapped |
| 3 | “I, Sella” | `timeline.json` event `entity_id` → `sella`; character entity `name` | mapped |
| 4 | “looked again at the carbon I had kept” | bounded span inside event `description` (inspection act); may cite prior keep-carbon only as dependency context, not as new claim | mapped (act); prior keep-carbon is **not** new depth |
| 5 | “The registry destination was still blank” / “no destination mark was present on the carbon” | event `description` core **thing-absent** span; optional item/claim only if a *new* named absent-thing entity is introduced (prefer description-only to avoid restating blank-destination history) | mapped (absence report) |
| 6 | “I do not know why it remained blank” | *(no cause field)* — preserves required **no cause** | deliberately unmapped (explicit non-cause) |
| 7 | Any clock reading equating “Later” to wall time or to tick | `tick` must not be treated as that clock | must-not-imply |
| 8 | Any cause (tampering, Mira, weather, seal press, ink fault, …) | no field; strip from description | must-not-imply |
| 9 | Any Blue Seal presence/absence/authorship/proof | no relation/claim/description upgrade | must-not-imply |
| 10 | Source identity of the note | `timeline.source_id` + `sources.json` `id` + excerpt labeled invented fiction | mapped |
| 11 | Reliability / non-omniscience | `sources.json` `reliability_note` | mapped (meta) |
| 12 | Checker-valid structural keys (`id`, `depends_on`, list types, …) | timeline/entity/source schema fields | mapped (structure only; not prose truth) |

### B. Negative control: r15 mark clauses (not the new class)

For calibration of “different class,” r15 clauses map as a **positive observation**, not absence:

| # | r15 clause | fixture field | status under r15 | status if misused as “absence” |
|---|---|---|---|---|
| R1 | “I saw a blurred blue oval mark on it” | `carbon-followup.description` (mark present) | mapped | **wrong class** — presence, not absence |
| R2 | “I cannot identify where the mark came from” | description uncertainty span | mapped | not an absence of a named thing |
| R3 | “I do not attribute it to Mira’s Blue Seal” | description non-attribution | mapped | Seal-link control, not thing-absent |
| R4 | Cause of the mark | — | must-not-imply | still must-not-imply |
| R5 | Mark time as clock fact | `tick: 3` ordering only | deliberately unmapped as clock | same |

Do **not** ship r23 depth by rewriting R1–R3. Witnessed absence needs a **negation** clause naming the missing thing.

### C. Field checklist (executor-facing, still report-only)

| Must-have clause content | Typical fixture landing | status |
|---|---|---|
| Speaker identity as reported | `entity_id` + entity `name` (+ optional claim only if new) | mapped |
| Place of report/scene | `place_id` + place `name` | mapped |
| Thing absent (named) | event `description` (primary); avoid new relation types the checker does not define | mapped |
| No cause | omit cause from description; no contradiction-as-explanation | deliberately unmapped / enforced absence of cause |
| Source citation | `source_id` ↔ sources row ↔ excerpt | mapped |
| Cause | — | must-not-imply |
| Time-of-absence as clock fact | — (`tick`/`depends_on` = order only) | must-not-imply |
| Blue Seal link | — | must-not-imply |

## Depth claim (falsifiable, non-canon)

**Before:** no clause-level map for a witnessed-absence note class; no `r23-note-class` fixture at baseline HEAD.

**After (when executor implements, out of this scout’s file ownership):** one fixture whose excerpt and timeline description can be table-checked clause-by-clause for speaker, place, thing-absent, and no-cause; checker exits 0 on structure; prior fixture bytes/outputs unchanged. Depth improves only if the negation class is new and not a restatement of r15 mark prose or r10 blank-destination wording alone.

## Non-claims

- No claim that any excerpt is recovered evidence, true, or canon.
- No claim the checker will verify prose ↔ description alignment (it will not).
- No Blue Seal, Mira destination, or mark-origin determination.
- No edit to checker, fixtures, LOG, or SCORECARD by this scout.
- Illustrative absence prose above is a design scaffold; final wording is executor-owned and must remain invented-fiction labeled.

## Finding (one line)

Witnessed absence = mapped {speaker, place, named thing-absent, source} + deliberately unmapped non-cause + must-not-imply {cause, clock-time, Blue Seal link}; distinct from r15 positive mark observation; r14 restatement forbidden.
