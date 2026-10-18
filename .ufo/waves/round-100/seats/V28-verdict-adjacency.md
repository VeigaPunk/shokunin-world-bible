# V28 — verdict-adjacency (round 100)

Seat: V28, leaf verifier in the 32-seat single wave. **One axis verdict: adjacency unchanged / not harmed (PASS, bounded).** Depth, coverage, calibration, operability, and freshness are named as non-regression witnesses, not independently scored or averaged here. This is not a round-admission, promotion, testimony-truth, rights, or canon verdict.

Subject: delivered uncommitted wave bytes against r99 closure `fe1ce466e9d7427948c0abe4ecfbf961880b72ff`. HEAD throughout the battery was `b5fe472957ab1e4e9c90f5613acc14cd24a288ae`, the committed pre-dispatch r100 declaration; `ae67105` between baseline and HEAD carries the r99 SCORECARD closure. Battery commands ran from `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`.

Only V28 writes: this exclusive report and `.ufo/waves/round-100/seats/V28-scratch/`. Every persistent scratch file is enumerated with absolute path, size, and SHA-256 in `V28-scratch/file-manifest.json` (154 files / 1,508,768 bytes before the manifest itself). No production file, other seat's scratch, sibling file, credential, commit, push, or network operation was written/performed by this seat. No nested agent. No needed background task remains.

## Producer gate and measurement identity

Actual readiness command:

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V28-scratch/poll.py
```

`poll.jsonl` records checks 1–23, 20 seconds apart, `23:33:01.413445`–`23:40:21.422820 -03:00`, with an unchanged 40-check maximum. It required all ten r100 fixture files, the contract/README/SKILL, both new knowledge documents, the blind-spot table, AND individual nonempty T1/T2/T3/T4 reports. Final observed output:

```text
READY artifacts=16/16 producer_reports=4/4; manifest=V28-scratch/ready-manifest.json
```

T2 first appeared at check 3, T1 at 7, T3 at 14; all artifacts at 15; T4's report at 23. No battery was run on the earlier incomplete states. No poll counter restart, timeout, stall escape, all-reports wait, or self-inclusive count occurred. An earlier preflight presence probe was not an additional polling loop or a verdict.

The readiness manifest's SHA-256 is `bb8876d3f043803691a38ce72cc7c99642543e7b28de1e73ee01ce68c56d085c`. It includes artifact and producer-report hashes. Audit at `23:40:30`, post-battery check at `23:40:59`, and final check at `23:41:56` all observed `changed_since_ready=[]`. Evidence: `ready-manifest.json`, `audit-initial.json`, `audit.json`, `audit-final.stdout`, and `final-stability.json`.

## 1. Charter and byte-ownership boundary

Actual audit command (exit 0; repeated after the audit-predicate correction described below):

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V28-scratch/audit.py
```

Observed `PROVINCE.md` identity against the declared baseline:

```text
base/work blob: 7c599c395e1710b6a7c7aca6d485c373bed6deb7
base/work SHA-256: 94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa
git_diff_charter_bytes: 0
```

SHONEN, root README, `l0-questions.md`, the delivered checker and all four gate implementations are also byte-identical to baseline. No expansion of PROVINCE's owned domain or refusals occurred (`PROVINCE.md:3-11`).

Whole-tree audit: **2,852 baseline non-`.ufo` tracked files**, six changed, zero missing, zero symlinks. Actual `git diff --numstat fe1ce46` observations:

```text
57   0  LOG.md
33   0  SCORECARD.md
3    2  SKILL.md
105  0  corpus/knowledge/r99-gate-blind-spot-table.md
60   0  corpus/tools/README.md
124  1  corpus/tools/dependency-freeze-contract.json
```

Attribution is exact:

