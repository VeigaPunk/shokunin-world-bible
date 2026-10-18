# V10 — C2 anti-overclaim (2026-10-17)

Axes: depth (review adds a bounded record, not a disposition), calibration (no testimony/chronology/semantic promotion), preservation (crossing-only relation and prior records). Baseline `fe1ce466e9d7427948c0abe4ecfbf961880b72ff`; observed live HEAD `b5fe472957ab1e4e9c90f5613acc14cd24a288ae` is the r100 declaration commit, not a replacement baseline. All commands ran from `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3` for Python execution.

This seat wrote only this report. No scratch was created, no other seat's scratch was changed, no agents were spawned, and no commit, push, network call, live fixture edit, or contract-writing freeze operation was performed. The invalid combined invocation below was checked against the delivered early rejection branch before execution and wrote no contract bytes.

## Producer wait and reviewed scope

Actual bounded polling command:

```sh
python3 -u - <<'PY'
from pathlib import Path
import time
root=Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
seats=root/'.ufo/waves/round-100/seats'
files=['corpus/fixtures/r100-docket-review/sources.json','corpus/fixtures/r100-docket-review/timeline.json','corpus/fixtures/r100-docket-review/fictional-excerpts.md','corpus/fixtures/r100-docket-review/README.md','corpus/fixtures/r100-docket-review/claim-excerpt-map.md','corpus/knowledge/r100-crossing-arc-synthesis.md','corpus/knowledge/r100-provenance-semantics-boundary.md']
for attempt in range(1,41):
    missing=[s for s in files if not (root/s).is_file() or (root/s).stat().st_size==0]
    reports={s:[p.name for p in seats.glob(s+'*.md') if p.is_file() and p.stat().st_size>0] for s in ('T2','T3','T4')}
    print(f'POLL {attempt}/40 {time.strftime("%Y-%m-%dT%H:%M:%S%z")} artifacts_missing={missing} producer_reports={reports}',flush=True)
    if not missing and all(reports.values()):
        print('READY: all requested artifacts and T2–T4 reports exist',flush=True)
        break
    if attempt<40: time.sleep(20)
else:
    print('ABSENT: bounded poll exhausted',flush=True)
PY
```

Observed initial absences resolved; final output, exit 0:

```text
POLL 25/40 2026-10-17T23:40:12-0300 artifacts_missing=[] producer_reports={'T2': ['T2-fixture-author.md'], 'T3': ['T3-fixture-docs.md'], 'T4': ['T4-knowledge-author.md']}
READY: all requested artifacts and T2–T4 reports exist
```

T2's landed owned payload was inspected after its report existed; T3's completed map/README and T4's completed knowledge records were inspected after their respective reports existed. All three full reports were read, as was `T1-chain-seven.md`. No producer plan was substituted for an artifact. No all-reports poll, self-inclusive wait, stall escape, or exhausted poll occurred; the background poll completed before this report.

The new/changed corpus-and-SKILL scope relative to `fe1ce46` was enumerated with `git diff --name-only fe1ce46 -- corpus SKILL.md` and `git ls-files --others --exclude-standard -- corpus SKILL.md` (via `python3`): exactly the ten files of `corpus/fixtures/r100-docket-review/`, the two r100 knowledge records, the r99 table addendum, `corpus/tools/{README.md,dependency-freeze-contract.json}`, and `SKILL.md` — 16 deliverable paths. All ten fixture files were covered by complete `Read` inspection of changed text and/or byte identity to the completely read r99 counterpart. Both new knowledge files, the entire added r99-table tail, the T1 README/SKILL additions, and every new contract field were read; tracked diffs confirmed append-only/owned-row boundaries. Round declaration/closure bookkeeping is not claimed as this seat's deliverable. Final report-only QA printed `DELIVERABLE PATH COUNT 16`; the initial draft's arithmetic count of 17 was corrected without changing any corpus bytes.

Citation convention below: bare fixture filenames resolve under `corpus/fixtures/r100-docket-review/`; bare r100 knowledge filenames resolve under `corpus/knowledge/`; “synthesis” names `corpus/knowledge/r100-crossing-arc-synthesis.md`. A bare `:NN` continues the named document in that same item.

## Adversarial closure/resolution readings

The strongest attempted readings fail against explicit delivered wording, not merely a green gate:

1. **Window closed / historical entry means case closed.** The positive close at `fictional-excerpts.md:70` names the crossing-window, not the matter. The inherited next lines retain a historical **open** entry and deny resolution (`:73-76`); the new note says “The entry remains open” (`:83`). The synthesis expressly separates window closure from matter closure (`corpus/knowledge/r100-crossing-arc-synthesis.md:37,48`). Treating the closed window as a disposed case requires changing the grammatical object and ignoring these clauses.
2. **Unfulfilled agreement establishes breach, blame, or a winner.** “The agreement was unfulfilled” is the clerk's inherited note statement, not a new adjudication. The new source reliability note explicitly refuses a breach finding or winner (`sources.json:54`); the review makes no finding and resolves nothing (`fictional-excerpts.md:85`). The synthesis preserves attribution and refuses duty expansion (`r100-crossing-arc-synthesis.md:54-56`). No new relation, accusation, breach finding, or positive blame assertion appears.
3. **A clerk's docket review is an institutional disposition.** The new note itself says “I make no finding and resolve nothing” and “Both accounts stand unresolved” (`fictional-excerpts.md:85-86`). `README.md:11` and `claim-excerpt-map.md:72` keep review distinct from a finding, renewed agreement, resolution, or reconciliation. Maren's office is not promoted to independently authenticated authority (`r100-crossing-arc-synthesis.md:36,54`).
4. **No new filings permits a default judgment / administrative closure.** No default-judgment rule or positive disposition is delivered. Reading one into the text conflicts with the adjacent open-entry and unresolved-account clauses. `README.md:11` distinguishes the review record from a new filing; the synthesis confines “No new filings” to the note rather than a global absence (`:38,54`). The newly authored review source is therefore not a claimed new lodged account or a resolved default.
5. **“Unresolved throughout” invents two accounts or an OPEN docket at r94/r95.** The dossier explicitly prevents that reading: r94 is the seed plus r95–r100 six continuation beats, seven snapshot records (`r100-crossing-arc-synthesis.md:8`); the first explicit two-account unresolved statement is r96 (`:34`); OPEN first appears at r98 (`:10,48`). Earlier non-adjudication is not retroactive docket creation.
6. **First-passage / tick 16 independently authenticates chronology or global first occurrence.** The excerpt attributes “After my lapse record” and “first-passage” to this note. The source reliability note, fixture README, map, and synthesis explicitly treat ticks and event IDs as editorial encodings, not authenticated chronology (`sources.json:54`; `README.md:13`; `claim-excerpt-map.md:72`; synthesis `:55`). No universal first-review claim was found.
7. **Preserved agreement or open entry renews continuing stewardship.** The unchanged relation is still `agreed_co_stewardship_for_this_crossing`, sourced to `crossing-minute`. The excerpt's “for this crossing only” is preserved at line 19; the new scope changes no term and creates no new duty (`fictional-excerpts.md:88`). Byte proof is below.
8. **Pin success establishes truth, canon, or dependency meaning.** The new boundary note explicitly separates byte identity and modeled JSON inventory from natural-language semantics (`r100-provenance-semantics-boundary.md:8,16-28`). The dossier's seven snapshots are expressly not the seven frozen fixtures (`synthesis:63`). T1's addendum and SKILL row retain these limits. No semantic promotion or silent r100 freeze claim was found.

The complete new quotation read at `corpus/fixtures/r100-docket-review/fictional-excerpts.md:82-86` is:

```text
> Tick 16: After my lapse record, I made the first-passage docket review at the Chalk Stair.
> The entry remains open.
> No new filings have been lodged.
> I make no finding and resolve nothing.
> Both accounts stand unresolved.
```

The event description (`timeline.json:95`), reliability note (`sources.json:54`), README (`:11`), J22 whole-proposition discussion (`claim-excerpt-map.md:72`), and synthesis (`:38,48,54-58`) agree with those bounds. The Grep sweep of closure/resolution/finding/chronology/canon/duty terms was a review aid; whole files and complete propositions were read. Negations were not counted as positive findings. The inherited “per that minute's terms” phrase at map line 70 remains descriptive framing, not a newly quoted minute clause; the synthesis expressly says the original minute does not contain the later lapse assertions (`:32`). This preserves r99 AC-6's distinction rather than silently strengthening the minute.

**No defensible closure/resolution reading of the delivered records was constructed.** A contrary reading requires dropping explicit negations/open-status clauses, importing an absent rule, changing an attributed report into a world fact, or confusing the window with the case.

## Byte preservation and relation-row proof

Actual command:

