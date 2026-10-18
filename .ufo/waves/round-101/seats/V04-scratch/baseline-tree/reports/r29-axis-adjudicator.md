# Round 29 — final non-author axis adjudication

**Verdict: admit.** Calibration **improved**; depth **unchanged**; coverage **unchanged**. No axis harmed. The improvement is a bounded human positive/negative decision on one unchanged relation, not a new checker capability or a determination of story truth.

## Independent replay and inspection

I read the r29 declaration and post-scout policy in `LOG.md`, the r28 positive excerpt/map, r29 negative excerpt/map, the r29 non-author reviewer and independent verifier reports, and the fixtures README. I independently extracted the baseline checker from `5ca92778c86b47bdc06c9cd971a82334c501359f` and ran it and the current checker with `python3` on **79/79** pre-r29 fixture directories. Their stdout bytes, stderr bytes, and exit codes matched exactly for each directory. All **394/394** baseline fixture JSON paths retain identical working-tree bytes. The five r29 JSON tables are each byte-identical to the r28 positive tables. Both positive and negative fixture checker runs exit **0**, emit exactly `CLEAN: schema, citations, relations, timeline; 0 violations\n` on stdout, and emit empty stderr. The checker reads JSON, not Markdown; these results are structural only.

The selected unchanged record is `relations[0] = {from: mira, to: seal, type: carries, source_id: courier-log}`. The r28 newly authored fictional clause, “I, Mira, carried the blue seal,” supplies a carrying verb with the named speaker as actor and seal as object. It supports this narrow encoding **conditional on** the fixture-local editorial alignments of “Mira” to `mira` and “the blue seal” to `seal`; the words alone do not prove those ID matches. The r29 newly authored fictional clause, “The blue seal was near Mira,” supplies proximity but no carrying action. Its negative map correctly labels only `relations[0].type=carries` **UNSUPPORTED BY THIS EXCERPT**, not contradicted or false: proximity neither entails carrying nor rules it out. The non-author reviewer independently makes this same bounded distinction, and the independent verifier reports the same replay counts and clean structural outcomes.

## Axis decision and boundary

- **Calibration improved:** the committed paired negative control, unlike r28's hypothetical near-miss mention, makes an unchanged structurally clean `carries` row fail a manual *support* test while the positive clause conditionally passes. The map refuses to turn missing support into falsity.
- **Depth unchanged:** the positive clause-to-relation reading remains r28's existing manual depth; the negative control adds no further source-to-record detail or support for other rows.
- **Coverage unchanged:** no checker rule or JSON input shape changed. The added fictional Markdown pair is not parsed by the checker.

At least one axis improves and none is harmed, so the declared admission rule holds. `courier-log` is a fixture source ID, not proof of source authenticity. Neither clean structure nor either authored clause proves the relation true, establishes other JSON claims, resolves canon, or establishes rights. No SHONEN checkmark, promotion, push, or merge follows from this verdict.
