# Round 73 replay verifier — independent correction and audit

## Independence and scope

I did not use the previous verifier child’s report as evidence. I independently extracted the pinned commit `af9d7c109b1b193da741d0851bd962ea9676b8e7` with `git archive` into `/tmp/lore-r73-replay` (outside the repository), then replayed from that archive and the current checkout. The raw process results are retained outside the repository at `/tmp/lore-r73-raw-results.json`; the pinned corpus archive is at `/tmp/lore-r73-replay/.shokunin/lore/corpus`. No files in the corpus, `LOG.md`, or other reports were edited by this verification.

For each of the 131 fixture directories present at the pinned commit, I ran from each tree root the same command and fixture path:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>
```

I captured return code and unmodified stdout/stderr bytes. I separately ran the current checker on the new r73 fixture. This verifies the CLI behavior in this environment, not behavior across other Python versions/platforms.

## Pinned corpus and baseline replay

The pinned corpus contains 1,336 regular files; the current corpus contains 1,355. Comparing relative paths and raw SHA-256:

- No pinned path is missing.
- Exactly one pinned file differs: `fixtures/README.md` (the new Round 73 subsection).
- The 19 added paths are all under `fixtures/r73-jorin-slate-claim/`.
- The pinned and current checker bytes match (SHA-256 `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81`).
- The pinned fixture subtree contains 725 regular files; no old fixture file differs except `fixtures/README.md`.

All **131/131** old fixture runs match exactly on `(exit status, stdout bytes, stderr bytes)`. Baseline has 26 exit-0 and 105 exit-1 results. There were no mismatches. The new fixture, excluded from that baseline denominator, exits **0** with raw stdout `CLEAN: schema, citations, relations, timeline; 0 violations
` and empty stderr.

## r72 inheritance and append-only claim

The current r72 directory has 16 files and the r73 directory retains those same 16 names. Comparing raw bytes, 14 inherited files are unchanged. Only `sources.json` and `entities.json` differ; the inherited `relations.json`, `timeline.json`, and `contradictions.json` are byte-identical. The other three r73 files are `jorin-slate-note-excerpt.md`, `jorin-slate-clause-map.md`, and `editorial-comparison.md`.

The source array preserves all seven r72 rows, in order and byte-equivalent as parsed JSON, then appends one row at index `/7` with unique ID `jorin-slate-note`. The entity table preserves all eight rows and their order. The existing Jorin entity’s prior claim is unchanged; exactly one claim is appended to it at `/7/claims/1`, citing `jorin-slate-note`. No entity is added. These are structural observations, not proof that the fictional source exists or is true.

## Literal excerpt, pointers, and editorial boundary

The excerpt is exactly:

> I was sent to copy a gate notice. At the east steps, I read “KEEP THE EAST GATE OPEN” on a slate. I did not see who put it there.

The appended claim reports the assignment, the stated location and wording, and the reported limit on seeing the placer. The map quotes each corresponding excerpt span, includes the nested curly quotation marks literally, and points to `/7/claims/1/statement`, `/7/claims/1/source_id`, and `sources.json` `/7/id`. The ID resolves uniquely. I found no excerpt/map/claim literal mismatch. The checker does not validate Markdown maps or semantic entailment; this is a manual comparison.

The editorial comparison quotes Vela’s r72 “KEEP THE EAST GATE CLEAR” and Jorin’s r73 “KEEP THE EAST GATE OPEN,” and limits its conclusion to different reported wording. It leaves shared slate/inscription identity, reading time, and the source relationship unresolved; it does not assert inscription change or direct contradiction. No new relation, timeline event, or contradiction row is present. The README’s Round 73 summary states the same limits.

## Cross-check of prior report and limits

The previous `reports/r73-independent-verifier.md` is **untrusted telemetry**, not a source for this result. My independent measurements reproduce its central numerical and structural claims: all 131 baseline invocations match; the old corpus has one changed path (README) and no removed paths; the new fixture is clean; and the r72 inheritance/append-only account is accurate. I found no discrepancy requiring correction to those claims. This statement does not validate any evidence or procedure used by that child.

This audit establishes repository bytes, process outputs, fixture structure and literal editorial alignment only. It does not establish source truth, slate or inscription identity, authorship, chronology, canon, rights, or game mechanics; it makes no source-truth, canon, rights, or mechanics inference and no axis verdict.
