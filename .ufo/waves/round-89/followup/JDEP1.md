# JDEP1 — Depth judge #1 (R8–R10 verification)

Seat: JDEP1. Wave: round-89 follow-up (world-bible lane), fleet root `/home/vgpnk/Projects/shokunin`, repo `lore-shokunin/`.
Judged on the DELIVERED tree at `1b09f3ff8016b26a2259e086f673d0112f4f54e5` (`1b09f3f`), baseline `51b286b`. Never on intent or scratch patches; scratch is used for probes/controls only.
Target: the R8/R9/R10 rows (lines 22–24) of `corpus/knowledge/r88-sourced-inspiration-decision-table.md` (delivered sha256 `9afb6ce9…a4b5f9`) plus the artifacts those rows cite.
Scratch: `/tmp/jdep1/`. Receipts: `.ufo/waves/round-89/followup/JDEP1-receipts.json`.
Provenance note: an earlier same-seat artifact was found at this path before this dispatch (written 04:21, before my run) and was preserved to `/tmp/jdep1/prior-JDEP1.md`. This report is based solely on my own measurements at `1b09f3f`; every receipt in it (term scans, both cluster replays, two-directory rejection, fixture replay, render counts) reproduced, and I added one stronger R9 control the predecessor did not run (excerpt file deleted).

## Work performed

