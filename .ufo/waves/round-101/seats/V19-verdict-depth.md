# V19 — verdict-depth (round 101)

Seat: V19, leaf verifier, C2 depth verdict. Baseline r100 closure `6f86bf2` (wave tree uncommitted). All commands run from the lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Object: `corpus/knowledge/r101-r10-register-first-entry.md` (U2, C2) — the R10 register's first worked entry, a demonstrated NON-conflict. My deliverable is one DEPTH verdict with bounds, on my own re-derivation of the compatibility check.

## Poll record (protocol + recorded stall-escape)

- Protocol window: 44 tries × 20 s (~14.7 min, from ~00:02): artifact and U2 report ABSENT throughout (`POLL LOOP DONE`, no ARTIFACT/U2-REPORT lines). The wave was demonstrably mid-flight (U1's `dependency_freeze.py` mtime 00:07:59, contract 00:08; U1 report 00:21).
- Recorded stall-escape (ENDGAME CONVENTION): +25 tries × 20 s → **C2 artifact appeared at try 9, 00:20:35**. U2 producer report (`U2-*.md`) **ABSENT at finalization (00:29:50)** — bounded, not fatal: the verified object is the delivered artifact on its own bytes; U2's report claims are not verified from this seat.
- C2 seats read: V08-c2-compatibility.md (in full — its independent reconstruction and four failed contradiction derivations match mine); V26-cross-seat-audit.md and V28-late-bookkeeper.md recorded C2 ABSENT at their earlier cutoffs (~00:17–00:19), superseded by the 00:20:35 landing. No U2 report existed to read.

## Own re-derivation of the compatibility check (seat-owned, before weighting the artifact)

Commands (all from lane root) and observed outputs:

```
python3 - <<'EOF'  # sha256 loop over seven arc fixtures
r94-paired-crossing c279254bc7de0636 139
r95-crossing-aftermath c279254bc7de0636 139
r96-crossing-response c279254bc7de0636 139
r97-crossing-acknowledgment c279254bc7de0636 139
r98-clerk-filing c279254bc7de0636 139
r99-window-lapse c279254bc7de0636 139
r100-docket-review c279254bc7de0636 139
```
→ the shared referent `relations.json#/0` is byte-identical (`{"from":"aru","to":"evin","type":"agreed_co_stewardship_for_this_crossing","source_id":"crossing-minute"}`) across all seven snapshots, exactly as the artifact's receipt records. Full hash head matches the r100-closure pin `c279254bc7de0636d918…` in LOG.md.

Pointer parse: `r95 timeline.json#/3` = `aftermath-missing-evin` (tick 11, aru, chalk-stair, deps `["paired-crossing-decision"]`, src `aru-aftermath-note`); `r96 timeline.json#/4` = `response-evin-salt-court` (tick 12, evin, salt-court, deps `["aftermath-missing-evin"]`, src `evin-response-note`) — both exactly as the artifact's record table asserts. Source IDs at `r95 sources.json#/3`, `r96 #/4`, `r94 #/2`, id lines 21/27/15 as cited.

Prefix chain: `r95 startswith r94: True`, `r96 startswith r95: True`; both quoted notes present in the r100 snapshot at lines 26 and 37. Ledgers: `contradictions.json` = `[]` in r95 and r96; `cross-cluster-contradictions.md` absent.

Compatibility derivation (mine):

- Claim A asserts: Aru waited at the Chalk Stair through the agreed bell; **Evin did not come** [to the Chalk Stair]; the agreement covered this crossing only; no other duty/breach asserted (`r95 fictional-excerpts.md:26-29`, read whole).
- Claim B asserts: **Evin was at Salt Court** through the same agreed bell; no accusation; no winner; both accounts unresolved (`r96 fictional-excerpts.md:37-40`, read whole).
- Joint model: Evin at Salt Court during the bell ⇒ did not come to the Chalk Stair. A ∧ B satisfiable. B asserts no arrival anywhere; A asserts no location for Evin. No field on which the two assertions take incompatible values. Nothing in either note claims performance of the agreement. → **COMPATIBLE; no conflict constructible.** This matches the artifact's outcome.
- World-truth discipline: compatibility is a relation between accounts, not corroboration. The artifact's verdict paragraph and non-establishment bounds explicitly disclaim testimony truth, chronology authentication, duty expansion, canon, rights — consistent with the arc invariant (`r100-crossing-arc-synthesis.md:10`, `:50`, `:54`, verified verbatim this pass).

## Citation and preservation audit (spot-checks that landed)

Verified verbatim at the cited lines: `r88:26` (R10 row), `:93` (register gate), `:97` ("the register's first real entry awaits a genuine conflict"), `:100` (path-qualified comparison keys); `LOG.md:2657` (r93 R10 negative case, "zero shared referents or supported conflicts" — inside the cited 2656-2658 range); `r96-crossing-response/README.md:3` (declared continuation) and `:9`-area phrase "records only Evin's second account of the same occasion"; `r94 fictional-excerpts.md:19` (crossing-only agreement wording); `r100 synthesis :46` (byte-identity claim) and `:50` (occupancy observation); `r96-response-scope-note.md:13`, `:31`, `:40`; r35 precedent (`contradictions.json#/0` `bell7-location-reports`, field `place_id` on `timeline.json#/2-3`; `fixtures/README.md:761` "Neither wins."; map `:3`, `:21`; the `why` is indeed conditional on identity/place/occasion assumptions); `r93-r8-worked-example.md:3-5/:26-34/:75-79` (scope-first, crosswalk, dated-corrections conventions). README variance honestly disclosed: all three arc READMEs carry `## Namespace and occasion comparison` at `:5`, not r90's `## R10 comparison outcomes`.

Preservation: `git status --porcelain` → tracked modifications are exactly `SKILL.md`, `corpus/tools/README.md`, `corpus/tools/dependency-freeze-contract.json`, `corpus/tools/dependency_freeze.py` (all U1-owned) plus untracked round-scratch/wave dirs and the single new corpus file `corpus/knowledge/r101-r10-register-first-entry.md` (U2-owned). No fixture and no pre-existing knowledge file touched from the producer seats.

## Evidence noted (not depth-fatal)

1. **Four citation line-pointer slips in the artifact** — substance verified verbatim nearby; none touches the compatibility derivation: `r96 README:11` cited, phrase at `:9`; `r94 README:13` cited, ticks sentence at `:11`; `r88:110` cited for "a per-cluster CLEAN is not cross-cluster evidence", exact phrase at `:26` (`:110` carries the same manual-gate discipline in different words); the `:93-94` gate quote's tail "(status `unresolved`)" falls on `:95`. (Slips 1–2 corroborate V08's independent findings; I re-verified both myself.)
2. **Register/entry naming tension resolved correctly**: the title says "first worked entry" while the body states "The register gains its first real exercise without gaining a first entry" and `cross-cluster-contradictions.md` stays uncreated — consistent with `r88:97`. No governance contradiction.
3. The "both accounts depict the agreed stewardship as not performed" phrasing is an account-level semantic reading slightly stronger than B's literal text; it is quarantined by the "as accounts" qualifier and the compatibility finding does not depend on it.

