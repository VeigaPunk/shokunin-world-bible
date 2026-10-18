# V12 — C3 semantics-boundary audit (2026-10-17)

Axes: calibration precision, delivered-artifact traceability, reproducible gate behavior. Scope is T4's `corpus/knowledge/r100-provenance-semantics-boundary.md`, its cited evidence, and agreement with r99 AC-1/AC-2/AC-3; this is not round-wide admission or a separate C2 synthesis audit.

All commands ran from `/home/vgpnk/Projects/shokunin/lore-shokunin`, with `python3` for Python. No nested agents, network, commits, pushes, live fixture mutations, valid live `--freeze`, or writes to another seat's paths. The deliberately invalid combined invocation was rejected before a write. All V12 writes are this report and `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V12-scratch/`.

## Delivered artifacts, not a plan

The bounded producer poll checked all three T4 knowledge artifacts and an actual `T4*.md` producer report every 20 seconds, maximum 40 attempts. It completed on attempt 26, after 500 seconds:

```text
POLL 1/40 missing=['corpus/knowledge/r100-provenance-semantics-boundary.md', 'corpus/knowledge/r100-crossing-arc-synthesis.md'] T4_reports=[]
POLL 26/40 missing=[] T4_reports=['.ufo/waves/round-100/seats/T4-knowledge-author.md']
READY: T4 delivered artifacts and producer report exist
```

The note, the completed producer report `T4-knowledge-author.md`, the table's delivered addendum, implemented tools, and T4's actual replay transcript were read after readiness. No all-reports poll or stall escape was used; no needed background task remains.

Final observed SHA-256 values, unchanged through the audit:

```text
r100-provenance-semantics-boundary.md 29cc7d856b2600bbb03dec577487bc0f09525ab444a3e3109ef0040ab7edeb36
r99-gate-blind-spot-table.md          f1b3719a3954bbae44562f9e01b99434327ff50fba0c3a0755634dc9d76830ff
dependency_freeze.py                 fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c
dependency-freeze-contract.json      ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5
```

Observed HEAD was `b5fe472957ab1e4e9c90f5613acc14cd24a288ae` (r100 declaration), with `fe1ce466e9d7427948c0abe4ecfbf961880b72ff` the named r99 closure ancestor. This is declaration history, not a substituted baseline.

## Citation and claim-by-claim audit

Actual command:

```sh
python3 .ufo/waves/round-100/seats/V12-scratch/audit_boundary.py
```

Observed output excerpts (complete receipt in `V12-scratch/citation-audit.txt`):

```text
CITED_ARTIFACTS: PASS 14 paths; missing=[]
CITED_RANGES: PASS 16 full/continued ranges; invalid=[]
NOTE_DELIVERED_HASH: PASS 29cc7d856b2600bbb03dec577487bc0f09525ab444a3e3109ef0040ab7edeb36
CONTRACT_DELIVERED_HASH: PASS ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5
PRE_R99_SUPPORT_UNCHANGED: PASS
HISTORICAL_TABLE_PREFIX: PASS 20526 baseline bytes
SIMULTANEOUS_EDGE_AND_PROSE: PASS
EXACT_SEVEN_PIN_BOUND: PASS
R88_EXTRA_FILE_UNPINNED: PASS
BOUNDARY-AUDIT PASS failures=[]
```

The audit also compared each of T4's four delivered tool/contract/support mirrors byte-for-byte with the live delivered files, the historical mirror with `git show 4265df5:<path>`, the three excerpt-only mutation definitions, and the simultaneous edge/prose definition: all passed. The independent script is read-only; it does not run T4's harness because that harness would rewrite T4's scratch outputs.

Every substantive claim is traceable to delivered artifacts; the note's `source:` header and citation convention cover its bare tool references, and its inline numeric ranges resolve to the described code rather than just existing line numbers:

