# Round 26 scribe: admitted vs malformed duplicate target

**Decision scope:** relation endpoint diagnostics under the entity required-field screen. This is a one-axis calibration probe, not an entity-resolution or canon rule.

| Target-ID rows in input | Screening result | Expected relation endpoint decision | Evidence limit |
|---|---|---|---|
| No admitted row with ID | No entity row resolves through the admitted index | Existing dangling endpoint diagnostic; no ambiguity | Says only that the fixture index has no admitted match. |
| Exactly one admitted row with ID | Row is indexed | No ambiguity finding for that endpoint | Does not establish source-text support or canon. |
| More than one admitted row with ID | Each complete row is admitted; ID count exceeds one | Emit endpoint-local ambiguous entity finding; do not choose a row | Duplicate-ID diagnostic is separate; no identity/canon inference. |
| One admitted row plus a same-ID row missing a required field | Malformed row is diagnosed and excluded; count remains one | No endpoint ambiguity from that malformed row | Absence of ambiguity is not proof that omitted/malformed evidence is false, absent from canon, or semantically irrelevant. |

| Test | Bounded pass condition |
|---|---|
| Matched malformed-target case vs `r25-to-ambiguous` | Keep relation and valid target; make only duplicate target fail one required field. Malformed case reports schema error but no `relations[0].to: ambiguous entity`; admitted-duplicate control retains `.to` ambiguity. |
| Unique control | No ambiguity finding for unique admitted target. |
| Regression | Replay the 75 declared prior fixture stdout/stderr/exit triples and confirm 374 existing JSON paths remain byte-identical, per `.shokunin/lore/LOG.md:385`. |

**Evidence.** Required-field screening appends a row only when every required field passes (`.shokunin/lore/corpus/fixtures/check_bible.py:32-43`). The entity index is built from screened rows and separately emits duplicate-ID diagnostics (`check_bible.py:45-51`); endpoint ID multiplicity is counted over `data['entities']` (`:119-121`). Relation checks report dangling or ambiguous endpoints from that index/count (`:123-130`). The round declaration states the admitted-duplicate baseline and absence of a paired malformed control (`.shokunin/lore/LOG.md:383-385`). The existing r25 paired target case is documented in `.shokunin/lore/reports/r25-scribe.md`; its fixture paths and exact rows should be cited by the eventual executor/verifier, not assumed here.

**Risk and bounds.** Do not describe the malformed row as a second resolvable target: required-field failure excludes it from the screened index. Conversely, no ambiguity finding does not prove canon uniqueness, truth, falsity, or absence of a real-world/in-world target. The checker does not inspect cited source text. Keep the paired mutation limited to one required field; if other fixture differences exist, calibration attribution weakens. This scribe report changes no fixture, checker, LOG, or knowledge document. Test success remains unverified until the paired fixture and regression replay are observed.
