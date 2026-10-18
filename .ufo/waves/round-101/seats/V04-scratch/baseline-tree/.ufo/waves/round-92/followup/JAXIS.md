# JAXIS — Synthesizer (round-92 follow-up, world-bible lane)

Seat JAXIS, round-92 follow-up wave. Mission: read **all** reports present in
`.ufo/waves/round-92/followup/`, reconcile the JDEP1-vs-V2 certification tension, rule the per-axis
verdict table (calibration / coverage / depth), and recommend the admission path.

Judgment surface: the committed tree at `c4d4823b9a8165a88e8199af136e62d6e961b6b9` (baseline
`396c568`), secondarily the committed r92 wave artifacts (`.ufo/waves/round-92/patches/`, which ARE
tracked in `c4d4823`) and the r91/e97613c revisions via `git show`. Peer follow-up `.md`/`.json`
artifacts are untracked at close — they are treated as testimony, corroborated where cheap, never as
the judgment surface. No commit, no push; repo writes are this report and
`followup/JAXIS-verdicts.json` only; my scratch was one `/tmp` file (`/tmp/jaxis-r89-checker.py`,
removed at close). Disclosure: the closing sweep also found and removed two pre-existing
`/tmp/jaxis-*` files (`jaxis-census2.py`, `jaxis-census.json`) that this run did not create — likely
a prior JAXIS-named run's residue; they were seat-named round-residue and are now swept (Q2 F4's
scratch-residue class).

## Work performed

- **Read all 32 follow-up `.md` reports — including both that landed mid-run** (P1.md at 10:43:02,
  JCOV5.md at 10:43:42): E1, H1–H5, JCAL1–JCAL5, JCOV1–JCOV5, JDEP1–JDEP5, K1, P1–P4, Q2, SE2,
  SF1, SF2, V2, W1 — plus the machine artifacts `JDEP1-certification.json`, `V2-freeze.json`,
  `P1-manifest-entry.json`, and the committed `patches/T1-certification.json`. Neither P1.md nor
  JCOV5.md existed at the opening sweep; both were read at their arrival. Two 60 s wait-checks were
  run (receipt at the end of this section); the follow-up batch was still landing around the
  judgment surface throughout.
- **Adjudicated the one contested region first-hand** (the C1 certification pivot), because every
  verdict below depends on its severity: frozen the identities, read the two contested byte regions,
  and settled the *lineage* question that separates JDEP1's "FAIL, blocking" from V2's "PASS with one
  named defect" — was the orphan tail's failure state inherited, or created at r92?
- **Cross-checked the reports' shared claims for internal conflicts** (census/checker/doc hashes,
  the R8/R9 landing defects, the tools-README drift, the certification attribution) and mapped
  agreements and the single real dissent.
- **Did not re-run** the census, the 14-case replay, or the support receipts: each has ≥2 independent
  runners inside the wave (H4/JCAL1/JCAL5/P2/V2; JDEP1/H5/SE2/V2/P2; JCOV1/H1/H2/H5/P2/SE2), and my
  charge was synthesis. Every claim I carry forward is attributed to its measuring seat; my own
  measurements are the ones in the next section.

**Dependency receipts** (two 60 s wait-checks, HEAD stable, batch still landing):

```text
CHECK1 t=0   2026-10-17T10:40:09-03:00 HEAD=c4d4823 files=53
CHECK1 t=60  2026-10-17T10:41:09-03:00 HEAD=c4d4823 files=53
CHECK2 t=120 2026-10-17T10:42:09-03:00 HEAD=c4d4823 files=55
TERMINAL status=0 checks=2
```

## Before → after measurements

**1. Freeze and identities (my probes, committed tree).**

```sh
git rev-parse HEAD; git status --porcelain | grep -v '^?? .ufo/waves/round-92/followup/'
sha256sum corpus/fixtures/check_bible.py corpus/knowledge/holder-assessment-boundary.md
wc -l corpus/fixtures/check_bible.py corpus/knowledge/holder-assessment-boundary.md
```

