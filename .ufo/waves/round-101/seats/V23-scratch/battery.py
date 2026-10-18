#!/usr/bin/env python3
"""V23 full ADJACENCY battery for round-101 (runs only after poll READY).

Sections: charter/byte-ownership, full census, frozen chain, live gates,
self-tests (mirrors), negative/boundary controls, contract comparison,
ordering, new-bytes refusal scan. Every CLI invocation is recorded with
argv, cwd, exit code, stdout, stderr into battery-results.json and a
readable battery-transcript.txt. Summary in battery-summary.json.
"""
import hashlib, json, os, re, shutil, subprocess, sys, time
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCRATCH = LANE / ".ufo/waves/round-101/seats/V23-scratch"
TMP = SCRATCH / "tmp"
MIRRORS = SCRATCH / "mirrors"
SEATS = LANE / ".ufo/waves/round-101/seats"
BASE = "6f86bf2"
results = []
summary = {"sections": {}, "started": time.strftime("%FT%T")}

# pre-wave hashes captured at 00:05 -03:00 before any producer byte landed
PRE = {
    "PROVINCE.md": "94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa",
    "SHONEN.md": "03b832c75efbf81300e87f6a95713a48b21b00d654c1222aee251a27c103d7d1",
    "README.md": "ad4adb1e6cfbec41c83281aa7dfe1439d453ab5cb4290a9d8c25c1a1b06c2caf",
    "l0-questions.md": "93105c95247bb80e6f2c4df0fca7f8cc31b271ca3f1777aa69302a9ea8d0cfdf",
}


def sh(*argv, cwd=LANE, env=None, record=True, timeout=300):
    r = subprocess.run([str(a) for a in argv], cwd=str(cwd), capture_output=True,
                       text=True, timeout=timeout,
                       env={**os.environ, **(env or {})})
    if record:
        results.append({"argv": [str(a) for a in argv], "cwd": str(cwd),
                        "exit": r.returncode, "stdout": r.stdout,
                        "stderr": r.stderr})
    return r


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def section(name):
    print(f"== {name} ==", flush=True)
    summary["sections"][name] = {"obs": {}}


def note(name, key, value):
    summary["sections"][name]["obs"][key] = value


def mirror_repo(name, tools=True, contract=True, fixtures="all", extra_fixtures=()):
    root = MIRRORS / name
    if root.exists():
        shutil.rmtree(root)
    (root / "corpus/tools").mkdir(parents=True)
    if tools:
        for p in sorted((LANE / "corpus/tools").iterdir()):
            if p.suffix in (".py", ".json"):
                shutil.copy2(p, root / "corpus/tools" / p.name)
    if fixtures == "all":
        shutil.copytree(LANE / "corpus/fixtures", root / "corpus/fixtures")
    elif isinstance(fixtures, str):
        shutil.copytree(LANE / "corpus/fixtures" / fixtures,
                        root / "corpus/fixtures" / fixtures)
    for fx in extra_fixtures:
        dst = root / "corpus/fixtures" / fx
        if not dst.exists():
            shutil.copytree(LANE / "corpus/fixtures" / fx, dst)
    return root


