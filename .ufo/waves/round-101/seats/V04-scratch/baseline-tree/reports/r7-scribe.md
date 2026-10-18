# Round 7 scribe — bounded wording proposal

## Observed evidence (not an r7 result)

The standing LOG claims the baseline at `4f6eaba9c7f4807b4a28ba9883af5bf479252294` has last-wins `sources` indexing: duplicate IDs are diagnosed, but a dict retains the later row. Current checkout inspection of `.shokunin/lore/corpus/fixtures/check_bible.py` is consistent with that claim: `index(section)` appends a duplicate-ID error and then unconditionally executes `result[row['id']] = row`; `source()` only tests `source_id not in sources`; contradiction witness and alliance-reverse checks likewise test membership in `sources`. These are code observations, not evidence yet that an r7 fix works.

The clean-control CLI was rerun from the repo root:

```text
$ python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/consistent
CLEAN: schema, citations, relations, timeline; 0 violations
```

Other existing observations in `.shokunin/lore/corpus/live/runs/20261012T165220Z/`: `ally-reciprocal.txt` exits 0 with `CLEAN ... 0 violations`; `item-chain-valid.txt` exits 0 with the same; `item-chain-broken.txt` exits 1 with `VIOLATION: entities[3].provenance[2]: provenance chain break; expected from_holder 'harbor', got 'mira'` followed by `1 violation(s); no canon changed`. Those runs are from round 6 and do not exercise duplicate-source IDs. `consistent/sources.json` has distinct `archive-ledger` and `courier-log` rows.

## Proposed README / decision-table language (only if r7 replay confirms)

> **Ambiguous source IDs:** A source ID is usable as a citation witness only when it identifies exactly one valid row in `sources.json`. A repeated ID remains a duplicate-ID violation, and references to that ID are reported as ambiguous rather than accepted as uniquely resolved. The checker retains/reports the source records; it does not choose one, merge them, or establish that source text supports a claim. This behavior is covered only for the committed cases below; it is not source-authenticity or canon-truth verification.

Suggested bounded decision table; fill measured exit/diagnostic fields from the non-author raw replay, not by treating the prediction column as fact:

| Case | One controlled condition | Expected bounded observation (proposal, not measured) | What it would establish |
|---|---|---|---|
| `consistent` | Existing unique-source control, unchanged | Preserve exit 0 / `CLEAN` | No regression for current clean bible |
| unique-source reciprocal alliance | Existing `ally-reciprocal` control | Preserve exit 0 / `CLEAN` | Existing unique witness still qualifies |
| duplicate source ID, referenced | Minimal copy with one source ID duplicated and one existing reference to it | Exit 1; duplicate-ID and local ambiguity diagnostic(s), exact count/output to be measured | Ambiguous ID does not qualify by dict last-wins |
| duplicate source ID used by reciprocal alliance | Paired fixture where the reverse alliance witness uses duplicate ID | Exit 1; duplicate-ID plus missing/ambiguous reciprocal-witness diagnostic(s), measured exactly | Duplicate-ID row cannot satisfy reverse witness |
| duplicate source ID used by provenance record | Paired fixture with provenance citation switched to duplicate ID | Exit 1; duplicate-ID plus local ambiguous-source diagnostic(s), measured exactly | Duplicate-ID does not count as unique provenance citation |

For each row, state the exact repo-root command, fixture path, exit status, stdout/stderr (or explicitly say stderr empty), and raw evidence path. Keep the “one change” claim only where a byte/path comparison proves it. Avoid promising exactly two diagnostics: downstream findings may cascade. Preserve both duplicate records; do not remove a source or select a winner. If the implementation intentionally emits only the duplicate-ID diagnostic and not local ambiguity, revise the proposed wording to avoid promising a local diagnostic, and adjudicate whether the original reference is still falsely presented as resolved.

## README placement suggestion

Add a short scope note near `.shokunin/lore/corpus/README.md`'s fixture/checker bullets, and link the measured table under `knowledge/` once committed. Do not describe this as checking citation *support*, validating source contents, proving truth, or resolving competing documents. Existing `.shokunin/lore/corpus/knowledge/2026-10-12-malformed-error-patterns.md` models the right evidence boundary: exact fixtures and outcomes, with explicit limits. No README or checker file was edited for this scribe task.
