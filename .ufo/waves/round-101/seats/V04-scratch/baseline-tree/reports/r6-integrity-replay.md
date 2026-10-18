# Round 6 integrity replay (independent)

No checker import and no code or fixture edits were made. The checker was run as a CLI. The only repository file written for this replay is this report.

## Method

From repository root, the pre/post inventory consists of `.shokunin/lore/corpus/fixtures/check_bible.py` plus every regular file matched recursively by `*.json` under `.shokunin/lore/corpus/fixtures/` (no other fixture file types). Count: **59 JSON files + checker = 60 paths**. Digest method: SHA-256 of each file’s raw bytes; paths are repository-relative. Exact pair comparison uses the full `(path, digest)` mappings, including additions/removals.

Equivalent Python algorithm:

```python
import hashlib
from pathlib import Path
root = Path.cwd()
fixtures = root / ".shokunin/lore/corpus/fixtures"
files = [fixtures / "check_bible.py"] + sorted(p for p in fixtures.rglob("*.json") if p.is_file())
mapping = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
```

For each target, the CLI command was `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<target>`; stdout and stderr were separately redirected to files, and the process status was recorded immediately. No module import was used. Output capture:

| Target | Exit | stdout | stderr |
|---|---:|---|---|
| `item-chain-valid` | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` | (empty) |
| `item-chain-broken` | 1 | `VIOLATION: entities[3].provenance[2]: provenance chain break; expected from_holder 'harbor', got 'mira'
1 violation(s); no canon changed` | (empty) |
| `consistent` | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` | (empty) |
| `contradictions` | 1 | `VIOLATION: relations[1].to: dangling entity 'missing-map'
VIOLATION: timeline[1].depends_on: timeline inversion 'later' tick 3 not before 'arrival' tick 2
VIOLATION: timeline[2]: double-booked 'mira' at tick 2 in timeline[1] ('tower') and 'harbor'
3 violation(s); no canon changed` | (empty) |
| `r5-invalid-citation` | 1 | `VIOLATION: relations[0].source_id: unknown in-world source 'absent-source'
1 violation(s); no canon changed` | (empty) |

## Input integrity result

**No input bytes changed.** Pre-run and post-run inventories each contained 60 paths; their exact path+SHA-256 mappings were equal (no changed, added, or removed paths). Outputs: item-chain-valid and consistent were CLEAN with exit 0; item-chain-broken, contradictions, and r5-invalid-citation each reported violations with exit 1. Thus the observed outputs match the expected valid/invalid distinction of these fixtures.

## Exact SHA-256 inventory

Pre-run map and post-run map are identical. The following complete map therefore records both observed maps (sorted by repository-relative path):

