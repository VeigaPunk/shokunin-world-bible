# r65 independent verifier report

## Pinned archive and regression replay

Pinned r64 report commit `de1fc0c940d0125f3c61a5183d031468935fcd61` was archived separately at `/tmp/r65-archive-Adoi1K`. Compared the complete `.shokunin/lore/corpus` inventory and raw bytes between that archive and the current root: **1,298/1,298 paths match**, with no additions or removals; all bytes match. This includes **623 old fixture JSON files** (all identical) and **125 fixture directories**. Replayed each directory from both roots using the same root-relative argv: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<dir>`. Compared raw stdout, stderr, and exit status: **125/125 tuples identical; zero mismatches**.

## Current-checker matched probes (outside repository)

Each probe used a temporary directory outside the repo, called the current checker with the absolute temp directory path, and held the other four fixture tables byte-identical to `ally-one-way`. Endpoints stayed `quay-guild` and `bell-wardens`. Exact stdout is quoted; stderr was empty throughout.

- Original one-way row (`quay-guild -> bell-wardens`, `allied_with`, citation `harbor-compact`): exit 1; `VIOLATION: relations[0]: allied_with faction relation 'quay-guild' -> 'bell-wardens' lacks a sourced reciprocal relation`; `1 violation(s); no canon changed`.
- Forward citation changed to absent ID `missing`, reverse absent: exit 1; additionally `VIOLATION: relations[0].source_id: unknown in-world source 'missing'`; same reciprocal violation; `2 violation(s); no canon changed`.
- Unique reverse row added (`bell-wardens -> quay-guild`, same type and unique `harbor-compact` citation), forward citation unique: exit 0; `CLEAN: schema, citations, relations, timeline; 0 violations`.
- Reverse absent (original one-way row): same exit 1 and reciprocal violation as baseline.
- Reverse unique (same as unique-reverse control): exit 0, clean output above.

### r7 ambiguous reverse control

Replayed committed `r7-ally-reverse-ambiguous` as a control (not part of the matched ally-one-way temp probes). Exit 1; stdout:

```
VIOLATION: sources[2].id: duplicate sources id 'harbor-compact'
VIOLATION: relations[1].source_id: ambiguous in-world source 'harbor-compact'
VIOLATION: relations[0]: allied_with faction relation 'quay-guild' -> 'bell-wardens' lacks a sourced reciprocal relation
3 violation(s); no canon changed
```

This control has a reverse relation whose citation is ambiguous, and it does not satisfy the sourced reciprocal check.

No candidate checker exists; no candidate replay or candidate comparison was performed. These results describe current checker behavior only. They do not establish source prose, canon, or rights conclusions.
