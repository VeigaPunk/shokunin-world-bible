# Round 27 non-author reviewer report

## Scope and pair

Reviewed `corpus/fixtures/r27-target-only/` and `corpus/fixtures/r27-both-ambiguous/`, read-only; no production or checker changes. The pair comparison confirms `sources.json`, `relations.json`, `timeline.json`, and `contradictions.json` are byte-identical. Only `entities.json` differs: the both case appends one structurally admitted row (`id: mira`, character, nonempty name, `first_appearance: courier-log`, empty claims). Existing `mira` and duplicate `seal` rows remain unchanged. The cited relation remains exactly `mira -> seal`, `carries`, `courier-log`; `courier-log` is present as a unique source ID.

## Checker replay

Ran `python3 .shokunin/lore/corpus/fixtures/check_bible.py` on each directory. Both exit 1, stderr empty.

- `r27-target-only`: duplicate `entities[4].id` for `seal`; `relations[0].to` ambiguous `seal` (2 findings).
- `r27-both-ambiguous`: duplicate `entities[4].id` for `seal`; duplicate `entities[5].id` for `mira`; `relations[0].from` ambiguous `mira`; `relations[0].to` ambiguous `seal`; `timeline[0].entity_id` and `timeline[1].entity_id` ambiguous actor `mira` (6 findings).

This matches the checker implementation: it counts admitted entity IDs, reports duplicate IDs, and checks relation endpoints independently; timeline actor validation separately reports the two unchanged references to the now-duplicated `mira` ID.

## Assessment and boundary

The two relation-local findings in the both case are precisely `.from` and `.to`; target-only retains only `.to`. The extra duplicate-`mira` diagnostic is expected for the added row, just as duplicate-`seal` is present in both. The two timeline actor ambiguities are collateral consequences of the unchanged timeline references, not additional relation findings or a change to timeline data. Do not describe the both-case output as only four findings.

This pair supports the narrow observation that the checker emits both endpoint ambiguity findings when both referenced IDs have duplicate admitted rows in this fixture. It does not establish distinct real-world entities, resolve identity, establish whether the cited relation is true, or infer canon/source truth from citation IDs or checker output. Review is limited to pair structure and replay; it is not a full historical regression replay.
