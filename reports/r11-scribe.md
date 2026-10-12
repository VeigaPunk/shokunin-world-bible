# Round 11 scribe — bounded entity-ID ambiguity table and README proposal

Scope: documentation draft only. No checker, fixture, shared document, or commit changed. The table below separates observed baseline behavior from proposed policy. The checker evidence is the checked-out `.shokunin/lore/corpus/fixtures/check_bible.py`; the round-11 declaration identifies baseline report commit `4337c6385ed3f00f45d03eb263028ae313507006` and its baseline checker. No claim below says a proposed ambiguity finding is implemented.

## Observed baseline and CLI probes

The checked-in code first collects schema-valid entity rows, then `index('entities')` emits a duplicate-ID diagnostic while assigning each subsequent row to `result[id]`, replacing the earlier row. Timeline validation tests `row['place_id'] in entities` and then reads `entities[row['place_id']]['kind']`; it has no duplicate-count guard. In contrast, the same file already counts entity IDs for provenance chain gating and allied-pair eligibility. Relation endpoints only test membership in that last-wins dictionary.

Repo-root CLI probes, using the checked-out baseline checker:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/r11-entity-place-char
# VIOLATION: entities[4].id: duplicate entities id 'harbor'
# VIOLATION: timeline[0].place_id: not a place 'harbor'
# exit 1
python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/r11-entity-char-place
# VIOLATION: entities[4].id: duplicate entities id 'harbor'
# exit 1 (no timeline place-kind finding)
python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/r11-entity-unique-place
# CLEAN; exit 0
python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/r11-entity-unique-char
# VIOLATION: timeline[0].place_id: not a place 'harbor'; exit 1
```

These four probe directories were generated under `/tmp` from `consistent/`; the paired duplicate cases contain the same two schema-valid `harbor` rows, `place` and `character`, with only their order swapped. The duplicate diagnostic path is `entities[4].id`; the baseline case difference confirms order-sensitive place classification. The unchanged control is `.shokunin/lore/corpus/fixtures/consistent/`. For a separate existing example of count-based policy, `corpus/fixtures/r7-item-ambiguous/entities.json` plus `corpus/live/runs/20261012T173416Z/r7-item-ambiguous.txt` show ambiguous source IDs block provenance interpretation while leaving raw records and reporting the citation issue. Existing duplicate-event probes at `corpus/fixtures/r9-dup-{low-high,high-low}/` and `corpus/live/runs/20261012T173416Z/r9-dup-low-high.txt`, `.../r9-dup-high-low.txt` provide another order-swapped control: ambiguous event dependency gets a local diagnostic. They are precedent, not direct evidence about entity IDs.

## Proposed bounded decision table (recommendation; not yet implemented)

| Input condition | Proposed decision / output | Boundary / evidence |
|---|---|---|
| A schema-valid entity row repeats an entity `id` | Keep existing duplicate-ID finding at the later row; retain every raw row. Do not choose a canonical row. | Existing baseline behavior `index('entities')`; duplicate-ID reporting is not identity resolution. |
| `timeline[i].place_id` has no schema-valid entity row | Keep existing dangling-entity finding; do not additionally classify its kind. | Current membership check in checker; `consistent/timeline.json` provides unique-place control only. |
| `timeline[i].place_id` resolves to exactly one schema-valid entity row whose `kind` is `place` | Accept this place-kind check (subject to unrelated checks). | Unique-place probe `/tmp/r11-entity-unique-place`, exit 0. |
| `timeline[i].place_id` resolves to exactly one schema-valid entity row with another kind | Keep the existing `not a place` finding. | Unique-character probe `/tmp/r11-entity-unique-char`, exit 1. |
| `timeline[i].place_id` matches more than one schema-valid entity row | Recommend an input-local `ambiguous entity reference` finding at `timeline[i].place_id`; skip kind classification for that reference. Keep duplicate-ID report(s) and all rows. The conclusion must be invariant to row order. | Opposite outputs from `/tmp/r11-entity-place-char` and `/tmp/r11-entity-char-place` establish the narrow bug. Avoid claiming ambiguity for malformed rows filtered before indexing. |
| Relation `from`/`to` or timeline `entity_id` has an entity ID duplicated | **Not covered by the round-11 claim.** Current relation and timeline membership checks do not establish uniqueness. Do not advertise a new diagnostic for these fields without separate premise, probes, and declared scope. | `relations` endpoint checks and timeline `entity_id` checks in baseline checker are membership-only. |
| Item provenance holder `from_holder` / `to_holder` has duplicated entity ID | Existing behavior suppresses chain continuity for non-unique holder IDs (`entity_id_counts`); preserve both records. Whether to emit a separate holder-ambiguity diagnostic is outside this round's declared place-reference move. | Baseline provenance loop; `corpus/fixtures/r7-item-ambiguous/entities.json` is source-ID, not entity-holder, ambiguity and must not be misrepresented as direct coverage. |
| `allied_with` endpoint ID is duplicated | Existing eligibility guard skips the faction reciprocal rule if either entity count is not one. Preserve this behavior; do not infer relation semantics. | Baseline `entity_id_counts` guard; round 11 does not claim to expand alliance handling. |

The phrase “ambiguous entity reference” is a proposed diagnostic class, not asserted literal CLI wording. This is structural ID ambiguity only; it makes no statement about names, aliases, in-world identity, source truth, or canon. Existing duplicate-ID diagnostics remain. Avoid saying “all entity-ID uses are checked” or “ambiguous IDs are globally rejected.”

## README / fixture-documentation text proposal (recommendation only)

Suggested addition to `.shokunin/lore/corpus/fixtures/README.md` under an entity-ID ambiguity heading (or a short link from its existing local-assumptions section):

> **Duplicate entity IDs and timeline place references.** Entity IDs are lookup keys, so a duplicate-ID diagnostic does not identify which row is canonical. For a timeline `place_id` that matches more than one schema-valid entity row, report the ambiguous reference and do not decide whether the ID names a place by taking the first or last row. Keep the duplicate-ID diagnostic and all input records. A unique place-kind row passes this particular check; a unique non-place row retains the `not a place` finding; an absent ID retains the dangling-reference finding. This rule concerns only the timeline `place_id` kind check. It does not establish identity from names, validate canon, or extend ambiguity diagnostics to every relation, timeline subject, or provenance holder reference.
>
> Reproduce the order-sensitivity probe with the `r11-*` fixture commands once those fixtures and independent verification exist. Until then, treat this paragraph as proposed policy, not current checker behavior.

Do not add this as established documentation until the executor change, paired committed fixtures, independent replay, and final axis adjudication confirm it. As of this scribe report, the checked-in corpus has no `r11-*` paired entity fixtures; no claim is made about post-change outputs or prior-fixture regression replay.
