# PROPOSAL ONLY — Round 88 SCORECARD section (W1)

Do not append this draft to `SCORECARD.md` without integration and L1 review. It summarizes reports available at W1's two 60-second wait-checks plus later arrivals read during finalization; it is not a closure record. Scores remain unassigned: no bounded score rubric is in evidence. Counts and exit codes are measurements, not scores or verdicts.

## Round 88 — proposed claim rows (all verdicts pending)

| # | axis / claim | proposed verdict | measured before → after | evidence and limit |
|---|---|---|---|---|
| C1 | calibration — provenance stop cause and disclosure | **PENDING-L1** | Baseline measured; X2 is an incomplete scratch alternative, and S1's A/B/C are separate prototypes. No integrated full C1 after-state. | B1/B2/C6 independently confirm 145 baseline direct tuples: 30 exit 0, 115 exit 1, 331 findings, empty stderr. B3/C6 reproduce the shape-invalid omission, mixed-stop over-attribution, and non-holder unknown-source/dangling-holder disclosure gaps. X2 changes only the shape probe (2→6 findings; 145 tuples, 144 unchanged, 1 changed; +4 findings, none removed; exits unchanged), but its `because ambiguous holder identity` wording still over-attributes when malformed shape stopped assessment first (C5). S1's separate prototypes address holder detection, first-cause tracking, and neutral wording, but are not a composed candidate. C5 also identifies an expected disclosure delta in existing `r87-probe-record-and-chain` from a non-object first record. TODO: measure and enumerate the composed integrated candidate; do not assume all 145 tuples stay unchanged. |
| C2 | coverage — second sourced-mythology cluster | **PENDING-L1** | Baseline inspiration-note count 1; M1, M2, and M3 each report a scratch candidate count of 2, but no cluster is integrated or selected. | Distinct candidate families are Japanese/Kojiki (M1), Norse/Völuspá (M2), and K'iche/Maya (M3), each distinct from r87's Sumerian/ETCSL family. M1 reports 6 resolvable passage locators, both cluster exits CLEAN, and count 2; M2 reports a delivered stanza-19 excerpt, 4/4 symbolism clauses matched, both exits CLEAN, and count 2; M3 reports both exits CLEAN and count 2, but T1/D2 identify only 1/2 exact source-clause matches and an interpretive overclaim. D2's draft checks M2/M3/M4 but does not include late-arriving M1. M4 alternatives remain unlanded; M4 recommends repoint, while C7/M5 and D2 find the absent `gate-witness` text prevents auditable support and prefer the excerpt option. TODO: select one cluster and one OBS-1 repair, resolve candidate-specific gaps, verify the chosen family/locators/index/attributions, and measure the integrated `1 → 2` count and both cluster exits. |
| C3 | depth — sourced-inspiration decision table and ETCSL ledger row | **PENDING-L1** | Baseline ledger has 3 data rows and no ETCSL row. D3/D2 ledger patch artifacts measure a fourth ETCSL row only in scratch. D2 decision-table draft exists, but is not integrated or independently checked against selected landed clusters. | D2 supplies a five-stage workflow draft with excerpt delivery and candidate-verification criteria; its companion ledger rows preserve attribution, rights, training permission, and use as separate columns. D2 checks M2/M3/M4 candidates, but not late-arriving M1; its own scope rule says the table is not against an integrated corpus. D3 and T1 confirm the ETCSL row's four-column shape and `lines 122–163` locator only in scratch. `seed.md:26-29` requires the three questions to stay separate and references outside canon. TODO: update/select a single table after cluster selection; verify every row and excerpt-delivery requirement against the delivered clusters, check all three fields, and register ETCSL on the integrated tree. |

### C1 baseline receipts and partial scratch alternatives (not integrated)

