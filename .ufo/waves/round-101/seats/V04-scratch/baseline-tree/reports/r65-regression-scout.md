# Round 65 regression scout — forward citation eligibility

## Scope and baseline

Independent scout only. I made no checker, fixture, README, or LOG changes and did not commit. Current inventory is **125 fixture directories / 623 JSON paths** (`.shokunin/lore/corpus/fixtures`). The requested old-case replay against the pinned baseline was not run here; these are code/fixture observations and a replay plan, not a claim of byte-identical regression outputs.

## Observed behavior and relevant prior reports

The current checker (`corpus/fixtures/check_bible.py`, alliance pass around lines 235–255) iterates every admitted `allied_with` forward row whose faction endpoints are unique. It searches for a reverse row with `source_status(candidate['source_id']) == 'unique'`. It does **not** test the forward row’s source status before requiring that reverse witness. The ordinary relation pass separately calls `source(row['source_id'], location + '.source_id')`, so an unknown/ambiguous forward citation gets its own direct finding.

Raw current fixture probes:

- `ally-one-way`: exit 1, with `relations[0]: allied_with faction relation 'quay-guild' -> 'bell-wardens' lacks a sourced reciprocal relation`.
- `r7-ally-reverse-ambiguous`: exit 1, with duplicate `harbor-compact`, `relations[1].source_id: ambiguous in-world source 'harbor-compact'`, and the forward `relations[0]` missing-reciprocal finding. In this fixture the forward citation is `separate-compact` (unique), while only the reverse citation is ambiguous. This is the explicit r7 qualified-forward/unqualified-reverse case; it does not test an ineligible forward.

The r2 executor report records a temporary unknown-source **reverse** probe that retained both reverse citation error and the forward missing-witness finding; consistent with r2’s structural reciprocity convention. R7 reports the ambiguous reverse must not qualify and a qualified-forward missing-reciprocal finding remains. R31 concerns generic relation citation ambiguity, not reciprocity eligibility. R61’s source-table availability work gates alliance checks only when the source index itself is unavailable; it does not decide whether a loaded unknown/ambiguous forward row is eligible. None of these is direct evidence for the proposed forward-status distinction.

## Calibration assessment

**NO-GO for material calibration on present evidence.** The proposed policy—skip only the derived missing-reciprocal finding when the forward source is unknown/ambiguous—has a coherent interpretation (“do not demand a matching assertion from a row whose citation is not uniquely resolved”). But current output already gives a repair location for the forward citation and the relation location for the missing reverse. The latter may still be useful structural guidance independent of whether the asserted forward row is well cited. Suppressing it risks losing an actionable second repair pointer; no current operator evidence demonstrates that withholding this finding improves repair decisions or avoids false confidence. The existing checker expressly demands reciprocal evidence for every otherwise eligible directed row and treats reverse witness qualification separately. A new untested eligibility convention is not enough to establish a material calibration gain.

Probe outputs above are observed checker behavior. The proposed status-gated output is hypothetical, not executed. If reconsidered, matched temporary inputs should vary only forward citation status (unique/unknown/ambiguous) and reverse state (absent/unique/ambiguous), preserve independent relation endpoint and source diagnostics, and compare full output. Unique-forward/reverse-absent must retain the finding; ambiguous reverse with unique forward must preserve the r7 result. Crucially, compare the usefulness of the currently separate forward-citation and missing-reciprocal repair pointers, not just count lines.

## Falsifier and replay plan

A demonstrated repair workflow in which the forward citation finding alone directs correction and the missing-reciprocal finding routinely misleads operators would falsify this NO-GO and justify a narrowly scoped reconsideration. Conversely, if operators need both citation and structural pointers—or cannot tell which relation is intended until both are repaired—the proposed suppression would harm calibration. Before any candidate admission, replay all 125 baseline fixture invocations comparing exact stdout, stderr, and exit status, plus all 623 JSON paths/bytes; enumerate every delta. Current evidence is insufficient to claim this replay was performed or to claim candidate invariance.

This concerns only membership/uniqueness of source IDs in supplied fixture input. It makes no claim about source prose, whether an alliance exists in story canon, the truth of any claim, or rights/permission.