```text
c4d4823b9a8165a88e8199af136e62d6e961b6b9
(no output — the only porcelain dirt is untracked followup/ artifacts)
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
8e1fe8774a70f06c31efd783b4313a1639c1da4bcfd830be92134e8964536728  corpus/knowledge/holder-assessment-boundary.md
  428 corpus/fixtures/check_bible.py
  671 corpus/knowledge/holder-assessment-boundary.md
```

(JDEP1 counts the doc at 672 by a `splitlines` convention — same bytes, same sha256; non-blocking.
The r92 checker is unchanged at every reported endpoint.)

**2. The stale delivered-context anchor (doc:330).**

```sh
sed -n '328,332p' corpus/knowledge/holder-assessment-boundary.md
```

```text
  conditions that used to disable the chain silently (no sources,
  non-item entity, duplicated item id) are now named first stops
  (`:198-203`). Comparisons require sources loaded, `kind == "item"`, and a
  unique item id — unchanged (`:183` baseline; delivered `:200-205`) — but a
```

The same bullet carries the wrong range at doc:330 and the right one at doc:331; the delivered
item-level first-stop tests are `:200-205` (JDEP1, H2, H5, W1 agree).

**3. The headless orphan tail (doc:545-556).**

```sh
sed -n '543,547p' corpus/knowledge/holder-assessment-boundary.md | cat -A | head -5
sed -n '545,556p' corpus/knowledge/holder-assessment-boundary.md | grep -oE ':[0-9]+(-[0-9]+)?'
```

```text
  behavior `:418-428`. The checker stayed byte-identical through r91 closure `396c568`.
  lines, sha256 `e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556`):
...
21 sites: :38-39 :72-76 :82-83 :85-91 :93 :97 :164-166 :168-173 :182 :185-352 :191 :192-194
:198-203 :206-208 :212-214 :215-221 :222-248 :249-312 :313-319 :320-352 :425-435
```

The tail begins mid-clause (`lines, sha256 `e2bb9639…`):`) with no lead-in, and `:429-435` points
past the delivered file's 428 lines.

**4. The lineage question — inherited, or manufactured at r92?** This decides the severity framing.

```sh
git show 396c568:corpus/knowledge/holder-assessment-boundary.md | sed -n '418,442p'   # r91 doc c0c59daf
git show e97613c:corpus/knowledge/holder-assessment-boundary.md | sed -n '505,512p'   # reference contract
```

```text
r91 doc lines 429-430 (and e97613c lines 508-509) before the same 21 sites:
- Checker at delivered `1b09f3f` (`corpus/fixtures/check_bible.py`, 435
  lines, sha256 `e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556`):
```

At r91/e97613c the 21 anchors were **attributable** — a revision-qualified historical block naming
`1b09f3f`. The r92 edit replaced that head with the delivered `ca7f9ef` / `ff9fd2aa` bullet (correct,
at doc:534-544) and left the tail from doc:545 — headless, therefore unqualified.

**5. Were the tail anchors factually right for their named revision?**

```sh
git cat-file -e 1b09f3f:corpus/fixtures/check_bible.py && git show 1b09f3f:corpus/fixtures/check_bible.py | wc -l
git show 1b09f3f:corpus/fixtures/check_bible.py | sha256sum
# per-span first/last-line signatures for all 21 anchors (python3 over the same blob)
```

```text
435 lines
e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556
:38-39 raw_entity_id_counts/raw_source_id_counts | :72-76 'if section in (…)': … raw_id_counts[identifier] = …
:82-83 'if valid:' → data[section].append(…) | :85-91 'def index(section):' → 'return result'
:164-166 entity_id_counts … | :168-173 'def holder_identity_detail(…)' → '… is not uniquely resolvable (…'
:182 '{location}.{endpoint}: ambiguous entity …' | :185-352 "for location, item in data['entities']:" → 'previous_tick = tick'
:191 'only valid on item entities' | :192-194 isinstance list → continue | :198-203 'if not sources_available:' → duplicate-item first_stop
:206-208 report_unassessed | :212-214 top-of-loop emission | :215-221 non-dict branch | :222-248 expected_keys → continue
:249-312 tick extraction → chain_has_ambiguous_source | :313-319 'if not valid:' → continue | :320-352 'if first_stop is None:' → previous_tick = tick
:425-435 "__main__" → 'CLEAN: schema, citations, relations, timeline; 0 violations'
```

