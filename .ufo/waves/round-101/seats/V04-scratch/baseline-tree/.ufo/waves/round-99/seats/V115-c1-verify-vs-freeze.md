# V115 c1-verify-vs-freeze-exit

Seat: V115. Exclusive write: this report plus `.ufo/waves/round-99/seats/V115-scratch/`. No live `--freeze`. No commits. Lane root: `/home/vgpnk/Projects/shokunin/lore-shokunin`. Measured 2026-10-17.

Axes: exit-code fidelity (verify vs `--freeze`), isolation (live contract not rewritten), evidence (quoted commands).

## Poll

40 tries, 20 s cadence, 22:02:55–22:15:56. Log: `.ufo/waves/round-99/seats/V115-scratch/poll.log`. Ends `POLL-EXHAUSTED`.

- S1 producer report (`seats/S1*.md`): ABSENT on every try, and still absent at 22:20:10. `S1-scratch/before/mirror/` exists; it is not a report.
- Artifacts were not a plan. From try 19 (22:08:56) through try 40 the contract was schema 2, six pins, 10 files each, `payload_schema_version` 2. Tool mtime 22:07:33 and contract mtime 22:08:46 held through the measurement window.

Stall-escape recorded, not treated as fatal: the owned bytes were on disk and hash-stable, so the exit codes below are measurements of the delivered revision, not of the declaration.

Delivered hashes (unchanged from before the live verify through after every scratch `--freeze`, rechecked at 22:20:10):

- `corpus/tools/dependency_freeze.py` sha256 `6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067`
- `corpus/tools/dependency-freeze-contract.json` sha256 `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628`

Full command transcript: `.ufo/waves/round-99/seats/V115-scratch/symmetry-run.log`.

## What the exits mean

Verify (positional fixture) compares the tree to the pin. A digest-class edit exits 2 `DIGEST-MISMATCH` and names the file (`dependency_freeze.py` verify path). `--freeze` does not refuse a same-path tamper. It writes the observed pin, then calls verify on what it just wrote (`dependency_freeze.py:441-448`):

```
contract["pins"][name] = pin
contract["revision"] = revision
CONTRACT_PATH.write_text(...)
return verify(target, read_contract())
```

So on a clean target both commands exit 0. On a digest-tampered target they are not symmetric: verify exits 2; `--freeze` rewrites the pin to the tampered bytes and then exits 0. That rewrite was run only against copies under `V115-scratch/mirror-work/`, where `ROOT` is the mirror (`Path(__file__).parents[2]`), so `CONTRACT_PATH` is the scratch contract.

Contract text already states the verify half (`dependency-freeze-contract.json` `precedence`): a content change the inventory does not model exits 2 `DIGEST-MISMATCH` and names each changed pinned file. It does not state that `--freeze` on that same tamper exits 0. That half is documented here from the scratch runs.

`SKILL.md` freeze row, read after the measurement, still says the pin covers the five JSON tables, 17 self-test cases, and that BR-01's prose half remains open. That row is S2's file and was not updated in the window this seat observed. It is not the exit-code result.

## Clean targets — both 0

Live verify only (read-only). Six pins, each with the ten declared files. No `--freeze` on the live tree.

```
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r88-m3-maya-cluster
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
RESULT PASS
EXIT:0

python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef
RESULT PASS
EXIT:0

python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
RESULT PASS
EXIT:0

python3 corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c
RESULT PASS
EXIT:0

python3 corpus/tools/dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
DIGEST a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54
RESULT PASS
EXIT:0

python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
RESULT PASS
EXIT:0
```

Scratch mirrors (tool + contract + fixture copied; commands are the copied script). Verify then `--freeze`, each fixture:

| fixture | verify | --freeze | pin content_sha256 unchanged | per-file digests unchanged |
|---|---|---|---|---|
| r88-m3-maya-cluster | 0 | 0 | yes | yes |
| r94-paired-crossing | 0 | 0 | yes | yes |
| r95-crossing-aftermath | 0 | 0 | yes | yes |
| r96-crossing-response | 0 | 0 | yes | yes |
| r97-crossing-acknowledgment | 0 | 0 | yes | yes |
| r98-clerk-filing | 0 | 0 | yes | yes |

