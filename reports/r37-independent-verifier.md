# Round 37 independent verifier

## Reproducible method and results

Pinned baseline report commit: `4e5dacf413d727595aec80ffc1f2e0e2a17f4f84`. Enumerated fixture JSON paths using `git ls-tree -r --name-only <commit> -- .shokunin/lore/corpus/fixtures`; derived the 88 fixture directories and 439 `.json` paths. Extracted the pinned fixture tree, including `check_bible.py`, with `git archive` to a temporary directory. For each directory, from each respective repository root, ran the identical argv:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py <root-relative-fixture-directory>
```

Captured each process return code and raw stdout/stderr bytes. Current worktree versus extracted baseline matched exactly for **88/88** directory invocations (exit, stdout bytes, stderr bytes). Compared every enumerated baseline JSON path byte-for-byte against the current worktree: **439/439 equal**.

Independently ran the same root-relative checker argv on each r37 fixture from the working-tree root. Unique control: exit **0**, stdout bytes decode to `CLEAN: schema, citations, relations, timeline; 0 violations\n`, stderr empty. Ambiguous case: exit **1**, stdout bytes decode exactly to:

```text
VIOLATION: timeline[4].id: duplicate timeline id 'tarin-envelope-observation'
VIOLATION: contradictions[0].claim_a.event_id: expected exactly one timeline event 'tarin-envelope-observation'
2 violation(s); no canon changed
```

stderr empty. Thus all output, not just the expected lines, was inventoried; exactly two findings occurred.

Compared r35 `r35-bell7-conflict` to the r37 copies across its nine inherited files: the unique fixture has all **9/9 byte-identical**. Ambiguous fixture differs only in `timeline.json`; its original four event objects are unchanged/in order, with the existing Tarin event appended as index 4. In the ambiguous data the Tarin ID occurs twice, Sella ID once, and the contradiction ledger has one target pair; checker output reports `claim_a.event_id` cardinality failure only, with `claim_b` unique. Source/excerpt and ledger files are unchanged.

## Limits

This establishes exact CLI-output regression for the 88 pinned fixtures and exact bytes for their 439 JSON inputs in the tested Python/runtime and filesystem, not general checker correctness. It does not establish Markdown/source truth, identity, chronology, canon, rights, or permission. The duplicate is an input alias that makes the Tarin ledger endpoint non-unique for this case; it does not select a canonical row, add a source claim, or resolve the attributed accounts. The coverage claim is limited to the previously untested two-sided ledger endpoint-cardinality case; generic duplicate-ID behavior was already covered elsewhere. No checker change was tested or claimed.