**All 21 tail anchors are content-correct against `1b09f3f`.** The tail is a *correct r89 inventory*
whose head was removed at r92 — not fabricated, and not a fresh error introduced by the re-derivation
— but the unqualified state that makes it fail-closed is new at r92.

**6. Certification artifacts.**

```sh
python3 -c "import json;d=json.load(open('.ufo/waves/round-92/patches/T1-certification.json'));print(d['overall'], d['candidate_selection']['status'])"
```

```text
FAIL FAIL   # 'No selected, integrated round-92 document is present at the required target …'
```

The commit message's "certified by T1: 3/3 receipts, 14/14 replay cases" cites T1's *baseline
control*, not a candidate pass (T1 is committed; H1 F4, JDEP5 M7, V2, JCOV4 F2 all agree).

**7. Duplicated tails.** `sed -n '591,596p;613,619p' <doc>` — doc:591-596 repeats the
fixture-inventory tail and doc:613-619 repeats the rules-text / "`## Round 89` section at
`1b09f3f`" tail of the preceding bullet (V2, H5, W1, JCOV4 F6).

## Findings & named debt

### F1 — Reconciliation of the C1 certification tension (the seat's core ruling)

**Two positions.** JDEP1 (the certifier) rules gate (b) **FAIL, blocking**: 14 of the tail's 21
sites do not resolve to the claimed content against the delivered checker, one lies past EOF, plus
the stale doc:330 range — "the doc is not certifiable as delivered". V2 (delivered-revision
verifier) rules the same region **PASS with one named document defect**, measured over 18
delivered-context anchor families, and calls the fragments "inherited from e97613c".

**Ruling: JDEP1's FAIL is the correct severity for the C1 *certification sub-claim*; V2's PASS is
correct for the surface V2 measured and must not be read as certifying the document.** Grounds,
each measured or cited above:

1. The round's own acceptance clause is explicit: C1 promised "a certifiable document: … **every
   code anchor resolves**" (`wave-spec.md`, C1). The delivered doc does not satisfy it.
2. The round's own certifier contract fails closed: B3 Gate C §3 "An unqualified citation whose
   target revision is ambiguous fails closed"; §4 "Any omitted, stale, malformed, unqualified, or
   content-mismatched citation is a failure"; §5 "Zero unresolved/unknown anchors is required."
   A headless tail of unqualified `:NNN` sites is exactly that class, regardless of whether the
   numbers happened to be right for a superseded revision.
3. **Every doc-wide certifying pass in the wave found Gate C red** — JDEP1 (FAIL), JCOV4 (F1
   "blocking … fails closed"), H2 ("anchor resolution FAILS at two verified sites"), H5 (two
   failing locations), W1 (residual list; "a full catalog pass is contradicted"), JDEP5 M4
   ("overall FAIL, blocking on gate (b)"). **No doc-wide run found it green.** P2's gate-C
   evidence is a sample (2/2 AST spans + 21 families); V2's is 18 families of delivered context;
   V2 itself concedes a strict doc-wide reading keeps the gate red.
4. **"Inherited" is true of the text but false of the failure state.** I measured the r91/e97613c
   counter-state: the same 21 sites sat under a head naming `1b09f3f`, and all 21 resolve
   content-wise against `1b09f3f`'s checker. The r92 edit *removed that head* and left the tail.
   So the severity downgrade V2's wording invites ("pre-existing, therefore inherited") is not
   available: r92 manufactured the gate-C failure state, even while it repaired the structure
   gates, the `:184` relation anchor, and the replay surface.
5. JDEP1's own residual imprecisions are non-blocking and do not disturb (1)-(4): the F5 census
   off-by-one (doc:581-590 "13 … across ten" at `ca7f9ef`; measured 12/10) and the 672-vs-671
   line convention.