```sh
python3 - <<'PY'
from pathlib import Path
from hashlib import sha256
import json,subprocess
root=Path.cwd().resolve(); old=root/'corpus/fixtures/r99-window-lapse'; new=root/'corpus/fixtures/r100-docket-review'
print('ROOT',root)
for n in ('entities.json','relations.json','contradictions.json','inspiration-note.md','source-excerpt.md'):
    a=(old/n).read_bytes(); b=(new/n).read_bytes()
    print(f'{n} byte_identical_to_r99={a==b} bytes={len(b)} sha256={sha256(b).hexdigest()}')
for n in ('sources.json','timeline.json'):
    a=json.loads((old/n).read_text()); b=json.loads((new/n).read_text())
    print(f'{n} inherited_prefix_equal={a==b[:-1]} old_count={len(a)} new_count={len(b)} appended={json.dumps(b[-1],sort_keys=True)}')
a=(old/'fictional-excerpts.md').read_bytes(); b=(new/'fictional-excerpts.md').read_bytes()
print(f'fictional-excerpts.md old_byte_prefix={b.startswith(a)} old_bytes={len(a)} new_bytes={len(b)}')
print('relation',json.dumps(json.loads((new/'relations.json').read_text()),sort_keys=True))
PY
```

Observed exit 0; selected complete receipt lines:

```text
entities.json byte_identical_to_r99=True bytes=1793 sha256=db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984
relations.json byte_identical_to_r99=True bytes=139 sha256=c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9
contradictions.json byte_identical_to_r99=True bytes=3 sha256=37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
inspiration-note.md byte_identical_to_r99=True bytes=1956 sha256=58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37
source-excerpt.md byte_identical_to_r99=True bytes=640 sha256=b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd
fictional-excerpts.md old_byte_prefix=True old_bytes=5114 new_bytes=5961
relation [{"from": "aru", "source_id": "crossing-minute", "to": "evin", "type": "agreed_co_stewardship_for_this_crossing"}]
```

The two omitted long appended-row lines printed `inherited_prefix_equal=True old_count=8 new_count=9`, with exactly the delivered `clerk-review-note` source and `clerk-review-first-passage` event read above. The event's tick/actor/place/dependency/source are `16 / clerk-maren / chalk-stair / [clerk-lapse-recorded] / clerk-review-note`.

A separate actual `python3 -` comparison used `git show fe1ce46:corpus/fixtures/<r94-through-r99>/relations.json`: all six current relation files were baseline-equal, 139 bytes, with the same full SHA-256 above. Thus the whole r100 relation file, not merely its parsed endpoint triple, is byte-identical to r99 and to the crossing-only relation at r94–r99 baseline. No widened or renewed relation is hidden by formatting normalization.

The map-row comparison printed:

```text
MAP inherited_rows 21 new_rows 22
MAP inherited_rows_same_except_namespace True
MAP new_row (43, '| J22 | `timeline.json#/8` (`tick`, `entity_id`, `place_id`, `depends_on`, `description`, `source_id`) | `clerk-review-note` | `r100-docket-review:clerk-review-note` | `fictional-excerpts.md` | 78-88 | `verbatim` | `Tick 16: After my lapse record, I made the first-passage docket review at the Chalk Stair.` |')
CENSUS 174
COUNTS {'entities': 6, 'relations': 1, 'timeline': 9, 'sources': 9, 'contradictions': 0}
RAW_OBLIGATIONS 22
```

The actual comparison paired each `| J` row from `git show fe1ce46:corpus/fixtures/r99-window-lapse/claim-excerpt-map.md` with the new row, required identical line positions, and normalized only `r100-docket-review:` back to `r99-window-lapse:`. Raw map-row byte identity is **not** claimed across namespaces. A separate Git-tree directory count gave `BASELINE FIXTURE DIRECTORIES 173` and `CURRENT FIXTURE DIRECTORIES 174`.

## Real delivered-fixture gates and complete dossier replay

These exact commands were executed concurrently as real CLI subprocesses:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r100-docket-review
python3 corpus/tools/support_check.py corpus/fixtures/r100-docket-review
python3 corpus/tools/map_obligations.py corpus/fixtures/r100-docket-review
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r100-docket-review
```

Observed outputs (support per-anchor PASS lines omitted, not replaced with semantic judgments):

