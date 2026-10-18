# V85 c1-ten-file-proof

Seat: V85. Read-only on producer bytes. Writes: this report and `.ufo/waves/round-99/seats/V85-scratch/` only. No commit. Lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`. Snapshot time `Sat Oct 17 10:51:24 PM -03 2026`.

Axes: completeness (every C1 chain fixture, not a sample); set equality (missing pinned file and extra unpinned file both count); detectability (an omitted file's edit must not stay invisible); evidence (quoted commands on the delivered pin, not the declaration).

## Scope

C1 chain = the six fixtures named in the delivered pin set. That matches the claim's 6/6, the contract provenance ("the six chain fixtures were re-frozen"), and S1's report (`S1-full-file-pins.md`, mtime 22:48): "C1's chain is the existing six." Pin keys, in contract order:

`r88-m3-maya-cluster`, `r94-paired-crossing`, `r95-crossing-aftermath`, `r96-crossing-response`, `r97-crossing-acknowledgment`, `r98-clerk-filing`.

Declared ten, contract root `pinned_files` and every pin's `pinned_files` / `files` keys:

`entities.json`, `relations.json`, `timeline.json`, `sources.json`, `contradictions.json`, `README.md`, `claim-excerpt-map.md`, `fictional-excerpts.md`, `inspiration-note.md`, `source-excerpt.md`.

`r99-window-lapse` is not in that set. S1 left it unpinned on purpose. It is recorded below and is not treated as a C1 chain fixture.

## Poll

Tries 1–20 started 22:02:42. Ten-file pins first appeared at try 20 (22:09:02); S1 report still absent; early exit recorded in `V85-scratch/poll.log`. Tries 21–40 resumed 22:36:37. Try 40 at 22:42:57: S1 report still ABSENT; contract stable since 22:08:46 (`ct_mtime=1792285726`, size 25987); pin counts stayed 10/10/10/10/10/10. Stall-escape: the pin artifact was already on disk, so this seat did not stop at ABSENT and did not verify the LOG declaration. S1's report was present on the post-window recheck (`ls` at 22:49:38 showed `S1-full-file-pins.md`, 11971 bytes, 22:48). Contract mtime did not move after that report. Verdict is on the on-disk pin plus that report.

## Listing vs pin

Command (lane root), observed 22:51:24:

```
ls -A corpus/fixtures/<name>
```

`r88-m3-maya-cluster` (11 names):

```
claim-excerpt-map.md
contradictions.json
entities.json
fictional-excerpts.md
inspiration-note.md
README.md
relations.json
source-excerpt.md
sources.json
symbolism-clause-map.md
timeline.json
```

`r94-paired-crossing`, `r95-crossing-aftermath`, `r96-crossing-response`, `r97-crossing-acknowledgment`, `r98-clerk-filing`: each `ls -A` printed exactly the declared ten, exit 0. No dotfiles. `find` of those six directories with `-mindepth 2` printed nothing (`find_exit=0`). No subdirectory, symlink, or other non-file in any of the six (`nonfile=[]`).

Set compare against `corpus/tools/dependency-freeze-contract.json` (`schema_version` 2, `payload_schema_version` 2), same snapshot:

| fixture | disk | pin.files | missing pinned | extra unpinned | pinned digests vs disk |
|---|---|---|---|---|---|
| r88-m3-maya-cluster | 11 | 10 | none | `symbolism-clause-map.md` | match |
| r94-paired-crossing | 10 | 10 | none | none | match |
| r95-crossing-aftermath | 10 | 10 | none | none | match |
| r96-crossing-response | 10 | 10 | none | none | match |
| r97-crossing-acknowledgment | 10 | 10 | none | none | match |
| r98-clerk-filing | 10 | 10 | none | none | match |

Each pin's `pinned_files` equals the declared ten. `symbolism-clause-map.md` is not a key of `pins["r88-m3-maya-cluster"]["files"]`. Live file sha256 `4bfe975967844bc6edaeb0375c22784de5c1295d3e1ae8606e0e3390a5f4783d`, 1094 bytes.

No missing pinned file in any chain fixture.

## The extra file is invisible to verify

`build_model` reads only `PINNED_FILES` (`DATA_FILES + MARKDOWN_FILES`). It never lists the directory. `--freeze` refuses a missing member of that closed list; it does not refuse an extra file.

Live verify (not `--freeze`; contract mtime stayed 22:08:46):

```
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r88-m3-maya-cluster
```

```
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
RESULT PASS
```

exit 0. The receipt label is `FREEZE` even on the verify path (`dependency_freeze.py` verify() builds that string). The other five also exited 0 with `RESULT PASS`.

Scratch copy only (`V85-scratch/omit-probe-final/`), final tool bytes copied in, pin path left as `corpus/fixtures/r88-m3-maya-cluster` relative to that tree. Appending `\nOMITTED-FILE-TAMPER\n` to the copy of `symbolism-clause-map.md` (sha256 `4bfe9759…` → `c10fba15d8e98b8ec10b507c0d69fcaa8f28776090cdb9b6880b51d96f9a741d`) still exited 0, same digest `acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae`, `RESULT PASS`. Appending one newline to the copy of `README.md` exited 2:

```
FINDING DIGEST-MISMATCH: content digest 134a79db887f81be6d7b9ce8931401892403d11890ad19893d472163e088bca5 != pin acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae; changed: README.md (sha256 55c9ba57ad7af5db0320fdc09142588c363c8b726d5ae1023dc01264f29b857c -> a1d9a942aef8928cbb1ff13b6448b60395bd293cc7886e1f14a4186a21bb6b44); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
```

So a pinned-file edit is named. An edit to the eleventh file is not.

S1 recorded the omission, not a miss. Contract `provenance_note`: "r88's extra symbolism-clause-map.md stays outside the declared ten". S1 report: "`r88-m3-maya-cluster/symbolism-clause-map.md` is outside the declared ten and is not pinned." The closed ten-name list is what shipped. The directory is not that list.

## r99, not a C1 chain pin

`ls -A corpus/fixtures/r99-window-lapse` printed exactly the declared ten. No eleventh file there.

```
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse
```

```
FINDING UNPINNED-FIXTURE: no pin for 'r99-window-lapse' in corpus/tools/dependency-freeze-contract.json (pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing'])
RESULT ERROR
```

exit 2. That is an absent pin for a fixture outside the delivered C1 chain, not an eleventh file inside a pin. 173 fixture directories exist under `corpus/fixtures/`; only the six pins were compared as the chain.

## Finding

Extra unpinned file: `corpus/fixtures/r88-m3-maya-cluster/symbolism-clause-map.md`. The pin omits it. Verify does not see it. Missing pinned files: none.

FAIL — chain fixture r88-m3-maya-cluster has an eleventh file the pin omits (symbolism-clause-map.md); the other five chain fixtures match the pin exactly.
