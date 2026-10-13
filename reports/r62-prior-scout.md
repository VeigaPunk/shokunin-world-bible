# Round 62 prior-scout — ledger event IDs and unavailable timeline

## Independent disposition

**Conditional GO for a narrow, material calibration probe; not GO for implementation from prior art alone.** The candidate is specifically whether a contradiction-ledger side pointing to an event in a wholly unavailable `timeline.json` is currently mislabeled as an absent/non-unique event. The uncertainty-vs-empty rationale is not novel: r60/r61 explicitly distinguish unavailable whole tables from loaded empty tables, and r61 applies it to sources. But timeline availability and this ledger event-ID consumer were expressly left outside those rounds. This is a distinct table/consumer and potentially material certainty correction, subject to the matched test below. If it only removes redundant lines without a meaningful calibration gain, reject.

## Prior-art audit

- **r7:** `reports/r7-reviewer.md` inspected ledger code and actually probed an ambiguous *source* citation (`archive-ledger` duplicated) for a uniquely identified event. Its observed ledger-side result is `contradictions[0].claim_a.source_id: ambiguous in-world source`; it did not make the timeline unavailable and does not test event-ID cardinality under an unavailable event index. The same report's `contradictions-ledger-malformed` replay is a dangling/missing event pointer with a successfully loaded timeline, not an unavailable timeline. `reports/r7-independent-verifier.md` confirms that malformed ledger fixture's outcome and baseline preservation. Thus r7 tests source ambiguity and loaded-timeline event resolution, not the proposed case.
- **r39:** `reports/r39-prior-scout.md` distinguishes unknown vs ambiguous **source status** after exactly one event resolves; `reports/r39-axis-adjudicator.md` confirms the durable probe changes the event's source ID to zero matching source rows and observes both `claim_b` “no resolvable source_id” and timeline unknown-source diagnostics. This is not event-ID zero/multiple cardinality. The r39 prior scout specifically notes malformed-ledger fixture tests missing event ID, but not a present ledger pointer against an unavailable timeline. Therefore r39 is adjacent, not a match.
- **r60/r61:** their LOG declarations and closures expressly scope entity-only then source-only whole-file availability gates; timeline was excluded. Their general status principle and method are strong analogs, not novelty in principle. They do not establish the materiality or safe suppression of `timeline.json` ledger event-cardinality output.

## Observed code vs proposed probe

**Observed current code:** `.shokunin/lore/corpus/fixtures/check_bible.py:40-56` maps timeline load/parse/top-level-shape failure to `rows=[]` (there is no `timeline_available` flag). At `:87-92`, an event index/count map is built from admitted rows. Ledger handling at `:109-137`, especially `:124-126`, emits `expected exactly one timeline event <id>` whenever count is not one. Accordingly an unavailable timeline currently takes the same zero-count branch as a successfully loaded empty timeline. This is code-path observation; the unavailable-case output is a **proposed/temporary probe**, not an observed durable fixture result in this scout.

**Proposed external temporary probe (outside repo):** clone a clean fixture to `/tmp`, keep `sources.json`, `entities.json`, `relations.json`, and `contradictions.json` byte-identical, and vary only timeline state:

1. malformed or missing timeline control: use the same ledger side naming an otherwise known event ID; expect a file-level load error plus the current ledger `expected exactly one timeline event` finding;
2. loaded `[]`: same four tables, valid empty timeline; expect the ledger cardinality finding, without a load error;
3. loaded partial array with the referenced event absent: expect the cardinality finding;
4. valid timeline with one event: expect no cardinality finding;
5. valid timeline with duplicate event IDs: expect existing duplicate-ID and ledger exact-one findings.

Capture complete stdout/stderr/exit. Preserve ledger shape, allowed field, side-difference, and unrelated source/entity/relation checks. The candidate rule to test—not presume—is: only when the *whole timeline file* is unavailable, retain load/shape error and ledger structural checks but withhold the event-ID exact-cardinality conclusion; loaded empty/partial still means zero match in supplied input and retains that finding. Do not skip the ledger loop wholesale. Verify all five mutation/control distinctions and independent checks before claiming gain.

## Falsifier, costs, and limits

Falsify conditional GO if a retained prior probe already exercises this exact unavailable-timeline ledger path; if matched output has no unsupported or materially misleading certainty beyond the direct loader error; if loaded-empty/partial or duplicate-ID behavior changes; or if suppression drops ledger shape/distinctness checks or independent source/entity/relation findings. A possible cost is loss of a useful pointer to affected ledger sides and repair triage; compare complete outputs, not only violation counts. Do not treat unavailable as CLEAN, empty, or event absence. A malformed/filtered row array that parses as a list remains an available index unless an independently justified policy says otherwise. This check concerns input-table ID resolvability only: no assertion about event occurrence, chronology, source prose, world truth, canon, ownership, rights, or permission.
