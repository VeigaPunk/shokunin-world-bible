# V19 — freshness (2026-10-17)

Axes: **freshness**, **calibration**, and **C9 recheck readiness**. Scope: the delivered r100 corpus additions/edits and their current digest references, not independent admission of C2's prose semantics or the whole round. Baseline `fe1ce466e9d7427948c0abe4ecfbf961880b72ff`; live HEAD `b5fe472957ab1e4e9c90f5613acc14cd24a288ae` (declaration, with the wave tree uncommitted).

**Result:** the new corpus bytes have no stale active pin identified; the four required document digest spots pass. The seven-fixture chain and C9 runtime pair are fresh. C9's r100 check-log row remains due, and two separately scoped documentation/report follow-ups are recorded below rather than hidden.

## Ownership and waiting

Every command ran from `/home/vgpnk/Projects/shokunin/lore-shokunin`, using `python3`. V19 wrote only this exclusive report and these declared scratch files:

- `.ufo/waves/round-100/scratch/V19-freshness/audit.py`
- `.ufo/waves/round-100/scratch/V19-freshness/audit-output.txt` (first delivered-tree replay)
- `.ufo/waves/round-100/scratch/V19-freshness/audit-final-output.txt` (expanded final replay)

No corpus, tool, contract, producer report, or C9-watch file was changed by V19. No nested agents, network, commits, pushes, or live `--freeze` operation. The report's absolute resolution was checked before Write. The initial direct AGENTS Read found no lane-root file, and the recursive lane AGENTS glob found none. Initial missing seats/artifacts were readiness observations, not verification verdicts.

The actual bounded poll command required both artifacts and all four producer reports; it slept 20 seconds between tries, maximum 40:

```sh
python3 -u - <<'PY'
from pathlib import Path
from datetime import datetime, timezone
import time
root = Path.cwd().resolve()
assert root == Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
seats = root / '.ufo/waves/round-100/seats'
files = ['entities.json','relations.json','timeline.json','sources.json','contradictions.json','README.md','claim-excerpt-map.md','fictional-excerpts.md','inspiration-note.md','source-excerpt.md']
artifacts = ['corpus/fixtures/r100-docket-review/' + x for x in files] + ['corpus/knowledge/r100-crossing-arc-synthesis.md', 'corpus/knowledge/r100-provenance-semantics-boundary.md', 'corpus/knowledge/r99-gate-blind-spot-table.md', 'corpus/tools/dependency-freeze-contract.json', 'corpus/tools/README.md', 'SKILL.md']
for attempt in range(1, 41):
 reports = {prefix: [p.name for p in sorted(seats.glob(prefix + '*.md')) if p.is_file() and p.stat().st_size] for prefix in ['T1', 'T2', 'T3', 'T4']}
 missing = [rel for rel in artifacts if not (root / rel).is_file() or not (root / rel).stat().st_size]
 print(datetime.now(timezone.utc).isoformat(), 'poll', attempt, 'reports', reports, 'missing', missing, flush=True)
 if all(reports.values()) and not missing:
  print('READY artifacts+producer-reports present', flush=True)
  break
 if attempt == 40:
  print('ABSENT bounded poll exhausted', flush=True)
  raise SystemExit(3)
 time.sleep(20)
PY
```

Observed terminal lines, exit 0 after 480 seconds:

```text
2026-10-18T02:40:23.341877+00:00 poll 25 reports {'T1': ['T1-chain-seven.md'], 'T2': ['T2-fixture-author.md'], 'T3': ['T3-fixture-docs.md'], 'T4': ['T4-knowledge-author.md']} missing []
READY artifacts+producer-reports present
```

All four actual producer reports were then read. No plan was treated as implementation. No all-verifier-reports poll was needed (so no SELF-inclusive endgame wait); no bounded stall escape was used. The poll finished before this report.

## Actual delivered-tree verifier command

