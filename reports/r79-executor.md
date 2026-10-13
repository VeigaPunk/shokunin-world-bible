# Round 79 executor — arrival-order note fixture

## Scope and implementation

Created `.shokunin/lore/corpus/fixtures/r79-arrival-order-note/` as a copy of `r73-jorin-slate-claim`. Preserved all inherited non-append-target files byte-for-byte (verified: no differences); preserved all eight inherited source rows and eight entity rows unchanged and in order. Appended one source row at `sources.json` `/8` (`iren-arrival-order-note`) and one new character row at `entities.json` `/8` (`iren`), with the sole cited claim at `/8/claims/0` pointing to `iren-arrival-order-note`. No relation, timeline, or contradiction rows were added or changed. New prose files: `iren-arrival-order-note-excerpt.md` and `iren-arrival-order-clause-map.md`.

## Excerpt and claim map

Exact excerpt in `iren-arrival-order-note-excerpt.md`:

> I wrote the names in the order people reached my desk, not the order the clerk called them. If I copied the clerk’s order, the people who had waited longest would look as though they came last.

`entities.json` `/8/claims/0/statement` paraphrases both clauses as Iren’s report: she/he writes names in arrival rather than call order, and reports the stated reason that copying call order makes longest-waiting people look last. The first exact clause and rationale are separately mapped in `iren-arrival-order-clause-map.md` to that claim and its source pointer `/8/claims/0/source_id` → `sources.json` `/8/id`. Source is explicitly fictional and unverified.

## Bounded editorial choice and limits

The clause map records one fiction-local presentation choice: for this hypothetical scene, display names in arrival order rather than silently rearranging them into the clerk’s call order. The rationale is the narrator’s explicit stated concern about how the longest-waiting people would appear. The choice is not a claim about an actual queue, institution, policy, fairness rule, or established canon; absent the invented excerpt, the fixture supplies no basis for preferring either order. No slate/occasion connection, timeline, relation, or contradiction is asserted. Citation checking does not authenticate source text or validate semantic support. No rights, mechanics, or source-authenticity inference is made.

## Checker observation

From the repository root, ran:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r79-arrival-order-note
```

Observed exit code: `0`

Exact stdout:

```text
CLEAN: schema, citations, relations, timeline; 0 violations
```

Exact stderr: empty.

This is a clean structural/schema and citation-pointer result only; the checker does not read the excerpt or clause map.
