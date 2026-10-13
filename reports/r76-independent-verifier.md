# Round 76 independent verifier — pinned preservation and Jorin pointer check

## Scope and method

Pinned baseline: `edf3060033331c403f00e6d29b8e78e3f91c2e61`. I extracted `.shokunin/lore/corpus` with `git archive` to `/tmp/lore-r76-independent-pin` (outside the repository). No candidate fixture was present at verification time. I made no edits to corpus, checker, LOG, or any other report; this file is the only file written by this verifier. No commit, push, or merge.

I compared every regular corpus file by relative path and raw bytes between the pinned archive and current corpus. I independently ran the checker for every pinned fixture directory, once against the archive and once against the current checkout, using the same root-relative symlinked execution path, working directory, argv, and Python executable. I compared `(exit status, raw stdout bytes, raw stderr bytes)` without normalizing output.

## Findings

- **Corpus baseline preservation:** 1,356/1,356 relative paths match; all 1,356 raw file contents match. No added, removed, or changed corpus file was present. This includes 132 fixture directories and 744 fixture files.
- **Old fixture replay:** 132/132 pinned fixture tuples exactly match current tuples across exit status, stdout bytes, and stderr bytes. Both runs have 27 exit 0 and 105 exit 1. This establishes baseline preservation only; it is not evidence of a candidate’s behavior.
- **r73 Jorin excerpt:** `r73-jorin-slate-claim/jorin-slate-note-excerpt.md` reads exactly: “I was sent to copy a gate notice. At the east steps, I read “KEEP THE EAST GATE OPEN” on a slate. I did not see who put it there.”
- **Source and claim pointers:** `sources.json` row `/7` has ID `jorin-slate-note`, titled “Jorin’s east-steps slate note,” and labels it newly authored, fictional, unverified first-person report. `entities.json` row `/7` is Jorin; `claims[1]` states Jorin reports that he was sent to copy a gate notice, read the quoted words on a slate at the east steps, and did not see who put it there; its `source_id` is `jorin-slate-note`, resolving to the source row. The earlier Jorin claim is separately attributed to `jorin-note`.
- **Clause map and comparison:** `jorin-slate-clause-map.md` quotes all three excerpt clauses and maps them to `/7/claims/1` and `/7/claims/1/source_id` → `/7/id`; it explicitly labels the claim alignment as paraphrase and records the unspecified sender/time/placer limits. The editorial comparison correctly characterizes the two accounts as separately reported “CLEAR” and “OPEN” wording, with same slate/inscription, reading time, source relationship, inscription change, and direct contradiction unresolved. These are document-level pointer/wording checks, not checker guarantees.

## Candidate validation status and limits

There is **no r76 candidate** in the corpus: no new `r76-gate-copy-request` fixture, registry excerpt, source/claim addition, clause map, or comparison was available to validate. Consequently, this report does not claim candidate structural cleanliness, candidate pointer correctness, old-tuple preservation after a candidate, or any candidate depth/calibration result. Do not treat the 1,356-file equality and 132/132 replay above as candidate validation.

The existing r73 excerpt already contains Jorin’s own report that he was sent to copy a gate notice. A later newly authored fictional registry entry would be a second authored attribution in the fixture, not authenticated independent corroboration merely by having a separate source ID or institutional-sounding label. This verification establishes neither tasking truth, sender identity, receipt/compliance, source independence, slate/inscription identity, chronology, canon, rights, nor game mechanics.
