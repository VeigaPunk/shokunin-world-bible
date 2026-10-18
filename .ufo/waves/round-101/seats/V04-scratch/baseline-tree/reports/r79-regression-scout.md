# Round 79 regression scout — pinned corpus and raw CLI replay

## Scope and method

Report-only verification of the Round 79 LOG declaration against pinned baseline HEAD `46904644eba532247b263654058060ad763494ee` (working HEAD matched). I archived only the declared corpus from that object:

```sh
git archive 46904644eba532247b263654058060ad763494ee .shokunin/lore/corpus | tar -x -C /tmp/lore-r79-pin
```

I enumerated and compared every corpus-relative path and raw file byte in the pinned archive and the checkout. For all 132 immediate fixture directories, I ran the pinned checker from the archived root, then repeated from the checkout root using the same root-relative argv:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture-directory>
```

For each invocation, I compared the exact tuple `(return code, stdout bytes, stderr bytes)`; no output normalization. The archive tree is `/tmp/lore-r79-pin`. Checker SHA-256: `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81`.

## Results

- Pinned corpus and checkout each contain **1,356 files**. There are **0 missing paths, 0 added paths, and 0 raw-byte differences**. Every pinned corpus file is byte-for-byte present in the checkout.
- The corpus snapshot manifest digest is `2db2c0d08daca42bae43c8d57bf0ae28f2485fa579a1635cc6f9e12ac6997f9c`; calculated as SHA-256 over sorted lines `<relative-path> NUL <byte-length> NUL <file-SHA256> LF` for all files.
- There are **132 fixture directories**, with **27 exit 0** and **105 exit 1** on the pinned archive.
- All **132/132** exact raw CLI tuples match between archive and checkout; mismatches: **0**.

## Reproduction and fixture declaration boundary

To independently replay locally, archive the pinned tree as above, list its immediate fixture directories, then invoke the command above from the archive root for each directory; capture `returncode`, `stdout` bytes, and `stderr` bytes, and repeat at the checkout root. Sort directory names for stable presentation. Do not substitute only exit-category counts for tuple comparisons.

The 27 clean and 105 failing counts are CLI outcomes for the repository's invented test fixtures, not evidence about any real-world source. A checker pass establishes only that the supplied structured records satisfy the checker’s schema/citation-ID and implemented relation/timeline checks. It does not validate prose excerpts, whether a cited source actually supports a claim, source authenticity or truth, canon, rights, or game mechanics. A checker citation-ID resolution is not textual support. Conversely, a failing synthetic fixture reports an implemented checker violation, not a real-world lore finding.

This replay supports corpus preservation and baseline regression compatibility only. It does not judge whether a new fictional claim is useful or deep, nor whether prose is true or canon. The only repository mutation from this task is this report; I did not edit LOG, corpus, or checker, and made no commit/push/merge.
