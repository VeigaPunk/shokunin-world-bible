# V11 — C2 synthesis audit (2026-10-17)

Axes: per-record byte fidelity; unresolved-state continuity; explicit non-establishment bounds; cited-path integrity. This is an independent leaf-seat audit of C2's dossier, not the round-wide admission verdict.

Audited `/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/knowledge/r100-crossing-arc-synthesis.md`, final SHA-256 `6fcffc8154a11419adbcaefba6d728ee544af831cb5e1b999429404c3b243acc`, matching T4's completed producer report. The final dossier is 111 lines; the final replay includes its appended delivered-revision receipts, not merely its earlier 65-line draft.

## Producer wait and revision

Actual command, run from `/home/vgpnk/Projects/shokunin/lore-shokunin`:

```sh
python3 - <<'PY'
from pathlib import Path
import time
root = Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
artifact = root / 'corpus/knowledge/r100-crossing-arc-synthesis.md'
seats = root / '.ufo/waves/round-100/seats'
for attempt in range(1, 41):
    reports = sorted(p for p in seats.iterdir() if p.is_file() and p.name.startswith('T4')) if seats.is_dir() else []
    print(f'POLL {attempt}/40 artifact={artifact.is_file()} T4_reports={[str(p.relative_to(root)) for p in reports]}', flush=True)
    if artifact.is_file() and reports:
        print('READY: artifact and producer report exist', flush=True)
        break
    if attempt < 40:
        time.sleep(20)
else:
    print('ABSENT: artifact and T4 report were not both present within the bounded poll', flush=True)
PY
```

Observed selected stdout, exit 0 after 500 seconds:

```text
POLL 1/40 artifact=False T4_reports=[]
POLL 17/40 artifact=False T4_reports=[]
POLL 18/40 artifact=True T4_reports=[]
POLL 25/40 artifact=True T4_reports=[]
POLL 26/40 artifact=True T4_reports=['.ufo/waves/round-100/seats/T4-knowledge-author.md']
READY: artifact and producer report exist
```

Read the actual completed T4 report, plus T2's `T2-fixture-author.md` and T3's `T3-fixture-docs.md`, before final verification. Initial missing artifact/seats-directory observations were delivery absences, not fixture verdicts. No producer plan was accepted as delivered evidence. No all-reports poll, self-inclusive wait, stall escape, or poll timeout was used; the background poll completed before this handoff.

Actual `git log -3 --oneline` output:

```text
b5fe472 lore r100: declare sol-max 32-seat round before dispatch
ae67105 lore r99: close round — SCORECARD admitted section
fe1ce46 lore r99: freeze admitted wave + closure docs (ten-file pins, lapse beat, blind-spot table, receipt 128/128)
```

The live HEAD is therefore `b5fe472957ab1e4e9c90f5613acc14cd24a288ae`, not an assumed `fe1ce46`; the declared r99 closure remains the inheritance baseline. Actual command:

```sh
git diff --name-only fe1ce46 -- corpus/fixtures/r94-paired-crossing corpus/fixtures/r95-crossing-aftermath corpus/fixtures/r96-crossing-response corpus/fixtures/r97-crossing-acknowledgment corpus/fixtures/r98-clerk-filing corpus/fixtures/r99-window-lapse
```

Observed no output, exit 0: those six existing fixtures remain unchanged from the declared baseline.

## Reproducible independent audit

Created only this report and the declared exclusive scratch file:

`/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V11-scratch/audit_synthesis.py`.

The scratch script performs read-only fixture/dossier/pin checks, prints the exact child commands and selected real stdout, and dispatches the independent CLI calls concurrently. It does not run another producer's script, mutate fixtures, freeze anything, or write bytecode. An initial syntax check printed `AUDIT SCRIPT SYNTAX PASS`, exit 0. After extending the citation scan to cover the final dossier's LOG, absolute-root, and scratch-receipt references, the complete final command was:

```sh
python3 -B .ufo/waves/round-100/seats/V11-scratch/audit_synthesis.py
```

Observed exit 0. The following sections quote its actual output and distinguish mechanical checks from manual prose review.

## Per-record fidelity: seven of seven match

The dossier explicitly resolves the declaration's seven-name/six-beat ambiguity: r94 is the seed, r95–r100 are six continuation beats (`r100-crossing-arc-synthesis.md:8`). The prior r98 and r99 notes' line-14 numbering agrees. No snapshot is dropped to force a count of six.

Actual output:

```text
ROW r94-paired-crossing E/R/T=5/1/3 sources=3 obligations=14/14 event=paired-crossing-decision pointer=timeline.json#/2 tick=10 source=crossing-minute source_pointer=sources.json#/2 contradictions=0
ROW r95-crossing-aftermath E/R/T=5/1/4 sources=4 obligations=15/15 event=aftermath-missing-evin pointer=timeline.json#/3 tick=11 source=aru-aftermath-note source_pointer=sources.json#/3 contradictions=0
ROW r96-crossing-response E/R/T=5/1/5 sources=5 obligations=16/16 event=response-evin-salt-court pointer=timeline.json#/4 tick=12 source=evin-response-note source_pointer=sources.json#/4 contradictions=0
ROW r97-crossing-acknowledgment E/R/T=5/1/6 sources=6 obligations=17/17 event=acknowledgment-aru-records pointer=timeline.json#/5 tick=13 source=aru-acknowledgment-note source_pointer=sources.json#/5 contradictions=0
ROW r98-clerk-filing E/R/T=6/1/7 sources=7 obligations=20/20 event=clerk-filing-open pointer=timeline.json#/6 tick=14 source=clerk-filing-note source_pointer=sources.json#/6 contradictions=0
ROW r99-window-lapse E/R/T=6/1/8 sources=8 obligations=21/21 event=clerk-lapse-recorded pointer=timeline.json#/7 tick=15 source=clerk-lapse-note source_pointer=sources.json#/7 contradictions=0
ROW r100-docket-review E/R/T=6/1/9 sources=9 obligations=22/22 event=clerk-review-first-passage pointer=timeline.json#/8 tick=16 source=clerk-review-note source_pointer=sources.json#/8 contradictions=0
```

These are comparisons against the dossier table, not hardcoded repetitions of it: raw table counts, entity first-appearance/claim obligations, relation/event obligations, map rows, event IDs/ticks, source IDs, and both contextual JSON pointers are independently resolved. The r98 jump is correctly three obligations (new entity first appearance + claim + filing event), while the other continuations add one event obligation. The r100 review's actor/place/dependency/source tuple matches `clerk-maren`, `chalk-stair`, `['clerk-lapse-recorded']`, `clerk-review-note`.

Actual preservation output:

```text
PRESERVATION r94-paired-crossing->r95-crossing-aftermath JSON=PASS excerpt-prefix=PASS external-bytes=PASS map=14/14 namespace-only edge=PASS
PRESERVATION r95-crossing-aftermath->r96-crossing-response JSON=PASS excerpt-prefix=PASS external-bytes=PASS map=15/15 namespace-only edge=PASS
PRESERVATION r96-crossing-response->r97-crossing-acknowledgment JSON=PASS excerpt-prefix=PASS external-bytes=PASS map=16/16 namespace-only edge=PASS
PRESERVATION r97-crossing-acknowledgment->r98-clerk-filing JSON=PASS excerpt-prefix=PASS external-bytes=PASS map=17/17 namespace-only edge=PASS
PRESERVATION r98-clerk-filing->r99-window-lapse JSON=PASS excerpt-prefix=PASS external-bytes=PASS map=20/20 namespace-only edge=PASS
PRESERVATION r99-window-lapse->r100-docket-review JSON=PASS excerpt-prefix=PASS external-bytes=PASS map=21/21 namespace-only edge=PASS
R99-R100 five byte-identical files; excerpt_bytes=5114->5961
```

