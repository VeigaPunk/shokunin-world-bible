# JCOV1 — Coverage judge #1 (support completeness)

Delivered tree judged: `1b09f3ff8016b26a2259e086f673d0112f4f54e5` (baseline `51b286b`). All
verdict evidence below was taken from the delivered tree; `/tmp` held only baseline
replays and the baseline checker copy. No commit, no push, no sibling-repo writes.
Machine receipts: `followup/JCOV1-probes.json`.

Dependencies: the seat block named two 60s wait-checks. Nothing was waited on — every
artifact this seat judges (the four delivered r87 excerpts, `patches/S2-fact-map.json`,
`check_bible.py`, `reference-ledger.md`, the decision table) is present in the delivered
tree, so there was no peer artifact to await. No gap is left by skipping the waits.

## Work performed

- Re-ran every one of the 14 anchor greps from `.ufo/waves/round-89/patches/S2-fact-map.json`
  against the delivered excerpt for that row's `source_id`, using the D1 rule's own form
  (`grep -nF -- '<anchor>' <excerpt-path>`), and recorded `path:line` for each hit.
- Resolved the six fact-map entity `first_appearance` pointers: checked the pointer's
  `source_id` against `sources.json`, the existence of `<source_id>-excerpt.md`, that the
  pointer equals the entity's claim `source_id`, and that the entity's naming anchor
  matches in that excerpt.
- Independently replayed the D1 support rule over the whole r87 cluster (22 source-attributed
  facts: 7 pointers, 7 entity claims, 4 relation edges, 4 timeline events) rather than
  trusting the `M4-verify.json` composition, and replayed the structural checker.
- Compared baseline vs delivered `check_bible.py` exit codes over every baseline fixture
  directory, and recomputed the fixture-dir delta.
- Adjudicated the R3 pledge boundary at whole-claim scope: read the delivered watch clause,
  its disclaimer line, the `sources.json` reliability note, the cluster README, and swept the
  tree for any performance-framed wording.
- Replayed the probe command recorded in `M4-verify.json` to test whether its `after` numbers
  reproduce, and checked documentation parity for the cluster and the rule table.

## Before → after measurements

Command (anchor sweep; full output in `JCOV1-probes.json` M1):

```sh
python3 - <<'PY'
import json, subprocess
d=json.load(open('.ufo/waves/round-89/patches/S2-fact-map.json'))
root='corpus/fixtures/r87-myth-cluster'
hits=0
for f in d['facts']:
    p=f'{root}/{f["source_id"]}-excerpt.md'
    r=subprocess.run(['grep','-nF','--',f['anchor_phrase'],p],capture_output=True,text=True)
    hits += r.returncode==0
    print(f'{f["id"]:3} rc={r.returncode} {p}:{r.stdout.strip()}')
print(f'ANCHORS {hits}/14')
PY
```

Observed: all 14 rows `rc=0`, `ANCHORS 14/14`. Locations:

| id | excerpt path:line |
|---|---|
| E1 | `gate-witness-excerpt.md:5` |
| E2 | `dune-register-excerpt.md:5` |
| E3 | `dune-register-excerpt.md:6` |
| E4 | `shell-charter-excerpt.md:7` |
| E5 | `shell-charter-excerpt.md:8` |
| E6 | `tide-bell-tally-excerpt.md:9` |
| R1 | `shell-charter-excerpt.md:9` |
| R2 | `shell-charter-excerpt.md:10` |
| R3 | `shell-charter-excerpt.md:11` |
| R4 | `dune-register-excerpt.md:7` |
| T1 | `gate-witness-excerpt.md:6` |
| T2 | `tide-bell-tally-excerpt.md:10` |
| T3 | `gate-witness-excerpt.md:7` |
| T4 | `dune-register-excerpt.md:8` |

Baseline replay (same command, excerpts replayed from `51b286b` via `git show`):
`BASELINE 51b286b anchors=0/14` — the four target excerpt files did not exist; only
`lowwater-hymn-excerpt.md` was delivered.

