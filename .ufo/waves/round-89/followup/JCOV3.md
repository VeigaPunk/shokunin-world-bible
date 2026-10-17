# JCOV3 — Coverage judge #3 (R9/R10 demo verification)

Subject: the delivered R9 demo fixture `corpus/fixtures/r89-inspiration-paraphrase/` and
the delivered R10 record demo `corpus/knowledge/r89-cross-cluster-contradiction.md`, on
the DELIVERED tree HEAD `1b09f3ff8016b26a2259e086f673d0112f4f54e5` (baseline `51b286b`).
`git status --porcelain --untracked-files=no` was empty at probe time. Checker
`corpus/fixtures/check_bible.py` sha256 `e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556`
(this is the C1-revised checker, not the r88 hash `dcacffd6…`). Per-file fixture hashes,
the demo hash, and every raw probe output are in `followup/JCOV3-probes.json`.

## Work performed

- Read both delivered artifacts, the delivered R9/R10 rows of
  `corpus/knowledge/r88-sourced-inspiration-decision-table.md` (the normative source of
  both rules), the delivered `corpus/fixtures/r87-myth-cluster/` (the R10 demo's
  "existing side"), and the D3/R1/D2 wave reports that drafted them.
- Mechanically audited the R9 fixture against the R9 rule as written: delivery mode
  declared in the excerpt **and** the map, paraphrase author named, path/line pointer,
  anchor equality with the claim, and the `not delivered / unverified` status — the
  question my block asks ("verify the fixture's README + map state the rule").
- Mechanically audited the R10 demo against R10's seven named record elements: stable
  ID, both relative cluster paths, both claim pointers (file + event ID + field),
  conflicting assertions, cited in-world sources, "why they cannot both be true as
  stated", and status `unresolved` — plus a cross-check that the demo's quoted
  statements are verbatim copies of the delivered r87 timeline and that its pointers
  actually resolve.
- Ran 6 recorded probes (positive replay, anchor grep, a scratch verbatim control,
  underlying-wording scan, R10 pointer resolution, r87 replay). All probes ran against
  `/tmp/jcov3-r89/` scratch or the delivered tree; the repository was written only by
  this seat's two followup files. `/tmp` was inode-exhausted at start (100 free inodes of
  1M), so the scratch footprint was kept to a 7-file twin; no other seat's scratch was
  touched.

## Before → after measurements

All checker invocations are `python3 corpus/fixtures/check_bible.py <dir>` with cwd =
`lore-shokunin/`, matching each artifact's own README replay line.

**Baseline absence (before).** Exact command:

```sh
git ls-tree -r --name-only 51b286b -- corpus/fixtures/r89-inspiration-paraphrase corpus/knowledge/r89-cross-cluster-contradiction.md | wc -l
git show 51b286b:corpus/knowledge/r88-sourced-inspiration-decision-table.md | grep -c -i 'paraphrase'
git show 51b286b:corpus/knowledge/r88-sourced-inspiration-decision-table.md | grep -c -i 'cross-cluster'
grep -c '^| R8 —\|^| R9 —\|^| R10 —' corpus/knowledge/r88-sourced-inspiration-decision-table.md
```

Observed: baseline tracked count `0`; baseline table `paraphrase`=0, `cross-cluster`=0;
delivered table R8/R9/R10 rows=3. Both artifacts and both governing rows are new at
`1b09f3f`.

**R9 fixture — delivered positive replay + anchor (P0/P1).** Observed:

```text
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
9:A modern paraphrase says that the keeper later summarized the ledger for the court: the tide-mark had been moved to the west stair.
grep exit=0
```

The anchor `moved to the west stair` matches at `ash-ledger-excerpt.md:9`, which is the
line the map's pointer `ash-ledger-excerpt.md:9` names. The same phrase also occurs in
`entities.json` (the claim) — the fixture deliberately makes claim and excerpt share it.

**R9 fixture — rule statement audit (README + map).** Exact command: the `R9` block of
`followup/JCOV3-probes.json`'s generating script; observed `R9_rule_statements=7/7`:

```text
readme_mode_paraphrase=True
readme_retelling_existence_only=True
readme_underlying_not_delivered=True
readme_anchor_lexical_preflight=True
map_supports_only_existence=True
map_marks_fail=True
map_mode_declared=True
```

