# Round 63 — LEAF simplifier assessment

**NO-GO: no implementation or fixture change is justified on the present record.** The decoder concern is real and reproducible, but the materiality/compatibility case required by the declaration has not been established here. This is not a claim that non-finite tokens are valid JSON.

## Path/line evidence and observed probe

At `.shokunin/lore/corpus/fixtures/check_bible.py:45`, all five tables are decoded by `json.loads(..., object_pairs_hook=unique_object)`. The hook at lines 16–22 rejects duplicate member names, but there is no `parse_constant` handler. Python's standard decoder therefore accepts `NaN`, `Infinity`, and `-Infinity` as non-standard constants. Downstream schema validation at lines 70–76 validates only required fields and ignores unknown fields; typed `tick` checks occur at lines 279–281. The README's parser/schema discussion describes required shapes but does not state a strict RFC JSON-number policy.

Observed, not hypothetical: I copied `consistent/` to `/tmp/lore-r63-nan` (outside the repository), added `"extra": NaN` to a source row, and ran the checker. It exited 0 with `CLEAN: schema, citations, relations, timeline; 0 violations`. This demonstrates that a non-JSON token in an ignored field can evade validation. It does not establish a fictional source claim or a checker conclusion about lore.

The proposed narrow fix—a `parse_constant` callback raising a parse-level error—would reject constants at any nesting depth and cause the affected table to unload under the existing whole-file error policy. That is small in code but not necessarily small in behavior: for `entities.json`, `sources.json`, or `timeline.json`, it could trigger cascades of dangling-reference or index findings. A diagnostic should identify the table and token only; no row path can be responsibly named by the decoder hook. Do not broaden this into a loader refactor or claim that a token's location implies an authored row.

## Prior art, novelty, and compatibility boundary

R5's invalid-JSON cases establish existing parse-error handling and document malformed-input diagnostics, so this proposal is not wholly novel. R59 establishes duplicate-member rejection as a deliberate parser policy and explicitly notes it is newly chosen, not a proved upstream contract. Neither establishes that Python's accepted non-finite extensions are a material false validation signal, nor that supported producers emit strict JSON only. The available README does not resolve producer compatibility. The single observed `sources.json` extra-field case proves the hypothesized CLEAN path, but does not establish downstream behavior, whether these inputs occur in the supported workflow, or net calibration improvement over the cost of whole-file unloading.

A meaningful falsifier/control set would hold all other table bytes fixed and compare: each non-finite spelling in ignored metadata; a nested object and a typed numeric field; ordinary finite numeric input; and loaded controls. It must record the complete diagnostics/cascade for each affected table and test documented supported producers or establish an explicit format contract. Without that evidence, admission would convert a plausible standards-based preference into an unverified compatibility rule. A parser-level rejection may improve strictness while materially worsening diagnostic usefulness if it drops otherwise usable rows; neither direction is measured here.

## Independent-axis recommendation and boundary

**Calibration: NO-GO / not demonstrated. Depth: unchanged. Coverage: unchanged.** The observed accepted token is a concrete gap, but this leaf has no matched old/current candidate suite, no supported-producer compatibility evidence, and no independent replay of the pinned 125 fixture tuples / 623 prior JSON paths. I therefore recommend no checker, fixture, README, or LOG change on this evidence. This is a no-go for material admission, not proof the candidate can never be justified.

Rejecting a non-finite JSON token would concern input syntax/validation only. Neither acceptance nor rejection establishes source-text support, truth, actual chronology, canon, rights, license, or permission. A falsifier for this no-go would be an explicit strict-JSON supported-input contract plus matched evidence that rejection prevents a misleading validation pass without material cascade harm, and independent preservation replay.
