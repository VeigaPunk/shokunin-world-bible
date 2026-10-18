# Round 77 independent verifier — pinned preservation and Neri fixture

## Scope and method

Independently archived pinned commit `045e8dea173e8ff4d1821c4097f9bb1cceb268b2` outside the repository with `git archive` to `/tmp/lore-r77-independent-pin`. Compared raw relative-path manifests and bytes for the pinned and working-tree `.shokunin/lore/corpus`. Used the pinned raw tuple record `/tmp/lore-r77-baseline-tuples.json` (SHA-256 `4973d3bc9dbe71ff25988d2528d8eb278544d68616d6baf6cf5d2d0429d2809d`) to independently replay every old fixture from the repository root with the original relative CLI argv. No fixture command output was redirected into or emitted as an absolute-path artifact. No corpus, checker, or LOG files were edited.

## Pinned corpus and old-fixture replay

- Pinned corpus archive: **1,356 files**. Current corpus: **1,378 files**.
- All **1,356/1,356** pinned paths remain present and raw-byte-identical; **zero** pinned paths were removed or changed.
- The only corpus additions are the **22 files** under `fixtures/r77-neri-latch-report/` (enumerated below). The checker is unchanged; SHA-256 `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81`.
- Replayed the same **132** prior fixtures using `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>` and compared raw `(exit, stdout bytes, stderr bytes)` to the pinned tuple record: **132/132 exact**, comprising 27 exit 0 and 105 exit 1. This establishes preservation/replay, not depth or prose quality.

## Candidate against the declared r73 clone

The candidate has **22 files**; r73 has **19**. No inherited file is missing. Exactly two inherited files differ, both append-only JSON arrays:

- `sources.json`: all 8 old rows remain byte/value-identical and in order; one row appended at `/8`, ID `neri-gate-note`.
- `entities.json`: all 8 old rows remain byte/value-identical and in order; one row appended at `/8`, ID `neri`, with exactly one claim at `/8/claims/0` citing `neri-gate-note`.

The other **17 inherited files are byte-identical**. In particular `relations.json`, `timeline.json`, and `contradictions.json` are each raw-byte-identical to r73: no event, relation, or contradiction row was added or altered. The only three new paths relative to r73 are:

1. `editorial-question.md`
2. `neri-clause-map.md`
3. `neri-gate-note-excerpt.md`

The entire new-fixture addition relative to the pinned corpus is exactly: `clause-map.md`, `contradictions.json`, `editorial-comparison.md`, `editorial-question.md`, `entities.json`, `jorin-clause-map.md`, `jorin-note-excerpt.md`, `jorin-slate-clause-map.md`, `jorin-slate-note-excerpt.md`, `manual-clause-pointer-map.md`, `neri-clause-map.md`, `neri-gate-note-excerpt.md`, `relations.json`, `sella-bell7-note-excerpt.md`, `sources.json`, `strength-contrast-map.md`, `tarin-note-excerpt.md`, `timeline.json`, `vela-clause-map.md`, `vela-note-excerpt.md`, `vela-slate-clause-map.md`, and `vela-slate-note-excerpt.md`.

## Candidate checker and literal/pointer check

Root-relative CLI invocation `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r77-neri-latch-report` returned exit 0, stdout exactly `CLEAN: schema, citations, relations, timeline; 0 violations\n`, and empty stderr.

The excerpt file is exactly `I, Neri, tended a gate. Its latch caught only after I lifted it twice.\n`. The source row `/8` identifies a newly authored fictional, unverified first-person account, explicitly not an authenticated record or objective gate condition. Entity `/8`, claim `/8/claims/0` points to source ID `neri-gate-note`, which resolves to source `/8`. The claim attributes the report to Neri. The clause map quotes both excerpt sentences literally and maps both to that claim/source pointer; the editorial question is present and limits the detail to character attention to ordinary hardware rather than asserting an explanation or fact.

The new excerpt states no east-gate identity, time/watch, place, relation to Jorin/Vela, notice/slate, compliance, or causal/access conclusion. The fixture’s timeline, relations, and contradiction tables are inherited r73 data and unchanged; they do not contain a Neri entry. Structural pointers and CLEAN status do not establish source truth, canon, corroboration, or that the detail provides material narrative depth.

## Verdict / boundary

**Verification passes for old-corpus preservation, declared r73 clone/append-only shape, pointer/excerpt checks, and checker cleanliness.** This is not a finding that the one-axis depth hypothesis improved: preservation and structural validity cannot establish prose depth. No judgment here on source truth, canon, rights, or mechanics. No commits, push, or merge.