The README states the rule in R9's own terms — "a paraphrase … documents only the
existence of the retelling, and its anchor only proves that the phrase occurs in the
paraphrase" — and the map's `R9 support result` cell reads `Fails: …`. Both the excerpt
(`**Delivery mode:** paraphrase (modern wording; not the source's own text)`) and the
map (`| `paraphrase`; fixture writer (R9 demonstration) |`) declare the mode.

**R9 — discrimination control (P2), scratch twin.** A fresh 7-file verbatim twin
(same JSON, same anchor, `**Delivery mode:** verbatim`, map cell flipped to `Passes`)
returns the identical checker result and the identical anchor:

```text
CLEAN: schema, citations, relations, timeline; 0 violations   (exit 0)
7:“The tide-mark moved to the west stair.”                    (anchor exit 0)
```

Conclusion: the checker does **not** discriminate paraphrase from verbatim (D2 measured
this too). The delivered fixture's discrimination is therefore **declarative** — carried
by the mode/author/status metadata and the map's `Fails` verdict, not by any mechanical
check. The README already says exactly this ("The checker is structural only; its
expected `CLEAN` result does not establish excerpt fidelity or prose support"), so the
artifact does not overclaim its own mechanism. The fixture does its intended job: it
pins the case where a matching anchor coexists with a failed source-text support check.

**R9 — underlying source wording is genuinely undelivered (P3).** Scan of every file in
the fixture for the source's own wording found only `entities.json` containing the
substring `Ash-Stair Ledger records` — i.e. the *claim about* the source, not the
source's own text. No file delivers the Ash-Stair Ledger's own words. The
`not delivered / unverified` label is factually correct for this fixture.

**R10 demo — seven-element format audit.** Exact command: the `R10` block of the probe
script; observed `R10_spec_elements_present=17/17`. Every R10-named element is present
and the demo's claims are grounded in the delivered corpus:

```text
1_stable_id=True                         (Record: `r89-demo-moon-basin-vow-cross-cluster`)
2_path_existing=True                     (`corpus/fixtures/r87-myth-cluster/`)
2_path_hypothetical=True                 (`corpus/fixtures/r89-hypothetical-moon-basin/`)
3_ptr_hara_file_plus_event_field=True    (…/timeline.json#moon-basin-vow-gate-account.place_id)
3_ptr_sen_file_plus_event_field=True     (…/timeline.json#moon-basin-vow-dune-account.place_id)
3_ptr_hypo_file_plus_event_field=True    (…/timeline.json#moon-basin-vow-river-account.place_id)
4_assert_hara=True / 4_assert_sen=True / 4_assert_hypo=True
5_src_gate_witness=True / 5_src_dune_register=True   (both resolve in r87 sources.json)
6_why_x2=True                            (two "Why they cannot both be true as stated:")
7_status_unresolved=True                 (Status: `unresolved` twice)
x_stmt_hara_verbatim=True                (r87 timeline description appears verbatim)
x_stmt_sen_verbatim=True
x_local_record_named=True                (contradictions.json#moon-basin-vow-location exists)
x_hypo_fixture_absent=True
```

**R10 — pointer resolution against the delivered corpus (P4/P5).** Observed:

```text
gate_account_exists=True  gate_place_id=mother-tide-gate   gate_source_resolves=True
dune_account_exists=True  dune_place_id=ash-dune-sanctuary dune_source_resolves=True
local_ledger_row_exists=True
hypo_fixture_absent=True
live_register_absent=True
r87 cluster replay: CLEAN: schema, citations, relations, timeline; 0 violations (exit 0)
```

The two real pointers resolve to the r87 events and their `source_id`s resolve to
`gate-witness` / `dune-register`; the hypothetical fixture is absent as the demo states;
the live register `corpus/knowledge/cross-cluster-contradictions.md` is correctly absent
(R10 is prospective). The demo's "existing side" still replays clean.

## Findings & named debt

**Verdict recommendation — coverage (R9/R10 demo sub-scope): improved (bounded).**
Both delivered demos meet the rules they demonstrate on the delivered tree. The R9
fixture is a self-consistent, structurally clean negative demo whose README and map
state the R9 rule in R9's own terms (7/7 statements); its anchor matches at the declared
line and its underlying text is genuinely undelivered. The R10 record carries all seven
elements R10 names (17/17 checks) and its claims are grounded verbatim in the delivered
r87 cluster. The bound is that neither demo is mechanically discriminated by the
checker (the R9 discrimination is declarative by design; the R10 demo is hypothetical
and its register is not yet created), which both artifacts state explicitly — so this is
a genuine coverage improvement over the `51b286b` baseline where neither artifact nor
either governing row existed.

**D1 (named debt): the R9 decision-table row does not name its own fixture path.**
`corpus/knowledge/r88-sourced-inspiration-decision-table.md:23` ends the R9 evidence
cell with "replay the durable R9 fixture and inspect the underlying text/translation
where applicable" but never writes `corpus/fixtures/r89-inspiration-paraphrase`. The
fixture's path appears only inside the fixture's own README. By contrast the R10
integration note names its demo path (`…/r89-cross-cluster-contradiction.md`). A future
integrator reading the R9 row cannot locate the fixture without a filesystem search.
Fix: add the path to the R9 row's evidence cell (one substring), or accept the
asymmetry as intentional. Documentation parity only; no rule is wrong.

**D2 (named debt, carried from r88 D4): the fixture index is not updated.**
`corpus/fixtures/README.md`'s highest section is `## Round 88: stop-cause disclosure +
second cluster`; there is no Round 89 section, and none of the 11 delivered `r89-*`
fixture directories is registered. The r88 JCOV3 carried this same debt forward at
`2ea9ef1`; it is still open at `1b09f3f` and is now larger. Command:

```sh
grep -n '^## ' corpus/fixtures/README.md | tail -3
grep -c 'r89' corpus/fixtures/README.md
```

Observed: last sections `## Round 83 …`, `## Round 87 …`, `## Round 88 …`; `r89` mention
count `0`.

**D3 (precision, not a coverage loss): the R10 demo is a format example with a
non-existent second cluster.** R10's register-entry schema presumes two *landed* cluster
paths; the demo's second path (`corpus/fixtures/r89-hypothetical-moon-basin/`) does not
exist. The demo marks this repeatedly ("hypothetical; absent from this repository";
"does not satisfy R10's landed-cluster trigger") and warns "Do not treat this demo as an
append to that register", so no reader is misled. The residual risk is naming: the demo
file is `r89-cross-cluster-contradiction.md` (singular) while the live register is
`cross-cluster-contradictions.md` (plural). The demo disambiguates in its first
paragraph, but the singular/plural pair is a cheap confusion trap. Consider a
`demo-` prefix or a leading `<!-- DEMO -->` marker if this matters at integration.

**Not this seat's to fix.** C1's cause-branch fixtures (`r89-c1-*`, `r89-f2-*`,
`r89-fn2-*`) and the 160-vs-161 fixture-directory census are the calibration lane's
subject; I only enumerated the `r89-*` dirs to establish that the R9 fixture is present.
C2's excerpt-delivery work on the r87 cluster is outside this seat; I replayed the r87
cluster only as the R10 demo's existing side.

## Handoff

- Deliverables: `followup/JCOV3.md` (this file) and `followup/JCOV3-probes.json`
  (6 probe records with exit codes, verbatim output, checker/demo/fixture hashes, and the
  R10 pointer-resolution result). No other repo writes; no commit, no push.
- Reproduction: the probe script is reproduced inline in the "Work performed" flow;
  the scratch twin lives at `/tmp/jcov3-r89/twin` and the consolidated receipts at
  `/tmp/jcov3-r89/receipts.json` (already copied into the repo as `JCOV3-probes.json`).
  Deleting `/tmp/jcov3-r89` loses nothing not recorded in the JSON. Note: a stray
  untracked `corpus/fixtures/__pycache__/check_bible.cpython-314.pyc` appeared during my
  session (created by an `import check_bible`, which neither the checker's own direct
  invocation nor any in-repo script performs — most likely a concurrent sibling seat's
  scratch script); I removed it as a regenerable build artifact. Final `git status
  --porcelain` shows only `?? .ufo/waves/round-89/followup/`, and `git diff --stat` is
  empty (no tracked changes).
- Gaps for the parent: (a) my block specified two 60-second wait-checks, but the wave is
  already committed (`1b09f3f`, tree clean), so no dependency was outstanding and no wait
  was needed — all judging inputs existed at HEAD; (b) I did not need any sibling seat's
  verdict; (c) I compared the delivered tree only — no patch-vs-delivered drift is
  claimed (D3/R1 wave reports already did the scratch-apply parity).
- Suggested follow-ups, in cost order: (D1) name the fixture path in the R9 row
  (one substring); (D2) open a `## Round 89` section in `corpus/fixtures/README.md`
  registering the 11 `r89-*` fixtures (carried debt); (D3) decide whether the singular
  demo filename needs disambiguation.
