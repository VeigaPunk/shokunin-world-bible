# R10 cross-cluster contradiction demo

## Scope and status

This is a worked example of the R10 record format, not a new canon assertion or an integration-ready register entry. The existing side is `corpus/fixtures/r87-myth-cluster/`; the second cluster is explicitly hypothetical, is not present, and is not a landed cluster. This D3 artifact is kept at the requested `corpus/knowledge/r89-cross-cluster-contradiction.md` path; R10's live corpus register destination is `corpus/knowledge/cross-cluster-contradictions.md`. Do not treat this demo as an append to that register. Preserve both clusters and the existing local contradiction record. The checker accepts one bible directory at a time and cannot validate cross-cluster references; the procedure is a manual integration gate.

## Record: `r89-demo-moon-basin-vow-cross-cluster`

**Status:** `unresolved` (conditional worked example). A shared event identity, date, and occasion must be supported by the cited in-world accounts. Equal local ticks, matching IDs, or an external mythology parallel do not establish those conditions. The hypothetical side is only for demonstrating the record shape; it does not satisfy R10's landed-cluster trigger.

**Relative cluster paths:**

- `corpus/fixtures/r87-myth-cluster/` (existing)
- `corpus/fixtures/r89-hypothetical-moon-basin/` (hypothetical; absent from this repository)

**Existing local record:** `corpus/fixtures/r87-myth-cluster/contradictions.json#moon-basin-vow-location` already records Hara's and Sen's different location claims. It says both concern the same single Moon-Basin Vow of Saltmonth 4 during the first low-water bell.

**Hypothetical account:** `corpus/fixtures/r89-hypothetical-moon-basin/timeline.json#moon-basin-vow-river-account.place_id`, cited to the hypothetical in-world source `reed-arch-register`, asserts `reed-arch`. Its hypothetical source text would read: “The one Moon-Basin Vow of Saltmonth 4 took place at Reed Arch during the first low-water bell.” Neither the path, source, assertion, nor sentence exists in the corpus; it is invented solely for this procedure demo.

### Pair A — Hara account versus hypothetical account

- Conflicting assertions and claim pointers: `corpus/fixtures/r87-myth-cluster/timeline.json#moon-basin-vow-gate-account.place_id` (`source_id=gate-witness`; asserts `mother-tide-gate`; statement: “Hara's slip places the single Moon-Basin Vow of Saltmonth 4 at the Mother-Tide Gate during the first low-water bell.”) and `corpus/fixtures/r89-hypothetical-moon-basin/timeline.json#moon-basin-vow-river-account.place_id` (`source_id=reed-arch-register`; asserts `reed-arch`; hypothetical statement: “The one Moon-Basin Vow of Saltmonth 4 took place at Reed Arch during the first low-water bell.”).
- Why they cannot both be true as stated: if both source-attributed assertions refer to the same single vow on Saltmonth 4 during the first low-water bell, that one event cannot have both distinct place values.
- Status: `unresolved`.

### Pair B — Sen account versus hypothetical account

- Conflicting assertions and claim pointers: `corpus/fixtures/r87-myth-cluster/timeline.json#moon-basin-vow-dune-account.place_id` (`source_id=dune-register`; asserts `ash-dune-sanctuary`; statement: “Sen's register places that same single Moon-Basin Vow of Saltmonth 4 at Ash-Dune Sanctuary during the first low-water bell.”) and `corpus/fixtures/r89-hypothetical-moon-basin/timeline.json#moon-basin-vow-river-account.place_id` (`source_id=reed-arch-register`; asserts `reed-arch`; hypothetical statement: “The one Moon-Basin Vow of Saltmonth 4 took place at Reed Arch during the first low-water bell.”).
- Why they cannot both be true as stated: under the same shared-event and shared-occasion condition, the single event cannot have both distinct place values.
- Status: `unresolved`.

This record links the existing Hara/Sen pair without changing its `contradictions.json`; foreign-cluster pointers do not belong in that fixture-local ledger. Keep all three claims distinct and unresolved, and do not select a canonical location. A real-world parallel cannot adjudicate this in-world disagreement. If the texts do not support the shared event/occasion or a pair's claim, record that limit and do not promote that candidate pair to a contradiction finding.