The five byte-identical r99→r100 files are `contradictions.json`, `entities.json`, `relations.json`, `inspiration-note.md`, and `source-excerpt.md`. Inherited entity/timeline/source prefixes and complete relations are parsed-value equal. Earlier excerpt bytes are exact prefixes, and external/inspiration bytes are equal on every adjacent step. Map JSON rows retain all cells except the fixture-qualified namespace; editorial rows are unchanged. The clerk's first appearance remains `clerk-filing-note`, and the relation remains the crossing-only agreement sourced to `crossing-minute`.

## Unresolved invariant: manual review, not a gate inference

Read the whole final dossier and delivered sections, including the full r100 excerpt and map. The script's observed source-text output includes these exact clauses:

- Beat 1, `r95-crossing-aftermath/fictional-excerpts.md:26-29`: `Tick 11: I waited at the Chalk Stair through the agreed bell.` / `Evin did not come.` / `The agreement we chalked covered this crossing only.` / `I assert no other duty, no breach, and no obligation beyond this crossing.` This is an attributed first report, not a breach verdict.
- Beat 2, `r96-crossing-response/fictional-excerpts.md:38-40`: `I make no accusation against Aru.` / `I select no winner between our two accounts.` / `Both accounts stand unresolved.`
- Beat 3, `r97-crossing-acknowledgment/fictional-excerpts.md:49-51`: `I hold to my own account; both accounts stand unresolved.` / `I make no accusation against Evin, and I select no winner between us.` / `I assert no reconciliation, no new duty, and no obligation beyond this crossing.` Receipt is not agreement or retraction.
- Beat 4, `r98-clerk-filing/fictional-excerpts.md:60-62`: `I am Maren, clerk of the Chalk Stair registry, and I record the matter OPEN.` / `I assert no finding.` / `I reach no verdict and reconcile nothing.`
- Beat 5, `r99-window-lapse/fictional-excerpts.md:70-74`: `Tick 15: The crossing-window named in the original minute has closed.` / `The agreement was unfulfilled.` / `No claim was lodged.` / `The matter stands as a historical open entry.` / `I record no resolution, assign no blame, and reconcile nothing.` The negations are not inverted, and window closure is not entry closure.
- Beat 6, `r100-docket-review/fictional-excerpts.md:82-86`: `Tick 16: After my lapse record, I made the first-passage docket review at the Chalk Stair.` / `The entry remains open.` / `No new filings have been lodged.` / `I make no finding and resolve nothing.` / `Both accounts stand unresolved.`

The dossier's temporal qualification at lines 10 and 48 is necessary and correct: r94 establishes the agreement, r95 introduces one account, the explicit two-account unresolved statement begins at r96, and OPEN is first recorded at r98. The invariant is non-adjudication across all six continuations, not an invented earlier two-account docket. Every snapshot's contradiction array is empty, but the dossier explicitly declines to treat that as proof of universal logical compatibility. No per-beat summary upgrades reported absence, institutional filing, lapse, or review into a truth finding.

The final r100 map's J22, line 43, uses `timeline.json#/8`, source `clerk-review-note`, span 78–88, and the exact line-82 anchor. Its line-72 whole-proposition explanation correctly points to the other four quoted lines; the dossier does not pretend that matching the first sentence proves those clauses.

## Bounds, cited paths, and final receipts

Actual audit output:

```text
CITED PATHS 77/77 exist; files=69 directories=8; explicit ranges=16/16 in bounds; contextual JSON pointers=14/14 resolve
BOUND PRESENT No testimony truth.
BOUND PRESENT No chronology authentication.
BOUND PRESENT No expansion of duty.
BOUND PRESENT No automatic source identity.
BOUND PRESENT No semantic or canon certification by gates.
BOUND PRESENT Rights and AI-training permission unassessed.
NUMBERING seed r94 + six continuations r95-r100 explicitly distinguished
PIN SET r88-m3-maya-cluster, r94-paired-crossing, r95-crossing-aftermath, r96-crossing-response, r97-crossing-acknowledgment, r98-clerk-filing, r99-window-lapse; r100 unpinned as dossier states
CENSUS 174
```