```text
# check_bible, exit=0
CLEAN: schema, citations, relations, timeline; 0 violations
# support_check, exit=0
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24; DISTINCT-ANCHORS 20/20
PASS J22: source-support; mode=verbatim; anchor=found; 82:> Tick 16: After my lapse record, I made the first-passage docket review at the Chalk Stair.
SOURCE-SUPPORT 22/22; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 24/24; VALIDATED-ROWS 24/24
RESULT PASS
# map_obligations, exit=0
OBLIGATIONS raw=22 mapped=22
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24
RESULT PASS
# dependency_freeze, exit=2 (expected coverage bound)
FINDING UNPINNED-FIXTURE: no pin for 'r100-docket-review' in corpus/tools/dependency-freeze-contract.json (pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing', 'r99-window-lapse'])
RESULT ERROR
```

The r100 unpinned result is retained as evidence, not relabeled green. It agrees with both new knowledge notes and T1's explicit scope; pinning r100 was not declared C1.

The synthesis's numerical/preservation statements were independently checked, rather than trusted from T4's report. Actual command:

```sh
python3 - <<'PY'
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json,subprocess
root=Path.cwd().resolve(); names=['r94-paired-crossing','r95-crossing-aftermath','r96-crossing-response','r97-crossing-acknowledgment','r98-clerk-filing','r99-window-lapse','r100-docket-review']
for i,n in enumerate(names):
    f=root/'corpus/fixtures'/n; load=lambda fn:json.loads((f/fn).read_bytes())
    e,r,t,s,c=[load(x+'.json') for x in ('entities','relations','timeline','sources','contradictions')]
    print('DOCKET',n,f'{len(e)}/{len(r)}/{len(t)}',f'sources={len(s)} obligations={len(e)+sum(len(x["claims"]) for x in e)+len(r)+len(t)} contradictions={c}')
    if i:
        old=root/'corpus/fixtures'/names[i-1]; checks=[]
        for fn in ('entities.json','timeline.json','sources.json'):
            a=json.loads((old/fn).read_bytes()); b=load(fn); checks.append(b[:len(a)]==a)
        checks.append((old/'relations.json').read_bytes()==(f/'relations.json').read_bytes())
        checks.append((f/'fictional-excerpts.md').read_bytes().startswith((old/'fictional-excerpts.md').read_bytes()))
        for fn in ('inspiration-note.md','source-excerpt.md'): checks.append((old/fn).read_bytes()==(f/fn).read_bytes())
        a=[x for x in (old/'claim-excerpt-map.md').read_text().splitlines() if x.startswith('| J')]; b=[x.replace(n+':',names[i-1]+':') for x in (f/'claim-excerpt-map.md').read_text().splitlines() if x.startswith('| J')]; checks.append(a==b[:len(a)])
        print('PRESERVATION',names[i-1]+' -> '+n,checks)
        assert all(checks)
    assert c==[]
cmds=[['python3',tool,'corpus/fixtures/'+n] for n in names for tool in ('corpus/fixtures/check_bible.py','corpus/tools/support_check.py','corpus/tools/map_obligations.py')]
def run(c):
    r=subprocess.run(c,text=True,capture_output=True)
    lines=[s for s in (r.stdout+r.stderr).splitlines() if s.startswith(('CLEAN:','OBLIGATIONS','SOURCE-SUPPORT','RESULT'))]
    return '$ '+' '.join(c)+'\n'+'\n'.join(lines)+'\nexit='+str(r.returncode),r.returncode
with ThreadPoolExecutor(max_workers=21) as pool: results=list(pool.map(run,cmds))
for out,_ in results: print(out)
print('ARC GATES',sum(code==0 for _,code in results),'/ 21 clean')
assert all(code==0 for _,code in results)
PY
```

Observed exit 0. Numerical receipt:

```text
DOCKET r94-paired-crossing 5/1/3 sources=3 obligations=14 contradictions=[]
DOCKET r95-crossing-aftermath 5/1/4 sources=4 obligations=15 contradictions=[]
DOCKET r96-crossing-response 5/1/5 sources=5 obligations=16 contradictions=[]
DOCKET r97-crossing-acknowledgment 5/1/6 sources=6 obligations=17 contradictions=[]
DOCKET r98-clerk-filing 6/1/7 sources=7 obligations=20 contradictions=[]
DOCKET r99-window-lapse 6/1/8 sources=8 obligations=21 contradictions=[]
DOCKET r100-docket-review 6/1/9 sources=9 obligations=22 contradictions=[]
ARC GATES 21 / 21 clean
```

