---
description: >
  Triggers: "world bible", "fictional canon claim", "in-world source support",
  "lore provenance", "R8/R9/R10 review". Anti-trigger: do not use for real-world
  source discovery, archive authentication, research-method design, rights or
  permission conclusions, or game-mechanics verification. Sibling arbitration:
  Lore owns fictional-world entities, relations, timeline and integration
  (PROVINCE.md:3,9); Chousa owns research method (Lore consumes its evidence,
  corpus/knowledge/r88-sourced-inspiration-decision-table.md:120-125);
  game-dev-2d owns mechanics (PROVINCE.md:9). Keep rights and permission open
  here, not adjudicated as lore (PROVINCE.md:9).
---

# Lore and world-bible craft

Use this lane for fictional entities, places, factions, items, relations, timeline events, their in-world citations, and the editorial support boundary. `PROVINCE.md` defines that scope and its refusals. A source ID is an in-world pointer, not proof of what a source says or that an event is true.

## Decision table

| Situation | Decision | Evidence and boundary |
|---|---|---|
| `corpus/fixtures/check_bible.py` reports `CLEAN` | Accept only the checked structural result: schema, citations/IDs, relations, timeline and enabled local rules. Continue to source-to-claim review. | `corpus/knowledge/r88-sourced-inspiration-decision-table.md:20`; `corpus/fixtures/r89-inspiration-paraphrase/README.md` demonstrates a structurally clean bible whose paraphrase still does not support its source claim. |
| Claim has an excerpt map and `corpus/tools/support_check.py` reports `RESULT PASS` | Treat as lexical preflight only: map inventory, delivery-mode consistency, fixed-string anchor presence and line span. Read the whole claim against the excerpt; an anchor match alone is insufficient. | `corpus/tools/README.md:10-25`; `corpus/knowledge/r88-sourced-inspiration-decision-table.md:16,77`. |
| R8: source text cannot be delivered, or influence is only plausible | If use is established, record the consulted source/locator, affected element, how consultation changed design, materiality, and what remains without the dependency; that records provenance, not passage content. If influence is only plausible, add a dated neutral `possible influence: unverified` note, not a source-use claim. R2 needs both a creator's no-source account and no contrary source-specific evidence (only a commonplace motif); if either is unresolved or fails, mark R2 unavailable. Withhold the whole element only when the dependency is inseparable and no independently supportable remainder survives; otherwise withhold the affected detail. This is an editorial screen, not proof of use or a rights ruling. | `corpus/knowledge/r88-sourced-inspiration-decision-table.md:24,28-42`; corrected hypothetical 12-cell record and parsed replay (`corpus/knowledge/r93-r8-worked-example.md#corrected-illustrative-r8-review-record`, `corpus/knowledge/r93-r8-worked-example.md#corrected-replay`; expected `record cells: 12/12`). This is not a source-use, rights, or canon finding. |
| R9: claim mapped to a delivered excerpt | Declare `verbatim`, `translation`, `paraphrase`, or `summary` in the excerpt/map, with path, span and anchor. Paraphrase/summary anchors support only that retelling, not the source's wording. Translation-backed support also needs a per-claim manual review by a non-submitter that verifies the exact printing/version, translator, source work, passage, whole-claim support and permitted scope; lexical `PASS` is not that receipt. | `corpus/knowledge/r88-sourced-inspiration-decision-table.md:25,44-79`; `corpus/tools/README.md:25`; negative case: `corpus/fixtures/r89-inspiration-paraphrase/README.md`. |
| R10: an incoming cluster resembles an account in a landed cluster | Compare a shared referent, field and occasion. Matching names/IDs alone, including a bare cross-cluster `source_id`, do not establish identity; source IDs are path-qualified namespaces. Keep unresolved candidates in the incoming README and route missing evidence; only a supported incompatible pair opens or enters `corpus/knowledge/cross-cluster-contradictions.md` as `unresolved`, preserving both accounts. The worked example is not a live register entry. This is a manual integration gate, not a checker verdict. | `corpus/knowledge/r88-sourced-inspiration-decision-table.md:26,87-110`; illustrative, non-register demo and single-directory limit: `corpus/knowledge/r89-cross-cluster-contradiction.md:1-9`. |

