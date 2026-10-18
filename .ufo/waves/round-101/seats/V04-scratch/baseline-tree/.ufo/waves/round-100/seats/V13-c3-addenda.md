# V13 — C3 dated-addenda replay (2026-10-17)

Scope: independently replay rows 10–12 of `corpus/knowledge/r99-gate-blind-spot-table.md:272-371` and verify that the historical table is append-only against r99 closure `fe1ce46`. Axes: calibration (actual behavior and exact receipts), freshness (dated additions), adjacency (historical bytes unchanged). This is a bounded C3 verdict, not round-wide admission.

## Delivery and ownership

All commands below ran from `/home/vgpnk/Projects/shokunin/lore-shokunin`; Python invocations used `python3`. The observed HEAD was `b5fe472957ab1e4e9c90f5613acc14cd24a288ae`, with the round-100 deliverables uncommitted. The comparison baseline was the requested `fe1ce46`, not HEAD.

The 20-second-cadence bounded poll reached readiness at attempt 21/40. The boundary note appeared by poll 8, the three dated rows by poll 9, and both knowledge artifacts by poll 15. After poll 21 at `2026-10-17T23:40:29-0300`, `Glob T4*` returned `.ufo/waves/round-100/seats/T4-knowledge-author.md`; that completed report was read before running any gate replay. All three owned corpus artifacts and the producer report existed. No absent plan was verified, no all-reports poll was used, and no stall escape was necessary.

V13 wrote only this absolute report path. Declared scratch `.ufo/waves/round-100/seats/V13-scratch/` was not needed and was not created. Producer mirrors were read-only inputs. In particular, I did **not** run T4's `replay.py run`, which copies files and writes T4's receipts. Instead I independently executed the exact nine table commands concurrently with `PYTHONDONTWRITEBYTECODE=1`, preventing local-import cache writes. No nested agents, network, commits, pushes, live fixture mutations, or contract writes were performed by this seat.

## Append-only and dates — PASS

Actual commands:

```sh
git diff fe1ce46 -- corpus/knowledge/r99-gate-blind-spot-table.md
git diff --numstat fe1ce46 -- corpus/knowledge/r99-gate-blind-spot-table.md && git diff --check fe1ce46 -- corpus/knowledge/r99-gate-blind-spot-table.md
```

The full diff was inspected: its only hunk appends after the old Limits paragraph; no historical line is removed or rewritten. Observed hunk header and numstat:

```text
@@ -268,3 +268,108 @@
105	0	corpus/knowledge/r99-gate-blind-spot-table.md
```

The chained whitespace check exited 0 without additional output. A read-only `python3` check used the actual baseline bytes and current bytes:

```python
path='corpus/knowledge/r99-gate-blind-spot-table.md'
base=subprocess.check_output(['git','show',f'fe1ce46:{path}'],cwd=root)
current=(root/path).read_bytes()
print('baseline lines:',len(base.splitlines()))
print('delivered lines:',len(current.splitlines()))
print('byte-for-byte baseline prefix preserved:',current.startswith(base))
print('baseline sha256:',hashlib.sha256(base).hexdigest())
```

Observed:

```text
baseline lines: 270
delivered lines: 375
byte-for-byte baseline prefix preserved: True
baseline sha256: 4670c0b71668c56c53c0bac90091531d3f0e881c7dcb2ac572d09f96ae22182e
```

The final read-only recheck also printed:

```text
TABLE baseline_bytes=20526 delivered_bytes=29433 added_bytes=8907 prefix_preserved=True
TABLE sha256 f1b3719a3954bbae44562f9e01b99434327ff50fba0c3a0755634dc9d76830ff
```

The actual new header is `## Dated addendum — 2026-10-17, round 100` at line 272. Rows 10, 11, and 12 at lines 278–280 each explicitly carry `2026-10-17 / r100`. A separate dated coverage supersession follows at lines 373–375, so historical “r99 unpinned / six fixtures” prose is retained as historical rather than silently made current.

## Replay-input audit — PASS

