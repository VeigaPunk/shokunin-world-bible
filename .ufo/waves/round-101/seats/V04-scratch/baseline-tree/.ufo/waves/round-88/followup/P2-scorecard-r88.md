# PROPOSAL ONLY — Round 88 SCORECARD section (seat P2)

Do not append to `SCORECARD.md` without L1 adoption. Built from follow-up
evidence on the DELIVERED tree at `2ea9ef1` (baseline `dfd1fbc`, tree clean).
All numbers are P2's own re-measurements; the follow-up seat reports are used
only as corroboration and are named where they disagree with each other.

Seat reports landed by the end of P2's work (third availability snapshot, after
the two specified 60-second wait-checks): `E1-message-inventory.json`,
`H2-delta.json`, `JCAL1-delta.json`, `JCAL3-receipts.json`, `JCAL5.md` +
`JCAL5-delta.json`, `JCOV1-measurements.json`, `JCOV2-support.json`,
`JCOV3-probes.json`, `JCOV5.md`, `JDEP1.md`, `JDEP2.md`, `JDEP3.md` +
`JDEP3-probes.json`, `JDEP4.md` + `JDEP4-drift.json`, `JDEP5-receipts.json`,
`K1.md`, `P4-shonen.md`, `V2.md`. Only `JDEP2.md` and `V2.md` existed at the
second wait-check; the rest arrived later and are marked as later arrivals, not
as an integration event.

**All three LIVE cells stay `PENDING-L1`** — see the conflict and the trade
below. Scores remain unassigned: no bounded 0–10 rubric is in evidence; counts
and exit codes are measurements, not scores or verdicts.

---

## Round 88 — luna round 2 of 12 (2026-10-17)

Two-wave regimen round: work wave (35 seats + 2 supplementary,
`openai-codex/gpt-6-luna-max`), follow-up wave (32–64 seats,
`hyper/deepseek-v4.1-flash`); evidence under `.ufo/waves/round-88/` (work) and
`.ufo/waves/round-88/followup/` (judging). Baseline `dfd1fbc`; work commit
`2ea9ef1` (103 files, 29 added / 5 modified outside `.ufo/`). Round record in
this section's commit. Scores remain unmeasured — every row below is a claim
carrying its counting command and measured commit.