- T1: contract, tools README, dependency-freeze registry section only (`SKILL.md:92-102`). The final audit reports `skill_freeze_row_only=true`; the trigger/anti-trigger, sibling-arbitration language, and all preceding rows are unchanged.
- T2/T3: exactly the ten new `r100-docket-review` files; all regular mode 0644, no symlinks. T2's initial baseline copies of README/map were subsequently owned and edited by T3, as both reports explicitly state.
- T4: exactly the two new r100 knowledge records plus the dated blind-spot-table append. Every one of the table's original **20,526 bytes is a prefix**, followed by 8,907 added bytes. The tools README is likewise a strict historical prefix plus its dated addendum.
- LOG +57 is the committed pre-dispatch declaration; SCORECARD +33 is committed r99 closure bookkeeping. Both match HEAD exactly and are not wave-seat writes.

The only untracked non-`.ufo` paths are the declared ten fixture files and two knowledge notes. The only untracked path outside the r100 wave is `.ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md`, already present in the initial seat status before r100 verification; it is not attributed to this wave. `past_waves_tracked_changes` is empty, so historical r99 reports/FAIL records were not rewritten or re-rolled.

A metadata sweep of the lane outside the r100 wave, since declaration time `23:30:55`, found only LOG and the declared 16 producer artifact paths; no ignored lane-root scratch residue or extra fixture appeared. Exact list: `lane-outside-wave-mtimes.json`. This is a bounded observation, not process tracing of deleted temporaries.

The contract is **not textually addition-only**: the guarded writer refreshes top-level `revision` from `337f0fa…` to `b5fe472…`. Parsed comparison observed only added pin `r99-window-lapse`, no removed pins, `prior_pins_changed=[]`, and no other non-revision metadata change. All seven paths resolve under `corpus/fixtures/`, all payload versions are 2, and all seven pins have ten file digests. T1's recorded actual authoring operation is the guarded `python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/r99-window-lapse`; this seat never re-froze the delivered contract. See T1 report:29-42 and tools README:369-389.

## 2. Parent/sibling boundary

Actual command, exit 0:

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V28-scratch/outside.py
```

Observed at `23:40:33`, metadata sweep since `23:30:55`, excluding `.git`, dependency/build directories, sensitive-file names, and the lore lane itself:

```text
parent_git_status: ""
parent_round100_wave_exists: false
parent_round100_strays: []
recent_counts: {"kotodama-shokunin": 56}
```

Those 56 paths are Kotodama's concurrent round-16 reports, own tooling, and `.scratch` activity. No other sibling or parent content path was newer in this bounded sweep. A dedicated Grep search over Kotodama `*.{md,json,py,yml,yaml}` for `r100-docket-review|r100-crossing-arc-synthesis|r100-provenance-semantics-boundary|clerk-review-first-passage|clerk-review-note` returned **No non-sensitive matches found**. No outside file contents or credentials were collected by the metadata sweep.

No r100 lore-attributable parent-cwd stray or sibling-domain write was found. This is fleet-root metadata plus a bounded content-leak search, not a claim to have audited every host path or traced every writer. Chousa's research-method ownership, Game-dev-2d's mechanics ownership, and Kotodama's generative/cultural craft remain read-only adjacent provinces; the new lore records absorb none of them. Their charter refusals were read, not edited.

## 3. Fiction/external-source separation and refusal scan

Preservation measured by the audit, not inferred from counts: six entities, one relation, eight inherited events, eight inherited sources, and the empty contradiction table are value-preserved. `entities.json`, `relations.json`, `contradictions.json`, `inspiration-note.md`, and `source-excerpt.md` are byte-identical to r99. All **5,114** r99 fictional-excerpt bytes are a prefix of the new **5,961** bytes. New counts are 6 entities / 1 relation / 9 events / 9 sources / 0 contradictions; every source kind is `fictional ...`.

A dedicated Grep on every r100 `*.json` for `Spence|Kojiki|Chamberlain|Gutenberg|ETCSL|Inana|Ovid|Maya|Kiche|K'iche` (case-insensitive) returned **No non-sensitive matches found**. Spence remains exactly two separately labelled editorial rows, not JSON facts or an in-world witness (`claim-excerpt-map.md:45-52`). The copied inspiration note keeps attribution, rights, and AI-training permission distinct and open.