- **Note lines 8, 12, 14–18: PASS.** `dependency_freeze.py:109-116`, `:145-213`, `:297-355`, `:358-398`, and the delivered schema-2 contract establish a path-bound comparison of ten declared files plus modeled inventory. The note correctly conditions named-file `DIGEST-MISMATCH` on an evaluable invocation and clean inventory. It does not turn a digest comparison into source authentication.
- **Note lines 18, 20: PASS.** `dependency_freeze.py:220-262`, `:384-394`, `:640-648` and `LOG.md:3303-3313` support the exact AC-1/AC-3 distinctions. “Semantic” is explicitly limited to modeled JSON inventory, not natural-language understanding. CLI validation is correctly distinguished from valid-verification precedence.
- **Note lines 24–26: PASS.** Inventory comparison does not infer the right predecessor or whether prose entails it. `support_check.py:215-377` checks inventory, fixed strings, spans and modes; `map_obligations.py` compares raw obligations/pointers/source IDs; `check_bible.py` checks schema, citations and structural chronology. The cited r95 map's lines 49 and 53 explicitly document editorial tick/ID normalization and lexical-not-entailment scope. These support the note's refusal to infer testimony truth, authenticated chronology, authority, blame, resolution or canon.
- **Note lines 27–28: PASS.** The declared-file constant and pin payload exclude r88's `symbolism-clause-map.md`; `corpus/tools/README.md:338` records that bound. `freeze()` is visibly a contract writer, not immutable authenticated history. No implemented receipt evaluates copyright, reuse/training permission, cultural authority or authenticity; the note leaves these unassessed, rather than asserting a positive rights/authority finding.
- **Note lines 32–36, 48–51: PASS.** The historical record is correctly identified as row 6 of the existing r99 table, not a fabricated r98 table. Its all-green class excludes an unmatched mapped verbatim anchor. The freshly added rows 10–12 and actual probes reproduce the r99 corrections. Regression success is explicitly capability evidence, not semantic certification.
- **Note line 55: PASS.** Seven pinned fixtures through r99 pass, while r100 is explicitly not claimed pinned. This separates byte coverage from semantic adequacy and source truth.

No unsupported guarantee, incorrect source citation, or contradiction with the r99 AC corrections was found. Global source metadata is not being mistaken for fresh empirical proof: replay claims were independently exercised below.

## Actual AC replay commands and observed outputs

The following commands were independently re-run against T4's delivered, byte-checked mirrors (verification only). Exact commands, complete digest finding lines, selected receipts and exits are preserved in `V12-scratch/t4-replays.txt`; omitted PASS rows are not findings.

**AC-2: mapped verbatim anchor removal was already support-visible.**

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replays/pre-r99-anchor/corpus/tools/support_check.py .ufo/waves/round-100/seats/T4-scratch/replays/pre-r99-anchor/corpus/fixtures/r95-crossing-aftermath
python3 corpus/tools/support_check.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-anchor/corpus/fixtures/r95-crossing-aftermath
```

Both observed:

```text
FAIL J14: source-support; mode=verbatim; anchor=not-found
SOURCE-SUPPORT 14/15; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 17/17; VALIDATED-ROWS 16/17
FAIL: J14: source-support anchor missing
RESULT FAIL
exit=1
```

`git show 4265df5:corpus/tools/support_check.py` is byte-identical to delivered support (`55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c`). Historical and delivered freeze controls were also re-run:

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replays/pre-r99-anchor/corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/T4-scratch/replays/pre-r99-anchor/corpus/fixtures/r95-crossing-aftermath
python3 .ufo/waves/round-100/seats/T4-scratch/replays/delivered-anchor/corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-anchor/corpus/fixtures/r95-crossing-aftermath
```

Historical: `DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9`, `RESULT PASS`, exit 0. Delivered: `FINDING DIGEST-MISMATCH` naming `fictional-excerpts.md` with content digest `b97a3b80df29110f6f369c7bd52ee09cd733e46f3f7d84420563c931744f7dca`, `RESULT ERROR`, exit 2. Thus historical freeze blindness is not all-gate blindness for this mutation.

**AC-1: a simultaneous semantic-inventory and prose change does not promise a digest finding.**

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replays/delivered-precedence/corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-precedence/corpus/fixtures/r98-clerk-filing
```

Complete observed stdout, exit 1:

```text
FREEZE r98-clerk-filing: events 7/7; dependency-edges 5/6; relations 1/1
FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']
RESULT FAIL
```

No `DIGEST-MISMATCH`. The independently re-run prose-only twin command:

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replays/delivered-prose-control/corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-prose-control/corpus/fixtures/r98-clerk-filing
```

