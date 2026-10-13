# Round 79 independent non-author verifier

## Method and regression result

Pinned HEAD was `46904644eba532247b263654058060ad763494ee`. I extracted its `.shokunin/lore/corpus` with `git archive` to `/tmp/lore-r79-pinned`; the extracted corpus is outside the repository. Compared every old corpus file by relative path and raw bytes with the working tree: all 1,356 old files exist and are byte-identical. There are no missing, modified, or removed old files. The working tree adds 21 files, all within the untracked `fixtures/r79-arrival-order-note/` fixture directory.

The pinned corpus has 132 fixture directories. For each directory I ran the checker from the root with root-relative arguments, once against the archive and once against the current tree:

```sh
cd <archive-root> && python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>
cd <working-tree-root> && python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>
```

All 132 archived/current triples `(exit status, stdout bytes, stderr bytes)` matched exactly. Thus all original fixtures retain their prior observed CLI behavior. This verifies regression parity, not the semantic correctness of checker rules or fictional assertions.

New fixture command and exact result:

```sh
cd <working-tree-root> && python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r79-arrival-order-note
```

- exit status: `0`
- stdout: `CLEAN: schema, citations, relations, timeline; 0 violations
`
- stderr: empty

## Clone and protected-record inspection

Compared `fixtures/r79-arrival-order-note/` against its stated predecessor `fixtures/r73-jorin-slate-claim/`. The 17 shared files other than `entities.json` and `sources.json` are byte-identical, including all inherited excerpt/maps and the three protected tables: `timeline.json`, `relations.json`, and `contradictions.json`. The old rows of both changed JSON files are exact prefixes of the new arrays (8/8 sources and 8/8 entities). The new source row and entity row are appended; no existing row was changed or reordered. Timeline remains six rows byte-for-byte equal; relations remains one row; contradictions remains one row. In particular the Bell-7 location-report ledger and its unresolved wording are unchanged.

The added source is `sources.json` row `/8`, ID `iren-arrival-order-note`, titled “Iren’s arrival-order note”; its reliability note explicitly calls it newly authored, fictional, unverified first-person account, not an authenticated record or established procedure. Added entity is `entities.json` row `/8`, ID `iren`, first appearance `iren-arrival-order-note`; its sole claim at `/8/claims/0` is attributed to that source.

## Excerpt and pointer audit

`iren-arrival-order-note-excerpt.md` labels itself newly authored fictional, unverified prose and says it is not authenticated. Its exact prose is:

> I wrote the names in the order people reached my desk, not the order the clerk called them. If I copied the clerk’s order, the people who had waited longest would look as though they came last.

`iren-arrival-order-clause-map.md` gives exact-span alignments to `entities.json` `/8/claims/0/statement`; both clause alignments point through `/8/claims/0/source_id` to `sources.json` `/8/id` (`iren-arrival-order-note`). Its source-row pointer `/8` agrees. The entity statement is an attribution/paraphrase of the excerpt, not verbatim quotation. The map explicitly limits this to Iren’s report and says the citation proves fixture attribution only—not truth, authenticity, canon, or institutional practice. The map’s narrow editorial choice (arrival-order display for the hypothetical scene) is clearly identified as a fiction-local presentation choice, not an established rule. It also expressly says the checker does not validate quotation, clause alignment, or editorial rationale.

The pointer paths resolve structurally to the intended IDs/rows. The checker’s clean result establishes only the validations it implements (schema, citations, relations, timeline); it is not evidence that these files accurately quote one another, that a desk/list/queue/clerk existed, that the account is true, or that arrival order is materially preferable beyond the stipulated fictional scene. Those remain editorial judgments about fictional prose, separate from structural integrity and ID resolution.
