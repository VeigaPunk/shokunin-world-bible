# V43 c1-negative-2 — round 99

- Seat: V43 c1-negative-2 (verifier, read-only on lane bytes; leaf). Lane repo `/home/vgpnk/Projects/shokunin/lore-shokunin`. Commands from the lane root with `python3`. Baseline r98 closure `4265df5` (tool `03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b`, contract `153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947`). No commits, no pushes, no network, no nested agents.
- Revision verified, equal to S1's report and to V08's POLL_HIT: `corpus/tools/dependency_freeze.py` `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c`; `corpus/tools/dependency-freeze-contract.json` `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628`. Live pair unchanged before the official matrix, after it, and at this report.
- Writes: this report and `.ufo/waves/round-99/seats/V43-scratch/` only. Harness `V43-scratch/matrix.py` sha256 `b1362837c6bcd6c6e3c01d02c1d43bba910e8f5f3db2068b9d478ac2dbaa9965`. Official log `V43-scratch/matrix-final.log` sha256 `284299c25cf283327c5d4869f058110421ab2f5bf8e5d0e6b8657ce7293db196`.

## 0. Poll-wait (20 s, 40 tries, then a recorded stall-escape)

Poller `V43-scratch/poll.sh` then `poll-cont.sh`. Hit required an `S1-*.md` report and tool+contract shas off the r98 baseline, stable for three checks. No matrix was scored before that.

```
try=1  t=22:02:48 report=none tool=same    contract=same    toolsha=03d04365… ctsha=153ebc5b…
try=6  t=22:04:28 report=none tool=changed contract=changed toolsha=1728ed89… ctsha=8f9c1f53…
try=16 t=22:24:53 report=none tool=changed contract=changed toolsha=6f81f8be… ctsha=8c2561b0…
try=40 t=22:32:53 report=none tool=changed contract=changed toolsha=6f81f8be… ctsha=8c2561b0…
POLL_ABSENT tries=40
```

The first poller was killed at try 15 by a 300 s wrapper cap (not by the protocol); tries 16–40 continued in `poll-cont.sh`. At try 40 the S1 report was absent. After that window the tool moved `6f81f8be…` → `fb9bb9ff…` (message string only: `fixture bytes changed outside the frozen inventory` → `pinned-file bytes changed outside the semantic inventory`; contract stayed `8c2561b0…`). That is a mid-edit revision, so a stall-escape was recorded rather than scoring the try-40 bytes:

```
STALL-ESCAPE start after POLL_ABSENT tries=40; tool moved post-window; extra tries 41-55
try=51 t=22:49:15 report=…/S1-full-file-pins.md toolsha=fb9bb9ff… ctsha=8c2561b0…
STAB i=53 sha=67d630b30cd0622820006fb5679462341b8d5224b8d6730dde9937f5654f1f05 stable=2
POLL_HIT try=53 report=…/S1-full-file-pins.md tool=fb9bb9ff… contract=8c2561b0… STALL-ESCAPE
```

V08's report was absent at matrix time. A separate V08-only poll (not an all-reports poll) hit at try 5: `V08-c1-negative-rerun.md` sha256 `198e08b243f42d6eaee105ebfbdfa93ccd532679cef70c7709e3e6a3f3f13b34`.

## 1. Method

Independent harness, not V08's `battery.py`. Each probe is a fresh scratch mirror of the snapshotted tool, contract, and the six chain fixtures. Mutations stay in the mirror. Each probe ran twice. Three rows printed `stable=False` because the finding embeds the mirror path or a `TemporaryDirectory` suffix (`N-path-mismatch`, `N-scope-outside`, `N-env-self-test`). Re-invoking those mirrors and normalizing only that suffix: exits equal and path-normalized stdout equal on all three. IDs did not flake.

An exploratory run on the same sha pair before `S1-full-file-pins.md` existed is not the verdict. The quotes below are from the post-hit `final` run unless marked as the separate gate probe.

## 2. Before (baseline `4265df5`, scratch mirror)

