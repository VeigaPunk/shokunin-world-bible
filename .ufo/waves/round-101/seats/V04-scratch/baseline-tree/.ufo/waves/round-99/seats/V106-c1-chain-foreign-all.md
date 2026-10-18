# V106 c1-chain-foreign-all

Seat: V106. Claim checked: foreign-path copies of all six chain fixtures each exit 2 `PATH-MISMATCH` (not only r94). Lane root: `/home/vgpnk/Projects/shokunin/lore-shokunin`. No commits. Writes: this report and `V106-scratch/` only.

## Poll and stall-escape

Artifacts polled 20 s × 40 (22:03:05–22:21:00). Contract became payload schema 2 with 10-file pins at try 19 (22:09:05). `S1*.md` was still absent at try 40. Bounded stall-escape, not fatal: tool and contract mtimes/sizes were unchanged from try 20 through the run at 22:30:07, and hashes were unchanged when rechecked at 22:32:22. Verified those delivered bytes, not the declaration.

Present producer reports at run time: `S3-fixture-author.md`, `S4-fixture-docs.md`. Absent: `S1*.md` (and S2/S5).

Delivered bytes:

- `corpus/tools/dependency_freeze.py` mtime `2026-10-17 22:07:33.506669398 -0300` size 29104 sha256 `6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067`
- `corpus/tools/dependency-freeze-contract.json` mtime `2026-10-17 22:08:46.248249589 -0300` size 25987 sha256 `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628`
- contract `schema_version` 2, `payload_schema_version` 2, `pinned_files` the ten declared names, `pin_count` 6

The six pins (r99-window-lapse is not pinned, so it is not one of the six): `r88-m3-maya-cluster`, `r94-paired-crossing`, `r95-crossing-aftermath`, `r96-crossing-response`, `r97-crossing-acknowledgment`, `r98-clerk-filing`. Each pin `files` has 10 keys and `payload_schema_version` 2.

`bind_path` on the delivered tool refuses any resolved path other than the pin's recorded path, before model build:

```
def bind_path(fixture, name, pin):
    expected = (ROOT / pin["fixture"]).resolve()
    observed = fixture.resolve()
    if observed != expected:
        fail("PATH-MISMATCH",
             f"pin {name} names {pin['fixture']} (resolves to {expected}); "
             f"invoked fixture resolves to {observed}")
```

## Method

Real `shutil.copytree` copies (not symlinks) under `V106-scratch/foreign/<fixture-name>`, keeping the directory name so pin lookup is by name and the failure is path, not `UNPINNED-FIXTURE`. Each copy's `resolve()` differed from the source. Invoked the delivered tool from the lane root. Canonical paths were a control only, so a foreign exit 2 is not a broken pin.

## All six foreign copies

| fixture | foreign exit | finding | canonical exit |
|---|---|---|---|
| r88-m3-maya-cluster | 2 | PATH-MISMATCH | 0 RESULT PASS |
| r94-paired-crossing | 2 | PATH-MISMATCH | 0 RESULT PASS |
| r95-crossing-aftermath | 2 | PATH-MISMATCH | 0 RESULT PASS |
| r96-crossing-response | 2 | PATH-MISMATCH | 0 RESULT PASS |
| r97-crossing-acknowledgment | 2 | PATH-MISMATCH | 0 RESULT PASS |
| r98-clerk-filing | 2 | PATH-MISMATCH | 0 RESULT PASS |

stderr empty on every foreign run. No `DIGEST-MISMATCH`, no `UNPINNED-FIXTURE`. Transcripts: `V106-scratch/run/<name>.txt` and `canon-<name>.txt`.

## Quoted two (not r94)

r88-m3-maya-cluster:

```
$ cd /home/vgpnk/Projects/shokunin/lore-shokunin && python3 /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V106-scratch/foreign/r88-m3-maya-cluster
# exit=2
FINDING PATH-MISMATCH: pin r88-m3-maya-cluster names corpus/fixtures/r88-m3-maya-cluster (resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r88-m3-maya-cluster); invoked fixture resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V106-scratch/foreign/r88-m3-maya-cluster
RESULT ERROR
```

r98-clerk-filing:

```
$ cd /home/vgpnk/Projects/shokunin/lore-shokunin && python3 /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V106-scratch/foreign/r98-clerk-filing
# exit=2
FINDING PATH-MISMATCH: pin r98-clerk-filing names corpus/fixtures/r98-clerk-filing (resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r98-clerk-filing); invoked fixture resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V106-scratch/foreign/r98-clerk-filing
RESULT ERROR
```

The other four foreign findings are the same shape. r94, for completeness, not as the only quote:

```
FINDING PATH-MISMATCH: pin r94-paired-crossing names corpus/fixtures/r94-paired-crossing (resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r94-paired-crossing); invoked fixture resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V106-scratch/foreign/r94-paired-crossing
RESULT ERROR
```

exit 2. Same for r95, r96, r97 (see transcripts).

## Not claimed

Did not re-run `--self-test`. Did not freeze. Did not treat `r99-window-lapse` as a seventh chain pin; it is absent from `pins`. r88's tree also contains `symbolism-clause-map.md` (source and copy); path refusal fires before content compare, so that extra file did not change this result.

PASS — all six foreign-path copies exit 2 PATH-MISMATCH (quoted r88 and r98; r94 is not the only case).
