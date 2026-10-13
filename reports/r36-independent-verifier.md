# Round 36 independent verifier report

## Method and results

I treated `356f75b32afed9abb85687689c8d5f55965c0cb3` as the pinned r35 baseline report commit. I enumerated its fixture JSON paths with `git ls-tree -r --name-only` and derived the 87 distinct fixture directories and 434 JSON paths. I extracted that commit’s fixture tree with `git archive` into a temporary directory, including the baseline `check_bible.py`.

For every baseline directory, from the repository root I invoked `python3 .shokunin/lore/corpus/fixtures/check_bible.py <root-relative fixture directory>` against both the current worktree and the extracted baseline tree, retaining each process exit status, raw stdout bytes, and raw stderr bytes. Result: exact equality **87/87**. Keeping argv root-relative and cwd at the same repository-root position preserves the path spellings in diagnostics, including `r5-missing-file`; this avoids treating absolute temporary paths as equivalent. Separately compared each of the 434 baseline JSON files byte-for-byte with its current-worktree path: **434/434 equal**.

Compared the r36 controlled fixture with r35 `633ba022b45c71a9049664e1d9ac181950820aee`: all five JSON files are byte-identical. Among the nine inherited r35 fixture files, the only difference is `sella-bell7-note-excerpt.md`; its explicit date changes from the seventh to the eighth day of Embermonth, year 12. The new `date-contrast-map.md` is additional editorial commentary. The map accurately calls out the unchanged Sella timeline description and contradiction-ledger rationale as still asserting seventh day without support from the changed excerpt, and notes the “that same Bell-7 ringing” tension rather than treating it as proof of shared occasion.

Ran the current checker from the repository root on both `.shokunin/lore/corpus/fixtures/r35-bell7-conflict` and `.shokunin/lore/corpus/fixtures/r36-bell7-wrong-date`. Both returned exit **0**, stdout exactly `CLEAN: schema, citations, relations, timeline; 0 violations
`, and empty stderr.

## Limits

The regression replay establishes byte-identical CLI behavior for these 87 baseline inputs under the tested Python/runtime and filesystem, not general correctness or semantic prose checking. The checker reads JSON structure and does not validate the Markdown excerpts, their truth/authenticity, source support, identity alignment, date accuracy, canon, rights, or permission. The r35/r36 comparison verifies the specified textual mutation and map, but does not establish which account is true or that the accounts describe different real-world occasions. The fixture’s local tick is not an absolute date.
