# r23 schema scout — witnessed-absence note class (depth axis)

**Worktree:** `/home/vgpnk/Projects/prymeagnt/lore` (`craft/lore-r23`)  
**Baseline HEAD:** `d6ea676fa43549c85eba6ea9291399db1b970af4`  
**Absence check:** `HEAD:.shokunin/lore/corpus/fixtures/r23-note-class` does not exist.  
**Scope:** How a new fixture can carry a **witnessed-absence** note without changing `check_bible.py`. No canon claim. Checker does not map source prose.

## What the checker actually validates

`check_bible.py` loads **only** these files under the bible directory (arrays of objects):

| File | Required fields (types) |
|------|-------------------------|
| `sources.json` | `id`, `title`, `kind`, `reliability_note` (nonempty str) |
| `entities.json` | `id`, `kind` ∈ {character, place, faction, item}, `name`, `first_appearance` (source id), `claims` (list of `{statement, source_id}`) |
| `relations.json` | `from`, `to` (entity ids), `type`, `source_id` |
| `timeline.json` | `id`, `tick` (int ≥ 0), `entity_id`, `place_id`, `depends_on` (list of event-id **strings**), `description`, `source_id` |
| `contradictions.json` | `id`, `claim_a`/`claim_b` (`event_id` + `field` ∈ {place_id, tick, depends_on}), `why` |

**Not loaded:** any `*.md` excerpt, LOG, SCORECARD, or free-form note class metadata.  
**Confirmed:** the checker **will not read** an excerpt. Clause-by-clause mapping of “speaker X reports thing Y was not present” is **manual fixture authoring**, not a checker feature. Source-text truth stays unverified.

## r15 vs this class

- **r15** (`r15-carbon-followup/`): private-note **mark observation** (blurred blue oval; origin unknown; not attributed to Mira’s Blue Seal). Timeline event `carbon-followup` + source `sella-carbon-followup` + excerpt md. That is **not** witnessed absence.
- **r23 target class:** **witnessed absence** — a **named speaker** reports that a **named thing was not present**. Do **not** restate r15 rows as new depth (round 14 rejection pattern).

## Files a separate `r23-note-class` (or similar) fixture needs

**Checker-required (minimum for exit 0):**

1. `sources.json`
2. `entities.json`
3. `relations.json` (may be `[]` if no edges needed, or one edge if useful)
4. `timeline.json`
5. `contradictions.json` (may be `[]`)

**Human-only (optional; checker ignores):**

6. One excerpt markdown (e.g. `sella-absence-excerpt.md`) documenting invented in-world prose and the manual clause map. Useful for depth/coverage craft; **not** required for `check_bible.py` exit 0.

Do **not** edit checker, fixtures outside this new dir, LOG, or SCORECARD in this scout’s mandate.

## Copy r15 or start from `consistent/`?

**Recommend: start from `consistent/`, then add the smallest delta for one witnessed-absence event.**

Reasons:

- `consistent/` already exits clean with unique ids, nonnegative ticks, valid place kinds, and a short Mira/harbor/tower/seal spine.
- Copying **all** r15 rows re-imports the mark-observation event and Sella registry carbon story; that risks “restated depth” and confuses the new note class with r15.
- r15 is still the **shape reference** (extra source + character + one later timeline row + empty contradictions), not the content to clone.

Minimal additive pattern on top of `consistent/`:

1. **One new source** with unique `id` (e.g. `sella-absence-note`) — fictional private note; reliability_note states invented fixture text, speaker report only.
2. **One new character entity** if the speaker is not already present (e.g. `sella`) with `first_appearance` → that source (or a second small source if preferred), and ≥1 claim with matching `source_id`.
3. **Reuse** existing `seal` (item) and `harbor` (place) as the named thing and locus of absence — no need for new item/place unless the prose demands it.
4. **One new timeline event** whose `description` is fixture-input-scoped and encodes the class in prose, e.g. speaker reports the named item **was not present** at place at tick T.  
   - `entity_id` = speaker (actor on the event)  
   - `place_id` = place kind `place`  
   - `source_id` = the new unique source  
   - `depends_on` = `[]` or earlier event ids as **strings** with strictly earlier ticks  
   - `tick` ≥ 0; avoid double-booking the same `(entity_id, tick)` at two places  
5. **`relations.json`:** optional; e.g. empty `[]`, or a single typed edge only if it stays citation-clean. Not required for the class.
6. **`contradictions.json`:** `[]` unless deliberately testing assertion pairs (not needed for smallest CLEAN).

## Constraints checklist (must hold for exit 0)

- **tick** nonnegative integer on every timeline row (and on item provenance ticks if used; provenance optional and item-only).
- **Unique** entity `id`s; **unique** source `id`s; **unique** timeline event `id`s (duplicates → ambiguous citations / deps).
- **`depends_on`:** list of **strings** that are other event ids; no self-dep; no repeats; dependency tick must be **strictly before** dependent when both ≥ 0.
- **`place_id`:** must resolve to an entity with `kind` **`place`** (and unique id).
- **`entity_id` (timeline actor):** unique entity id; dangling or ambiguous ids fail.
- All `source_id` / `first_appearance` citations must resolve to exactly one source.
- **Descriptions** (and claims/reliability notes): **fixture-input-scoped** invented fiction; no omniscient canon voice; state that the speaker reports absence, not that absence is world-true.
- Faction `allied_with` reciprocity only matters if you add such edges — avoid for smallest fixture.
- Empty `relations` / `contradictions` arrays are valid.

## Smallest fixture that still exits 0

**Directory sketch:** `.shokunin/lore/corpus/fixtures/r23-note-class/` containing the five JSON files only.

**Content sketch (illustrative ids — implementer may rename):**

- Sources: keep `archive-ledger`, `courier-log`; add `sella-absence-note`.
- Entities: keep mira, harbor, tower, seal; add sella (character) with one claim citing `sella-absence-note`.
- Relations: `[]` **or** keep consistent’s `mira→seal carries` only (copy from consistent).
- Timeline: keep `departure` / `arrival` **or** drop arrival if unused; add e.g. `seal-absence-report` at tick 3, `entity_id=sella`, `place_id=harbor`, `depends_on=["departure"]` or `[]`, description stating Sella reports the Blue Seal was **not present** (named speaker + named thing + absence). Cite `sella-absence-note`.
- Contradictions: `[]`.

That is enough for:

```text
CLEAN: schema, citations, relations, timeline; 0 violations
```

Optional excerpt md documents the clause map for craft judges; checker never opens it.

## Depth move (this round)

- **New mapped class:** witnessed absence as a **timeline description + dedicated source + speaker entity**, not a new checker field and not r15’s mark row.
- **Does not change checker:** no schema extension; class lives in authored JSON (+ manual excerpt).
- **Avoid:** cloning r15 `carbon-followup` wording; claiming source prose is checker-verified; multi-event restatements of existing consistent rows without the absence proposition.

## Recommendation (one line)

Ship the smallest bible as **`consistent/` + one speaker + one absence source + one timeline event + empty contradictions**; keep excerpt out of the checker path; leave `check_bible.py` untouched.
