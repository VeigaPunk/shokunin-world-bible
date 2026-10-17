#!/usr/bin/env python3
"""F14 independent R10 semantic-namespace judge scan (round 93, DeepSeek follow-up).

Read-only. Compares the delivered M-17 cluster (corpus/fixtures/r93-m2-kojiki-cluster)
against the two landed clusters (r87-myth-cluster, r88-m3-maya-cluster) over
referents, claims, fields, and occasions. Stdlib only.

Independent of R10-key-scan.py: this script re-derives its own normalization,
adds token-level claim/occasion n-gram overlap, prose proper-noun mention sweeps,
JSON field-name/value inventories, and bootstrap checks for the R10 record's
supersession of the M6 wrong-candidate note and the absent contradiction register.
"""

import hashlib
import json
import re
import subprocess
import unicodedata
from pathlib import Path

ROOT = Path("corpus/fixtures")
NAMES = ("r93-m2-kojiki-cluster", "r87-myth-cluster", "r88-m3-maya-cluster")
M2 = NAMES[0]
PRIORS = NAMES[1:]

WORD_RE = re.compile(r"[^\W_]+", re.UNICODE)
PROPER_RE = re.compile(r"\b[A-Z][a-z]{2,}\b")

PRIOR_EXTERNAL_PARALLELS = {
    "r87-myth-cluster": "ETCSL Inana's descent (Sumerian) — external-only",
    "r88-m3-maya-cluster": "Spence 1913 Kiche/Maya passage — delivered external",
}


def norm(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).casefold()
    return "".join(ch for ch in value if not unicodedata.combining(ch) and ch.isalnum())


def toks(value: str):
    value = unicodedata.normalize("NFKD", value).casefold()
    cleaned = "".join(ch if (ch.isalnum() or ch.isspace()) else " " for ch in value
                      if not unicodedata.combining(ch))
    return [t for t in cleaned.split() if t]


