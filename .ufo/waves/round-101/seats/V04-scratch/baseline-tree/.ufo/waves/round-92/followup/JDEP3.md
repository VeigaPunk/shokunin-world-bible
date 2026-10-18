# JDEP3 — Edge-decision verification (r92 follow-up)

Seat JDEP3, round-92 follow-up wave, world-bible lane. Judged tree: **delivered**
`c4d4823b9a8165a88e8199af136e62d6e961b6b9` (baseline `396c568`); tracked tree clean, only
untracked follow-up artifacts. Checker `corpus/fixtures/check_bible.py` sha256
`ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` (r92 unchanged);
delivered support command blob `55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c`.
All measurements below are from this tree; scratch proxies under `/tmp/jdep3-r8` and
`/tmp/jdep3-r9` (14 small files; swept).

Mission: replay the R8 worked example (the seven-threshold-names case) end-to-end; verify the R9
manual-gate record format (required fields list); verify R10 namespace unchanged + register absent.

## Work performed

- Axes: edge-decision delivery fidelity (instrument vs delivered text), R9 record-format
  verification, R10 delta/absence verification, bounded evidence (editorial screens not upgraded
  to mechanical findings).
- Read at HEAD: the delivered decision table (whole file, esp. `:40`, `:42-48`, `:50-92`,
  `:94-113`), the r92 diff `396c568..c4d4823` for it (one hunk), the instrument patches
  `patches/E1-edges.md` and `patches/E2-wording.md` (r92) and the r91 chain
  (`round-89/followup/JDEP2*.md|json`, `round-90/followup/JDEP2*`, `round-91/patches/D1-edges.patch`,
  `E2-wording.md`), `holder-assessment-boundary.md` (no R8/R9/R10 text), `corpus/tools/README.md`,
  `corpus/fixtures/README.md`, the r89 register demo, peer follow-up artifacts
  (SF1/SF2/JDEP1/JDEP4/H3/H4/JCAL*/JCOV*/K1 — read JDEP4's edge-attack report and JDEP1's
  certification report for scope division; no duplication claimed).
- Two 60 s dependency checks (one background call, exact receipts):
  `check-01 2026-10-17T10:26:22-03:00 followup_dir=yes head=c4d4823` ·
  `check-02 10:27:22 followup_dir=yes head=c4d4823 E1=yes E2=yes E1edges=yes T1cert=yes`.
- Built two scratch proxies (delivered tools only): the seven-threshold case as a minimal
  cluster (5 JSON like `r8-deps-distinct` + the neutral `possible influence: unverified` note),
  and a translation-mode probe (map + excerpt + companion JSON). Exact probe content in
  "Before → after", §5–6. Scratch swept at the end; no tracked file other than this report and
  `JDEP3-receipts.json` was written; no commit, no push.

## Before → after measurements

**1. R8 seven-threshold case — chain walk (r89 → delivered).** Each hop carries the case; the
delivered table does not.

```sh
# file-level chain probe (needles per hop), then delivered-table counts
python3 - <<'PY'  # full script inline in seat run
from pathlib import Path
hops = {
 'r89 JDEP2 origin report': ('.ufo/waves/round-89/followup/JDEP2.md','seven-stair-descent'),
 'r89 JDEP2 pre-followup probes': ('.ufo/waves/round-89/followup/JDEP2-probes.json','seven thresholds'),
 'r90 JDEP2 case definition': ('.ufo/waves/round-90/followup/JDEP2.md','seven threshold names'),
 'r90 JDEP2 probe case': ('.ufo/waves/round-90/followup/JDEP2-probes.json','seven threshold names'),
 'r91 D1 edge patch': ('.ufo/waves/round-91/patches/D1-edges.patch','Kesh Hymn'),
 'r91 E2 wording patch': ('.ufo/waves/round-91/patches/E2-wording.md','Kesh Hymn'),
 'r92 E1 edge patch': ('.ufo/waves/round-92/patches/E1-edges.md','Kesh Hymn'),
 'r92 E2 wording patch': ('.ufo/waves/round-92/patches/E2-wording.md','Kesh Hymn'),
 'delivered table': ('corpus/knowledge/r88-sourced-inspiration-decision-table.md','Kesh Hymn'),
}
for label,(p,needle) in hops.items():
    t=Path(p).read_text(); print(f'{label}: {"FOUND" if needle in t else "ABSENT"}')
PY
```

