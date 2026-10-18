# V39 — receipt (round 99)

**Seat:** V39 `receipt`. **Role:** presence audit of the 128 declared round-99 seats and authoring of the skeleton receipt at `.ufo/waves/round-99/receipt.json`. V39 judges **no claim** (C1/C2) and **no axis**. It records presence and bytes. It does not re-adjudicate any seat and does not smooth an ABSENT into a presence.

**Axes for this seat (godspeed):** presence completeness (every declared seat accounted), byte honesty (sha256 only of files that exist; no invented agent ids), schema fidelity (`agent_id` / `outcome` / dispatch ids left null for the L1), non-interference (exclusive writes only), freshness (poll bound and snapshot times quoted).

**Lane root for every command:** `/home/vgpnk/Projects/shokunin/lore-shokunin` (session cwd is the parent repo). **Baseline:** r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). **HEAD at the 22:22 audit:** `337f0fa52b02626b7687eedbb2d99fab30446fe4` (`337f0fa` records the blocked first dispatch; zero corpus increment). `git merge-base --is-ancestor 4265df5 HEAD` was exit 0. The re-dispatch tree is uncommitted. Leaf seat: no nested agents, no commits, no pushes, no network.

Writes by this seat: this report, `.ufo/waves/round-99/receipt.json`, and `.ufo/waves/round-99/seats/V39-scratch/` (`expected.json`, `poll.log`, `poll-meta.json`, `V39-receipt-builder.py`, `audit.json`, `audit-summary.txt`).

## 1. Dispatch context

LOG.md declaration at `## Round 99 — declaration before dispatch (2026-10-17)` stands. `git diff --stat HEAD -- LOG.md` was empty at audit time, so this re-dispatch did not rewrite the declaration. The blocked attempt (all 128 seats `502 "shim: token helper printed nothing"`) is the commit at HEAD and left no reports; it is not this snapshot. This audit is of the re-dispatch that actually wrote under `.ufo/waves/round-99/`.

Roster used: **S1–S5 (5) + V01–V123 (123) = 128**. Report presence = a top-level `seats/<SEAT>-*.md` whose prefix is that seat. Scratch directories are not reports.

## 2. Poll-wait (SELF subtracted)

Poll started 2026-10-17T22:03:11-0300. Cadence 20 s, max 40 tries. A seat counted as present only when its report file existed. Producer artifacts checked for existence (not for claim truth): the 10 `corpus/fixtures/r99-window-lapse/` files, `corpus/tools/dependency_freeze.py`, `corpus/tools/dependency-freeze-contract.json`, `corpus/tools/README.md`, `SKILL.md`, `corpus/knowledge/r99-gate-blind-spot-table.md`, `corpus/knowledge/r99-lapse-scope-note.md`. Early stop was allowed only if all five producer reports and all 16 artifact paths existed and the report-file set was unchanged for 3 tries. That condition never fired. V39's own report did not exist during the poll (ENDGAME: all-reports poll subtracts SELF). Expected others = 127.

Opening look, before the poll loop (22:02:58-0300):

```
$ date '+%Y-%m-%dT%H:%M:%S%z'
2026-10-17T22:02:58-0300
$ git rev-parse HEAD
337f0fa52b02626b7687eedbb2d99fab30446fe4
$ git rev-parse 4265df5
4265df5e86e4121bde4125b649b89bb1676676a5
$ git merge-base --is-ancestor 4265df5 HEAD && echo baseline_is_ancestor=yes
baseline_is_ancestor=yes
$ ls -1 .ufo/waves/round-99/seats/*.md | wc -l
2
$ ls -1 .ufo/waves/round-99/seats/*.md
.ufo/waves/round-99/seats/S3-fixture-author.md
.ufo/waves/round-99/seats/V80-c2-prose-prefix.md
```

At that instant `corpus/fixtures/r99-window-lapse/` existed (10 files) and both knowledge paths were ABSENT.

Observed poll log (`.ufo/waves/round-99/seats/V39-scratch/poll.log`), first and last lines plus the exhaustion marker:

```
try=1 2026-10-17T22:03:26-0300 reports=3 roster_present=3/128 producer_missing=['S1', 'S2', 'S4', 'S5'] artifact_missing=2 unexpected=-
try=40 2026-10-17T22:16:26-0300 reports=13 roster_present=13/128 producer_missing=['S1', 'S2', 'S5'] artifact_missing=2 unexpected=-
POLL-EXHAUSTED tries=40; writing receipt from last observation. ABSENT stays ABSENT.
```

