# Round 23 scribe — witnessed-absence note class (draft only)

**Status:** documentation proposal for depth axis. This report does **not** edit the decision table, fixtures README, checker, LOG, SCORECARD, or any fixture. It does not commit. No `r23-note-class` tree is claimed present at baseline HEAD `d6ea676fa43549c85eba6ea9291399db1b970af4` (`git cat-file -e HEAD:.shokunin/lore/corpus/fixtures/r23-note-class` fails).

**Axes this round:** depth (single move), coverage, calibration. **Not** a restatement of r14/r15 rows. Distinct from r15 mark observation (positive sighting of a blurred blue oval; origin unknown; not attributed to Mira’s Blue Seal).

**Explicit limit:** checker does not validate prose; source-text truth unverified. `check_bible.py` checks schema, citations, relations, and timeline structure only. It does **not** map source prose. No canon claim.

---

## Proposed decision-table row (paste candidate only)

## Round 23 — witnessed-absence note class

| Input condition | Decision / output | Fixture evidence and limit |
|---|---|---|
| Named speaker S (character entity with resolvable `source_id`) authors a private-note excerpt that states a named thing T was **not** present at a named place/time/context C; fixture maps one clause per absence claim without inventing a positive sighting of T | Accept as **witnessed-absence** note class: record speaker, named absent thing, reported context, and exact excerpt clause; keep ordinary schema/citation/timeline checks; do not coerce absence into entity deletion, occupancy clearance, or contradiction with other sources | Proposed `fixtures/r23-note-class/` plus clause map `fixtures/r23-note-class/witnessed-absence-clause-map.md` (or sibling path under that fixture). Distinct from `fixtures/r15-carbon-followup/` mark observation. Absence is S’s report only—not proof T never existed, was never elsewhere, or that other witnesses agree. |

One-row summary for table tools: **input** = named speaker reports named thing absent in named context; **decision** = classify/map as witnessed-absence with clause-level pointers; **evidence** = `r23-note-class/` + `witnessed-absence-clause-map.md`.

---

## Proposed fixtures README blurb (paste candidate only)

## Round 23: witnessed-absence note class

`r23-note-class/` is a separate fictional micro-bible intended to introduce the
**witnessed-absence** note class: a named speaker reports that a named thing was
**not** present (not a positive mark sighting). Clause-by-clause mapping lives in
`r23-note-class/witnessed-absence-clause-map.md` beside the excerpt and JSON
tables. This class is not the r15 carbon-mark observation
(`r15-carbon-followup/`). Run from repo root when the fixture exists:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r23-note-class
```

Map only what the excerpt states (speaker, named absent thing, context). Do not
infer destruction, never-existence, seal non-involvement, or resolution against
other sources. Checker does not validate prose; source-text truth unverified.
Clean checker output means schema/IDs/timeline structure only—not that the
absence report is true or canon.

---

## Depth move (why this is not r14 restatement / not r15)

- **New class:** witnessed absence (speaker + named thing + not-present claim), previously unmapped clause-by-clause.
- **Contrast r15:** r15 maps a **positive** visual report (“blurred blue oval mark”) plus unknown origin and non-attribution; r23 maps **absence of a named thing**, not mark morphology.
- **Calibration:** no claim that checker reads excerpts; no claim source prose entails JSON beyond manual clause map; no canon.

## Out of scope this report

Fixture JSON/excerpts, checker changes, decision-table or README file edits, commits, child spawns.
