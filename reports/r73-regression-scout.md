# Round 73 regression scout — pinned 131-tuple replay and r72 clone plan

## Scope and pin

Plan/evidence report only; no r73 candidate has been created. The Round 73 declaration is `.shokunin/lore/LOG.md`, “Round 73 — 2026-10-13T08:24:52.862998+00:00.” It pins clean baseline `af9d7c109b1b193da741d0851bd962ea9676b8e7`, requires all old 131 raw CLI tuples unchanged, and calls for a new five-table clone of r72. `git rev-parse HEAD` matched the pin when inspected. The worktree already had a modification to LOG; I did not change it. For baseline inspection/replay I extracted the fixture tree directly from the pinned Git archive, rather than treating working-tree files as the baseline.

The baseline fixture directory manifest contains **131** directories (SHA-256 of sorted newline-delimited names: `7c13aa85b7196bfa6dddbfceed3a52e927af7ea7a35f61c238dd44fedc2eeb3d`). The full fixture tree contains **725 files** including `README.md` and `check_bible.py` (sorted relative-path manifest SHA-256 `ce86fd955394393e70a53724dea07928267c89d262d4ee5fb438befa6280a149`). Baseline checker SHA-256 is `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81`; it is byte-identical in the inspected worktree.

## Baseline raw-tuple replay

For every one of the 131 pinned fixture directories, I ran from repository root with the declared root-relative command and identical argv at baseline and current checkout:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture-directory>
```

Each result was captured as `(process exit status, stdout bytes, stderr bytes)` without stream normalization. **131/131 tuples match exactly; no mismatches.** Baseline outcomes: 26 exit 0 and 105 exit 1. This includes delivered fixture `r72-vela-slate-claim`, which is part of this pin's old denominator, not a new r73 case. Across the complete baseline fixture tree, no old paths are missing or byte-changed in the inspected checkout, and there are no extra fixture-tree paths at this inspection point. This is evidence for the current checkout only; rerun the same pinned comparison after any candidate is added.

## Inherited excerpts and r72 clone plan

The declaration's relevant delivered fixture is `.shokunin/lore/corpus/fixtures/r72-vela-slate-claim/`, a 16-file r43-derived fixture. Its `vela-slate-note-excerpt.md` says Vela leaned close and read “KEEP THE EAST GATE CLEAR,” wondered whether the cramped letters meant the writer hurried, and could not tell who wrote them. Its cited Vela entity claim and `vela-slate-clause-map.md` map those three spans to source `vela-slate-note` and claim `/6/claims/1`; the source calls this a fictional, unverified account, not an authenticated slate or writer. `timeline.json`, `relations.json`, and `contradictions.json` are byte-identical to r43 in this delivered clone.

The inherited `jorin-note-excerpt.md` says: “I, Jorin, am a registrar, and I stood at the Lantern Harbor registry doorway. I saw Vela standing on the Lantern Harbor east steps during what I called Bell-7. I did not see who, if anyone, struck a bell.” Its `jorin-clause-map.md` attributes those statements to Jorin and explicitly cautions that the matching Bell-7 label does not establish shared occasion, chronology, or objective bell sounding. It reports neither reading a slate nor witnessing Vela read one. Neither inherited report states when slate wording was written or whether the same words remained visible.

Recommended append-only implementation check for the declared new clone (not an implementation or result):

1. Clone all five tables and other inherited r72 files without mutation. In `sources.json`, retain the entire old array in order and append only one distinct fictional Jorin report source. In `entities.json`, retain every old entity and claim, append exactly one attributed Jorin claim citing that source, and do not alter Vela's claim or other rows. The declaration calls for a Jorin first-person report of different words read on a slate at the east steps; keep it an account, not authentication or an assertion it is the same inscription/time as Vela's account.
2. Add the declared short excerpt, exact source-to-claim clause map, and concise editorial comparison note as new files. The note should describe a discrepancy in *reported wording* and preserve the bounded open question of slate identity/time/source; do not call the reports a direct contradiction or resolve either account. Map exact spans and pointers to the new source/claim.
3. Keep `relations.json`, `timeline.json`, and `contradictions.json` byte-identical to r72. Add no slate entity, event/tick, place assignment, dependency, relation, automatic contradiction row, or shared-time claim. A structural checker clean result cannot establish literal quotation, semantic support, meaningful depth, or source truth; non-author review is needed for those.
4. Separately replay all 131 pinned paths using the raw tuple procedure above; require exact status/stdout/stderr equality. Compare pinned old corpus path manifest and raw bytes, checker hash, and all inherited r72 clone paths. For r72-to-candidate, confirm only the declared source/claim append and new prose files differ; the protected three tables and all inherited excerpts/maps remain byte-identical. Run the new clone checker separately and record exact raw streams/status; it is not in the old denominator.

## Limits

I inspected the Round 73 declaration, r72 reports (executor, regression scout, independent verifier, axis adjudicator), r43/r72 inherited excerpt and map files, five-table baseline/clone data, checker implementation, and performed the pinned replay described above. I did not execute or validate an r73 candidate because none exists. The checker validates structure and references; it does not compare source prose, authenticate reports, establish an inscription/writer/time, or determine canon. This report makes no source-truth, canon, rights, or game-mechanics inference and no axis verdict. No source, fixture, checker, README, LOG, or other report was edited; only this requested report was written. No commit, push, or merge was made.
