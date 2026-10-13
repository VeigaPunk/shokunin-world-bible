# Round 67 scribe — README wording and evidence boundaries

## Scope and recommendation

**Conditional GO for the declared calibration move; no README edit made here.** The intended rule is narrow: require a nonempty claim `source_id` even if `sources.json` cannot load. Existing README text says the schema requires a source, but it does not explain that source-index availability currently gates ID lookup. A short operational note could make this specific validation boundary clear. This is a proposed wording/evidence note, not evidence that the proposed checker change has been implemented or verified. Independent adjudication should still decide whether the benefit is material and whether the candidate causes harm.

Suggested concise wording, after the rule is implemented and replayed:

> Each entity claim needs a nonempty `statement` and nonempty `source_id`. The checker validates that required field even when `sources.json` is unavailable; it checks whether a nonempty source ID is known only when that index loads. An unavailable index is reported separately and does not establish whether a citation is valid.

Do not publish this as current behavior before implementation. Until then, an accurate description of observed current behavior is: claim validation requires a nonempty statement and a string `source_id`; source-ID membership is checked only when the source index is available, and empty/whitespace IDs can escape claim-local validation when it is unavailable.

## Observations and commands

Working tree baseline observed with `git status --short --branch`: branch `craft/lore-r1`; pre-existing `M .shokunin/lore/LOG.md`, `?? .shokunin/lore/corpus/live/r67-probe/`, and `?? .shokunin/lore/reports/r67-simplifier.md`. HEAD was `262486d719ff1690c41b48dd1d0413305c396cdb`. I did not modify these paths. Mission and `.shokunin/lore/LOG.md` Round 67 declare the hypothesis, calibration axis, and probe scope.

Read `.shokunin/lore/corpus/fixtures/check_bible.py` lines 97–109 and 145–155. `source_status()` returns `unavailable` when sources are unavailable; `source()` emits unknown/ambiguous diagnostics only for those statuses. Claim validation checks statement nonemptiness and only that `source_id` is a string; if those checks pass it calls `source()`.

Ran, from repository root:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/live/r67-probe/empty-loaded
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/live/r67-probe/empty-unavailable
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/live/r67-probe/control-unavailable
```

Observed results (all exit 1):

- `empty-loaded`: `VIOLATION: entities[0].claims[0].source_id: unknown in-world source ''`; summary `1 violation(s); no canon changed`.
- `empty-unavailable`: one `sources.json: cannot load JSON` violation; **no claim-local diagnostic**; summary one violation.
- `control-unavailable`: same one missing-`sources.json` load error, no claim-local diagnostic. Its claim has a nonempty source ID, unlike the empty-ID probe.

These are existing, uncommitted `live/r67-probe` inputs, not canonical fixtures. The probes show the gap and a limited control on the current checker; they do not replay a candidate implementation, establish stability of existing fixture outputs, or independently verify the declared gain.

README context: `.shokunin/lore/corpus/fixtures/README.md` lines 38–41 currently says the schema requires every entity claim, relation, and event to cite an in-world source, and that these entries are invented for the fixture. The proposed text should complement—not expand—the checker’s structural validation description.

## Evidence boundaries

- This concerns checker behavior on the named JSON inputs only. It is not evidence that a fictional assertion is true, false, canon, or supported by source text.
- `source_id` is a data identifier; the checker’s index membership check does not verify source contents, authenticity, provenance, or the adequacy of a citation.
- An unavailable `sources.json` means the checker cannot resolve source-ID membership; its load error is not proof that the referenced source does or does not exist.
- No claim about real-world rights, permissions, historical facts, or game mechanics is made.
- No README, checker, fixture, or LOG edits were made by this scribe. No commit, push, or merge was performed.
