# Round 67 simplifier report

## Finding and recommendation

**GO for the scoped checker move, subject to independent replay.** The smallest appropriate change is to reject an entity claim whose `source_id` is empty/whitespace at the claim-local validation, regardless of whether `sources.json` loads. Do not change the schema, fixtures, or other source resolution behavior. This is a claim-input structural requirement; it establishes neither missing fictional-world evidence nor any canon, source-text support, rights, or game-mechanics fact.

Exact checker path: `.shokunin/lore/corpus/fixtures/check_bible.py`. In the entity-claims loop, current condition checks `claim['source_id']` is a `str`, but not that it is nonempty; its `else` calls `source()`. `source_status()` returns `unavailable` if `sources.json` is unavailable, and `source()` emits no finding for that status. The minimal change is to add `or not claim['source_id'].strip()` to the existing claim guard. It reuses the current claim-local message, `expected nonempty statement and source_id`, and leaves nonempty IDs under existing resolution checks.

## Observed commands/results

From repository root (`/home/vgpnk/Projects/prymeagnt/lore`), ran:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/live/r67-probe/empty-unavailable
```

Exit 1; output reports only missing `sources.json` and `1 violation(s); no canon changed`. The probe has a claim at `entities[0].claims[0]` with empty `source_id`. The same command on `.shokunin/lore/corpus/live/r67-probe/control-unavailable` (same input except that claim source ID is nonempty) also exits 1 with only the missing-source-table finding. Thus the empty value receives no claim-local structural finding when the index is unavailable.

Ran the checker on `.shokunin/lore/corpus/live/r67-probe/empty-loaded`, where `sources.json` is present. It exits 1 with `entities[0].claims[0].source_id: unknown in-world source ''`. This confirms the existing index-dependent unknown-source diagnostic when the index is available, but it does not meet the distinct requirement to diagnose the empty required value independently of index availability.

These were read-only checker invocations. I did not edit checker, fixtures, README, LOG, or any other file. The probe directories and Round 67 LOG entry were already present in the working tree when inspected; I make no claim to have authored them.

## Boundaries / validation still needed

This is a narrow code-reading plus current-probe recommendation, not a patch or post-patch verification. Executor should keep the change to the claim guard and test empty and whitespace source IDs with unavailable `sources.json`, the nonempty control, and existing fixtures/raw CLI outcomes. No claim is made about full regression preservation until a non-author verifier replays it. The evidence concerns checker behavior on input only; it cannot establish fictional-world absence, canon, source-text authenticity/support, rights, or game mechanics.
