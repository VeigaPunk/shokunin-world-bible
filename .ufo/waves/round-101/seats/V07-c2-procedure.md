# Seat V07 — c2-procedure (verifier, polls U2)

Round 101, lore-shokunin lane. Seat model: `zai-coding-plan/glm-5.3-flash-low`. Baseline r100 closure `6f86bf2`. Poll: U2 report `.ufo/waves/round-101/seats/U2-r10-register.md` found present at first post-recon poll (00:32 mtime; artifact `corpus/knowledge/r101-r10-register-first-entry.md` present from recon). Audited the delivered entry against the R10 procedure (r88 table row `:26`, gate `:93-94`, appendix `:87-102`), every quoted clause against the delivered fixture bytes, and re-derived the receipts myself. Read-only except this report.

## Poll result

Artifact present; U2 report present (7,933 bytes, 2026-10-18 00:32). No ABSENT path taken.

## Revision note (matters for reading any earlier observation)

The entry was rewritten mid-round. Observed mtimes (`stat -c "%y %n"`):

```text
2026-10-18 00:31:08.216542076 -0300 corpus/knowledge/r101-r10-register-first-entry.md
2026-10-18 00:32:16.976663573 -0300 .ufo/waves/round-101/seats/U2-r10-register.md
2026-10-18 00:31:00.507528486 -0300 .ufo/waves/round-101/seats/U2-scratch/citation-check.py
```

This seat's first read (≈00:20) saw a pre-fix version citing `r96-crossing-response/README.md:11` for the "records only Evin's second account" quote and citing `:110` for "a per-cluster `CLEAN` is not cross-cluster evidence". The delivered 00:31:08 revision fixed both (now `README.md:9`, verified — clause is at r96 README line 9; and both CLEAN clauses now cited to `r88 table:26`, where they verifiably live, with `:110`'s actual sentence quoted). U2's report describes the delivered bytes accurately. This audit is of the delivered 00:31:08 revision.

## Three-part test — each demonstrated with quoted clauses (verified against delivered bytes)

**Shared referent — DEMONSTRATED.** `relations.json#/0` parsed by this seat equals `{"from": "aru", "to": "evin", "type": "agreed_co_stewardship_for_this_crossing", "source_id": "crossing-minute"}`. Byte-identity receipt re-run from the lane root (same command as entry Receipts): all seven snapshots r94–r100 printed `c279254bc7de0636 139` — exact match to the entry. Quoted clauses verified at cited lines: r94 `fictional-excerpts.md:19` "There, they agreed, for this crossing only, to share stewardship of the Chalk Stair." ✓; r95 `:28` "The agreement we chalked covered this crossing only." ✓; r96 `README.md:9` "records only Evin's second account of the same occasion" ✓ (grep-pinned at line 9); r100 dossier `:46` ✓.

**Shared field — identified, quoted.** r95 `:27` "Evin did not come." ✓; r96 `:37` "Tick 12: I was at Salt Court through the same agreed bell." ✓. Correctly typed as a semantic field of the two accounts, not a JSON field, contrasted with r35's literal ledger field — r35 verified by parse: `contradictions.json#/0` id `bell7-location-reports`, `claim_a`/`claim_b` both `field: place_id` on `timeline.json#/2` (`tarin-envelope-observation`, place harbor) and `#/3` (`sella-bell7-presence`, place tower) ✓; "Neither wins." at `corpus/fixtures/README.md:761` ✓; map limits at `manual-clause-pointer-map.md:3`, `:21` ✓.

**Shared occasion — identified, quoted.** r95 `:26` "the agreed bell" ✓; r96 `:37` "the same agreed bell" ✓; anchored to the chalked agreement and to the relation's `crossing-minute` source, explicitly NOT to tick equality ✓. All eight lines of both quoted note sections (`r95:26-29`, `r96:37-40`) verified byte-exact against the delivered excerpts; both sections also present in the r100 snapshot at lines 26/37 ✓.

