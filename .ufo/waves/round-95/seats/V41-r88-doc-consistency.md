# V41 — r88-doc-consistency seat report (round 95)

- Seat: V41 r88-doc-consistency. Scope: after all producers, confirm every knowledge/README record that describes r88 is still accurate now that `map_obligations` covers the r88 map dialect; list every stale wording with path:line (no edits — L1 updates at integration).
- Baseline: r94 closure `fb118c4`. All five producer reports present before verification (`P1-tool-code.md` seen 16:27:48; `P2-contract-docs.md` seen 16:29:48; P3/P4/P5 earlier).
- Verified revision pin: `corpus/tools/map_obligations.py` sha256 `d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108`, size 33320, mtime `2026-10-17 16:26:27.696443074 -0300` — identical to the hash P2 verified (§1 of its report).

## 1. Premise verified on the delivered revision (actual commands)

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r88-m3-maya-cluster
OBLIGATIONS raw=10 mapped=10
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12
RESULT PASS
exit=0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r87-myth-cluster
FINDING unsupported_map: pointer cells must contain one canonical inline-code pointer
RESULT ERROR
exit=2

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r89-inspiration-paraphrase
FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column
RESULT ERROR
exit=2

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r89-c1-invalid-tick
FINDING map_missing: expected exactly one conventional claim-to-excerpt map
RESULT ERROR
exit=2

