# V08 — C2 anchor verification (2026-10-17)

Seat scope: C2 component 1, all 22 source-attributed JSON anchors in `corpus/fixtures/r100-docket-review/`, preservation of inherited line numbers, and confinement of the sole new anchor to the appended review section. This is not a round-wide admission judgment.

Axes: depth (complete 22-row lexical coverage), calibration (independent implementation plus negative controls), preservation (r99 excerpt bytes, inherited row fields and line positions), and operability (actual delivered-revision gate replays).

## Delivery and independence

Waited for the actual fixture files **and** `.ufo/waves/round-100/seats/T3-fixture-docs.md`; readiness occurred at poll 16. Then read T3's complete report and the complete delivered README, map, and fictional excerpts before reporting. No producer plan was treated as delivery.

The independent implementation is:

`/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/scratch/V08-c2-anchors/independent_anchors.py`

It uses Python's standard library only; it does not import, call, or reuse `support_check.py` or `map_obligations.py`. It independently splits Markdown rows, parses inclusive numeric spans, enumerates every fixed-substring hit in each delivered excerpt, rejects absent/out-of-span occurrences, checks baseline bytes with read-only `git show fe1ce46:...`, and compares inherited cells except the intentional path-qualified namespace change. It also determines the review section from its heading and checks that J22's span and every occurrence are wholly inside it. Four in-memory negative controls exercise rejection; no fixture mutation was made.

Only this exclusive report and the one declared scratch script were created by V08. No corpus/document/contract bytes were edited, no nested agents, commits, pushes, or network requests were made. Every command used the lane cwd `/home/vgpnk/Projects/shokunin/lore-shokunin`.

## Independent replay: 22/22 anchors, inherited lines, review-only addition

Actual command, exit 0:

```sh
python3 .ufo/waves/round-100/scratch/V08-c2-anchors/independent_anchors.py
```

Observed complete stdout:

```text
PRODUCER-REPORTS .ufo/waves/round-100/seats/T3-fixture-docs.md
ROW-INVENTORY JSON=22 EDITORIAL=2 TOTAL=24
ANCHOR J01 fictional-excerpts.md:12-12 hits=[12] IN-SPAN
ANCHOR J02 fictional-excerpts.md:13-13 hits=[13] IN-SPAN
ANCHOR J03 fictional-excerpts.md:12-12 hits=[12] IN-SPAN
ANCHOR J04 fictional-excerpts.md:13-13 hits=[13] IN-SPAN
ANCHOR J05 fictional-excerpts.md:17-17 hits=[17] IN-SPAN
ANCHOR J06 fictional-excerpts.md:12-12 hits=[12] IN-SPAN
ANCHOR J07 fictional-excerpts.md:13-13 hits=[13] IN-SPAN
ANCHOR J08 fictional-excerpts.md:12-12 hits=[12] IN-SPAN
ANCHOR J09 fictional-excerpts.md:13-13 hits=[13] IN-SPAN
ANCHOR J10 fictional-excerpts.md:18-18 hits=[18] IN-SPAN
ANCHOR J11 fictional-excerpts.md:19-19 hits=[19] IN-SPAN
ANCHOR J12 fictional-excerpts.md:12-12 hits=[12] IN-SPAN
ANCHOR J13 fictional-excerpts.md:13-13 hits=[13] IN-SPAN
ANCHOR J14 fictional-excerpts.md:18-20 hits=[20] IN-SPAN
ANCHOR J15 fictional-excerpts.md:22-31 hits=[26] IN-SPAN
ANCHOR J16 fictional-excerpts.md:33-42 hits=[37] IN-SPAN
ANCHOR J17 fictional-excerpts.md:44-53 hits=[48] IN-SPAN
ANCHOR J18 fictional-excerpts.md:60-60 hits=[60] IN-SPAN
ANCHOR J19 fictional-excerpts.md:59-60 hits=[59] IN-SPAN
ANCHOR J20 fictional-excerpts.md:55-64 hits=[59] IN-SPAN
ANCHOR J21 fictional-excerpts.md:66-76 hits=[70] IN-SPAN
ANCHOR J22 fictional-excerpts.md:78-88 hits=[82] IN-SPAN
ANCHOR S01 source-excerpt.md:5-5 hits=[5] IN-SPAN
ANCHOR S02 source-excerpt.md:5-5 hits=[5] IN-SPAN
ANCHORS JSON=22/22 EDITORIAL=2/2 ALL=24/24
DISTINCT-ANCHOR-PAIRS 20
PRESERVATION r99=fe1ce46; excerpt-prefix-lines=1-76 byte-identical; J01-J21 fields/spans/anchors identical except namespace; S01-S02 identical
NEW-ANCHOR J22 pointer=timeline.json#/8 source=clerk-review-note span=78-88 review-section=78-88 hits=[82] inherited-hits=0
CONTROL PASS new anchor with span 1-1 rejected as out-of-span
CONTROL PASS missing anchor rejected as anchor-absent
CONTROL PASS duplicated new anchor after EOF rejected as out-of-span
CONTROL PASS prepended line rejected by inherited-byte-prefix predicate
DELIVERED-SHA256 README.md a312a364d4d9476e98c0fae3f62b23bf72e73a06c508aac04ffe48cf9cf4c5fa
DELIVERED-SHA256 claim-excerpt-map.md 16981162f8476a8fcc1bd892ac0b1b9e6cb916e1d45e6f2ea392a5eeca769244
DELIVERED-SHA256 fictional-excerpts.md d01825a7e3c8f4af549b7acdde7eb8e1b9074a6eccb8ce6d12401cea19745705
DELIVERED-SHA256 source-excerpt.md b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd
RESULT PASS: 22/22 JSON anchors in span, inherited line numbers stable, only J22 new and wholly in review section
```