Observed:

```text
r89 origin/probes, r90 case/probe, r91 D1/E2, r92 E1/E2: FOUND (8/8)
delivered table: ABSENT  (Kesh count = 0; "seven" count = 0)
```

At `396c568` the same counts hold (`grep -c seven` = 0; `Kesh` = 0): the r91 integration of
D1/D2 landed a merged, reduced paragraph and no worked example, so the case has never been part
of a delivered table — the r92 replacement was applied only in part.

**2. R8 delivered paragraph vs the instrument (E1/E2).** E1 and E2 carry identical R8 blocks;
the delivered paragraph equals the instrument byte-for-byte after removing one duplicated opener.

```sh
python3 - <<'PY'
from pathlib import Path
d = Path('corpus/knowledge/r88-sourced-inspiration-decision-table.md').read_text()
p = Path('.ufo/waves/round-92/patches/E1-edges.md').read_text()
i = d.index('**Failed-gate disposition (clarified r92):**'); dp = d[i:d.index('\n\n', i)]
ip = p.index('> **Failed-gate disposition (clarified r92):**'); pp = p[ip+2:p.index('\n>\n', ip)]
print('delivered len:', len(dp), 'patch len:', len(pp), 'equal:', dp == pp)
print('equal after removing duplicate opener:', dp.replace('**Failed-gate disposition (clarified r92):** ','',1) == pp)
PY
grep -o "Failed-gate disposition (clarified r92):" corpus/knowledge/r88-sourced-inspiration-decision-table.md | wc -l
grep -o "Failed-gate disposition (clarified r92):" .ufo/waves/round-92/patches/E1-edges.md | wc -l
```

Observed:

```text
delivered len: 1677 patch len: 1632 equal: False
equal after removing duplicate opener: True
delivered opener count: 2   patch opener count: 1
```

`:40` starts `**Failed-gate disposition (clarified r92):** **Failed-gate disposition
(clarified r92):** **Owner:** …` (independently measured; JDEP4 also reports this as
D-JDEP4r92-2). The instrument's 1632-char paragraph is otherwise exact, including
`withhold the **whole element from supported canon**`.

**3. R8 case → delivered-rule clause coverage (whitespace-normalized).** Every disposition the
case requires maps to delivered text, including the retained separable-branch rule:

```text
trigger (inseparable branch): True          whole-element hold: True
keep note + R2 unavailable: True            not proof of source use: True
no external-only marker: True               record fields (failed condition/contrary
l0 route: True                              evidence/separability/scope/next action): True
no notice-instead-of-hold: True             note removal condition: True
separable branch retained (r90 text): True
clause_coverage=10/10
```

**4. R8 case → mechanical replay (scratch proxy).** The held case, materialized as a valid
cluster with the `possible influence: unverified` note, passes the delivered checker — the R8
screen is editorial, as `:117` states ("governance rows, not checker or schema changes").

```sh
PYTHONDONTWRITEBYTECODE=1 python3 corpus/fixtures/check_bible.py /tmp/jdep3-r8/seven-threshold
```

Observed: `CLEAN: schema, citations, relations, timeline; 0 violations` — `r8_case_exit=0`.
Proxy: `sources.json` (`shore-threshold-record`), two entities (`seven-stair-descent` item,
`kesh-witness` character) whose claims name the seven shore thresholds in a fixed order, empty
relations/timeline/contradictions, and `inspiration-note.md` carrying the dated note, the
sequence match to *Kesh Hymn* lines 12–19, "no independently authored, supportable remainder",
and the whole-element-hold disposition under the delivered r92 text.

**5. R9 r92 content vs instrument — verbatim.** All four delivered paragraphs are byte-identical
to E1 (and E2): gate 1345/1345, required record 546/546, receipt boundary 651/651, new worked
example 884/884 (`equal=True` each, splitline compare).

Required-record field list (delivered `:44`, byte-identical to the instrument):

```text
claim pointer · excerpt path and span · delivered printing/edition and year plus a stable
identifier or copy locator · translator · source work and source-text/version field (including
explicit unknown status) · evidence citation and inspection method · reviewer name/role and
review date · disposition `PASS`, `FAIL`, or `OPEN` · exact claim scope permitted
```

