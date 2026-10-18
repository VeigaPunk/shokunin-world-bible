# V27 — verdict-freshness (round 100)

**FRESHNESS: unchanged (bounded; no material live-pin harm).** This is one freshness verdict, not round admission and not a verdict on another axis. The delivered pins, newly dated corrections, and their executable receipts were re-verified against the live wave bytes. Historical text is explicitly superseded rather than silently rewritten. I do not credit routine maintenance as an additional claimed axis-move. Carried navigation debt, unowned closure updates, and two producers' hash-transcription defects remain explicitly flagged below; this PASS does not certify those defective quoted hashes.

Baseline: r99 closure `fe1ce466e9d7427948c0abe4ecfbf961880b72ff`. Observed HEAD: `b5fe472957ab1e4e9c90f5613acc14cd24a288ae` (declaration commit), with the round's work uncommitted as instructed. Measurements name live file hashes rather than pretending this HEAD contains the delivered wave. Final stability check: `2026-10-17T23:41:47.576698-03:00`.

## Scope and readiness

All commands ran from `/home/vgpnk/Projects/shokunin/lore-shokunin`, with `python3` for Python. Only this exclusive report and `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V27-scratch/` were written. No nested agents, commits, pushes, network, live fixture edits, or contract writes. The scratch `file-manifest.json` enumerates all 86 scratch files, including copied fixtures/tools, scripts, and generated receipts. Initial direct Read found no lane `AGENTS.md`.

Actual bounded readiness command:

```sh
python3 .ufo/waves/round-100/seats/V27-scratch/poll_producers.py > .ufo/waves/round-100/seats/V27-scratch/poll.log 2>&1
```

The script checked all 16 required artifacts AND producer report prefixes T1–T4, sleeping 20 seconds between tries, maximum 40. Observed readiness at **try 24**, `2026-10-17T23:40:19.057362-03:00`, after 460 seconds:

```text
missing_artifacts=[]
missing_producer_reports=[]
T1-chain-seven.md; T2-fixture-author.md; T3-fixture-docs.md; T4-knowledge-author.md
READY artifacts=16 producer-prefixes=4
```

The poll completed exit 0. No all-reports poll or SELF wait was used; no bounded stall escape was needed. Two foreground WaitFor snapshots timed out while that same correctly spaced poll continued; neither restarted or shortened its budget. No plan was substituted for a missing report.

## Delivered-revision replay

Actual command, exit 0:

```sh
python3 .ufo/waves/round-100/seats/V27-scratch/replay_freshness.py > .ufo/waves/round-100/seats/V27-scratch/replay.log 2>&1
```

The script records every exact child command, stdout, stderr, and exit. Full log: `V27-scratch/replay.log`; structured results and before/after file pins: `V27-scratch/replay-20261017T234035/{results.json,before-manifest.json,after-manifest.json}`. It ran the independent calls concurrently and contained both self-tests' transient writes inside its own byte-identical mirror.

Observed summary:

```text
CONTRACT-PINS 7
OLD-PIN-FIELDS-UNCHANGED True
NEW-PINS ['r99-window-lapse']
R100-COUNTS {'entities': 6, 'relations': 1, 'timeline': 9, 'sources': 9, 'contradictions': 0}
FIXTURE-CENSUS 174
LIVE-INPUT-DRIFT []
LIVE-INPUTS-HASHED 100
V27-REPLAY-PASS
```

All seven actual live invocations were replayed:

```sh
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r88-m3-maya-cluster
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse
```

Each printed `RESULT PASS`, exit 0. The new receipt was:

```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
DIGEST 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e
RESULT PASS
```

Parsed comparison against `git show fe1ce46:corpus/tools/dependency-freeze-contract.json` showed every field of the six inherited pins unchanged; only the new r99 pin and tool-managed top-level `revision` differ. The new pin contains ten file digests. The revision refresh is disclosed at `SKILL.md:99` and `corpus/tools/README.md:389`; it is not falsely described as a strictly addition-only contract diff.

