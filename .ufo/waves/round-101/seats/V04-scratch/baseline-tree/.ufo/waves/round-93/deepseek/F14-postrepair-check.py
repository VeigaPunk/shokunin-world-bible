#!/usr/bin/env python3
"""F14 post-repair replay: R10 namespace comparison on the final committed inputs.

Runnable from the `lore-shokunin/` lane root:

    python3 .ufo/waves/round-93/deepseek/F14-postrepair-check.py

Deliberately contains NO expected-HEAD assertion: every assertion is on input
content hashes and on observed tool/comparison results, so the command keeps
working on later metadata-only descendant commits as long as the three fixture
input trees are unchanged. Exit 0 = all assertions held; exit 1 = at least one
failed (each failure is printed).

First capture preserved as filed: `.ufo/waves/round-93/deepseek/F14-namespace-scan.py`
and `F14-namespace-inventory.json`. This replay re-runs that same scan script over
the final committed inputs and pins the post-repair input hashes explicitly.
"""

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path("corpus/fixtures")
SCAN = Path(".ufo/waves/round-93/deepseek/F14-namespace-scan.py")
M2 = "r93-m2-kojiki-cluster"
NAMES = (M2, "r87-myth-cluster", "r88-m3-maya-cluster")

# Post-repair input pins (sha256 of file bytes), measured at the final committed HEAD
# 8e5a68d2a75338c8931c35dadd86fa04fb7c4c41 (2026-10-17 corrections landed).
EXPECTED_FILES = {
    M2: {
        "archive-record-excerpt.md": "71876794bcdff367c30f64bc1c7c60f2f06dff46c081d3fce52c1c0dc9419287",
        "claim-excerpt-map.md": "17f0e8123f26e4f7c534c01a6fe843fe0e8e1278858c0b0ce74623cb7291f7d6",
        "contradictions.json": "37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570",
        "entities.json": "19f75678dae1b59e6704d1be903a5cecf1b070dd44165e3047bc47efdb8e2d1d",
        "inspiration-note.md": "357820cfa4a8361fd4faeac00d8a81a1b045af1225def3695d9a51c60da78e48",
        "kojiki-chamberlain-excerpt.md": "7a4a671ad46dfa4c4eb38304f5aaf9cf381c024a8e5a16361c264bd335f52912",
        "README.md": "ddac89a43f3addcd14eb4044ec3933e80a6a4ddf1893787071486672744df42a",
        "relations.json": "32b79cd4d02793ce4c1f600522fb3810ffdbbad173b5707975fe9197ebf6e46d",
        "sources.json": "658610f15d677616adb758c347d2c0afe53b269d926515de686e1a12ceb7fdbd",
        "symbolism-clause-map.md": "eeb56880b93f4a239516cd0f38b61097e0d834afee29392713491700f3c10243",
        "timeline.json": "69da079eb29104cf4da04942ec3df79155569aa61d64fec00cb4aa7ffe2417e2",
    },
    "r87-myth-cluster": {
        "claim-excerpt-map.md": "3ad4e810c56e737d505a1963dfb1ffe23498045f5d81d8810e2ce6b779876f1a",
        "contradictions.json": "14bf96df22053ecb7251fb46a5d0b28213cb9b4d5e5a2b7e99c701a83de74aa4",
        "dune-register-excerpt.md": "23754ebe792898c3b9399c8f55404149c1cf90b7cd436cf6a613a92945aa690a",
        "entities.json": "fb96a323c849f0640eb2227633a510f1a39d8340886fa854ba8b2d986e30ac1a",
        "gate-witness-excerpt.md": "c8011512451658e681ae7accdd12932d4bef70e2aa854ddf025e92e7a9236b84",
        "inspiration-note.md": "91c0dba91c282bc3b2755c01a532d22ff067eaca3b2c6e1efe12cf5cbfe3cb8a",
        "lowwater-hymn-excerpt.md": "0cb263e8d5fd79a617f16dc57f476f9dc4d526e4f9ba90f05be68d8f8cc5cc6c",
        "README.md": "2b8e35a956829f766358f3d328b60bc2c0e077165d349a7259e03a18ce2a021c",
        "relations.json": "8bd0b78801bacee5ffd2df72bad3f0915704ec5918618c8f7d64d840a1272631",
        "shell-charter-excerpt.md": "7e06891ae849771bc52c064447fca04d3b2cfee22ffd07055ba5a217d5350b7f",
        "sources.json": "23fbb75a0f1f8cf07164debaf68dd1cca6b9a225854a73e7ebe20704efeb2d04",
        "symbolism-clause-map.md": "ad84d836f3eb709e40b3ccfdf2c274c797f77b84fdb0d5129e3856027a854854",
        "tide-bell-tally-excerpt.md": "ca589fd27e737832510a41d65d3b95e46121939af0a7447362fccd70583569a8",
        "timeline.json": "b4626c33a9f1d7fda75532e4e221e8c159cd8c4dcc25c80724bb54318c7284f1",
    },
    "r88-m3-maya-cluster": {
        "claim-excerpt-map.md": "b3b79fe5b5b9272b898b5714291739503c4250c415b3959032fcdba84a73fd43",
        "contradictions.json": "37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570",
        "entities.json": "042b6cc0d70c4d747121d9b277ac031cf21e66822d3c9a3e5ffe0282bba2bddc",
        "fictional-excerpts.md": "e456bb1204b88792d4fe6396e9e8b0deb9ff6f47e1821b0e875738431b9bda89",
        "inspiration-note.md": "58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37",
        "README.md": "55c9ba57ad7af5db0320fdc09142588c363c8b726d5ae1023dc01264f29b857c",
        "relations.json": "37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570",
        "source-excerpt.md": "b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd",
        "sources.json": "aa252416abc2c863ec4ae86cf25bd4f6e6e841d89e8586255b53362897282d63",
        "symbolism-clause-map.md": "4bfe975967844bc6edaeb0375c22784de5c1295d3e1ae8606e0e3390a5f4783d",
        "timeline.json": "f74c664b17fd8d575235ab59432a0ce6f938380e9b5a8d07640aae1d38773493",
    },
}
EXPECTED_TREES = {
    M2: ("854092b4e61457362c6f920275e5ccfa6214b06229d3d528408bae8a15a77d20",
         "72e4b2b82840318e9d092b1bfd1a504e3e278137293498327107b6fc12b0e505"),
    "r87-myth-cluster": ("c07d286df828d7c25a1d6304f9bb9abae2670a46287d436764d1b290eb665c39",
                         "997472173c52010858d620626874976759c5a7f82ccc657f0ec8960f67573e31"),
    "r88-m3-maya-cluster": ("edc94bc5b7b3e31192892a143602241f1b65d18a7ea3c3b4abba32bcf90dc254",
                            "0bb9084f5945951fee9d9a9c47c34ed808428fafc840a471648c9ef3b9ba8e7f"),
}
# R10 receipt (recovery/R10-key-scan.json) recorded post-addendum input hashes.
# r87/r88 are unchanged by the 2026-10-17 corrections; M2's recorded value predates them.
R10_RECORDED_EXCL_README = {
    "r87-myth-cluster": "997472173c52010858d620626874976759c5a7f82ccc657f0ec8960f67573e31",
    "r88-m3-maya-cluster": "0bb9084f5945951fee9d9a9c47c34ed808428fafc840a471648c9ef3b9ba8e7f",
    M2: "599d2507c26c57b7b185ecbb644b02880300a099df973501f6be665e832b1e23",
}
DECLARED_REFERENTS = {
    M2: {"teva", "orni", "slate-table", "lorn-index"},
    "r87-myth-cluster": {"hara", "sen", "mother-tide-gate", "ash-dune-sanctuary",
                         "shellweavers", "reedwardens", "reed-bell"},
    "r88-m3-maya-cluster": {"aru", "evin", "quiet-rise", "salt-court"},
}

