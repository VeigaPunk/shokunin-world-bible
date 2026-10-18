# V58 — presence-final (round 98, completion wave)

**Seat scope:** final presence audit for round 98. Verify (a) every roster
seat's report exists, (b) producer artifacts all present with hashes, (c) no
duplicate seat prefixes, (d) no header/filename seat mismatches, (e) the
`r98-clerk-filing` fixture's 10 files plus map and README, and the three
knowledge notes exist. Read-only over the lane tree; this report is my only
write.

Repo root for every command: `/home/vgpnk/Projects/shokunin/lore-shokunin`
(session cwd is the parent repo). Baseline r97 closure `9a3d648`
(HEAD during the round `dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb`, wave tree
uncommitted). Leaf seat: no nested agents, no commits, no pushes, no network.
Completion-wave re-dispatch (original V58 aborted by host interruption); the
lane carries a prior V58 scratch run (`V58-scratch/`, 20:28–20:59) whose
snapshots I re-used as corroboration, and I re-verified everything live.

---

## 1. Roster and report presence

Roster is defined by the LOG.md round-98 declaration ("64 seats: 5 producer
seats + 59 verifier/judge seats") and by V36's own roster constant
`ROSTER = ["S1".."S5"] + ["V01".."V59"]` in
`V36-scratch/V36-receipt-builder.py`. There is **no V60–V64**; the 64 seats
are exactly S1–S5 + V01–V59.

Command:

```
cd .../round-98/seats
for i in $(seq -w 1 64); do f=$(ls V${i}-*.md 2>/dev/null | head -1); \
  if [ -n "$f" ]; then echo "V$i OK $f"; else echo "V$i MISSING"; fi; done
```

Observed: 58 seat reports present — **5 producers (S1–S5) + 53 verifiers**.
`ls V*.md | wc -l` → `53`; `ls S*.md | wc -l` → `5`.

**Absent at my cutoff (6, all marked ABSENT, none inferred):**

| Seat | Status | Evidence |
|------|--------|----------|
| V20  | ABSENT | no `V20-*.md`; `V20-scratch/` exists (aborted mid-run) |
| V31  | ABSENT | no `V31-*.md`; no scratch |
| V36  | ABSENT | no `V36-*.md`; `V36-scratch/` has a completed stall poll and a skeleton receipt builder (aborted after writing the skeleton) |
| V51  | ABSENT | no `V51-*.md`; no scratch |
| V57  | ABSENT | no `V57-*.md`; no scratch |
| V58  | ABSENT (pre-redispatch) | `V58-scratch/` exists; this re-dispatch is the replacing run |

These are precisely the six endgame seats named as aborted by the host
interruption. **58/64 present; 6/64 ABSENT** (V20, V31, V36, V51, V57, V58).
No other seat is missing.

## 2. Duplicate prefixes / header mismatches / stray files

- **Duplicate prefixes:** none. `ls V*.md | sed 's/^\(V[0-9]*\)-.*/\1/' |
  sort | uniq -c | awk '$1>1'` → empty. Each V-prefix appears at most once.
- **Header/filename seat mismatches:** none. For every `V*.md`/`S*.md` I
  extracted all `\b(V\d{2}|S[1-5])\b` tokens from the first 20 lines and
  required the filename prefix to appear:
  `HEADER-PREFIX-MISMATCH COUNT: 0`. (Spot check: `V01-*.md` header is
  `# V01 — c1-mismatch-pin (round 98, single-wave)`; `S1-*.md` header is
  `# S1 freeze-hygiene — round 98` with `- Seat: S1 freeze-hygiene`.)
- **Unexpected files in seats dir:** none beyond the roster. Only
  `V*.md`, `S*.md`, `V33-debt.json` (a declared V33 companion artifact, not a
  report), and per-seat `*-scratch/` dirs. `ls *.md | grep -vE
  '^(V[0-9]{2}|S[1-5])-'` → empty.

## 3. Producer artifacts — presence and final hashes

All producer-owned paths exist. Because the receipt snapshot (below) is stale,
these are the **final delivered-revision hashes**, measured live at my cutoff:

```
03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b  corpus/tools/dependency_freeze.py
153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947  corpus/tools/dependency-freeze-contract.json
1d299c16bf9a0b34526f4a799cdd3117867f6d4d278866b66366b78700d79b84  corpus/tools/README.md
80440d61122488a267a4f0a58a55cb54d89c037d93160f1123e5fb3b2f396f61  corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
8e9e1774c1072bd1476d86977804e945301e4583acbfcb80a81b37a2334d4827  corpus/knowledge/r95-aftermath-scope-note.md
a9b51f8ccd78e0dcd8b5e890183068e48cdccd195065c43212211b65ee25f048  corpus/knowledge/r96-response-scope-note.md
1162262c742441115681d30be588039be4f1a026b755eeb7d15c9ba41952a4b8  corpus/knowledge/r98-clerk-scope-note.md
```

`corpus/knowledge/r98-clerk-scope-note.md` is the S5 artifact the receipt
listed under `missing_candidate_paths`; it is **now present** (15 839 bytes,
mtime 20:33). The other three knowledge/tool artifacts are present and match
the delivered revision S1's own report declares (`S1-freeze-hygiene.md` names
`dependency_freeze.py` = `03d04365…` and the contract = `153ebc5b…`, both
matching the live tree).

## 4. r98 fixture and knowledge notes

`corpus/fixtures/r98-clerk-filing/` — **10 files present** (README + map + 8
JSON/MD tables), matching the LOG's declared fixture shape (6 entities / 1
relation / 7 events / 7 sources):

