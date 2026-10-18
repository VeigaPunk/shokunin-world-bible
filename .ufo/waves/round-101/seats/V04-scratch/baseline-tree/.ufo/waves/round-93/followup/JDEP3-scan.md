# JDEP3 scan receipt — cross-cluster referent comparison at HEAD 65838f8

Script: /tmp/jdep3/compare.py (verbatim below). Working tree == HEAD for all measured paths (`git status --porcelain` shows only `.ufo/waves/round-93/followup/` untracked).

```
$ python3 /tmp/jdep3/compare.py
== L1: all JSON id-bearing values per cluster ==
r87-myth-cluster: 17 ids
   ['ash-dune-sanctuary', 'bell-tally-return', 'dune-register', 'first-lowwater-signal', 'gate-witness', 'hara', 'lowwater-hymn', 'moon-basin-vow-dune-account', 'moon-basin-vow-gate-account', 'moon-basin-vow-location', 'mother-tide-gate', 'reed-bell', 'reedwardens', 'sen', 'shell-charter', 'shellweavers', 'tide-bell-tally']
r88-m3-maya-cluster: 8 ids
   ['aru', 'aru-ninth-bell', 'evin', 'evin-ninth-bell', 'paired-clock', 'quiet-rise', 'salt-court', 'veil-verse']
r93-m2-kojiki-cluster: 7 ids
   ['lorn-index', 'm2-record-archive', 'orni', 'orni-marks-index', 'slate-table', 'teva', 'teva-files-index']

== L2: entity display names (lowercased) ==
r87-myth-cluster: ['ash-dune sanctuary', 'hara', 'mother-tide gate', 'reed bell', 'reedwardens', 'sen', 'shellweavers']
r88-m3-maya-cluster: ['aru', 'evin', 'quiet rise', 'salt court']
r93-m2-kojiki-cluster: ['lorn index', 'orni', 'slate table', 'teva']

== L3: source titles (lowercased) ==
r87-myth-cluster: ['first low-water bell tally', "hara's mother-tide gate witness slip", 'low-water hymn of the basin', "sen's ash-dune sanctuary register", 'shellweaver–reedwarden shore charter']
r88-m3-maya-cluster: ['chalk stair verse', 'ninth bell paired clock register']
r93-m2-kojiki-cluster: ['m-17 margin register']

== PAIRWISE intersections (ids+names+titles) ==
r87-myth-cluster ∩ r88-m3-maya-cluster: EMPTY
r87-myth-cluster ∩ r93-m2-kojiki-cluster: EMPTY
r88-m3-maya-cluster ∩ r93-m2-kojiki-cluster: EMPTY

== THREE-WAY intersection: EMPTY ==

== L4: word tokens inside entity names+source titles (NOT referents; overlap audit) ==
r87-myth-cluster ∩ r88-m3-maya-cluster tokens: ['bell', 'register']
r87-myth-cluster ∩ r93-m2-kojiki-cluster tokens: ['register']
r88-m3-maya-cluster ∩ r93-m2-kojiki-cluster tokens: ['register']

== L5: markdown excerpt filenames + external-work mentions ==
r87-myth-cluster: files=['README.md', 'claim-excerpt-map.md', 'dune-register-excerpt.md', 'gate-witness-excerpt.md', 'inspiration-note.md', 'lowwater-hymn-excerpt.md', 'shell-charter-excerpt.md', 'symbolism-clause-map.md', 'tide-bell-tally-excerpt.md']
    external-mentions=['ETCSL', 'etcsl']
r88-m3-maya-cluster: files=['README.md', 'claim-excerpt-map.md', 'fictional-excerpts.md', 'inspiration-note.md', 'source-excerpt.md', 'symbolism-clause-map.md']
    external-mentions=["K'iche", 'Spence']
r93-m2-kojiki-cluster: files=['README.md', 'archive-record-excerpt.md', 'claim-excerpt-map.md', 'inspiration-note.md', 'kojiki-chamberlain-excerpt.md', 'symbolism-clause-map.md']
    external-mentions=['Chamberlain', 'Kojiki', 'chamberlain', 'kojiki']
r87-myth-cluster ∩ r88-m3-maya-cluster files: ['README.md', 'claim-excerpt-map.md', 'inspiration-note.md', 'symbolism-clause-map.md']; external works: EMPTY
r87-myth-cluster ∩ r93-m2-kojiki-cluster files: ['README.md', 'claim-excerpt-map.md', 'inspiration-note.md', 'symbolism-clause-map.md']; external works: EMPTY
r88-m3-maya-cluster ∩ r93-m2-kojiki-cluster files: ['README.md', 'claim-excerpt-map.md', 'inspiration-note.md', 'symbolism-clause-map.md']; external works: EMPTY

== L6: claim-map row labels (map-local labels, not corpus ids) ==
r87-myth-cluster: ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'R1', 'R2', 'R3', 'R4', 'T1', 'T2', 'T3', 'T4']
r88-m3-maya-cluster: ['E1', 'E2', 'E3', 'E4', 'P1', 'P2', 'P3', 'P4', 'S1', 'S2', 'T1', 'T2']
r93-m2-kojiki-cluster: ['E1', 'E10', 'E11', 'E12', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'S1', 'S2', 'S3']
r87-myth-cluster ∩ r88-m3-maya-cluster row-labels: ['E1', 'E2', 'E3', 'E4', 'T1', 'T2']  (expected non-empty; not referents)
r87-myth-cluster ∩ r93-m2-kojiki-cluster row-labels: ['E1', 'E2', 'E3', 'E4', 'E5', 'E6']  (expected non-empty; not referents)
r88-m3-maya-cluster ∩ r93-m2-kojiki-cluster row-labels: ['E1', 'E2', 'E3', 'E4', 'S1', 'S2']  (expected non-empty; not referents)
```