```
$ python3 V43-scratch/pre/corpus/tools/dependency_freeze.py --self-test
SELF-TEST 17/17
RESULT PASS
EXIT 0
```

Chain verify on that mirror, all exit 0, JSON-only digests `15ef230e… / 2527beb9… / d541ae64… / d422a9b3… / 3c922d20… / 59a0f4fa…`.

Appending a comment to `r95-crossing-aftermath/fictional-excerpts.md` and verifying with the baseline tool: `DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9` / `RESULT PASS` / exit 0. The prose edit was invisible to the freeze.

Same for the dependency-wording replacement (`depends on both ninth-bell entries` → `follows both ninth-bell entries`) in the official matrix row `B-wording-invisible`:

```
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
RESULT PASS
```

## 3. Delivered matrix

Pin shape, recomputed in the harness (not by calling the tool): each of the six pins has `payload_schema_version` 2, `pinned_files` equal to the declared ten, and per-file plus content digests equal to the fixture bytes. r88's `symbolism-clause-map.md` is not in the pin. Pin set is exactly the six chain names. Inherited `events` / `relations` / `counts` match the r98 contract; the only self-test key added is `markdown_tamper`; the 17 inherited expectation objects are unchanged. Content digests moved off the JSON-only pins:

```
r88 acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
r94 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef
r95 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
r96 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c
r97 a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54
r98 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
```

Chain verify of all six: exit 0, `RESULT PASS`, contract unchanged. Those digests match S1's re-verify receipts.

Self-test on the mirror tool:

```
CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
SELF-TEST 18/18
RESULT PASS
```