The final audit was executed as this real subprocess, with stdout/stderr saved to the final scratch receipt:

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/scratch/V19-freshness/audit.py
```

Observed wrapper output: `AUDIT_EXIT 0 OUTPUT_BYTES 41257`. The script is retained for exact reproduction; `.ufo/waves/round-100/scratch/V19-freshness/audit-final-output.txt` contains every child command, complete gate stdout, stderr, exit, current digest, and freshness-reference scan. The earlier replay also exited 0 (`OUTPUT_BYTES 39724`).

The sweep covered the changed `SKILL.md` freeze row, the tools README r100 addendum, the table's dated addendum, both new knowledge notes, and every Markdown file in the new fixture; all ten new fixture files were hashed. Existing-file comparison was against `git show fe1ce46:<path>`, not an assumed clean HEAD.

### Four current document digest spots

Observed output from the final command:

```text
SPOT-PASS corpus/tools/dependency_freeze.py fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c corpus/knowledge/r99-gate-blind-spot-table.md:274
SPOT-PASS corpus/tools/dependency-freeze-contract.json ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5 corpus/knowledge/r100-provenance-semantics-boundary.md:40
SPOT-PASS corpus/fixtures/check_bible.py ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 corpus/knowledge/r100-crossing-arc-synthesis.md:111
SPOT-PASS corpus/tools/support_check.py 55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c corpus/knowledge/r99-gate-blind-spot-table.md:284
REQUIRED_DIGEST_SPOTS 4/4 current
```

The table's current contract hash at `:274` and `:371` also equals `ea012b9c…`; the same tool/contract pair is in the boundary note at `:40`. Additional matching references: synthesis `:111` map tool `86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9`; tools README `:381`, `:383`, `:405`, table `:375`, and boundary note `:55` all carry r99's actual aggregate digest `7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e`.

Historical and mutant digests were not misclassified as current-file pins. In particular, table `:284` explicitly labels the `4265df5` tool/contract as historical, and `:320`/`:352` explicitly distinguish mutation digests from the frozen pin. The old top-of-table `8c2561b0…` contract measurement remains historical text, not the addendum's current measurement.

### Supersessions, inventory, and pin freshness

Observed final-audit lines:

```text
PIN_COUNT 7
PINS_ADDED ['r99-window-lapse']
PINS_REMOVED []
PREEXISTING_PIN_FIELDS_UNCHANGED True
SELF_TEST_EXPECTATION_COUNT 18
PIN_FILE_DIGEST_CHECKS 70 mismatches=[]
TABLE_APPEND_ONLY historical_bytes=20526 dated_rows=3 old_contract_pin_not_carried_into_addendum=True
SNAPSHOT_STABLE True
CONTRACT_STABLE True
```

All seven aggregate digests recomputed from the current filename-to-file-hash payload matched their contract values. The six inherited pins retain every field, including their historical revision `337f0fa52b02626b7687eedbb2d99fab30446fe4`; the new r99 pin names `b5fe472957ab1e4e9c90f5613acc14cd24a288ae`. Historical revision fields do not require changing when their pinned bytes are unchanged. T1 correctly discloses the guarded writer's top-level revision refresh at tools README `:389`; this is not an addition-only textual contract diff.

Current wording is explicit:

- `SKILL.md:96-102`: seven chain fixtures; ten-file payload; 18 expectations; dated six-to-seven supersession.
- `corpus/tools/README.md:363-421`: seven-fixture coverage; old six-fixture receipts retained as history; r100 expressly excluded from this frozen set.
- `corpus/knowledge/r99-gate-blind-spot-table.md:272-375`: exactly three dated rows 10–12; current tool/contract measurements; `:375` supersedes the old r99-unpinned/six-fixture wording.
- `corpus/knowledge/r100-crossing-arc-synthesis.md:8,63`: r94 seed plus six continuations, seven dossier snapshots; explicitly distinguishes those snapshots from the seven frozen fixtures (r88 plus r94–r99).
- New fixture README `:3,21` and map `:3-5,43,72`: 6/1/9, 9 sources, 22 obligations, 24 mapped rows, 20 anchors, new anchor at excerpt line 82. No carried r99 count is presented as the new fixture's count.

The final audit inventories 18 persisted freeze expectations; V19 did not run `--self-test` and does not offer that count as its own 18/18 self-test receipt.

## Live checks supporting those documentation numbers

These exact child commands were executed concurrently by the audit, all with empty stderr and exit 0:

```sh
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r88-m3-maya-cluster
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse
```

All seven printed `RESULT PASS`; complete receipts are in the final scratch output. The seventh's actual stdout was:

```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
DIGEST 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e
RESULT PASS
```

The new fixture's actual commands and observed output (support output excerpt explicitly abbreviated):

```text
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r100-docket-review
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT 0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r100-docket-review
OBLIGATIONS raw=22 mapped=22
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24
RESULT PASS
EXIT 0
$ python3 corpus/tools/support_check.py corpus/fixtures/r100-docket-review
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24; DISTINCT-ANCHORS 20/20
SOURCE-SUPPORT 22/22; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 24/24; VALIDATED-ROWS 24/24
RESULT PASS
EXIT 0
```

The same final audit enumerated fixture directories and invoked `python3 corpus/fixtures/check_bible.py corpus/fixtures/<name>` for all 174 (16 concurrent subprocesses), using repository-relative argv. Observed summary:

```text
CENSUS directories=174 exit_counts={0: 40, 1: 134}
CENSUS violations=421
CENSUS stderr_nonempty=[]
```

This independently corroborates the synthesis's current directory count and the new fixture's clean contribution. It is not a testimony, chronology, semantic-entailment, or canon finding.

## C9 next-recheck state

These exact final-audit commands were executed against the delivered tree, with empty stderr:

```text
$ python3 corpus/tools/discriminate_check.py
mode=delivered checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression
EXIT 0
$ python3 corpus/tools/discriminate_check.py --checker e97613c
mode=e97613c checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=False baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=FAIL
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=False baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=FAIL
REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present
EXIT 2
```

The historical control's exit 2 / semantic FAIL lines are expected negative-control evidence, not a failing delivered discriminator. The audit also ran `python3 corpus/tools/boundary_doc_check.py`: exit 0, `CHECK pinned inputs: PASS`, receipt replay 3/3 and cases 14/14, anchors 2/2, and `CERTIFIED (bounded: frozen-document drift + receipts + explicit-anchor range + structure; no semantic/AST validation)`. The live checker equals the boundary contract's SHA-256 pin.

Observed watch-state lines:

```text
C9_DATED_ROWS 8
C9_R100_SECTION_PRESENT False
C9_BASELINE_EQUAL True
C9_SEQUENCE_SCOPE_EXCERPT_FILES []
C9_SEQUENCE_SCOPE_README_LINE3 Fixture scaffolding only; not sourced story evidence.
```

`corpus/knowledge/r91-c9-watch.md:335` remains the r99 eighth row, saying **Next re-check: r100**. The explicit ongoing owner at `:219` is the lore-shokunin calibration lane. The r100 runtime replay above has now been performed by V19, but **no ninth/r100 check-log row has been filed**. Closure follow-up: the authorized integrator should record the delivered/expected-control receipts as check 9 and set the next recheck to r101, if adopting this replay. V19 did not edit that unowned file or silently advance the pointer. The inspected durable sequence-scope evidence remains scaffolding only; this replay supplies no gate-3 evidence to reopen the ruling and is not a new four-gate falsification test.

## Separate follow-ups and contradictions

The final command establishes the following documents are all byte-identical to baseline `fe1ce46`:

```text
CARRIED_DOCUMENT_BASELINE_EQUAL corpus/README.md True
CARRIED_DOCUMENT_BASELINE_EQUAL corpus/fixtures/README.md True
CARRIED_DOCUMENT_BASELINE_EQUAL corpus/knowledge/r91-c9-watch.md True
```

- **Carried navigation staleness, not new r100 corpus harm:** `corpus/README.md:41` still advertises r98-era six-fixture/17-case/five-JSON-only freeze coverage. Actual current coverage is seven fixtures, ten declared files, 18 expectations. It should be refreshed on the next authorized navigation touch. The r100 fixture and two new knowledge notes also have no new navigation entries there.
- **Normal closure bookkeeping still pending:** `corpus/fixtures/README.md` ends at the r99 section (`:1267-1288`), with the historical 173/39/134/421 census at `:1286` and the historical r99-unpinned candidate sentence at `:1282`. Those are accurate r99 measurements, not current r100 receipts. A dated r100 entry/current census/coverage supersession remains for closure. C9's due row is separately described above.
- **Producer-report transcription contradiction, not a corpus pin mismatch:** the final audit found these exact non-SHA-256 tokens in T2's report:

```text
PRODUCER_REPORT_MALFORMED_DIGEST T2-fixture-author.md:66 length=55 c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4a6ff9
PRODUCER_REPORT_MALFORMED_DIGEST T2-fixture-author.md:153 length=55 c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4a6ff9
ACTUAL_R100_RELATIONS_SHA256 c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9
```

The real relations file, its inherited bytes, and the live pin comparisons are clean; the two quoted producer-report digest strings need an explicitly labeled report-only transcription correction by their owner/integrator. V19 did not edit another seat's report. This report does not extend its 4/4 corpus-document result into a claim that every producer-report token is correct.

Freshness judgment: **not harmed on the new corpus bytes; bounded improvement from explicit dated supersessions**. C9 behavior is retained, but persistent check-log maintenance is not yet complete. Historical bounds remain explicit: r100's tick-16 edge is unpinned, r88's symbolism map is outside the declared ten, and byte detectability is not semantic validation. All needed background work finished; no required task was left running.

PASS — delivered new-corpus freshness and 4/4 digest spots pass; seven pins and C9 behavior are fresh, with C9/navigation closure bookkeeping and T2's report-only digest transcription explicitly left for authorized follow-up.
