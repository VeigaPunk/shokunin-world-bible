# Round 73 replay verifier — independent pinned replay

## Scope and reproducible method

Verified current working tree against pinned clean HEAD `af9d7c109b1b193da741d0851bd962ea9676b8e7`. The checkout `HEAD` is that pin. Archived only the baseline corpus using:

```sh
git archive af9d7c109b1b193da741d0851bd962ea9676b8e7 .shokunin/lore/corpus | tar -x -C /tmp/lore-r73-replay-current
```

Compared sorted relative file paths and raw bytes under archived and working `.shokunin/lore/corpus`. For each of the 131 baseline fixture directories, ran the same argv from each tree's corresponding repository root and captured the process return code plus unmodified stdout/stderr bytes:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture-directory>
```

The archives were exercised separately (cwd `/tmp/lore-r73-replay-current` for baseline, checkout root for current); the script path and fixture argument above are root-relative and identical. No output normalization or exit-category-only comparison was used. Checker SHA-256 is `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81` in both trees.

## Pinned corpus and regression results

- Archived baseline: **1,336 files**. Current corpus: **1,355 files**.
- Missing baseline paths: **0**. Raw-byte-changed baseline paths: **1**, `fixtures/README.md` (Round 73 subsection). Added paths: **19**, all under `fixtures/r73-jorin-slate-claim/`.
- The baseline fixture tree contains **131** fixture directories / **725** files. All **131/131** old invocations have identical `(return code, stdout bytes, stderr bytes)` on baseline and current trees; mismatches: **0**. Baseline exit counts: 26 exit 0, 105 exit 1.
- Separately ran the current checker on `r73-jorin-slate-claim`: exit 0, stdout bytes are `CLEAN: schema, citations, relations, timeline; 0 violations\n`, stderr empty.

## Clone and source/claim append audit

Compared current `r73-jorin-slate-claim/` with delivered `r72-vela-slate-claim/` by relative filenames and raw bytes. All **16/16** inherited paths are present; **14/16** are byte-identical. Only `sources.json` and `entities.json` differ. `relations.json`, `timeline.json`, and `contradictions.json` remain byte-identical. Three new files are `jorin-slate-note-excerpt.md`, `jorin-slate-clause-map.md`, and `editorial-comparison.md`.

Parsed JSON and compared records: `sources.json` preserves the entire r72 source array and order, then appends exactly one source at `/7`, ID `jorin-slate-note`. The `jorin` entity retains its previous claim and appends exactly one claim at `/7/claims/1`, citing that source; no other entity/claim row changed. The source ID is present and unique. No timeline event, relation, or contradiction row was added or changed.

The excerpt text is exactly:

> I was sent to copy a gate notice. At the east steps, I read “KEEP THE EAST GATE OPEN” on a slate. I did not see who put it there.

The clause map contains that complete literal excerpt once and its three clause spans, including the nested curly quotation, exactly match the excerpt. Its pointers identify `/7/claims/1/statement`, `/7/claims/1/source_id`, and `sources.json` `/7/id`; it labels the claim alignment as paraphrase. No excerpt/map literal or pointer mismatch found. The claim says Jorin reports his assignment, reading, and not seeing who placed the slate.

The editorial note quotes Vela's r72 wording (“KEEP THE EAST GATE CLEAR”) and Jorin's r73 wording (“KEEP THE EAST GATE OPEN”), calls them different reported wording, and explicitly leaves same-slate/inscription identity, reading time, and source relationship unresolved. It does not say they concern the same object or occasion, does not establish a changed inscription, and does not assert direct contradiction. The README subsection describes the same scope limits.

## Discrepancy against provisional worker report and limits

Independent replay confirms the provisional `r73-independent-verifier.md`'s corpus counts, lone old-byte change, 131 raw replay result, and 14/16 clone-byte result. I did not copy its conclusions. One wording distinction: its “archived delivered r72 fixture has 16/16 paths ... byte-identical” describes the unchanged r72 source fixture in the working tree; it should not be read as claiming all clone-to-clone files are identical. The r73 clone differs in the two appended JSON files as detailed above. No result discrepancy found.

This verifies repository contents, checker replay, structural/source-ID integrity, and literal excerpt/map consistency only. The checker does not validate prose maps or semantic support. No inference here establishes source truth, a real slate/inscription, common object or time, authorship, canon, game mechanics, real-world rights, or a depth/axis verdict.