`poll-meta.json` names the two missing artifacts at try 40:

```
corpus/knowledge/r99-gate-blind-spot-table.md
corpus/knowledge/r99-lapse-scope-note.md
```

S4's report landed between try 2 and try 3 (producer_missing dropped S4). S1, S2, and S5 reports were absent on all 40 tries. No stall-escape. Bounded exhaustion is the stop, not a claim that a later seat cannot still write.

Two reports landed after try 40 and before the 22:22 audit, observed by mtime, not inferred: `V41-anchor-replica-2.md` (22:17:06) and `V12-c2-support-map.md` (22:21:50). They are present in the audit below because the files existed. Seats with no file at the receipt snapshot stay ABSENT.

## 3. Presence audit at 2026-10-17T22:22:17-0300

Command (lane root):

```
$ python3 .ufo/waves/round-99/seats/V39-scratch/V39-receipt-builder.py
{
 "snapshot": "2026-10-17T22:22:17-0300",
 "present_incl_self": 15,
 "present_excl_self": 15,
 "absent": 113,
 "producer_absent": ["S1", "S2", "S5"],
 "missing_candidates": [
  "corpus/knowledge/r99-gate-blind-spot-table.md",
  "corpus/knowledge/r99-lapse-scope-note.md"
 ],
 "duplicates": {},
 "header_mismatches": 0,
 "unexpected_md": [],
 "parent_tree_md": [],
 "head": "337f0fa52b02626b7687eedbb2d99fab30446fe4",
 "baseline_ancestor": true
}
```

V39 was not in that 15 (this file did not exist yet). **15/128 reports on disk, 113 absent, including this seat.** Full absent list is in `V39-scratch/audit.json` and in `receipt.json`.

Present at that audit, with sha256 of the bytes then on disk:

| seat | file | bytes | sha256 |
|---|---|---:|---|
| S3 | S3-fixture-author.md | 5069 | `3d81a75e0f154ed6c2297da8a9521391797a81740e0ede5443070b0c471cf73a` |
| S4 | S4-fixture-docs.md | 9303 | `61bfdec1f5b7bbcdda653230bb4be1b6c1913683af67e2ae02e4ee46a327f72f` |
| V10 | V10-c2-checker.md | 6894 | `9ee8c876b7ff1be1481c7219b06307163ed5a0553ef168bdda23e677f99f7f45` |
| V11 | V11-c2-inherited-equality.md | 13546 | `a2f60b65b440efd0b178c5c314fc51ded510e8b8bd80db3c0ce6fd87b2d20e03` |
| V12 | V12-c2-support-map.md | 10805 | `b559cdb76adbebc6791e3b784d92188437f4195a828120ac9c9b522028fc9246` |
| V13 | V13-c2-anchors.md | 12948 | `a7ef2d47c29e97cfe41f93800f0fc1a24ca6ad6a636734f4517300d70c2778dd` |
| V41 | V41-anchor-replica-2.md | 9792 | `40af4141891fe1d0a91017080d5ce232e2e252743811ec61dc8c751e984ea0d6` |
| V47 | V47-byte-prefix-2.md | 14225 | `321491fb9b0757f867b5e0cc45338bc106960908f64eb3b8c37aed47ab8c5410` |
| V68 | V68-adjacency-2.md | 7930 | `d1ab2308693704bcb848559e051ede400414cac29807fe8a52f8a734b6d1ae97` |
| V77 | V77-c2-map-inventory.md | 8641 | `e51103276a7db11c4a5c9ed188ec396c34962d320efd1910f0cbea151c8ce7f1` |
| V80 | V80-c2-prose-prefix.md | 7122 | `aaf5b0d1c47b44478bcac40af92c81bb2bce1025d41add69e1494283b08d2cee` |
| V86 | V86-c2-no-new-entity.md | 9403 | `775bd16a31f906bc3cc2f4a14139504598ddd9c907725e4e864412d258b0a38f` |
| V105 | V105-c2-event-description.md | 9976 | `3668a34e84ee36a5ce2e3cdbffe9ce4eb34982f786b53f13013b0bcf39d0d1e2` |
| V109 | V109-c2-inherited-map-rows.md | 5160 | `8bcbd46a1f5888cc99bb7a8e29947a6ae5a81e5455b917ac00d7c5e25495c362` |
| V119 | V119-c2-anchors-3.md | 9125 | `9206493b7fe5fb982f53756d2f1d260d91e6ce265d3c7c7f14277a82efc66b35` |

