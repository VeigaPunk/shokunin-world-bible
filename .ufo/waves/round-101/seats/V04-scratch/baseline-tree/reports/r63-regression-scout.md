# Round 63 regression scout — non-finite JSON token

## Scope, inventory, and pin

Regression scout only; no checker, fixture, README, LOG, or commit edits. Active fixture inventory is **125 immediate directories / 623 `*.json` paths**, counted from `.shokunin/lore/corpus/fixtures`. Round 63 LOG pins r62 work commit `80dab411111258412ffaf125d5683851372c251d` and report commit `b8c1eeed94ef677349ee32a08c2244a7b4a4d8bf`. Any candidate needs a separate pinned archive, exact full-path/raw-byte corpus comparison and all 125 raw `(stdout, stderr, exit)` tuples; this report did not perform that replay.

## Code and observed behavior

`.shokunin/lore/corpus/fixtures/check_bible.py:41-57` decodes each table via `json.loads(..., object_pairs_hook=unique_object)`, catches duplicate members and JSON decode errors as file-level failures, and validates decoded row types at `:65-76`. `unique_object` at `:16-22` rejects repeated names recursively. Python's default `json.loads` accepts `NaN`, `Infinity`, and `-Infinity` as float values even though these spellings are not JSON number values. The row validator checks required known fields/types but does not reject extra keys, so a non-finite value in an ignored extra property can pass without affecting checks.

The r63 LOG records an observed outside-repository probe: copy `consistent/`, add `"extra": NaN` under `sources[0]`, run active checker; exit **0 CLEAN**, no violation. I did not independently reproduce that probe. This is a parser/input acceptance fact, not a lore claim. The clean control and typed/nested token behavior still need matched reproducible probes before any implementation/admission decision.

## Prior art and materiality

R5 malformed-input evidence (`reports/r5-loader-scout.md`; `corpus/knowledge/2026-10-12-malformed-error-patterns.md`) covers absent file, syntactically invalid JSON, non-array, non-object row, and citation error. It explicitly bounds its cases and does not document non-standard numeric constants. R59 (`reports/r59-simplifier.md`, `reports/r59-independent-verifier.md`) introduced recursive duplicate-member rejection to prevent last-wins ambiguity; that does not address distinct parser extensions for non-finite constants. The present checker has no explicit strict-JSON contract found in the inspected README areas, so novelty alone does not settle compatibility or materiality.

**Scout recommendation: conditional GO to a small compatibility/probe gate; NO-GO to implementation/admission on evidence here alone.** A CLEAN result for an otherwise unchecked extra field containing a non-JSON token is a plausible calibration defect in the promised JSON input boundary. But rejecting every such token at any depth could invalidate existing producer output or previously accepted extensions, and file-level rejection may suppress independent checks in that table. No supported producer contract or real fixture use was established by my read-only search. Establish whether any required producer emits these constants and compare ignored extra, nested object, and typed field placements against unique valid-number controls before claiming materiality.

## Falsifier, harm, and boundary

Falsify a proposed gain if the project intentionally documents/uses Python's non-finite extension, or a supported producer requires it; also if the strictness change causes greater practical loss than the bounded false-clean it prevents. If tested, retain a unique finite-number control and existing duplicate-member behavior; vary NaN/±Infinity only in otherwise identical inputs, and establish exactly which table becomes unavailable and which diagnostics disappear. A parser hook should not invent row locations it cannot know. Preserve unrelated tables' checks; do not claim whole-table dependent consequences without replay. Exact old corpus bytes/tuples and candidate same-byte old/current comparisons are mandatory.

Rejecting malformed numeric input establishes neither source-text support nor fictional-world truth, event occurrence, chronology, canon, or rights/license/permission. No numerical JSON value here is itself lore evidence.