The independent census command template, run once per direct fixture directory from B1/B2's scratch archive of pinned baseline `dfd1fbc3711f2b28597d74444819aca91fe6bc31`, was:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/<dir>
```

B1/B2 report 145 matching direct tuples, exit counts `0=30, 1=115`, 331 findings, and empty stderr. C6 independently confirms B1's 145 direct tuples and captures 154 corpus-input directories. No full combined C1 candidate census is available.

B3/C6 baseline receipts:

- `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-probe-shape-ambiguous` → exit 1, 2 findings, no `unassessed` disclosure. A shape-invalid dict contains an ambiguous holder id; later assessment is neither reported nor disclosed.
- `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-probe-multi-invalid` → exit 1, 7 findings, 4 `unassessed` lines. An unknown source at record `[0]` stops the chain; later notices name holder ambiguity at `[1]` instead of the actual first cause.
- B3's unknown-source-only scratch case exits 1 with a missing-source-file finding and no disclosure. C6's unknown-source-with-unique-holders control and dangling-holder-only probe also have no tail disclosure; the dangling case exits 1 with only `to_holder: dangling entity 'missing-holder'`.
- C5 notes existing `r87-probe-record-and-chain` begins the `lamp` provenance list with a non-object at `[0]`, after which `[1]`–`[10]` are currently emitted without a tail disclosure. Under the spec's “at/after ANY stop” language, this is a known expected changed tuple to enumerate against the integrated candidate.

X2's alternative patch was measured only in `/tmp/lore-r88-X2`. `python3 /tmp/lore-r88-X2/census.py` reports 145 direct tuples: 144 unchanged stdout, 1 changed (`r87-probe-shape-ambiguous`); exits remain 30=0 and 115=1; findings `331 → 335` (+4, 0 removed); exit statuses unchanged. The changed case exits 1 with 6 findings. X2 inspects ambiguous holder fields before the shape-gate `continue`, but its disclosure says comparisons are unassessed “because holder identity is ambiguous.” C5 warns that shape-invalidity is the actual structural stop on that record, so this wording still over-attributes unless it separates stop cause from the additional ambiguous-reference finding. X2's mixed and non-holder probes also retain the first-cause and tail-disclosure gaps. It is not an integrated/full C1 fix.

S1's isolated scratch prototypes must not be summed into a claimed composite result: A changes 1 fixture (+5/-1 output lines; findings 331→335), B changes 9 fixtures (+48/-28 lines; findings 331→351), and C changes 5 fixtures (+18/-24 lines; findings 331→325). A detects shape-invalid ambiguous holders; B tracks first-stop cause (including pre-loop gates and same-record cause sets); C neutralizes causal wording but does not identify an earlier cause. S1 recommends composing and re-measuring. E1's wording alternatives are likewise proposals, not runtime evidence. No primary X1/full candidate after-state was available.

### C2/C3 bounded proposal and candidate evidence

M4 applied each OBS-1 alternative to a fresh baseline archive; both structural checker replays returned `CLEAN: schema, citations, relations, timeline; 0 violations` (exit 0). The direct text check reported:

```text
Baseline: gate_named=False; first_appearance=lowwater-hymn; claim_source=lowwater-hymn; clause_matches=7/7
Repoint:  gate_named=False; first_appearance=gate-witness; claim_source=gate-witness; clause_matches=7/7
Excerpt:  gate_named=True; first_appearance=lowwater-hymn; claim_source=lowwater-hymn; clause_matches=8/8
```

These alternatives are mutually exclusive and neither is landed. M4 recommends repoint; C7/M5 and the D2 table note `gate-witness` has no delivered witness-slip text and favor the excerpt option for direct claim support. No choice is made here.

M1, M2, and M3 each applied a different cluster patch to a fresh baseline archive; all are candidate-only, not integrated. M1's Japanese/Kojiki candidate reports a 4-line excerpt, 6 passage locators that resolve to delivered lines, a 3-row symbolism index, and CLEAN r87/new-cluster checkers (exit 0 each), with inspiration-note count 1→2. M2's Norse/Völuspá candidate reports a delivered stanza-19 excerpt, 4/4 exact symbolism-clause matches, structurally supported rows and CLEAN r87/new-cluster checkers, with fixture dirs 145→146 and note count 1→2. M3's K'iche/Maya candidate reports CLEAN r87/new-cluster checkers and note count 2; T1/D2 find its symbolism map has 1/2 exact source-clause matches (2/2 only after quote normalization) and flag “explicitly rejects” as interpretive overclaim. None is selected; M1 arrived after D2's candidate table and D2 must be updated if M1 is the selected cluster. M3's patch supplies the printed-p.209 locator and delivered English excerpt, but the external source's authenticity is not independently established in these reports.

D2's `patches/D2-decision-table.md` is a five-stage sourced-inspiration workflow proposal, not a landed knowledge file. It states excerpt-delivery, exact clause-to-element, and candidate verification criteria, and its verification cells record M2/M3/M4 scratch checks. Its companion `patches/D2-ledger-rows.md` proposes the r87 ETCSL row plus an unfilled r88 template; do not register the template. The r87 ledger row is also proposed by D3. D3/T1 report the same scratch-only baseline→patched measurement (3→4 data rows, one ETCSL row, four columns, locator present at lines 122–163). D2 predates M1's late arrival; T1's report predates D2's artifact. Neither candidate table nor ledger row has been integrated or independently verified as a final selected result. The existing ETCSL note summarizes its cited passage rather than delivering the external excerpt, a limitation the final table must preserve.

### TODO before SCORECARD integration

- **C1:** compose a candidate that distinguishes structural stop cause from holder ambiguity and discloses every record at/after all stop classes; resolve same-record and pre-loop-cause scope; replay 145 direct fixtures plus targeted controls; enumerate expected and unexpected tuple deltas (including `r87-probe-record-and-chain`); verify no removed findings/exit changes beyond declared scope and no causal overclaim.
- **C2:** select exactly one of the Japanese/Kojiki, Norse/Völuspá, or K'iche/Maya patches; complete non-author locator, map, and attribution checks; correct any M3 exact-clause/interpretive defects if selected; choose and land one OBS-1 alternative after resolving M4 vs C7/M5/D2 evidence; measure inspiration-note count and both delivered cluster exits.
- **C3:** reconcile/update D2's workflow table for the selected cluster; verify its distinct attribution, rights, and training-permission fields, excerpt-delivery rules, and every row against the actual delivered clusters; integrate the ETCSL ledger row and verify its exact locator/columns.
- Keep all three verdict cells **PENDING-L1** until integrated evidence and independent adjudication exist. Do not infer rights or AI-training permission, assign scores, or record round admission from scratch candidates.