$ python3 corpus/tools/map_obligations.py --self-test   # tail
SELF-TEST PASS frozen_expected_failure exit=1 findings=['missing_obligation']
SELF-TEST PASS frozen_verdict_mismatch exit=2 findings=['frozen_verdict_mismatch']
RESULT PASS
exit=0   (22 SELF-TEST PASS lines, 0 FAIL)
```

So the premise "map_obligations now covers the r88 dialect" is real and fail-closed elsewhere (r87 co-mapped, r89 no-map forms stay exit 2). One transient untracked scratch dir `map-obligations-self-test-841_wfrx/` was observed under the repo root during my runs and was absent at the final check — consistent with the still-open BR-05 (self-test scratch under repo root).

## 2. Audited records — the four named r88 targets

| Record | Pin (sha256 prefix) | Producer-untouched? | Verdict |
|---|---|---|---|
| `corpus/fixtures/README.md` r88 section (lines 1008-1010) and r94 section (1154-1169) | `01161b047f318c24` | yes (`git status --porcelain` empty) | **Accurate.** No map_obligations status claim in the r88 section; the r94 section's statement "`map_obligations` covers raw-JSON↔map completeness and source-ID agreement only" (line 1169) remains true. |
| `corpus/README.md` r88 bullet (line 19), r94 bullet (21), knowledge bullets (25-26) | `d27ed4981037904d` | yes | **Accurate** except the tools bullet at line 35 — stale (S-3 below). |
| `corpus/knowledge/r94-cross-myth-design-comparison.md` (r88 mentions lines 1, 12, 23, 25) | `e039c57764678be3` | yes | **Accurate.** All r88 references are content/design (Spence comparator, path-qualified namespaces); no map-tool status wording. |
| `corpus/fixtures/r88-m3-maya-cluster/README.md` (11 lines) | `55c9ba57ad7af5db` | yes | **Accurate.** No map-tool status claim. (`grep -rn "map_obligations\|unsupported_map" corpus/fixtures/r88-m3-maya-cluster/` → no hits.) |

Also swept for map-tool status wording in the other r88-describing knowledge records — `r88-sourced-inspiration-decision-table.md`, `reference-ledger.md`, `holder-assessment-boundary.md`, `r93-r8-worked-example.md`: no `map_obligations` / `unsupported_map` / dialect wording (grep hits: none). Nothing stale there.

## 3. Stale wording to be updated by L1 at integration (path:line, no edits made)

**Live records (should change):**

- **S-1 `SKILL.md:89`** — current: "…for the canonical map form used by the r93 and r94 clusters; legacy map forms exit 2 `unsupported_map` (fail-closed). … Bounded residuals BR-01…BR-04 and BR-16 of the round-94 debt ledger apply."
  Stale: the r88 `JSON fact and fields` legacy form now exits 0 `RESULT PASS` (command in §1), so "legacy map forms exit 2" is false as written; and BR-02 (schema drift) and BR-03 (self-test coverage) are closed by r95 C1. Suggest: name the r88 dialect as covered, keep r87/r89 co-mapped/no-map forms as fail-closed examples, drop BR-02/BR-03 from the residual list.
- **S-2 `SKILL.md:87`** — "20 cases with independently persisted expected exits and finding IDs…" → contract now persists 22 cases (delivered `--self-test` 22/22).
- **S-3 `corpus/README.md:35`** — "`tools/map_obligations.py` (round 94) — … for canonical one-obligation-per-row cluster maps; `--self-test` (20 persisted cases)…"
  Stale twice: 20 → 22 persisted cases; "canonical one-obligation-per-row" no longer describes full coverage (r88 field-path dialect added; point to `corpus/tools/README.md` Round-95 addendum, optionally "(round 94; r95 addendum)").

**r94 historical records (L1 judgment — may be intentionally preserved as history; superseded wording should at least be cross-referenced):**

- **S-4 `SCORECARD.md:374`** — "`--self-test` → 20/20 real-CLI cases, exit 0."
- **S-5 `SCORECARD.md:399`** — "legacy maps exit 2 `unsupported_map` (fail-closed, BR-14)."
- **S-6 `SCORECARD.md:400`** — "`--self-test` 20/20 … renamed-`claims`-key + removed row = silent PASS (BR-02)."
- **S-7 `SCORECARD.md:416`** — "self-test `--self-test` (20 persisted cases); pinned values".
- **S-8 `corpus/tools/README.md:95`** — "# 20/20 SELF-TEST PASS / RESULT PASS, exit 0" (r94 addendum example). This is the repo's deliberate dated-history pattern: the Round-95 addendum at `corpus/tools/README.md:101-119` explicitly supersedes it and states the 22-case contract and the r88 dialect. No edit strictly required; an inline cross-reference would remove any standalone misreading.

No other stale wording found: repo-wide grep for `unsupported|dialect` over top-level docs and `corpus/**/*.md` returned only the items above plus accurate historical usage.

## 4. Adjacent observations (not edits, for L1)

- **O-1 — round declaration precision.** LOG.md's C3 wording "12/12 PASS over the r88 map's obligations" should be worded at closure as `OBLIGATIONS raw=10 mapped=10` + `TOTAL-ROWS 12/12` (10 JSON obligations + 2 editorial rows), per P1 §6.1 and P2 §6.2 — the delivered tool cannot report `raw=12` without a `phantom_obligation` exit 1. My §1 run shows both numbers, correctly labeled.
- **O-2 — minor omission.** `corpus/README.md:36` lists tools/README as covering `support_check.py`, `discriminate_check.py` and the boundary-document checker; it omits `map_obligations.py` (pre-existing since r94, not r95-caused). L1 may fold this into the S-3 edit.

## 5. Verification method notes

- Poll-wait honored: producer artifacts were checked for existence and completeness (P1's report + stable tool mtime) before verification; the tool hash matches P2's independently recorded hash.
- All quoted commands were run from `/home/vgpnk/Projects/shokunin/lore-shokunin` on the delivered revision; outputs above are verbatim.
- `git status --porcelain` on the six audited documents is empty (producer-untouched); their pins are recorded in §2.
- No files were edited by this seat; only this report was written. No commits, no pushes, no network, no nested agents.

**Bottom line: PASS — r88-dialect premise verified on the delivered revision (r88 exit 0 PASS, r87/r89 fail-closed, self-test 22/22); the four named r88 records audited (three accurate, `corpus/README.md:35` stale) and every stale wording enumerated for L1 with path:line: SKILL.md:87, SKILL.md:89, corpus/README.md:35 (live) plus SCORECARD.md:374/399/400/416 and corpus/tools/README.md:95 (r94 history).**
