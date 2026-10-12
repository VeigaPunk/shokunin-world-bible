# Round 10 test scout — baseline replay and source-mapping checks

## Observations

- The round-10 declaration in `.shokunin/lore/LOG.md` identifies baseline report commit `29159c263771d425f215f275491c6614219cea59`, the clean original `consistent/` fixture, and the intended new separate cited micro-bible. At inspection there was no round-10 fixture directory; `consistent/` contains only `sources.json`, `entities.json`, `relations.json`, `timeline.json`, and `contradictions.json` (the latter is empty). Its two source rows contain metadata, not excerpts.
- The raw baseline outputs are present at `.shokunin/lore/corpus/live/runs/20261012T172227Z/<fixture>.txt`. Exactly 19 fixture directories were present. I replayed each with `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>` from repo root; all exit codes and stdout matched the corresponding recorded output (stderr empty). For `r5-missing-file`, matching the recorded relative-path invocation also matches its path-bearing error text.
- Current 19-case replay matrix (exit status / violations):

| Fixture | Exit / findings | Fixture | Exit / findings |
|---|---:|---|---:|
| `ally-one-way` | 1 / 1 | `ally-reciprocal` | 0 / 0 |
| `consistent` | 0 / 0 | `contradictions` | 1 / 3 |
| `contradictions-ledger-malformed` | 1 / 4 | `item-chain-broken` | 1 / 1 |
| `item-chain-valid` | 0 / 0 | `r5-invalid-citation` | 1 / 1 |
| `r5-invalid-json` | 1 / 1 | `r5-missing-file` | 1 / 1 |
| `r5-row-shape` | 1 / 1 | `r5-wrong-top-level` | 1 / 1 |
| `r7-ally-reverse-ambiguous` | 1 / 3 | `r7-item-ambiguous` | 1 / 7 |
| `r8-deps-anomalous` | 1 / 3 | `r8-deps-distinct` | 0 / 0 |
| `r9-dup-high-low` | 1 / 2 | `r9-dup-low-high` | 1 / 2 |
| `r9-unique-control` | 0 / 0 | | |

  The run files provide the exact diagnostics, including malformed-file load errors, dangling IDs, reciprocal relation, provenance chain, dependency anomalies, and r9 ambiguous event findings.
- The checker at `.shokunin/lore/corpus/fixtures/check_bible.py` validates schema and source-ID resolution; it does not read or validate excerpt prose. `consistent/sources.json` defines `courier-log` as first-person and `archive-ledger` as non-omniscient, but supplies no text to independently compare to the entity, relation, or event assertions. The round-10 scribe report `.shokunin/lore/reports/r10-scribe.md` likewise records those baseline claims and notes that no r10 fixture/report existed at its inspection.

## Replay commands (reproducible)

Run from repository root; these print the recorded command for each case and should exit with the same statuses above:

```sh
for d in .shokunin/lore/corpus/fixtures/*/; do
  [ -f "$d/sources.json" ] || [ "${d##*/}" = r5-missing-file ] || continue
  python3 .shokunin/lore/corpus/fixtures/check_bible.py "$d"
done
```

For exact per-case output comparison, run the individual command shown in each `.txt` under `.shokunin/lore/corpus/live/runs/20261012T172227Z/` and compare stdout/status; the `r5-missing-file.txt` case includes a path-bearing diagnostic, so retain the recorded relative invocation. To check fixture/checker integrity around future read-only replays, snapshot `sha256sum .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/*/*.json` before and after. This is a recommendation, not a claim that I performed those hash snapshots in this round.

## Independent source-to-claim validation (expected for the new fixture; recommendation)

No prose-mapping test can be run against the absent fixture. Once authored, an independent reviewer should first print the actual file list and all relevant raw inputs, then compare each claim with excerpt text. Suggested read-only commands (replace `NEW_FIXTURE` and `EXCERPT_FILE` with the actual paths; no checker command can substitute for this semantic comparison):

```sh
find NEW_FIXTURE -maxdepth 2 -type f -print
cat NEW_FIXTURE/sources.json NEW_FIXTURE/entities.json NEW_FIXTURE/relations.json NEW_FIXTURE/timeline.json NEW_FIXTURE/contradictions.json
cat NEW_FIXTURE/EXCERPT_FILE
```

Expected mapping procedure: for every `entities[].first_appearance`, `entities[].claims[]`, `relations[]`, and `timeline[]` row, follow its `source_id` to exactly one source metadata row; locate its labeled excerpt; record the excerpt sentence and the precise fields it supports (identity, action/relation, place, and tick only if stated). Verify excerpts actually contain those details and flag unsupported, conflicting, or ambiguous claims rather than inferring them. For the additional registry perspective specifically, check that it independently states Mira and the departure/movement detail asserted by its event/claim; do not treat source metadata or a citation ID as textual corroboration. Record unsupported/ambiguous mappings as findings; checker success establishes only structural validity and citation identity. This mapping is a human review, not an automated pass/fail expected from `check_bible.py`.

## Recommendations, not observed results

- Keep the new fixture separate from `consistent/`; include clearly labeled fictional excerpt text and unique source IDs as required by the LOG declaration.
- Have a non-author run the checker on the new fixture and replay all 19 existing fixtures using the commands above; compare exact outputs and unchanged checker/fixture hashes. This report does not claim source-mapping validation of a new fixture or hash verification.
- Report excerpt-to-assertion mismatches explicitly; do not call checker-clean output proof of textual support, corroboration, or canon truth.
