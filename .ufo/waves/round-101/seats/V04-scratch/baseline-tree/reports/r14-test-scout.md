# Round 14 test scout — baseline replay and correspondence method

## Scope and method

Observed repository state: `HEAD` is `319d3101a7d2396a2170da1fd677be6a00dba0ef` (round-13 report commit); the working tree already had `.shokunin/lore/LOG.md` modified on entry. I did not edit that file or any fixture/checker. In this repo, `.shokunin/lore/corpus/fixtures/` contains 28 fixture directories. I replayed each with the raw CLI form `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>` and captured stdout, stderr, and exit status under `/tmp/r14-replay/` (current) and `/tmp/r14-replay/*.baseline.*` (baseline). For baseline I extracted the checker from the declared baseline commit using `git show 319d3101a7d2396a2170da1fd677be6a00dba0ef:.shokunin/lore/corpus/fixtures/check_bible.py > /tmp/r14-check-bible-baseline.py`.

## Observed replay results

- All 28 current fixture replays completed; stderr was empty for all 28.
- Current and extracted-baseline stdout bytes, stderr bytes, and exit codes matched for **28/28** fixtures. Thus the existing checker and fixture set at this baseline are mutually byte-stable on replay. This does not assess prose-to-claim truth.
- Current checker SHA-256 and extracted baseline checker SHA-256 were both `eaa2f1178c4571d8a911cb3d880068216614766d8f35922cb78d6584179dad80`.
- Hashed all **139** fixture JSON files before and after replay. Per-path SHA-256 maps were equal; sorted path/hash manifest SHA-256 was `87ee35628b6d81c4a2291abfe21412b18e01ab3eabf529ba28562e55567ec8da` on both passes. Replay made no JSON changes.
- Exit status is fixture-specific, not an aggregate success claim: 7 fixtures exited 0, and 21 exited 1; no run produced stderr. This is observed checker output, not a judgment that every flagged fixture is defective lore.
- `r10-registry-witness` exited 0. Its `sources.json` has metadata records for `courier-log`, `archive-ledger`, and `registrar-copy`; the latter has a separate `registrar-copy-excerpt.md`. The courier-log and archive-ledger have no excerpt file in that fixture as observed. Checker success therefore does not itself show that cited prose supports any claim.

## Manual hash/correspondence verification design (recommendation, not performed)

Recommend a reproducible two-part review for any later authored excerpt/map change:

1. Hash-preservation review: record exact fixture-relative paths and SHA-256 for the five JSON inputs (`sources.json`, `entities.json`, `relations.json`, `timeline.json`, `contradictions.json`) before and after. Require identical path/hash maps, and separately hash the checker to show it was not changed. A hash proves byte identity only; it does not validate meaning or prose.
2. Human correspondence review: reviewers read each excerpt as raw text, then compare every pre-existing JSON assertion in the touched fixture against its cited source and record a compact mapping of `(JSON file + row/index + field/assertion) -> source_id -> exact excerpt span/quoted words -> supported / unsupported / ambiguous`. Include `first_appearance` assertions, each entity claim, every relation, and every timeline event description/place/tick as applicable. Include negative/absence claims (e.g., destination left blank) only when the exact text warrants them. Mark unsupported or ambiguous rather than filling gaps through inference; revise or reject the proposed excerpt/map if it fails. Independently inspect source metadata and excerpt labels for fiction/invention and avoid describing invented prose as recovered evidence or independent corroboration.

The map is a human-auditable index, not machine-verified semantics. It should state reviewer identity/date and use verbatim spans sufficient to relocate wording. Hashes can bind the review to exact bytes if recorded, but neither hashes, checker exit 0, nor a correspondence table establish source reliability, canon truth, or independent corroboration. The checker validates structural/identifier consistency and declared rules; it does **not** check that prose entails JSON claims. This recommendation is prospective; I did not author or verify excerpts or a correspondence map in this scout task.

## Raw observed paths

- Checker: `.shokunin/lore/corpus/fixtures/check_bible.py`
- Fixture corpus: `.shokunin/lore/corpus/fixtures/` (28 directories)
- Baseline fixture outputs: `.shokunin/lore/corpus/live/runs/20261012T180109Z/` (28 `.txt` files; prior-run evidence)
- Prior non-author replay report: `.shokunin/lore/reports/r13-independent-verifier.md`
- Registry witness JSON: `.shokunin/lore/corpus/fixtures/r10-registry-witness/{sources,entities,relations,timeline,contradictions}.json`
- Existing fictional excerpt observed: `.shokunin/lore/corpus/fixtures/r10-registry-witness/registrar-copy-excerpt.md`
- Current and extracted-baseline replay captures from this task: `/tmp/r14-replay/`

No excerpts, fixture JSON, checker, shared docs, or commits were changed by this scout. Recommendation only; no checker prose-validation claim.