Every adjacent step printed eight `True` preservation checks. Every checker printed CLEAN and exited 0; all seven support/map invocations printed RESULT PASS and exited 0, with the seven numerical source-support/map totals above. These establish structural/lexical/inventory properties only. The manual non-disposition review is a separate result.

## Calibration new-byte claims replayed without taking ownership

The three delivered T4 mirrors' freeze tools and contracts were compared byte-for-byte to the live delivered files: all six comparisons printed `True`. The actual mutant contents were independently checked: each excerpt equals its live original with only `depends on both ninth-bell entries` → `follows both ninth-bell entries`; the precedence mirror additionally drops only `evin-ninth-bell` from `paired-crossing-decision.depends_on`. These are producer-owned scratch inputs, used read-only; this seat did not run T4's writing harness.

The following exact child commands were replayed in a concurrent `python3` wrapper. Quoted output is selected observed stdout, not a predicted result:

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replays/pre-r99-anchor/corpus/tools/support_check.py .ufo/waves/round-100/seats/T4-scratch/replays/pre-r99-anchor/corpus/fixtures/r95-crossing-aftermath
python3 corpus/tools/support_check.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-anchor/corpus/fixtures/r95-crossing-aftermath
```

Both exit 1:

```text
FAIL J14: source-support; mode=verbatim; anchor=not-found
SOURCE-SUPPORT 14/15; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 17/17; VALIDATED-ROWS 16/17
FAIL: J14: source-support anchor missing
RESULT FAIL
```

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replays/pre-r99-anchor/corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/T4-scratch/replays/pre-r99-anchor/corpus/fixtures/r95-crossing-aftermath
```

Exit 0: `DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9`, `RESULT PASS`.

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replays/delivered-anchor/corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-anchor/corpus/fixtures/r95-crossing-aftermath
```

Exit 2: `FINDING DIGEST-MISMATCH` named `fictional-excerpts.md`, content digest `b97a3b80df29110f6f369c7bd52ee09cd733e46f3f7d84420563c931744f7dca`, followed by `RESULT ERROR`. This confirms row 10's distinction: historically invisible to freeze does not mean invisible to every gate.

```sh
python3 corpus/fixtures/check_bible.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-anchor/corpus/fixtures/r95-crossing-aftermath
python3 corpus/tools/map_obligations.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-anchor/corpus/fixtures/r95-crossing-aftermath
```

Both exit 0: respectively `CLEAN: schema, citations, relations, timeline; 0 violations` and `OBLIGATIONS raw=15 mapped=15` / `RESULT PASS`.

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replays/delivered-precedence/corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-precedence/corpus/fixtures/r98-clerk-filing
```

Complete stdout, exit 1:

