# Round 54 independent verifier — pinned baseline

## Scope and evidence

Baseline archived separately at `/tmp/lore-r54-baseline`, pinned to `585a00f1b5c22001bb590a55276f0c22193ca305` (`craft/lore-r1`). Compared pinned baseline against the live tree: **1,149 relative paths**, same path set and identical bytes (0 differences). The fixture directory-name inventory is **95**; there are exactly **474 fixture JSON paths**, all captured by the byte comparison. The checker `check_bible.py` bytes also match (part of corpus comparison).

Replayed all 95 fixtures in both pinned baseline root and live-tree root using the same repo-root-relative argv:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>
```

Compared raw `(stdout, stderr, exit status)` tuples per fixture: **95/95 exact matches**, 0 differences. Both sides completed all runs: 24 exit 0, 71 exit 1; stderr was empty in all runs. No candidate output was substituted.

## Boundary

No Round 54 candidate fixture or checker was built or available, so this report makes **no candidate comparison, candidate-result claim, or canon inference**. This is an independent baseline archive/integrity and replay receipt only.
