# Round 26 replacement final axis adjudication

**Verdict: admit the narrow fixture-only calibration move.** Calibration **improved**; depth **unchanged**; coverage **unchanged**. At least one axis improved and none harmed. The earlier adjudicator exit without a report is not evidence for this verdict.

## Evidence and decision

The declared claim in `LOG.md` was a paired malformed duplicate target: a second `seal` row fails exactly one required field, so it remains a raw input row but does not become an admitted entity or make `relations[0].to` structurally ambiguous. Direct comparison of the fixture JSON confirms that `r26-to-malformed/` and `r25-to-ambiguous/` have byte-identical sources, relations, timeline, and contradictions files; among parsed entity rows only `entities[4].name` changes from `"Seal in courier ledger"` to `""`. The unchanged raw row retains `id: "seal"` and `first_appearance: "courier-log"`; the cited `mira -> seal` relation is unchanged. This is a controlled one-field mutation, not a change to the checker.

I independently ran the current checker on the three target directories:

| Fixture | Exit | Exact stdout | stderr |
|---|---:|---|---|
| `r26-to-malformed` | 1 | `VIOLATION: entities[4].name: required nonempty str` then `1 violation(s); no canon changed` | empty |
| `r25-to-ambiguous` | 1 | `VIOLATION: entities[4].id: duplicate entities id 'seal'` then `VIOLATION: relations[0].to: ambiguous entity 'seal'` then `2 violation(s); no canon changed` | empty |
| `r25-to-unique` | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` | empty |

Each stdout line above is newline-terminated. The checker validates required nonempty fields before appending a row to `data[section]`; `index('entities')` and `entity_id_counts` operate on those admitted rows. The relation endpoint check emits ambiguity only if the admitted count exceeds one. Thus the malformed row is reported at its own location and cannot silently create the same admitted-target ambiguity as the valid duplicate. The unique control remains clean.

The non-author reviewer independently confirmed the one-field pair, admission path, and no-canon boundary in `r26-reviewer.md`. The non-author independent verifier in `r26-independent-verifier.md` replayed all **75** baseline fixture directories against the checker from baseline `f44e7281a5438dc86e4fd8a03b19476e4cce7371` and the current checker: exact stdout bytes, stderr bytes, and exit code matched in **75/75**, with zero mismatches. That verifier also compared all **374** baseline JSON paths byte-for-byte with the current files: **374/374 unchanged**; the new directory contains five JSON files. I checked the baseline lists have 75 directories and 374 JSON paths, and the checker itself has no tracked diff from that baseline. The exhaustive output and byte comparisons are attributed to the independent verifier rather than presented as my own replay.

**Calibration improves** because this paired case exposes the distinction between a raw malformed duplicate and a second admitted, structurally resolvable target: the checker reports the schema fault without incorrectly signaling a duplicate admitted entity or relation-target ambiguity. This calibrates interpretation of *this checker's findings*, not the underlying lore. Depth is unchanged: no deeper reasoning rule, contradiction resolution, or checker algorithm was added. Coverage is unchanged: this fixture probes the existing admission boundary and adds no new semantic category or checker behavior; the unchanged 75 prior outputs support no regression. No axis is harmed on the observed scope.

**Limits:** An absent ambiguity diagnostic does not prove that the malformed row is false, that source evidence is absent, that the target is uniquely real, or that any cited source text supports the relation. `courier-log` is an in-world source ID; neither fixture nor checker verifies source text, truth, rights, or canon. No canon is changed or established. This admission is limited to the one-field fixture and the stated regression set; it does not generalize to every malformed field or to source-text adjudication.
