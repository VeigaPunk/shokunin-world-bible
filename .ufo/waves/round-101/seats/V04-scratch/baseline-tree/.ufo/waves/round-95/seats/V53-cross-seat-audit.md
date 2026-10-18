# V53 — cross-seat-audit (round 95)

Seat: V53 `cross-seat-audit` (leaf verifier). Mandate: after seats land, pick 6
load-bearing quoted outputs from other seats' reports (2 checker, 2
`map_obligations`, 1 `support_check`, 1 census) and re-run each command myself;
report each as REPRODUCED or MISMATCHED with my own output.

Baseline: r94 closure `fb118c4`. Repo root: `/home/vgpnk/Projects/shokunin/lore-shokunin`.
Read-only audit: my only write is this report; scratch under `/tmp/v53-audit/`
(no repo scratch dir declared for this seat). No commits, no pushes, no network,
no nested agents. All commands run from repo root with `python3`.

## 0. Revision pins and stability at audit time

Hashes captured at the start of the audit and re-checked unchanged at audit close
(tool mtime `2026-10-17 16:26:27 -0300`, never rewritten during the audit):

```
d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108  corpus/tools/map_obligations.py
8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db  corpus/tools/map-obligations-contract.json
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py
```

Combined digest of tool + contract + all 10 r95 fixture files, identical at first
and last check:

```
4225dfe74a6b2b87c42927402dbee406f0285d4ac1f310f55435ed135adb2418  -
```

Report set: 55 `.md` seat reports present in `.ufo/waves/round-95/seats/` at audit
close. All six source reports were byte-stable across the audit window
(`sha256sum -c` of their pre-audit digests → 6 × `OK` at close):

```
9b42876a9dac58d7731c8e637d2ac58ff76f13e291168697b14bdd8a45621907  V08-c2-checker.md
30e7e53104ada68ee0176a75c5463fbf02c7499b81016f0332704d975915ba43  V44-exit-contract-c2.md
b96d55b6f5af77d641e0f50fa2247fde8f8552206784a57a03780bda9ccbeb54  V24-verdict-coverage.md
ae6c8e2afb998a6f34ab5952c77763532b9456b5dd174a495be24640e415991c  P1-tool-code.md
5f95b09e606f5ec3602112ddf6f064d7bfec0dcc5d7873535bd2909b403afab2  V45-census-paths.md
476e17c6667d4e9027ff1b720824c931e10fb0db233f3bf4157db184d36154ab  V20-doc-parity.md
```

Revision-drift note: several reports quote transient mid-flight P1 revisions
(`3f87fe8b…`, `52d838b0…`, `8eb5051d…` — V24 §0, V45 §Receipt). None of the six
audited quotes is one of those; every audited quote is a frozen-revision claim
(`d1c239cc…`), and every re-run below matched.

## Audit 1 — checker: `check_bible` on r95 (V08)

Source: `.ufo/waves/round-95/seats/V08-c2-checker.md`, §"Check 1 — check_bible on
r95 (expected CLEAN exit 0)", quoted verbatim:

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT=0
```

My re-run (exact command, stdout captured, exit code captured immediately):

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

stderr bytes: 0. Output and exit code are byte-identical to the quote (modulo the
report's `EXIT=` spelling). **REPRODUCED.**

## Audit 2 — checker: V44 negative-tick probe (exit-1 calibration class)

Source: `.ufo/waves/round-95/seats/V44-exit-contract-c2.md`, §4 table row
`neg-tick | r19-negative-tick`, quoted: `VIOLATION: timeline[4].tick: must be
nonnegative` / `VIOLATION: timeline[5].tick: must be nonnegative` /
`2 violation(s); no canon changed`, exit `1`. The report's command form is
`python3 corpus/fixtures/check_bible.py <probe dir>` with the probe under
`V44-scratch/probes/neg-tick` (its `logs/neg-tick.stdout.txt` contains exactly the
three quoted lines; I read it before re-running).

My re-run:

```
$ python3 corpus/fixtures/check_bible.py .ufo/waves/round-95/seats/V44-scratch/probes/neg-tick
VIOLATION: timeline[4].tick: must be nonnegative
VIOLATION: timeline[5].tick: must be nonnegative
2 violation(s); no canon changed
exit=1
```

stderr bytes: 0. All three lines, their order, the summary line and exit 1 match
the quote. **REPRODUCED.**

## Audit 3 — `map_obligations`: frozen-revision r88 replay (V24; identical block in P1 §2)

Source: `.ufo/waves/round-95/seats/V24-verdict-coverage.md`, §2 (revision pinned
`# d1c239cc`):

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r88-m3-maya-cluster     # d1c239cc
OBLIGATIONS raw=10 mapped=10
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12
RESULT PASS
exit=0
```

My re-run:

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r88-m3-maya-cluster
OBLIGATIONS raw=10 mapped=10
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12
RESULT PASS
exit=0
```