```
 5829 32efc78f70e6de4f9670134080711923199e8693015d3ebea75a4a1ca6362926  README.md
15028 c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba  claim-excerpt-map.md
    3 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  contradictions.json
 1793 db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984  entities.json
 4187 29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de  fictional-excerpts.md
 1956 58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  inspiration-note.md
  139 c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  relations.json
  640 b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  source-excerpt.md
 2725 32ee15b1f3d72d94f4228cbc9cefa69b7185d18b47bbe219833d7aaf30eed0f3  sources.json
 2552 eb24e0848e597efa29ed858cb8557d8f3126a47e1231f9469d719257e191e7af  timeline.json
```

The three knowledge notes exist:
`corpus/knowledge/r95-aftermath-scope-note.md`,
`corpus/knowledge/r96-response-scope-note.md`,
`corpus/knowledge/r98-clerk-scope-note.md` (hashes in §3).

## 5. Receipt audit (receipt.json already existed at my cutoff)

`receipt.json` sha256 `50251f0e4e563ec301002a902027d8138398a0457479ca1afb51ebe93c637833`.
It is a **V36 SKELETON, not a finalized receipt**, and its own `state` field
says so: *"Skeleton receipt written by V36 (receipt seat) at
2026-10-17T20:29:02-0300 … Presence audit only."* Two defects:

**(a) Collection block is un-populated.** `collection.reports_present = 0`,
`reports_present_incl_self = 0`, and `reports_absent` lists all 64 seats
(`['S1'..'S5','V01'..'V59']`). This is the pre-run state, contradicted by the
tree (§1). The skeleton correctly leaves `agent_id/outcome/dispatch_tool_call_id/
returned_summary` null for the L1.

**(b) `candidate_revision_pinned` is a mid-flight snapshot, and 6 of its 16
entries have drifted.** V36's snapshot was taken at 20:29:02, but S1/S2/S4/S5
made their final writes at 20:30–20:34 (mtimes: tools `20:31:49`/`20:33:36`/
`20:34:06`; r98 README/map `20:30`; r95/r96 notes `20:29`). The receipt pinned
the **r97 baseline** bytes for the tool/note paths (V58's own earlier
`V58-scratch/baseline-hashes.txt` lists the identical values as r97-baseline).
Drift table (receipt value → live value):

| Path | receipt (20:29) | live (final) |
|------|-----------------|--------------|
| `corpus/tools/dependency_freeze.py` | `b06275f3…` | `03d04365…` |
| `corpus/tools/dependency-freeze-contract.json` | `27273be2…` | `153ebc5b…` |
| `corpus/tools/README.md` | `8678abc1…` | `1d299c16…` |
| `corpus/knowledge/r95-aftermath-scope-note.md` | `f87ed42a…` | `8e9e1774…` |
| `corpus/knowledge/r96-response-scope-note.md` | `6db32ca2…` | `a9b51f8c…` |
| `corpus/fixtures/r98-clerk-filing/README.md` | `d9387b7d…` | `32efc78f…` |
| `corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md` | `49d4834e…` | `c1099d0e…` |

The other 9 pinned entries match live (r95 map `80440d61…`, r98
contradictions/entities/fictional-excerpts/inspiration-note/relations/
source-excerpt/sources/timeline). This is **not** a producer failure — it is a
snapshot-vs-finalization gap: V36 was aborted before re-pinning. Its stall poll
(`V36-scratch/V36-poll.log`) confirms the tree was frozen at `reports=58
producers=5 r98fix=10 know=1` from try 22 through try 108, ending
`21:04:43 STALL READY held, reports=58 unchanged for 60 tries; exiting` —
i.e. no writer moved after the snapshot except the producers' final writes.

**Consequence for the L1/V36 finalize step:** to finalize, replace the
`candidate_revision_pinned` values with the §3/§4 live hashes, set
`reports_present = 58` (`reports_present_incl_self` = 58 as well, since V36's
own report is absent), and set `reports_absent = ["V20","V31","V36","V51",
"V57","V58"]`. The `r98-clerk-scope-note.md` entry must move out of
`missing_candidate_paths` (now present, hash `1162262c…`).

## 6. Verdict

| Check | Result |
|-------|--------|
| All roster reports present | **PARTIAL — 58/64**; 6 ABSENT (V20,V31,V36,V51,V57,V58) |
| Producer artifacts present with hashes | **PASS** (all present; live hashes recorded §3) |
| No duplicate seat prefixes | **PASS** (0 duplicates) |
| No header/filename mismatches | **PASS** (0 mismatches) |
| r98 fixture 10 files + map + README | **PASS** (all 10 present) |
| Three knowledge notes present | **PASS** (r95, r96, r98) |
| receipt.json finalized | **FAIL — skeleton** (counts 0; 6/16 pins drifted) |

Per-axis, no scalars; I judge no claim (C1/C2/C3). The 6 missing seats are the
known host-aborted endgame seats; V36's receipt is a skeleton that the L1 must
finalize against the live hashes above.

**Bottom line: INCONCLUSIVE — presence is 58/64 with the 6 known aborted
endgame seats (V20, V31, V36, V51, V57, V58) honestly ABSENT; all producer
artifacts, the r98 fixture's 10 files, and the three knowledge notes are
present and hash-recorded, with no duplicate prefixes or header mismatches, but
`receipt.json` remains an un-finalized V36 skeleton whose pinned hashes are a
pre-finalization snapshot (6/16 drifted) and whose collection counts are still
zero.**
