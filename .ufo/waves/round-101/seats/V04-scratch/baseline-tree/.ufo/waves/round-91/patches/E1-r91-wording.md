# E1 — Round-91 wording proposal

Status: wording proposal only. This does not apply fixture or tracked knowledge-file changes. Axes: **calibration** (the certainty matches each checker predicate), **discrimination** (a silent revert changes the pinned output), and **scope** (input diagnostics do not become source or canon claims).

## README wording: `r91-c1-null-chain`

Keep both checker blocks, labelled by checker version. Add a reproducible baseline invocation so a reader can produce the `e97613c` output without extracting a worktree. From `lore-shokunin/`:

```sh
git show e97613cc276f5fa9cac49ff1900798cf6863c020:corpus/fixtures/check_bible.py | python3 - corpus/fixtures/r91-c1-null-chain
python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-null-chain
```

The first command is the `e97613c` checker; the second is the delivered checker. Expected complete stdout and exit status:

**e97613c — exit 1; stderr empty**

```text
VIOLATION: entities[3].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'mira'; got None; from_holder None is not uniquely resolvable (0 raw entity rows carry this id, but only 0 is in the resolved index)
1 violation(s); no canon changed
```

**Delivered checker — exit 1; stderr empty**

```text
VIOLATION: entities[3].provenance[1]: provenance chain break; expected from_holder 'mira', got None
1 violation(s); no canon changed
```

Rationale: `None` is a sentinel, not a holder ID whose zero-row count makes identity uncertain. Since the prior `mira` holder is uniquely resolved, the later null `from_holder` is a definite break in the supplied record fields. The fixture must retain the literal `got None` line, with no vacuous `0 raw / 0 indexed` clause, so a revert is visible.

Over-claim risk: this is an input-record continuity diagnostic, not proof that no transfer occurred in the story, that the source is false, or that canon is settled. Do not generalize the definite wording to a mismatch between unresolved non-null holder IDs.

## README wording: `r91-c1-tick-unresolved`

The fixture's duplicate raw `f3-dup` row is intentional: one of two rows is rejected by the empty `first_appearance`, leaving the compared holder unresolved. Keep the separate `first_appearance` finding visible; do not describe it as story evidence. From `lore-shokunin/`:

```sh
git show e97613cc276f5fa9cac49ff1900798cf6863c020:corpus/fixtures/check_bible.py | python3 - corpus/fixtures/r91-c1-tick-unresolved
python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-tick-unresolved
```

**e97613c — exit 1; stderr empty**

```text
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1].tick: input-structural finding, not sourced-canon; holder identity is not uniquely resolvable: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); provenance tick 1 must be greater than previous tick 3
VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
3 violation(s); no canon changed
```

**Delivered checker — exit 1; stderr empty**

```text
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3
VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
3 violation(s); no canon changed
```

Rationale: the accepted records' integer ticks (`3`, then `1`) alone decide their local ordering. The same output retains a qualified chain-break finding because that separate comparison depends on the unresolved non-null `f3-dup` identity. Only the tick line changes; it must not inherit the chain-break qualifier.

Over-claim risk: the diagnostic is about local integer ordering in these supplied provenance rows, not real-world dates, event chronology, transfer truth, or source reliability. The unresolved `f3-dup` and invalid duplicate row are fixture mechanics, not evidence of multiple in-world people or a real transfer.

## C9 watch wording

Use the following as the proposed tracked `corpus/knowledge/r91-c9-watch.md` text. S1's patch pins the same checker hash and ruling but uses angle-bracket placeholders for its future counterexample/control; this wording assigns prospective names while explicitly marking them as not yet present:

```markdown
# Round 91 C9 watch

## Pinned checker and ruling

- Delivered checker: `corpus/fixtures/check_bible.py` at r90 closure `a7c6a1773d5994246a76e4eff30d645f161920e0`.
- SHA-256: `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`.
- Ruling carried from r90 C9: after record-shape, source, and tick validation, `tick <= previous_tick` is a definite input-structural finding. Holder identity is not an operand of this comparison. An unresolved holder may still qualify a separate chain-break identity comparison; it does not by itself qualify the tick finding.
- This concerns the checker's local integer ordering rule, not real-world chronology, source reliability, ownership, or canon.

## Reproducible boundary probes (not falsifiers)

The durable pair is `r91-c1-null-chain` and `r91-c1-tick-unresolved`. Run from `lore-shokunin/`:

```sh
sha256sum corpus/fixtures/check_bible.py
python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-null-chain
python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-tick-unresolved
```

The hash must equal the SHA-256 above. The null-chain output must contain `provenance chain break; expected from_holder 'mira', got None` (exit 1, one violation). The unresolved-tick output must contain the definite `provenance tick 1 must be greater than previous tick 3` line while retaining the qualified `possible provenance chain break` line (exit 1, three violations, including the deliberate invalid-duplicate row diagnostic). These probes pin the selected behavior; they do not themselves falsify C9. The corresponding `e97613c` outputs are preserved in both fixture READMEs.

## Falsification trigger

Reopen the ruling only if a demonstrated, source-backed case shows that the integer tick finding itself needs holder-identity context. If such evidence is found, preserve it in a durable pair named `r91-c9-tick-context-counterexample` and `r91-c9-tick-context-control`; these are prospective names, not existing fixtures. The counterexample must:

1. Contain one uniquely identified, structurally valid item and valid nonnegative integer ticks in one provenance list, so item identity and tick parsing are not the reason a check stops.
2. Have a genuinely unresolved non-null compared holder, record its raw-row and resolved-index counts, and include a matched uniquely resolved control.
3. Include independently reviewable source evidence that the compared values are not on one shared item-local sequence (for example, the cited record establishes that they are holder-local ordinals whose comparison depends on resolving the holder).
4. Show that the delivered checker reports a definite inversion that the evidence makes indeterminate. A holder mismatch or unresolved ID alone does not meet this trigger.

After adding that pair, run from `lore-shokunin/`:

```sh
sha256sum corpus/fixtures/check_bible.py
python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c9-tick-context-counterexample
python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c9-tick-context-control
```

Record complete stdout, stderr and exit status, checker hashes, source excerpts, and the exact tick/holder mappings. If all four gates are met, the next C1 owner reviews a narrowly scoped tick-qualification proposal; no automatic checker change follows. Keep the chain-break qualification as a separate decision.

## Owner

S1 owns the watch design for round 91 and hands it to the next C1 calibration owner at closure. That owner runs and reviews any qualifying probe.
```

The wording distinguishes the current hostile boundary probe from a genuine falsifier. A synthetic duplicate row, unresolved holder, qualified chain-break, or unrelated ambiguity alone is not a C9 counterexample. The prospective fixture names prevent a reader from mistaking a placeholder command for a runnable probe; no evidence-backed counterexample is claimed to exist.
