# Round 68 independent verifier — no-candidate baseline replay

## Scope and conclusion

I read the Round 68 declaration and synthesis in `.shokunin/lore/LOG.md`, the current checker, and all eight declared scout reports: `r68-dependency-scout.md`, `r68-prior-scout.md`, `r68-fixture-scout.md`, `r68-schema-scout.md`, `r68-critic.md`, `r68-simplifier.md`, `r68-scribe.md`, and `r68-regression-scout.md`. The independent reviewer report was not present at inspection. This assignment was baseline verification only.

**No Round 68 candidate exists.** There are no `r68-*` fixture directories; the checker and corpus match pinned baseline HEAD byte-for-byte. Accordingly, the results below are archived-baseline replay and matched baseline probes, **not candidate validation** and not evidence of a candidate improvement.

## Pinned archive and corpus inventory

Pinned HEAD is `c3b090fb6df57bbe8f6e2680b24045c2db33e4fe` (`git rev-parse HEAD` returned that hash). I saved the archive outside the repository at `/tmp/r68-verify-skmdiw6v/baseline` using:

```sh
mkdir -p /tmp/r68-verify-skmdiw6v/baseline
 git archive c3b090fb6df57bbe8f6e2680b24045c2db33e4fe .shokunin/lore/corpus .shokunin/lore/reports/r67-independent-verifier.md | tar -x -C /tmp/r68-verify-skmdiw6v/baseline
```

The archived baseline contains **1,320 corpus files**, including **130 fixture directories** and **709 files** under `corpus/fixtures` (**645 JSON files**). The archive also preserves the r67 independent-verifier report. I compared the full archived corpus against the working-tree corpus by relative path and raw bytes: baseline/current each had 1,320 files; **0 removed paths, 0 added paths, 0 byte differences**. Thus all pinned checker and fixture source bytes used here were archived outside the repo and also match the checked-out baseline.

## Full fixture raw tuple replay

For each of the 130 fixture directories enumerated from the archive, I ran the archived checker and the checked-out checker against the same archived fixture directory, from the repository root. Command forms were:

```sh
python3 /tmp/r68-verify-skmdiw6v/baseline/.shokunin/lore/corpus/fixtures/check_bible.py /tmp/r68-verify-skmdiw6v/baseline/.shokunin/lore/corpus/fixtures/<fixture>
python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/r68-verify-skmdiw6v/baseline/.shokunin/lore/corpus/fixtures/<fixture>
```

Compared `(exit status, raw stdout bytes, raw stderr bytes)` for each fixture: **130/130 identical; 0 mismatches**. This is an old-checker versus identical-baseline-checker replay, not a candidate comparison.

## Matched dependency probes on the baseline checker

I copied `consistent/` to four temporary directories outside the repository. Each copy changed only `timeline[1].depends_on` to a one-element list; all other input values were held constant. I used the archived pinned checker and these commands (one per value):

```sh
python3 /tmp/r68-verify-skmdiw6v/baseline/.shokunin/lore/corpus/fixtures/check_bible.py /tmp/r68-verify-skmdiw6v/probes/<blank|whitespace|unknown|known>
```

Raw observations (stderr was empty in all four cases):

| Probe dependency | Exit | Exact stdout |
|---|---:|---|
| `""` | 1 | `VIOLATION: timeline[1].depends_on: unknown event ''`<br>`1 violation(s); no canon changed` |
| `"   "` | 1 | `VIOLATION: timeline[1].depends_on: unknown event '   '`<br>`1 violation(s); no canon changed` |
| `"ghost"` (nonempty unknown) | 1 | `VIOLATION: timeline[1].depends_on: unknown event 'ghost'`<br>`1 violation(s); no canon changed` |
| `"departure"` (known) | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` |

The baseline checker therefore distinguishes the known valid control from the three unmatched index values, but emits the same *kind* of unknown-event finding for blank/whitespace and nonempty unknown input. These results concern supplied JSON and its indexed event IDs only; they say nothing about fictional-world event absence, source text, truth, canon, chronology, rights, or game mechanics.

## Limits

No implementation or fixtures were changed, and no candidate behavior was tested. This report establishes pinned baseline bytes, existing-fixture output tuples, and the four baseline probe outputs only. It makes no verdict on whether a hypothetical diagnostic replacement would be materially more actionable. No commits, pushes, merges, or canon/rights conclusions were made.
