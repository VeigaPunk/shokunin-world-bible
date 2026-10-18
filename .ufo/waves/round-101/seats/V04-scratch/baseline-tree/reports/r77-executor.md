# Round 77 executor report — Neri latch report

## Scope and delivered files

Implemented the narrowed, attributed-fiction candidate after reading the active r77 declaration and its narrowing correction/synthesis, all eight scout reports, r73 fixture source/entity/excerpt/map material, and `check_bible.py`. I changed only the new fixture directory and this report; no README, checker, LOG, or inherited fixture was edited.

New files under `corpus/fixtures/r77-neri-latch-report/`:
- `sources.json` — appended newly authored, fictional, unverified source `neri-gate-note` at `/8`.
- `entities.json` — appended character `neri` at `/8`, with one cited attributed claim at `/8/claims/0` citing `neri-gate-note`.
- `neri-gate-note-excerpt.md` — “I, Neri, tended a gate. Its latch caught only after I lifted it twice.”
- `neri-clause-map.md` — exact excerpt span-to-source/claim pointer map and attribution limits.
- `editorial-question.md` — short question: what Neri’s repeated tactile adjustment suggests about character attention to ordinary hardware; asks whether it yields useful character/setting depth rather than decorative texture.

The fixture is a clone of `r73-jorin-slate-claim`. Every inherited file other than the two append-only JSON tables is byte-identical. The tables retain the original arrays and append one row each. `relations.json`, `timeline.json`, and `contradictions.json` remain byte-identical; no place, event, relation, contradiction, or additional claim rows were added.

## Self-critique and limits

The editorial question is deliberately not “what did the latch mean for the notice?” It remains about a fictional character’s tactile attention and could be judged without any role label or slate linkage; the excerpt uses only “tended a gate,” not “gatekeeper.” However, this is still a very small detail. Its material character/setting value is **unproven** until a non-author reviewer judges it more than decorative texture. It is not a factual question answered by existing evidence.

No east gate, east steps, notice, slogan, Bell-7, watch, time, place, relation to r73 characters/readings, physical gate fact, objective condition, causal account, access outcome, or canon assertion appears in the new passage. Source/claim pointers establish attribution structure only, not authentication, corroboration, or world truth. No rights or game-mechanics claim is made.

## Validation

- Candidate checker invocation: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r77-neri-latch-report` → exit 0, exact stdout `CLEAN: schema, citations, relations, timeline; 0 violations\n`, empty stderr.
- Old raw replay: from repository root, ran the same CLI command/argv for all 132 prior fixture directories and compared `(exit, stdout bytes, stderr bytes)` to `/tmp/lore-r77-baseline-tuples.json`: **132/132 exact matches** (27 exit 0; 105 exit 1). The first attempted replay passed absolute fixture paths and differed for five diagnostics whose output embeds the command path; those were invocation-path mismatches, not corpus changes. Re-running with the original relative paths yielded exact matches. This replay does not assess material depth or prose semantics.
- The checker result and inherited-file byte checks are structural only; no reviewer judgment or candidate-wide corpus archive comparison is claimed here.

No commit, push, or merge was made.
