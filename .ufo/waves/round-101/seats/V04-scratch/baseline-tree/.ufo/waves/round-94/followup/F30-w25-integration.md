# F30 — w25-integration (docs/registry integration review)

**Seat:** F30, r94 FOLLOW-UP wave, leaf. **Role:** take W25's minimal docs/registry proposals, check each against the delivered tree, and produce the integrator's pre-closure checklist with priorities. Read-only: no corpus, tool, or sibling-report writes were made; this file is the sole artifact.

## Evidence base

- `git rev-parse HEAD` → `65a9329` (FOLLOW-UP declaration commit; WORK candidate `abbc3e0`, baseline `9c2eea3`); `git status --porcelain` → empty (clean worktree).
- Inputs read: `.ufo/waves/round-94/work/W25.md` (all 64 lines), `W06.md`, `W12.md`, `.ufo/waves/round-94/wave-spec.md`, `wave-spec.json`, `SCORECARD.md:369-383`, `LOG.md` r94 declaration, `PROTOCOL.md` (fleet root) `360-406`, `SKILL.md` (lane, 79 lines), the three corpus READMEs, both tool contracts, `corpus/fixtures/r94-paired-crossing/README.md`.
- Governing deferral rule (why "not implemented" is correct, not a defect): `wave-spec.md:31` — "Documentation/registry additions are appended after the actual tools/files exist and their commands run"; `wave-spec.md:34` — "No capability row or final verdict is entered before its demonstrated final result".

## W25 proposal → delivered-tree status (four proposals, four NOT implemented)

| # | W25 proposal | Status | Evidence |
|---|---|---|---|
| 1 | `corpus/README.md`: Round 94 section indexing the fixture README + `knowledge/r94-cross-myth-design-comparison.md` | **NOT implemented** | `grep -n "r94\|Round 94\|Round-94" corpus/README.md` → rc=1, no lines; `grep -c` → `0`. Headings are lines 1, 12, 16, 22, 30 only; `### Myth-comparison fixture clusters` (line 16) lists r87/r88/r93 and no r94 entry |
| 2 | `corpus/fixtures/README.md`: Round 94 usage subsection | **NOT implemented** | `grep -n "r94\|Round 94\|Round-94" corpus/fixtures/README.md` → rc=1; `grep -c` → `0`. Last sections remain `## Round 93…` (line 1099) and `### 2026-10-17 correction: Round 90 support-receipt shorthand` (line 1133) |
| 3 | `corpus/tools/README.md`: Round 94 addendum for `map_obligations.py` | **NOT implemented** | `grep -n "r94\|map_obligations" corpus/tools/README.md` → rc=1; `grep -c` → `0`. Last sections: `### Round-93 addendum…` (line 38), `#### Boundary-document checker` (42), `#### discriminate_check.py outcomes` (74), `### 2026-10-17 correction…` (84) |
| 4 | `SKILL.md` Gate registry: `map_obligations` row | **NOT implemented** | `grep -c "map_obligations" SKILL.md` → `0`; `grep -c "map_obligations" /home/vgpnk/Projects/shokunin/PROTOCOL.md` → `0`. Registry rows are `boundary_doc_check` (line 48, owner 57), `discriminate_check` (59, owner 68), `support_check` (70, owner 79); SKILL.md is 79 lines, so a new row appends at EOF |

`map_obligations` appears in no registry or capability row anywhere in the tree; outside `corpus/tools/` the only mentions are `SCORECARD.md` (checkpoint/candidate text) and `LOG.md` (`grep -rln "map_obligations" --include="*.md" --include="*.json" . --exclude-dir=.git --exclude-dir=.ufo` → `./SCORECARD.md`, `./LOG.md`).

## The deferral condition is now satisfied: products present, commands green

W25's own gate ("do not apply until the products and commands are present", W25.md:15, 27, 38, 46, 62) was written at baseline when they were absent. On the delivered candidate they exist and run:

Presence (`test -f`, all `PRESENT`): `corpus/fixtures/r94-paired-crossing/README.md`, `corpus/knowledge/r94-cross-myth-design-comparison.md`, `corpus/tools/map_obligations.py`, `corpus/tools/map-obligations-contract.json`, `.ufo/waves/round-94/frozen/map-obligations-r93/expected.json`.

Commands, actual observed output (repo root):