The authored scenario was read end-to-end, including the new source/event values and `fictional-excerpts.md:78-88`. The five quoted lines at 82–86 say the entry remains open, no new filings have been lodged, the clerk makes no finding and resolves nothing, and both accounts stand unresolved. README:11-21 and map:72-74 qualify chronology, testimony truth, literal JSON syntax, and lexical-versus-whole-claim support. No gate is being treated as authentication.

Both knowledge records retain the same boundary. The synthesis explicitly resolves the naming ambiguity as r94 seed + six continuation beats = seven snapshots (:8), bounds “unresolved throughout” temporally (:48), does not fabricate a pre-r98 OPEN docket, and separates the seven dossier snapshots from the seven frozen fixtures (:63). Its non-establishment section (:52-59) refuses truth, chronology authentication, expanded duty, automatic source identity, rights, and permission. The semantics note (:8-28) confines “semantic inventory” to modeled JSON comparison, not natural-language understanding.

The complete scan input was generated by the audit: `round-new-bytes.txt`, **94,106 bytes**, SHA-256 `224b3a6275435cc3bb498c1c5accc60b77181a330953cb91fca893a20f58f8fe`: zero-context diffs of the four changed producer-owned tracked files plus full bytes of both new notes and all ten fixture files. Actual dedicated Grep pattern:

```text
(?i)\b(mechanics?|gameplay|ruleset|damage|stats|balancing|combat|dice|hit[ -]?points?)\b|public domain|fair use|free to (use|reuse)|permission is granted|licensed under
```

Observed: **No non-sensitive matches found**. The broader `rights|licen[cs]e|copyright|permission|canon|training|attribut` search was inspected completely: matches are refusals/open questions, attributed fictional records, or JSON-pointer “canonical” terminology, not rights grants or canon certification. The path/sibling-name scan found only unchanged `../PROTOCOL.md` text in Git hunk labels and three statements of this lane's own absolute working directory; no new sibling write target or `/tmp/` path.

## 4. Full running battery and negative boundaries

Actual battery command, exit 0:

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V28-scratch/battery.py
```

Observed summary: **211 real CLI invocations**, `expected_exit_mismatches=[]`, `stderr_cases=[]`. Complete actual argv, stdout, stderr and exit codes: `battery-results.json` and `battery-transcript.txt`; summary: `battery-summary.json`.

Representative delivered scenario commands and observed results:

```text
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r100-docket-review
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r100-docket-review
OBLIGATIONS raw=22 mapped=22
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24
RESULT PASS
exit=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r100-docket-review
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24; DISTINCT-ANCHORS 20/20
SOURCE-SUPPORT 22/22; EDITORIAL-ANCHORS 2/2; ... MODES 24/24; VALIDATED-ROWS 24/24
RESULT PASS
exit=0
```

The support excerpt omits unchanged individual PASS rows; the full stdout is retained. Further observed outcomes:

- Seven live frozen-chain invocations: 7/7 `RESULT PASS`, exit 0. r99 prints `events 8/8; dependency-edges 7/7; relations 1/1`, digest `7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e`.
- The live r100 freeze invocation intentionally returns `UNPINNED-FIXTURE`, `RESULT ERROR`, exit 2. Its tick-16 edge is not silently claimed pinned.
- Bible census of all 174 fixture directories: **40 clean, 134 intentional negatives, 421 VIOLATION lines, no other exits or stderr**. This preserves the inherited 134/421 negative corpus and adds the one clean review fixture.
- Support and mapping replays across r88/r93/r94–r100 passed. r87/r89 mapping remain expected `unsupported_map`, exit 2; their lexical support receipts still exit 0.
- Byte-identical scratch mirrors ran the standard real-CLI self-test flags: freeze **18/18**, map **25/25**, both exit 0. Mirror tool/contract identity was explicitly checked. Direct live-root versions were not run because their temporary directories would exceed this seat's exclusive scratch boundary.
- `python3 corpus/tools/boundary_doc_check.py` → bounded `CERTIFIED`, receipts 3/3, cases 14/14, anchors 2/2, exit 0. `--self-test` → eight controls PASS, exit 0; `TMPDIR` points to V28 scratch.
- `python3 corpus/tools/discriminate_check.py` → `DISCRIMINATION HELD`, exit 0; `--checker e97613c` → expected `REGRESSION-DETECTED`, exit 2. The watch file is byte-unchanged; no new C9 check-log row is claimed by this seat.
- `python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93` → four digests verified, expected PASS/0 matched, exit 0.

Actual isolated boundary-control command, exit 0:

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V28-scratch/boundary-replays.py
```

