# Round 34 independent verifier

Independent replay against baseline `e717c7430db82b46c8aa9255dbf78504c770ca59`.

## Reproduction

From repository root, extract the baseline checker and replay each fixture directory enumerated by JSON paths in the baseline tree. For each directory, compare the raw stdout, stderr, and exit code of the baseline checker and current checker with the same Python 3 interpreter and fixture argument:

```sh
git show e717c7430db82b46c8aa9255dbf78504c770ca59:.shokunin/lore/corpus/fixtures/check_bible.py > /tmp/r34-baseline-checker.py
# Repeat for each baseline fixture directory:
python3 /tmp/r34-baseline-checker.py .shokunin/lore/corpus/fixtures/<fixture>
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>
```

Captured stdout/stderr bytes and exit status for all **85/85** baseline fixture directories; every triple matched exactly. Compared each baseline JSON path's current bytes with `git show e717c7430db82b46c8aa9255dbf78504c770ca59:<path>`: **424/424 unchanged**. The five r34 tables (`sources.json`, `entities.json`, `relations.json`, `contradictions.json`, `timeline.json`) are each byte-identical to r33's corresponding table.

Run the current checker against both prose variants:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r33-tarin-envelope
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r34-tarin-hearsay
```

Both exited **0**, stdout exactly `CLEAN: schema, citations, relations, timeline; 0 violations
`, stderr empty. r34 contains `tarin-note-excerpt.md` and `modality-contrast-map.md`; the checker reads JSON table paths only (`read_text` at checker line 24), not Markdown. Therefore this clean result validates structural JSON consistency, not the modality prose or correspondence between prose and unchanged records.

## Limits

This replay verifies deterministic checker behavior, byte preservation, and structural cleanliness only. It does not establish whether Tarin saw or heard anything, whether the placement occurred, or the truth/reliability of any attributed report. The new prose/map are observed present; their semantic interpretation requires manual review. No inference about the envelope's contents, ownership, recipient, motive, links to other items, canon, rights, or training permission follows.
