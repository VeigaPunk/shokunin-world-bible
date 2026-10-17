# Round 88 F1: unknown-source-only stop disclosure

Purpose: prove that a non-holder stop produces disclosures even when there is no holder ambiguity. The unknown source at `[0]` latches an otherwise well-formed, otherwise continuous three-record chain.

## Expected after the C1 fix (integration verification pending)

- Checker exit: `1` (intentional unknown source remains a finding).
- Disclosures at `[0]`, `[1]`, and `[2]` name the unknown source `f1-nonholder-missing-source` first encountered at `entities[3].provenance[0]`.
- No holder ambiguity, chain break, or decreasing-tick finding is expected; the later records are intentionally continuous and increasing.

These are post-fix expectations, not measurements against the unpatched checker. The delivered baseline run is recorded in `.ufo/waves/round-88/F1.md`; recheck these expectations against the integrated revision.

Verified on the delivered tree at r88 closure (follow-up seat V2, line-by-line): expectations hold, exit 1, 4 findings.