**6. R9 placement / replacement / row-append deviations.** The block landed *before* the
`### R9 appendix` heading; the appendix's own worked example was not replaced; the row-level
evidence-cell append is absent.

```sh
python3 - <<'PY'
import subprocess, hashlib
from pathlib import Path
d = Path('corpus/knowledge/r88-sourced-inspiration-decision-table.md').read_text()
pre = subprocess.check_output(['git','show','396c568:corpus/knowledge/r88-sourced-inspiration-decision-table.md'],text=True)
for name,s in (('R8 appendix','### R8 appendix'),('r8 failed-gate','**Failed-gate disposition'),
               ('R9 manual gate','**Manual R9 gate'),('R9 required record','**Required record:**'),
               ('R9 receipt boundary','**Receipt boundary:**'),('R9 appendix','### R9 appendix'),
               ('R10 appendix','### R10 appendix')):
    print(f'{name}: idx={d.find(s)}')
h = lambda s: hashlib.sha256(s.encode()).hexdigest()[:16]
seg = lambda t: t[t.index('### R9 appendix'):t.index('### R10 appendix')]
print('R9 appendix seg hash pre/delivered:', h(seg(pre)), h(seg(d)))
row = [l for l in d.splitlines() if l.startswith('| R9 — An in-world claim')][0]
print('mandated append present in row:', 'separate per-claim R9 manual-review record' in row)
PY
```

Observed:

```text
R8 appendix: idx=16733   r8 failed-gate: 17599   R9 manual gate: 19278
R9 required record: 20625   R9 receipt boundary: 21173   R9 appendix: 22712   R10 appendix: 26285
R9 appendix seg hash pre/delivered: effe405e92c7895b / effe405e92c7895b
mandated append present in row: False
```

So `:42-48` sit inside the R8 appendix region, while E1/E2 both instruct "within the R9 appendix,
after its existing **Decision** paragraph and before **Worked example**"; the R9 appendix is
byte-identical pre/post (its old r90 worked example still serves as the appendix's example, and
the new M. A. Translator example sits outside it); and E1's mandated R9-row append ("For every
translation-backed R5 claim, require the separate per-claim R9 manual-review record; …") is
document-wide absent. T1's own r8/r9 delivery scan replayed at HEAD is 2/4 — its two R9 checks
read the R9 appendix region and therefore report False for text that exists elsewhere:

```sh
python3 - <<'PY'   # T1.md:249-262 scan, replayed verbatim
from pathlib import Path
p=Path('corpus/knowledge/r88-sourced-inspiration-decision-table.md').read_text()
r8=p.split('### R8 appendix',1)[1].split('### R9 appendix',1)[0]
r9=p.split('### R9 appendix',1)[1].split('### R10 appendix',1)[0]
checks={
'r8_inseparable_whole_element_branch':'inseparable' in r8.lower() and 'whole element' in r8.lower(),
'r8_failed_gate_not_proof_of_source_use':'not proof' in r8.lower() or 'does not prove source use' in r8.lower(),
'r9_manual_review_gate':'manual r9 gate' in r9.lower() or 'manual review' in r9.lower(),
'r9_lexical_receipt_not_manual_receipt':'lexical preflight' in r9.lower() and 'not that receipt' in r9.lower()}
print(sum(checks.values()), '/4', checks)
PY
```

Observed: `2 /4 {'r8_inseparable_whole_element_branch': True, 'r8_failed_gate_not_proof_of_source_use':
True, 'r9_manual_review_gate': False, 'r9_lexical_receipt_not_manual_receipt': False}`.

**7. R9 record format → behavioral replay (scratch proxy, delivered tools).** A
translation-backed claim reaches lexical `RESULT PASS` while the map itself records no manual
review; the tool cannot see any record field.

Probe (`/tmp/jdep3-r9/translation-probe`), map and excerpt verbatim:

