# B3 — Boundary-document certification script specification

## Purpose and invocation

Specify a fail-closed, read-only certifier for the re-derived `corpus/knowledge/holder-assessment-boundary.md`. It certifies the delivered document and `corpus/fixtures/check_bible.py`, not a proposed patch or an earlier checker. The implementation is intentionally not added by this seat; this file is the runnable-tool contract for the integrator/certifier.

From the lore-shokunin repository root, the conforming interface is:

```sh
python3 tools/certify_boundary_doc.py \
  --doc corpus/knowledge/holder-assessment-boundary.md \
  --checker corpus/fixtures/check_bible.py \
  --expected-checker-sha256 ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
```

The command reads the document, checker, fixture inputs, and explicitly selected historical source revisions only. It must not write files, invoke shell text copied from the document, or create `/tmp` scratch. It reports each gate and a final `CERTIFICATION PASS` or `CERTIFICATION FAIL`; exit 0 means every gate passes, exit 1 means a content/certification failure, and exit 2 means invalid invocation or unavailable required input. A nonzero gate must name its document location or fixture.

## Gate A — pin the delivered checker

1. Hash the exact checker argument with SHA-256 and require the command-line expected hash. The round-92 delivered value is `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` (428 lines at the pinned tree).
2. A mismatch is a hard failure before replay or anchor resolution; do not silently substitute the baseline checker or a working-tree proposal.
3. Resolve unqualified/current `check_bible.py:NNN` citations against this pinned checker. Resolve historical citations only when the adjacent claim explicitly names its source commit; load that source with `git show <commit>:corpus/fixtures/check_bible.py`. An unqualified citation whose target revision is ambiguous fails closed.

## Gate B — replay every pasted checker output

1. Read Markdown fences without evaluating Markdown or shell. A fenced output block is a checker receipt if it contains a checker invocation's expected output, including `VIOLATION:`, `CLEAN: schema, citations, relations, timeline; 0 violations`, the checker violation-count footer, or a case wrapper plus `[rc=N]`.
2. Pair every receipt block one-to-one, in document order, with its immediately preceding fenced `sh`/`bash` command block. Every checker invocation in such a command block must have exactly one expected result; every checker-looking receipt must be paired. Missing, duplicate, orphaned, or unsupported pairs fail rather than being skipped.
3. Support a deliberately small command grammar only: a direct `python3 corpus/fixtures/check_bible.py <repo-relative-fixture>` invocation, or a literal `for` loop over fixture names that runs that same command and emits `=== name ===` / `[rc=N]` wrappers. Expand fixture names and paths as data. Reject command substitutions, arbitrary shell commands, absolute paths, path traversal, and any target outside `corpus/fixtures/` or `corpus/live/runs/round-85/probe-inputs/`. Never use `shell=True`.
4. For each expanded invocation, run `[sys.executable, checker, fixture]` with repository-root cwd and captured stdout/stderr. Compare checker stdout byte-for-byte with the corresponding expected text after removing only the case and return-code wrappers and the Markdown fence's final newline. Require the recorded `[rc=N]` to equal the actual exit status. Stderr must be empty unless a separately labelled expected-stderr block is present and matches byte-for-byte. No whitespace, line-ending, count, or wording normalization is permitted inside a receipt.
5. Fail if any command is not understood, any fixture is absent, a receipt has no return-code record, or any output differs. Print `replay_receipts=<matched>/<found>`, `replay_cases=<matched>/<expanded>`, and each mismatch path/case.

## Gate C — resolve every code anchor by content

The anchor catalog is built from CB1's r90 D1–D13 replacement instructions, not copied from old document line ranges. For each `check_bible.py:NNN` or `check_bible.py:NNN-MMM` occurrence:

1. Extract the sentence or table cell containing the citation and assign it to exactly one catalogued claim family. Unknown or multiply matched claims fail closed.
2. Each catalog row contains (a) the claim predicates required in the document, (b) AST/token signatures for the claimed checker behavior, and (c) the AST-derived source span. Locate the behavior by function/statement content first, then derive the current line numbers. Require the written numeric anchor to equal the derived span and require the span to contain all signatures. Do not validate an anchor merely because its old line number still exists or because a manually copied line range is in bounds.
3. Seed the catalog with these source-content signatures and document assertions; AST spans are discovered from the signatures rather than hard-coded line numbers:

   | Claim family | Checker signature to locate | Document assertion to require |
   |---|---|---|
   | Raw/resolved counters | `raw_entity_id_counts`, `raw_source_id_counts`, and resolved `entity_id_counts` increments/lookups | Raw-row counts are distinct from schema-valid resolved indexes. |
   | Valid rows and indexes | `if valid: data[section].append(...)`; `def index(section)` and the entity/source index calls | Only valid rows enter the resolved index; duplicate IDs are counted/reported as described. |
   | Null and unresolved holder detail | `holder_identity_detail`; `if holder_id is None: return None`; raw/indexed counts and the “not uniquely resolvable” detail | Null contributes no identity clause; non-null unresolved identities are qualified only for the applicable holder comparison. |
   | Relation endpoint | relation `from`/`to` lookup and `ambiguous entity` error | Relation endpoint ambiguity is a local structural finding, not a provenance-chain conclusion. |
   | First-stop setup | sources-unavailable, non-item, and duplicate-item predicates assigning `first_stop` | Each named item-level cause and its origin match the delivered first-stop conditions. |
   | Record validation/causes | exact-key-set branch; record field validation; ordered `record_stop_causes` appends and `'; '.join(...)` | Each documented malformed, dangling, ambiguous, and source cause and its ordering match the code. |
   | Disclosure/latch | `report_unassessed`, `first_stop`, `origin_label`, and per-record emission | One first-stop disclosure is emitted at the arming record and later records; comparisons do not resume. |
   | Raw-presence wording | `present in raw entities but` / `absent from raw entities and`, and corresponding raw-source wording | The phrase distinguishes a rejected raw row from no raw row. |
   | Comparison gate | `if first_stop is None` enclosing comparison logic | The stated stop gate matches the delivered run. |
   | Chain/first-record forms | `from_holder != previous_holder`, `holder_identity_detail` calls, and the `from_holder is not None` first-record branch | Qualified and definite chain/first-record forms and their directions match the delivered checker. |
   | Tick semantics | `tick <= previous_tick`; tick diagnostic; prefix conditional on `chain_has_ambiguous_source` | Validated integer tick order is definite regardless of unresolved holder identity; only ambiguous source status can prefix it. |
   | CLI/exit | `VIOLATION:` printing, violation footer, `SystemExit(1)`, and clean footer | Each stated stdout form and exit behavior matches the delivered CLI. |

4. For anchors explicitly describing baseline behavior, resolve the named baseline commit separately and compare to that version's content signatures. They do not excuse a stale or misattributed delivered-tree anchor. Any omitted, stale, malformed, unqualified, or content-mismatched citation is a failure.
5. Print `anchors=<resolved>/<found>` and list each occurrence, revision, claim family, derived span, and result. Zero unresolved/unknown anchors is required.

Required C9 catalog entry: find the AST branch testing `tick <= previous_tick`; prove it is reachable only on the valid-record path after the nonnegative-integer check and the `if not valid: ... continue` guard. Find the tick diagnostic's prefix expression and require it to depend on `chain_has_ambiguous_source`, then trace that flag to the ambiguous-source-status branch. Assert the tick branch does not call `holder_identity_detail` or inspect holder identity. Its document predicates must state all of: strict order is a comparison of validated integer tick values; unresolved holder identity does not qualify a tick finding; an independently ambiguous source may supply the tick prefix. Also require the null-holder helper claim to say that `None` contributes no identity clause. A legacy or contradictory holder-qualified tick claim fails even if the correct paragraph is also present.

## Gate D — document structure and instruction cruft

Parse headings outside fenced code blocks. Strip inline emphasis/code delimiters, collapse whitespace, trim optional closing `#` marks, and compare titles case-insensitively.

- Require exactly one level-one heading.
- Require every normalized heading title at every level to be unique; report duplicates with line numbers.
- Require zero instruction markers in non-fenced prose and HTML comments. The marker set is exact and case-insensitive: `TODO`, `TBD`, `FIXME`, `REPLACE:`, `INSERT HERE`, `PASTE HERE`, `APPLY ORDER`, `OLD TEXT`, `NEW TEXT`, `INSTRUCTION SHEET`, `SECTION-REPLACEMENT INSTRUCTIONS`, and `SKIPPED AS NAMED DEBT`. Report marker text and line number. Do not flag ordinary uses such as “replaced” unless they match a complete marker phrase.
- Print `h1_count=...`, `duplicate_headings=...`, and `instruction_markers=...`; each must be respectively `1`, `0`, and `0`.

## Gate E — C9 wording and contradiction check

Check the authoritative decision-table and limits prose, not code examples alone. Require a positive statement for integer-only tick ordering, non-qualification by unresolved holder identity, and the independent ambiguous-source prefix. Reject the superseded r89 rule that unresolved holder identity qualifies a tick finding. A positive phrase elsewhere does not cancel a contradictory claim. Cross-check the text against Gate C's AST-derived C9 entry. Require `c9_semantics=PASS` only if both document and checker agree.

## Required summary

On success, print the checker SHA-256, replay receipt/case counts, anchor count, H1 count, duplicate-heading count, marker count, and C9 result, followed by `CERTIFICATION PASS`. Any failed gate prints `CERTIFICATION FAIL` and a nonzero exit. The certifier must not rewrite or normalize the candidate document; repair belongs to the reconstruction/integration seat, followed by a fresh run against the frozen delivered checker.