```text
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing
CLEAN: schema, citations, relations, timeline; 0 violations        exit=0

$ python3 corpus/tools/support_check.py corpus/fixtures/r94-paired-crossing
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16; DISTINCT-ANCHORS 12/12
... MODES 16/16; VALIDATED-ROWS 16/16 / RESULT PASS               exit=0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing
OBLIGATIONS raw=14 mapped=14 / RESULT PASS                        exit=0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r93-m2-kojiki-cluster
OBLIGATIONS raw=12 mapped=12 / RESULT PASS                        exit=0

$ python3 corpus/tools/map_obligations.py --self-test
20 x "SELF-TEST PASS <case> exit=<n> findings=[...]" / RESULT PASS  exit=0

$ python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93
SNAPSHOT inputs=4 digests=verified
OBLIGATIONS raw=12 mapped=12
FROZEN expected=PASS/0 findings=none matched / RESULT PASS         exit=0
```

Cross-checks: self-test emits exactly 20 PASS lines and `map-obligations-contract.json` holds exactly 20 `self_test.cases` (both counted = 20). `--frozen`'s `expected.json` pins SHA-256 for all four inputs (`entities.json` `19f75678…`, `relations.json` `32b79cd4…`, `timeline.json` `69da079e…`, `claim-excerpt-map.md` `17f0e812…`), satisfying PROTOCOL.md:375-382 "Two evidences" (self-test + digest-pinned frozen run) — so the row is registry-eligible as a **gate**, not a probe.

C1 support for proposal 2's wording: `python3 .ufo/waves/round-94/work/W01-preservation.py` → exit 0, `INHERITED: 4/4 entity records, 2/2 timeline events, and 2/2 source records parsed-value equal`, `COUNTS: 4/0/2 -> 5/1/3`, `TICK 10: both … dependencies present`, `MAP: 14 unique canonical JSON pointers`. So the fixtures-README sentence "inherited r88 records preserved" can cite parsed-value equality (raw files differ in bytes: `sha256sum` r88 vs r94 entities `042b6cc0d70c…` vs `026af0bc2cda…`).

W25's provisional wording can now be replaced with observed reality: entry command is `python3 corpus/tools/map_obligations.py <cluster-directory>` (positional, `--help` observed), plus `--map`, `--frozen`, `--self-test`. W25's "replace with the actual accepted command, do not register the placeholder" (W25.md:53) is satisfied by the above.

## Boundary and pin interactions ("boundary-doc touch if pinned")

- **Boundary pins intact; r94 did not touch them.** `sha256sum corpus/knowledge/holder-assessment-boundary.md` → `7f815a9389c4…` and `corpus/fixtures/check_bible.py` → `ff9fd2aa6811…`, both equal to `corpus/tools/boundary-doc-contract.json` (`document.sha256`, `checker.sha256`). `git diff --stat 9c2eea3 abbc3e0` contains no `check_bible.py` or `holder-assessment-boundary.md` entry.
- **The three READMEs are not boundary-checker inputs.** `boundary_doc_check.py:21` → `DEFAULT_DOC = "corpus/knowledge/holder-assessment-boundary.md"`; the contract pins only that document, the delivered checker and the legacy checker. Live run: default → `CERTIFIED (bounded: …)` exit 0, `replay_cases=14/14 anchors=2/2`; `--self-test` → `SELF-TEST PASS` exit 0. Doc appends to the READMEs therefore cannot break the boundary gate.
- **Do not touch the boundary doc.** It is whole-file digest-pinned and contains dated fixture-count claims (lines 129 `160 fixture directories`, 144, 147 `164`, 607 `165`). Any r94 count text added there would fail `document_drift` and require a deliberate re-pin plus self-test re-run — no r94 proposal requires it.
- **Census side effect the integrator must declare.** `.ufo/waves/round-94/work/W05-baseline-corpus.sha256` has 984 pins = 980 `corpus/fixtures` + 4 `corpus/tools`; `corpus/fixtures/README.md` is pinned at `a13d1af3…` and the current file hashes to exactly `a13d1af3…` (match). Appending W25 proposal 2 therefore **changes one pinned byte** and invalidates the "984/984 unchanged" observable as stated. `corpus/README.md` and `corpus/tools/README.md` are **not** in the census (`grep -c` → 0 each), so proposals 1 and 3 are pin-neutral. The 4 pinned `corpus/tools` files are `boundary-doc-contract.json`, `boundary_doc_check.py`, `discriminate_check.py`, `support_check.py` — `map_obligations.py` and `map-obligations-contract.json` are new in r94 and unpinned.
- Fixture directory count is now 168 (`ls -d corpus/fixtures/*/ | wc -l` → 168), consistent with `SCORECARD.md:375` (167→168).

## Registry / capability-row status for `map_obligations`

