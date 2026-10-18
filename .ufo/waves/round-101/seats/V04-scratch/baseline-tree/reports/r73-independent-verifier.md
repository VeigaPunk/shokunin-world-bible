# Round 73 independent verifier — pinned archive, raw replay, and append-only audit

## Scope and method

Verified the delivered candidate against pinned clean HEAD `af9d7c109b1b193da741d0851bd962ea9676b8e7`. Extracted `.shokunin/lore/corpus` from `git archive` of that commit to `/tmp/lore-r73-verifier`; compared sorted relative paths and SHA-256 of every regular file against the current `.shokunin/lore/corpus`. For baseline replay, ran both the archived checker+fixture tree and current checker+fixture tree from their respective repository roots, with the same root-relative command and argv for each old fixture:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture-directory>
```

Captured process return code, stdout bytes, and stderr bytes without normalization. Separately ran the current checker on the new candidate. The archive and working checkout checker have the same SHA-256: `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81`.

## Pinned old-corpus comparison

- Pinned corpus: **1,336 files**. Current corpus: **1,355 files**.
- Missing old paths: **0**. Changed old-file bytes: **1**, only `fixtures/README.md` (the declared Round 73 subsection). Added paths: **19**, all within `fixtures/r73-jorin-slate-claim/` (the 16 inherited r72 files plus three new prose files).
- No other old corpus file or path differs. The archived delivered r72 fixture has **16/16** paths present and byte-identical in the working tree.
- The pinned old fixture tree had **725 files**. Its old fixture content was not modified; the only modification within the old corpus fixture tree is the intended README subsection.

## Raw regression replay

All **131/131** pinned fixture invocations produced identical `(exit status, stdout bytes, stderr bytes)` from the archived baseline and current checkout. **No mismatches.** Baseline outcomes: **26** exit 0, **105** exit 1. The new fixture is outside the 131-fixture baseline denominator; separately it returns exit **0**, stdout bytes `CLEAN: schema, citations, relations, timeline; 0 violations
`, stderr empty.

## r72 clone and append-only source/claim audit

Compared `r73-jorin-slate-claim/` against delivered `r72-vela-slate-claim/` by filename and raw bytes:

- All **16/16** inherited filenames remain, with no omitted path. **14/16** inherited files are byte-identical.
- The only changed inherited files are `sources.json` and `entities.json`. `relations.json`, `timeline.json`, and `contradictions.json` are byte-identical to r72.
- `sources.json` retains the complete r72 array in order and appends exactly one row at `/7`: ID `jorin-slate-note`, a fictional unverified first-person report.
- `entities.json` retains the same eight entity rows/order. The existing `jorin` row at `/7` preserves its previous claim and appends exactly one claim at `/7/claims/1`, citing `jorin-slate-note`; no new entity or other claim change was observed.
- Exactly three files are new relative to the r72 fixture: `jorin-slate-note-excerpt.md`, `jorin-slate-clause-map.md`, and `editorial-comparison.md`.

The new excerpt literally reads: “I was sent to copy a gate notice. At the east steps, I read “KEEP THE EAST GATE OPEN” on a slate. I did not see who put it there.” The claim statement summarizes those three clauses as Jorin’s report and cites the new source. The clause map reproduces each excerpt span, including the nested curly quotes, and points to `/7/claims/1/statement`, `/7/claims/1/source_id`, and `sources.json` `/7/id`. The source ID resolves and is unique. I found no literal quotation or pointer mismatch in the excerpt/map/claim.

The editorial comparison quotes Vela’s r72 “KEEP THE EAST GATE CLEAR” and Jorin’s r73 “KEEP THE EAST GATE OPEN,” and says only that the reports give different wording. It leaves same-slate/inscription identity, reading time, and source relationship unresolved; it does not claim a direct contradiction or inscription change. The inherited Jorin Bell-7 account does not evidence his slate reading or show he witnessed Vela reading. No new event, relation, or contradiction record was added. The README’s Round 73 subsection describes the same limits.

## Limits

This verifies repository bytes, checker behavior, fixture structure/source-ID resolution, and literal excerpt/map/candidate consistency. The checker does not test Markdown maps or semantic support. This verification cannot establish source truth, the existence or identity of any slate/inscription, whether either wording was present, authorship, chronology, canon, depth, real-world rights, or game mechanics. In particular, byte preservation and different reported words do not establish that the reports concern one object or occasion, and this report makes no axis verdict.