## Error signatures and response

- `CLEAN: schema, citations, relations, timeline; 0 violations` from `python3 corpus/fixtures/check_bible.py <cluster>` is not prose verification. `VIOLATION: ...` and exit 1 identify an input finding; repair or explicitly retain the unresolved record, then rerun. Do not infer missing history or canon from the result. See `corpus/fixtures/README.md` and `corpus/knowledge/2026-10-12-lore-decision-table.md:104-123`.
- `RESULT FAIL` / exit 1 from `corpus/tools/support_check.py` includes findings such as `delivery mode missing or mismatched`, `source-support anchor missing`, `anchor hit outside declared line span`, or inventory mismatch. Fix the map/excerpt or withhold that source-support claim. `RESULT ERROR` / exit 2 means invalid usage, cluster, or map; it is not a pass. `RESULT PASS WITH WARNINGS` / exit 0 still needs review of warnings and the whole claim. Details: `corpus/tools/README.md:10-25`, implementation `corpus/tools/support_check.py:341-417`.
- `CERTIFICATION FAIL` / exit 1 from `corpus/tools/boundary_doc_check.py` identifies a failed pinned-input, receipt-replay, explicit anchor-range, or limited structure check. `CERTIFIED` is bounded to frozen-document drift, receipts, explicit anchor ranges, and structure; anchor ranges use pinned checker bytes but do not establish referenced meaning or content. This gate does not perform semantic, AST, or general content validation. `--self-test` exercises committed inputs in an isolated temporary tree and checks expected exits/finding IDs from the pin manifest; a self-test pass is not a live-document certification, so run the default separately. See `corpus/tools/README.md` under “Round-93 addendum: boundary certification and result interpretation” and `corpus/tools/boundary_doc_check.py`.
- `REGRESSION-DETECTED` / exit 2 from the default discriminator means its pinned regression fixtures found the reverted semantics. Do not confuse the expected `--checker e97613c` negative-control result with a passing delivered run: `corpus/tools/README.md:27-36`, `corpus/tools/discriminate_check.py:81-141`.

## Executable integration checklist

1. From the lane root, run `python3 corpus/fixtures/check_bible.py <cluster-dir>` and retain its exact exit/output. This certifies only the local structural rules.
2. Map every source-attributed JSON fact to its in-world source ID, excerpt path, inclusive line span, delivery mode and distinctive fixed-string anchor. Run `python3 corpus/tools/support_check.py <cluster-dir>`; resolve all failures and warnings.
3. Read each complete mapped claim against its excerpt. Confirm the passage supports the whole claim, not merely the anchor. Do not substitute a clean schema or lexical receipt for this review.
4. For R8, file the provenance/materiality/separability record in the inspiration note and map. Keep the no-source account distinct from contrary evidence; if R2 is unavailable, follow the affected-detail versus inseparable-whole-element rule above. Route unresolved disputes through `l0-questions.md`.
5. For each translation-backed R9 claim, attach the required manual-review record next to its map row; if edition, version, reviewer access, passage, or whole-claim support is unverified, do not grant R5 support.
6. For R10, compare against relevant landed clusters manually, qualify every source ID by cluster path, establish referent + field + occasion before calling a conflict, and preserve both claims. Do not send a namespace collision or unresolved candidate to the live contradiction register.

## Gate registry

Rows follow the fleet schema in `../PROTOCOL.md:360-406`. `boundary_doc_check` now exposes `--self-test`; the missing self-tests for `discriminate_check` and `support_check` remain conformance debt, not implied passes.

### Boundary-document check