| LIVE axis | r88 verdict | Evidence and limit |
|---|---|---|
| calibration | **PENDING-L1** | C1 `2ea9ef1` replaces the holder-only latch with first-stop cause tracking in `corpus/fixtures/check_bible.py` (+59/−20). Three r87 residuals are closed on the delivered tree: (i) `r87-probe-shape-ambiguous` 2 → 5 findings, the shape-invalid dict now arms the stop and names the combined cause; (ii) `r88-mixed-stop` names the unknown source at `[0]` as first cause at `[0]`–`[2]`, never the later ambiguity at `[1]`; (iii) `r88-nonholder-stop` discloses at `[0]`–`[2]` with no holder ambiguity present. Closure census: 149 dirs (was 145), exits `0=31 / 1=118`, 367 violation lines (baseline-145 subset 352), 0 stderr cases, **9 changed tuples + 4 new, 0 exit changes**; 2 of the 9 are pre-r87 (`r61-independent-empty`, `r61-independent-unavailable`). Corroboration: `JCAL1`, `JCAL5` and `H2` independently reproduce `9 changed / 4 new / 0 exit changes` (JCAL5 with a regenerated baseline byte-identical to `B1-tuples.json`); `V2` verifies all three fixture READMEs line-by-line and shows each fixture discriminates against the baseline checker; `JCAL5`'s sweep finds 47 disclosure lines, 0 qualifier omissions, 0 coverage gaps, 0 causal `because` strings. Bounds: disclosure is per-entity provenance chain, not global; non-dict records cannot carry an ambiguous holder id (stated bound in the commit); the dangling-holder cause has **no durable fixture** (`JCAL5` D-2); combined same-record causes are demonstrated only on shape-invalid records (`JCAL5` D-3); chain-level origins are labelled `entities[i].provenance` while record-level origins carry `[k]` (`JCAL5` D-4). |
| coverage | **PENDING-L1** | C2 `2ea9ef1`: `corpus/fixtures/r88-m3-maya-cluster/` (K'iche/Maya via Spence 1913, printed p. 209, delivered English excerpt, passage locator, clause→element map, occupied-slot near-miss at tick 9 with distinct actors/places) + OBS-1 repair to `corpus/fixtures/r87-myth-cluster/` (hymn line now carries `at the Mother-Tide Gate`, the attributed claim narrowed to "places the shell ring and bowl at", clause map 7 → 8 rows). Counting: `find corpus/fixtures -name inspiration-note.md \| wc -l` → **2** (baseline 1); `ls -d corpus/fixtures/*/ \| wc -l` → **149** (baseline 145); both cluster replays → `CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0; OBS-1 clause replay **8/8 exact** clause matches against the delivered excerpt. Bounds: the new Maya cluster's own map is **1/2 exact** clause matches on the delivered tree — the map quotes `“He called out ‘Earth,’”` while `source-excerpt.md` delivers `“Earth”`; the round's own decision-table rule requires a fixed-string anchor, so this is a live inconsistency between two artifacts in the same commit (`JDEP1` debt 3, `JDEP3`, Q1/T1/D2 pre-integration; unresolved). `corpus/fixtures/README.md` still has **0** `Round 87`/`Round 88` sections (`JCOV5` D-JCOV5-2; carried D-C3-012). `JCOV5` also carries the absent kotodama↔lore handoff contract (D-JCOV5-1). |
| depth | **PENDING-L1** | C3 `2ea9ef1`: new `corpus/knowledge/r88-sourced-inspiration-decision-table.md` (added file) with the R1B scope note in an HTML comment, and `corpus/knowledge/reference-ledger.md` gains the r87 ETCSL row. Counting: `grep -c '^\|' corpus/knowledge/reference-ledger.md` → 6 table lines = header + separator + **4 data rows** (baseline 3); `git diff --numstat dfd1fbc..2ea9ef1 -- corpus/knowledge/reference-ledger.md` → `3  2`; row-only diff is a pure append (`5a6`), all three prior rows md5-identical, header/separator untouched. The ETCSL row's `lines 122–163` locator was verified against the live ETCSL page and matches `seed.md:26–29`'s three-separate-questions contract. **Judge conflict (recorded, not averaged):** `JDEP1` recommends `improved` with `unprovable-but-better` as the strict-spec alternative, and `JDEP3` recommends `improved (bounded)`; `JDEP4` recommends **`harmed` (bounded)** for checker-semantics fidelity of two pre-existing `corpus/knowledge/` docs — see the trade row below. Bounds: the **Spence reference with a delivered excerpt is not registered** in the ledger (grep `Spence` → 0) while the external-only ETCSL reference is (`JDEP1` debt 1, `JDEP2` F2); the ETCSL row omits the table's own requested delivery-status / `external-only / unverified` marker (`JDEP2` F3); the table's rows 1/4/5/7 cite M1/M2 evidence that does not exist on the delivered tree (`JDEP1` debt 2); row 5 carries the 1/2 clause overclaim (`JDEP1` debt 3); the table file still opens `Draft destination: …`; the r87 cluster's metadata-only support state (`1/7` entity claims, `1/7` first-appearance, `0/4` edges, `0/4` events) is undisclosed by the table (`JDEP1` debt 5). |
| **documentation parity** | **harmed (bounded)** — the round's trade | Two tracked knowledge docs that state the checker's provenance contract and paste its verbatim outputs were **not refreshed** by the C1 semantic replacement: `git diff --stat dfd1fbc 2ea9ef1 -- corpus/knowledge/holder-assessment-boundary.md corpus/knowledge/r87-provenance-chain-decision-table.md` → empty (0 lines changed). Measured drift: `grep -c 'first occurred at' corpus/fixtures/check_bible.py` → **0**, while `holder-assessment-boundary.md` → **8** and `r87-provenance-chain-decision-table.md` → **17** (and `at this and all later records` → 6 / 9 respectively). Replaying the boundary doc's own pasted command block: `python3 corpus/fixtures/check_bible.py corpus/live/runs/round-85/probe-inputs/<case>` → `r85-control` 0 findings rc=0, `r85-unique-break-control` 1 rc=1, `r85-masked-ambiguous` **4** rc=1, `r85-isolated-ambiguous` **3** rc=1, `r85-harbor-repro` **6** rc=1 — the doc's "Observed output (verbatim)" states 5 / 4 / 7. The boundary doc's census line (`:318`) says "nine fixture directories containing `provenance`, none does [combine with a duplicated holder id]"; measured on the delivered tree: **19** provenance-bearing dirs, **9** also carrying a duplicate entity id (`JDEP4` measures 8 with a narrower criterion). The docs pin their own snapshot commit (`2b48ca7`) so they are not fabrications, and no checker or test consumes them — the harm is that the lane's stated behavioral contract contradicts the shipped checker, and one line (the census) would misdirect an editor sizing the regression surface. Independent findings: `JCAL5` D-1, `JDEP4` F1/F2/F5. |

**Trade rule applied.** A trade anywhere is not an improvement. While these two
in-repo contract docs describe a checker the tree no longer ships, no axis above
can be recorded as a clean improvement for the round as a whole, and the round is
not a clean improvement until they are refreshed. That is why every cell stays
`PENDING-L1`: the honest r88 record is "C1/C2/C3 improve the measured surfaces,
and the round simultaneously harms documentation parity". L1 may still admit the
round with the trade named; it may not record an unqualified improvement.

### Per-claim before → after rows (measured commits)

| # | claim | before (`dfd1fbc`) | after (`2ea9ef1`) | counting command |
|---|---|---|---|---|
| C1-a | fixture-dir census + tuple deltas | 145 dirs, exits `0=30 / 1=115`, 331 violation lines, 0 stderr | 149 dirs, exits `0=31 / 1=118`, 367 lines (baseline-145 subset 352), 0 stderr | see census block below |
| C1-b | tuple preservation | — | `changed=9  new=4  missing=0  exit_changes=0` | same census block |
| C1-c | r87 shape-ambiguous residual | `r87-probe-shape-ambiguous` → 2 findings, 0 `unassessed` lines | → 5 findings, 2 disclosures naming `malformed record (unexpected field set); ambiguous holder identity to_holder 'dup' at entities[5].provenance[0]`, exit 1 | `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-probe-shape-ambiguous` |
| C1-d | mixed-stop first-cause attribution | (baseline checker, same fixture files) `[1]`/`[2]` blame the later ambiguity; `[0]` silent | `[0]`–`[2]` all name `unknown source 'f1-mixed-missing-source' at entities[5].provenance[0]`; exit 1 | `python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-mixed-stop` (baseline control in `followup/V2.md`) |
| C1-e | non-holder stop disclosure | unknown-source-only stop emits 1 finding, no disclosure | 4 findings; disclosures at `[0]`–`[2]`; exit 1 | `python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-nonholder-stop` |
| C1-f | r87 duplicate-notice polish debt | stop record emitted two near-duplicate notices | one disclosure per record (2 records → 2 `unassessed` lines) | `python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-shape-ambiguous-armed \| grep -c unassessed` → 2 |
| C2-a | inspiration-note files | 1 | 2 | `find corpus/fixtures -name inspiration-note.md \| wc -l` |
| C2-b | fixture dirs | 145 | 149 | `ls -d corpus/fixtures/*/ \| wc -l` |
| C2-c | cluster replays | r87 cluster CLEAN | both clusters `CLEAN … 0 violations`, exit 0 | `python3 corpus/fixtures/check_bible.py corpus/fixtures/{r87-myth-cluster,r88-m3-maya-cluster}` |
| C2-d | OBS-1 repair | hymn lacked the Gate; clause map 7 rows; attributed claim was "names the Mother-Tide Gate as a shore threshold" | hymn line carries `at the Mother-Tide Gate`; map 8 rows; claim narrowed; **8/8** exact clause matches | `git diff dfd1fbc 2ea9ef1 -- corpus/fixtures/r87-myth-cluster/`; clause replay script (see P2.md) |
| C2-e | Maya map exact-anchor consistency | n/a (new) | **1/2** exact clause matches on the delivered tree | same clause replay script |
| C3-a | reference-ledger data rows | 3 | 4 (ETCSL row, 4 populated columns) | `grep -c '^\|' corpus/knowledge/reference-ledger.md` → 6 |
| C3-b | ledger diff scope | — | pure append `5a6`; prior 3 rows md5-identical | `git diff --numstat dfd1fbc..2ea9ef1 -- corpus/knowledge/reference-ledger.md` → `3  2` |
| C3-c | decision table file | absent | added, 19 lines, with R1B scope note | `git diff --name-status dfd1fbc 2ea9ef1 -- corpus/knowledge/` → `A …r88-sourced-inspiration-decision-table.md` |
| DP-a | provenance-contract doc drift | docs matched the checker they described | checker emits the new wording; docs still paste the old one (0 / 8 / 17 `first occurred at`) | `grep -c 'first occurred at' corpus/fixtures/check_bible.py corpus/knowledge/holder-assessment-boundary.md corpus/knowledge/r87-provenance-chain-decision-table.md` → `0 / 8 / 17` |
| DP-b | doc-pasted probe receipts | doc receipts reproduced at `2b48ca7` | `r85-masked-ambiguous` 5 → **4**, `r85-isolated-ambiguous` 4 → **3**, `r85-harbor-repro` 7 → **6** findings; 0 `first occurred at` lines in delivered output | `for c in r85-control r85-unique-break-control r85-masked-ambiguous r85-isolated-ambiguous r85-harbor-repro; do python3 corpus/fixtures/check_bible.py corpus/live/runs/round-85/probe-inputs/$c; done` |
| DP-c | boundary-doc regression census | doc: "nine … none" | 19 provenance-bearing dirs; 9 also carry a duplicate entity id | see P2.md |

Exact census command (run from the repo root; `PYTHONPYCACHEPREFIX` keeps the
run from writing `__pycache__` into the tree):

```sh
cd /home/vgpnk/Projects/shokunin/lore-shokunin && python3 - <<'PY'
import hashlib,json,os,subprocess,sys
b1=json.load(open(".ufo/waves/round-88/patches/B1-tuples.json"))
dirs=sorted(d for d in os.listdir("corpus/fixtures") if os.path.isdir("corpus/fixtures/"+d))
env=dict(os.environ,PYTHONPYCACHEPREFIX="/tmp/p2-pycache")
res={}
for d in dirs:
    p=subprocess.run([sys.executable,"-I","corpus/fixtures/check_bible.py","corpus/fixtures/"+d],
                     capture_output=True,text=True,env=env)
    res["corpus/fixtures/"+d]={"exit":p.returncode,"sha":hashlib.sha256(p.stdout.encode()).hexdigest(),
                               "v":sum(1 for l in p.stdout.splitlines() if l.startswith("VIOLATION:"))}
ec={}
for r in res.values(): ec[r["exit"]]=ec.get(r["exit"],0)+1
ch=sorted(k for k in b1 if res[k]["sha"]!=b1[k]["stdout_sha256"] or res[k]["exit"]!=b1[k]["exit"])
print("dirs=%d exits=%s violations=%d changed=%d new=%d exit_changes=%d"%(len(res),json.dumps(ec,sort_keys=True),
      sum(r["v"] for r in res.values()),len(ch),len(set(res)-set(b1)),
      len([k for k in b1 if res[k]["exit"]!=b1[k]["exit"]])))
print("changed:", ",".join(ch)); print("new:", ",".join(sorted(set(res)-set(b1))))
PY
```

Observed: `dirs=149 exits={"0": 31, "1": 118} violations=367 changed=9 new=4 exit_changes=0`.
Changed: `r61-independent-empty`, `r61-independent-unavailable`,
`r87-masked-break-from-ambiguous`, `r87-masked-break-to-ambiguous`,
`r87-probe-entry-shape`, `r87-probe-multi-invalid`, `r87-probe-nonitem-kinds`,
`r87-probe-record-and-chain`, `r87-probe-shape-ambiguous`.
New: `r88-m3-maya-cluster`, `r88-mixed-stop`, `r88-nonholder-stop`,
`r88-shape-ambiguous-armed`.

**Reproducibility caveat (measured).** The census must pass the fixture path
*relative to the repo root*. A first P2 run that passed absolute paths reported
`changed=14` because the five "cannot load JSON" fixtures (`r5-missing-file`,
`r62-missing`, `r67-claim-source-unavailable-{control,empty,whitespace}`) embed
the argument path in their message text; with relative paths the same run
reproduces `changed=9` and matches `patches/V1-delta.json` with an empty
symmetric difference. `JCOV1-measurements.json` independently records
`path_only_differences_excluded_from_count = 5`, confirming the artifact. Any
future census receipt should state the path form.

Learning trends: expansion improved (fixture dirs 145 → 149; inspiration-note
files 1 → 2; a new sourced-mythology family landed). Quality improved on the
measured surfaces (calibration: first-stop cause tracking replaces the
holder-only latch; depth: a sourced-inspiration rule table + a verified ledger
row). Documentation parity **harmed** — the round's one regression, found
independently by `JCAL5` and `JDEP4`. Discernment improved: the round's own
landed decision table predicted the Spence registration gap it now exhibits,
and every claim above carries its own bound. Record hygiene: the r87 section's
"133 → 145 dirs" line is stale against 149 until this section lands (`H2`).

planned (r89; derived from `Q1.md` + `patches/Q1-r88-debt-map.json` (41 open
rows: 2 closed by C1, 2 by C2, 1 by C3, 5 rejected, **31 carried**), the landed
follow-up reports, and the trade above):
1. **documentation parity (top obligation, closes the r88 trade)** — refresh
   `corpus/knowledge/holder-assessment-boundary.md` (~15 drifted items; the
   census line is the actionable one) and
   `corpus/knowledge/r87-provenance-chain-decision-table.md` (the larger
   carrier, 9 + 16 dead-string occurrences) to the delivered wording and counts;
   move the R1B scope sentence into the row-5 rule cell so it survives comment
   stripping (`JDEP4` D-JDEP4-1/2, `JDEP1` debt 4).
2. **calibration** — add one durable dangling-holder-stop fixture (`JCAL5` D-2)
   and one two-non-shape-cause fixture (`JCAL5` D-3); record the two origin-label
   formats explicitly (`JCAL5` D-4). The r87 residual set is closed, so the next
   lowest-axis obligation must be **re-derived**, not inherited.
3. **coverage** — repair the Maya clause-map exact anchor (map `‘Earth,’` vs
   delivered `“Earth”`) and re-run the exact-match count to 2/2 (`JDEP1` debt 3);
   add the Spence ledger row (`JDEP2` F2, `JDEP1` debt 1) and a
   `corpus/fixtures/README.md` Round 87/88 section (`JCOV5`, D-C3-012).
4. **depth** — de-draft `r88-sourced-inspiration-decision-table.md`: drop the
   `Draft destination:` opening, rewrite rows 1/4/5/7 to cite only landed
   evidence, add the ETCSL delivery-status marker (`JDEP2` F3), and either
   disclose the r87 `1/7 / 1/7 / 0/4 / 0/4` support state or deliver that prose
   (`JDEP1` debt 5); extend the table to the three uncovered inspired-content
   classes `JDEP3` demonstrated (S1 rights-blocked source / element disposition
   and materiality trigger, S2 paraphrased in-world excerpt / delivery mode,
   S3 parallel conflicts with landed canon / cross-cluster scope) — all three
   are probe-stage, none is a harm to a previously working surface.
5. **carried debt to keep visible:** D-C3-005 (r87 metadata-only in-world
   sources), D-C3-009 / D-JCOV5-1 (absent kotodama↔lore handoff contract),
   D-CEN-003..011 labeling cautions, D-REP-004 (stale r87 report placeholders),
   `JDEP4` D-JDEP4-3 (no measurement helper for the five-gate sample).

saturation: not declared — no rubric exists; the stagnation nudge is not
triggered. Note for the next round: calibration has held the falsifiability
tie-break for two consecutive rounds (r87, r88) and its named r88 residuals are
closed on the delivered tree, so the tie-break must be re-derived, not assumed.
retired: none added; the historical duplicate-name rejection remains in force.

SHONEN unchanged (`P4-shonen.md`): `SHONEN.md` bytes unchanged by the round; all
four boxes stay `[~]`/`[ ]` with no `[x]`; box 2's evidence improved (the LOG
clause is satisfied by `LOG.md:1699` plus the round's replay receipts), boxes 1
and 4 unchanged. No named non-author verifier this round.