```text
**Expected inventory:** 1 JSON facts; 0 editorial rows; 1 total mapped rows; 1 distinct excerpt anchors.
## R9 excerpt declarations
| Excerpt | Source / reference | Delivery mode | Status |
| `source-excerpt.md:5` | private 2011 reprint of a 1901 translation | `translation` | scan + copy locator supplied; no manual review recorded |
## JSON facts
| ID | JSON fact and fields | `source_id` | Excerpt path:line | R9 mode | Exact anchor |
| P1 | `entities[0].claims[0]`: the keeper set the ring upon the fourth stair | `keeper-record` | `source-excerpt.md:5` | `translation` | `The keeper set the ring upon the fourth stair in slow measure.` |

source-excerpt.md:  heading · blank · `Delivery mode (R9): translation` · blank · the anchor line (line 5)
```

```sh
PYTHONDONTWRITEBYTECODE=1 python3 corpus/fixtures/check_bible.py /tmp/jdep3-r9/translation-probe
PYTHONDONTWRITEBYTECODE=1 python3 corpus/tools/support_check.py /tmp/jdep3-r9/translation-probe
```

Observed:

```text
CLEAN: schema, citations, relations, timeline; 0 violations        r9_checker_exit=0
INVENTORY JSON-FACTS 1/1; EDITORIAL-ROWS 0/0; TOTAL-ROWS 1/1; DISTINCT-ANCHORS 1/1
PASS P1: source-support; mode=translation; anchor=found; 5:The keeper set the ring upon the fourth stair in slow measure.
SOURCE-SUPPORT 1/1; EDITORIAL-ANCHORS 0/0; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 1/1; VALIDATED-ROWS 1/1
RESULT PASS                                                        r9_support_exit=0
```

Static probe of the delivered support command — no required-record field is readable by it
(`Source text/version`, `Delivered printing`, `translator`, `edition/year`, `catalogue`,
`R9 manual review`, `reviewer`, `copy locator`: all 0). The delivered procedure text therefore
carries the whole manual gate; `RESULT PASS`/`SOURCE-SUPPORT` alone cannot clear it — the
receipt-boundary sentence is accurate against the delivered tool.

**8. R10 namespace + register (delta verification).** The r92 diff for the table is one hunk
(`@@ -37,14 +37,15 @@`); the R10 row and appendix are byte-identical across `c2ab3d0` → `396c568` →
`c4d4823`; the live register is absent; the landed clusters remain disjoint.

```text
R10 appendix seg hash:   c2ab3d0=14ea47d3652171ef  396c568=14ea47d3652171ef  c4d4823=14ea47d3652171ef
Namespace paragraph:     c2ab3d0=28b3ce4f2e7b4657  396c568=28b3ce4f2e7b4657  c4d4823=28b3ce4f2e7b4657
register_present= False   (find for cross-cluster-contradictions.md: 0; tracked cross-cluster file: r89 demo only)
r89 demo disclaimers: 'not a new canon assertion or an integration-ready register entry' = 1; 'Do not treat this demo as an append' = 1
r87 source ids ∩ r88-m3 source ids = []   (['dune-register','gate-witness','lowwater-hymn','shell-charter','tide-bell-tally'] vs ['paired-clock','veil-verse'])
python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster corpus/fixtures/r88-m3-maya-cluster  →  usage error, two_dir_exit=2
```

`git show --stat c4d4823 -- corpus/knowledge/` lists only `holder-assessment-boundary.md`,
`r88-sourced-inspiration-decision-table.md`, `r91-c9-watch.md` — no register file was created.
r92 artifacts mentioning the register are the two JDEP4 follow-up files (peer, no creation).

**9. Contract probes of the delivered support command (context for the tools README finding).**

```text
missing inventory  → stdout 'RESULT FAIL'  stderr 'FAIL: map must contain exactly one expected inventory declaration'  exit=1
missing map        → stdout 'RESULT ERROR' stderr 'FAIL: claim-to-excerpt map not found'                              exit=2
missing cluster    → stdout 'RESULT ERROR' stderr 'FAIL: cluster directory not found: /tmp/jdep3-r9/nodir'            exit=2
```

## Findings & named debt

- **F1 (new). The R8 worked example (seven-threshold-names case) is not in the delivered table.**
  The case chain is intact through the wave artifacts (r89 JDEP2 origin → r90 case probes → r91
  D1/E2 → r92 E1/E2, 8/8 hops) but the delivered table carries it 0 times, and the r91 table
  never carried it either. The integrated r92 replacement dropped the instrument's second
  blockquote (worked example) while keeping the first. **Debt D-JDEP3r92-1:** land the worked
  example (E1/E2 text) at the next table touch, or record why the instrument was narrowed.