- **name:** `boundary_doc_check`
- **gate/probe:** gate
- **entry command:** `python3 corpus/tools/boundary_doc_check.py` (repository root)
- **code → class:** `0 → clean`; `1 → failed`; other codes → `could-not-evaluate`
- **self-test command:** `python3 corpus/tools/boundary_doc_check.py --self-test`; exercises the committed default and adversarial cases in an isolated temporary tree, checking expected exits and stable finding IDs. This is capability evidence, not certification of the live document; run the default command separately.
- **pinned-values path:** `corpus/tools/boundary-doc-contract.json` records the frozen document and delivered checker SHA-256 pins and full Git revisions, the legacy checker revision/digest and anchor mapping, bounded scope, and independent expected self-test outcomes. The self-test loads document, checker, legacy-checker, and fixture bytes from exact committed revisions using Git objects (`git show`/`git ls-tree`), then copies and mutates them only in a temporary tree. The colocated manifest is not independently pinned against coordinated edits to both it and the gate.
- **scope:** default run verifies the frozen document and checker digests, replays recorded checker receipts, checks explicit numeric anchor ranges against the delivered or pinned legacy checker revision, and checks fences plus limited heading/instruction-marker structure. The document digest catches other edits to the frozen document; a numeric range does not establish that an anchor points to relevant content. No semantic, AST, or general prose validation; no whole-claim support or source review.
- **owner:** `lore-shokunin`

### Checker regression discriminator

- **name:** `discriminate_check`
- **gate/probe:** gate
- **entry command:** `python3 corpus/tools/discriminate_check.py` (repository root); negative control: `python3 corpus/tools/discriminate_check.py --checker e97613c`
- **code → class:** for the valid entry commands above, `0 → clean` (delivered semantics held); `2 → failed` only with `REGRESSION-DETECTED` (expected for the negative control); `1 → could-not-evaluate` (check error/inconclusive). Argparse/usage errors also exit 2 but mean `could-not-evaluate`, not a regression verdict; require both the valid invocation and result text. Other codes → `could-not-evaluate`.
- **self-test command:** unavailable; no self-test mode/flag (`--selftest` spelling absent); conformance debt
- **pinned-values path:** `corpus/tools/discriminate_check.py` (`PIN`, `BASELINE`, fixture names) plus expected outputs in `corpus/fixtures/r91-c1-null-chain/README.md` and `corpus/fixtures/r91-c1-tick-unresolved/README.md`
- **scope:** read-only comparison of the delivered checker and the pinned `e97613c` source on two durable fixtures; not a world-bible or source-support verdict
- **owner:** `lore-shokunin`

### Claim-to-excerpt lexical support

- **name:** `support_check`
- **gate/probe:** gate
- **entry command:** `python3 corpus/tools/support_check.py <cluster-directory>` (repository root; optional `--map <path>`)
- **code → class:** `0 → clean` (including warnings); `1 → failed`; `2 → could-not-evaluate`; other codes → `could-not-evaluate`
- **self-test command:** unavailable; no self-test mode/flag (`--selftest` spelling absent); conformance debt
- **pinned-values path:** the selected cluster's map and excerpt files (examples: `corpus/fixtures/r89-inspiration-paraphrase/claim-to-excerpt-map.md` and `corpus/fixtures/r87-myth-cluster/claim-excerpt-map.md`); the map stores declared inventory/modes/anchors. No independent digest/frozen snapshot is checked.
- **scope:** one cluster's inventory, row shape, delivery-mode declarations, exact anchors, excerpt paths and line spans; does not decide whole-claim entailment, translation identity/fidelity, rights, permission, or canon
- **owner:** `lore-shokunin`

### Raw-obligation mapping completeness