**Every pinned file, one trailing newline, r95.** Each exit 2, ID `DIGEST-MISMATCH`, and the finding names only that file. Representative (the after-sha matches V08's timeline-class newline row for `entities.json`):

```
FINDING DIGEST-MISMATCH: content digest dca16aa3065e2da7581bb42846ec72c67e22b8680e81c7806b7b7ab842cab7ee != pin 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710; changed: entities.json (sha256 026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b -> 3489f303d1e9c4e34610294e788ca1f304bd9093d28b5c704b7556b86b57550f); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
```

The other nine (`relations.json`, `timeline.json`, `sources.json`, `contradictions.json`, `README.md`, `claim-excerpt-map.md`, `fictional-excerpts.md`, `inspiration-note.md`, `source-excerpt.md`) are the same ID, exit, and single-file naming. Two files at once (`README.md` and `source-excerpt.md`) names both.

Dependency-wording removal on the delivered pin:

```
FINDING DIGEST-MISMATCH: … changed: fictional-excerpts.md (sha256 0ef6734ae52d28656e75869d942d6b1e8e324b116977a2811b3b36dc0880b282 -> b0725e215a8c51bd0dda5b384396913a6d8ea36e58caa928d5b0315d47fc1aae); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
```

exit 2. Same phrase was exit 0 on the baseline tool (section 2).

**Exit 1 semantic class, all on r95, contract unchanged:**

| row | exit | ID |
|---|---|---|
| drop `evin-ninth-bell` from `paired-crossing-decision` | 1 | `REDUCTION-DETECTED` |
| phantom edge on `aftermath-missing-evin` | 1 | `ADDITION-DETECTED` |
| `place_id` flip | 1 | `ENDPOINT-CHANGE` |
| relation endpoint flip | 1 | `ENDPOINT-CHANGE` |
| relations cleared | 1 | `REDUCTION-DETECTED` |
| relation added | 1 | `ADDITION-DETECTED` |
| event removed | 1 | `REDUCTION-DETECTED` |

Quoted reduction line, same event and edge V08 dropped:

```
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 2/3; relations 1/1
FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']
RESULT FAIL
```

Precedence: that edge drop plus a README newline stays exit 1 `REDUCTION-DETECTED` only. No `DIGEST-MISMATCH`.

**Exit 2 structural class:**

| row | exit | ID |
|---|---|---|
| `timeline.json` → `[{` | 2 | `MALFORMED-JSON` |
| `timeline.json` deleted | 2 | `FILE-MISSING` |
| `timeline.json` non-UTF-8 | 2 | `MALFORMED-JSON` |
| timeline not an array | 2 | `MALFORMED-MODEL` |
| duplicate event id | 2 | `MALFORMED-MODEL` |
| `depends_on` not strings | 2 | `MALFORMED-MODEL` |
| relation missing from/to/type | 2 | `MALFORMED-MODEL` |
| renamed copy `v43-unpinned` | 2 | `UNPINNED-FIXTURE` |
| absent path whose basename is not a pin | 2 | `UNPINNED-FIXTURE` |
| pinned directory deleted, same path invoked | 2 | `FIXTURE-MISSING` |
| foreign same-named copy | 2 | `PATH-MISMATCH` |
| fixture and `--freeze` together | 2 | `INVALID-ARGUMENTS` |
| `--freeze` outside `corpus/fixtures/**` | 2 | `SCOPE-REFUSED` |
| `--freeze corpus/fixtures` | 2 | `SCOPE-REFUSED` |
| `--freeze` same name, other in-scope path | 2 | `SCOPE-REFUSED` |
| `--freeze` fixture missing `inspiration-note.md` | 2 | `FILE-MISSING` (pin not written) |
| pin `payload_schema_version` 1 | 2 | `CONTRACT-INVALID` |
| pin `files` missing `README.md` | 2 | `CONTRACT-INVALID` |
| pin `pinned_files` shortened | 2 | `CONTRACT-INVALID` |
| contract deleted / not JSON | 2 | `CONTRACT-INVALID` |
| `markdown_tamper` key deleted from expectations | 2 | `CONTRACT-INVALID` |
| `clean.exit` set to 1, then `--self-test` | 2 | `SELF-TEST-MISMATCH` |
| r98 schema-1 pin under the delivered tool | 2 | `CONTRACT-INVALID` (`payload_schema_version None != 2`) |

Pinned-dir absence:

```
FINDING FIXTURE-MISSING: fixture directory not found: corpus/fixtures/r95-crossing-aftermath
RESULT ERROR
```

Verify-side deletion of a non-required pinned file is not `FILE-MISSING`. It is `DIGEST-MISMATCH` and names the file with `-> None`:

```
FINDING DIGEST-MISMATCH: … changed: inspiration-note.md (sha256 58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37 -> None); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
```

Same ID for a deleted `contradictions.json`. Freeze-side absence remains `FILE-MISSING` and does not rewrite the pin. Both are exit 2 and name the file. That matches S1's stated contract (verify names a deletion; freeze refuses a missing declared file).

Non-UTF-8 markdown is `DIGEST-MISMATCH` naming `fictional-excerpts.md`, not `MALFORMED-JSON`. Markdown is hashed, not parsed.

**Upgrade path.** Delivered tool plus the r98 contract refuses verify (`CONTRACT-INVALID`, schema None). Guarded `--freeze` of that mirror then writes a schema-2 ten-file pin whose content digest and file map equal the delivered r95 pin (`digest_eq_delivered=True`, `files_eq_delivered=True`). Path-less `--freeze` on the canonical path prints `MIGRATED r95-crossing-aftermath: path-less legacy pin now names corpus/fixtures/r95-crossing-aftermath`, exits 0, and the new pin has schema 2 and all ten files, digest `97cffd7b…`.

**Neutralization.** Replacing `for name in MARKDOWN_FILES` with `for name in ():` does not make a markdown edit pass. Verify exits 2 `DIGEST-MISMATCH` naming all five markdown files as `-> None`. `--self-test` exits 2 `SELF-TEST-MISMATCH` because `clean` fails; `markdown_tamper` still exits 2 `DIGEST-MISMATCH` and so still matches its own expectation. The case is load-bearing for a real newline edit when hashing is present (18/18, and the contract's `names_file` check is in the delivered `run_self_test`). It is not, by itself, the detector of "stop hashing markdown" — `clean` fails first. Fail-closed either way.

Seen finding IDs: all 14 (`REDUCTION-DETECTED`, `ADDITION-DETECTED`, `ENDPOINT-CHANGE`, `DIGEST-MISMATCH`, `UNPINNED-FIXTURE`, `CONTRACT-INVALID`, `FIXTURE-MISSING`, `PATH-MISMATCH`, `FILE-MISSING`, `MALFORMED-JSON`, `MALFORMED-MODEL`, `INVALID-ARGUMENTS`, `SELF-TEST-MISMATCH`, `SCOPE-REFUSED`). `MISSING_IDS []`.

## 4. Unanchored heading — the class that was invisible to every gate

Separate scratch mirrors `V43-scratch/gate-before` (r98 tool+contract) and `gate-after` (delivered snap). Only change: `# Authored in-world excerpts` → that heading plus ` (dependency wording left intact)` in `r94-paired-crossing/fictional-excerpts.md`. That token is not a map anchor.

Before, cwd `gate-before`:

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing
DIGEST 2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75
RESULT PASS
EXIT 0

$ python3 corpus/tools/support_check.py corpus/fixtures/r94-paired-crossing
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; … VALIDATED-ROWS 16/16
RESULT PASS
EXIT 0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing
OBLIGATIONS raw=14 mapped=14
RESULT PASS
EXIT 0

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT 0
```

After, same edit, delivered tool+contract:

```
FINDING DIGEST-MISMATCH: content digest f559baaa7e6facbefb8a65f6be4eb4b5feb622c233e18bd4ace5ba03c332a034 != pin 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef; changed: fictional-excerpts.md (sha256 585f4d0746eadffcdd13a12aa4068392820201ae668dc9b66e9154beccf495c2 -> 1deff0153f063b504cb4e2414c1d6bfd5d9c889c8a1c92fbf279c41d7f18be33); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
EXIT 2
```

Digest and file shas match S1's non-anchor receipt. Not re-run here: S1's J14 `support_check` exit 1 on the anchored sentence removal. That sentence is a map anchor, so "invisible to every gate" does not hold for it. The unanchored heading is the class that was green on all four gates before and is named `DIGEST-MISMATCH` after. Edit-detectable, not semantics-provable.

## 5. ID comparison with V08

V08 report `V08-c1-negative-rerun.md` sha256 `198e08b2…`, same tool/contract shas. Overlapping classes:

| class | V43 | V08 | agree |
|---|---|---|---|
| `REDUCTION-DETECTED` edge drop on `paired-crossing-decision` / `evin-ninth-bell` | exit 1 | exit 1, same event and edge | yes |
| `ADDITION-DETECTED` / `ENDPOINT-CHANGE` | exit 1 | exit 1 | yes |
| precedence (edge drop + README newline) | exit 1, no digest finding | exit 1, no digest finding | yes |
| trailing newline on each of the ten files | exit 2 `DIGEST-MISMATCH`, names that file | same; `entities.json` after-sha `3489f303…` matches | yes |
| `FILE-MISSING` deleted `timeline.json` | exit 2 | exit 2 | yes |
| `FILE-MISSING` on `--freeze` of a fixture missing a declared markdown file | exit 2, pin not written | exit 2 (`README.md` missing) | yes |
| `MALFORMED-JSON` | exit 2 | exit 2 | yes |
| `SCOPE-REFUSED` outside / fixtures root / same-name | exit 2 | exit 2, same message shapes | yes |
| `PATH-MISMATCH` | exit 2 | exit 2 | yes |
| `INVALID-ARGUMENTS` fixture+`--freeze` | exit 2 | exit 2 | yes |
| `SELF-TEST-MISMATCH` corrupted `clean.exit` | exit 2, `cases failed: ['clean']` | exit 2, same | yes |
| baseline markdown edit | exit 0, JSON-only digest | exit 0 | yes |
| `symbolism-clause-map.md` edit | exit 0, digest `acf677a7…` | exit 0, same digest | yes |
| chain digests r88 / r95 / r98 | `acf677a7…` / `97cffd7b…` / `5ecf84e1…` | same | yes |

No ID or exit disagreement on any class both seats ran.

Coverage, not contradiction: V08 also ran an unpinned-event addition (`ADDITION-DETECTED`), no-args and `--self-test`+fixture `INVALID-ARGUMENTS`, and a 25-row markdown sweep on the other five pins. This seat did not re-run those three shapes. This seat additionally ran `CONTRACT-INVALID` (schema, incomplete file map, shortened `pinned_files`, missing/bad contract, dropped case key, schema-1 pin), `UNPINNED-FIXTURE`, `FIXTURE-MISSING`, four `MALFORMED-MODEL` shapes, path-less migration, the schema-1 upgrade freeze (digest equal to the delivered pin), neutralization, the ambient env marker, verify-side deletion (`-> None`), and the four-gate unanchored heading probe. V08's bottom line does not list `CONTRACT-INVALID`, `UNPINNED-FIXTURE`, `FIXTURE-MISSING`, or `MALFORMED-MODEL`; those are extra coverage here, not a conflict with their reported IDs.

## 6. Bounds (recorded, none a silent hole in the ten-file claim)

1. **Eleventh file.** `r88-m3-maya-cluster/symbolism-clause-map.md` is outside the declared ten. A trailing newline still verifies exit 0, digest `acf677a7…`. Same bound V08 recorded.
2. **Path-less migration adopts the invoked in-scope path.** `--freeze corpus/fixtures/nested/r95-crossing-aftermath` on a path-less pin exits 0 and records that nested path. r98 bound, not closed by r99. Pins that already record a path still `SCOPE-REFUSED`.
3. **Content digest is the verify gate; the per-file map is not rechecked when it matches.** Setting `pin.files["README.md"]` to 64 zeroes while leaving `content_sha256` equal still exits 0. A fixture edit still changes the recomputed digest and is named. A hand-edited pin can lie about one file hash. Low severity.
4. **Root `schema_version` is documentary.** Setting it to 1 while pins stay at payload schema 2 still verifies exit 0. The load-bearing check is `pin.payload_schema_version` (None or 1 → `CONTRACT-INVALID`).
5. **Verify-side deletion ID is `DIGEST-MISMATCH`, not `FILE-MISSING`.** Names the file (`-> None`), exit 2. Freeze-side absence is `FILE-MISSING`. Not a miss of the edit.
6. **Env marker.** `DEPENDENCY_FREEZE_SELF_TEST_CHILD=1 --self-test` exits 2 `SELF-TEST-MISMATCH` (`self_test_mismatch` inner run is `FIXTURE-MISSING`). Verify of r95 under the same variable exits 0. Stdout differs only by the temp-dir suffix.
7. **Anchored wording is not "every gate".** See section 4. The declaration's phrase is true for an unanchored heading edit, not for a sentence that is a `support_check` anchor. Not re-proven here as a `support_check` failure; S1's J14 receipt stands as theirs.

## 7. Hygiene

`git status --porcelain -- corpus/tools corpus/fixtures` shows `dependency_freeze.py`, `dependency-freeze-contract.json`, `corpus/tools/README.md` (S2), and untracked `corpus/fixtures/r99-window-lapse/`. None of those were written by this seat. No `dependency-freeze-self-test-*` residue at the lane root. Live shas at report time still `fb9bb9ff…` / `8c2561b0…`.

## Bottom line

**PASS** — on the post-stall-escape revision (`fb9bb9ff…` / `8c2561b0…`, report `S1-full-file-pins.md`), the independent 14-ID matrix on scratch mirrors is stable: every pinned-file byte edit exits 2 `DIGEST-MISMATCH` naming the file; semantic findings still exit 1 and win precedence; self-test is 18/18; the six pins match an independent ten-file digest and verify 6/6; an unanchored heading edit is exit 0 on all four r98 gates and exit 2 `DIGEST-MISMATCH` after. V08's IDs agree on every overlapping class. Bounds recorded (eleventh file, path-less migration, content-digest-only recheck, documentary root schema, deletion ID split); none is a silent miss of a declared pinned-file edit.
