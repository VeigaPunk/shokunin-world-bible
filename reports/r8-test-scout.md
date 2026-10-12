# Round 8 test scout — replay plan and old-fixture bounds

## Observed surface

- Active checker: `.shokunin/lore/corpus/fixtures/check_bible.py`. Timeline loading retains valid timeline rows in `data['timeline']`; `index('timeline')` reports duplicate event IDs while retaining a last-wins `events` mapping, and `event_id_counts` is available separately. The timeline loop currently checks that each `depends_on` member is a string, then checks unknown IDs and `events[dep]['tick'] >= row['tick']` (timeline inversion). There is no explicit duplicate-member or self-dependency diagnostic in that loop.
- Current timeline fixture: `.shokunin/lore/corpus/fixtures/contradictions/timeline.json` has `arrival -> later` (inversion), `departure` with empty deps, and other empty dependency lists. It does not exercise a repeated member or a self reference.
- Existing regression inventory is physically under `.shokunin/lore/corpus/fixtures/`: `consistent`, `contradictions`, `ally-reciprocal`, `ally-one-way`, `contradictions-ledger-malformed`, `r5-{missing-file,invalid-json,wrong-top-level,row-shape,invalid-citation}`, `item-chain-{valid,broken}`, and `r7-{ally-reverse-ambiguous,item-ambiguous}`. I replayed all 13 with the active checker from the repo root. Outcomes matched the expected statuses documented in `.shokunin/lore/corpus/fixtures/README.md`: clean controls `consistent`, `ally-reciprocal`, `item-chain-valid` exit 0; all others exit 1. In particular `contradictions` still produced exactly its three seeded errors (dangling relation, timeline inversion, double booking), with no dependency-list-integrity diagnostic. `item-chain-broken` retains its one chain-break diagnostic; malformed cases remain nonzero.
- Saved prior output snapshots exist in `.shokunin/lore/corpus/live/runs/20261012T170333Z/` (14 `.txt` cases) and earlier timestamped run directories. These are useful comparison artifacts, not proof of identical stdout unless compared byte-for-byte. This replay was against the active checker only; I did not compare old fixture output to the round-8 baseline revision.

## Recommended round-8 replay matrix

Use the repo-root CLI form and record stdout plus exit status for each case. Keep old fixture expectations unchanged, and add two minimal new bibles copied from `consistent/` (or construct equivalent isolated inputs):

| Case | Dependency-list input | Expected result |
|---|---|---|
| Existing `consistent` | Empty/distinct valid lists | exit 0; no new diagnostics |
| Existing `contradictions` | `arrival` lists `later` once | exit 1 with the same three existing findings, including one inversion; no new integrity finding |
| New `r8-dependency-distinct` | One event lists two distinct, uniquely identified earlier event IDs | exit 0; verifies no false positive for an ordinary multi-prerequisite list |
| New `r8-dependency-self` | One event lists its own unique ID once | exit 1; one relation-local self-dependency diagnostic (and define whether the existing equal-tick inversion is intentionally retained or suppressed; assert the chosen behavior) |
| New `r8-dependency-duplicate` | One event lists the same uniquely identified, earlier prerequisite ID twice | exit 1; one repeated-member diagnostic at the second occurrence or dependency-list location, without changing the JSON |
| Optional boundary probe | Dependency ID points to duplicate event IDs, unknown event, or non-string member | Preserve current duplicate-event / unknown / non-string findings; do not mislabel ambiguous or malformed references as a confirmed self/repeated valid prerequisite unless the implemented rule explicitly defines that behavior |

For all old fixtures, compare the relevant expected exit code and existing diagnostic set (ideally exact stdout against the pinned baseline checker at `17736ae5ed260c4b99f98efd9b194254ccd2aa87`, not merely “still fails”). Include the three malformed-dependency boundaries only if the implementation changes that path; they are not necessary to prove the narrow duplicate/self rule. Do not assert unchanged full-tree hashes without actually capturing and comparing the path maps.

## Recommendation (not an implementation)

Keep this test move relation-local and isolate each anomaly: one fixture where only a unique event has self-reference, one where only a valid earlier prerequisite is repeated, and one clean distinct-prerequisite control. Retain `contradictions/` as a regression for the existing inversion and verify its exact three-finding output. Treat duplicate event IDs as ambiguous input, not a uniquely resolved self-reference. Distinguish new list-integrity findings from the existing per-reference unknown/inversion checks, and document any intentional overlap for self-reference (same tick naturally satisfies the existing inversion predicate). This report makes no checker or fixture changes and does not claim source/canon truth verification.
