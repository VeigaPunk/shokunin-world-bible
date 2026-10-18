# V59 source inventory (SCORECARD planned/retired + LOG corrections)

Method constraint: do not expand IDs by opening debt ledgers. Status notes below come from later SCORECARD planned lines and LOG closure/errata text, not from `.ufo/**/debt.*`.

## Detection-gap items (a gate does not catch a class, or a receipt stays silent)

| ID | Source | Named fact | Later record in the same sources |
|---|---|---|---|
| DG-01 | SCORECARD:426 planned r95; :461 planned r96 | BR-01 dependency-reduction detection | LOG r96 closure: JSON-edge half closed. Prose half remains (see DG-02). |
| DG-02 | SCORECARD:492 planned r97; :524 planned r98; :558 planned r99. LOG r97 errata: pin payload is the five JSON tables only; map digest cannot be pinned. LOG r97 C-5: BR-01 prose half carried. | Markdown / dependency-wording edits invisible to the freeze pin | Still the r99 planned candidate. Not closed by any later correction in LOG. |
| DG-03 | SCORECARD:426 planned r95 | BR-02 schema-drift class | LOG r95 closure: class closed with a stable FINDING. Residual scope is DG-04. |
| DG-04 | LOG r95 carried (conditions 4): drift scope limited to claim-shaped records under unexpected entity keys. SCORECARD:461 planned r96: "drift scope widening decision" | Relations/timeline/nested drift not in the closed class | No later planned line or LOG correction says the widening landed. |
| DG-05 | LOG r95 carried: deleting `claims` + row exits 0, only non-gating INVENTORY MISMATCH. SCORECARD:461 planned r96: deletion class silent PASS | map_obligations deletion class | LOG r96 closure: now exits 1 `inventory_mismatch`. Historical, closed. |
| DG-06 | LOG r95 correction (7): INVENTORY receipt is non-gating | Same mechanism as DG-05 | Superseded as a silent path when DG-05 closed. |
| DG-07 | LOG r95 carried: V37-D1 legacy-dialect hidden-second-pointer. SCORECARD:461 | hidden second pointer | LOG r96 closure: `dual_pointer` closes it. Residual: LOG r97 C-5 canonical-dialect `dual_pointer` bound. |
| DG-08 | LOG r96 closure conditions: consistent regeneration exits 0 | regenerated declaration still passes | Not named as closed in later planned lines or errata. |
| DG-09 | LOG r96 closure conditions: droppable added pins (subset-tolerant loader). SCORECARD:492 planned r97 | self-test can pass with a pinned case removed | LOG r97 closure: loader fails closed on any dropped pinned case. Historical, closed. |
| DG-10 | LOG r95 carried: `schema_drift` not pinned by a persisted self-test case. SCORECARD:461 planned r96 lists the pinning | silent revert of the closed class would not fail self-test | No later LOG correction says a persisted `schema_drift` case landed. |
| DG-11 | LOG r95 correction (2): `map_obligations` reads pointer and source-ID columns only; anchors/spans/modes are not its coverage | anchor/span/mode edits invisible to that gate | No later correction withdraws this. |
| DG-12 | LOG r93 receipt-terminology correction: lexical support tool does not read raw JSON and does not prove entailment | raw-JSON fact with no map change can still be lexically fine | Pre-r94 correction; standing bound. Not an r94–r98 accumulation item unless the table claims an unbounded consolidation. |
| DG-13 | LOG r97 C-5: "checker/support blind spots" (class name only; mutations not listed) | unnamed checker/support misses | Expanding the phrase would require a debt ledger. Left unexpanded on purpose. |
| DG-14 | LOG r96 errata (2): cosmetic map delimiter cell and "new relation" sentence; no gate reads them | prose cells invisible to every gate | Narrower than DG-02. r97 repaired the two cells; the "no gate reads them" fact is the blind spot, not the cosmetic text. |
| DG-15 | LOG r97 errata (2): r97 tick-13 edge outside the pin set, so freeze does not see it | unpinned fixture | LOG r98 closure: V46 discharged by a reproduced REDUCTION-DETECTED. Closed. |
| DG-16 | SCORECARD:492 planned r97: path binding (before the fix, a foreign path verified). LOG r96 closure: no path binding | foreign-path byte copy verifies | LOG r97 closure: PATH-MISMATCH landed. Historical, closed. |
| DG-17 | SCORECARD:12 planned (header, still present): holder-dup silently latches `can_check_chain=False`, hiding a real break | pre-fleet masked break | Later SCORECARD r87 row records the repair. Pre-r94. Not retired. |
| DG-18 | LOG r93 r89-admission correction: null `from_holder` and tick findings were wrongly qualified at `e97613c` | checker wording blind/mis-fire | Same correction: repaired forward at r90 `ca7f9ef`; r89 not admitted. Pre-r94. |

## LOG corrections that are not detection gaps

- r93: missing `## Round 89` heading; r91 report missing `## SHONEN`; SHONEN file stayed `[ ]` while SCORECARD prose said `[~]`; shared-ledger attribution commits; two legacy tools lack self-test modes.
- r94: denominator shorthand at LOG:2312-2314; W30 `node corpus-gate.mjs` exit 1 disclosed; F40 bookkeeping defective; watchdog existence-only and lore omitted from LANES.
- r95 corrections (1)(3)(4)(5)(6): denominator wording, parsed-value vs byte identity, ratio denominators, r87 detail-string change, `schema_drift` detail embeds the renamed key. Carried non-gaps: BR-05 scratch location; P4 empty addendum; P5 stale pin.
- r96 errata (1): r95 source count is 4, not 5.
- r97 C-5 non-gaps: stale r95/r96 knowledge-note pins; path-less legacy pin migration.
- r98 errata: "not gitignored" superseded; "lists only two files" corrected; in-flight contract pin `c435239d…` corrected to `153ebc5b…`.

## Retired sections (must not be reopened as open blind spots)

- SCORECARD:14 and :33 and :367: hard-failing exact duplicate names / duplicate-display-name detector remains rejected.
- SCORECARD:70, :93, and every round from r87 through r98: `retired: none` (no expertise axis retired).

## r99 planned line (the claim, not an extra source row)

SCORECARD:558 and LOG Round 99 declaration: the table is supposed to document checker blind spots. The declaration names seven classes (emptied `depends_on`, wrong-but-earlier edge, deleted terminal row, F15 support_check-silent mutants, dependency-wording removal, consistent-regeneration, checker frozen-pin status). Those seven names are the claim under test. They are not used here as the enumeration source. DG-13 is the only LOG-correction handle for the checker/support class, and it does not list those mutations.
