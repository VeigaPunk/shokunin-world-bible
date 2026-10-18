# Seat U2 — r10-register (producer, C2 depth)

Round 101, lore-shokunin lane. Seat model: `zai-coding-plan/glm-5.3-flash-low`. Baseline: r100 closure `6f86bf2` (wave tree uncommitted during the round). Date of record: 2026-10-18T00:18-03:00 (all receipts measured this pass from the lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`).

## Deliverable

Authored `corpus/knowledge/r101-r10-register-first-entry.md` (20,823 bytes, 122 lines) — the R10 register's first worked entry, a demonstrated NON-conflict, per the round declaration's C2 (`LOG.md:3477-3486`). Structure: source/verified-at/recheck/citation-convention metadata header; scope and limits; the procedure applied (r88 table R10 row `:26`, register gate `:93-94`, r90 appendix owner clause `:97`, r91 namespace scoping `:99-100`, integration boundary `:110`, r89-closure integration notes, r89 format demo, r93 worked-example record-and-replay conventions and the r93 R10 negative case at `LOG.md:2656-2658`); the record `r101-crossing-agreed-bell-nonconflict-01` in the register-entry field shape with the conflict-presupposing fields replaced by the compatibility finding; both accounts quoted exactly; referent/field/occasion demonstrations; the COMPATIBLE outcome; the verdict; non-establishment bounds; cross-references to the r100 six-beat dossier and the r35 two-sided-preservation precedent; receipts; limits.

Key recorded findings, each verified against the delivered tree:

- **Shared referent demonstrated:** `relations.json#/0` (`agreed_co_stewardship_for_this_crossing`, source `crossing-minute`) is byte-identical across all seven arc snapshots r94–r100.
- **Shared field identified:** performance status of the crossing-scoped agreement at the agreed bell — a semantic field of the two accounts, explicitly contrasted with r35's literal `place_id` ledger field; no ledger pair created.
- **Shared occasion identified:** the agreed bell, carried by the two notes' common reference ("the agreed bell" r95 `:26` / "the same agreed bell" r96 `:37`), anchored to the r94 minute's "for this crossing only" (`r94 fictional-excerpts.md:19`); explicitly not tick-equality-based (ticks are editorial encodings, `r94 README.md:13`).
- **Outcome:** the assertions are COMPATIBLE (Aru: "Evin did not come."; Evin: "I was at Salt Court through the same agreed bell.") — no incompatible assertions, so the register gate (`r88 table:93-94`) is not met: no entry in `cross-cluster-contradictions.md` (file verified absent), no ledger pair, both clusters' `contradictions.json` stay `[]`, no register `unresolved` status used, no winner, no world-truth assertion. Testimony-level non-adjudication preserved separately.
- One variance recorded, not normalized: the arc READMEs carry comparison records under `## Namespace and occasion comparison` (`:5` in r94/r95/r96 READMEs), not the r90 appendix's `## R10 comparison outcomes` heading (`r88 table:90-92`); this entry is filed as the durable examination record instead, no README edited.

## Receipts — commands and observed outputs

Relation byte-identity (abbreviated output as embedded in the entry's Receipts section):

```sh
python3 - <<'PY'
import hashlib
from pathlib import Path
for fx in ["r94-paired-crossing","r95-crossing-aftermath","r96-crossing-response","r97-crossing-acknowledgment","r98-clerk-filing","r99-window-lapse","r100-docket-review"]:
    b = Path(f"corpus/fixtures/{fx}/relations.json").read_bytes()
    print(fx, hashlib.sha256(b).hexdigest()[:16], len(b))
PY
```

Observed: all seven lines `c279254bc7de0636 139` — byte-identical. `relations.json#/0` parsed value equals `{"from": "aru", "to": "evin", "type": "agreed_co_stewardship_for_this_crossing", "source_id": "crossing-minute"}`.

Claim pointers, parsed: r95 `timeline.json#/3` = `aftermath-missing-evin` (tick 11, aru, chalk-stair, `["paired-crossing-decision"]`, `aru-aftermath-note`); r96 `timeline.json#/4` = `response-evin-salt-court` (tick 12, evin, salt-court, `["aftermath-missing-evin"]`, `evin-response-note`). Sources: r95 `sources.json#/3` id `aru-aftermath-note`; r96 `sources.json#/4` id `evin-response-note`; r94 `sources.json#/2` id `crossing-minute`.

Excerpt prefix chain (`python3`, `bytes.startswith`): r94 file is a byte prefix of r95 (`True`), r95 of r96 (`True`); both quoted note sections present in `corpus/fixtures/r100-docket-review/fictional-excerpts.md` at lines 26 and 37 (`grep -n` confirmed). `contradictions.json` = `[]` in both compared clusters (parsed). `ls corpus/knowledge/cross-cluster-contradictions.md` → "No such file or directory".

Citation self-check (scratch harness `.ufo/waves/round-101/seats/U2-scratch/citation-check.py`, run from the lane root):

```sh
python3 .ufo/waves/round-101/seats/U2-scratch/citation-check.py
```

Final observed output, exit 0:

```text
line-quote checks: 34, substring checks: 10, pointer/derived checks: 15
CITATION-CHECK PASS: every cited line quote, path, JSON pointer, byte-identity, prefix-chain, and absence claim in the entry verified against the delivered tree.
```

Coverage: every line-numbered quote in the entry re-matched against the delivered file at the cited line; every JSON pointer re-parsed; the sha-prefix, prefix-chain, empty-ledger, and register-absence claims re-derived; the r35 ledger checked by parse (`#/0` id `bell7-location-reports`, both fields `place_id`; `timeline.json#/2-3` ids `tarin-envelope-observation` / `sella-bell7-presence`).

## Corrections found and fixed during self-check (recorded, not hidden)

1. r96 README quote for "records only Evin's second account of the same occasion" was first cited `:11`, then `:13`, before `grep -n` pinned it at `:9` — the delivered entry cites `:9`, verified. The intermediate numbers were never delivered.
2. The "Checker limits" bound originally attributed "a per-cluster CLEAN is not cross-cluster evidence" to r88 table `:110`; that clause lives in the R10 row at `:26`. Fixed; `:110`'s actual clause ("R10's proposed corpus-level register is a manual procedure until a corpus-wide validator exists. Do not mark any of those surfaces mechanically verified solely from a clean fixture replay.") is now quoted instead.
3. Two scratch-check misses were checker-side, not entry-side: an over-broad LOG.md substring expectation and a line-number probe of the r35 ledger where the entry correctly cites the JSON pointer; both checker expectations corrected.

No entry correction remains open; the delivered entry passed the full check set.

## Write discipline

`git status --porcelain` this pass shows, beyond the pre-existing r98 scratch and this round's seat tree: modified `SKILL.md`, `corpus/tools/README.md`, `corpus/tools/dependency-freeze-contract.json`, `corpus/tools/dependency_freeze.py` (producer U1's owned bytes — not touched by this seat), and untracked `corpus/knowledge/r101-r10-register-first-entry.md` (this seat's owned byte). This seat wrote only: the owned entry, this report, and `U2-scratch/citation-check.py`. No commits, no pushes, no network, no nested agents, no other file touched.

## Limits

Author-seat record: not independent verification, not admission, not a canon or rights finding. The entry's compatibility finding is a claim about the two authored records as stated, not about the fictional world; the entry states this in its own bounds. No poll was required for this seat (producer seat; no upstream artifact dependency). Other seats' reports observed present under `.ufo/waves/round-101/seats/` at filing time but were not read and are not relied on.

**Bottom line:** PASS — C2 delivered as declared: the R10 procedure's first real exercise on a demonstrated shared referent, field, and occasion, examined COMPATIBLE (non-conflict), both claims preserved byte-exact, no register entry, no winner, no world truth; every citation in the delivered entry machine-verified against the delivered tree (59/59, exit 0).
