# Round 7 executor report — source-ID qualification

## Implementation

Added one count per source ID while retaining the existing duplicate-source-ID diagnostic and every input row. All source references now classify as unknown, unique, or ambiguous: entity first appearances and claims, relation citations, timeline citations, item provenance citations, and contradiction-ledger event-source references. Unknown retains its prior wording at ordinary reference sites; ambiguous references report `ambiguous in-world source` at each local reference and are not called unknown.

Alliance reverse witnesses now qualify only when their source ID occurs exactly once. An ambiguous reverse edge does not qualify; a distinct uniquely sourced reverse edge can still satisfy reciprocity. Item provenance keeps its structural tick/holder-chain check independent of citation qualification. Where an ambiguous source exists in that item's chain, any structural chain finding is explicitly labeled `input-structural finding, not sourced-canon`. Unique-source chain diagnostics retain their previous text. These checks establish ID identity/structure only, not source-text support or canon truth.

## Regression replay

Ran `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<case>` against all twelve pre-existing cases: `consistent` (0), `contradictions` (3 violations), `ally-one-way` (1), `ally-reciprocal` (0), `contradictions-ledger-malformed` (4), `item-chain-valid` (0), `item-chain-broken` (1), and all five r5 malformed/invalid cases (each 1). The outputs were unchanged, including the unique-source provenance chain-break wording.

## Round-7 fixture replay (fixtures supplied by parent)

- `r7-ally-reverse-ambiguous`: exit 1; retains duplicate-ID finding, reports the affected reverse relation's ambiguous source locally, and reports that the unique-source forward relation lacks a qualified reciprocal. No arbitrary source row is selected.
- `r7-item-ambiguous`: exit 1; retains duplicate-ID finding and emits local ambiguous-source diagnostics for every affected first appearance, claim, and provenance record. No unknown-source diagnostic is substituted.

No fixtures, source rows, or canon assertions were changed. This report and checker are the only edited paths; no commit was made.
