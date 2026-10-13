# Round 60 independent reviewer — entity availability gate

## Verdict: PASS, material but narrowly scoped calibration improvement

The candidate correctly distinguishes “entity index unavailable” from a successfully loaded empty/partial index. This is material beyond the known r5 cascade: matched controls demonstrate that the six reference findings are conditional on the table being loadable, while retaining exactly those findings for loaded-empty and loaded-partial inputs. It does not establish absence/presence in the fictional world. Approval is for the entity-availability policy evidenced here, not generalized suppression for other tables.

## Evidence and replay

Reviewed the r60 prior, regression, loader, pair, citation, critic, simplifier, scribe and executor reports; the r59/r5 historical records; candidate checker and README diff; and all four current r60 fixture directories. Independently ran `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture>`:

| Fixture | Exit | Diagnostics |
|---|---:|---|
| `r60-unavailable` | 1 | malformed `entities.json` load diagnostic only; 1 violation |
| `r60-empty` | 1 | dangling relation endpoints `mira`,`seal`; timeline actor `mira` twice and places `harbor`,`tower`; 6 violations |
| `r60-partial` | 1 | dangling `seal`,`harbor`,`tower`; 3 violations |
| `r60-unavailable-independent` | 1 | entity parse error plus negative timeline tick, unknown source `absent`, unknown dependency `missing`; 4 violations |

The matched three fixtures have identical raw bytes (verified SHA-256) for `sources.json`, `relations.json`, `timeline.json`, and `contradictions.json`. Only entity-table state varies. Thus the missing six diagnostics in the unavailable case cannot be attributed to different references or other input mutations. Empty and partial retain expected lookups rather than being globally treated as unavailable.

The unavailable-independent fixture independently confirms that source, tick, and dependency findings are not suppressed by the failed entity load. This is consistent with the code: relation source checks and timeline source/tick/dependency checks remain outside the availability gate.

Historical context: r5’s loader scout observed missing, invalid, and non-array entities yielding six dangling findings plus a load/shape error; its critic cautioned that “one mutation” did not mean one diagnostic. r59’s nested duplicate-member fixture is a concrete unload case: current checker now emits the duplicate-member diagnostic alone, whereas r59 records six downstream dangling findings before this change. I replayed the current nested fixture and got exactly that one diagnostic. These prior examples support relevance but do not substitute for the matched r60 controls. R5’s unrelated missing-contradictions example is not a high-fanout entity control.

## Code-path audit and limits

The candidate tracks `entities_available` only for a decoded top-level list, independently of `data['entities']`; invalid JSON and duplicate-member failures do not masquerade as loaded empty. Empty and valid partial arrays are available. The gate covers relation endpoint membership/duplicate ambiguity; alliance reciprocity/kind inference; timeline actor/place membership, ambiguity, place-kind and derived occupancy; and provenance holder membership/chain processing over valid entity rows. Existing valid entity-row source/claim checks remain; relation/timeline source checks and timeline-local tick/dependency validation remain independent.

Important coverage limitation: malformed rows in a successfully loaded array are omitted from `data['entities']` and therefore from entity indexes, while `entities_available` remains true. A reference to an ID appearing only in an invalid row can still be labeled dangling. That is distinct from whole-table unavailability, but the README’s phrase “successfully parsed top-level array” could be read as implying a complete/usable index. Policy should remain precisely “table loaded as array”; do not imply the index is complete when row validation rejected rows. Duplicate valid IDs remain counted and ambiguity checks are preserved on loaded input. No additional malformed-row or duplicate-ID fixture was included in this round, so behavior is code-audited rather than independently exercised here.

The distinction is input-table membership only. A missing ID in a loaded input is not evidence of fictional-world absence; an unavailable table supports no such conclusion. Nor does resolvable citation membership establish source-text support, truth, canon, rights, or permissions.

## Harm / calibration assessment

No material harm observed in the requested negative controls: entity unavailability no longer emits false-certainty dangling/kind/occupancy conclusions; loaded-empty/partial still expose genuinely absent-from-input IDs; and independent tick/source/dependency findings survive. The load diagnostic itself explains why entity references were not assessed, though output does not individually label each skipped reference as “unassessable.” Given the narrow entity-only gate and visible loader error, this is acceptable calibration rather than masking independent findings. No evidence supports suppressing checks against unavailable source or timeline tables.

**Decision: PASS, material calibration improvement; scope limited to entity-index availability and input referential conclusions.**
