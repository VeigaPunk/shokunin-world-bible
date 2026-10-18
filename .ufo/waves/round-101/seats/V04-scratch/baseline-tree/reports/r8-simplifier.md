# Round 8 simplifier note — dependency-list integrity

## Observed scope

- `.shokunin/lore/corpus/fixtures/check_bible.py`: `FIELDS["timeline"]["depends_on"]` requires a list. The timeline loop already rejects any list containing a non-string (`{location}.depends_on: expected event-id strings`) and then skips dependency processing for that row. For valid string lists, its dependency loop currently does only unknown-ID lookup and the existing direct tick comparison; it does not compare a dependency with the owning event ID or count repeated list entries.
- `.shokunin/lore/corpus/fixtures/consistent/timeline.json`: `arrival` lists the distinct prerequisite `departure` once (clean control for normal dependencies).
- `.shokunin/lore/corpus/fixtures/contradictions/timeline.json`: `arrival` lists `later` once, already exercising the existing timeline-inversion finding. Its other rows have empty dependency lists. This is not a self/duplicate case.
- `.shokunin/lore/corpus/fixtures/README.md`: documents the local convention that dependency event IDs must have strictly earlier ticks and says the checker reports contradictions rather than choosing canon. It does not currently describe self/duplicate list rules.
- `.shokunin/lore/LOG.md`, “Round 8 — 2026-10-12”: the declared scope is specifically a cited event listing itself or listing one prerequisite ID twice, with no event/source mutation; distinct-prerequisite control should stay clean.

## Smallest implementation recommendation (no graph engine)

After the existing `depends_on` string-list validation succeeds, make one pass over that event's list with a local `seen` set. For each dependency string, independently report (a) equality with this event's own `id`, and (b) a repeat already in `seen`; then add it to `seen`. Keep the current unknown-ID and direct tick checks as they are. This is O(list length), needs no adjacency structure, traversal, cycle detection, sorting, or inference, and emits a relation-local finding without editing the input. Do not let an anomalous entry suppress diagnostics for other entries.

The self comparison should use the row's own `id` directly, not `events[dep]`: that catches self-reference even if the event ID is otherwise missing/duplicated in the index. Duplicate detection is likewise within each individual `depends_on` list; do not reject two different events for independently naming the same prerequisite.

## Separate recommendations / limits

- Keep duplicate timeline event-ID handling separate. `index('timeline')` currently reports duplicates and the resulting `events` mapping is last-wins; changing that resolution policy is outside this list-integrity move.
- Do not add general cycle detection. Self-dependency is an explicit list anomaly; multi-event cycles are not part of the stated claim and would require broader graph semantics.
- Preserve existing diagnostics for unknown prerequisites and timeline inversion. A duplicate occurrence may still independently encounter those checks; avoid silently deduplicating the list before checking it.
- A paired fixture recommendation: clone `.shokunin/lore/corpus/fixtures/consistent/`, changing only one event's `depends_on` to `['departure', 'departure']` for the duplicate case and to `[<that event's own id>]` for self; use separate cases so each intended diagnostic is observable. Existing `consistent` and `contradictions` outputs should remain unchanged. These are recommendations only; no fixtures or checker were edited here.
