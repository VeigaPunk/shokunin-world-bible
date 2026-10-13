# Round 72 regression scout — pinned 130-tuple replay and r43 clone plan

## Scope, pin, and evidence

Plan only. I inspected the Round 72 declaration in `.shokunin/lore/LOG.md`, the r43 fixture and regression report, the r71 regression report, and `.shokunin/lore/corpus/fixtures/check_bible.py`. I did not run a candidate replay or edit any fixture/checker/LOG/README file. The only intended write is this report.

The declared baseline is full commit `274906575c3462aabb9f27752513e7c588c511a5` (`git rev-parse HEAD` matched); the worktree has a pre-existing modification to `.shokunin/lore/LOG.md`, which I did not change. Treat the pinned commit as authority, not the mutable checkout. The latest prior regression report, r71, specifies the 130-old-fixture denominator and exact tuple method; r70 reported 130 fixtures and 709 tracked fixture paths (645 JSON) at its earlier pin. Re-enumerate at the r72 pin rather than assuming those historical counts/path manifests. The r43 regression report's 94/469 denominator is older and is not the r72 baseline.

The inherited fixture to clone is `.shokunin/lore/corpus/fixtures/r43-jorin-vela-sighting/`. Its `vela-note-excerpt.md` records Vela's east-steps position, hearing the registry bell twice during Bell-7, and not seeing Sella or an envelope; it is not a Vela slate-reading account. The r43 regression report describes its earlier scope and checker boundary, not this round's denominator. The Round 72 declaration calls for a **new r43-derived five-table fixture** with a new in-world source and exactly one cited Vela entity claim; no timeline event/dependency, relation, or contradiction. The specific new directory name is not fixed in the declaration; use the executor's declared candidate path and record it exactly, rather than presuming a path exists.

## Baseline replay: preserve all 130 raw tuples

1. At pinned commit `274906575c3462aabb9f27752513e7c588c511a5`, enumerate and save sorted immediate fixture-directory and fixture-tree path manifests. Confirm the 130 declared old directories against the round's applicable scope. If the count or scope differs, report actual count and exact delta; do not call it a 130-case result. Record checker bytes/hash and baseline raw outcomes.
2. For each old fixture, run from repository-root cwd with identical root-relative argv:
   `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture-directory>`
   Capture process exit status plus raw stdout and stderr bytes, keyed by fixture path. Do not normalize streams, compare only pass/fail, or rely on aggregate counts.
3. At candidate, run exactly the same command, cwd, and argv for every path in the pinned 130-directory manifest. Compare all three tuple components byte-for-byte. Require 130/130 exact matches and list every mismatch. Run the new clone separately and record its exact status/stdout/stderr; its result does not enter the old denominator.
4. Independently compare the full pinned fixture-tree path manifest and raw bytes against candidate: every old path must remain present and byte-identical; report missing, changed, and extra paths. Verify specifically that all inherited paths under `r43-jorin-vela-sighting/` are byte-identical in the new clone except the explicitly declared append-only source/claim changes. Compare the five JSON tables individually. Preserve unchanged `relations.json`, `timeline.json`, and `contradictions.json`; in `entities.json`, retain every existing row/field and append only the one Vela claim; in `sources.json`, retain all old rows and append only the cited new source. Verify excerpt/map additions and inherited non-JSON files explicitly. The clone is additive and must not excuse changes to any old-corpus path.
5. Pin/hash the checker at baseline and candidate and report any difference. A byte-identical old corpus with a changed checker is not an unchanged replay environment. A non-author verifier should retain manifests and hashes but use raw bytes as the equality criterion.

## Clone attribution checks and checker boundary

Inspect the actual new source row, Vela claim, excerpt, and clause-to-pointer map. The map should quote the excerpt literally and point to exact source/claim fields. Trace each reported observation separately from the tentative maker inference and its uncertainty. Confirm the claim cites the new source ID, and that the source is the in-world fictional report described by the excerpt. Check that prose and structured wording do not turn the tentative inference into identification of a writer, authenticated slate, provenance, event chronology, or canon. Do not add a timeline position or event, dependency, relation, contradiction, or resolution of inherited material.

Run the checker on the clone using the same root-relative command and report raw streams/status. The checker validates table structure, references, and declared structural rules; it does not parse excerpt language or prove exact quotation, clause entailment, perspective depth, source truth, chronology, or canon. A clean checker result is structural evidence only. Manual non-author review is needed for exact clause/citation correspondence and whether the report adds meaningful character perspective rather than decorative wording. Review depth, coverage, and calibration separately, per LOG; regression success alone does not establish improvement.

## Limits

This is a replay and clone-verification plan, not an observed candidate result or axis verdict. The r43/r71 reports establish prior procedures and reported evidence at their own pins, not r72 candidate outcomes. No conclusion is made about fictional source truth/canon, real-world rights or permissions, or game mechanics. No other file should be changed by this scout.
