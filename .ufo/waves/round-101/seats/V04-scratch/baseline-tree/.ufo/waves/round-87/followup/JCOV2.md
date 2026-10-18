# JCOV2 — Coverage judge #2 (province adjacency)

Seat: JCOV2, round-87 follow-up wave (world-bible lane). Judged on the delivered
tree at `2b48ca7` (clean at start; the only working-tree entries were another
seat's `l0-questions.md` edit and the untracked `followup/` directory). No
tracked file was written by this seat; outputs are this report and
`followup/JCOV2-adjacency.json` only.

Verdict vocabulary used below: improved / harmed / unchanged /
unprovable-but-better. No scalar scores.

## Work performed

- Read `PROVINCE.md` (all 11 lines), `.ufo/waves/round-87/S3.md`,
  `.ufo/waves/round-87/K1.md`, the delivered cluster
  `corpus/fixtures/r87-myth-cluster/` (all 9 files), `corpus/fixtures/README.md`,
  `corpus/knowledge/{reference-ledger.md,seed.md,2026-10-12-lore-decision-table.md,holder-assessment-boundary.md}`,
  `SCORECARD.md`, and the five sibling declarations named by S3.
- Replayed the delivered checker on the cluster, the four C1 fixtures, all 138
  fixture directories, and the four round-85 live probes (read-only; nothing
  written).
- Independently fetched the cited real-world work to check the attribution
  claim rather than trusting the note: `https://etcsl.orinst.ox.ac.uk/section1/tr141.htm`
  (ETCSL, "Inana's descent to the nether world", tr141). Its lines 122–163 do
  describe the bolting of the seven gates and the removal of dress/regalia item
  by item (line 123-128 seven gates bolted; 129-133 turban removed at gate one;
  159-163 *pala* dress removed at gate seven), and its opening lines describe
  Inana's descent. The note's characterization is accurate; the site itself
  carries a "credits and copyright" page, which the note's deferral points at.
- Verified each of S3's five rejected-fit rulings against the sibling
  declarations line by line, and re-ran K1's independent sibling scan result
  against the current fleet root.

## Invariant verification — C3 cluster

**V1 — attribution / rights / AI-training-permission stay three distinct
questions: verified.** `inspiration-note.md` carries three separate `##`
sections (`:7` Attribution, `:11` Rights, `:15` AI-training-permission) and each
answers only its own question. Cross-inference is explicitly refused:
`:9` "Attribution to the cited page is separate from any rights conclusion";
`:13` "The age of an underlying ancient composition does not by itself answer the
rights question for a modern translation or edition"; `:17` "Public
accessibility, attribution, and any conclusion about copyright status do not
imply permission for AI training". The cluster README restates the separation
(`README.md:7`).

**V2 — no rights claims: verified.**
`grep -rniE "public domain|copyright|licen[cs]|permission|rights|all rights|cc-by|attribut" corpus/fixtures/r87-myth-cluster/`
returns only non-claims and attribution statements: the three question headings;
"has not been determined here" (`:13`); "has not been assessed or established"
(`:17`); and attribution wording about *fictional in-world* sources
(`lowwater-hymn-excerpt.md:1,7`; `sources.json:18,24`; `symbolism-clause-map.md:3`).
No term asserts a status, and no rights conclusion is drawn anywhere in the
cluster.

**V3 — no canon claim without in-world citation: verified.**
The checker validates every entity `first_appearance`, every entity claim, every
relation and every event against `sources.json` and exits 0. Programmatic
cross-check: the 5 referenced source IDs
(`dune-register, gate-witness, lowwater-hymn, shell-charter, tide-bell-tally`)
all resolve, 0 unresolved. Prose keeps the separation: the inspiration note
states "It is not an in-world source and supplies no fictional canon" (`:19`);
the symbolism map states "These are interpretive readings of authored words, not
new canon" (`:15`); the hymn excerpt is attributed to in-world `lowwater-hymn`
and flagged "not an authenticated ritual or objective world account" (`:7`). The
two world-shape assertions in the fixture README — reciprocal alliance edges and
the reported place disagreement — are both verifiable in `relations.json` and
`timeline.json`.
*Sub-finding (limit, not a violation):* relation `shellweavers
keeps_watch_with reed-bell` cites `shell-charter`, whose declared scope is a
faction treaty (`sources.json:3-6`, reliability note: records a reciprocal
pledge). No charter excerpt exists in the fixture, so no prose is available to
check that citation, and the symbolism map explicitly declines the
joint-handling inference (`:12`). This is a cited-but-unattested claim, the same
limit the lane already records for excerpt-less sources
(`2026-10-12-lore-decision-table.md:112`: "do not claim textual support for
them"). Not an uncited-canon violation.

**V4 — no silently resolved contradiction: verified.**
`contradictions.json` records exactly one pair, `moon-basin-vow-location`, over
`moon-basin-vow-gate-account.place_id` and `moon-basin-vow-dune-account.place_id`
— two distinct events, both retained at `timeline.json:22-43`, with distinct
unique sources (`gate-witness` vs `dune-register`) and different places
(`mother-tide-gate` vs `ash-dune-sanctuary`). The ledger `why` states the
disagreement "is reported and left unresolved"; `README.md:5` says the same and
adds "**The contradiction is reported, not resolved.**" Nothing is dropped,
reordered or deduplicated; the shared tick 3 is not an occupancy case (distinct
actors), and no dependency inversion exists (both depend on tick 2). The checker
emits no winner and no ledger finding (exit 0) — matching the established
precedent for ledger-carrying fixtures, which I re-ran:
`r35-bell7-conflict` exit 0, `r36-bell7-wrong-date` exit 0, `r37-ledger-unique`
exit 0 (contrast `contradictions` exit 1, which carries ordinary non-ledger
violations).

**V5 (bonus) — declared expectation met.** The cluster's declared expected exit
is 0 (`S4.md:22`; C3 commit message `e4708cb`); observed 0.

## Adjacency rulings — S3's five siblings, verified independently

Each declaration was read directly; S3's quoted line ranges all check out:

| sibling | S3 cite | verified content | ruling |
|---|---|---|---|
| mori | `:3-18` | `:3-4` fleet/host observability; `:6-10` owns liveness, `.ufo/waves/*` settlement, kill/OOM, resources; `:12-16` refuses dispatch/OS/endpoint/credentials | **cannot absorb** — a fictional mythology/symbolism bible is not an observability object; "events" there are kill/OOM and host events, not fictional timeline events |
| chousa | `:3-17` | `:3` deep-research method; `:5-8` owns source hierarchy, citation chaining, claim-vs-source verification | **cannot absorb**; method adjacency is genuine (see A2) |
| kaidoku | `:3-6` | `:3-6` RE of shipped artifacts, evidence-first static analysis | **cannot absorb** — the deliverable is authored fiction |
| kotoba | `:3-6` | `:3` prompt & skill craft; `:5` playbooks/error patterns/checklists; `:6` refuses outside domain | **cannot absorb** — a symbolism map is world-bible content, not a playbook |
| revenger | `:3-29`, `:19-23` | `:3-7` RE with evidence ledger; `:19-23` refuses asset rights claims and "narrative canon (lore)" | **cannot absorb**; its rights refusal does not conflict because C3 asks for distinct open questions, not a rights verdict |

Cross-check with K1: K1 rejected these same five plus 13 others from the same
declarations and flagged the same chousa method edge — the two independent scans
agree. Sequencing note: K1 recorded S3 absent after two 60s-spaced checks
(`K1.md:6,34-35`); S3 is present in the delivered wave, so the absence was a
work-wave ordering artifact, not a missing deliverable. No harm: K1's rulings
rest on direct PROVINCE reads, and I verified S3's separately.

### Adjacency findings

- **A1 — the cluster is in-province.** Fictional entities, factions, relations,
  timeline events, sourced inspiration and the citation discipline are all
  expressly lore-owned (`PROVINCE.md:3,5-8`), and the cluster touches none of the
  five siblings' declared domains. Ruling: in-province, no encroachment.
- **A2 — the C3/Chousa method edge is real but narrow; no encroachment now.**
  The note characterizes the cited page's content, which is inseparable from
  making an attribution meaningful, but it builds no source hierarchy, does no
  citation chaining, and ranks or validates nothing — those are chousa's
  (`chousa-shokunin/PROVINCE.md:5-8`). `PROVINCE.md:5-8` does not draw the line
  in words. Ruling: **unprovable-but-better** if the integrator refines
  `PROVINCE.md` as K1 proposed (lore owns the in-world inspiration record and its
  citation fields; chousa owns reusable external-source research/validation
  method). No lane silently took the other's scope.
- **A3 — `art-east-asian-design` is a dangling recipient reference.**
  `PROVINCE.md:9` names it as the rights-claim recipient; `ls -d
  art-east-asian-design` at the fleet root → `No such file or directory`. Three
  other lanes name the same recipient (`game-dev-2d-shokunin/PROVINCE.md`,
  `game-dev-3d-shokunin/PROVINCE.md`, `revenger-shokunin/PROVINCE.md`), so this
  is a fleet-wide dangling reference, not a lore-specific defect. The C3 note
  does not name any recipient lane at all; it defers generically to "the
  corpus's credits/copyright information and applicable terms". Ruling:
  acceptable for lore (lore refuses rights claims and the note makes none); the
  dangling recipient name is flagged to the integrator for the fleet, and no
  rights conclusion is implied here.
- **A4 — the real-world citation is not registered in the reference ledger.**
  `corpus/knowledge/seed.md:26-29` states real-world references "enter through a
  reference ledger with the art lane's three distinct questions ... kept separate
  from in-world canon", and the decision table's real-world row points at
  `reference-ledger.md` (`2026-10-12-lore-decision-table.md:13`). The cluster
  keeps the three questions separate in its own file and correctly keeps the work
  out of the fictional table (`sources.json` holds 5 fictional rows;
  `grep -c etcsl corpus/fixtures/r87-myth-cluster/sources.json` → 0), so the
  *separation* invariant holds — but `grep -c etcsl corpus/knowledge/reference-ledger.md`
  → 0, and `grep -ril etcsl corpus/` finds the citation only inside the fixture.
  The inspiration is therefore discoverable only from inside the fixture, and the
  corpus's own declared entry point does not list it. Ruling: a coverage gap in
  the lane's documented discipline; assigned to the integrator (no seat block I
  can see authorizes `reference-ledger.md`, and it is not mine to edit).

## Census and documentation coverage

- Independent census: 138 fixture directories on disk, exits 30×0 / 108×1.
  `I3-new-fixtures.json` covers exactly the same 138 keys (no key without a
  directory, no directory without a key) and all five r87 expected/observed exits
  match; the C1 commit message's own claim ("30 clean / 108 violations of 138
  dirs") also matches. The four C1 fixtures and the C3 cluster are therefore
  counted and replayed consistently.
- C1 and C3 are independent in the delivered tree: the cluster contains zero
  `provenance` keys (`grep -c provenance corpus/fixtures/r87-myth-cluster/*.json`
  → 0 in every table), so C1's checker change cannot alter the cluster's output.
- **Documentation gap:** `corpus/fixtures/README.md` documents every prior
  fixture round (…, `## Round 72`, `## Round 73`, `## Round 83`) but has no
  `## Round 87` section — `grep -c '^## Round 87'` → 0 — although five new
  directories now live under `corpus/fixtures/`. (Round 85 needs none: its probes
  are under `corpus/live/runs/round-85/`, not the fixture corpus.) This is the
  lane's own established convention, so it is a real coverage-documentation gap,
  unassigned in the follow-up blocks I can see.
- **Declaration gap in two new fixtures:** `r87-chain-unique-valid` and
  `r87-chain-unique-broken` READMEs declare their expected exit explicitly
  ("expected result is CLEAN with exit 0" / "a reported final-record chain break
  and exit 1"), but `r87-masked-break-{from,to}-ambiguous` READMEs declare no
  exit code and describe the *baseline* behavior ("the baseline should report the
  ambiguous first holder and stop notice, but does not locally disclose that
  later record comparisons were skipped") — which the delivered tree now does
  disclose. `r87-myth-cluster/README.md` gives the replay command but no explicit
  exit code either (its declared 0 comes from `S4.md:22`/the C3 message, and I3's
  artifact quotes that source correctly even though its `declared_expected_exit_source`
  field says the fixture README). S4's procedure step 2 requires a declared
  expected exit before replay; I3 supplied it by inference for the masked pair.
  Ruling: contract gap to close with one line per fixture; not a measurement error.
- **Boundary-knowledge staleness (I2's authorized file).**
  `corpus/knowledge/holder-assessment-boundary.md:52-55` still states "Exactly
  one notice per item, located at the FIRST ambiguous-holder record" and its
  decision table (`:73`) describes only that one notice. The delivered C1 checker
  emits two findings at the first ambiguous record plus one per later record —
  verified: `r87-masked-break-to-ambiguous` prints the record-[0] stop notice,
  a record-[0] "…first occurred at entities[3].provenance[0]" disclosure, and
  record-[1]/[2] disclosures (6 findings total). The doc's own header
  (`:14-19`) already says `verified-at: STATIC PENDING PARENT RUNTIME`, i.e. its
  content was never runtime-verified. This confirms the follow-up wave's
  "boundary-knowledge refresh" item is still owed.

## Before → after measurements (exact commands and observed output)

All commands run from `/home/vgpnk/Projects/shokunin/lore-shokunin`; nothing was
written. Baseline identity:
`git log --oneline -1` → `2b48ca7 lore r87: work-wave evidence — 39 seat reports + patches (.ufo/waves/round-87), luna-max wave`;
`git status --short` → ` M l0-questions.md` and `?? .ufo/waves/round-87/followup/`
(neither from this seat).

- Cluster replay — `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster` →
  `CLEAN: schema, citations, relations, timeline; 0 violations`, `exit=0`.
- C1 fixture replays —
  `r87-chain-unique-valid` → `CLEAN … 0 violations` `exit=0`;
  `r87-chain-unique-broken` → `VIOLATION: entities[3].provenance[2]: provenance chain break; expected from_holder 'harbor', got 'mira'` / `1 violation(s); no canon changed` `exit=1`;
  `r87-masked-break-from-ambiguous` → 6 findings `exit=1`;
  `r87-masked-break-to-ambiguous` → 6 findings `exit=1` (both enumerate the
  duplicate ID, the local `ambiguous entity` field error, the record-[0] stop
  notice, and per-record "…first occurred at" disclosures).
- Independent C6 replication (same three live probes C6 audited) —
  `r85-masked-ambiguous` → 5 violations (C6: 3→5);
  `r85-isolated-ambiguous` → 4 (C6: 3→4);
  `r85-harbor-repro` → 7 (C6: 5→7);
  `r85-unique-break-control` → 1, unchanged. Every old finding line is present
  in order; only additions and the summary footer changed, exactly as C6's
  additions-only audit states.
- Full census — one run per immediate `corpus/fixtures/*/` directory, histogram
  `{0: 30, 1: 108}` for 138 directories. Cross-checks: 138 keys in
  `followup/r87-extended-tuples.json`, 0 keys without a directory on disk, and
  I3's five r87 rows all `match: true`.
- Precedent replays — `r35-bell7-conflict` exit 0, `r36-bell7-wrong-date` exit 0,
  `r37-ledger-unique` exit 0, `contradictions` exit 1.
- Source check — `FetchURL("https://etcsl.orinst.ox.ac.uk/section1/tr141.htm")`
  returned the composition; lines 122–163 match the note's description (see
  "Work performed"). `grep -c etcsl corpus/knowledge/reference-ledger.md` → 0.

## Findings & named debt

1. The C3 cluster satisfies all four invariants this seat was asked to verify,
   with one documented limit (V3 sub-finding: `keeps_watch_with` cites a source
   that has no excerpt in the fixture).
2. S3's five rejected-fit rulings are confirmed against the declarations;
   S3 and K1 agree on the chousa method edge; the K1-observed S3 absence was a
   work-wave ordering artifact.
3. Coverage documentation is incomplete: no Round 87 section in
   `corpus/fixtures/README.md`; two new fixtures declare no expected exit; one
   fixture README attributes its declared exit to S4 rather than the README.
4. `corpus/knowledge/holder-assessment-boundary.md` is stale against the
   delivered C1 checker (one-notice wording) — I2's authorized refresh is still
   owed.
5. The ETCSL citation is not registered in `corpus/knowledge/reference-ledger.md`
   despite `seed.md:26-29` naming the ledger as the entry point for real-world
   references.
6. `art-east-asian-design`, named as the rights-claim recipient in
   `PROVINCE.md:9`, does not exist at the fleet root (fleet-wide issue; also
   named by three other lanes).
7. Not verified by this seat: the 133 inherited baseline tuples were not
   re-derived byte-for-byte against r86's recorded artifact (C6's audit covers
   that; I checked the current histogram, the 138-key extension artifact, and
   the four live probes). The I3 extension artifact was read, not regenerated.

## Verdict recommendation

| axis | verdict | evidence and bound |
|---|---|---|
| coverage | **improved** (bounded) | +5 fixture directories (133→138) and a previously absent class: a world-bible cluster with 7 entities (4 kinds, 2 factions), 4 relations incl. a reciprocal `allied_with` pair, 4 events with 3 dependency edges, one reported-not-resolved contradiction, a sourced-inspiration note and a symbolism clause map. S2 measured no mythology/folklore citation precedent anywhere in `corpus/knowledge`, `corpus/fixtures`, `corpus/live`. Replay clean, exit 0 as declared; 138-dir census and I3's extension artifact agree. Bound: breadth of the cluster's own schema, not depth of any existing rule; the citation is fixture-local and unregistered in the ledger (A4). |
| coverage (documentation sub-axis) | **unchanged / partial** | No Round 87 section in `corpus/fixtures/README.md`; two new fixture READMEs lack a declared expected exit. The fixtures are counted and replayed correctly, so the measurement sub-axis is improved while the documentation sub-axis is not. |
| adjacency (province boundary) | **unchanged, no harm** | Cluster stays inside `PROVINCE.md:3,5-9`; all five sibling refusals verified; no lane's scope silently absorbed. The C3/Chousa line remains a wording gap, not a boundary move — refine `PROVINCE.md:5-8` and the verdict becomes **unprovable-but-better**. |
| calibration (not this seat's remit; observed only) | **improved** (as measured by others, replicated here) | C1's per-record disclosure adds findings only on the four ambiguous-holder inputs; every old line preserved in order; no resumed comparison, no identity choice, no fictional-record edit. Side effect, not harm: three inherited live probe tuples change and their footers move (3→5, 3→4, 5→7); the one-notice wording in `holder-assessment-boundary.md` is now stale. |
| depth | **unchanged** | No new checker rule was added by C1 or C3 in the delivered tree; the cluster is new coverage of existing rules. |

No trade is recorded as an improvement: the documentation gaps, the stale
boundary doc, and the unregistered citation are all reported as debt rather than
folded into the coverage gain.

## Handoff

- Land only `lore-shokunin/.ufo/waves/round-87/followup/JCOV2.md` and
  `lore-shokunin/.ufo/waves/round-87/followup/JCOV2-adjacency.json` from this
  seat. No tracked file, checker, fixture, or knowledge file was written; no
  commit, push, or registry write was made.
- Integrator actions recommended (in order): (1) refresh
  `corpus/knowledge/holder-assessment-boundary.md` to the delivered two-notice /
  per-record disclosure output (I2's authorized file); (2) append a `## Round 87`
  section to `corpus/fixtures/README.md` and add a declared expected exit to the
  two `r87-masked-break-*` READMEs and to `r87-myth-cluster/README.md`;
  (3) refine `PROVINCE.md:5-8` to name the lore/chousa source-method split;
  (4) decide whether the ETCSL citation belongs in
  `corpus/knowledge/reference-ledger.md` (or record explicitly that fixture-local
  inspiration notes are the intended home); (5) raise the dangling
  `art-east-asian-design` recipient name as a fleet-level item.
- Do not read this report as a rights conclusion: no rights or AI-training
  permission determination was made or implied by this seat.
