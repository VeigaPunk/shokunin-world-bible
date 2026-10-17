# E1 — Round-89 wording proposals

Status: wording proposals; no checker or knowledge-table implementation changed.

Axes: calibration wording accuracy; depth-rule coverage; boundary between structural evidence and canon/legal claims.

## C1 — Valid-key combined cause summary

**Proposed emitted form** (retain the existing envelope and origin locator):

```text
{record_label}: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: {cause_1}; {cause_2}[; {cause_n}] at {origin_label}
```

Join the complete set of simultaneous causes that latch the stop on that valid-key record with `'; '.join(causes)`. Keep the existing single-cause form byte-for-byte when the set has one member. The list is the complete *latching-cause* set in validation order, not a list of every local diagnostic.

**Rationale:** preserves the current structural qualifier, tail-disclosure scope and first-stop locator while making valid-key multi-defect summaries complete. A semicolon is an unambiguous separator even when a cause itself contains commas; a stable validation order avoids claiming semantic priority.

**Over-claim risk:** “complete” is bounded to stop-latching causes actually evaluated on the record. It must not imply that every schema error was discovered on a branch that exits early (for example, an unexpected-key-set record), or that pre-loop stops have a record-level cause. Include only causes that independently latch comparison suppression.

## C1 — FN-2 unresolved-holder qualification

**Proposed clause for a would-be chain-break line when a referenced holder ID occurs more than once in raw entity rows but only one schema-valid row entered the resolved index:**

```text
input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
```

The example values are placeholders; render the actual field, ID, raw occurrence count, indexed count, expected value and observed value. Do not emit an unqualified definite chain-break finding for this unresolved-identity case.

**Rationale:** states why the comparison cannot establish identity continuity rather than silently treating the valid-row index as the whole raw entity table. It preserves the structural/non-canon boundary and reports both sides of the attempted comparison.

**Over-claim risk:** use this only when raw multiplicity and a non-unique/unresolved identity are demonstrated. Do not describe every chain break as uncertain, infer an entity's identity from the surviving valid row, or imply that the duplicate rows are otherwise equivalent.

## C1 — FN-1 absent-from-index wording

Use separate causes for raw absence and schema-invalid raw presence; do not use `dangling` or `unknown` as though an ID were absent from the input when it is present there.

```text
holder reference {field} {id!r} absent from raw entities and absent from the resolved index
holder reference {field} {id!r} present in raw entities but absent from the resolved index
source reference {id!r} absent from raw sources and absent from the resolved index
source reference {id!r} present in raw sources but absent from the resolved index
```

**Rationale:** the exact phrase “absent from the resolved index” describes the actual lookup result in both cases, while the raw-presence clause distinguishes genuinely missing IDs from IDs omitted during schema validation. Apply the same distinction to source lookups where the raw source row exists but no valid row is indexed.

**Over-claim risk:** only say “present in raw …” when the raw ID occurrence is measured, and only say “absent from raw …” when the whole raw table was successfully loaded and searched. A missing/unparseable table is unavailable, not evidence of raw absence; duplicate valid rows are ambiguous, not absent.

## C3 — Proposed R8–R10 decision-table rows

Use the existing six-column table shape: Decision / Rule-output / Attribution / Rights status / AI-training permission / Evidence and integration check.