```text
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  .shokunin/lore/corpus/fixtures/ally-one-way/contradictions.json
317ff21e03e7038eba6e414a97a37f1c2adfd8f0e98b4e3eba864120609f7c45  .shokunin/lore/corpus/fixtures/ally-one-way/entities.json
933839488045e6b6bda4b885a5766d90a4d6034c4f7107059ed83798580f2726  .shokunin/lore/corpus/fixtures/ally-one-way/relations.json
ded882756d6cfaf4bb7f542e27c0030b0af10312a25b89301636cacedd4214d1  .shokunin/lore/corpus/fixtures/ally-one-way/sources.json
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  .shokunin/lore/corpus/fixtures/ally-one-way/timeline.json
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  .shokunin/lore/corpus/fixtures/ally-reciprocal/contradictions.json
317ff21e03e7038eba6e414a97a37f1c2adfd8f0e98b4e3eba864120609f7c45  .shokunin/lore/corpus/fixtures/ally-reciprocal/entities.json
7882d138cb8178c0d674ee8d3ea64954eef5ce9428a0c2f7efbb6017a71e81c2  .shokunin/lore/corpus/fixtures/ally-reciprocal/relations.json
ded882756d6cfaf4bb7f542e27c0030b0af10312a25b89301636cacedd4214d1  .shokunin/lore/corpus/fixtures/ally-reciprocal/sources.json
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  .shokunin/lore/corpus/fixtures/ally-reciprocal/timeline.json
14638c4730500503ace7a609c004f659729cddeec63ca2e78901a263c9537a78  .shokunin/lore/corpus/fixtures/check_bible.py
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  .shokunin/lore/corpus/fixtures/consistent/contradictions.json
b285c561b6d338a8f3f4d4d94692ad30951fd4afb3c60f93164e3471297801ac  .shokunin/lore/corpus/fixtures/consistent/entities.json
d983a04cfa8d51dab5a2fc92032ab29696d80c3dc6d5384d724e6225b6fd0b4f  .shokunin/lore/corpus/fixtures/consistent/relations.json
644767a6b53acc9760a441cb38663d4110219f9a80a56f4cfb90f0dc655d77f4  .shokunin/lore/corpus/fixtures/consistent/sources.json
2ba4a9d51a20d2a76387c25cee9e064f9440fd45984d07d5e5f8ec05666b3968  .shokunin/lore/corpus/fixtures/consistent/timeline.json
3f479df414f98274e75811657051c1dacb9c905dedc0b4d51ebf4282f8950a35  .shokunin/lore/corpus/fixtures/contradictions-ledger-malformed/contradictions.json
b285c561b6d338a8f3f4d4d94692ad30951fd4afb3c60f93164e3471297801ac  .shokunin/lore/corpus/fixtures/contradictions-ledger-malformed/entities.json
5ba89505e83b4d8c999619f253bc8c8c2bffbc15073836f6eab009cb56964a19  .shokunin/lore/corpus/fixtures/contradictions-ledger-malformed/relations.json
644767a6b53acc9760a441cb38663d4110219f9a80a56f4cfb90f0dc655d77f4  .shokunin/lore/corpus/fixtures/contradictions-ledger-malformed/sources.json
0050252d49dc0596b110c2d2dff6f03e87f3ba0cb18072162db4743f8d834b50  .shokunin/lore/corpus/fixtures/contradictions-ledger-malformed/timeline.json
131890ede960716bcc46da5e0afa1a4a8e10b52300e3f10beafda4acd79c5621  .shokunin/lore/corpus/fixtures/contradictions/contradictions.json
b285c561b6d338a8f3f4d4d94692ad30951fd4afb3c60f93164e3471297801ac  .shokunin/lore/corpus/fixtures/contradictions/entities.json
5ba89505e83b4d8c999619f253bc8c8c2bffbc15073836f6eab009cb56964a19  .shokunin/lore/corpus/fixtures/contradictions/relations.json
644767a6b53acc9760a441cb38663d4110219f9a80a56f4cfb90f0dc655d77f4  .shokunin/lore/corpus/fixtures/contradictions/sources.json
0050252d49dc0596b110c2d2dff6f03e87f3ba0cb18072162db4743f8d834b50  .shokunin/lore/corpus/fixtures/contradictions/timeline.json
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  .shokunin/lore/corpus/fixtures/item-chain-broken/contradictions.json
65374c8cafc05330ad39e05a9aff492ba13875a8994460b936b9e979b0757a74  .shokunin/lore/corpus/fixtures/item-chain-broken/entities.json
d983a04cfa8d51dab5a2fc92032ab29696d80c3dc6d5384d724e6225b6fd0b4f  .shokunin/lore/corpus/fixtures/item-chain-broken/relations.json
644767a6b53acc9760a441cb38663d4110219f9a80a56f4cfb90f0dc655d77f4  .shokunin/lore/corpus/fixtures/item-chain-broken/sources.json
2ba4a9d51a20d2a76387c25cee9e064f9440fd45984d07d5e5f8ec05666b3968  .shokunin/lore/corpus/fixtures/item-chain-broken/timeline.json
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  .shokunin/lore/corpus/fixtures/item-chain-valid/contradictions.json
fc1d000f9a17ead19e0f541fffd9752710dcfc7a12d73ec9cbc2a78db5ced637  .shokunin/lore/corpus/fixtures/item-chain-valid/entities.json
d983a04cfa8d51dab5a2fc92032ab29696d80c3dc6d5384d724e6225b6fd0b4f  .shokunin/lore/corpus/fixtures/item-chain-valid/relations.json
644767a6b53acc9760a441cb38663d4110219f9a80a56f4cfb90f0dc655d77f4  .shokunin/lore/corpus/fixtures/item-chain-valid/sources.json
2ba4a9d51a20d2a76387c25cee9e064f9440fd45984d07d5e5f8ec05666b3968  .shokunin/lore/corpus/fixtures/item-chain-valid/timeline.json
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  .shokunin/lore/corpus/fixtures/r5-invalid-citation/contradictions.json
b285c561b6d338a8f3f4d4d94692ad30951fd4afb3c60f93164e3471297801ac  .shokunin/lore/corpus/fixtures/r5-invalid-citation/entities.json
004fde3fbea3f0410a15e358ba4f8b86b402b92879bb0a35c7f15f9a04e492b0  .shokunin/lore/corpus/fixtures/r5-invalid-citation/relations.json
644767a6b53acc9760a441cb38663d4110219f9a80a56f4cfb90f0dc655d77f4  .shokunin/lore/corpus/fixtures/r5-invalid-citation/sources.json
2ba4a9d51a20d2a76387c25cee9e064f9440fd45984d07d5e5f8ec05666b3968  .shokunin/lore/corpus/fixtures/r5-invalid-citation/timeline.json
a6fb08fda1acb957b6116bd37811a1fe41a01611c0631edbf786d6889a27a55c  .shokunin/lore/corpus/fixtures/r5-invalid-json/contradictions.json
b285c561b6d338a8f3f4d4d94692ad30951fd4afb3c60f93164e3471297801ac  .shokunin/lore/corpus/fixtures/r5-invalid-json/entities.json
d983a04cfa8d51dab5a2fc92032ab29696d80c3dc6d5384d724e6225b6fd0b4f  .shokunin/lore/corpus/fixtures/r5-invalid-json/relations.json
644767a6b53acc9760a441cb38663d4110219f9a80a56f4cfb90f0dc655d77f4  .shokunin/lore/corpus/fixtures/r5-invalid-json/sources.json
2ba4a9d51a20d2a76387c25cee9e064f9440fd45984d07d5e5f8ec05666b3968  .shokunin/lore/corpus/fixtures/r5-invalid-json/timeline.json
b285c561b6d338a8f3f4d4d94692ad30951fd4afb3c60f93164e3471297801ac  .shokunin/lore/corpus/fixtures/r5-missing-file/entities.json
d983a04cfa8d51dab5a2fc92032ab29696d80c3dc6d5384d724e6225b6fd0b4f  .shokunin/lore/corpus/fixtures/r5-missing-file/relations.json
644767a6b53acc9760a441cb38663d4110219f9a80a56f4cfb90f0dc655d77f4  .shokunin/lore/corpus/fixtures/r5-missing-file/sources.json
2ba4a9d51a20d2a76387c25cee9e064f9440fd45984d07d5e5f8ec05666b3968  .shokunin/lore/corpus/fixtures/r5-missing-file/timeline.json
3fd749edd9d66aefcae32cac2b69026e4f11f37edd763160d42db7945dee8c32  .shokunin/lore/corpus/fixtures/r5-row-shape/contradictions.json
b285c561b6d338a8f3f4d4d94692ad30951fd4afb3c60f93164e3471297801ac  .shokunin/lore/corpus/fixtures/r5-row-shape/entities.json
d983a04cfa8d51dab5a2fc92032ab29696d80c3dc6d5384d724e6225b6fd0b4f  .shokunin/lore/corpus/fixtures/r5-row-shape/relations.json
644767a6b53acc9760a441cb38663d4110219f9a80a56f4cfb90f0dc655d77f4  .shokunin/lore/corpus/fixtures/r5-row-shape/sources.json
2ba4a9d51a20d2a76387c25cee9e064f9440fd45984d07d5e5f8ec05666b3968  .shokunin/lore/corpus/fixtures/r5-row-shape/timeline.json
ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356  .shokunin/lore/corpus/fixtures/r5-wrong-top-level/contradictions.json
b285c561b6d338a8f3f4d4d94692ad30951fd4afb3c60f93164e3471297801ac  .shokunin/lore/corpus/fixtures/r5-wrong-top-level/entities.json
d983a04cfa8d51dab5a2fc92032ab29696d80c3dc6d5384d724e6225b6fd0b4f  .shokunin/lore/corpus/fixtures/r5-wrong-top-level/relations.json
644767a6b53acc9760a441cb38663d4110219f9a80a56f4cfb90f0dc655d77f4  .shokunin/lore/corpus/fixtures/r5-wrong-top-level/sources.json
2ba4a9d51a20d2a76387c25cee9e064f9440fd45984d07d5e5f8ec05666b3968  .shokunin/lore/corpus/fixtures/r5-wrong-top-level/timeline.json
```