- **No admitted row, no capability row.** `SCORECARD.md:377` — "no new admitted row yet; C2 is a demonstrated candidate awaiting FOLLOW-UP and registry integration"; `SCORECARD.md:374` records the candidate results (r93 12/12, r94 14/14, self-test 20/20, frozen four digests) and `SCORECARD.md:379` lists "integrate W25's minimal docs/registry proposals and the C9 watch append" as planned. Per `wave-spec.md:34` and the FOLLOW-UP declaration (`LOG.md`, "no capability row before a demonstrated final result"), the row may be appended only after the per-axis/calibration verdict seats and the all-axis adjudicator return; if any C2 claim fails or is unprovable, no row and no promotion.
- Registry home is the lane `SKILL.md` (`PROTOCOL.md:383-386`: "a child lane's *registry home* is its own `SKILL.md`"; row fields = name, gate|probe, entry command, verdict map, self-test command+spelling, pinned-value path, write scope, owner). Fleet root `SCORECARD.md` has no `lore-shokunin` row (`grep -n "lore-shokunin" /home/vgpnk/Projects/shokunin/SCORECARD.md` → no output), so there is no fleet-side expected-value copy to update; at most a fleet-index pointer if the fleet integrator maintains one.

## Integrator pre-closure checklist (priority order)

**P0 — decide admission before anything is appended.** Owner: the F-calibration verdict seat + final all-axis adjudicator. Evidence to weigh: r93 12/12, r94 14/14, self-test 20/20 vs the 20 persisted contract cases, `--frozen` digests verified with matching expected verdict. If harmed/unprovable → no registry row, no capability row, W25 stays a proposal.

**P1 — `SKILL.md` Gate registry row (after admission).** Append at EOF (current 79 lines) after the `support_check` row. Use the observed entry command `python3 corpus/tools/map_obligations.py <cluster-directory>` (repo root) with the optional `--frozen <dir>` demonstration; `gate/probe: gate`; verdict map `0 → clean`, `1 → failed`, `2 → could-not-evaluate`, other → could-not-evaluate; self-test `--self-test` citing the 20 cases in `corpus/tools/map-obligations-contract.json`; pinned-values path that same contract **plus** `.ufo/waves/round-94/frozen/map-obligations-r93/expected.json` (the digest-pinned snapshot); scope = canonical one-obligation-per-row mapping completeness and source-ID agreement only, no entailment/fidelity/authenticity/chronology/rights/permission/canon.

**P2 — `corpus/tools/README.md` addendum.** Pin-neutral. Use W25.md:42 wording, but replace the provisional/help-unverified sentence with the observed `--help` output and cite the observed exits (14/14, 12/12, 20/20, frozen matched).

**P3 — `corpus/fixtures/README.md` Round-94 section.** Pin-affecting: either append and re-declare the census as measured at `abbc3e0` (with a dated note that the pinned byte `a13d1af3…` for this file changed post-candidate), or record the append as a dated post-closure doc change. Must state: structural `CLEAN` is structural only; the support receipt is lexical/map-declared (14/14 JSON + 2/2 editorial); `map_obligations` covers raw-JSON↔map completeness/source-ID agreement only; whole-claim and comparison review remain manual.

**P4 — `corpus/README.md` index update.** Pin-neutral. Prefer slotting into the existing structure (`### Myth-comparison fixture clusters`, line 16 for the fixture README; `### Source, boundary and calibration records`, line 22 for `knowledge/r94-cross-myth-design-comparison.md`) rather than a bare EOF `## Round 94`, and avoid claiming the r94 minute was independently verified beyond the observed receipts.

**P5 — boundary doc: no touch.** If ever touched, re-pin `boundary-doc-contract.json` digest and re-run both boundary commands; not required by r94.

**P6 — housekeeping note.** `corpus/fixtures/r94-paired-crossing/README.md` already carries the two repository-root replay commands, so P3/P4 are index-level, not the fixture's only navigation surface.

## Verification boundary

This seat ran read-only commands on the delivered candidate and read files; it implemented nothing and changed no corpus, tool, or sibling artifact. The registry admission decision itself is **not** made here — it remains with the verdict seats and adjudicator. All green results above are the tool's own outputs on the delivered revision; they do not establish entailment, fidelity, authenticity, chronology, rights, permission, or canon, and no outside non-author verification is claimed.

**Bottom line: PASS** — all four W25 proposals are verifiably unimplemented (consistent with `wave-spec.md:31` deferral), their unblocking condition is now met by present, green products, and the prioritized integrator checklist with the pin/census and boundary-touch constraints is produced; capability admission itself remains correctly pending.