```
$ cat /tmp/jdep3/compare.py
import json, re, sys, pathlib
BASE = pathlib.Path("/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures")
CLUSTERS = ["r87-myth-cluster", "r88-m3-maya-cluster", "r93-m2-kojiki-cluster"]

def load(c, f):
    p = BASE/c/f
    return json.loads(p.read_text()) if p.exists() else None

def ids_from_json(obj, out, prefix=""):
    """Collect every id-bearing value."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in ("id","entity_id","place_id","source_id","first_appearance","event_id","from","to","depends_on","depends") and isinstance(v,(str,list)):
                vals = v if isinstance(v,list) else [v]
                for x in vals:
                    if isinstance(x,str): out.add(x)
            ids_from_json(v, out)
    elif isinstance(obj, list):
        for x in obj: ids_from_json(x, out)

levels = {}
names = {}
srctitles = {}
alljson = {}
for c in CLUSTERS:
    J = {}
    for f in ["entities.json","relations.json","timeline.json","sources.json","contradictions.json"]:
        J[f] = load(c, f)
        if J[f] is not None: alljson.setdefault(c,[]).append(f)
    ids = set()
    for f,d in J.items():
        if d is not None: ids_from_json(d, ids)
    levels[c] = ids
    names[c] = {e["name"].strip().lower() for e in (J["entities.json"] or [])}
    srctitles[c] = {s["title"].strip().lower() for s in (J["sources.json"] or [])}

print("== L1: all JSON id-bearing values per cluster ==")
for c in CLUSTERS:
    print(f"{c}: {len(levels[c])} ids")
    print("  ", sorted(levels[c]))

print("\n== L2: entity display names (lowercased) ==")
for c in CLUSTERS: print(f"{c}: {sorted(names[c])}")

print("\n== L3: source titles (lowercased) ==")
for c in CLUSTERS: print(f"{c}: {sorted(srctitles[c])}")

def inter(a,b): return sorted((levels[a]&levels[b]) | (names[a]&names[b]) | (srctitles[a]&srctitles[b]))

print("\n== PAIRWISE intersections (ids+names+titles) ==")
import itertools
for a,b in itertools.combinations(CLUSTERS,2):
    print(f"{a} ∩ {b}: {inter(a,b) or 'EMPTY'}")

three = (levels[CLUSTERS[0]]|names[CLUSTERS[0]]|srctitles[CLUSTERS[0]]) & (levels[CLUSTERS[1]]|names[CLUSTERS[1]]|srctitles[CLUSTERS[1]]) & (levels[CLUSTERS[2]]|names[CLUSTERS[2]]|srctitles[CLUSTERS[2]])
print(f"\n== THREE-WAY intersection: {sorted(three) or 'EMPTY'} ==")

# L4: generic proper-noun tokens in entity names (word-level overlap check, referent≠token)
def tokens(s): return {w for w in re.split(r"[^a-z0-9]+", s.lower()) if len(w)>2}
toksets = {c: set().union(*[tokens(n) for n in names[c]]) | set().union(*[tokens(t) for t in srctitles[c]]) for c in CLUSTERS}
print("\n== L4: word tokens inside entity names+source titles (NOT referents; overlap audit) ==")
for a,b in itertools.combinations(CLUSTERS,2):
    print(f"{a} ∩ {b} tokens: {sorted(toksets[a]&toksets[b]) or 'EMPTY'}")

# L5: markdown referents — excerpt filenames + external source works
mdrefs = {}
for c in CLUSTERS:
    d = BASE/c
    fs = {p.name for p in d.glob("*.md")}
    txt = "\n".join(p.read_text() for p in d.glob("*.md"))
    ext = set(re.findall(r"(?i)(ETCSL|Spence|Kojiki|Chamberlain|K'iche|Dresden)", txt))
    mdrefs[c] = (fs, ext)
print("\n== L5: markdown excerpt filenames + external-work mentions ==")
for c in CLUSTERS: print(f"{c}: files={sorted(mdrefs[c][0])}\n    external-mentions={sorted(mdrefs[c][1])}")
for a,b in itertools.combinations(CLUSTERS,2):
    print(f"{a} ∩ {b} files: {sorted(mdrefs[a][0]&mdrefs[b][0]) or 'EMPTY'}; external works: {sorted(mdrefs[a][1]&mdrefs[b][1]) or 'EMPTY'}")

# L6: claim-excerpt-map row labels (map-local, namespace-isolated by design)
rowlabels = {}
for c in CLUSTERS:
    t = (BASE/c/"claim-excerpt-map.md").read_text()
    rowlabels[c] = set(re.findall(r"^\| ([A-Z]+\d+) \|", t, re.M))
print("\n== L6: claim-map row labels (map-local labels, not corpus ids) ==")
for c in CLUSTERS: print(f"{c}: {sorted(rowlabels[c])}")
for a,b in itertools.combinations(CLUSTERS,2):
    print(f"{a} ∩ {b} row-labels: {sorted(rowlabels[a]&rowlabels[b]) or 'EMPTY'}  (expected non-empty; not referents)")
```