- **F2. Doubled R8 label (independently measured; also JDEP4 D-JDEP4r92-2).** `:40` opener count
  2 vs instrument 1; paragraph otherwise exact. **Debt D-JDEP3r92-2:** de-duplicate the opener
  when fixing F1.
- **F3 (new). R9 r92 block placement and replacement deviations.** Content is verbatim (4/4
  paragraphs byte-equal) but (i) `:42-48` sit inside the R8 appendix region, not within the R9
  appendix as instructed; (ii) the R9 appendix is byte-identical pre/post — its worked example
  was not replaced, and both the old appendix example and the new M. A. Translator example now
  exist; (iii) E1's mandated R9-row evidence-cell append is absent, so the row does not point at
  the manual gate. Effect: T1's r9 checks (appendix-scoped) read False; a reader of the R9
  appendix will not find the mandatory gate; `:48`'s example is orphaned from its gate text.
  **Debt D-JDEP3r92-3:** move the block into the R9 appendix after **Decision** and before
  **Worked example**, apply the worked-example replacement, and append the row sentence.
- **F4 (verified positive). R8/R9 normative content and format.** R8 paragraph exact modulo F2;
  R8 clause coverage 10/10 including the retained separable-branch rule; R9 required-record line
  byte-identical to the instrument with all nine field groups; lexical-vs-manual boundary
  demonstrated on the delivered tools (`RESULT PASS` with no manual record; 0 tool hits for
  record fields). The R8 case passes the checker by design — the screen stays editorial.
- **F5 (verified positive). R10 unchanged and register correctly absent.** Namespace paragraph
  and R10 appendix byte-identical since `c2ab3d0`; no register file; demo disclaimers intact;
  landed-cluster source ids disjoint; two-directory calls remain a usage error (exit 2).
- **F6 (new, adjacent to C2). `corpus/tools/README.md` is stale against the delivered tool.**
  The file is unchanged in r92 while `support_check.py` changed; its "Named debt — S2
  terminal-status contract" section (`:16-21`) still says missing inventory exits 2 and that
  map/cluster errors return 2 without `RESULT ERROR`, and tells callers to compensate "until the
  checker is updated". The delivered tool now returns exit 1 + `RESULT FAIL` (inventory) and exit
  2 + `RESULT ERROR` (map/cluster), and `corpus/fixtures/README.md:1037-1038` documents exactly
  those new statuses. **Debt D-JDEP3r92-4 (parent/r93):** refresh or delete the stale section.
- **Verdict-shaped summary (verification seat, evidence-bounded):** edge-decision *content*
  improved-bounded at r92 (both decisions now decided, structured, and format-verified);
  text hygiene **harmed** (doubled label, F2) and instrument completeness **partial** (F1, F3) —
  the positives do not offset the harm. R10 is unchanged-verified. Boundary-document
  certification is JDEP1's lane (its gate (b) is blocking there) and was not re-run here; T1's
  committed record speaks of its own baseline, so the delivered table's r8/r9 checks were
  replayed by this seat instead (2/4, location-sensitive).

## Handoff

- Written: `.ufo/waves/round-92/followup/JDEP3.md` (this report) and
  `JDEP3-receipts.json` (machine-readable counts/hashes/probe outcomes). No other tracked write;
  no commit or push.
- Scratch: `/tmp/jdep3-r8/seven-threshold` (6 files) and `/tmp/jdep3-r9/translation-probe`
  (7 files) + `/tmp/jdep3-r9/bad-inventory.md`; all swept. Probe content is inline above
  (§4, §7) and repeated in the receipts JSON for recreation.
- For the parent/r93: F1+F2 are one small edit to `:40`; F3 is one section move + row append;
  F6 is a docs touch-up. None is a blocker to reading the delivered decisions, but as delivered
  the edge-decision surface is not a faithful full application of the work-wave instrument.
- Not covered here (other lanes): boundary-doc certification (JDEP1), C3 watch re-check,
  census, boundary-doc anchors. No `l0-questions.md` append (not authorized for this seat).