Before executing gates, a separate read-only `python3` audit compared each of the four T4 mirrors to the live fixture across all ten declared files. It required exactly the excerpt-only replacement `depends on both ninth-bell entries` → `follows both ninth-bell entries`; the precedence mirror additionally had exactly one parsed-value change, removal of `evin-ninth-bell` from `paired-crossing-decision.depends_on`. The audit also compared all three mirrored tool/contract files directly against delivered bytes, or against actual `git show 4265df5:<path>` bytes for the historical mirror. These were real comparisons, not acceptance of labels.

The central executed comparisons were:

```python
changes=[file for file in files if (source/file).read_bytes()!=(mirror/file).read_bytes()]
expected=['timeline.json','fictional-excerpts.md'] if case=='delivered-precedence' else ['fictional-excerpts.md']
assert changes==expected,(case,changes,expected)
original=(source/'fictional-excerpts.md').read_bytes()
modified=(mirror/'fictional-excerpts.md').read_bytes()
assert original.count(needle)==1 and modified==original.replace(needle,replace,1)
```

Observed output excerpts:

```text
pre-r99-anchor changed files: ['fictional-excerpts.md']
pre-r99-anchor excerpt-only replacement exact: True
delivered-anchor changed files: ['fictional-excerpts.md']
delivered-anchor excerpt-only replacement exact: True
delivered-precedence changed files: ['timeline.json', 'fictional-excerpts.md']
delivered-precedence excerpt-only replacement exact: True
delivered-precedence parsed timeline exact single dropped evin dependency: True
delivered-prose-control changed files: ['fictional-excerpts.md']
delivered-prose-control excerpt-only replacement exact: True
MUTATION-AND-TOOL-AUDIT PASS
```

Historical tool / support / contract SHA-256 values matched their real `4265df5` versions:

```text
dependency_freeze.py 03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b
support_check.py 55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c
dependency-freeze-contract.json 153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947
```

Each delivered mirror matched the live delivered tool/support/contract hashes recorded under Stability below.

## Row 10 / AC-2 — PASS

The following two **actual commands**, executed independently by V13, both exited 1:

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replays/pre-r99-anchor/corpus/tools/support_check.py .ufo/waves/round-100/seats/T4-scratch/replays/pre-r99-anchor/corpus/fixtures/r95-crossing-aftermath
python3 corpus/tools/support_check.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-anchor/corpus/fixtures/r95-crossing-aftermath
```

Both complete stdout streams matched T4's saved streams byte-for-byte. The measured lines relevant to the mutation were identical (unchanged individual PASS rows omitted here):

```text
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; DISTINCT-ANCHORS 13/13
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
FAIL J14: source-support; mode=verbatim; anchor=not-found
RECEIPT JSON-FACTS 15; EDITORIAL-ROWS 2; TOTAL-ROWS 17
SOURCE-SUPPORT 14/15; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 17/17; VALIDATED-ROWS 16/17
FAIL: J14: source-support anchor missing
RESULT FAIL
exit=1
```

Historical freeze control, actual command and complete observed stdout:

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replays/pre-r99-anchor/corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/T4-scratch/replays/pre-r99-anchor/corpus/fixtures/r95-crossing-aftermath
```

```text
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
RESULT PASS
exit=0
```

Delivered freeze on the same excerpt-only mutant, actual command and complete observed stdout:

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replays/delivered-anchor/corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-anchor/corpus/fixtures/r95-crossing-aftermath
```

```text
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
FINDING DIGEST-MISMATCH: content digest b97a3b80df29110f6f369c7bd52ee09cd733e46f3f7d84420563c931744f7dca != pin 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710; changed: fictional-excerpts.md (sha256 0ef6734ae52d28656e75869d942d6b1e8e324b116977a2811b3b36dc0880b282 -> b0725e215a8c51bd0dda5b384396913a6d8ea36e58caa928d5b0315d47fc1aae); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
exit=2
```

The additional two row-10 control commands were also replayed exactly:

```sh
python3 corpus/fixtures/check_bible.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-anchor/corpus/fixtures/r95-crossing-aftermath
```

```text
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

```sh
python3 corpus/tools/map_obligations.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-anchor/corpus/fixtures/r95-crossing-aftermath
```