The actual r100 README commands reproduced the delivered receipts:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r100-docket-review
python3 corpus/tools/map_obligations.py corpus/fixtures/r100-docket-review
python3 corpus/tools/support_check.py corpus/fixtures/r100-docket-review
```

All exit 0, empty stderr. Observed respectively: `CLEAN: schema, citations, relations, timeline; 0 violations`; `OBLIGATIONS raw=22 mapped=22` / `TOTAL-ROWS 24/24` / `RESULT PASS`; `SOURCE-SUPPORT 22/22` / `VALIDATED-ROWS 24/24` / `DISTINCT-ANCHORS 20/20` / `RESULT PASS`. These remain structural/inventory/lexical observations, not semantics or testimony truth.

Other actual replay commands and outputs:

- `python3 corpus/tools/boundary_doc_check.py` → `CERTIFIED`, receipts 3/3, cases 14/14, anchors 2/2, exit 0.
- `python3 corpus/tools/discriminate_check.py` → checker `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`, `matches_pin=True`, `RESULT: DISCRIMINATION HELD`, exit 0.
- `python3 corpus/tools/discriminate_check.py --checker e97613c` → `REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved`, exit 2, expected negative control.
- `python3 .ufo/waves/round-93/deepseek/F14-postrepair-check.py` → `RESULT ALL CHECKS HELD`, `checks_failed=0`, exit 0. Its content pins, not a stale expected-HEAD assertion, still hold.
- `python3 .ufo/waves/round-100/seats/V27-scratch/replay-20261017T234035/selftest-mirror/corpus/tools/dependency_freeze.py --self-test` → `SELF-TEST 18/18`, including `markdown_tamper`, `RESULT PASS`, exit 0.
- `python3 .ufo/waves/round-100/seats/V27-scratch/replay-20261017T234035/selftest-mirror/corpus/tools/map_obligations.py --self-test` → `SELF-TEST CASES 25/25 pinned`, 25 PASS cases, `RESULT PASS`, exit 0.

Existing checker/support/map/freeze/boundary tool bytes and the boundary contract were each compared with `fe1ce46`; all were identical. The 100-input manifest stayed unchanged during the replay and again at the final check above.

## Dated knowledge records and exact row replay

Both new knowledge records open with `source:`, `verified-at: 2026-10-17`, and `recheck:`. Their current SHA-256 values match T4's final report:

```text
r100-crossing-arc-synthesis.md 6fcffc8154a11419adbcaefba6d728ee544af831cb5e1b999429404c3b243acc
r100-provenance-semantics-boundary.md 29cc7d856b2600bbb03dec577487bc0f09525ab444a3e3109ef0040ab7edeb36
r99-gate-blind-spot-table.md f1b3719a3954bbae44562f9e01b99434327ff50fba0c3a0755634dc9d76830ff
```

The semantics note's recorded freeze-tool hash is the live `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c`; its contract hash is the live `ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5`. The synthesis's checker/support/map hashes are likewise current. A local path/range sweep observed `KNOWLEDGE-PATHS-CHECKED 76 MISSING []` and `EXPLICIT-PATH-RANGES-CHECKED 18 BAD []`; this tests existence/range, not relevance or entailment.

Baseline table comparison observed:

```text
TABLE-PREFIX-PRESERVED True baseline_bytes=20526 added_bytes=8907
DATED-ROW-IDS ['10', '11', '12']
READY-HASH-DRIFT []
```

The three new rows are dated at `r99-gate-blind-spot-table.md:278-280`. Current coverage explicitly supersedes the historical r99-unpinned/six-fixture statements at `:373-375`. T1 similarly supersedes the old chain counts in `corpus/tools/README.md:363-389` and `SKILL.md:102`. The new notes explicitly distinguish r94 seed + six continuations from the seven frozen fixtures, and explicitly leave r100 unpinned; no old snapshot is relabelled as current.

I independently ran the table's exact seven published verification commands, without invoking T4's mutating preparation/replay harness or writing T4 scratch:

```sh
python3 .ufo/waves/round-100/seats/V27-scratch/replay_published_rows.py > .ufo/waves/round-100/seats/V27-scratch/published-row-replay.log 2>&1
```

Exit 0. The script first proved the three delivered mirror tool/contract pairs byte-identical to live, and pre-r99 support tool byte-identical to both `git show 4265df5:corpus/tools/support_check.py` and live. It checked every full emitted FINDING against the published table. Complete exact child commands and stdout: `V27-scratch/published-row-replay.log`; structured results: `published-row-results.json`.

Observed:

- Row 10: both support commands → `FAIL: J14: source-support anchor missing`, `RESULT FAIL`, exit 1; historical freeze → `DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9`, `RESULT PASS`, exit 0; delivered freeze → named `DIGEST-MISMATCH` for `fictional-excerpts.md`, exit 2. Full finding matched `:320` exactly.
- Row 11: `FREEZE r98-clerk-filing: events 7/7; dependency-edges 5/6; relations 1/1`; `FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']`; `RESULT FAIL`, exit 1, no `DIGEST-MISMATCH`. The prose-only twin emitted the exact full named-file mismatch at `:352`, exit 2.
- Row 12, exact live command `python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing --freeze corpus/fixtures/r98-clerk-filing` → only `FINDING INVALID-ARGUMENTS: pass either a fixture (verify) or --freeze DIR, not both` and `RESULT ERROR`, exit 2. Contract unchanged.

