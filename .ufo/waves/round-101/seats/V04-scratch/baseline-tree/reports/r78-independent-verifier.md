# Round 78 independent verifier

## Scope and pinned archive

Independent, report-only verification against baseline pin `dd47e67387b05705e819e04c4176eb07ad0fb00d`. I read the active Round 78 LOG declaration, Round 78 scout reports, the fixture README, and active checker. I made no changes to corpus, checker, README, or LOG. There is no Round 78 candidate to verify.

Archived the pinned `.shokunin/lore/corpus` outside the repository at `/tmp/lore-r78-independent-verifier/archive/.shokunin/lore/corpus` using `git archive`. The archive contains 1,356 files. Comparing complete relative-path manifests and SHA-256 of raw file bytes against the current corpus: **1,356/1,356 identical**, with no missing, added, or differing paths. The archived checker SHA-256 is `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81`.

## Pinned fixture replay

From the archive root, replayed all 132 immediate fixture directories using root-relative argv and the archived checker:

`python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture-directory>`

Ran the same 132 commands from the repository root with the checkout checker. Compared exact `(exit status, stdout bytes, stderr bytes)` for every fixture: **132/132 exact matches**. The pinned baseline has 27 exit-0 and 105 exit-1 fixtures. No normalization was applied. This confirms baseline preservation/replay only; it is not a post-candidate regression result.

## Temporary r35 controls

Made three isolated copies of pinned `r35-bell7-conflict` under `/tmp/lore-r78-independent-verifier/r35/`; only `contradictions.json` `claim_a` was varied. The unique pointed event `tarin-envelope-observation` has event-level `source_id` `tarin-note`. The absent case keeps the original side; matching adds `source_id: "tarin-note"`; conflicting adds `source_id: "sella-bell7-note"`. Ran the checkout checker against each temporary directory. Exact outcomes:

| Side source field | Exit | stdout | stderr |
|---|---:|---|---|
| absent | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations
` | empty |
| matching `tarin-note` | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations
` | empty |
| conflicting `sella-bell7-note` | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations
` | empty |

This reproduces silent handling of the optional side member in these controls. README Round 3 documents side pointers as `(event_id, field)` and assigns citation to the event's own source; active checker likewise resolves the event and its source, not the copied side member. The result does not prove that readers are misled, that the optional member is forbidden, or that a new diagnostic would improve review. It does not establish source-text support or any story fact.

## Verdict and limits

**No candidate and no improvement proof.** The archived corpus and raw fixture replay establish the pinned baseline only. The three temporary controls establish their exact current outcomes only. They do not justify a checker, schema, or documentation change, and they do not constitute candidate validation. No finding about source truth/authenticity, canon, rights, chronology, or mechanics is made.