- Read the delivered table incl. the `## Integration boundary` + `Integration notes (r89 closure)` block, the r88 source report `.ufo/waves/round-88/followup/JDEP3.md` and `JDEP3-probes.json` (the rows' cited evidence), the r89 sibling reports `JDEP2.md` (adversarial attack) and `JDEP3.md` (register readiness), and the r89 C3 artifacts: `corpus/knowledge/r89-cross-cluster-contradiction.md`, `corpus/fixtures/r89-inspiration-paraphrase/*`, `corpus/knowledge/reference-ledger.md`.
- Replayed every evidence command the three rows cite: the JDEP3 S1 15-term scan (on the r88 measured revision `2ea9ef1` and on the `51b286b` baseline), the S1 ETCSL locator/excerpt probe, the S2 durable-fixture replay plus an independent paraphrase-vs-verbatim control and a missing-excerpt control, the S3 per-cluster replays, the two-directory CLI rejection, and the registry scan.
- Resolved every cited line range and probe key in `JDEP3.md` / `JDEP3-probes.json`.
- Verified owner clauses + prospective scoping by whitespace-normalized phrase extraction; verified the table's pipe-line/column shape and its actual GFM rendering with a real parser (`marked` 18.1.1, installed under `/tmp/jdep1/md`).
- Ran harm/attribution checks: baseline-vs-delivered render, landed-cluster replays, C3-attributable diff subset, and whether the wave's checker diff touches excerpt/delivery-mode behaviour.
- Ran two timestamped 60-second wait-checks on `.ufo/waves/round-89/followup/`.
- No tracked file was written; the only repository writes are this report and `JDEP1-receipts.json`.

## Before → after measurements

All commands run from `lore-shokunin/` unless stated.

**Tree identity and hashes.**

```sh
git rev-parse HEAD
git status --porcelain
git diff HEAD --stat -- corpus/knowledge/r88-sourced-inspiration-decision-table.md corpus/knowledge/r89-cross-cluster-contradiction.md corpus/fixtures/r89-inspiration-paraphrase corpus/knowledge/reference-ledger.md corpus/fixtures/check_bible.py
sha256sum corpus/knowledge/r88-sourced-inspiration-decision-table.md
git show 51b286b:corpus/knowledge/r88-sourced-inspiration-decision-table.md | sha256sum
git show 2ea9ef1:corpus/knowledge/r88-sourced-inspiration-decision-table.md | sha256sum
```

```text
1b09f3ff8016b26a2259e086f673d0112f4f54e5
 M l0-questions.md
?? .ufo/waves/round-89/followup/
(no diff output -> every target file is byte-identical to HEAD at 1b09f3f)
9afb6ce93d8472d1487caba6c00ad24f462a32476c35e955b46f7054b8a4b5f9  corpus/knowledge/r88-sourced-inspiration-decision-table.md
3a218d2a19cd51362fe4f52232e9b3d4da1a968ea747ec9aa3fbde04c0b777e0  -
f85b63e46516f16f2f717574d08be46a9bcc96acee507492f5875fecd113b873  -
```

The working tree's only tracked deviation is the follow-up wave's own `l0-questions.md` line (uncommitted; it concerns the kotodama handoff contract, not R8–R10). Target evidence is read from `1b09f3f`.

**R8 — evidence replay.** The row's "the R8 terms scanned 0 times" is a baseline claim; replay on the JDEP3-measured revision and on the r89 baseline:

```sh
for t in 'may not land' 'must not ship' 'blocked' 'withhold' 'may remain' 'disposition' 'materiality' 'cross-cluster' 'landed canon' 'another fixture' 'aggregate' 'paraphrase' 'verbatim' 'derivative' 'delivery mode'; do
  printf '%-16s %s\n' "$t" "$(git show 2ea9ef1:corpus/knowledge/r88-sourced-inspiration-decision-table.md | grep -ic -- "$t")"; done
```

```text
may not land 0 / must not ship 0 / blocked 0 / withhold 0 / may remain 0 / disposition 0 /
materiality 0 / cross-cluster 0 / landed canon 0 / another fixture 0 / aggregate 0 /
paraphrase 0 / verbatim 0 / derivative 0 / delivery mode 0
```

The same 12-term subset on `51b286b` is also all-zero. On the delivered table the R8–R10 vocabulary is present: `materiality 2`, `disposition 1`, `re-derive 1`, `external-only / unverified inspiration 1`, `paraphrase 1`, `verbatim 1`, `delivery mode 1`, `cross-cluster 3`, `landed canon 0`.

```sh
python3 - <<'PY'
from pathlib import Path
note = Path('corpus/fixtures/r87-myth-cluster/inspiration-note.md').read_text()
cluster = Path('corpus/fixtures/r87-myth-cluster')
led = Path('corpus/knowledge/reference-ledger.md').read_text()
print('etcsL_locator_present_122_163 =', 'lines 122–163' in note)
print('source_excerpt_md_exists =', (cluster/'source-excerpt.md').exists())
print('ledger_ETCSL_row_present =', 'ETCSL' in led)
print('ledger_external_only_marker =', 'external-only / text not delivered at lore' in led)
PY
sed -n '21p;38p' .ufo/waves/round-88/followup/JDEP3.md
python3 -c "import json; d=json.load(open('.ufo/waves/round-88/followup/JDEP3-probes.json')); print(list(d['probes'].keys()), d['measured_revision'], d['baseline'])"
```

```text
etcsL_locator_present_122_163 = True
source_excerpt_md_exists = False
ledger_ETCSL_row_present = True
ledger_external_only_marker = True
**S1 — rights-blocked real-world source. Classification: uncovered** (citation side covered, element
R4 (`:14`) governs the **citation**: "mark the passage `external-only / unverified` … if text cannot
['S1-rights-blocked-source', 'S2-paraphrased-in-world-excerpt', 'S3-parallel-conflicts-with-landed-canon'] 2ea9ef13a928475b13fd578740ea521bed4bd649 dfd1fbc3711f2b28597d74444819aca91fe6bc31
```

Matches the row's "Baseline probe: locator present, `source-excerpt.md` absent" and its citation targets (`:21-38` = the S1 block; probe key present).

**R9 — evidence replay (durable fixture).** The row tells the integrator to replay the durable R9 fixture; that fixture is `corpus/fixtures/r89-inspiration-paraphrase/`:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r89-inspiration-paraphrase; echo "checker_exit=$?"
grep -nF -- 'moved to the west stair' corpus/fixtures/r89-inspiration-paraphrase/ash-ledger-excerpt.md
grep -n 'Delivery mode\|not delivered / unverified' corpus/fixtures/r89-inspiration-paraphrase/ash-ledger-excerpt.md corpus/fixtures/r89-inspiration-paraphrase/claim-to-excerpt-map.md
```

```text
CLEAN: schema, citations, relations, timeline; 0 violations
checker_exit=0
9:A modern paraphrase says that the keeper later summarized the ledger for the court: the tide-mark had been moved to the west stair.
corpus/fixtures/r89-inspiration-paraphrase/ash-ledger-excerpt.md:3:**Delivery mode:** paraphrase (modern wording; not the source's own text)
corpus/fixtures/r89-inspiration-paraphrase/claim-to-excerpt-map.md:3:| Claim pointer | In-world source | Excerpt path and lines | Delivery mode / author | Anchor | R9 support result |
corpus/fixtures/r89-inspiration-paraphrase/claim-to-excerpt-map.md:7:The underlying Ash-Stair Ledger text is `not delivered / unverified`. …
```

The mode is declared in both excerpt (`:3`) and map (header `:3`, single data row `:5` = `` `paraphrase` `` + author); map pipe-line widths are `[6, 6, 6]`. Independent control of the row's "identical valid JSON with paraphrase vs verbatim excerpt" claim (my own scratch, not the cited probe dir):

```sh
SRC=corpus/fixtures/r89-inspiration-paraphrase
cp -r "$SRC" /tmp/jdep1/r9replay/paraphrase; cp -r "$SRC" /tmp/jdep1/r9replay/verbatim
printf '# Ash-ledger delivered excerpt\n\n**Delivery mode:** verbatim\n\n## Excerpt\n\n> The tide-mark moved to the west stair.\n' > /tmp/jdep1/r9replay/verbatim/ash-ledger-excerpt.md
diff -q /tmp/jdep1/r9replay/paraphrase/entities.json /tmp/jdep1/r9replay/verbatim/entities.json
for m in paraphrase verbatim; do python3 corpus/fixtures/check_bible.py /tmp/jdep1/r9replay/$m; echo "checker_exit=$?"; \
  grep -nF -- 'moved to the west stair' /tmp/jdep1/r9replay/$m/ash-ledger-excerpt.md >/dev/null && echo anchor_match=True || echo anchor_match=False; done
cp -r "$SRC" /tmp/jdep1/r9replay/no-excerpt && rm /tmp/jdep1/r9replay/no-excerpt/ash-ledger-excerpt.md
python3 corpus/fixtures/check_bible.py /tmp/jdep1/r9replay/no-excerpt; echo "no_excerpt_exit=$?"
```

```text
json_identical=True
-- mode=paraphrase: CLEAN … 0 violations / checker_exit=0 / anchor_match=True
-- mode=verbatim:   CLEAN … 0 violations / checker_exit=0 / anchor_match=True
-- control: excerpt file deleted: CLEAN … 0 violations / no_excerpt_exit=0
```

The row's claim reproduces exactly; the deletion control additionally shows the checker never touches excerpt files — root cause visible in the delivered source: `path = directory / (section + '.json')` (`corpus/fixtures/check_bible.py:44`), and the file contains no `excerpt`/`.md`/`glob` token at all. `JDEP3.md:40` = the S2 heading; probe key present.

**R10 — evidence replay.**

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster; echo "r87_exit=$?"
python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-m3-maya-cluster; echo "m3_exit=$?"
python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster corpus/fixtures/r88-m3-maya-cluster; echo "two_dir_exit=$?"
ls corpus/knowledge/ | grep -i 'contradict\|registry'
test -e corpus/knowledge/cross-cluster-contradictions.md && echo PRESENT || echo ABSENT
```

```text
CLEAN: schema, citations, relations, timeline; 0 violations   r87_exit=0
CLEAN: schema, citations, relations, timeline; 0 violations   m3_exit=0
usage: check_bible.py [-h] bible
check_bible.py: error: unrecognized arguments: corpus/fixtures/r88-m3-maya-cluster   two_dir_exit=2
r89-cross-cluster-contradiction.md
ABSENT
```

Both clusters return `CLEAN` alone and the CLI rejects two directories with exit 2, exactly as the row states. The registry scan is the one changed observation vs JDEP3's quoted `none`: on the delivered tree it returns the r89 demo file. The live register destination (`cross-cluster-contradictions.md`) is still absent, and the row describes it as proposed/manual — the row is not falsified, but its quoted scan carries no revision marker (named debt D2). Pointers, per the row's "manually verify both pointers":

```sh
python3 - <<'PY'
import json
from pathlib import Path
c = json.loads(Path('corpus/fixtures/r87-myth-cluster/contradictions.json').read_text())
print('contradictions_ids=', [r.get('id') for r in c])
for ev in json.loads(Path('corpus/fixtures/r87-myth-cluster/timeline.json').read_text()):
    if ev.get('id','').startswith('moon-basin-vow'):
        print(' ', ev['id'], 'place_id=', ev.get('place_id'), 'source_id=', ev.get('source_id'))
print('hypothetical_path_exists=', Path('corpus/fixtures/r89-hypothetical-moon-basin').exists())
PY
sha256sum corpus/knowledge/r89-cross-cluster-contradiction.md
```

```text
contradictions_ids= ['moon-basin-vow-location']
  moon-basin-vow-gate-account place_id= mother-tide-gate source_id= gate-witness
  moon-basin-vow-dune-account place_id= ash-dune-sanctuary source_id= dune-register
hypothetical_path_exists= False
7f56bdd6c7ea78494fff46d5fb9a3800e4d3f3cda95899c3bc4e2223180cb580  corpus/knowledge/r89-cross-cluster-contradiction.md
```

The demo carries `status: unresolved`, both relative cluster paths, both claim pointers per pair, and explicitly refuses to be read as the live register; the hypothetical side is correctly absent and self-labelled. `JDEP3.md:57` = the S3 heading, `:75` = the R7-limit discussion; probe key present.

**Owner names and prospective scoping.** All three rows carry the Owner clause (regex/`grep` extraction of each row; `**Owner:**` count = 3): "**Owner:** the lore lane applies this row at integration; unresolved disputes are appended to `l0-questions.md` for the operator — the row is an editorial screen, never a rights or canon determination." Whitespace-normalized phrase checks against the `Integration notes (r89 closure)` block all return True: `R8–R10 are prospective`; `applies to clusters landed from r89 onward`; `R10's register is created on first real cross-cluster conflict`; `R8 does not retroactively affect the landed Spence row`; `(named debt, r89 ledger)`. Caveat, measured: the named-debt pointer does not yet resolve — `grep -c "Round 89" LOG.md` → `0` (last LOG section is Round 88); the r89 log text exists only as `.ufo/waves/round-89/patches/W2-log-r89.proposal.md` (D5). The working tree's one `l0-questions.md` addition is r89 but concerns the kotodama contract, not R8–R10; no R8–R10 dispute line was appended (correct for prospective rows with no recorded dispute).

**Table parse / row shape (after append).**

```sh
python3 - <<'PY'
from pathlib import Path; import re
raw=[(i+1,l) for i,l in enumerate(Path('corpus/knowledge/r88-sourced-inspiration-decision-table.md').read_text().splitlines()) if l.lstrip().startswith('|')]
cells=lambda l: re.sub(r'\\\|','\x00',l).split('|')[1:-1]
print('pipe_lines=', [n for n,_ in raw]); print('widths=', [len(cells(l)) for _,l in raw])
print('delimiter_rows=', [n for n,l in raw if re.match(r'^\s*\|[\s\-:|]+\|\s*$', l)])
PY
```

```text
pipe_lines= [10, 11, 12, 13, 14, 15, 16, 17, 18, 22, 23, 24]
widths= [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
delimiter_rows= [11]
```

Column shape is consistent — the append added three 6-cell lines and no existing line changed (verified by `git diff 51b286b..1b09f3f -- <table>`: insertion-only `+17` after line 18). But the appended block is structurally separate: main table = lines 10–18 (header + delimiter + R1–R7), appended rows = lines 22–24 with **no header/delimiter**, separated by the `check_bible.py` prose paragraph. Measured with GFM `marked` 18.1.1 (`gfm: true`):

```sh
node /tmp/jdep1/md/render.mjs
```

```text
baseline-51b286b: tables=1 thead=1 tr=8 R8_in_table=false R8_in_paragraph=false header6_present=true
delivered-1b09f3f: tables=1 thead=1 tr=8 R8_in_table=false R8_in_paragraph=true header6_present=true
```

So R8/R9/R10 do **not** render as table rows; they render as a paragraph of pipe-delimited text (D1). The pre-existing table renders identically before/after (1 table, 8 rows), and the sixth header cell still reads `r87 / round-88 evidence and integration check` (D4).

**Harm / attribution checks.** No measured harm to any previously working surface:

```sh
git diff --numstat 51b286b..1b09f3f -- corpus/knowledge/r88-sourced-inspiration-decision-table.md corpus/knowledge/r89-cross-cluster-contradiction.md corpus/knowledge/reference-ledger.md corpus/fixtures/r89-inspiration-paraphrase
git diff 51b286b..1b09f3f -- corpus/fixtures/check_bible.py | grep '^+' | grep -ci 'excerpt\|delivery mode\|inspiration'
git diff --numstat 51b286b..1b09f3f -- corpus/fixtures/r87-myth-cluster | grep -c 'json'
git diff --stat 51b286b..1b09f3f -- corpus/fixtures/r88-m3-maya-cluster
```

```text
19  0  …/r89-inspiration-paraphrase/README.md        17  0  …/r88-sourced-inspiration-decision-table.md
9   0  …/ash-ledger-excerpt.md                       32  0  …/r89-cross-cluster-contradiction.md
7   0  …/claim-to-excerpt-map.md                      1  1  …/reference-ledger.md
1   0  …/contradictions.json
14  0  …/entities.json
1   0  …/relations.json
8   0  …/sources.json
1   0  …/timeline.json
0        (checker diff has no excerpt/inspiration-related additions; the +54/-14 is the C1 cause-repair)
0        (r87 JSON untouched; the 4 netnew files are .md excerpts added by C2)
         (empty: r88-m3-maya-cluster untouched)
```

The new fixture exits 0 (`CLEAN`); the two landed clusters replay `CLEAN` exit 0 as at baseline; the checker change (+54/-14) introduces no excerpt/delivery-mode behaviour, so it does not move any C3 row's meaning. Also unchanged: the r87 local contradiction record byte-identical to baseline (per JDEP3 r89 `14bf96df…`).

**Wait-checks.** Two timestamped 60-second polls of `.ufo/waves/round-89/followup/` (protocol per wave brief): listing md5 `71abf123a67d4fe67bad6f5cdd84ee40` at 04:28:51 and again after 60 s — identical, so no dependency for this seat's fixed target arrived or was needed. Sibling reports read and cited below were already present.

## Findings & named debt

- **Verdict recommendation: depth — improved (bounded).** Every evidence command cited in the R8/R9/R10 rows replays to the cited result; owner clauses and prospective-scoping notes are present as stated; the append is insertion-only and column-consistent (6 cells/row) and harms nothing that previously rendered or passed (baseline render identical; both landed clusters still `CLEAN` exit 0; C3 touched no checker code and no fixture JSON). It is bounded, not unqualified:
  - **D1 (rendering, measured).** The R8–R10 block has no header/delimiter row, so GFM emits it as a paragraph of pipe text — the rows govern but do not render as table rows. Fix: add a header + delimiter row (or fold into the main table).
  - **D2 (evidence freshness).** R10's evidence cell quotes JDEP3's registry scan (`none`) with no revision marker; on the delivered tree the same scan returns `r89-cross-cluster-contradiction.md`. The row text is not falsified (register = proposed/manual; destination still absent), but the quote needs a revision/date marker.
  - **D3 (unexercised R8 marker).** `external-only / unverified inspiration` occurs exactly once in the tree — inside the R8 row itself (`grep -rn` → single hit at the table line 22). The ledger uses a different string (`external-only / text not delivered at lore`), and R4 uses `external-only / unverified`. Corroborated by peer `JDEP2.md:98-99` (three variants, one occurrence each) and `JDEP3.md` (r89). No R8 demo fixture was required by the wave spec, but the marker path has no in-tree example.
  - **D4 (stale column label).** The sixth header cell still reads `r87 / round-88 evidence and integration check` while the new rows carry r89 evidence (and after a D1 fix would sit under no updated header).
  - **D5 (named-debt pointer unresolved at this revision).** The integration note's `(named debt, r89 ledger)` has no target yet: `LOG.md` has no Round 89 section (count 0); only `W2-log-r89.proposal.md` / `W2-scorecard-r89.proposal.md` exist. The r87/r88-cluster annotation debt must land at closure.
- **No harm recorded.** This move does not degrade any axis: the baseline table renders identically, the landed fixtures are untouched and still replay `CLEAN`, and no exit code is attributable to C3 (new fixture exits 0; r87/m3 unchanged). D1–D5 are omissions/deferred pointers, not regressions.
- **Corroboration/divergence vs siblings.** `JDEP3.md` (r89, attacker) independently replays the R10 format and pointer set and rates the R10 row + worked example **improved**, register operability **unprovable-but-better** (no shared referent between landed clusters); `JDEP2.md` rates each row's residual sub-cases uncovered and independently reports the marker-string proliferation (D3) — its findings are about ungoverned sub-cases within a prospective screen, not about the evidence citations this seat audits. `H1/H2/H5/JCAL1/E1/CB1` independently replay the R9 fixture with the same `CLEAN`/anchor result.

## Handoff

- **For the integrator:** record the R8–R10 depth claim as **improved (bounded)** with D1–D5 as the bound. Do not promote to unqualified "improved": D1 is a measured rendering defect on the delivered artifact, and D2/D5 are evidence/pointer hygiene items.
- **Cheapest fixes, in order:** (1) give the R8–R10 block a header + `|---|…` delimiter row and refresh the sixth column label to cover r89 evidence (D1/D4); (2) add a revision marker to R10's quoted registry scan (D2); (3) record the r87/r88-cluster annotation debt in the r89 LOG/SCORECARD so the named-debt pointer resolves (D5); (4) optionally land an R8 rights-blocked demo fixture so the `external-only / unverified inspiration` marker is exercised like R9's (D3).
- **Files written (only these):** `.ufo/waves/round-89/followup/JDEP1.md`, `.ufo/waves/round-89/followup/JDEP1-receipts.json` (replaced an earlier same-seat artifact; its text preserved at `/tmp/jdep1/prior-JDEP1.md`). No tracked corpus file was written; no commit, no push; scratch under `/tmp/jdep1/`.
- **Not done / left open:** the r89 LOG/SCORECARD entry does not exist yet, so the named-debt landing could not be verified as resolved (measured absent, D5); I did not re-run the corpus-wide C1/C2 census/delta (other seats own those); R8's marker path and R9's non-paraphrase modes remain unexercised in-tree (D3; `JDEP2` D-JDEP2-3/4).