The 22 JSON rows are **not** 22 distinct anchors: co-mapping is retained; the declared/observed 20 distinct anchor pairs include the two editorial rows. No missing anchor, invalid span, or out-of-span hit occurred.

The J22 row is at `corpus/fixtures/r100-docket-review/claim-excerpt-map.md:43`; its review-only explanation is at map line 72. The exact new anchor is at `corpus/fixtures/r100-docket-review/fictional-excerpts.md:82`:

> Tick 16: After my lapse record, I made the first-passage docket review at the Chalk Stair.

The section begins at line 78 and ends at line 88. The inherited prefix ends at line 76; J22 has zero hits in that prefix. The following authored quote lines explicitly leave the entry open (83), report no new filings (84), make no finding and resolve nothing (85), and retain unresolved accounts (86). This is a description of the delivered wording, not an independently authenticated history or semantic verdict.

## Additional independent map-position and byte-prefix replay

Actual command, exit 0:

```sh
python3 - <<'PY'
from pathlib import Path
import subprocess,hashlib
r=Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
old_map=subprocess.check_output(['git','show','fe1ce46:corpus/fixtures/r99-window-lapse/claim-excerpt-map.md'],cwd=r).decode()
new=r/'corpus/fixtures/r100-docket-review'
old=[(i,line) for i,line in enumerate(old_map.splitlines(),1) if line.startswith('| J')]
current=[(i,line) for i,line in enumerate((new/'claim-excerpt-map.md').read_text().splitlines(),1) if line.startswith('| J')]
assert len(old)==21 and len(current)==22
for (before_i,before),(after_i,after) in zip(old,current):
    assert before_i==after_i
    assert before==after.replace('r100-docket-review:','r99-window-lapse:')
print('MAP-POSITIONS PASS J01-J21 remain at lines 22-42; J22 appended at line',current[-1][0])
prefix=subprocess.check_output(['git','show','fe1ce46:corpus/fixtures/r99-window-lapse/fictional-excerpts.md'],cwd=r)
assert (new/'fictional-excerpts.md').read_bytes().startswith(prefix)
print('EXCERPT-PREFIX PASS',len(prefix),'bytes /',len(prefix.splitlines()),'lines exactly preserved')
scratch=r/'.ufo/waves/round-100/scratch/V08-c2-anchors/independent_anchors.py'
print('HELPER-SHA256',hashlib.sha256(scratch.read_bytes()).hexdigest())
print('SCRATCH-FILES',[str(p.relative_to(r)) for p in sorted(scratch.parent.iterdir())])
PY
```

