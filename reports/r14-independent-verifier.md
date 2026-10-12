# Round 14 independent verifier — non-author replay and excerpt review

## Scope and raw evidence

Non-author verification against baseline commit `319d3101a7d2396a2170da1fd677be6a00dba0ef`. I did not edit fixture JSON, excerpts, or checker. Current CLI was run for each of the 28 fixture directories using `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<directory>`. Baseline checker bytes were extracted with `git show 319d3101a7d2396a2170da1fd677be6a00dba0ef:.shokunin/lore/corpus/fixtures/check_bible.py > /tmp/r14-check-bible-baseline.py`, then each fixture was replayed using `python3 /tmp/r14-check-bible-baseline.py .shokunin/lore/corpus/fixtures/<directory>`.

For all **28/28**, current and baseline raw stdout bytes, stderr bytes, and exit codes match. The 28 saved round-13 outputs in `.shokunin/lore/corpus/live/runs/20261012T180109Z/<fixture>.txt` also correspond to current stdout and exit status. All stderr was empty. Exit status is fixture-specific (six zero, 22 one); this is not an aggregate pass claim. For a concrete raw example, the saved and replayed `r10-registry-witness` output is `exit_code=0` and `CLEAN: schema, citations, relations, timeline; 0 violations`.

I hashed every fixture JSON file, before and after replay, by relative path and SHA-256. All **139/139** match baseline commit bytes and remained unchanged after replay. Sorted path/hash manifest SHA-256: `cc3544069700ef8d2a2a1f3e27b16264282c331e7b069d0e3aebd517f4d2931f`. The checker is also baseline-identical; SHA-256 `eaa2f1178c4571d8a911cb3d880068216614766d8f35922cb78d6584179dad80`.

## Manual excerpt correspondence

Read the three raw fixture excerpt files:

- `r10-registry-witness/courier-log-excerpt.md` says “I am Mira. At local tick 1, I leave Lantern Harbor carrying the blue seal. At local tick 2, I reach North Tower.”
- `r10-registry-witness/archive-ledger-excerpt.md` says “Lantern Harbor has a registry. North Tower has a watch bell.”
- `r10-registry-witness/registrar-copy-excerpt.md` says “At first bell at Lantern Harbor, I, Sella, registrar there, recorded seeing Mira leave. At Mira’s request, I left the registry destination blank and kept the carbon.”

The new courier wording corresponds to existing `entities.json` Mira/seal claims and `first_appearance` source assignments, `relations.json` carries edge, and `timeline.json` tick-1 departure at harbor and tick-2 arrival at tower. The archive wording corresponds to the existing harbor registry and tower bell entity claims/assignments. The existing registrar passage corresponds to Sella’s entity/registrar assertion, recording relation, and registry-entry event, but says “first bell,” not fixture tick 1, and expressly leaves destination blank. No JSON row cites archive-ledger for a relation or timeline event. The phrase-to-row mapping in `reports/r14-executor.md` is accurate as a correspondence index, subject to its stated limits; correspondence is not semantic entailment proof.

## Circularity and depth judgment

Both added excerpts are explicitly labeled newly authored fictional fixture text, not recovered evidence. Their wording was composed to restate rows already present under the same source IDs. Therefore the source-to-row “support” is **authored circularity**: it improves inspectability/traceability of the designed fixture, but is not independent corroboration, discovery, or validation of the JSON claims. The archive statements and courier route merely restate existing assertions. I find **no new story fact** in either excerpt; there is no additional event, relationship, route segment, duration, or qualification that deepens the account. Preserve the blank destination and do not infer a tick mapping from “first bell.”

Accordingly, this verification does not support a substantive depth improvement; it supports documentation/legibility only. Treat depth as unchanged (or unproven) rather than improved. No checker prose validation, canon truth, or independent evidence is established. This is a verification finding, not an axis-adjudicator verdict.