failures = []


def check(label, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'} {label}{(' :: ' + detail) if detail else ''}")
    if not ok:
        failures.append(label)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tree_sha256(root: Path, exclude=()) -> str:
    digest = hashlib.sha256()
    for p in sorted(root.rglob("*")):
        if p.is_file() and p.name not in exclude:
            digest.update(p.relative_to(root).as_posix().encode("utf-8"))
            digest.update(b"\0")
            digest.update(p.read_bytes())
    return digest.hexdigest()


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def main():
    head = run(["git", "rev-parse", "HEAD"]).stdout.strip()
    tree = run(["git", "rev-parse", "HEAD^{tree}"]).stdout.strip()
    print(f"MEASURED_REVISION {head}")
    print(f"MEASURED_TREE {tree}")
    print("NOTE no HEAD assertion by design: assertions below are content/tool based.")

    print("\n-- input hash pins --")
    for name in NAMES:
        root = ROOT / name
        for fname, expected in EXPECTED_FILES[name].items():
            path = root / fname
            check(f"file sha256 {name}/{fname}",
                  path.is_file() and sha256(path) == expected,
                  "" if path.is_file() else "missing")
        actual_full, actual_excl = tree_sha256(root), tree_sha256(root, exclude=("README.md",))
        check(f"tree sha256 {name}", (actual_full, actual_excl) == EXPECTED_TREES[name],
              f"full={actual_full[:16]} excl_readme={actual_excl[:16]}")

    print("\n-- declared finite cluster records --")
    for name in NAMES:
        ids = {e["id"] for e in json.loads((ROOT / name / "entities.json").read_text(encoding="utf-8"))}
        check(f"declared referent set {name}", ids == DECLARED_REFERENTS[name],
              f"ids={sorted(ids)}")
    m2_json = sorted(p.name for p in (ROOT / M2).glob("*.json"))
    check("M2 JSON file set complete", m2_json == ["contradictions.json", "entities.json",
                                                   "relations.json", "sources.json", "timeline.json"],
          f"{m2_json}")
    check("M2 contradictions.json empty",
          json.loads((ROOT / M2 / "contradictions.json").read_text(encoding="utf-8")) == [])

    print("\n-- independent namespace comparison (filed first-capture script) --")
    scan = run([sys.executable, str(SCAN)])
    check("scan script exit 0", scan.returncode == 0, f"exit={scan.returncode}")
    live = json.loads(scan.stdout)
    for prior, comp in live["comparisons"].items():
        nonempty = {k: v for k, v in comp["key_intersections"].items() if v}
        check(f"normalized key intersections {M2} vs {prior}",
              set(nonempty) <= {"entity_kind_kind"},
              f"nonempty={nonempty}")
        check(f"generic kind vocabulary only {prior}",
              set(nonempty.get("entity_kind_kind", [])) <= {"character", "place", "item", "faction"})
        check(f"claim/event token n-gram overlap >=3 {prior}",
              comp["token_ngram_overlaps_ge3"] == [])
        prior_names = [e["name"] for e in live["fixtures"][prior]["referents"]]
        name_hits, reed_files = [], set()
        for path in sorted((ROOT / M2).rglob("*")):
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            for name in prior_names:
                if re.search(r"\b" + re.escape(name) + r"\b", text):
                    name_hits.append((path.name, name))
            if re.search(r"\breed", text, re.I):
                reed_files.add(path.name)
        check(f"prior display names inside M2 only in README {prior}",
              name_hits and all(f == "README.md" for f, _ in name_hits),
              f"files={sorted({f for f, _ in name_hits})}")
        check(f"Reed lookalike text only external excerpt + README {prior}",
              reed_files <= {"README.md", "kojiki-chamberlain-excerpt.md"},
              f"files={sorted(reed_files)}")
        check(f"no M2 name inside prior cluster {prior}",
              live["comparisons"][prior]["m2_display_names_mentioned_in_prior_files"] == {})
    for name in NAMES:
        check(f"no alias/epithet fields {name}", live["fixtures"][name]["alias_epithet_fields"] == [])
    boot = live["bootstrap_checks"]
    check("register file absent", boot["register_absent"])
    check("M6 target path absent from repo", boot["m6_target_absent_from_repo"])
    check("delivered cluster is not M6 target", boot["delivered_cluster_is_not_m6_target"])
    check("superseded sentence verbatim + superseded", boot["superseded_sentence_verbatim_in_readme"]
          and boot["supersession_claim_present"])
    check("M2 files never reference the register path", boot["m2_files_mention_register_path"] is False)
    check("r89 demo disclaims register status",
          "integration-ready register entry" in Path("corpus/knowledge/r89-cross-cluster-contradiction.md")
          .read_text(encoding="utf-8"))
    readme_text = (ROOT / M2 / "README.md").read_text(encoding="utf-8")
    r10_text = Path(".ufo/waves/round-93/recovery/R10.md").read_text(encoding="utf-8")
    check("README cites the current content-pinned replay + receipt",
          "python3 .ufo/waves/round-93/deepseek/F14-postrepair-check.py" in readme_text
          and "F14-postrepair-checks.out" in readme_text and "checks_failed=0" in readme_text)
    check("R10.md erratum supersedes the original active command",
          "## ERRATUM (2026-10-17)" in r10_text
          and "python3 .ufo/waves/round-93/deepseek/F14-postrepair-check.py" in r10_text)
    check("R10.md original command bytes retained (not rewritten)",
          "- Exact consistency command: `set -o pipefail" in r10_text
          and "R10-key-scan.py" in r10_text)

    print("\n-- R10 receipt cross-check (r87/r88 unchanged; M2 post-dates the capture) --")
    for prior in ("r87-myth-cluster", "r88-m3-maya-cluster"):
        check(f"R10 recorded input hash still live {prior}",
              live["fixtures"][prior]["dir_excl_readme_sha256"] == R10_RECORDED_EXCL_README[prior])
    m2_live = live["fixtures"][M2]["dir_excl_readme_sha256"]
    print(f"INFO R10 recorded M2 input hash {R10_RECORDED_EXCL_README[M2][:16]} vs post-repair "
          f"{m2_live[:16]} (2026-10-17 corrections landed after the R10 capture; comparison re-run above)")

    print("\n-- project tools --")
    bible_m2 = run([sys.executable, "corpus/fixtures/check_bible.py", f"corpus/fixtures/{M2}"])
    check("check_bible M2 CLEAN exit 0", bible_m2.returncode == 0 and "CLEAN" in bible_m2.stdout
          and "0 violations" in bible_m2.stdout, f"exit={bible_m2.returncode}")
    support = run([sys.executable, "corpus/tools/support_check.py", f"corpus/fixtures/{M2}"])
    check("support_check M2 12 facts + 3 editorial + PASS exit 0",
          support.returncode == 0 and "INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3" in support.stdout
          and "SOURCE-SUPPORT 12/12; EDITORIAL-ANCHORS 3/3" in support.stdout
          and "RESULT PASS" in support.stdout, f"exit={support.returncode}")
    for prior in ("r87-myth-cluster", "r88-m3-maya-cluster"):
        res = run([sys.executable, "corpus/fixtures/check_bible.py", f"corpus/fixtures/{prior}"])
        check(f"check_bible {prior} CLEAN exit 0", res.returncode == 0 and "CLEAN" in res.stdout
              and "0 violations" in res.stdout, f"exit={res.returncode}")

    print(f"\nRESULT {'ALL CHECKS HELD' if not failures else 'FAILED: ' + '; '.join(failures)}")
    print(f"checks_failed={len(failures)}")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