**Why bounded, nevertheless.** No receipt, no checker behavior, and no census tuple is affected
(the doc is not read by any tool; checker `ff9fd2aa` untouched). The gate-C failure is one stale
delivered range plus one superseded-history tail; the repair is line-level and checker-free. The
r91 baseline for C1 was worse on the structure gates (2 H1s, duplicate heading, 2 instruction
markers, stale `:182`) — r92 is a strict improvement there. The correct record wording is:

> C1: re-derivation delivered byte-exactly (delivered doc = `396c568` bytes + D2's patch; V2/H1
> hash-chain); certification attempted post-integration at `c4d4823` → **gate (b)/C FAIL** per the
> round's own B3 contract (one stale delivered range + one 21-site headless r89 tail); replay,
> structure and C9 gates pass; repair is documentation-only; **do not record "certified"** until a
> post-repair gate-C re-run passes.

**Repair preference (measured):** *delete* doc:545-556 rather than restore its head. The delivered
bullet at doc:534-544 already carries every claim family with correct spans; restoring the r89 head
would re-create a second, superseded anchor inventory for the same families — the duplication class
CB1's r90 audit already named.

### F2 — Per-axis verdict table

Verdicts are per axis, never scalar, and never netted across axes; sub-harm is named inside the axis
that carries it.

| Axis | Verdict | Positive evidence (measuring seats) | Named harm / bound |
|---|---|---|---|
| **depth** (C1) | **improved (bounded), conditional** | D2 candidate = committed bytes (V2/H1 hash-chain); replay 3/3 blocks, 14/14 cases byte-identical (JDEP1, H5, SE2, V2, P2, H2); structure gates now PASS — 1 H1, unique headings, 0 markers (V2, H5, P2; r91 FAILED these); C9 wording 5/5 + AST PASS (P2, JDEP1); `:184` relation anchor repaired (V2, H2); JDEP2 residual edges decided and applied (P2, JDEP4, JDEP3: R8 whole-element hold; R9 manual gate + receipt boundary) | **Certification sub-claim not admissible as delivered**: gate-C FAIL (F1) — headless 21-site tail (14 delivered-mismatching, `:429-435` past EOF) + doc:330 stale; **R8/R9 table landing fidelity harmed (bounded)** — doubled label at decision-table `:40`, R9 block inside the R8 appendix (`:42-48`), R8 worked example and R9 evidence-cell append absent, old R9 worked example un-replaced (JCAL4 "harmed (bounded)"; JDEP3 "harmed / partial"; E1 "harmed (bounded)"; H1 F1/F3; JCOV2-1; JDEP4); doc provenance header still says r90 with no r92 line (JDEP5 M8, E1 W3) |
| **coverage** (C2) | **improved (bounded)** | Spence rows close the WARN: baseline 10+0 + WARN → 10/2/12/8, `RESULT PASS`, no WARN (JCOV1, JCOV2, JCOV3, H5, P2); mutation control shows the S1 anchor cells are load-bearing (JCOV2: mutated anchor → `FAIL S1`, exit 1); support contract conforms across 15 designed failure paths — missing inventory exit 2→1 with `RESULT FAIL`, map/cluster/structural errors exit 2 with `RESULT ERROR`, row failures exit 1 (JCOV1, H1, H2, H5, P2, SE2); positive-path output byte-identical to baseline | **tools-README contradiction at HEAD** — `corpus/tools/README.md:16-21` unchanged while the tool it describes changed: it still sells exit-2/no-terminal-summary deviations as current "until the checker is updated" (K1-1, Q2 F2, JDEP3 F6, JCOV4 F3, H5 3(a), E1 W2-harmed, H1 F2); K1's patch applies cleanly and is unapplied. Carried: V1 D-V1-1 duplicate-row detection (H1 F7). No new mechanism this round — capabilities table unchanged (JDEP5) |
| **calibration** (C3) | **improved (bounded)** | Watch check-log row 1 (2026-10-17, `ff9fd2aa`, DISCRIMINATION HELD) accurate; durable pair + four C5 probes byte-identical to their pins and re-derived independently (JCAL2, P2, P3, H3); path-convention claims confirmed exactly (five argv-embedding fixtures; repo-relative guidance reproduces B1/B2 hashes) (JCAL3, H5, JCAL2); census 166/166, exits {0:32, 1:134}, 421 violation lines, B1≡B2 (`185ce02d`), canonical digest `a92a4f22` — zero drift (JCAL1, JCAL5, H4, P2, V2, SE2) | No next-recheck pointer in the committed watch/README (JCAL2); CB R3 residuals (e97613c hash pin, ambiguous-SOURCE wording) open; path-note wording overbroad — `./`, doubled slashes, trailing slash normalize away; only absolute and `../`-preserving prefixes alter stdout (JCAL5, JCAL3 precision note); watch over-claim "paired resolved-holder control" vs the P2/P4 near-control, E3's correction unintegrated (JCAL4 F3/F4); JCAL4 F5 referent ambiguity, F6 under-enumeration |

