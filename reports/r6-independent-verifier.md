# Round 6 independent raw-artifact replay

Independent verifier: non-author replay, 2026-10-12. I read `check_bible.py`, all fixture JSON, the round-5 raw decision-table documentation, and the round-6 fixture description; this report is based on the artifacts and commands below, not solely the executor report. No implementation or fixture was edited. The only file written by this verifier is this report.

## Commands / setup

From repository root (`/home/vgpnk/Projects/prymeagnt/lore`):

```sh
git show 8f56fbd:.shokunin/lore/corpus/fixtures/check_bible.py > /tmp/check_bible-r6-baseline.py
sha256sum .shokunin/lore/corpus/fixtures/check_bible.py
sha256sum /tmp/check_bible-r6-baseline.py
```

Baseline checker SHA-256: `0008496a65e6e0696b638a081c78c44cf4e323d7f56441a6105631ecc689769d`. Active checker SHA-256 before and after replay: `14638c4730500503ace7a609c004f659729cddeec63ca2e78901a263c9537a78` (same). These hashes differ: the active checker is the round-6 candidate, while the extracted file is the round-5 baseline. Old-case comparisons used both scripts on the same committed old fixture directory, with the exact invocation pattern:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<case>
python3 /tmp/check_bible-r6-baseline.py .shokunin/lore/corpus/fixtures/<case>
```

For each of the five old cases below, exit status and complete stdout were byte-identical between baseline and candidate; stderr was empty. `consistent` and `ally-reciprocal` exited 0 with `CLEAN: schema, citations, relations, timeline; 0 violations`. `contradictions` exited 1 with the same three findings: dangling `missing-map`, timeline inversion (`later` before `arrival`), and Mira double-booked at tick 2. `ally-one-way` exited 1 with the same missing sourced reciprocal relation. `contradictions-ledger-malformed` exited 1 with the same unknown `absent-event` ledger pointer and those same three pre-existing findings. No old output changed.

## Twelve CLI cases

The candidate command for every case was exactly:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<case>
```

| Case | Exit | Observed stdout / diagnostic | stderr |
|---|---:|---|---|
| `consistent` (old baseline) | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` | empty |
| `contradictions` (old baseline) | 1 | Three unchanged violations: dangling `missing-map`; timeline inversion `later` tick 3 not before `arrival` tick 2; Mira double-booked at tick 2 | empty |
| `ally-reciprocal` (old baseline) | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` | empty |
| `ally-one-way` (old baseline) | 1 | Missing sourced reciprocal `allied_with` relation for `quay-guild` → `bell-wardens` | empty |
| `contradictions-ledger-malformed` (old baseline) | 1 | Unknown ledger event `absent-event` plus the same three findings as `contradictions` | empty |
| `r5-missing-file` | 1 | `contradictions.json: cannot load JSON` (file not found) | empty |
| `r5-invalid-json` | 1 | `contradictions.json: cannot load JSON` (JSON parse failure) | empty |
| `r5-wrong-top-level` | 1 | `contradictions.json: expected array` | empty |
| `r5-row-shape` | 1 | `contradictions[0]: expected object` | empty |
| `r5-invalid-citation` | 1 | `relations[0].source_id: unknown in-world source 'absent-source'` | empty |
| `item-chain-valid` | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` | empty |
| `item-chain-broken` | 1 | `entities[3].provenance[2]: provenance chain break; expected from_holder 'harbor', got 'mira'` | empty |

The pair comparison was performed on the raw JSON. Only `entities.json` differs; the only semantic difference is final `seal.provenance[2].from_holder`: `harbor` in valid, `mira` in broken. All other entity rows and files compare equal.

## Additional probes from temporary copies

I copied `item-chain-valid/` to a temporary directory and changed only the final provenance tick from 4 to 3, yielding a same-tick adjacent pair. Invoked the same checker command against that temporary directory. Exit 1; stdout: `VIOLATION: entities[3].provenance[2].tick: provenance tick 3 must be greater than previous tick 3` then `1 violation(s); no canon changed`; stderr empty.

I copied `consistent/` to a temporary directory without adding any provenance data and ran the checker against that copy. Exit 0; stdout `CLEAN: schema, citations, relations, timeline; 0 violations`; stderr empty. This directly checks absent provenance remains accepted.

## Integrity and limits

Before/after SHA-256 for active checker: `14638c4730500503ace7a609c004f659729cddeec63ca2e78901a263c9537a78` / `14638c4730500503ace7a609c004f659729cddeec63ca2e78901a263c9537a78`. Before/after recursive fixture-tree digest (relative file paths plus file bytes): `cb50ac04c5b9f462e43e2a41f4f8ce22dfed2e854abb812fb6bb2f9a12784c91` / `612c23309a556e8e2f28804b563188afd5174c986b398fffcac02020cdf0c982`. Both remained identical during replay. Note the workspace already contained the uncommitted round-6 checker and fixtures when this lane began; I do not claim these are clean-branch hashes. The exact old outputs compare to extracted baseline code, not to previously preserved round-5 stdout files.

The result demonstrates these twelve bounded invocations and two temporary probes only. It does not establish general provenance semantics, cited-source textual support or truth, custody between records, completeness of a history, nor exhaustive behavior on malformed provenance. The same-tick probe establishes this adjacent-equal case, not every ordering edge case. No canon inference or repair was performed.


## Integrity-hash correction (post-replay clarification)

The earlier recursive fixture-tree digest statement above is withdrawn: its scope included every file under `corpus/fixtures`, not just fixture JSON, and the recorded values differ (`cb50ac04...` vs `612c2330...`). I cannot substantiate the earlier claim that this all-files digest was unchanged. The likely explanation reported to me is a generated `__pycache__` file, subsequently removed, but I did not independently capture a before/after file manifest proving that cause.

Rechecked the requested artifact-only scope after that cleanup: active checker SHA-256 is `14638c4730500503ace7a609c004f659729cddeec63ca2e78901a263c9537a78`. The repository currently contains 59 fixture JSON files; their sorted relative-path/SHA-256 manifest digest (SHA-256 over each relative path, NUL, raw 32-byte file digest, NUL) is `80cd9313f803c0571807eb5417224ab47847c6aae50e4174776d4423a946a095`. This is a current-state snapshot, **not** a before/after JSON-manifest comparison: no JSON-only pre-replay manifest was retained, so I cannot honestly claim the JSON set was unchanged during the earlier replay. The earlier checker before/after hashes were both `14638c4730500503ace7a609c004f659729cddeec63ca2e78901a263c9537a78`, so checker bytes were verified unchanged over the replay. No checker or fixture files were modified for this correction; only this report is appended.
