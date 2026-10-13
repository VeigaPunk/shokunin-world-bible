# Round 30 regression scout — exact 80/399 replay plan

## Evidence and contract

- `.shokunin/lore/LOG.md:460` identifies baseline work/report commits `657da3259de1caab48c6ba8caeaab1baefb1ceec` / `533e36712a3acefe7aa2ccb7e03f44aeb20efdbd`, notes no r30 fixture at baseline, and states the checker does not read prose. `.shokunin/lore/LOG.md:461` declares the calibration move and requires 80 prior fixture stdout/stderr/exit outcomes and 399 prior JSON path bytes unchanged.
- `.shokunin/lore/corpus/fixtures/r28-courier-excerpt/relation-clause-map.md:5,9,13` maps the literal “I, Mira, carried the blue seal.” to `relations[0].type=carries`, conditional on explicitly editorial `mira`/`seal` ID alignment.
- `.shokunin/lore/corpus/fixtures/r29-near-miss/negative-clause-map.md:3-9` treats “The blue seal was near Mira” as **unsupported by this excerpt**, explicitly not contradicted or false; proximity does not entail carrying but also does not establish non-carrying.
- `.shokunin/lore/corpus/fixtures/r28-courier-excerpt/relations.json:2-6` holds the unchanged structured relation. It is not prose evidence. The r29 pair has `relations.json` and four other JSON tables that should be compared raw-byte-wise to r28 before constructing r30.

## Replay plan

1. In a disposable checkout of baseline `657da3259de1caab48c6ba8caeaab1baefb1ceec`, enumerate all 80 fixtures and 399 JSON relative paths. Record each fixture invocation’s exact argv/cwd, exit code, stdout bytes and stderr bytes; key results by fixture-relative path. Inventory raw bytes (or raw-byte-derived SHA-256 plus length) for every JSON path.
2. Run the same documented commands on the candidate, compare old fixture/path sets and per-path results without traversal-order dependence, and exclude only the new r30 fixture from the old-set comparison. Require exactly 80 old outcomes and 399 old JSON paths, with exact exit/stdout/stderr and byte identity. Do not regenerate the baseline from the candidate; report additions separately.
3. Run r28 positive, r29 near-miss, and r30 explicit-negation fixture checkers separately; each must exit 0. Compare all five r30 JSON tables raw-byte-identically to r28/r29. A named non-author reviewer must distinguish: r28 lexical support conditional on editorial ID alignment; r29 unsupported (not false); r30 **textual conflict** with the unchanged `carries` row conditional on those same alignments. Explicit negation is at most textual conflict, never canon falsity or proof resolving which record is true.
4. Verifier report records baseline revision, commands, counts, exact comparison outcomes and first mismatch. Any count/path mismatch, changed old bytes/outcome, changed JSON table, nonzero checker, or reviewer treating unsupported as false / textual conflict as canon false falsifies the claim; investigate rather than relaxing targets.

## Risks and falsifiable check

Raw-byte comparison is necessary; parsed JSON can miss formatting changes. Recursive discovery may have aggregate effects, so preserve old per-fixture runs and aggregate command behavior if available. Baseline counts are LOG claims until independently replayed: if baseline does not yield exactly 80/399, report discrepancy, do not adjust the target. Checker exit 0 establishes structure/reference consistency only, not prose interpretation. The explicit negative sentence can conflict with a positive record at the textual level, but it does not establish canon, resolve truth, prove source authenticity, or speak for other JSON claims.

Pass iff independent replay yields exact 80/80 old fixture outcomes and 399/399 old JSON bytes, all three fixture checkers exit 0, r30’s five tables match r28/r29 byte-for-byte, and non-author review preserves the support / unsupported / textual-conflict distinction with the latter bounded to this constructed excerpt and editorial ID alignment. This supports only the proposed calibration distinction; depth and coverage should remain unchanged.
