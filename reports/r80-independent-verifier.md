# Round 80 independent verifier — pinned archive and map-crossing candidate

## Method and corpus regression

Archived commit `e665e76abec8e88bd87c39f8cfe38877fedf43ed` outside the repository at `/tmp/lore-r80-baseline-e665e76` with `git archive`. Compared every old `.shokunin/lore/corpus` relative path and raw file bytes against the working tree: **1,356/1,356 old paths present and byte-identical**, **0 missing**, **0 changed**. The working corpus has **21 additional paths**, all under `fixtures/r80-map-crossing-response/`.

Replayed each of the **132** archived fixture directories against both archive and working checkout, invoking from each root with the same root-relative argv: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture-dir>`. Compared each exact `(exit status, stdout bytes, stderr bytes)` tuple: **132/132 exact matches; 0 mismatches**. Both versions have **27 exit 0** and **105 exit 1**. The failure outputs are expected fixture controls, unchanged by this candidate.

## Candidate preservation and structure

Compared `r80-map-crossing-response` to `r73-jorin-slate-claim`: it contains all **19 inherited relative paths**. The **17 non-append-target files** are byte-identical. `relations.json`, `timeline.json`, and `contradictions.json` are byte-identical; no rows or links were added there. The source and entity arrays preserve the old **8/8 rows and ordering** exactly, then append one row each (9 total apiece): source at `/8` with ID `r80-map-crossing-note`, and narrator character entity at `/8` with claim `/8/claims/0`, whose `source_id` is `r80-map-crossing-note`.

The new fixture has **21 files**. Its excerpt’s exact text is: “I laid my map between us with a marked crossing toward the door. Mara turned it around and tapped a different crossing.” The excerpt attributes both clauses to a newly authored fictional, unverified narrator account. The clause map points both spans to `entities.json` `/8/claims/0/statement`, and points the cited source to `sources.json` `/8` / `/8/id`; the claim’s source pointer is `/8/claims/0/source_id`. The claim paraphrases both actions. The map limits alternatives to the scene framing and explicitly avoids asserting motive, objective disagreement, agreement, outcome, real/canonical geography, shared slate, relationship, or chronology. Mara is not represented as an independently sourced entity.

Exact new-fixture checker invocation from repository root:
`python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r80-map-crossing-response`

Result: **exit 0**; stdout exactly `CLEAN: schema, citations, relations, timeline; 0 violations
`; stderr **0 bytes**.

## Interpretation boundary

These checks establish preservation, structural citation-ID resolution, and replay stability. They do **not** validate Markdown-to-claim semantic entailment, source authenticity, fiction truth, canon, rights, mechanics, or editorial merit. I independently inspected the actual excerpt, claim, clause map, and blind reader/reviewer materials. The clauses support a literal framing difference—one marked crossing is followed by Mara tapping another. The candidate itself does not establish objective disagreement or a consequential choice. The independent reviewer likewise finds a text-supported framing distinction but **no demonstrated material depth beyond restaging the newly authored second beat**. Structural cleanliness is not a depth or truth verdict; no material-depth improvement is established by this verification.

No corpus, checker, LOG, or other file was edited. This report is the sole verifier output.