Pointers: `POINTERS RESOLVED 6 /6`, each with `in_sources=True excerpt_exists=True
claim_src==fa:True anchor_rc=0` (`hara`→`gate-witness:5`, `sen`→`dune-register:5`,
`ash-dune-sanctuary`→`dune-register:6`, `shellweavers`→`shell-charter:7`,
`reedwardens`→`shell-charter:8`, `reed-bell`→`tide-bell-tally:9`). Baseline:
`BASELINE pointers with delivered excerpt=1/7` (only the seventh pointer,
`mother-tide-gate`→`lowwater-hymn`, had a delivered excerpt).

Independent D1-rule replay over all 22 facts:
`D1-rule facts=22 supported=22 unsupported=0` (all 7 pointers resolve with a delivered
excerpt; all 7 entity claims, 4 relations and 4 timeline events carry a matching anchor —
the hymn claim at `lowwater-hymn-excerpt.md:3`).

Structural replay:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster; echo "exit=$?"
```

Observed: `CLEAN: schema, citations, relations, timeline; 0 violations` / `exit=0`.
Same result and same exit at baseline, so the r89 change is exit-neutral for the cluster.

No-regression sweep (baseline checker copy vs delivered checker, all 149 baseline dirs):
`(no CHANGED lines) comparison done` — 0 exit-code changes. Fixture-dir delta: 149 → 160
dirs, 11 new dirs, and inside `corpus/fixtures` exactly 1 modified file (`check_bible.py`)
plus 4 added files (the r87 excerpts), consistent with the C1 "4 changed + 11 new of 160
dirs" delta.

ETCSL ledger marker: `reference-ledger.md:8` fourth cell now reads
`external-only / text not delivered at lore; citation is a research lead with verified line
locators, not delivered support.` The four-column header and the three separate
question cells are intact.

Whole-claim review (not just lexical): each anchor sentence is the sentence the JSON claim
is drawn from — E1/E2 self-identification, E3 the register's "Place of keeping" line, E4/E5
the two signatory lines, E6 the tally's carried-bell entry, R1/R2 the reciprocal alliance
clauses, R4 the register's keeping line, T1 the gate-witness sounding, T2 the tally's
return entry (framed as a tally record, matching the fixture-local-ordering note), T3/T4
the two tick-3 vow accounts. No anchor was used to support a claim wider than its sentence.

R3 pledge boundary: the delivered watch clause is `shell-charter-excerpt.md:11`
`Watch clause: Under this charter's pledge, Shellweavers keep watch with the Reed Bell.`
The tree contains exactly two "keep watch" surfaces — that line and the `keeps_watch_with`
relation type at `relations.json:17` — and no delivered text upgrades the pledge to
performed conduct. The boundary is carried by three further surfaces:
`shell-charter-excerpt.md:13` ("it records a pledge, not its performance"),
`sources.json:6` ("it records a reciprocal pledge, not whether either faction kept it"),
and `README.md:3` ("a reciprocal Shellweaver–Reedwarden pledge"). Whole-claim scope holds:
the relation edge records the charter's pledged watch relation, not fulfilled history. This
resolves the S2-R3 debt, whose M3 candidate line (`This charter assigns Shellweavers to keep
watch with the Reed Bell`) was less explicit about pledge scope than the delivered M4 line.

## Findings & named debt

Verdict recommendation — **C2 coverage: improved (bounded).**

- Improved on measurable fronts: 0/14 → 14/14 delivered anchors; 1/7 → 7/7 first-appearance
  pointers with a delivered excerpt; 8 → 22 D1-rule-supported facts under an independent
  replay; the ETCSL ledger row carries the external-only marker. Nothing on the coverage
  axis is traded away: the r87 cluster exits 0 before and after, and 0 exit changes across
  the 149 baseline fixture dirs, so the support work is exit-neutral corpus-wide.
- Bounded by four debts below. None of them falsifies the coverage claim; each is a
  record-completeness or reproducibility gap.