```text
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS
exit=0
```

Conclusion: the old JSON-only freeze missed this prose edit, but the pre-r99 support checker already rejected its missing mapped anchor. The addendum correctly bounds “invisible to every gate”; it does not claim that a lexical anchor proves prose meaning.

## Row 11 / AC-1 — PASS

Actual edge-plus-prose command and complete observed stdout:

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replays/delivered-precedence/corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-precedence/corpus/fixtures/r98-clerk-filing
```

```text
FREEZE r98-clerk-filing: events 7/7; dependency-edges 5/6; relations 1/1
FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']
RESULT FAIL
exit=1
```

Exactly one finding, `REDUCTION-DETECTED`; no `DIGEST-MISMATCH` despite the additional excerpt edit.

Actual inventory-clean prose-only control and complete observed stdout:

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replays/delivered-prose-control/corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-prose-control/corpus/fixtures/r98-clerk-filing
```

```text
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
FINDING DIGEST-MISMATCH: content digest c811669ea2534d48122939e270599376160b8f5936eecb2e766c141464b6808b != pin 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0; changed: fictional-excerpts.md (sha256 29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de -> dbcd5f11f4260f0e85c3271698afe1bac79ace52c31e9b651187371fb79e4b26); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
exit=2
```

Conclusion: modeled JSON inventory findings precede digest reporting on this valid invocation. “Any edit → exit 2” is not a universal rule, and “semantic inventory” is not natural-language entailment.

## Row 12 / AC-3 — PASS

Actual command on the delivered live tool:

```sh
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing --freeze corpus/fixtures/r98-clerk-filing
```

Complete observed stdout:

```text
FINDING INVALID-ARGUMENTS: pass either a fixture (verify) or --freeze DIR, not both
RESULT ERROR
exit=2
```

Exactly one finding, `INVALID-ARGUMENTS`, with no FREEZE/DIGEST receipt and no inventory or digest finding. The live contract hash before and after the nine-command batch was identical (below). This invalid combined invocation does not exercise the guarded write path.

## Exact-output comparison and stability — PASS

V13 executed each quoted argv via `subprocess.run(..., cwd=root, capture_output=True, text=True, env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})`, using a nine-worker `ThreadPoolExecutor`. Each result was checked against the corresponding command record in T4's already-delivered `replay-results.json`; the actual equality test was:

```python
exact=(shlex.join(argv)==saved['command'] and result.stdout==saved['stdout'] and result.stderr==saved['stderr'] and result.returncode==saved['exit'])
```

This checks complete streams, not only the excerpted lines above. All stderr streams were empty. Observed per-command marker: `EXACT-COMMAND-STDOUT-STDERR-EXIT-MATCH True` for each of A1–A6, B1–B2, and C1. Final actual summary:

```text
EXACT-REPLAY 9/9; failures=[]
```

The same independent batch hashed the delivered inputs before and after. Actual observed output:

```text
HASH corpus/knowledge/r99-gate-blind-spot-table.md: before=f1b3719a3954bbae44562f9e01b99434327ff50fba0c3a0755634dc9d76830ff after=f1b3719a3954bbae44562f9e01b99434327ff50fba0c3a0755634dc9d76830ff unchanged=True
HASH corpus/tools/dependency_freeze.py: before=fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c after=fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c unchanged=True
HASH corpus/tools/support_check.py: before=55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c after=55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c unchanged=True
HASH corpus/tools/dependency-freeze-contract.json: before=ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5 after=ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5 unchanged=True
```

## Bounds

The intentional non-zero exits above are the negative probes' expected outcomes, not unresolved test failures. No replay contradiction or source-table drift was observed. This seat does not certify prose entailment, source truth, chronology authentication, the separate C2 dossier, or round-wide admission. Verification was of the delivered three dated rows and their nine gate commands. There is no remaining seat blocker and no needed background task remains.

PASS — all three dated C3 addenda independently reproduce, exact commands/stdout/stderr/exits match 9/9, all 20,526 historical table bytes remain unchanged, and delivered table/tool/contract hashes stay stable.