Observed **15/15 expected outcomes**, `failed=[]`, live and all mirror contracts unchanged at SHA-256 `ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5`:

- Clean r99 copy PASS/0; excerpt-only mapped-anchor removal makes support FAIL/1 and freeze `DIGEST-MISMATCH`/2, while bible/map remain green.
- Coherent excerpt+anchor replacement leaves bible/map/support green but freeze names both changed files and exits 2. These are byte/lexical outcomes, not semantic judgments.
- Dropped tick-15 edge reports `REDUCTION-DETECTED`/1 without `DIGEST-MISMATCH`.
- Combined fixture + `--freeze` reports only `INVALID-ARGUMENTS`/2; outside-scope freeze refuses `SCOPE-REFUSED`/2 without a contract write; a foreign same-named copy refuses `PATH-MISMATCH`/2.
- Editing r88's outside-the-ten `symbolism-clause-map.md` remains PASS/0; a newline-only `source-excerpt.md` edit names that file in `DIGEST-MISMATCH`/2. Both documented bounds hold.

Complete exact commands and stdout: `boundary-replays.json` / `.txt`; summary: `boundary-replays-summary.json`. Additionally, seven exact read-only commands from T4's delivered table rows 10–12 were independently rerun on its already-created mirrors (not its mutating preparation harness). `t4-row-replay.json` records historical support FAIL/1, delivered support FAIL/1, historical freeze PASS/0, delivered freeze ERROR/2, edge+prose reduction FAIL/1, prose-only digest ERROR/2, and combined invalid ERROR/2. All seven matched; the live contract hash was unchanged. Thus the dated correction rows' refusal semantics were exercised, not accepted on author assertion alone.

## 5. Ordering, audit correction, and limits

Every artifact mtime precedes its final owning report; final audit observed no exceptions:

- T1 artifacts latest `23:33:36.053074`, report `23:35:33.507343`.
- T2 latest `23:32:26.219905`, report `23:33:39.600083`.
- T3 latest `23:35:32.293340`, report `23:37:15.388561`.
- T4 latest `23:38:32.885720`, report `23:40:12.515917`.

The initial audit returned `skill_freeze_row_only=false`: its predicate incorrectly prohibited any new bullet after `owner`, despite the owned section extending to EOF. `git diff fe1ce46 -- SKILL.md` showed only the seventh-fixture entry, updated pinned-values bullet, and dated supersession bullet inside `### Dependency-edge freeze check`; the actual file was read. I corrected **only V28's scratch predicate** to compare the prefix and section boundaries, then reran it: true. The original false output is preserved in `audit-initial.json`. No production byte was altered to make a test pass; this is a disclosed verifier false alarm, not a re-rolled province verdict.

`git diff --check` exited 0 with no output; untracked files were not misrepresented as covered by that command. The initial missing lane AGENTS/QUALITY Reads were preflight observations, not r100 regression findings. Existing absence of support/discriminator self-test modes is carried registry debt, not a newly claimed capability.

Outside-write evidence is bounded to the stated fleet-root sweep and search, not a machine-wide forensic guarantee. Gates establish their declared structural, lexical, mapping, inventory, byte, and regression properties only. r100 remains unpinned; r88's eleventh symbolism file remains unpinned. No external reference was fetched or authenticated. SHONEN remains four `[~]` and no `[x]`; same-lane verifier dispatch is not outside promotion verification.

PASS — ADJACENCY unchanged / not harmed on the delivered r100 bytes: charter and prior fixtures preserved, changes confined to declared ownership, no lore-attributable parent/sibling breach found, external material remains editorial-only, rights/mechanics/authentication refusals hold, and the full running battery plus negative-boundary controls match their declared bounded outcomes.