1. **JCOV1-D1 — the 22/22 receipt does not reproduce from its own command.** Replaying the
   exact command stored in `.ufo/waves/round-89/patches/M4-verify.json`
   (`before.d1_support.command`) against the delivered tree prints
   `D1 r87 delivered: facts=22 OK=8 not-OK=14`. That probe counts pointer support as
   "`source_id` resolves in `sources.json`" and entity-claim support as literal
   `statement in prose[source]`, which no delivered excerpt contains; it therefore yields 8
   both before and after. `M4-verify.json`'s `after.facts_supported: 22` is a hand-composed
   8 + 14. The number is *true* (see the independent replay above), but the wave's own
   receipt for it is not a single reproducible command. Fix: replace the probe with a
   per-fact anchor map, or record the 22 as an explicit composition (probe 8 + checks-array
   14) and say so.
2. **JCOV1-D2 — r87 cluster README not updated at its r89 content touch.** `README.md` is
   unchanged from baseline; line 7 still names only `lowwater-hymn-excerpt.md` and
   `symbolism-clause-map.md`, so the four newly delivered excerpt files are unlisted, and
   line 3 still describes only the two `allied_with` edges, not the `keeps_watch_with` edge.
   The second half predates r89; the unlisted excerpts are new at r89.
3. **JCOV1-D3 — decision-table row-5 evidence cell is stale.** The r89 diff to
   `corpus/knowledge/r88-sourced-inspiration-decision-table.md` adds only the R8/R9/R10 rows,
   the Integration boundary section, and the r89 integration notes. The row-5 evidence cell
   (line 16) still reads "M4's repoint patch cites `gate-witness` metadata but delivers no
   witness excerpt", and its closing instruction "Recheck the selected cluster's
   claim-to-excerpt map at integration" has no recorded outcome, although the delivered tree
   does deliver that witness excerpt. The r87 claim-to-excerpt map lives in the wave artifact
   `patches/M4-verify.json`, not in the cluster (unlike the new
   `corpus/fixtures/r89-inspiration-paraphrase/claim-to-excerpt-map.md`).
4. **JCOV1-D4 — no R9 delivery-mode declaration on the r87 excerpts.** The delivered r87
   excerpts declare provenance ("newly authored fictional … the source record calls it
   unverified") but not a delivery mode; `grep -rn "Delivery mode\|verbatim\|paraphrase\|summary"
   corpus/fixtures/r87-myth-cluster/` returns nothing. The table's own integration note defers
   r87/r88 to "their next content touch (named debt, r89 ledger)", and r89 is such a touch,
   so the deferral needs to be re-stated in the r89 closure record or discharged. Related
   minor staleness: `S2-fact-map.json`'s `anchor_basis` still says patch M3 and "candidate
   excerpt text only; not applied to the cluster", while the delivered shell-charter wording
   is M4's (only the R3 row's `anchor_note` records the M4 update).

Not a coverage finding: the two tick-3 vow accounts still disagree on place and remain
unresolved — `contradictions.json` is unchanged and the R10 worked example
(`corpus/knowledge/r89-cross-cluster-contradiction.md`) keeps its second cluster explicitly
hypothetical, so it adds no r87 canon and no cross-cluster pointer into the fixture-local
ledger.

## Handoff

Verdict to rule: **C2 coverage — improved (bounded)**, on the strength of 14/14 delivered
anchors, 6/6 pointers, an independently replayed 22/22 D1-rule result, an exit-0 r87 cluster,
0 exit changes over the 149 baseline dirs, and the ETCSL external-only marker. Carry the four
debts (JCOV1-D1…D4) into the round record: D1 as a receipt-reproducibility fix, D2/D3 as
documentation parity for the touched cluster and the rule table, D4 as the R9 delivery-mode
deferral that the r89 ledger must re-state or discharge. The rule verdict itself is unaffected
by the debts — but the coverage claim should not be cited from `M4-verify.json`'s `after`
block alone, since that block's number is not what its own command prints.

Files written by this seat (no other tracked writes): this report and
`followup/JCOV1-probes.json`.