Observed complete stdout:

```text
MAP-POSITIONS PASS J01-J21 remain at lines 22-42; J22 appended at line 43
EXCERPT-PREFIX PASS 5114 bytes / 76 lines exactly preserved
HELPER-SHA256 9d9838481c44ad3e7af2e546a1814ac4f3371cc95f1c16f7a376a9819786c337
SCRATCH-FILES ['.ufo/waves/round-100/scratch/V08-c2-anchors/independent_anchors.py']
```

Qualification: inherited raw Markdown rows are not byte-identical because `r99-window-lapse:...` becomes `r100-docket-review:...`. Independent comparison confirms this is the **only** J01–J21 row change; inherited pointer/field lists, local source IDs, excerpt paths, spans, modes, anchor strings, map-row positions, and actual excerpt line numbers are preserved. The inherited excerpt itself is byte-identical across its complete 5,114-byte prefix.

## Delivered-revision standard gate replays

Issued concurrently after T3 delivery; every command exited 0. These are separate corroborating receipts, not the implementation of the independent check above.

Actual command:

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r100-docket-review
```

Selected observed stdout lines (all J01–J22 and S01–S02 lines were PASS):

```text
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24; DISTINCT-ANCHORS 20/20
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS J22: source-support; mode=verbatim; anchor=found; 82:> Tick 16: After my lapse record, I made the first-passage docket review at the Chalk Stair.
RECEIPT JSON-FACTS 22; EDITORIAL-ROWS 2; TOTAL-ROWS 24
SOURCE-SUPPORT 22/22; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 24/24; VALIDATED-ROWS 24/24
RESULT PASS
```

Actual command:

```sh
python3 corpus/tools/map_obligations.py corpus/fixtures/r100-docket-review
```

Observed complete stdout:

```text
OBLIGATIONS raw=22 mapped=22
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24
RESULT PASS
```

Actual command:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r100-docket-review
```

Observed complete stdout:

```text
CLEAN: schema, citations, relations, timeline; 0 violations
```

Before T3 delivery, baseline-only checks also succeeded: the independent parser found 21 JSON + 2 editorial anchors in span in r99, and `python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse` exited 0 with `SOURCE-SUPPORT 21/21`, `VALIDATED-ROWS 23/23`, `RESULT PASS`. The independent delivered replay rechecks r99 map/excerpt/external-excerpt equality against the declared baseline `fe1ce46`, rather than trusting mutable working-tree inheritance alone.

## Poll protocol and initial absence

Initial `pwd` returned `/home/vgpnk/Projects/shokunin/lore-shokunin`. The initial actual command `ls .ufo/waves/round-100/seats` exited 2 with:

```text
ls: cannot access '.ufo/waves/round-100/seats': No such file or directory
```

This was transient pre-delivery absence, not a fixture validation failure. The recursive lane `AGENTS.md` glob found no matches. Polls 1–5 and 6–10 ran as five-iteration Python batches with 20-second sleeps between unsuccessful tries. At poll 1, README/map/fictional excerpts and T3 report were all absent. The three artifacts existed from poll 2 onward, but no new-artifact verification was performed before T3's report arrived.

The final actual bounded poll command was:

```sh
python3 - <<'PY'
from pathlib import Path
import time,json
r=Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
for i in range(11,41):
    time.sleep(20)
    seats=r/'.ufo/waves/round-100/seats'
    artifacts=[r/'corpus/fixtures/r100-docket-review/README.md',r/'corpus/fixtures/r100-docket-review/claim-excerpt-map.md',r/'corpus/fixtures/r100-docket-review/fictional-excerpts.md']
    reports=sorted(p for p in seats.glob('T3*') if p.is_file()) if seats.is_dir() else []
    print(json.dumps({'attempt':i,'artifacts':{str(p.relative_to(r)):p.is_file() for p in artifacts},'producer_reports':[str(p.relative_to(r)) for p in reports]}),flush=True)
    if all(p.is_file() for p in artifacts) and reports:
        print('READY: T3 artifacts and producer report exist',flush=True)
        break
else: print('ABSENT: no complete T3 artifact/report set after 40 attempts',flush=True)
PY
```

It completed normally, exit 0. Last observed output lines:

```text
{"attempt": 15, "artifacts": {"corpus/fixtures/r100-docket-review/README.md": true, "corpus/fixtures/r100-docket-review/claim-excerpt-map.md": true, "corpus/fixtures/r100-docket-review/fictional-excerpts.md": true}, "producer_reports": []}
{"attempt": 16, "artifacts": {"corpus/fixtures/r100-docket-review/README.md": true, "corpus/fixtures/r100-docket-review/claim-excerpt-map.md": true, "corpus/fixtures/r100-docket-review/fictional-excerpts.md": true}, "producer_reports": [".ufo/waves/round-100/seats/T3-fixture-docs.md"]}
READY: T3 artifacts and producer report exist
```

The poll task was fully consumed before handoff. No all-reports poll, self-count dependency, stall escape, or timeout-exhaustion verdict was needed.

## Final path and snapshot check

Actual command immediately before writing this report, exit 0:

```sh
python3 - <<'PY'
from pathlib import Path
import hashlib
r=Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
assert Path.cwd().resolve()==r
p=r/'.ufo/waves/round-100/seats/V08-c2-anchors.md'
assert p.resolve()==r/'.ufo/waves/round-100/seats/V08-c2-anchors.md'
assert p.parent.resolve()==r/'.ufo/waves/round-100/seats'
assert not p.exists() and not p.is_symlink()
print('VERIFIED-WRITE-PATH',p.resolve())
expected={'README.md':'a312a364d4d9476e98c0fae3f62b23bf72e73a06c508aac04ffe48cf9cf4c5fa','claim-excerpt-map.md':'16981162f8476a8fcc1bd892ac0b1b9e6cb916e1d45e6f2ea392a5eeca769244','fictional-excerpts.md':'d01825a7e3c8f4af549b7acdde7eb8e1b9074a6eccb8ce6d12401cea19745705','source-excerpt.md':'b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd'}
for name,digest in expected.items():
    observed=hashlib.sha256((r/'corpus/fixtures/r100-docket-review'/name).read_bytes()).hexdigest()
    assert observed==digest,name+' changed after anchor replay'
print('DELIVERED-SNAPSHOT-STABLE 4/4 checked files unchanged after replay')
PY
```

Observed complete stdout:

```text
VERIFIED-WRITE-PATH /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V08-c2-anchors.md
DELIVERED-SNAPSHOT-STABLE 4/4 checked files unchanged after replay
```

No V08 anchor failure or unresolved blocker remains. Bounds: these checks establish lexical hits, numeric-span containment, obligation inventory, schema cleanliness, and inherited-byte/row preservation, not whole-claim entailment, dependency semantics, testimony truth, authenticated chronology, rights, permission, canon, C2 synthesis correctness, C1 freeze coverage, C3 calibration, census, or whole-round admission.

PASS — 22/22 JSON anchors are independently in-span; inherited excerpt/map line numbers and anchor fields are preserved; J22 is the sole new row/anchor and occurs only at review line 82 within section 78–88; all three delivered fixture gates pass.