def file_sha(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def tree_sha(root: Path, exclude=()):
    h = hashlib.sha256()
    for p in sorted(root.rglob("*")):
        if p.is_file() and p.name not in exclude:
            h.update(p.relative_to(root).as_posix().encode("utf-8"))
            h.update(b"\0")
            h.update(p.read_bytes())
    return h.hexdigest()


def read_json(root: Path, name: str):
    return json.loads((root / name).read_text(encoding="utf-8"))


def field_paths(value, path="$"):
    out = []
    if isinstance(value, dict):
        for key, child in value.items():
            out.append(f"{path}.{key}")
            out.extend(field_paths(child, f"{path}.{key}"))
    elif isinstance(value, list):
        for i, child in enumerate(value):
            out.extend(field_paths(child, f"{path}[{i}]"))
    return out


def scalar_pairs(value, path="$"):
    out = []
    if isinstance(value, dict):
        for key, child in value.items():
            out.extend(scalar_pairs(child, f"{path}.{key}"))
    elif isinstance(value, list):
        for i, child in enumerate(value):
            out.extend(scalar_pairs(child, f"{path}[{i}]"))
    else:
        out.append((path, value))
    return out


def inventory(name: str):
    root = ROOT / name
    entities = read_json(root, "entities.json")
    sources = read_json(root, "sources.json")
    timeline = read_json(root, "timeline.json")
    relations = read_json(root, "relations.json")
    contradictions = read_json(root, "contradictions.json")

    json_fields, json_values = set(), []
    for path in sorted(root.glob("*.json")):
        doc = json.loads(path.read_text(encoding="utf-8"))
        json_fields.update(field_paths(doc))
        json_values.extend((p, v) for p, v in scalar_pairs(doc))

    aliases = [
        {"entity": e["id"], "field": key, "value": e[key]}
        for e in entities
        for key in ("aliases", "epithets", "alias", "epithet")
        if key in e
    ]

    claims = []
    for e in entities:
        for i, c in enumerate(e.get("claims", [])):
            claims.append({"pointer": f"entities.json#{e['id']}/claims/{i}",
                           "statement": c["statement"], "source_id": c["source_id"]})
    for i, r in enumerate(relations):
        claims.append({"pointer": f"relations.json#{i}",
                       "statement": f"{r['from']} {r['type']} {r['to']}", "source_id": r["source_id"]})
    for i, ev in enumerate(timeline):
        claims.append({"pointer": f"timeline.json#{i}", "statement": ev["description"],
                       "source_id": ev["source_id"]})

    events = [
        {"id": ev["id"], "tick": ev["tick"], "entity_id": ev["entity_id"], "place_id": ev["place_id"],
         "depends_on": ev["depends_on"], "description": ev["description"], "source_id": ev["source_id"]}
        for ev in timeline
    ]

    md_text = {}
    for p in sorted(root.glob("*.md")):
        md_text[p.name] = p.read_text(encoding="utf-8")

    proper = {}
    for fname, text in md_text.items():
        found = sorted(set(PROPER_RE.findall(text)))
        if found:
            proper[fname] = found

    return {
        "name": name,
        "dir_full_tree_sha256": tree_sha(root),
        "dir_excl_readme_sha256": tree_sha(root, exclude=("README.md",)),
        "file_sha256": {p.name: file_sha(p) for p in sorted(root.rglob("*")) if p.is_file()},
        "referents": [
            {"id": e["id"], "kind": e["kind"], "name": e["name"],
             "first_appearance": e.get("first_appearance")}
            for e in entities
        ],
        "alias_epithet_fields": aliases,
        "claims": claims,
        "sources": sources,
        "events": events,
        "relations": relations,
        "contradictions": contradictions,
        "json_field_names": sorted(json_fields),
        "normalized": {
            "entity_ids": sorted({norm(e["id"]) for e in entities}),
            "entity_labels": sorted({norm(v) for e in entities
                                     for v in [e["name"], *e.get("aliases", []), *e.get("epithets", [])]}),
            "entity_kinds": sorted({norm(e["kind"]) for e in entities}),
            "claim_statements": sorted({norm(c["statement"]) for c in claims}),
            "source_ids_bare": sorted({norm(s["id"]) for s in sources}),
            "source_titles": sorted({norm(s["title"]) for s in sources}),
            "source_kinds": sorted({norm(s["kind"]) for s in sources}),
            "source_ids_path_qualified": sorted(f"{name}:{norm(s['id'])}" for s in sources),
            "event_ids": sorted({norm(e["id"]) for e in events}),
            "event_descriptions": sorted({norm(e["description"]) for e in events}),
            "event_endpoints": sorted({norm(v) for e in events for v in (e["entity_id"], e["place_id"])}),
            "event_dependencies": sorted({norm(d) for e in events for d in e["depends_on"]}),
            "relation_endpoints": sorted({norm(v) for r in relations for v in (r["from"], r["to"])}),
            "relation_types": sorted({norm(r["type"]) for r in relations}),
            "relation_tuples": sorted({(norm(r["from"]), norm(r["type"]), norm(r["to"]), f"{name}:{norm(r['source_id'])}")
                                       for r in relations}),
        },
        "claim_tokens": {c["pointer"]: toks(c["statement"]) for c in claims},
        "event_tokens": {e["id"]: toks(e["description"]) for e in events},
        "proper_nouns_by_file": proper,
        "proper_noun_set": sorted({t for found in proper.values() for t in found}),
    }


def ngram_overlap(a_tokens, b_tokens, n):
    def grams(tokens):
        return {" ".join(tokens[i:i + n]) for i in range(len(tokens) - n + 1)}
    return sorted(grams(a_tokens) & grams(b_tokens))


def main():
    inv = {name: inventory(name) for name in NAMES}
    m2 = inv[M2]

    result = {
        "measured_head": subprocess.run(["git", "rev-parse", "HEAD"], check=True,
                                        capture_output=True, text=True).stdout.strip(),
        "measured_tree": subprocess.run(["git", "rev-parse", "HEAD^{tree}"], check=True,
                                        capture_output=True, text=True).stdout.strip(),
        "normalization": "NFKD -> casefold -> drop combining marks -> keep alphanumeric; "
                         "tokens additionally split on any non-alphanumeric/non-space",
        "fixtures": inv,
        "comparisons": {},
        "bootstrap_checks": {},
    }

    for prior in PRIORS:
        p = inv[prior]
        a, b = m2["normalized"], p["normalized"]
        keys = {}
        for label, k1, k2 in [
            ("entity_id_id", "entity_ids", "entity_ids"),
            ("entity_label_label", "entity_labels", "entity_labels"),
            ("event_id_id", "event_ids", "event_ids"),
            ("source_id_bare", "source_ids_bare", "source_ids_bare"),
            ("source_id_path_qualified", "source_ids_path_qualified", "source_ids_path_qualified"),
            ("source_title_title", "source_titles", "source_titles"),
            ("claim_statement_exact", "claim_statements", "claim_statements"),
            ("event_description_exact", "event_descriptions", "event_descriptions"),
            ("relation_type_type", "relation_types", "relation_types"),
            ("source_kind_kind", "source_kinds", "source_kinds"),
            ("entity_kind_kind", "entity_kinds", "entity_kinds"),
        ]:
            keys[label] = sorted(set(a[k1]) & set(b[k2]))
        keys["entity_id_label_either"] = sorted((set(a["entity_ids"]) & set(b["entity_labels"]))
                                                | (set(b["entity_ids"]) & set(a["entity_labels"])))
        keys["m2_endpoint_to_prior_entity_key"] = sorted(
            (set(a["relation_endpoints"]) | set(a["event_endpoints"])) & (set(b["entity_ids"]) | set(b["entity_labels"])))
        keys["prior_endpoint_to_m2_entity_key"] = sorted(
            (set(b["relation_endpoints"]) | set(b["event_endpoints"])) & (set(a["entity_ids"]) | set(a["entity_labels"])))
        keys["m2_dependency_to_prior_event_id"] = sorted(set(a["event_dependencies"]) & set(b["event_ids"]))
        keys["prior_dependency_to_m2_event_id"] = sorted(set(b["event_dependencies"]) & set(a["event_ids"]))
        keys["m2_event_id_to_prior_entity_key"] = sorted(set(a["event_ids"]) & (set(b["entity_ids"]) | set(b["entity_labels"])))
        keys["prior_event_id_to_m2_entity_key"] = sorted(set(b["event_ids"]) & (set(a["entity_ids"]) | set(a["entity_labels"])))

        # Token-level claim/description reuse: n-gram overlaps >= 3 tokens.
        overlaps = []
        for n in (3, 4, 5):
            for m2_ptr, m2_toks in list(m2["claim_tokens"].items()) + list(m2["event_tokens"].items()):
                for p_ptr, p_toks in list(p["claim_tokens"].items()) + list(p["event_tokens"].items()):
                    shared = ngram_overlap(m2_toks, p_toks, n)
                    if shared:
                        overlaps.append({"n": n, "m2": m2_ptr, "prior": p_ptr, "shared": shared})
        # Cross-direction: do prior files mention M2's referent display names, and vice versa?
        m2_names = {e["name"] for e in m2["referents"]}
        prior_names = {e["name"] for e in p["referents"]}
        m2_text = "\n".join(v for v in m2["file_sha256"])  # placeholder, replaced below
        m2_all = "\n".join((ROOT / M2 / f).read_text(encoding="utf-8") for f in m2["file_sha256"])
        prior_all = "\n".join((ROOT / prior / f).read_text(encoding="utf-8") for f in p["file_sha256"])
        m2_mentions = {n: len(re.findall(r"\b" + re.escape(n) + r"\b", m2_all)) for n in sorted(prior_names)
                       if re.search(r"\b" + re.escape(n) + r"\b", m2_all)}
        prior_mentions = {n: len(re.findall(r"\b" + re.escape(n) + r"\b", prior_all)) for n in sorted(m2_names)
                          if re.search(r"\b" + re.escape(n) + r"\b", prior_all)}
        reed_ctx = [f"{M2}:{ln.strip()}" for ln in m2_all.splitlines() if re.search(r"\breed", ln, re.I)]
        # Prose proper-noun intersection
        proper_shared = sorted(set(m2["proper_noun_set"]) & set(p["proper_noun_set"]))

        result["comparisons"][prior] = {
            "prior_external_parallel": PRIOR_EXTERNAL_PARALLELS[prior],
            "key_intersections": keys,
            "token_ngram_overlaps_ge3": overlaps,
            "prior_display_names_mentioned_in_m2_files": m2_mentions,
            "m2_display_names_mentioned_in_prior_files": prior_mentions,
            "m2_reed_token_lines": reed_ctx,
            "shared_prose_proper_nouns": proper_shared,
        }

    # Dead-bearing checks (bootstrap).
    repo = Path(".")
    registered = repo / "corpus/knowledge/cross-cluster-contradictions.md"
    demo = repo / "corpus/knowledge/r89-cross-cluster-contradiction.md"
    m6_receipt = json.loads((repo / ".ufo/waves/round-93/patches/M6-namespace.json").read_text(encoding="utf-8"))
    readme = (ROOT / M2 / "README.md").read_text(encoding="utf-8")
    superseded = ("M6's current report reviews M1's distinct `r93-myth-cluster3` candidate, not this M-17 cluster; "
                  "an independent M2-specific scan and semantic review remain pending before any integrated "
                  "zero-referent conclusion.")
    result["bootstrap_checks"] = {
        "register_absent": not registered.exists(),
        "r89_demo_present_but_disclaims_register": demo.exists() and "not an integration-ready register entry" in demo.read_text(encoding="utf-8"),
        "m6_receipt_cluster_path": m6_receipt.get("candidate", {}).get("cluster_path"),
        "m6_target_absent_from_repo": not (ROOT / "r93-myth-cluster3").exists(),
        "delivered_cluster_is_not_m6_target": (ROOT / M2).is_dir() and m6_receipt.get("candidate", {}).get("cluster_path") != f"corpus/fixtures/{M2}",
        "superseded_sentence_verbatim_in_readme": superseded in readme,
        "supersession_claim_present": "This entry supersedes the pending-review sentence above" in readme,
        "m2_contradictions_empty": m2["contradictions"] == [],
        "m2_files_reference_prior_cluster_paths": sorted(
            {other for other in NAMES if other != M2 and other in m2_all}),
        "m2_files_mention_register_path": "cross-cluster-contradictions" in m2_all,
    }
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