Representative scratch pair (r98; the other five printed the same shape, `RESULT PASS`, exit 0, digest equal to the live pin):

```
python3 <mirror>/corpus/tools/dependency_freeze.py <mirror>/corpus/fixtures/r98-clerk-filing
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
RESULT PASS
EXIT:0

python3 <mirror>/corpus/tools/dependency_freeze.py --freeze <mirror>/corpus/fixtures/r98-clerk-filing
FROZEN r98-clerk-filing: events 7; dependency-edges 6; relations 1
DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
RESULT PASS
EXIT:0
```

Idempotent rewrite check, separate mirror `clean-rewrite-proof`, same r98 copy, `--freeze` only:

```
scratch contract sha256 before=8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628
scratch contract sha256 after =8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628
contract file bytes changed=False
EXIT:0
```

`write_text` still runs. On an already-matching pin the serialized contract was byte-identical, so a clean `--freeze` did not change the pin. The live contract hash stayed `8c2561b0…` after every scratch freeze.

## Tampered — verify 2; scratch `--freeze` rewrites and exits 0

Not run on the live tree.

Markdown append, scratch copy of `r98-clerk-filing` `fictional-excerpts.md` (`+ b"\nV115 scratch tamper: prose byte added.\n"`):

```
python3 <mirror>/corpus/tools/dependency_freeze.py <mirror>/corpus/fixtures/r98-clerk-filing
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
FINDING DIGEST-MISMATCH: content digest abac966391ca9fb5391b8c0e453a88de067d9473afddf971668950279c415b40 != pin 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0; changed: fictional-excerpts.md (sha256 29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de -> 0136a06af0d673703deae1d3de0b7acd7c02bcc8cb3c74ffb691e8da6da9e6ca); fixture bytes changed outside the frozen inventory
RESULT ERROR
EXIT:2
```

Same tamper, separate mirror, `--freeze` only:

```
python3 <mirror>/corpus/tools/dependency_freeze.py --freeze <mirror>/corpus/fixtures/r98-clerk-filing
FROZEN r98-clerk-filing: events 7; dependency-edges 6; relations 1
DIGEST abac966391ca9fb5391b8c0e453a88de067d9473afddf971668950279c415b40
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST abac966391ca9fb5391b8c0e453a88de067d9473afddf971668950279c415b40
RESULT PASS
EXIT:0
```

Pin `files["fictional-excerpts.md"]` moved `29e384bf…` → `0136a06a…`, equal to the tampered file sha256. Content digest moved `5ecf84e1…` → `abac9663…`. A verify after that freeze exited 0. The tamper was absorbed, not rejected.

JSON trailing-newline doubling on scratch `r95-crossing-aftermath` `timeline.json` (parse unchanged, bytes changed):

```
FINDING DIGEST-MISMATCH: ... changed: timeline.json (sha256 3c0faad6bf32f944f9f2a20f3bd15829044afa04f1a8837601903433b00ea177 -> bd64e666f77d6981d2871fdab750d5622942c7c18ceca8cfdd8bc82fa6aa6ff2) ...
RESULT ERROR
EXIT:2
```

`--freeze` on a separate copy of that tamper exited 0, rewrote the pin's `timeline.json` digest to `bd64e666…`, and changed the content digest (`97cffd7b…` → `f79cefa3…`).

## Not claimed

- `r99-window-lapse` is not in `pins`. This seat did not freeze it and did not treat its absence as an exit-code failure.
- Self-test 17→18 was not this seat's measurement.
- `SKILL.md` still describing the five-file bound is S2's row, observed stale, not re-scored here.

## Bottom line

PASS — clean verify and `--freeze` both exit 0 on all six delivered pins; digest tamper verify exits 2 `DIGEST-MISMATCH` naming the file; scratch `--freeze` on that tamper rewrites the pin and exits 0. Live contract untouched. S1 report ABSENT after 40 polls (stall-escape; artifacts were present).
