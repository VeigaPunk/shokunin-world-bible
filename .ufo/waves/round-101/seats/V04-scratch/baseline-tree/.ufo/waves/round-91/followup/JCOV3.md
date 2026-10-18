# JCOV3 — Denominators judge (r91 follow-up)

Seat: JCOV3, round-91 follow-up wave (freeze-then-verify). Lane target: alibaba-token-plan/deepseek-v4.1-flash (per wave-spec; served lane not exposed to this seat).
Delivered tree under test: `c2ab3d07eaa86ce58f3f9c7fdff702f4b91ea7b7` (work `6332115` + `c2ab3d0`, baseline `a7c6a17`). All measurements below were taken on this tree; `git status --porcelain` was clean except the untracked `followup/` directory. Date of run: 2026-10-17, 08:32–08:37 (-03:00).

Mission: independent recount of both clusters' raw JSON facts (14+8 vs 10); every map row's pointer resolves; verify the M6 reconciled formats are what the script actually parses.

## Work performed

- Ran the two-dependency wait protocol (one call, 60 s checks, timestamped): HEAD constant across check1/check2/check3; sibling followup artifacts arrived during the window; terminal line emitted.
- Independently recounted the r87-myth-cluster and r88-m3-maya-cluster maps with my own table parser and JSON-pointer resolver (not the delivered `support_check.py` code paths) — row counts by section, distinct `(path, anchor)` pairs, exact-duplicate rows, pointer resolution over every backticked pointer token, `path:line` locator resolution, and `grep -nF`-style anchor-line checks.
- Cross-checked the 14-fact denominator against its source: `.ufo/waves/round-89/patches/S2-fact-map.json` (S2's map the r87 map claims to carry).
- Cross-checked every row's `source_id`/`Source` column against `sources.json` ids, and every explicit source-bearing JSON token (`.source_id`, `.first_appearance`) against the row's declared source.
- Verified the delivered `support_check.py` actually parses the delivered `**Expected inventory:**` lines: regex-level fullmatch, `parse_map()` on each delivered map, end-to-end runs on all three fixtures, plus three format controls (heading removed / M1-style `json_rows=` / commas) and a missing-inventory temp-cluster probe.
- Swept scratch: removed the one bytecode artifact my import probe created (`corpus/tools/__pycache__/`, git-ignored, restored), removed all /tmp probe files and dirs, and the wait log/t0 marker after transcription.

Relevant delivered hashes (commands: `sha256sum`, `git rev-parse <rev>:<path>`):

```sh
sha256sum corpus/tools/support_check.py
# 9da149b8e51f5c6c39477f17b8b19d17da3568a1a7c72412079efccff1f330bf
git rev-parse c2ab3d0:corpus/tools/support_check.py a7c6a17:corpus/tools/support_check.py
# f75af1ce66ba45a70189d1ed9540fff0a76d5fee   (delivered)
# 7c050acb970c04ca74e9a60674120d252f0f3333   (r90 closure; changed by r91, expected)
sha256sum corpus/fixtures/check_bible.py
# ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
git rev-parse c2ab3d0:corpus/fixtures/check_bible.py a7c6a17:corpus/fixtures/check_bible.py
# 20c56dbb90d9f59ca4fb85971154c0774f5ce0d0  (both) -> checker untouched in r91
```

`corpus/knowledge/r91-c9-watch.md:6` pins the same `ff9fd2aa…` SHA-256 — consistent with the delivered `check_bible.py`.

Wait-protocol receipt (background call, log transcribed verbatim; log removed after transcription):

```text
[check1] 2026-10-17T08:32:58-03:00 HEAD=c2ab3d07eaa86ce58f3f9c7fdff702f4b91ea7b7
[check2] 2026-10-17T08:33:58-03:00 HEAD=c2ab3d07eaa86ce58f3f9c7fdff702f4b91ea7b7
H4-census.json H4-lineage.json H4-probes.json
[check3] 2026-10-17T08:34:58-03:00 HEAD=c2ab3d07eaa86ce58f3f9c7fdff702f4b91ea7b7 followup=H4-c1-discrimination.json H4-census.json H4-lineage.json H4-probes.json JCAL5-delta.json
[terminal] deadline_reached=true
```

Independent recount probe (condensed logic of the probe actually run from `lore-shokunin/`; my own parser/resolver, not the delivered script's code paths — observed output shown under Before → after):

```python
import json, re
from pathlib import Path
FILES = {"entities":"entities.json","relations":"relations.json","timeline":"timeline.json",
         "contradictions":"contradictions.json","sources":"sources.json"}
TOKEN = re.compile(r"`([a-z_]+\[\d+\](?:\.[a-z_]+(?:\[\d+\])?)*)`")
def load(cluster):
    return {n: json.loads((cluster/f).read_text()) for n,f in FILES.items()}
def resolve(data, ptr):
    m = re.fullmatch(r"([a-z_]+)(\[\d+\])(.*)$", ptr); cur = data[m.group(1)]
    for part in re.finditer(r"\.([a-z_]+)(?:\[(\d+)\])?", m.group(3)):
        cur = cur[part.group(1)]; cur = cur[int(part.group(2))] if part.group(2) else cur
        if isinstance(cur, list) is False and part.group(2): raise TypeError("scalar index")
    return cur
def rows(mapfile):
    out, hdr, section = [], None, None
    for ln in mapfile.read_text().splitlines():
        if ln.startswith("## "): section = ln[3:].strip()
        if not ln.lstrip().startswith("|"): hdr = None; continue
        cells = [c.strip().strip("`") for c in ln.strip().strip("|").split("|")]
        if hdr is None:
            if "ID" in cells and any("Excerpt" in c for c in cells): hdr = cells
            continue
        if all(re.fullmatch(r":?-{3,}:?", c.replace(" ","")) for c in cells): continue
        if len(cells) == len(hdr): out.append((section, dict(zip(hdr,cells)), ln))
    return out
for label, cdir in (("r87","r87-myth-cluster"), ("r88-m3-maya-cluster","r88-m3-maya-cluster")):
    data = load(Path("corpus/fixtures")/cdir)
    rws = rows(Path("corpus/fixtures")/cdir/"claim-excerpt-map.md")
    json_rows  = [r for s,r,_ in rws if s and s.lower().startswith("json facts")]
    ed_rows    = [r for s,r,_ in rws if s and s.lower().startswith("editorial rows")]
    pf = af = 0
    for s,r,ln in rws:
        for t in set(TOKEN.findall(ln)):
            try: resolve(data, t)
            except Exception as e: pf += 1; print("POINTER-FAIL", r.get("ID"), t, e)
        m = re.match(r"`?([^`:]+\.md):\s*(\d+)", r["Excerpt path:line"])
        a = r["Exact anchor"]
        hits = [i+1 for i,l in enumerate(data and (Path("corpus/fixtures")/cdir/m.group(1)).read_text().splitlines()) if a in l]
        if int(m.group(2)) not in hits: af += 1; print("ANCHOR-FAIL", r.get("ID"), m.group(1), m.group(2), hits)
    print(label, "jsonRows",len(json_rows),"edRows",len(ed_rows),"pointerFails",pf,"anchorFails",af)
```

## Before → after measurements

"Before" = the wave's declared denominators and M6's claimed receipts; "after" = my independent observations on the delivered tree. Every line below is observed output; commands are exact.

1. Inventory denominator recount (probe above):

```text
### r87: total table rows w/ ID+Excerpt header: 22
  JSON facts section rows: 14, editorial rows section: 8
  pointer failures: 0
  anchor/line failures: 0
### r88-m3: total table rows w/ ID+Excerpt header: 10
  JSON facts section rows: 10, editorial rows section: 0
  pointer failures: 0
  anchor/line failures: 0
```

2. Distinct anchors / duplicates / source columns (second probe, same parser idea):

```text
C. r87: rows=22; distinct (path,anchor)=22; distinct anchor strings=22; repeats=0
C. r88: rows=10; distinct (path,anchor)=6; distinct anchor strings=6; repeats=4
B. r87: fact rows=22; source-col outside sources.json=0; explicit tokens checked=20 mismatches=0
B. r88: fact rows=10; source-col outside sources.json=0; explicit tokens checked=4 mismatches=0
D. r87 entities=7 claims=7; mapped=6; disclosed-extra exists=True
D. r88 entities=4 all-paired-clock=True relations=0 contradictions=0 timeline=2 sources=['veil-verse','paired-clock']
D. r89 entities.json#/0/claims/0 -> {"statement": "The Ash-Stair Ledger records the tide-mark moved to the west stair.", "source_id": "ash-ledger"}
```

(r88's four claims and two timeline events were additionally read directly: all `source_id` values = `paired-clock`; r89 anchor `moved to the west stair` hits exactly line 9 of `ash-ledger-excerpt.md`; `ash-ledger` is in r89 `sources.json`.)

3. Denominator source cross-check (S2's r89 map vs delivered r87 rows):

```sh
python3 -  # loads .ufo/waves/round-89/patches/S2-fact-map.json, matches all 14 facts to map rows
```

```text
A. S2 14 facts -> delivered r87 rows: discrepancies = NONE
   ids identical: True
```

S2's own counts: `{'entity_claims': 6, 'relation_edges': 4, 'timeline_events': 4, 'total': 14}`; the facts list has exactly 14 entries with matching `json_fields`, `source_id`, and `anchor_phrase` against the delivered rows.

4. Delivered script end-to-end, three fixtures (exit codes separately):

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster
python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster
python3 corpus/tools/support_check.py corpus/fixtures/r89-inspiration-paraphrase
```

```text
r87: INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 8/8; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 22/22
     ANCHORS repeated-references=0; DUPLICATE-ROWS 0
     SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 8/8; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22; VALIDATED-ROWS 22/22
     RESULT PASS   (exit 0)
r88: INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 0/0; TOTAL-ROWS 10/10; DISTINCT-ANCHORS 6/6
     ANCHORS repeated-references=4; DUPLICATE-ROWS 0
     SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 0/0; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 10/10; VALIDATED-ROWS 10/10
     WARN: unreferenced excerpt declaration: source-excerpt.md (mode=verbatim)
     RESULT PASS WITH WARNINGS   (exit 0)
r89: INVENTORY JSON-FACTS 1/1; EDITORIAL-ROWS 0/0; TOTAL-ROWS 1/1; DISTINCT-ANCHORS 1/1
     PASS entities.json#/0/claims/0: retelling-support-only; anchor=found; mode=paraphrase; 9:A modern paraphrase says ...
     SOURCE-SUPPORT 0/0; EDITORIAL-ANCHORS 0/0; RETELLING-SUPPORT-ONLY 1 entries (1/1 anchors); MODES 1/1; VALIDATED-ROWS 1/1
     RESULT PASS   (exit 0)
```

These match M6.md's claimed receipts line-for-line, including the r88 expected WARN and the r89 retelling row.

5. M6 reconciled format is what the delivered script actually parses (format controls; one temp file reused, then deleted):

```sh
python3 -  # importlib-loads corpus/tools/support_check.py; sc.parse_map on mutated copies of the delivered r87 map
```

```text
i  delivered form (## Inventory + **Expected inventory:** line): PARSE-OK inv=(14, 8, 22, 22) rows=22
ii heading removed, line kept: PARSE-OK inv=(14, 8, 22, 22) rows=22
iii M1-style json_rows= format: ValueError: map must contain exactly one expected inventory declaration
iv commas instead of semicolons: ValueError: map must contain exactly one expected inventory declaration
```

Regex fullmatch of the delivered `EXPECTED_INVENTORY` on the delivered map lines:

```text
r87 line fullmatch: True groups=('14', '8', '22', '22')
r88 line fullmatch: True groups=('10', '0', '10', '6')
r89 line fullmatch: True groups=('1', '0', '1', '1')
control (M1-style 'json_rows=14, editorial_rows=8'): False
control (missing total field): False
control (bold dropped): False
```

`parse_map()` on the delivered maps returns exactly `(14,8,22,22)`, `(10,0,10,6)`, `(1,0,1,1)` with kinds json/editorial 14/8, 10/0, 1/0; the delivered `## Inventory` heading is structural (control ii still parses) while the `**Expected inventory:**` line is load-bearing.

6. Missing-inventory path (README-documented deviation #1) on a temp cluster:

```sh
python3 corpus/tools/support_check.py /tmp/jcov3-badmap2   # map with a JSON-facts table but no inventory line
# stdout: (empty)                      stdout-exit=2
# stderr: FAIL: map must contain exactly one expected inventory declaration
```

7. Remnant sweep (no M1-format leftovers in the delivered tree):

```sh
grep -rn "json_rows\|INVENTORY_HEADING\|Inventory must declare" corpus/tools/ corpus/fixtures/r87-myth-cluster/claim-excerpt-map.md corpus/fixtures/r88-m3-maya-cluster/claim-excerpt-map.md corpus/fixtures/r89-inspiration-paraphrase/claim-to-excerpt-map.md
# no matches
```

All three `Expected inventory`-bearing maps in `corpus/` parse under the delivered parser (README.md's occurrences are prose, correctly rejected as a map).

## Findings & named debt

- **C2 denominators — verdict: improved (independently corroborated, 0 discrepancies).** r87 = 14 JSON facts + 8 editorial rows = 22 rows with 22 distinct `(path, anchor)` pairs and 0 repeated references; r88-m3 = 10 JSON facts, 0 editorial, 6 distinct anchors, 4 legitimate repeated co-maps. Both match the declared inventories and the wave-spec line "r87 14+8, r88-m3 10". The 14-fact set is traceable to S2's r89 map (`S2-fact-map.json`, counts 6/4/4=14) with ids, fields, sources, and anchors identical.
- **Every map row's pointer resolves — verdict: improved (corroborated).** 32 fact rows across the two clusters plus r89's single row: 0 pointer-resolution failures (all `entities[i]…`, `relations[i]…`, `timeline[i]…`, and r89's `entities.json#/0/claims/0` form), 0 locator/anchor-line failures, 0 source-column values outside `sources.json`, 0 explicit source-token mismatches.
- **M6 reconciled formats — verdict: improved (corroborated and load-bearing).** The delivered maps carry exactly the syntax the delivered script fullmatches and parses; M1-style or punctuation-variant declarations are rejected (`ValueError` → exit-2 path). The r89 map's inventory line (landed in `c2ab3d0`, "missed from the work commit") also parses: `(1, 0, 1, 1)`.
- **README's two named deviations — documented, and the live probe matches.** Missing inventory → stderr `FAIL: map must contain exactly one expected inventory declaration`, stdout empty, exit 2 (README bullet 1 confirmed live; also confirms no `RESULT ERROR`). The collected-failure path (`FAIL:` diagnostics, exit 1, no `RESULT FAIL`) and the map-error path (`exit 2` without `RESULT ERROR`) were verified by reading `run()`/`main()` (lines 365–370, 393–395) — code-read only, not re-probed with a failing row.
- **Scope observations (not discrepancies).** r87 `entities.json` has 7 claims; the 7th (`entities[2].claims[0]`, the hymn claim) exists verbatim and is disclosed in the map's full-crosswalk note as outside the 14-fact S2 set. r87 `contradictions.json` has 1 entry (`moon-basin-vow-location`); it is not a row in either declared scope, and the map's notes preserve the T3/T4 location conflict unresolved — consistent with the declared scope, worth keeping in view for future breadth rounds.
- **Boundary of this seat's evidence.** I did not re-run M6's five mutating attacks (they need disposable cluster copies; M4/attack seats' territory), and I did not re-verify the B1/B2 census (C1 seat). Within those bounds, every non-mutating M6 receipt reproduces exactly on the delivered tree, and the parse gate the attacks target is demonstrably live (controls iii/iv, missing-inventory probe).
- **Scratch/cleanup debt: none outstanding.** `corpus/tools/__pycache__/` created by my import probe was removed (git-ignored, tree restored: `git status --porcelain` shows only `?? .ufo/waves/round-91/followup/`); `/tmp` probes and the wait log/t0 removed. No tracked file other than this report was written.

## Handoff

- Deliverable: this file, `.ufo/waves/round-91/followup/JCOV3.md`. No other repo writes; no commit, no push.
- Freeze integrity: HEAD `c2ab3d0` held across the entire run (three checks over 120 s + final status check); if a later integration moves HEAD, re-run measurements 4–5 (cheap, read-only).
- Pins for downstream seats: `support_check.py` sha256 `9da149b8…f330bf` (git blob `f75af1ce…`), `check_bible.py` sha256 `ff9fd2aa…d1421` (blob `20c56db…`, unchanged in r91, agrees with `corpus/knowledge/r91-c9-watch.md:6`).
- For the parent: C2's denominator and format claims are confirmed on the delivered tree; the one open documentation-adjacent nuance is that README bullet 2's collected-failure path was code-read rather than live-probed here — a cheap follow-up probe if the judgement wants a live receipt for it.