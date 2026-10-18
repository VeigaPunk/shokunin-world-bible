# V16 — operability

Round 101, lore-shokunin. Seat: leaf verifier, operability axis. Baseline: r101 declaration HEAD `ebec6bb` ("lore r101: declare GLM 28-seat round before dispatch"); r100 closure `6f86bf2`. Verified 2026-10-18 00:02–00:35 -03:00, all commands run from the lane root with python3 as documented.

**Claim under test (round C-brief, operability):** after producers, every documented command in U2's entry (`corpus/knowledge/r101-r10-register-first-entry.md`) plus the tools README addendum (`corpus/tools/README.md`, "Round-101 addendum", landed 00:20) runs as written.

## Axes

- A1 artifacts exist — PASS
- A2 U2-entry commands run as written — PASS
- A3 README-addendum commands run as written — PASS
- A4 non-interference (my bytes only) — PASS
- A5 evidence quality — every claim below quotes the actual command and observed output

## A1 — artifacts exist

- `corpus/knowledge/r101-r10-register-first-entry.md` present (122 lines; `verified-at: 2026-10-18T00:18-03:00`). Revised once at 00:31 after first delivery (00:20:42): one citation corrected — `corpus/fixtures/r96-crossing-response/README.md:11` → `:9` with the quoting phrase adjusted to "the tick-12 event …" — the Receipts command block unchanged. All A2 checks below were (re)run against the 00:31 bytes.
- `corpus/tools/README.md` Round-101 addendum present (file mtime 2026-10-18 00:20); `SKILL.md` freeze row updated to "19 cases … r101 added `repointed_edge`" and "exactly the eight chain fixtures, verifying 8/8 clean" with a dated supersession paragraph (file mtime 00:20).
- Delivery timeline witnessed: contract `dependency-freeze-contract.json` 00:08:32, `dependency_freeze.py` 00:07:59, README/SKILL 00:20, U1 report `U1-chain-eight.md` in seats/ by 00:23, U2 report `U2-r10-register.md` by 00:33 (bottom line: PASS). Both producer reports present at close; no verification was performed against a plan: every command below ran against delivered bytes.

## A2 — U2 entry's documented command (Receipts, lines 96–104), verbatim

Command (exactly as printed in the entry):

```sh
python3 - <<'PY'
import hashlib, json
from pathlib import Path
for fx in ["r94-paired-crossing","r95-crossing-aftermath","r96-crossing-response","r97-crossing-acknowledgment","r98-clerk-filing","r99-window-lapse","r100-docket-review"]:
    b = Path(f"corpus/fixtures/{fx}/relations.json").read_bytes()
    print(fx, hashlib.sha256(b).hexdigest()[:16], len(b))
PY
```

Observed output, exit=0 — exactly the seven lines the entry documents (r94 through r100, all `c279254bc7de0636 139`), byte-identical to the entry's expected block, and nothing else. Run twice: once against the 00:20:42 delivery and again at 00:33 against the 00:31 revision — identical output both times.

The revision's new citation was checked against the delivered file: `corpus/fixtures/r96-crossing-response/README.md:9` contains "…it records only Evin's second account of the same occasion: that he was at Salt Court through the same agreed bell." — the quoted phrase is byte-exact within line 9 (line 11, the superseded target, is different text; the correction is right).

Supporting prose claims of the entry's Receipts section, re-measured this pass (all byte-exact):

- `r95 timeline.json#/3` = `aftermath-missing-evin` (tick 11, aru, chalk-stair, `["paired-crossing-decision"]`, `aru-aftermath-note`) — parsed, exact.
- `r96 timeline.json#/4` = `response-evin-salt-court` (tick 12, evin, salt-court, `["aftermath-missing-evin"]`, `evin-response-note`) — parsed, exact.
- Source ids at cited lines: `r95 sources.json` line 21 `"id": "aru-aftermath-note"`; `r96 sources.json` line 27 `"id": "evin-response-note"`; `r94 sources.json` line 15 `"id": "crossing-minute"` — exact.
- `contradictions.json` parses to `[]` in both r95 and r96 — exact.
- Prefix chain: `r95 fictional-excerpts.md`.startswith(r94 full text) = True; `r96` startswith r95 = True.
- Quoted lines byte-exact: `r94:19` "> There, they agreed, for this crossing only, to share stewardship of the Chalk Stair."; `r95:26-28` (Tick 11 / "Evin did not come." / "The agreement we chalked…"); `r96:37` "> Tick 12: I was at Salt Court through the same agreed bell."; both notes present in `r100 fictional-excerpts.md` at lines 26 and 37.
- `corpus/knowledge/cross-cluster-contradictions.md` absent (`ls` → "No such file or directory"; `Path.exists()` False).

## A3 — tools README addendum commands

1. Self-test — command as written: `python3 corpus/tools/dependency_freeze.py --self-test`.
   Observed: 19 `CASE … ok` lines; final lines `CASE repointed_edge: exit=1 expected=1 findings=['ADDITION-DETECTED', 'REDUCTION-DETECTED'] ok`, `SELF-TEST 19/19`, `RESULT PASS`; exit 0. Matches the addendum's documented output, including the quoted `repointed_edge` CASE line, byte-for-byte.