Integrity at that audit: duplicate report prefixes **none**; header/seat mismatch (first line must start with `# <seat>`) **none**; unexpected top-level `.md` **none**; parent-tree `*.md` under `/home/vgpnk/Projects/shokunin/.ufo/waves/round-99` **none** (`find` printed nothing). `receipt.json` did not yet exist.

Scratch-without-report is not presence. `S1-scratch/` and `S2-scratch/` existed; `S5-scratch/` did not. Many verifier scratch dirs existed without a report. Those seats were dispatched and had started; their reports were still ABSENT. Not inferred.

`git status --porcelain=v1` captured inside the same audit:

```
 M corpus/tools/dependency-freeze-contract.json
 M corpus/tools/dependency_freeze.py
?? .ufo/waves/round-99/
?? corpus/fixtures/r99-window-lapse/
```

LOG.md and SCORECARD.md are clean versus HEAD. The declaration is unchanged.

## 4. Producer artifacts — existence only, not a claim verdict

This seat does not run C1 or C2 checks and does not treat an in-flight edit as a delivery.

Missing at the audit (ABSENT, not verified):

- `corpus/knowledge/r99-gate-blind-spot-table.md`
- `corpus/knowledge/r99-lapse-scope-note.md`

Present as files, owner report absent, so not a confirmed delivery:

- `corpus/tools/dependency_freeze.py` sha256 `6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067` (29104 bytes, mtime 22:07:33; working tree modified vs HEAD). S1 report ABSENT.
- `corpus/tools/dependency-freeze-contract.json` sha256 `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628` (25987 bytes, mtime 22:08:46; working tree modified vs HEAD). S1 report ABSENT.
- `corpus/tools/README.md` sha256 `294dd56f29ce1fd40be3a80d365b33724c9cd1969d3f7b7abb271fd1adaaa207` (mtime 21:32:05, before this wave). S2 report ABSENT.
- `SKILL.md` sha256 `22ffaa822ec7614fa85322f7fa07e6f369c0888e1107f9f297f76a14e18c20c5` (mtime 21:34:23, before this wave). Observed freeze row still states the pre-C1 bound (`17 cases`; "pin payload covers the JSON tables only"; "BR-01's markdown/prose half remains open"). That is a byte observation, not a C1 verdict. S2 report ABSENT.

`corpus/fixtures/r99-window-lapse/` had exactly these 10 files: README.md, claim-excerpt-map.md, contradictions.json, entities.json, fictional-excerpts.md, inspiration-note.md, relations.json, source-excerpt.md, sources.json, timeline.json. S3 and S4 reports were present. Hashes are in `receipt.json` `candidate_revision_pinned`. This seat does not judge the lapse claim.

## 5. Skeleton receipt

`.ufo/waves/round-99/receipt.json` is the skeleton. `dispatch_tool_call_id`, `returned_summary`, `served_backend_echo`, and every seat's `agent_id` and `outcome` are **null** for the L1 to fill from the AgentSwarm result. None invented.

The receipt's collection is a re-audit taken after this file is closed, not the 22:22:17 table. The first receipt write was not immediate: it landed at 2026-10-17T22:37:23-0300 with 46 reports present (including this file) and 31 seats changed since the quoted audit. That first JSON is preserved at `seats/V39-scratch/receipt-223723.json` and is superseded by the post-correction `receipt.json`, which re-pins this file's sha256. Drift from the 22:22:17 audit is `collection.changed_since_pre_receipt_audit`. This report does not quote `receipt.json`'s own sha256 (that would make the two files mutually hash-dependent) and is not rewritten again to chase later landings.

Absent seats stay `reports: null`. Present seats carry `report_path` and `report_sha256` of the bytes at the receipt snapshot.

## 6. Honesty

V39 records presence and bytes. It adjudicates no claim and no axis. Producer reports S1, S2, and S5 were absent for all 40 poll tries and at the 22:22 audit; the two S5 knowledge files were absent for the same window. Those absences are recorded, not inferred, and no plan was verified in their place. The wave was still landing verifier reports after the poll bound; a later seat or the L1 may supersede this skeleton. This snapshot does not claim 128/128.

**Bottom line:** PASS — 128-seat presence audit recorded and skeleton `receipt.json` written with `agent_id` null; 15 other reports hashed at the 22:22:17 audit; S1, S2, S5 reports and both knowledge files ABSENT after 40×20s (not inferred, no claim verified).
