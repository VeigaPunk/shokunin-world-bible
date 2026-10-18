#!/usr/bin/env python3
"""V48 scratch mutations for dependency_freeze demos. Operates only on
copies under V48-scratch/mutations/. Never touches corpus/."""
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent / "mutations"


def load(p):
    return json.loads(p.read_text())


def save(p, obj):
    p.write_text(json.dumps(obj, indent=2) + "\n")


def reduction(dirname):
    p = BASE / dirname / "timeline.json"
    tl = load(p)
    for ev in tl:
        if ev["id"] == "paired-crossing-decision":
            ev["depends_on"] = [d for d in ev["depends_on"] if d != "evin-ninth-bell"]
    save(p, tl)
    print(f"{dirname}: removed evin-ninth-bell from paired-crossing-decision.depends_on")


def addition(dirname):
    p = BASE / dirname / "timeline.json"
    tl = load(p)
    for ev in tl:
        if ev["id"] == "aru-ninth-bell":
            ev["depends_on"] = ["evin-ninth-bell"]
        if ev["id"] == "aftermath-missing-evin":
            ev["depends_on"] = sorted(set(ev["depends_on"] + ["evin-ninth-bell"]))
    save(p, tl)
    print(f"{dirname}: added evin-ninth-bell edge(s)")


def endpoint_swap(dirname):
    p = BASE / dirname / "relations.json"
    rel = load(p)
    rel[0]["from"], rel[0]["to"] = rel[0]["to"], rel[0]["from"]
    save(p, rel)
    print(f"{dirname}: swapped relation endpoints -> {rel[0]['from']}->{rel[0]['to']}")


def tamper_text(dirname):
    p = BASE / dirname / "timeline.json"
    tl = load(p)
    for ev in tl:
        if ev["id"] == "aru-ninth-bell":
            ev["description"] += " [tampered text, edges unchanged]"
    save(p, tl)
    print(f"{dirname}: text-only tamper on aru-ninth-bell.description")


if __name__ == "__main__":
    reduction("r94-reduction")
    reduction("r95-reduction")
    addition("r94-add")
    addition("r95-add")
    endpoint_swap("r96-endpoint")
    tamper_text("r94-tamper-text")
    print("mutations applied")