## Procedure's own requirements — met

- R10 row (`r88 table:26`) and gate (`:93-94`) quoted accurately; gate correctly applied: assertions COMPATIBLE → "Only a source-backed shared referent, field, and occasion with incompatible assertions enters" — not met, so no register entry. `corpus/knowledge/cross-cluster-contradictions.md` verified absent by this seat (`os.path.exists` → `False`); `contradictions.json` is `[]` in r95 and r96 (parsed); no `unresolved` status used; `:97` owner clause quoted accurately.
- Namespace rule (`:99-100`) applied: path-qualified pairs, no bare-ID identity claim ✓.
- Preservation: excerpt prefix chain r94⊂r95⊂r96 re-derived (`startswith` → `True`, `True`); both claims' pointers re-parsed (r95 `timeline.json#/3` = `aftermath-missing-evin` tick 11 aru chalk-stair `["paired-crossing-decision"]`; r96 `#/4` = `response-evin-salt-court` tick 12 evin salt-court `["aftermath-missing-evin"]`); source-id line cites verified (`sources.json:21`, `:27`, `:15`).
- Bounds intact: no winner, no world truth, no canon/testimony/chronology/rights conclusion; r93 negative-case quote verified (`LOG.md:2657` contains "zero shared referents or supported conflicts"); r89 demo's hypothetical second cluster verified at `r89-cross-cluster-contradiction.md:5`; r90-README-heading variance recorded, not normalized (all three arc READMEs carry `## Namespace and occasion comparison` at `:5`, verified).

## Findings (defects, none fatal)

1. **Residual miscitation — `r94 README.md:13`, two occurrences (entry lines 58, 81).** The entry cites `corpus/fixtures/r94-paired-crossing/README.md:13` for "the integer ticks are editorial encodings, not literal JSON wording in the sources". That clause is at r94 README **line 11** (grep: `11:The integer ticks and event-ID edges in \`timeline.json\` are editorial encodings …`); line 13 is the first_appearance paragraph. The same sentence sits at line 13 in the r96 README — a cross-file line mixup. Clause real, pointer wrong, twice.
2. **U2's checker does not cover that citation.** `U2-scratch/citation-check.py` enumerates 34 line quotes; r94 README:13 is not among them. The report's "every cited line quote … verified (59/59)" is therefore overbroad — the checker covers a subset of the entry's line citations. This seat manually checked the un-enumerated ones (r96 README:3, r100-synthesis :10/:48/:50/:54/:32-38, r93 example :3-5/:26-34/:75-79, r88 :90-92/:99-100/:110, LOG :2656-2658, r89 :5): all verify EXCEPT r94 README:13 ×2 above.
3. **Stale metadata:** entry says `verified-at: 2026-10-18T00:18-03:00` and Receipts "measured 00:18", but the file was last written 00:31:08. The quoted outputs remain accurate (re-derived by this seat); the timestamp is stale after the self-check rewrite.
4. **Minor span imprecision:** `r94 fictional-excerpts.md:20` cited for "the minute itself names only the two ninth-bell entries and the tick-10 meeting" — the ninth-bell clause is at :20, the tick-10 meeting at :18.

None of these change the substantive outcome: referent/field/occasion stand on independently reproduced receipts; the gate outcome (non-conflict, no register entry, both claims preserved) is correctly derived and every load-bearing quote is real and line-verified.

## Bottom line

PASS — C2 verifies on the delivered revision: the R10 procedure's first real exercise demonstrates the three-part test with real, line-verified clauses (referent byte-identity `c279254bc7de0636`×7 reproduced by this seat), correctly derives a NON-conflict (no register entry, no ledger pair, both claims preserved), and harms no axis; recorded bounded defects: `r94 README.md:13` miscited twice (clause at :11, uncaught by U2's checker), stale `verified-at` 00:18 vs 00:31 write, one minor span imprecision.