**Process note (not a craft axis):** SF1/SF2's pre-commit FAILs (`396c568`, dirty tree) are
superseded by `c4d4823` — Q2 replayed the SF1 fail-set at the commit and SE2 reproduced the
candidate-scope receipts byte-for-byte; the one standing process gap is that no SF1 rerun against
`c4d4823` exists on record. Roster arithmetic (32 declared / 30 named / 31+2 reported: H1 F5,
Q2 F3), scratch budget (530,932 residual files, 1.477 % free inodes vs a 5 % gate: Q2 F4), and
poll-helper residuals (Q2 F5) are r93 process hygiene. SE2's naming census conforms (37/37 at its
snapshot; 53 → 55 files across my checks). The fleet report `.ufo/reports/round-92/lore.md` was
written by seat P1 at 10:43:02 with verdicts marked PENDING L1 (it cites this seat's
`JAXIS-verdicts.json` in its Verdicts section); the `MANIFEST` `rounds[]` entry exists only as
P1's proposal (`P1-manifest-entry.json`, explicitly not landed) — both outside this seat's write
scope, and the MANIFEST landing is still open for L1.

### F3 — Admission recommendation

**Primary: repair-then-admit.** The repair is smaller than the record work already pending — the
r92 `LOG.md`/`SCORECARD.md`/`SHONEN.md`/`PROVINCE.md` records are unwritten at `c4d4823` (K1-2, P4,
JDEP5 M9; `git diff 396c568 c4d4823` touches none of them), so the repair can land in the same
closure commit as the record and convert depth from "improved but blocked" to "improved" with no
checker or receipt change.

Repair list (each item: verification basis in the reports and in my probes above):