Terminal harness output:

```text
LIVE-CONTRACT-UNCHANGED True ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5
PUBLISHED-ROWS 3/3 replayed; commands 7/7 expected; exact findings match; no contract write
```

Separate independently authored mutations under V27 scratch also reproduced the missing-anchor/digest distinction and semantic-before-digest behavior (`mutant-results.json`). Their expected non-zero exits are evidence, not failed live gates.

## Flagged debt and receipt contradictions

1. **Carried active index staleness, not repaired.** `corpus/README.md:41` still says a 17-case freeze self-test and a five-JSON-only payload. Its current navigation stops at r99 and its chain at r98. `replay_freshness.py` compared the entire index with `git show fe1ce46:corpus/README.md` and printed `BASELINE-BYTE-IDENTITY corpus/README.md True`: the wrong 17/five statement predates this round. Correct it at closure to 18 cases, ten declared files, seven pinned fixtures through r99, while separately indexing the unpinned r100 fixture and both new notes. Do not claim this carried debt was fixed by the producer addenda.
2. **Unowned closure surfaces still due.** `corpus/fixtures/README.md` remains byte-identical to r99, ending with historical census 173 and the historical r99-unpinned candidate at `:1282-1288`. Append r100 navigation, measured census, and current pin coverage rather than falsifying its historical section. `corpus/knowledge/r91-c9-watch.md:335` remains the r99 eighth re-check, next r100; the ninth row is not yet filed. This seat reproduced the exact green discriminator pair above, so the closure append has current measurements available. Neither file is producer-owned this wave.
3. **New producer-report hash transcription defects, not live pin drift.** T1 `T1-chain-seven.md:152` and T2 `T2-fixture-author.md:66,153` quote this supposed full SHA-256 for `relations.json`:

   ```text
   c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4a6ff9
   ```

   It has **55 characters**, not 64. Actual `hashlib.sha256(...).hexdigest()` for both r99 and r100, also matching the new r99 contract pin, is:

   ```text
   c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9
   ```

   Actual audit parsed the reports' `R99 FILE ... sha256 ... matches`, `COPIED ... sha256=...`, and `BYTE-IDENTICAL ... sha256=...` lines and recomputed the referenced files. Observed `T1-SHA256 line=152 file=relations.json quoted_length=55 matches_live=False`; `T2-SHA256 line=66 ... quoted_length=55 matches_live=False`; `line=153 ... quoted_length=55 matches_live=False`. All other compared T1 r99 file hashes matched; T2's final sources/timeline/excerpt hashes matched; T4's three final knowledge hashes matched. The live relation bytes are baseline-identical and the actual pin is correct. Route append-only receipt errata to T1/T2 or record the correction in closure; do not propagate the bad hash or call it a pin mismatch. This is an evidence-transcription defect surfaced for adjudication, not silently averaged away or certified by this freshness PASS.

Actual census command, exit 0:

```sh
python3 .ufo/waves/round-100/seats/V27-scratch/census.py
```

Observed `{"clean_exit0":40,"fixture_dirs":174,"negative_exit1":134,"non01":[],"nonempty_stderr":[],"violation_lines":421}`; full per-fixture commands/stdout/exits in `V27-scratch/census.json`. A separate `git ls-tree`/`git hash-object` comparison observed `BASELINE-JSON-FILES 860`, `OLD-FIXTURE-DIRS 173`, `BASELINE-JSON-DRIFT []`; no inherited JSON bytes changed. These measurements support the closure queue, not an assertion that historical census text was false at its own revision.

PASS — FRESHNESS unchanged (bounded): delivered pins and dated replay records are current and stable; carried index/closure debt and the T1/T2 quoted-hash defects are explicitly flagged, not certified or erased.
