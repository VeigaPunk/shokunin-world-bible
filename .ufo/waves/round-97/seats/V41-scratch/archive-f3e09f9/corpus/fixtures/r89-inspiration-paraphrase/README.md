# R9 paraphrase-delivery negative demo

This is a minimal fictional bible for the in-world source `ash-ledger`. Its delivered `ash-ledger-excerpt.md` is explicitly a modern paraphrase, not the source's own text; the underlying wording is not included. The entity claim and excerpt deliberately share the exact anchor `moved to the west stair`.

R9 requires declaring the excerpt's delivery mode (verbatim, translation, paraphrase, or summary) in both the excerpt and each claim-to-excerpt map entry, with the path, line span, and paraphrase author/editor when known. A paraphrase is not the source's own text and cannot by itself support a claim about that source; it documents only the existence of the retelling, and its anchor only proves that the phrase occurs in the paraphrase. The underlying source text is marked `not delivered / unverified`, so the mapped claim fails R9 support even though the excerpt is anchored and the bible is structurally clean. See `claim-to-excerpt-map.md`.

Replay from the repository root:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r89-inspiration-paraphrase
```

The checker is structural only; its expected `CLEAN` result does not establish excerpt fidelity or prose support. The exact anchor is present, but a fixed-string match is only a lexical preflight:

```sh
grep -nF -- 'moved to the west stair' corpus/fixtures/r89-inspiration-paraphrase/ash-ledger-excerpt.md
```

That match does not turn the paraphrase into the source's own text. A production response would re-source or rephrase the claim; it remains unchanged here only to demonstrate the R9 support failure.
