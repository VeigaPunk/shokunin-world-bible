# K2 — Rejected-fit summary table (round-87, world-bible lane)

Seat: K2 (Connector follow-up). Measured tree: `lore-shokunin` HEAD `2b48ca72033dfd1060b6f81c4cf27ad83deae57f` (clean at start; the only tracked change this seat makes is the authorized one-line append to `l0-questions.md`).

Purpose: consolidate the sibling-fit rulings from `K1.md` (Connector scope adjudication) and `S3.md` (sibling-overlap scout) into one table, **re-verify the fleet-root scan against the delivered tree**, and record the boundary rulings the integrator must confirm. K1 and S3 are treated as prior work, not re-derived; every row below carries the command that produced the current evidence.

## Scan receipt

Command:

```sh
cd /home/vgpnk/Projects/shokunin && for f in */PROVINCE.md; do [ -f "$f" ] && printf '%s\n' "$f"; done | sort
```

Observed (20 paths, including lore's own):

```
audio-shokunin/PROVINCE.md
chousa-shokunin/PROVINCE.md
game-dev-2d-shokunin/PROVINCE.md
game-dev-3d-shokunin/PROVINCE.md
kagi-shokunin/PROVINCE.md
kaidoku-shokunin/PROVINCE.md
kake-shokunin/PROVINCE.md
kama-shokunin/PROVINCE.md
kasegi-shokunin/PROVINCE.md
kengaku-shokunin/PROVINCE.md
kotoba-shokunin/PROVINCE.md
kotodama-shokunin/PROVINCE.md
kumitate-shokunin/PROVINCE.md
lore-shokunin/PROVINCE.md
mado-shokunin/PROVINCE.md
mori-shokunin/PROVINCE.md
revenger-shokunin/PROVINCE.md
tabi-shokunin/PROVINCE.md
tameshi-shokunin/PROVINCE.md
tsukuroi-shokunin/PROVINCE.md
```

Directories without a `PROVINCE.md` (`research/`, `scripts/`, `templates/`) are not lanes and were excluded.

**K1's scan was incomplete against this tree.** K1 recorded 19 paths (its `K1.md:36`), i.e. the same list minus `kotodama-shokunin`. `kotodama-shokunin` was minted during round-87, after K1's scan and before the wave evidence commit:

```sh
stat -c '%y %n' kotodama-shokunin/PROVINCE.md
# 2026-10-17 01:27:33.732858290 -0300 kotodama-shokunin/PROVINCE.md
git -C kotodama-shokunin log --oneline -5
# a527120 mint: kotodama-shokunin seed kit (operator directive 2026-10-17)
```

S3 (scanned 5 named siblings only) also missed it. So **both prior scouts predate the lane that is closest to C3**, and this table adds it.

## Rejected-fit table

Ruling vocabulary: **rejected** = the lane's declaration excludes this work outright; **rejected (method adjacency)** = the deliverable stays in lore but a reusable *method* sits in the other lane; **hands-off contract** = the lane declares the domain and explicitly hands the world-bible record back to lore (not a rejection).

| # | Lane | Declared domain (evidence) | Ruling | Basis |
|---|---|---|---|---|
| 1 | audio-shokunin | game audio production; `Refuses: … narrative canon (lore)` (`PROVINCE.md:3,13-15`) | rejected | No audio asset or canon assignment requested; lore owns the record. |
| 2 | chousa-shokunin | deep-research method — source hierarchy, citation chaining and hop resolution, claim-vs-source verification (`PROVINCE.md:3-8`) | rejected (method adjacency, **contested**) | The deliverable is a lore world-bible record. The reusable method for choosing/verifying the real-world reference overlaps chousa; the split is not stated in either declaration. See §Contested boundary. |
| 3 | game-dev-2d-shokunin | 2D game production; `Refuses: … narrative canon (lore lane — contested scope is reported, not absorbed)` (`PROVINCE.md:3,10`) | rejected | Fictional-world data is not executable 2D production. |
| 4 | game-dev-3d-shokunin | 3D game production; `Refuses: … narrative canon (lore` (`PROVINCE.md:3,33-35`) | rejected | Same as #3. |
| 5 | kagi-shokunin | secrets & vault ops; `Refuses: anything outside this domain` (`PROVINCE.md:3-6`) | rejected | No credential/custody surface in a world bible. |
| 6 | kaidoku-shokunin | reverse engineering of shipped artifacts (`PROVINCE.md:3`) | rejected | C3 is authored data, not a shipped artifact under RE. |
| 7 | kake-shokunin | web properties & publishing (`PROVINCE.md:3-6`) | rejected | No deploy or publishing surface. |
| 8 | kama-shokunin | local model serving & endpoint health (`PROVINCE.md:3-6,40`) | rejected | No endpoint/model surface. |
| 9 | kasegi-shokunin | bounty & security research (`PROVINCE.md:3-4,24-25`) | rejected | Out of domain; no program scope. |
| 10 | kengaku-shokunin | LLM/model research & evaluation (`PROVINCE.md:3-6`) | rejected | No model-quality claim. |
| 11 | kotoba-shokunin | prompt & skill craft (`PROVINCE.md:3-6`) | rejected | A symbolism clause-map is fictional-world content, not a skill playbook. |
| 12 | **kotodama-shokunin** | linguistic-cultural worldbuilding — conlang, **mythic and symbolic systems**, era models, naming; `Refuses: claiming or recording canon — that is lore-shokunin (kotodama hands off systems; lore records and verifies them)`; `Adjacent contract (load-bearing): lore-shokunin owns the world bible and its consistency verification` (`PROVINCE.md:3-7,13-21`) | **hands-off contract — the closest fit, and NOT a rejection** | C3 is a mythology/symbolism cluster, which is kotodama's declared *generative* domain, while the record + consistency verification is lore's by explicit contract. Neither K1 nor S3 saw this lane. See §Kotodama boundary. |
| 13 | kumitate-shokunin | orchestration & tooling (`PROVINCE.md:3-6`) | rejected | No dispatch/runtime surface. |
| 14 | mado-shokunin | desktop & compositor craft (`PROVINCE.md:3-6,14`) | rejected | No display/compositor surface. |
| 15 | mori-shokunin | fleet & host observability, read-only probes (`PROVINCE.md:3-6,12`) | rejected | "Events" is wording-level only: mori's are host/kill/OOM events, not fictional timeline events (S3 `S3.md:12`). |
| 16 | revenger-shokunin | reverse engineering of shipped artifacts; `Refuses: … narrative canon (lore)` (`PROVINCE.md:3,19-23`) | rejected | Authored fiction is not an RE target. |
| 17 | tabi-shokunin | browser & web-interaction craft (`PROVINCE.md:3-6,15`) | rejected (route-later) | A static corpus note needs no live-site interaction; any later browser-evidence task routes to tabi. |
| 18 | tameshi-shokunin | verification-fixture craft; `Refuses: product domains — every lane's gate remains its own` (`PROVINCE.md:3-14`) | rejected (method adjacency) | tameshi owns *fixture method*; lore's checker and its fixtures stay lore's own gate. |
| 19 | tsukuroi-shokunin | host operability & system repair (`PROVINCE.md:3-6,16`) | rejected | No host-repair surface. |
| — | **lore-shokunin** (self) | fictional-world records — entities, relations, timeline events — with consistency verification and sourced inspiration; `Refuses: … real-world rights claims (art-east-asian-design)` (`PROVINCE.md:3,7,9`) | **owner** | C1/C2/C3 all land here. |

## Contested boundary — chousa (C3 source method)

- chousa owns `source hierarchy (primary / secondary / aggregator / unsourced); citation chaining and hop resolution; claim-vs-source verification` (`chousa-shokunin/PROVINCE.md:5-7`).
- lore owns `sourced inspiration` and `real-world reference works, cited with the art ledger's discipline: attribution, rights, and AI-training permission kept as distinct questions` (`lore-shokunin/PROVINCE.md:3,7`).
- The C3 fixture's `inspiration-note.md` cites a real-world parallel (ETCSL composition 1.4.1) and keeps **attribution / rights / AI-training permission** as three separate, unanswered questions; `sources.json` carries fixture-local `reliability_note` fields but no external source-hierarchy ranking.
- **Ruling:** the record stays in lore; the *reusable method* of finding/ranking/verifying external sources is chousa's. Neither declaration states this split, so it is genuinely contested and is what the `l0-questions.md` line asks the operator to confirm. This table does **not** assert chousa owns the fictional cluster.
- Rights must not become a determination: lore refuses real-world rights claims (`lore-shokunin/PROVINCE.md:9`), and the C3 note's rights/training questions are recorded as open, not answered.

## Kotodama boundary (new — the load-bearing one)

- kotodama declares `mythic and symbolic systems` as its own generative craft and states the handoff: `lore-shokunin owns the world bible and its consistency verification` (`kotodama-shokunin/PROVINCE.md:5-6,19-20`).
- C3 (`corpus/fixtures/r87-myth-cluster/`) is a Mother-Tide Gate / Moon-Basin Vow cluster with `symbolism-clause-map.md` and `lowwater-hymn-excerpt.md` — i.e. exactly the myth/symbolism material kotodama generates and lore records.
- **Ruling:** C3 as delivered is a world-bible record with consistency verification, so it stays in lore — this is the contract's own split, not a rejection of kotodama. But the boundary is now *live* for C3 in a way K1/S3 could not see, and it should be reflected in the integrator's boundary note.
- **Named gap:** kotodama names the handoff format as `corpus/knowledge/synthesis/worldbible-integration-contract.md`. That path is **empty** in the delivered tree:

```sh
ls -la kotodama-shokunin/corpus/knowledge/synthesis/
# total 0
# drwxr-xr-x 1 vgpnk vgpnk  0 Oct 17 01:26 .
# drwxr-xr-x 1 vgpnk vgpnk 94 Oct 17 01:26 ..
```

So the contract both lanes' declarations depend on is referenced but unwritten. C3 was authored without it, which is consistent with C3 predating the mint — but any future lore↔kotodama handoff has no written format yet.

## Named gaps for the integrator

1. `art-east-asian-design` — lore names it as the rights-claim recipient (`lore-shokunin/PROVINCE.md:9`) but it is not a fleet-root sibling:

```sh
ls -d *art* 2>/dev/null || echo "no fleet-root dir matching *art*"
# no fleet-root dir matching *art*
find . -maxdepth 2 -iname '*art-east*'
# (no output)
```

   Either the lane lives outside this fleet root or the reference is stale. Rights questions currently have no resolvable owner in-tree.
2. K1's rejected-fit list is one lane short (kotodama, §Scan receipt). Any downstream use of `K1.md`'s sibling rulings should carry this correction.
3. K1 recorded S3 absent after two checks (`K1.md:34-35`). That gap is **closed**: `S3.md` is present at `2b48ca7` and is read above; S3 covered 5 siblings, so it is not a substitute for the full scan.

## Method / provenance

- `K1.md` and `S3.md` were read in full at the delivered tree; their rulings are reused as prior work and re-attributed where re-verified.
- Rows 1–11 and 13–19 were re-derived from the current declarations by the scan command above (grep of `Domain`/`Owns`/`Refuses` lines); no row contradicts K1 or S3.
- Row 12 is new to this seat. No checker, fixture, knowledge-table, or sibling file was modified by K2.