2. Eight-fixture verification — the eight documented commands run one at a time from the repository root.
   Observed: all eight print `FREEZE … / DIGEST … / RESULT PASS`, exit 0 (8/8 clean). Every documented digest matches exactly: r88 `acf677a7085be3f6…96aae`, r94 `048b8ff39e4a5232…53ef`, r95 `97cffd7bfe6e0c92…c710`, r96 `43911900923c110b…7a7c`, r97 `a28b9ea0d65ec355…1d54`, r98 `5ecf84e19121ea12…f0` (full values observed), r99 `7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e`, r100 `77debadf5c0f6e2c27f18902f0710278eb4305c633ff73158df7082936325c19`. Counts observed per fixture: 2/3/4/5/6/7/8/9 events, 0/2/3/4/5/6/7/8 dependency-edges, relations 1 for the seven arc fixtures (r88 has 0) — all `x/x` clean.

3. Contract-delta claim — `git diff 6f86bf2 -- corpus/tools/dependency-freeze-contract.json` shows exactly 3 hunks (observed `grep -c '^@@'` → `3`; stat: 142 insertions, 1 deletion): the r100 pin addition, the `repointed_edge` expectation, and the guarded writer's `revision` refresh (`b5fe472…` → `ebec6bbdeb1d919c9eb19e7fdd5b9c6dd14db026`, read from the delivered contract). Matches the addendum.

4. The documented `--freeze` command (`python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/r100-docket-review`) was **not rerun**: the addendum marks it integration-time-only, "not a verification command and must not be rerun to check a delivery". Its recorded effects were verified against the delivered tree instead: new pin `r100-docket-review` with `fixture` `corpus/fixtures/r100-docket-review`, `payload_schema_version` 2, `revision` `ebec6bb…` (the r101 declaration commit, as documented), `content_sha256` `77debadf…25c19` (equals the observed verify digest), `counts` `{events 9, dependency_edges 8, relations 1, entities 6, sources 9}` (as documented), all ten declared per-file SHA-256 values recomputed against the live fixture — 10/10 `ok`; pins grew 7 → 8 with the only addition `r100-docket-review`; comparing every inherited pin field-by-field against `git show 6f86bf2:…` — NONE changed. The documented tick-16 edge present: `clerk-review-first-passage` tick 16 `depends_on ['clerk-lapse-recorded']`.

5. Independent `repointed_edge` reproduction outside the harness (my declared scratch `.ufo/waves/round-101/seats/.v16-scratch/repoint-mirror/`, laid out as a repo mirror with the delivered tool + contract copy + `r95-crossing-aftermath` copy; the swap `aftermath-missing-evin.depends_on = ['aru-ninth-bell']` applied by hand). Observed, exit 1:

```text
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
FINDING ADDITION-DETECTED: event aftermath-missing-evin gained depends_on ['aru-ninth-bell']
FINDING REDUCTION-DETECTED: event aftermath-missing-evin lost depends_on ['paired-crossing-decision']
RESULT FAIL
```

Byte-matches the addendum's recorded mirror output line-for-line (both findings on one event in one run; old edge REDUCTION, new-but-earlier edge ADDITION).

## A4 — non-interference

My writes: `seats/.v16-scratch/{poll.sh,repoint-mirror/}` and this report only. `git status --short` on the delivered tree shows exactly: `M SKILL.md`, `M corpus/tools/README.md`, `M corpus/tools/dependency-freeze-contract.json`, `M corpus/tools/dependency_freeze.py` (U1's four owned files) and untracked `corpus/knowledge/r101-r10-register-first-entry.md` (U2's owned file), plus pre-existing seat scratch (`seats/*-scratch`, lane-root `.scratch/` holding other seats' dirs — not mine). No self-test scratch residue at the repository root after my runs (self-test dirs are gitignored per `.gitignore` `*-self-test-*/`; none remained at check time).

## Bounds and recorded observations

- Operability only: I judge that documented commands run as written; depth/freshness/adjacency of the claims themselves are other seats' axes (my pointer/quote spot-checks are corroborating, not adjudicating).
- `--freeze` effect-verification assumes the delivered contract's pin faithfully records the single documented run; the run itself was not witnessed by this seat (pre-00:02).
- Producer-report latency recorded, not fatal: U2's report landed only after both 40-try/20s poll windows had expired (artifact present from 00:20:42, U1 report 00:23, U2 report by 00:33; poll try 40 at 00:31:23 still absent). One bounded stall-escape (relaunch of the expired first window). All artifact-side verification ran against delivered bytes throughout.
- Wave tree remains uncommitted; digests/pin values above are measurements of the working tree at HEAD `ebec6bb`.

**Bottom line: PASS — every documented command in U2's r101 entry and the tools README Round-101 addendum runs as written from the lane root (self-test 19/19, chain 8/8 clean with all nine documented digests, contract delta exactly 3 hunks, U2 receipts byte-exact); the integration-time `--freeze` was not rerun per its own prohibition and its recorded effects verify against the delivered tree.**