def main():
    TMP.mkdir(parents=True, exist_ok=True)
    MIRRORS.mkdir(parents=True, exist_ok=True)

    # ---------- A. charter & byte-ownership ----------
    section("charter")
    bad = []
    for rel, want in PRE.items():
        got = sha256(LANE / rel)
        note("charter", rel, got)
        if got != want:
            bad.append(rel)
    note("charter", "charter_changed", bad)
    r = sh("git", "diff", "--numstat", BASE)
    note("charter", "numstat_vs_base", r.stdout.strip())
    r = sh("git", "status", "--short")
    note("charter", "git_status", r.stdout.strip())
    r = sh("git", "diff", "--name-only", "HEAD")
    note("charter", "worktree_changed_vs_HEAD", r.stdout.strip())
    r = sh("git", "diff", "--check")
    note("charter", "diff_check", (r.stdout + r.stderr).strip() or "(clean)")
    r = sh("git", "ls-files", "--others", "--exclude-standard")
    untracked = [l for l in r.stdout.splitlines()
                 if not l.startswith(".ufo/") and not l.startswith(".scratch")]
    note("charter", "untracked_non_ufo_scratch", untracked)
    # committed vs worktree LOG/SCORECARD equality (no wave writes to them)
    r = sh("git", "diff", "--name-only", "HEAD", "--", "LOG.md", "SCORECARD.md")
    note("charter", "log_scorecard_wave_writes", r.stdout.strip() or "(none)")

    # ownership diffs saved for inspection
    for rel in ("SKILL.md", "corpus/tools/README.md",
                "corpus/tools/dependency_freeze.py",
                "corpus/tools/dependency-freeze-contract.json"):
        r = sh("git", "diff", BASE, "--", rel, record=False)
        (SCRATCH / f"diff-{rel.replace('/', '__')}.patch").write_text(r.stdout)

    # ---------- B. census ----------
    section("census")
    fixtures_root = LANE / "corpus/fixtures"
    dirs = sorted(p.name for p in fixtures_root.iterdir() if p.is_dir())
    clean, negative, other = [], [], []
    for d in dirs:
        r = sh("python3", "corpus/fixtures/check_bible.py", f"corpus/fixtures/{d}")
        (clean if r.returncode == 0 else negative if r.returncode == 1 else other).append(d)
    violations = 0
    for step in results[-len(dirs):]:
        violations += step["stdout"].count("VIOLATION")
    note("census", "fixture_dirs", len(dirs))
    note("census", "clean", len(clean))
    note("census", "negative", len(negative))
    note("census", "other", other)
    note("census", "violation_lines", violations)

    # ---------- C. frozen chain ----------
    section("chain")
    contract = json.loads((LANE / "corpus/tools/dependency-freeze-contract.json").read_text())
    base_contract = json.loads(subprocess.run(
        ["git", "show", f"{BASE}:corpus/tools/dependency-freeze-contract.json"],
        cwd=LANE, capture_output=True, text=True).stdout)
    pins = sorted(contract["pins"])
    note("chain", "pins_delivered", pins)
    note("chain", "pins_baseline", sorted(base_contract["pins"]))
    note("chain", "revision", (base_contract["revision"], contract["revision"]))
    added = set(contract["pins"]) - set(base_contract["pins"])
    removed = set(base_contract["pins"]) - set(contract["pins"])
    changed = {n for n in set(contract["pins"]) & set(base_contract["pins"])
               if contract["pins"][n] != base_contract["pins"][n]}
    note("chain", "pins_added", sorted(added))
    note("chain", "pins_removed", sorted(removed))
    note("chain", "prior_pins_changed", sorted(changed))
    for name in pins:
        rel = contract["pins"][name]["fixture"]
        r = sh("python3", "corpus/tools/dependency_freeze.py", rel)
        note("chain", f"verify:{name}", r.returncode)

    # ---------- D. live gates on key fixtures ----------
    section("live_gates")
    for fx in ("r100-docket-review", "r94-paired-crossing", "r99-window-lapse"):
        for tool in ("corpus/fixtures/check_bible.py", "corpus/tools/map_obligations.py",
                     "corpus/tools/support_check.py"):
            r = sh("python3", tool, f"corpus/fixtures/{fx}")
            note("live_gates", f"{tool.split('/')[-1]}:{fx}", r.returncode)

    # ---------- E. self-tests on mirrors ----------
    section("self_tests")
    freeze_mirror = mirror_repo("freeze-self-test", tools=False, fixtures=None,
                                extra_fixtures=("r95-crossing-aftermath",))
    shutil.copy2(LANE / "corpus/tools/dependency_freeze.py",
                 freeze_mirror / "corpus/tools/dependency_freeze.py")
    shutil.copy2(LANE / "corpus/tools/dependency-freeze-contract.json",
                 freeze_mirror / "corpus/tools/dependency-freeze-contract.json")
    r = sh("python3", freeze_mirror / "corpus/tools/dependency_freeze.py",
           "--self-test", cwd=freeze_mirror)
    note("self_tests", "freeze_self_test", r.returncode)
    m = re.search(r"SELF-TEST (\d+)/(\d+)", r.stdout)
    note("self_tests", "freeze_score", m.group(0) if m else "?")
    # mirror tool/contract identity vs live bytes
    note("self_tests", "mirror_tool_identity",
         sha256(freeze_mirror / "corpus/tools/dependency_freeze.py") ==
         sha256(LANE / "corpus/tools/dependency_freeze.py"))
    note("self_tests", "mirror_contract_identity",
         sha256(freeze_mirror / "corpus/tools/dependency-freeze-contract.json") ==
         sha256(LANE / "corpus/tools/dependency-freeze-contract.json"))

    map_mirror = mirror_repo("map-self-test")
    r = sh("python3", map_mirror / "corpus/tools/map_obligations.py",
           "--self-test", cwd=map_mirror)
    note("self_tests", "map_self_test", r.returncode)
    m = re.search(r"SELF-TEST (\d+)/(\d+)", r.stdout)
    note("self_tests", "map_score", m.group(0) if m else "?")

    r = sh("python3", "corpus/tools/boundary_doc_check.py",
           env={"TMPDIR": str(TMP)})
    note("self_tests", "boundary_doc_check", r.returncode)
    r = sh("python3", "corpus/tools/boundary_doc_check.py", "--self-test",
           env={"TMPDIR": str(TMP)})
    note("self_tests", "boundary_doc_self_test", r.returncode)
    r = sh("python3", "corpus/tools/discriminate_check.py")
    note("self_tests", "discriminate_delivered", r.returncode)
    r = sh("python3", "corpus/tools/discriminate_check.py", "--checker", "e97613c")
    note("self_tests", "discriminate_regression_control", r.returncode)
    r = sh("python3", "corpus/tools/map_obligations.py", "--frozen",
           ".ufo/waves/round-94/frozen/map-obligations-r93")
    note("self_tests", "frozen_map_replay_r93", r.returncode)

    # ---------- F. negative / boundary controls ----------
    section("controls")
    # clean r99 mirror
    root = mirror_repo("ctl-clean", tools=False, fixtures="r99-window-lapse")
    shutil.copy2(LANE / "corpus/tools/dependency_freeze.py", root / "corpus/tools/dependency_freeze.py")
    shutil.copy2(LANE / "corpus/tools/dependency-freeze-contract.json",
                 root / "corpus/tools/dependency-freeze-contract.json")
    r = sh("python3", root / "corpus/tools/dependency_freeze.py",
           root / "corpus/fixtures/r99-window-lapse", cwd=root)
    note("controls", "clean_r99_mirror", r.returncode)
    # repointed edge (row-2 class) on mirror
    root = mirror_repo("ctl-repoint", tools=False, fixtures="r99-window-lapse")
    shutil.copy2(LANE / "corpus/tools/dependency_freeze.py", root / "corpus/tools/dependency_freeze.py")
    shutil.copy2(LANE / "corpus/tools/dependency-freeze-contract.json",
                 root / "corpus/tools/dependency-freeze-contract.json")
    tl_path = root / "corpus/fixtures/r99-window-lapse/timeline.json"
    tl = json.loads(tl_path.read_text())
    for rec in tl:
        if rec.get("id") == "clerk-lapse-recorded":
            rec["depends_on"] = ["acknowledgment-aru-records" if d == "clerk-filing-open" else d
                                 for d in rec.get("depends_on", [])]
    tl_path.write_text(json.dumps(tl, indent=2) + "\n")
    r = sh("python3", root / "corpus/tools/dependency_freeze.py",
           root / "corpus/fixtures/r99-window-lapse", cwd=root)
    note("controls", "repointed_r99", r.returncode)
    note("controls", "repointed_findings",
         sorted(l.split(":", 1)[0].split(" ", 1)[1] for l in r.stdout.splitlines()
                if l.startswith("FINDING ")))
    r = sh("python3", "corpus/fixtures/check_bible.py",
           root / "corpus/fixtures/r99-window-lapse")
    note("controls", "repointed_bible", r.returncode)
    # digest newline tamper on mirror
    root = mirror_repo("ctl-digest", tools=False, fixtures="r99-window-lapse")
    shutil.copy2(LANE / "corpus/tools/dependency_freeze.py", root / "corpus/tools/dependency_freeze.py")
    shutil.copy2(LANE / "corpus/tools/dependency-freeze-contract.json",
                 root / "corpus/tools/dependency-freeze-contract.json")
    ex = root / "corpus/fixtures/r99-window-lapse/fictional-excerpts.md"
    ex.write_bytes(ex.read_bytes() + b"\n")
    r = sh("python3", root / "corpus/tools/dependency_freeze.py",
           root / "corpus/fixtures/r99-window-lapse", cwd=root)
    note("controls", "newline_digest", r.returncode)
    # invalid combined args (live)
    r = sh("python3", "corpus/tools/dependency_freeze.py",
           "corpus/fixtures/r99-window-lapse", "--freeze",
           "corpus/fixtures/r99-window-lapse")
    note("controls", "invalid_combined", r.returncode)
    # scope-refused freeze outside corpus/fixtures + contract untouched
    before = sha256(LANE / "corpus/tools/dependency-freeze-contract.json")
    r = sh("python3", "corpus/tools/dependency_freeze.py", "--freeze", TMP)
    note("controls", "scope_refused", r.returncode)
    note("controls", "contract_unchanged_after_scope_refusal",
         sha256(LANE / "corpus/tools/dependency-freeze-contract.json") == before)
    # foreign same-named copy (live tool, scratch path)
    foreign = TMP / "foreign-r99"
    shutil.copytree(LANE / "corpus/fixtures/r99-window-lapse", foreign)
    r = sh("python3", "corpus/tools/dependency_freeze.py", foreign)
    note("controls", "foreign_path", r.returncode)
    # unpinned fixture (live)
    r = sh("python3", "corpus/tools/dependency_freeze.py",
           "corpus/fixtures/r87-myth-cluster")
    note("controls", "unpinned_live", r.returncode)

    # ---------- G. C2 record spot-checks ----------
    section("c2_checks")
    arc = ["r94-paired-crossing", "r95-crossing-aftermath", "r96-crossing-response",
           "r97-crossing-acknowledgment", "r98-clerk-filing", "r99-window-lapse",
           "r100-docket-review"]
    rel_hashes = set()
    for fx in arc:
        b = (LANE / "corpus/fixtures" / fx / "relations.json").read_bytes()
        rel_hashes.add((hashlib.sha256(b).hexdigest(), len(b)))
    note("c2_checks", "relation_identity", sorted(rel_hashes))
    r95 = LANE / "corpus/fixtures/r95-crossing-aftermath"
    r96 = LANE / "corpus/fixtures/r96-crossing-response"
    tl95 = json.loads((r95 / "timeline.json").read_text())
    tl96 = json.loads((r96 / "timeline.json").read_text())
    e_a = tl95[3]
    e_b = tl96[4]
    note("c2_checks", "claim_A", e_a)
    note("c2_checks", "claim_B", e_b)
    note("c2_checks", "claim_A_expected",
         e_a.get("id") == "aftermath-missing-evin" and e_a.get("tick") == 11
         and e_a.get("place_id") == "chalk-stair"
         and e_a.get("depends_on") == ["paired-crossing-decision"]
         and e_a.get("source_id") == "aru-aftermath-note")
    note("c2_checks", "claim_B_expected",
         e_b.get("id") == "response-evin-salt-court" and e_b.get("tick") == 12
         and e_b.get("place_id") == "salt-court"
         and e_b.get("depends_on") == ["aftermath-missing-evin"]
         and e_b.get("source_id") == "evin-response-note")
    b94 = (LANE / "corpus/fixtures/r94-paired-crossing/fictional-excerpts.md").read_bytes()
    b95x = (r95 / "fictional-excerpts.md").read_bytes()
    b96x = (r96 / "fictional-excerpts.md").read_bytes()
    note("c2_checks", "prefix_chain", (b95x.startswith(b94), b96x.startswith(b95x)))
    note("c2_checks", "contradictions_empty",
         (json.loads((r95 / "contradictions.json").read_text()) == [],
          json.loads((r96 / "contradictions.json").read_text()) == []))
    note("c2_checks", "register_absent",
         not (LANE / "corpus/knowledge/cross-cluster-contradictions.md").exists())
    note("c2_checks", "register_absent_at_baseline",
         subprocess.run(["git", "ls-tree", BASE, "--name-only", "-r"],
                        cwd=LANE, capture_output=True, text=True
                        ).stdout.count("cross-cluster-contradictions") == 0)
    quotes = {
        "r95_evins_absence": b"Evin did not come." in b95x,
        "r95_crossing_scope": b"The agreement we chalked covered this crossing only." in b95x,
        "r96_salt_court": b"I was at Salt Court through the same agreed bell." in b96x,
        "r96_no_winner": b"I select no winner between our two accounts." in b96x,
        "r94_minute_scope": b"to share stewardship of the Chalk Stair" in b94,
    }
    note("c2_checks", "quoted_lines_present", quotes)
    note("c2_checks", "blind_spot_table_untouched",
         "corpus/knowledge/r99-gate-blind-spot-table.md" not in
         subprocess.run(["git", "diff", "--name-only", BASE], cwd=LANE,
                        capture_output=True, text=True).stdout)

    # ---------- H. ordering ----------
    section("ordering")
    artifacts = ["corpus/tools/dependency_freeze.py",
                 "corpus/tools/dependency-freeze-contract.json",
                 "corpus/tools/README.md", "SKILL.md",
                 "corpus/knowledge/r101-r10-register-first-entry.md"]
    import glob as _glob
    reps = sorted(_glob.glob(str(SEATS / "U[12]-*.md")))
    obs = {}
    for a in artifacts:
        p = LANE / a
        obs[a] = p.stat().st_mtime if p.exists() else None
    for rp in reps:
        obs[os.path.basename(rp)] = os.path.getsize(rp) and os.path.getmtime(rp)
    art_mtimes = [v for k, v in obs.items() if k in artifacts and v]
    rep_mtimes = [v for k, v in obs.items() if k not in artifacts and v]
    ok_order = bool(art_mtimes) and bool(rep_mtimes) and max(art_mtimes) <= min(rep_mtimes)
    note("ordering", "artifacts<=reports", ok_order)
    note("ordering", "detail", {k: (time.strftime("%FT%T", time.localtime(v)) if v else None)
                                for k, v in obs.items()})

    # ---------- H. new-bytes refusal scan ----------
    section("refusals")
    blob = []
    for rel in ("SKILL.md", "corpus/tools/README.md",
                "corpus/tools/dependency_freeze.py",
                "corpus/tools/dependency-freeze-contract.json"):
        r = subprocess.run(["git", "diff", BASE, "--", rel], cwd=LANE,
                           capture_output=True, text=True)
        blob.append(r.stdout)
    newk = LANE / "corpus/knowledge/r101-r10-register-first-entry.md"
    if newk.exists():
        blob.append(newk.read_text())
    text = "\n".join(blob)
    (SCRATCH / "round-new-bytes.txt").write_text(text)
    patterns = {
        "mechanics": r"(?i)\b(mechanics?|gameplay|ruleset|damage|stats|balancing|combat|dice|hit[ -]?points?)\b",
        "rights": r"(?i)public domain|fair use|free to (use|reuse)|permission is granted|licensed under|all rights reserved",
        "network_or_paths": r"https?://|/home/[a-z]+/(?!Projects/shokunin/lore-shokunin)",
    }
    for label, pat in patterns.items():
        matches = re.findall(pat, text)
        note("refusals", label, matches)
    canon_ctx = [text[max(0, m.start() - 60):m.start() + 80].replace("\n", " ")
                 for m in re.finditer(r"(?i)\bcanon\b", text)]
    note("refusals", "canon_mentions", canon_ctx)

    # ---------- persist ----------
    with open(SCRATCH / "battery-results.json", "w") as f:
        json.dump(results, f, indent=1)
    with open(SCRATCH / "battery-summary.json", "w") as f:
        json.dump(summary, f, indent=1)
    with open(SCRATCH / "battery-transcript.txt", "w") as f:
        for s in results:
            f.write(f"$ (cwd={s['cwd']}) {' '.join(s['argv'])}\n")
            f.write(f"exit={s['exit']}\n")
            if s["stdout"]:
                f.write(s["stdout"])
            if s["stderr"]:
                f.write(f"[stderr] {s['stderr']}")
            f.write("\n" + "-" * 72 + "\n")
    print(json.dumps(summary["sections"], indent=1, default=str)[:4000])
    print(f"BATTERY DONE steps={len(results)}")


if __name__ == "__main__":
    sys.exit(main())
