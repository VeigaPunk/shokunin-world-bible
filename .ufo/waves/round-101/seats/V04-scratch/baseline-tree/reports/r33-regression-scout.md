# Round 33 regression scout — replay plan

## Scope and precedents

Round 33 requires exact replay of the 84 prior fixture outcomes (stdout, stderr, exit status) and byte identity for 419 existing fixture JSON paths. This is a regression plan only; I did not run or modify the checker, fixtures, or log. The baseline claim and counts are in `.shokunin/lore/LOG.md` (Round 33 declaration; round-23 closure corrects an earlier inventory count from 319 to 359, illustrating why the current declared 419 must be measured at the pinned baseline rather than inferred from a prior round).

Round 10's strongest precedent is the explicit comparison of every old CLI output plus fixture JSON hashes against a pinned baseline, with a separate new fixture. Its caveat matters: equal local ticks do not establish exact simultaneity or clock conversion (`.shokunin/lore/LOG.md`, Round 10 reviewer caveat and closure). Round 23 similarly compared all saved outputs and baseline JSON paths, and kept the clause map manual rather than implying checker entailment validation (`.shokunin/lore/LOG.md`, Round 23 closure). Apply both: compare exact streams and status; hash old JSON paths; keep any new clause-to-text review distinct from checker guarantees.

## Replay procedure

1. Pin the baseline commit named in the Round 33 declaration (`6e0151a1601663755e29b4ce103d7f1d5ed1175a` for work; report commit `56f924458673e86cd82588ceb7818c1cdaad44a8`). Enumerate the 84 pre-existing fixture directories and 419 JSON paths from that baseline, recording sorted path manifests and SHA-256 hashes. Do not count only active-looking directories: include the same corpus scope used for the declaration.
2. At baseline and candidate revisions, run the same repo-root command for each fixture: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>`. Capture stdout bytes, stderr bytes, and process exit status separately, keyed by fixture path. Require exact equality for all 84 keys. Do not compare only pass/fail or violation totals.
3. Hash the 419 baseline JSON paths at both revisions and require unchanged bytes. Separately assert that the new `r33-*` fixture path was absent at baseline and exists at candidate; exclude its new files from the 419-path equality comparison.
4. Run the new fixture once with the same command. Require exit 0, empty stderr, and the expected clean result. Inspect its clause map manually against the invented first-person excerpt and each newly added assertion. This manual review is not checker verification.
5. Save the command, baseline/candidate identifiers, manifests, per-case stream/status comparison, JSON hash comparison, and new-fixture outcome in the verifier record. A missing path, changed stream byte, status difference, or hash difference falsifies the regression claim; report discrepancies instead of normalizing them away.

## Risks / boundaries

- Counts may drift if inventory scope or fixture path inclusion differs; make the baseline manifest authoritative and explain any discrepancy from 84/419 before claiming success.
- Golden output files can be stale or omit stderr. Replay commands at both revisions; do not treat a saved run alone as execution evidence.
- A fixture that is copied from `consistent/` could accidentally alter inherited JSON; compare its inherited records against the baseline and keep the original 419 files byte-identical.
- A superficially matching event may overstate the excerpt. Review only the requested observation: Tarin sees Sella place an unlabeled paper envelope on the Lantern Harbor registry desk. Do not infer paper contents, owner, recipient, destination, or relation to the Blue Seal; do not inspect or disclose envelope contents. Citation identity and a manual clause map do not establish source truth or canon.
- Existing checker behavior includes strict timeline ordering and same-tick occupancy constraints (README lines 29–34). Choose a non-inverting tick/event arrangement that does not accidentally imply ordering beyond the source. Round 10's tick/“first bell” caveat warns against treating local labels as synchronized time.

## Falsifiable check

The regression claim passes only if a non-author replay from the pinned baseline and candidate yields identical stdout bytes, stderr bytes, and exit status for each of the 84 baseline fixture paths, with all 419 baseline JSON path bytes unchanged; the new fixture is absent at baseline, present at candidate, and exits 0. Any one mismatch falsifies it. The depth claim additionally requires a non-author clause-by-clause trace from the invented excerpt to the single observation assertion, with no unsupported envelope detail or Blue Seal/canon linkage. The checker itself validates structure and references, not prose entailment.