| Decision | Rule / output | Attribution | Rights status | AI-training permission | Evidence and integration check |
|---|---|---|---|---|---|
| **R8 — A real-world source materially informs a fictional element, but its relevant text cannot be delivered (including because reproduction is blocked)** | Record the source/locator, affected element/aspect, and contemporaneous evidence that consulting the source changed the design; this establishes use, not the passage's contents. Screen materiality by asking whether the element depends on a source-specific claim, distinctive expression, sequence, or combination of details rather than only a broad idea/general motif, and state what remains if that dependency is removed. A named parallel still requires R1 citation; actual use or unresolved influence is not R2. If only a general motif remains, the element may remain as newly authored fiction only with `external-only / unverified inspiration` marked in the note/map, ledger `Use here` stating the text is not delivered, and independent in-world support for each canon claim; do not claim source-text support. A paraphrase, citation, or metadata entry is not a rights workaround. If distinctive expression/sequence informed it, or materiality is unresolved, withhold the dependent detail from supported canon pending independent re-derivation/redesign or a permitted text and review. Record the test and disposition in the note, element map, and ledger `Use here`. | Identify the supported work and consulted edition/version and locator; keep evidence of authorial influence distinct from a verified passage claim. Non-delivery does not mean no source was used. | Record the block/open question, scope, and evidence for the exact expression/edition; make no legal finding or rights grant. | Keep separate and open unless explicit, scoped terms establish permission; neither attribution nor a materiality screen answers it. | Record the blocked passage/element, dependency evidence, materiality result, disposition, and independent support. Recheck the affected element, note/map, and ledger at integration. |
| **R9 — An in-world claim is mapped to a delivered passage whose mode may be verbatim, translation, paraphrase, or summary** | Declare the mode in both excerpt and every claim-to-excerpt map entry. Only delivered source words, or an identified translation tied to a named source text/version, may support a source-attributed claim under R5; translated wording is the translator's rendering, not the source's exact wording. A paraphrase/summary is later-authored text, not the source's own text, and cannot satisfy source-text support or its exact-anchor check. It supports only the existence of the intermediary's retelling, attributed to that intermediary—not a claim about the underlying source; if the underlying text is not delivered, mark it `not delivered / unverified`. Identify the actual intermediary or deliver permitted underlying text for separate review; an anchor hit alone proves neither mode nor fidelity. | Attribute verbatim text or identified translations to the supported source; attribute editorial paraphrase/summary to its actual author/intermediary, not as a quotation. Identify translator/version where known. | Scope review to the exact delivered expression, edition, and translation; do not infer clearance from a mode label. | Assess separately; source ID, attribution, and delivery mode imply no training permission. | Record mode, source/edition, locator, map entry, and anchor where applicable. Replay exact-anchor checks for verbatim/translated text and inspect the underlying text; replay the durable paraphrase fixture without mistaking a paraphrase anchor for source-text support. |
| **R10 — An inspired claim conflicts with a claim in another landed cluster or fixture** | Before accepting a new cluster, compare source-attributed claims against relevant landed claims. When a shared referent/field is supported, record an unresolved corpus-level entry at `corpus/knowledge/cross-cluster-contradictions.md` with stable ID, both relative fixture paths, exact claim/event pointers and fields, each in-world `source_id`, competing statements, and why they cannot both be true as stated. Preserve both claims; do not silently select, reconcile, rewrite, or let a real-world parallel adjudicate canon. If identity/occasion remains uncertain, record a candidate discrepancy and missing evidence, not a confirmed contradiction. Keep `contradictions.json` for locally resolvable references; until a corpus-wide checker exists, manually verify both pointers and replay both fixture checks. Any resolution is a separate sourced decision that retains the original record. | Preserve each account's own in-world source and locator; an external parallel is not an in-world witness or tie-breaker. | A rights conclusion cannot decide fictional canon or authorize changing either account. | Training permission cannot decide fictional canon; assess independently. | Record both claim pointers, sources, anchors, and shared-referent evidence. Manually check the registered pair and keep unresolved status; a per-fixture `CLEAN` result is not cross-cluster evidence. |

### Rationale and over-claim risks for R8–R10

- **R8 rationale:** joins a provenance-based materiality screen to explicit outcomes: retain only a high-level motif with an unverified-inspiration marker and independent in-world support, or withhold expression-dependent details for re-derivation/review. This incorporates D1's and D2's complementary materiality/disposition criteria.
  **Risk:** the screen is editorial, not legal advice; source use or uncertainty cannot be relabeled as no influence. Do not imply that redesign preserves a claim or that independent in-world support clears rights in copied expression.
- **R9 rationale:** requires delivery mode in both excerpt and claim map and prevents a self-consistent paraphrase anchor from being treated as the source's words; translation is explicitly the translator's rendering.
  **Risk:** a paraphrase/summary may support only the existence of that intermediary's retelling—not the underlying source claim, wording, or source-text anchor. A translation does not prove unprovided original-language wording, and a lexical hit does not prove fidelity or whole-claim support.
- **R10 rationale:** turns cross-cluster comparison into a concrete unresolved register and manual integration gate while preserving the local scope of `contradictions.json` and the checker's one-directory limit.
  **Risk:** similar names do not establish a shared referent/occasion; until identity is supported, label only a candidate discrepancy. A local `CLEAN` result cannot establish global consistency, and recording a contradiction does not decide which claim is true.

