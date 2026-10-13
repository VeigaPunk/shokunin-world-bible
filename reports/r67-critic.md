# Round 67 critic — falsification and layer review

## Scope and verdict

Read-only critic review of `.shokunin/lore/LOG.md` Round 67, `/tmp/mission-lore-standing.md`, the active checker, current probes, and available scout reports. I wrote only this report. **NO-GO on demonstrated material calibration gain; the narrow implementation is technically coherent, but materiality is not established.** The defect is reproducible, so this is not a falsification of the reported baseline behavior. It is a falsification challenge to the leap from “no claim-local message” to an operator-relevant improvement: every unavailable-index case already fails with an explicit source-table load error, never CLEAN. No observed workflow or decision is shown to change.

## Commands and observed results

From `/home/vgpnk/Projects/prymeagnt/lore`:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/live/r67-probe/empty-unavailable
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/live/r67-probe/empty-loaded
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/consistent
```

Observed (captured with `printf` exit markers):

- `empty-unavailable`: exit 1; one `sources.json: cannot load JSON: ... No such file or directory ...` finding; `1 violation(s); no canon changed`; stderr empty.
- `empty-loaded`: exit 1; `entities[0].claims[0].source_id: unknown in-world source ''`; one violation; stderr empty.
- `consistent`: exit 0; `CLEAN: schema, citations, relations, timeline; 0 violations`.

The pre-existing `reports/r67-fixture-scout.md` records that `empty-unavailable` and `control-unavailable` differ only in the claim source ID (`''` vs `courier-log`) and currently both yield just the source-table load error. I read that report and did not create or alter its probes. `git status --short` showed the Round 67 LOG/probe/scout work already present; `git diff -- .shok…` showed no checker diff. HEAD was `262486d`.

## What can and cannot be falsified

At `.shokunin/lore/corpus/fixtures/check_bible.py:149-154`, current validation rejects non-string claim source IDs but accepts blank strings into `source()`. At lines 97-108, `source_status()` returns `unavailable` without an unknown/ambiguous finding when the sources table cannot load. Thus the narrow technical premise is true. With an available index, the same blank string already gets an `unknown in-world source ''` finding. The proposed nonempty check therefore adds a *shape/required-value* diagnostic only where index status currently suppresses membership conclusions.

That new finding would be valid and claim-local, not a source-text, fictional-world, or canon inference. Reusing the existing message `expected nonempty statement and source_id` is in the correct layer: claim structural validation. It should not be implemented by changing `source_status()` or treating unavailable as empty/unknown, which would affect unrelated citation sites. However, source-table unavailability is already an explicit global hard error and the checker refuses CLEAN, including for the control input with a nonempty ID. The proposed pair proves a changed diagnostic count/message, not that an operator would make a different repair, avoid a false pass, or gain a distinct resolution path. I found no such material consequence in the declaration or inspected reports. Hence the move may improve local specificity, but that alone does not establish the declared material calibration axis.

## Bounded recommendation

Reject this round absent evidence that claim-local diagnosis during a source-index failure changes a real validation/repair decision. If the move is nevertheless admitted by later adjudication, keep it to the claim guard (`not claim['source_id'].strip()`), and test both `''` and whitespace with missing and malformed source tables plus a nonempty control. Preserve the independent load error, do not add an unknown-source conclusion for blank IDs when the index is unavailable, and retain existing resolution behavior for nonblank IDs. Candidate replay and full regression evidence are not available to me. Nothing here establishes source support/authenticity, rights, fictional canon, chronology, or game mechanics.