stderr bytes: 0. **REPRODUCED.** (Cross-check: this is also the exact block quoted
by P1 §2 and by V05 §7/§8 — three seats, one output.)

## Audit 4 — `map_obligations`: `--self-test` 22/22 (P1 §7; V05/V24 concur)

Source: `.ufo/waves/round-95/seats/P1-tool-code.md`, §7: `python3
corpus/tools/map_obligations.py --self-test` against the live contract → 22/22
`SELF-TEST PASS`, `RESULT PASS`, exit 0, with the block including

```
SELF-TEST PASS map_missing exit=2 findings=['map_missing']
SELF-TEST PASS invalid_arguments exit=2 findings=['invalid_arguments']
```

My re-run (full stdout saved at `/tmp/v53-audit/a4.out`, sha256 `430d0319…`, 24 lines):

```
$ python3 corpus/tools/map_obligations.py --self-test
SELF-TEST PASS complete exit=0 findings=none
SELF-TEST PASS missing exit=1 findings=['missing_obligation']
...
SELF-TEST PASS map_missing exit=2 findings=['map_missing']
SELF-TEST PASS invalid_arguments exit=2 findings=['invalid_arguments']
...
RESULT PASS
exit=0
```

`grep -c "SELF-TEST PASS"` → `22`; both new-case lines verbatim; `RESULT PASS`;
exit 0; stderr bytes 0. **REPRODUCED.**

## Audit 5 — `support_check`: r95 receipt (V45 §Receipt)

Source: `.ufo/waves/round-95/seats/V45-census-paths.md`, §Receipt:

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath
RECEIPT JSON-FACTS 15; EDITORIAL-ROWS 2; TOTAL-ROWS 17
SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 17/17; VALIDATED-ROWS 17/17
RESULT PASS                                                          # exit 0
```

My re-run (stdout saved at `/tmp/v53-audit/a5.out`, sha256 `463032ca…`; 23 lines,
the last being my appended `exit=0` echo):

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; DISTINCT-ANCHORS 13/13
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
... 15 × "PASS Jxx: source-support; mode=verbatim; anchor=found; ..." + 2 × "PASS S0x: editorial-row; ..."
RECEIPT JSON-FACTS 15; EDITORIAL-ROWS 2; TOTAL-ROWS 17
SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 17/17; VALIDATED-ROWS 17/17
RESULT PASS
exit=0
```

The three quoted lines match byte-for-byte; exit 0; stderr bytes 0. (The same
receipt is independently quoted by V52 §4 and V10 §2 — three seats, one output.)
**REPRODUCED.**

## Audit 6 — census sweep (V20 §1 post-integration)

Source: `.ufo/waves/round-95/seats/V20-doc-parity.md`, §1 "Post-P3-tables", quoted
recipe `python3 -I corpus/fixtures/check_bible.py corpus/fixtures/<name>` over
`sorted(p.name for p in Path('corpus/fixtures').iterdir() if p.is_dir())`, counting
exit codes, `VIOLATION:` lines and non-empty stderr; quoted result:

```
direct_fixture_dirs=169
exit0=35 exit1=134 other=0 violations=421 stderr_nonempty=[]
```

My replica: `/tmp/v53-audit/census_replica.py` (sha256 `c923230141cc8391ac15cbae9fe1ba22aa8ff470ee28023ca31c3b126560ef41`,
stdlib only, read-only) implements the quoted recipe; output (stdout saved at
`/tmp/v53-audit/a6.out`, sha256 `6cd899fc…`):

```
$ python3 /tmp/v53-audit/census_replica.py
direct_fixture_dirs=169
exit0=35 exit1=134 other=0 violations=421 stderr_nonempty=[]
```

All four counters and the empty stderr list match the quote exactly. **REPRODUCED.**
Bound: my replica recomputes the two headline counters only; V20's per-directory
tuple diff (`new_dirs=['r95-crossing-aftermath']`, `changed_inherited=[]`) was not
recomputed.

## Cross-seat observations (evidence, not audit mismatches)

1. **C3 wording: "12/12" vs the tool's `raw=10 mapped=10`.** The round declaration
   says r88 goes to "12/12 PASS". The delivered tool prints `OBLIGATIONS raw=10
   mapped=10` plus `INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS
   12/12` (Audit 3, reproduced). Three seats independently surfaced the same
   reconciliation (P1 §6.1, V24 §1d, V05 §8 "Correction"; V39 concurs): "12" is the
   map's total mapped-row count (10 JSON facts + 2 editorial rows), not the
   obligation counter. No quoted output mismatched; the delivered numbers are the
   ones I reproduced.
2. **Stale pin in a P5 artifact (not among my six).** V19 reports the knowledge
   note `corpus/knowledge/r95-aftermath-scope-note.md` pins `map_obligations.py`
   sha256 `9224a684…` while the delivered tool is `d1c239cc…`. A cross-seat
   consistency item for L1 at closure; I did not re-verify it myself (outside my
   six-command mandate).
3. **Bounded residuals reported consistently across seats.** `schema_drift` fires
   only on claim-shaped records under unexpected keys (P1 §6.3; V03 §5 records a
   deletion variant that still exits 0 with an `INVENTORY … MISMATCH` receipt);
   the inventory declaration is echoed but not gated (P1 §6.4, V39, V55); and
   `check_bible` does not report a *removed* `depends_on` (V14 §2a: exit 0 CLEAN on
   a mutated r95 copy). These are quoted in the source reports and are consistent
   with the frozen revision I audited; none contradicts my six re-runs.
4. **Mid-flight revision quotes are not audit evidence.** V24/V45 quote transient
   P1 revisions that failed r88 (`3f87fe8b…`) before the fix; those are superseded
   by `d1c239cc…`, on which every audited quote reproduces.

## Limits

- I audited 6 quoted outputs, not the C1/C2/C3 verdicts or the other ~49 seat
  reports; a mismatch elsewhere is not excluded.
- The census replica implements V20's stated recipe in my own script; it is not
  V20's script and does not recompute the per-directory tuple diff.
- Audit 2 ran on V44's scratch probe directory (their artifact); the probe bytes
  were not independently re-derived from the r95 fixture.
- The seat set was not yet complete at audit close (55 reports); late reports
  could contain claims I did not audit.

Bottom line: **PASS** — 6/6 load-bearing quoted outputs (2 checker, 2
`map_obligations`, 1 `support_check`, 1 census) reproduced exactly on the frozen
revision (`map_obligations.py` `d1c239cc…`, contract `8173bb97…`, checker
`ff9fd2aa…`, `support_check.py` `55a5eb27…`), zero MISMATCHED, with three
cross-seat consistency notes (C3 "12/12" wording reconciliation, P5 stale tool pin,
bounded residuals) recorded for L1.