1. **doc:545-556** — delete the headless r89 tail (preferred over restoring the head; §F1).
2. **doc:330** — `:198-203` → `:200-205`.
3. **doc:591-596, doc:613-619** — delete both duplicated tails.
4. **decision-table `:40`** — drop one doubled label.
5. **`corpus/tools/README.md`** — apply `patches/K1-tools-readme.patch` (clean apply at `c4d4823`).
6. Optional-but-recommended: r92 provenance header line for the doc (E2's block); move the R9
   block `:42-48` into the R9 appendix and reconcile the R9 worked examples / missing pieces.
7. Re-run the B3 gate-C census after (1)-(4); record `CERTIFICATION PASS`/`FAIL` — the certifier
   implementation is absent by design (B3 is spec-only; `tools/certify_boundary_doc.py` does not
   exist), so the doc-wide census used by JDEP1/JCOV4 serves as the re-run.

**Fallback: admit-with-harm**, only under these conditions: (i) strike "certified" from every record
surface including the commit-message claim, recording instead "certification attempted
post-integration; gate C FAIL (blocking)"; (ii) carry items 1-5 as the opening r93 repair item with
the receipts above; (iii) no SHONEN box promotion and no fourth capability row (P4; JDEP5);
(iv) do not cite `corpus/tools/README.md`'s contract text as current until item 5 lands.

### Named debt (rollup; owner-ready)

Doc/gate: `D-doc-gateC` (items 1-3 + re-run) · Table: `D-table-r92-integration` (item 4 + R9 venue /
missing pieces) · Tools README: `D-r92-tools-readme-integration` (item 5) · Record:
`D-r92-certification-record` ("certified by T1" cites baseline controls; T1 = overall FAIL) ·
Governance: `D-JDEP4r92-1` (R8 reviewer independence), `D-JDEP4r92-3` (R9 sustainment/lapsed
access), `D-JDEP4r92-4` (R10 alias channel, carried), `D-JDEP2r91-4/-5` (R9 verification command;
translation-mode counting), `D-JDEP3r92-1` (R8 worked example absent) · Watch/calibration:
`D-watch-next-pointer`, `D-path-note-wording`, `D-watch-F3-F4-F5` · Province/adjacency:
`D-JCOV5-3` (r91 "withhold-scope precedence" absent with no supersession clause), `D-JCOV5-4`
(adjacency owner unnamed — optional one-line addition; JCOV5) · Process: `D-V1-1`,
`D-r92-roster`, `D-r92-scratch`, `D-r92-helper-residual`, `D-README-r91-index`.
Full machine-readable rollup: `followup/JAXIS-verdicts.json` → `named_debt_rollup`.

### Agreements and the one real dissent

Agreements (independent runners): checker unchanged + census 166/166 zero drift (H4, JCAL1, JCAL5,
P2, V2, SE2, H5, JDEP1); coverage improved-bounded (JCOV1/2/3, H1, H5, P2, P3, E1); calibration
improved-bounded (JCAL2, JCAL3, P2, P3, H5); R8/R9 content landed but table text harmed (JCAL4,
JDEP3, E1, H1, JCOV2, JDEP4, H5, P2); gate C red doc-wide (JDEP1, JCOV4, H2, H5, W1, JDEP5, P4);
province fit unchanged (JCOV5: zero chousa/kotodama method markers in the r92 diff, chousa
cross-reference block byte-identical, all three sibling pointers resolve).
Dissent: V2's severity framing only — reconciled in §F1; V2's measurements are unmodified, and
V2's own handoff pre-declares the strict-reading caveat. JDEP5's "capabilities table unchanged /
no fourth row" met no dissent in the wave.

## Handoff

- **Deliverables:** `.ufo/waves/round-92/followup/JAXIS.md` (this report) and
  `.ufo/waves/round-92/followup/JAXIS-verdicts.json` (machine-readable: reconciliation, per-axis
  verdicts, admission recommendation + repair list, debt rollup, agreements/dissents, gaps).
  No other tracked write; no commit; no push.
- **The ruling, in one paragraph for the record:** C1 is *improved (bounded) on method, content,
  replay, structure and C9 semantics* but **fails its own certification clause as delivered** —
  gate (b)/C red on one stale delivered range (doc:330) and one 21-site headless r89 tail
  (doc:545-556; all 21 correct for `1b09f3f`, unqualified at `c4d4823`, `:429-435` past EOF).
  JDEP1's severity stands; V2's PASS describes only the delivered-context surface it measured, and
  "inherited from e97613c" describes the tail text, not the failure state, which r92 created.
  C2 coverage is improved (bounded) with one introduced doc contradiction (tools README; fix
  ready). C3 calibration is improved (bounded) with named watch wording/pointer debt. Nothing in
  the wave supports recording "certified".
- **Recommended admission:** repair-then-admit (lead item for the closure commit, alongside the
  still-unwritten r92 record); admit-with-harm is the fallback, under the four conditions in §F3.
- **Gaps:** no committed passing gate-C certification exists anywhere and none can be recorded
  before a post-repair re-run; my per-span check of the 21 tail anchors verified each span's
  first/last-line signatures, not full interiors; the wait-checks are point-in-time with the batch
  still landing (53 → 55 followup files across my checks); `/tmp/jdep1` (JDEP1) and JDEP4's scratch dirs are flagged in
  those reports for the closure sweep.