Observed `events 7/7; dependency-edges 6/6; relations 1/1`, `DIGEST-MISMATCH` naming `fictional-excerpts.md`, content digest `c811669ea2534d48122939e270599376160b8f5936eecb2e766c141464b6808b`, `RESULT ERROR`, exit 2.

**AC-3: invalid combined invocation has exactly one usage finding.**

```sh
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing --freeze corpus/fixtures/r98-clerk-filing
```

Complete observed stdout, exit 2:

```text
FINDING INVALID-ARGUMENTS: pass either a fixture (verify) or --freeze DIR, not both
RESULT ERROR
```

No inventory/digest receipt. Live contract hash after the command remained `ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5`, identical to the pre-command delivered contract.

## Independent controls and bounded coverage

Before T4 readiness, V12 prepared its own six path-bound scratch mirrors and independently exercised the already-delivered tools; those preparatory runs were not treated as verification of an absent note. `V12-scratch/replays.txt` retains all 18 exact commands and observed receipt excerpts/exits:

- Excerpt-only J14 replacement: checker CLEAN 0, map PASS 0, support FAIL 1, freeze `DIGEST-MISMATCH` 2.
- Coherent excerpt+J14 replacement: checker CLEAN 0, support PASS 0 (`SOURCE-SUPPORT 20/20`, `VALIDATED-ROWS 22/22`), map PASS 0 (`raw=20 mapped=20`), freeze `DIGEST-MISMATCH` 2 naming both Markdown files.
- Non-anchor map prose replacement: the same three lexical/structural gates stay green, while freeze names `claim-excerpt-map.md`, exit 2.
- Edge-only reduction: freeze `REDUCTION-DETECTED` 1 without digest finding; other three gates remain green.
- Edit only r88's extra `symbolism-clause-map.md`: freeze remains `RESULT PASS` 0, digest `acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae`.

These controls support the note's detectability/meaning and declared-file distinctions; lexical-green is not asserted to prove entailment.

Actual regression command (byte-identical delivered tool and contract; all self-test temporary writes contained within V12 scratch):

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V12-scratch/clean/corpus/tools/dependency_freeze.py --self-test
```

Observed 18 `CASE … ok` lines, including `markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok`, then `SELF-TEST 18/18`, `RESULT PASS`, exit 0. No temporary self-test directories remained afterward.

Actual live verification commands, independently run concurrently, each `RESULT PASS`, exit 0:

```sh
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r88-m3-maya-cluster
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse
```

The r99 receipt was `FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1`, `DIGEST 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e`. The exact pin-set/ten-files checks in `audit_boundary.py` passed against the unchanged delivered contract.

Actual negative coverage control:

```sh
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r100-docket-review
```

Observed `FINDING UNPINNED-FIXTURE: no pin for 'r100-docket-review'` listing exactly the seven named pins, `RESULT ERROR`, exit 2. This is the declared coverage bound the note retains, not a failed claim that r100 should be pinned.

`git diff --check -- corpus/knowledge/r99-gate-blind-spot-table.md` exited 0 with no output. `git diff --name-only --` restricted to the four live gate/checker files and inherited r88/r98 fixture paths returned no output; V12 modified no production bytes. The historical table's 20,526-byte baseline prefix remains intact.

## Verdict and remaining limits

Calibration precision PASS; delivered-artifact traceability PASS; reproducible gate behavior PASS. No required correction was identified in this seat's scope. The note's semantic non-establishment, unassessed rights/permission, extra-file exclusion, mutable integration-time pin operation, and unpinned r100 tick-16 edge are explicit bounds, not silently discharged debt. C2 synthesis correctness and round-wide admission remain with the assigned seats.

Created report: `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V12-c3-boundary.md`. Created scratch only: `V12-scratch/audit_boundary.py`, `citation-audit.txt`, `replays.txt`, `t4-replays.txt`, and the six isolated mirror subtrees `clean/`, `mapped-anchor-removal/`, `coherent-anchor-replacement/`, `narrative-only/`, `semantic-precedence/`, `outside-ten/`. `clean/` also contains the r95 self-test base. Scratch mutations were made only with exact Read→Edit operations; no other seat's scratch was rewritten.

PASS — the delivered semantics-boundary note is artifact-backed, preserves all r99 AC distinctions, reproduces the claimed gate behavior, and makes no byte-identity-to-semantics overclaim.