- **name:** `map_obligations`
- **gate/probe:** gate
- **entry command:** `python3 corpus/tools/map_obligations.py <cluster-directory>` (repository root; optional `--frozen <dir>` demonstration: `python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93`)
- **code → class:** `0 → clean`; `1 → failed` (failed obligation comparison: `missing_obligation` / `duplicate_mapping` / `phantom_obligation` / `source_id_mismatch` / `schema_drift` / `inventory_mismatch` / `dual_pointer`); `2 → could-not-evaluate`; other codes → `could-not-evaluate`
- **self-test command:** `python3 corpus/tools/map_obligations.py --self-test`; 25 cases (r97 added `dual_pointer`) with independently persisted expected exits and finding IDs in `corpus/tools/map-obligations-contract.json`, executed as real CLI subprocesses in an isolated tree. Loader (r97): the self-test fails closed if ANY pinned case is missing from the contract (r96's subset tolerance closed). Notes: self-test binds consistency, not truth; the self-test scratch directory is created at the repository root and gitignored (see `.gitignore` `*-self-test-*/`).
- **pinned-values path:** `corpus/tools/map-obligations-contract.json` plus the digest-pinned snapshot `.ufo/waves/round-94/frozen/map-obligations-r93/expected.json` (four input digests)
- **scope:** canonical one-obligation-per-row mapping completeness and source-ID agreement between raw fixture JSON and the cluster's Markdown map, for the canonical map form (r93–r97 clusters) AND the r88-m3 legacy map dialect (r95; `OBLIGATIONS raw=10 mapped=10`, `INVENTORY … TOTAL-ROWS 12/12`); all other legacy forms (r87, r89) exit 2 `unsupported_map` (fail-closed). `schema_drift` (r95): entity records carrying sourced-claim-shaped dicts under any key other than `claims` exit 1 — bounded to that mutation class. `inventory_mismatch` (r96): declared-vs-observed map inventory mismatch is gating, exit 1; bound: a consistently regenerated declaration still exits 0. `dual_pointer` (r96 detection, r97 pin): legacy-dialect cells naming a second pointer in prose exit 1; bound: canonical-dialect variants stay `unsupported_map` exit 2 (fail-closed). No entailment, fidelity, authenticity, chronology, rights, permission, or canon judgment. Bounded residuals: round-94 BR-16; r97-debt items per the round-97 SCORECARD section.
- **owner:** `lore-shokunin`

### Dependency-edge freeze check

- **name:** `dependency_freeze`
- **gate/probe:** gate
- **entry command:** `python3 corpus/tools/dependency_freeze.py <fixture-dir>` (repository root; frozen chain: r88-m3-maya-cluster, r94-paired-crossing, r95-crossing-aftermath, r96-crossing-response)
- **code → class:** `0 → clean`; `1 → failed` (`REDUCTION-DETECTED` / `ADDITION-DETECTED` / `ENDPOINT-CHANGE`); `2 → could-not-evaluate`; other codes → `could-not-evaluate`
- **self-test command:** `python3 corpus/tools/dependency_freeze.py --self-test`; 16 cases (r97 added `SCOPE-REFUSED`, `PATH-MISMATCH`) with expectations persisted in `corpus/tools/dependency-freeze-contract.json`; the scratch directory is created at the repository root and gitignored (see `.gitignore` `*-self-test-*/`).
- **pinned-values path:** `corpus/tools/dependency-freeze-contract.json` — per-fixture repo-relative path binding, event→depends_on edge sets, relation endpoint triples, and content SHA-256 over the five JSON tables; exactly the four chain fixtures (a foreign `c3red` scratch pin written by an r96 verifier probe was removed at r96 closure, adjudication condition C-1). The r96 pin's `revision` was refreshed through the guarded `--freeze` path at r97 closure (revision-only refresh; the pin payload covers the JSON tables only — the map digest is not pinned, r97 condition C-1 erratum).
- **scope:** JSON-layer dependency edges, relation endpoints, and content digests only, over the five JSON tables per fixture. Path-bound since r97 (pins carry repo-relative paths; a byte-identical copy at a foreign path exits 2 `PATH-MISMATCH`); `--freeze` is scope-guarded to `corpus/fixtures/**` (exit 2 `SCOPE-REFUSED` otherwise) and is integration-time only; `DIGEST-MISMATCH` names the changed file. Bounds (r97-debt): the pin payload covers the JSON tables only — fixture Markdown (maps, excerpts) is not pinned; BR-01's markdown/prose half remains open; the frozen chain is the declared four fixtures (r97-crossing-acknowledgment unpinned as of r97 closure — r98 candidate); a path-less legacy pin cannot be refreshed in place (manual contract edit). No prose entailment, testimony, chronology-truth, rights, permission, or canon judgment.
- **owner:** `lore-shokunin`
