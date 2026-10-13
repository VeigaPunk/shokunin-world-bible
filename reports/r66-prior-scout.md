# Round 66 prior-scout — active R59/R60 documentation calibration

## Scope and evidence

Read the R66 declaration in `LOG.md`, active `.shokunin/lore/corpus/fixtures/README.md` R59/R60 sections, historical `reports/r59-executor.md` / `r59-independent-verifier.md`, and `reports/r60-executor.md` / `r60-independent-verifier.md`; replayed the current checker on `r59-nested-duplicate/`. No files other than this report were changed.

## Exact active/history distinction

The active README R59 section currently says: “Other files are still checked; as shown by `r59-nested-duplicate/`, unloading an entity table can consequently produce dangling-reference findings in other tables. Those are consequences of missing loaded rows, not proof that entities are absent.” It further points readers to `r59-executor.md` “for raw candidate output and replay limits.” This is materially stale as a description of the named fixture's current output: current `check_bible.py` run on `.shokunin/lore/corpus/fixtures/r59-nested-duplicate` exits 1, stderr empty, and prints exactly:

```text
VIOLATION: entities.json: duplicate object member 'source_id'; cannot load JSON
1 violation(s); no canon changed
```

By contrast, `reports/r59-executor.md` accurately records the creation-time candidate output: the same load error plus six dangling findings for relation endpoints `mira`/`seal` and timeline entity/place references `mira`/`harbor`/`mira`/`tower`, total 7. `reports/r60-executor.md` identifies the intended later change: unavailable entity-index lookups are gated, and its parent-correction says current `r59-nested-duplicate` retains the load diagnostic alone (1 vs 7). The independent R60 verifier likewise identifies that exact delta. These reports are history and must not be edited or read as current output.

Active README R60 already says unavailable entity tables do not yield dangling/ambiguous/kind or derived conclusions; empty/partial loaded arrays still do. Its policy is therefore accurate, but its later placement does not qualify the R59 example at the point where an operator is told to inspect it. This is unlike a purely historical claim explicitly marked as creation-time: R59's “as shown by” plus link to raw candidate output invites current reproduction of an output that no longer occurs.

## Prior repair precedent and materiality

R48 corrected the actual local Vela maps; R50 separately corrected an active README instruction that still routed readers around those now-correct maps. R50's recorded reviewer judged that live navigation mismatch a modest reader-action calibration gain beyond R48, while R51 rejected a residual specialized warning because no consequential misreading was demonstrated. Applied here, this is closer to R50 than R51: the active R59 section points to a runnable fixture and historical raw output without a time qualification, and the current CLI demonstrably contradicts the implied behavior. R60's lower section mitigates the error for a reader who reads ahead, but does not make the R59 example/output pairing current. The likely operator mistake is expecting six dangling-reference findings when reproducing the named fixture, or treating the historical 7-count as the current expected result.

Independent materiality remains unproven by a reader study. I assess **conditional, narrow GO for calibration** only if a reviewer confirms that a reader following the R59 subsection could reasonably take its named example/raw-output link as current, and that a minimal local qualification changes that expectation. Suggested correction would label the six-dangling/7 result explicitly as R59 creation-time output, state that current R60 behavior reports only the duplicate-member load failure (1 total), and cross-reference the active R60 rule. Preserve all historical reports and the substantive original duplicate-member explanation. If R60's existing section is found to make the R59 wording unambiguously historical to an ordinary reader, or reviewer testing finds no changed expectation/action, NO-GO as redundant polish.

## Falsifier and boundaries

Falsifier: a blind reader given the active R59 subsection and its linked historical report correctly distinguishes R59's creation-time seven findings from the current one-finding output before any README qualification, and the proposed qualification does not improve that distinction. Conversely, a concise before/after reader check that prevents expectation of the six removed findings supports material calibration; this is not established by checker tests alone.

No checker, fixture, source excerpt, historical report, or canon change is indicated by this prior-art audit. The six old diagnostics were consequences of an unavailable index, not evidence of entity absence; neither 7 nor 1 findings establishes fictional-world facts, source-text truth, canon, rights, or permission. The round's proposed README-only move is not yet admitted; baseline replay/path verification and independent review remain necessary.