The path check expands every brace-list source citation and includes final tool citations, `LOG.md:3343-3344`, the absolute lane root, and all three cited T4 scratch artifacts (script/output/JSON). All 16 fully specified numeric ranges are within the delivered files; contextual source/event pointers resolve inside the correct fixture. Generic `file.json#/pointer` is explanatory notation, not a fictitious file citation. The context-only map-line-72 citation was also checked manually against the delivered map.

Manual inspection of dossier lines 54–59 confirms that these are substantive bounds, not merely headings: no testimony or institutional-authority authentication; ticks, IDs, and edges are editorial normalizations rather than literal JSON quotations or authenticated dates; no continuing duty, blame, or adjudication; no bare-ID identity inference; no semantic/rights/permission/canon certification. The Spence references remain external editorial comparison, not an in-world witness or authenticated K'iche text. No URL was fetched.

The dossier also distinguishes seven arc snapshots (r94–r100) from the different seven freeze pins (r88 plus r94–r99). The new tick-16 edge is explicitly unpinned, not silently credited to C1.

The final audit's 21 real child calls are checker/map/support × the seven fixture paths printed above. Every checker prints `CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0; each map/support prints `RESULT PASS`, exit 0. The map counts are 14/14, 15/15, 16/16, 17/17, 20/20, 21/21, 22/22; lexical source-support counts match those seven values. These are independently replayed live outcomes, not T4's claimed receipts alone.

The exact new-scenario child commands were:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r100-docket-review
python3 corpus/tools/map_obligations.py corpus/fixtures/r100-docket-review
python3 corpus/tools/support_check.py corpus/fixtures/r100-docket-review
```

Observed selected stdout, all three exits 0:

```text
CLEAN: schema, citations, relations, timeline; 0 violations
OBLIGATIONS raw=22 mapped=22
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24
RESULT PASS
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24; DISTINCT-ANCHORS 20/20
SOURCE-SUPPORT 22/22; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 24/24; VALIDATED-ROWS 24/24
RESULT PASS
```

The final script additionally reproduced all three full tool hashes quoted in the dossier. Its closing output was:

```text
STABILITY 70/70 cited/document/tool files unchanged across gate replay
RESULT PASS: byte/count/pointer/path checks and 21 live gate calls; prose conclusions require the manual review recorded in V11 report
```

## Ownership, initial errors, and scope

Absolute resolution was checked before each new-file Write. The report-path verification command printed:

```text
REPORT PATH VERIFIED /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V11-c2-synthesis.md
```

No production file, shared report, or other seat's scratch was edited. No nested agents, commits, pushes, network calls, or contract writes. The only V11 files are this report and the one declared scratch script. Initial `Read` of the lane's `AGENTS.md` returned `does not exist`; the recursive lane glob found no `AGENTS.md`. Initial `pwd && ls .ufo/waves/round-100/seats` printed the correct lane root followed by `ls: cannot access '.ufo/waves/round-100/seats': No such file or directory`, exit 2; the later poll resolved that delivery absence. There were no failed audit assertions or live gate runs.

The first independent pass scanned corpus citations; the final pass deliberately extended that scan to the final dossier's appended LOG/scratch citations and added complete inherited-map comparisons, census, and tool-hash checks. Its successful final figures above supersede the narrower preliminary counts. No unresolved V11 blocker remains. C3 mutation replays, guarded-freeze authorship, and round-wide all-axis admission remain outside this seat's verdict; gate success is not semantic proof.

PASS — the delivered dossier's seven records/six continuation beats match fixture bytes, counts, events, sources, obligations, and preserved maps; unresolved non-adjudication holds throughout, explicit non-establishment bounds are present, all cited paths resolve, and all 21 live gate calls pass.
