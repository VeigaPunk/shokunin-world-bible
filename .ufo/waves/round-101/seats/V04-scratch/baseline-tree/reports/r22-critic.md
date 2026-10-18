# Round 22 critic — partial recovery calibration, diagnostics, and invalid edges

## Raw observations

I inspected the current checker and ran the baseline CLI (`check_bible.py`) on temporary copies of `r20-valid-inversion`, changing only the dependent row’s `depends_on`. These are checker-input observations, not source-text chronology or canon:

| `depends_on` | stdout finding(s) | exit |
|---|---|---:|
| `["r20-prereq"]` | `timeline[1].depends_on: timeline inversion 'r20-prereq' tick 2 not before 'r20-dependent' tick 1`; summary `1 violation(s)` | 1 |
| `["r20-prereq", null]` | `timeline[1].depends_on: expected event-id strings`; summary `1 violation(s)` | 1 |
| `[null, "r20-prereq"]` | same row-level type diagnostic only | 1 |
| `[null, "missing"]` | same row-level type diagnostic only (unknown edge is masked too) | 1 |
| `["r20-prereq", "r20-prereq", null]` | same row-level type diagnostic only (inversion and repeated-member finding are masked) | 1 |
| `[{}, "r20-prereq"]` and `[["nested"], "r20-prereq"]` | same row-level type diagnostic only | 1 |

The single malformed-list diagnostic currently precedes any dependency-member diagnostics because its whole-list check occurs before the loop. Any non-string prevents all member traversal; consequently the non-string never reaches `seen_dependencies` or a dictionary lookup. The loop’s string semantics are ordered: it checks self first, then repeated; only the first occurrence is resolved for unknown/ambiguous/inversion. Inversion is reported only for a uniquely resolved ID whose two ticks are nonnegative. The row summary counts emitted findings, so recovery can increase both detail and total count while exit remains 1.

These probes establish baseline behavior only. I did not run the 64-output regression corpus and cannot verify the proposed implementation or its count/order behavior.

## Calibration challenge

Recovering string members is plausibly safe as a *separate input-level diagnostic*: a JSON string can be resolved without hashing/coercing the malformed value, and the dependent event’s other fields are already used by independent checks. But it is a policy choice, not an entailment that the row’s dependency list is valid. It must not be described as proving the malformed edge absent, satisfied, irrelevant, or chronological. Preserve the malformed-list finding even when string findings are also emitted. For malformed values, do not call `seen_dependencies` membership/addition, event-ID count lookup, or tick comparison; this matters for arrays/objects (unhashable) as well as `null`.

A subtle diagnostic regression is possible if the type test is simply moved into the loop: with `["later", null]`, the inversion may be appended before the type error, while `[null, "later"]` puts the type error first. More complex lists could interleave errors differently. If retaining exactly one existing wording/count for malformed members is the chosen contract, pre-scan whether any member is non-string, append the existing row-level `expected event-id strings` once, then traverse in input order while skipping non-strings. That preserves the current type-finding’s precedence and avoids a new per-member diagnostic/count policy. Alternatively, a per-member diagnostic is a legitimate distinct design, but it changes wording/count and should be explicitly selected and tested; do not accidentally introduce one.

Also preserve current string behavior exactly, including repeated-string handling and the existing inversion endpoint-validity gate. Do not let a malformed member suppress later valid strings, and do not let its position change which string findings are emitted. Probe malformed members at beginning/middle/end, multiple malformed members, unknown and ambiguous strings, self/repeated strings, valid inversion/order controls, negative endpoint, and a mixed row with both malformed value and string edges. A list-wide malformed diagnostic is one finding per row under current behavior, not one per malformed member.

## Recommendation (not raw evidence)

The candidate can improve coverage, narrowly: safe string edges currently hidden by one malformed member can be diagnosed while retaining that malformed-list finding. I recommend **pre-scan + one existing row-level diagnostic + per-member skip/traversal**, rather than an unqualified move of the type check into the loop. That is the least ambiguous policy given the declared wording/count constraint and preserves the current diagnostic precedence. Before admission, obtain paired raw CLI outputs and explicitly verify exact finding text/order/count, malformed-first and malformed-last, multiple malformed values, and all string edge controls; replay and inventory all 64 saved outputs. If choosing new member-local wording/count instead, declare it before implementation and make that change explicit in fixtures/docs and review. No recommendation here establishes source chronology or canon.

I did not edit the checker, fixtures, shared docs, or commit. This report is the only file I wrote.