```text
FREEZE r98-clerk-filing: events 7/7; dependency-edges 5/6; relations 1/1
FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']
RESULT FAIL
```

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replays/delivered-prose-control/corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-prose-control/corpus/fixtures/r98-clerk-filing
```

Exit 2: inventory `7/7; dependency-edges 6/6; relations 1/1`, `FINDING DIGEST-MISMATCH` naming `fictional-excerpts.md`, content digest `c811669ea2534d48122939e270599376160b8f5936eecb2e766c141464b6808b`, `RESULT ERROR`. Together these confirm row 11's conditional exit rule; the edge-plus-prose probe emitted no DIGEST-MISMATCH.

```sh
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing --freeze corpus/fixtures/r98-clerk-filing
```

Complete stdout, exit 2:

```text
FINDING INVALID-ARGUMENTS: pass either a fixture (verify) or --freeze DIR, not both
RESULT ERROR
```

The delivered `dependency_freeze.py:643-644` rejects that combination before the freeze branch at `:647-648`. The wrapper's final observed lines were:

```text
CONTRACT BEFORE ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5
CONTRACT AFTER ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5
REPLAY expected_exits_match True contract_unchanged True
```

All nine replay outcomes matched their expected exits. The non-zero negatives are evidence, not hidden failures. The table's 20,526 historical bytes remain an exact prefix; the dated addition is 8,907 bytes and contains the three rows 10–12. `r100-provenance-semantics-boundary.md` correctly names “semantic inventory” as JSON modeling rather than prose understanding. No new checker behavior or semantics proof is claimed.

## Coverage cross-check and byte snapshot

An actual `ThreadPoolExecutor(max_workers=7)` wrapper invoked `python3 corpus/tools/dependency_freeze.py corpus/fixtures/<name>` for each of `r88-m3-maya-cluster`, `r94-paired-crossing`, `r95-crossing-aftermath`, `r96-crossing-response`, `r97-crossing-acknowledgment`, `r98-clerk-filing`, and `r99-window-lapse`. Observed `CHAIN 7 / 7 clean`, all RESULT PASS / exit 0. The r99 receipt was:

```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
DIGEST 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e
RESULT PASS
```

Parsed comparison to `git show fe1ce46:corpus/tools/dependency-freeze-contract.json` printed:

```text
PIN ADDITIONS ['r99-window-lapse']
EXISTING PINS UNCHANGED True
TOP LEVEL CHANGED ['revision']
R100 PINNED False
```

Thus the T1 docs' coverage claim agrees with the delivered contract. The top-level revision metadata refresh is disclosed, not mislabeled as a literally addition-only contract diff. The r88 symbolism map remains outside the ten declared files. This seat did not rerun any valid `--freeze` operation and does not independently certify the producer's authoring mechanism from a diff alone.

Final SHA-256 snapshot (modified/new textual payloads rechecked against their previously read bytes; the five copied files were independently byte-compared above):

```text
corpus/fixtures/r100-docket-review/README.md a312a364d4d9476e98c0fae3f62b23bf72e73a06c508aac04ffe48cf9cf4c5fa
corpus/fixtures/r100-docket-review/claim-excerpt-map.md 16981162f8476a8fcc1bd892ac0b1b9e6cb916e1d45e6f2ea392a5eeca769244
corpus/fixtures/r100-docket-review/fictional-excerpts.md d01825a7e3c8f4af549b7acdde7eb8e1b9074a6eccb8ce6d12401cea19745705
corpus/fixtures/r100-docket-review/sources.json effa5160eb7a6b228d52a972bf52beeffc1544d3cb1f6c5edb2850f88bd2d22e
corpus/fixtures/r100-docket-review/timeline.json 008a1ff8dbef63e552e271f1be8eb536b1361c5a0fe83f008423b06d505ab7f8
corpus/knowledge/r100-crossing-arc-synthesis.md 6fcffc8154a11419adbcaefba6d728ee544af831cb5e1b999429404c3b243acc
corpus/knowledge/r100-provenance-semantics-boundary.md 29cc7d856b2600bbb03dec577487bc0f09525ab444a3e3109ef0040ab7edeb36
corpus/knowledge/r99-gate-blind-spot-table.md f1b3719a3954bbae44562f9e01b99434327ff50fba0c3a0755634dc9d76830ff
corpus/tools/dependency-freeze-contract.json ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5
SKILL.md 09b2949ae26ec5e257fce0e879749d8abccaf75c888151159ef857597f418ac6
corpus/tools/README.md c99217cd0663125214cee7007951a1b9ae98f466f7081344c03ad0f45f87f399
```

Delivered tool hashes were independently measured: checker `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`, support `55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c`, map `86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9`, freeze `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c`. No self-test was run by this read-only seat because those tools create temporary files; producer self-test receipts are not mislabeled as V10 executions.

Before the sole report Write, a lane-root `python3 -` assertion checked the resolved root, exact absolute report path and resolved parent, nonexistence, and absence of a report symlink. It printed `VERIFIED REPORT WRITE PATH /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V10-c2-anti-overclaim.md`. An initial pre-production `ls` had exited 2 because the seats directory did not yet exist; that was an observed setup absence, resolved by the bounded producer wait, not a delivered-fixture failure.

## Verdict and limits

Depth: C2's two components survive this anti-overclaim review — one review source/event, preserved records, all seven dossier snapshots, and no disposition or truth promotion. Calibration: the new boundary prose and dated corrections remain bounded and replay-consistent. Preservation: the whole relation file is byte-identical, as are the five preserved r99 files; all six arc transitions preserve the measured prefixes and mapped claims modulo explicit namespace qualification. No harm on these checked axes was found.

This is a non-author current-byte review, not proof that the fictional testimony is true, that chronology is authenticated, that no future continuation will resolve the matter, or that all possible semantic readings have been mechanically ruled out. Rights and AI-training permission remain unassessed. The r100 tick-16 edge remains unpinned by declared scope. Global admission and unrelated verifier findings remain the parent's responsibility. No unresolved V10 blocker or needed background task remains.

PASS — no supported closure/resolution reading found in the delivered new bytes; the crossing-only relation is byte-identical, the dossier preserves non-adjudication bounds, 21/21 arc gates and 7/7 chain checks pass, and all nine correction replays match their bounded outcomes.
