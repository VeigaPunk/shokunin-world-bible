# Round 75 independent verifier — coverage leaf

## Scope and method

- **No implementation candidate.** The checked-out tree is still pinned at `58edd17eb080fc707e959bf3dfc56d01afa54234`; I made no corpus, checker, LOG, commit, push, or merge changes.
- Independently archived that pinned commit's `.shokunin/lore/corpus` with `git archive` into `/tmp/r75-independent-0s3js8p8/archive/.shokunin/lore/corpus` (outside the repository). Compared the archived corpus against the current tree by relative file path and raw bytes.
- Replayed each of the 132 directories under `fixtures/` using the archived and current checkers. Each invocation ran `python3 fixtures/check_bible.py fixtures/<fixture>` with that corpus root as cwd. Compared exit status, stdout bytes, and stderr bytes.
- Made three independent temporary copies of `fixtures/consistent` under `/tmp/r75-independent-0s3js8p8/probes/`; only `relations.json` was changed in each. These are probes of current no-candidate behavior, not candidate changes.

## Results

- Corpus comparison: **1,356 files on each side; identical path sets and raw bytes** (no extra or missing paths, no differing file contents).
- Fixture replay: **132/132 exact matches** for exit status, raw stdout, and raw stderr between archived and current roots. No mismatch.
- Temporary relation probes, with exact raw CLI outcome:

| Probe | Relation mutation | Exit | stdout | stderr |
|---|---|---:|---|---|
| Exact duplicate | Duplicated the existing `mira → seal`, `carries`, `courier-log` relation byte-equivalently as a second JSON row. | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations\n` | empty |
| Same edge, different valid source ID | Added the same endpoints/type with `source_id: "archive-ledger"` (a source ID present in `consistent/sources.json`). | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations\n` | empty |
| Reverse carries edge | Added `seal → mira`, `carries`, `courier-log`. | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations\n` | empty |

These are raw checker outcomes on isolated temporary copies only. **No improvement proof** is claimed: no implementation candidate was supplied or tested, and these probes do not establish a desired policy or broader behavior. No registry-depth idea is proposed. No source-of-truth, canon, rights, or game-mechanics inference is made.
