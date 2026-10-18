# Round 37 — final non-author axis adjudication

**Admit the bounded coverage move:** one axis improved; neither other axis harmed.

| Axis | Verdict | Basis |
| --- | --- | --- |
| Coverage | **Improved** | The r35-derived control and one-row variant exercise a previously unexercised **two-sided contradiction-ledger endpoint cardinality** case. `claim_a` names a timeline ID occurring twice, and the checker reports its endpoint-local exact-one error alongside the global duplicate-ID error; `claim_b` names an ID occurring once. Round 9 already covers duplicate IDs and ambiguous dependencies, so generic duplicate behavior is not the novelty. |
| Depth | **Unchanged** | No new account, source assertion, semantic conflict, or canon fact; the added row is byte-for-byte the existing Tarin event. The inherited ledger remains an editorial pointer pair rather than a proof of incompatible testimony. |
| Calibration | **Unchanged** | This probe preserves the structural/prose boundary and records all diagnostics; it does not establish new source support, testimony truth, contradiction semantics, or chronology. No evidence of harm on this axis. |

## Independent checks

I read the r37 declaration and wave receipts in `.shokunin/lore/LOG.md`, r35/r37 fixture JSON and cited excerpts/maps, fixture README, checker implementation, r9 duplicate controls and adjudication, and r37 critic/reviewer/independent-verifier reports. I independently extracted the fixture tree and checker from pinned report commit `4e5dacf413d727595aec80ffc1f2e0e2a17f4f84` to a temporary directory outside the repository. For every pinned fixture I ran identical **root-relative** argv from its respective root: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>`. Comparing raw stdout bytes, raw stderr bytes, and exit code separately gave **88/88 exact old CLI tuple matches**. Comparing the pinned JSON paths against current worktree bytes gave **439/439 exact matches**. The archived tree and worktree invocation each used their own root, avoiding path-echo mismatches. This protects prior observed behavior and inputs, not universal correctness.

Across nine inherited files, `r37-ledger-unique/` equals `r35-bell7-conflict/` byte-for-byte. `r37-ledger-ambiguous/` differs from r35 only in `timeline.json`: its original four rows are intact and in order, and `timeline[4]` is an exact object copy of existing `timeline[2]` (`tarin-envelope-observation`). Both excerpts, the cited source rows, manual maps and `contradictions.json` remain unchanged. The sole `bell7-location-reports` ledger pair names `claim_a.event_id=tarin-envelope-observation` twice in the ambiguous timeline and `claim_b.event_id=sella-bell7-presence` once; both point at `place_id`. The checker counts schema-admitted timeline IDs and checks `event_id_counts != 1` before dereferencing an endpoint (`check_bible.py:60–62, 76–105`). The ordinary duplicate-ID finding comes from the separate index pass (`:45–50`). R9's order-swapped duplicate controls produce duplicate-ID and ambiguous-**dependency** findings; they do not probe this contradiction endpoint.

From the current repository root, the exact control command `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r37-ledger-unique` exits **0**, raw stdout `CLEAN: schema, citations, relations, timeline; 0 violations\n`, raw stderr empty. The equivalent `r37-ledger-ambiguous` command exits **1**, raw stderr empty and complete stdout:

```text
VIOLATION: timeline[4].id: duplicate timeline id 'tarin-envelope-observation'
VIOLATION: contradictions[0].claim_a.event_id: expected exactly one timeline event 'tarin-envelope-observation'
2 violation(s); no canon changed
```

Thus there are **exactly two findings** here, not an unreported collateral double-booking; no `claim_b` diagnostic. The r37 critic's warning about possible collateral findings was appropriately tested rather than assumed away. The duplicate makes the structured A endpoint non-unique; it does not select a first/last row or add another independent witness. Tarin's `place_id=harbor` remains the reported sighting scene, not a Sella-actor occupancy row. Neither this error nor the clean control establishes that the excerpts are authentic, the accounts are true or false, the date and ringing are independently verified, or the source-conditional conflict is canon. No checker rule was changed. This verdict is not a SHONEN checkmark, promotion, push, or merge.
