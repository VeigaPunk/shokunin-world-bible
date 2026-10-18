## Work performed

- Axes: **causal precision**, **regression safety**, and **reproducibility**.
- Created separate fresh `/tmp` archives from pinned `dfd1fbc3711f2b28597d74444819aca91fe6bc31`; applied X1’s patch only in the candidate archive. The patch applied cleanly and changed only `corpus/fixtures/check_bible.py` there.
- Reconstructed C6’s eight original probe/control inputs from the pinned baseline. Their `entities.json` SHA-256 values match C6’s recorded inputs exactly (8/8); no probe or checker files were written in the repository.

## Before → after measurements

**Archive and patch.** From `lore-shokunin/`:

```sh
scratch=$(mktemp -d /tmp/lore-shokunin-C6B-XXXXXX) && git archive dfd1fbc3711f2b28597d74444819aca91fe6bc31 | tar -x -C "$scratch" && printf 'SCRATCH=%s\n' "$scratch" && patch --batch -p1 -d "$scratch" < .ufo/waves/round-88/patches/X1-c1.patch
```

Observed: `SCRATCH=/tmp/lore-shokunin-C6B-1NR81u`; `patching file corpus/fixtures/check_bible.py` (exit 0). A separate pristine archive had checker SHA-256 `3ae4134d1d7d0f4b72f5ed0b344de54e886b60ab7cacd8e8ab0008521efcb237`, matching C6’s baseline capture.

**145-directory tuple comparison.** From `/tmp/lore-shokunin-C6B-1NR81u`:

```sh
python3 compare_145.py
```

Observed: 145 directories; before exits `0:30, nonzero:115`, 331 violation lines; after exits `0:30, nonzero:115`, 352 violation lines, stderr cases 0. The nine changed tuples match X1’s tuple-delta JSON exactly (full exit/stdout/stderr); the other 136 tuples match. There were 40 added and 19 removed violation lines, zero exit-code flips, and zero stderr changes. Changed paths: `r61-independent-empty`, `r61-independent-unavailable`, `r87-masked-break-from-ambiguous`, `r87-masked-break-to-ambiguous`, `r87-probe-entry-shape`, `r87-probe-multi-invalid`, `r87-probe-nonitem-kinds`, `r87-probe-record-and-chain`, and `r87-probe-shape-ambiguous`.

**Changed-line classification.** Across the changed outputs, 26 lines are **added disclosures**; 32 are **reworded disclosure line sides** (16 old notices removed and 16 replacement notices added); 19 are **other**. The 19 others are the old/new final violation-count line in each of the nine changed tuples (18 lines total), plus this new diagnostic in `r87-probe-shape-ambiguous`:

```text
VIOLATION: entities[5].provenance[0].to_holder: ambiguous entity 'dup'
```

That additional ambiguity diagnostic is a non-disclosure output change, recorded as a finding rather than hidden in the disclosure counts. Exact per-line classifications and complete changed tuples are in `patches/C6B-c1-audit.json`.

**Pre-r87 fixture check.** The requested set—basenames not beginning `r87-` or `r88-`—contains 133 fixtures. Only 131 are unchanged: `r61-independent-empty` and `r61-independent-unavailable` changed. The first adds a non-item provenance disclosure naming `provenance attached to a non-item entity`; the second adds one naming `source table unavailable`. Therefore the required “none of the 133 changed” condition is **not met**. The comparison command exited 1 because its explicit zero-change assertion failed; the census and full tuple comparison completed and were captured.

**Causal probes and controls.** From `/tmp/lore-shokunin-C6B-1NR81u`:

```sh
python3 make_probes.py /tmp/lore-shokunin-C6B-base-iIXakW /tmp/lore-shokunin-C6B-1NR81u && python3 replay_probes.py /tmp/lore-shokunin-C6B-1NR81u
```

Observed: constructed 8 inputs, replayed all 8; exits `{0:1, 1:7}`, stderr nonempty 0. Exact case stdout/stderr, disclosures, and hashes are in the JSON audit. The three probe families and their controls show:

- Shape-invalid plus ambiguous `to_holder`: both records disclose `ambiguous holder identity to_holder 'dup'`; the same-shape unique-holder control instead discloses `malformed record (unexpected field set)`. The shape-valid ambiguous control discloses ambiguity.
- Mixed stop: the unknown source at `provenance[0]` is named as first stop on records 0–2; the later ambiguity is not named as the cause. The holder-only control names ambiguity; the unknown-only control names the unknown source.
- Dangling stop: records 0–2 disclose `dangling holder to_holder 'missing-holder'`; the valid-chain control is CLEAN, exit 0, with no disclosure.

All eight probe entity hashes match C6’s original audit. Patched-checker syntax validation also passed:

```sh
PYTHONPYCACHEPREFIX=/tmp/lore-shokunin-C6B-1NR81u/pycache python3 -m py_compile corpus/fixtures/check_bible.py; status=$?; printf 'py_compile_exit=%s\n' "$status"; exit "$status"
```

Observed: `py_compile_exit=0` (exit 0).

## Findings & named debt

- **Regression requirement fails:** two of the 133 named pre-r87/non-r88 fixtures changed, although the complete 145-tuple delta matches X1’s JSON exactly. This is an explicit conflict between the requested preservation criterion and X1’s declared non-holder disclosure changes; do not report the 133-fixture check as passing.
- **Non-disclosure output delta:** the shape-invalid ambiguous-holder diagnostic is the only added non-disclosure finding line; changed aggregate counts account for the other 18 “other” lines.
- **Cause controls:** no tested control lacking the cause receives that cause’s disclosure, and the mixed-stop case preserves the earlier unknown-source cause. The simultaneous shape-error/ambiguous-holder case selects ambiguity as `first stop`, while the unique-holder shape control selects malformed shape. Both conditions are present in the ambiguous case, so this is not evidence of an absent cause being named; however, the test pair does not settle the tie-break between simultaneous causes. Keep this as a causal-precedence review note.

## Handoff

- Report: `.ufo/waves/round-88/C6B.md`.
- Machine-readable audit: `.ufo/waves/round-88/patches/C6B-c1-audit.json` (includes exact changed tuples, every changed stdout line’s classification, probe transcripts, and command/output records).
- Only these two paths were written in the repository. No tracked checker/fixture, sibling repository, or git history was modified. No commit or push was performed.