## DEPTH verdict

**DEPTH IMPROVED (bounded).** The entry is a genuine depth increment over r100's dossier: the R10 gate (shared referent → field → occasion → incompatibility) is re-derived and discharged stepwise on a *demonstrated* referent (byte-identity receipt across seven snapshots) rather than asserted from the different-actors/different-places observation (`synthesis:50`); the register-gate inversion (compatible ⇒ no entry, no ledger row, `unresolved` unused) is correct against `r88:26/:93-94/:97`; non-establishment bounds are explicit; the README-heading variance is disclosed, not normalized; the new-byte delta (referent receipt + explicit gate finding) is real and reproducible.

Bounds: (a) intra-lineage exercise — both claims are continuations of one declared lineage, so the R10 row's cross-cluster trigger and the register-append branch remain unexercised (correctly: no genuine conflict exists); (b) the shared field is semantic (performance status), not a JSON field — manual gate only, no mechanical check; (c) one pair examined, no corpus sweep claimed; (d) four line-pointer citation slips recorded; (e) author-seat record — U2's producer report ABSENT at finalization, so the artifact's self-reported process claims rest on my re-derivation, which passed.

**Bottom line: PASS — C2 depth IMPROVED (bounded): a correctly-derived, byte-receipted, preservation-clean R10 NON-conflict exercise; four citation line-slips noted; U2 report absent (recorded stall-escape).**
