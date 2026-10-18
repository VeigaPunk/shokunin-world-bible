#!/usr/bin/env python3
"""V43 independent full negative matrix for dependency_freeze C1.

Mutates only scratch mirrors. Does not import the tool. Does not write the
lane tree. Each probe is a fresh mirror of the snapshotted tool, contract,
and the six chain fixtures, run twice for stdout stability.
"""

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCRATCH = LANE / ".ufo/waves/round-99/seats/V43-scratch"
BASE_TOOL = SCRATCH / "baseline-dependency_freeze.py"
BASE_CONTRACT = SCRATCH / "baseline-dependency-freeze-contract.json"
CHAIN = (
    "r88-m3-maya-cluster",
    "r94-paired-crossing",
    "r95-crossing-aftermath",
    "r96-crossing-response",
    "r97-crossing-acknowledgment",
    "r98-clerk-filing",
)
CLAIM_FILES = (
    "entities.json",
    "relations.json",
    "timeline.json",
    "sources.json",
    "contradictions.json",
    "README.md",
    "claim-excerpt-map.md",
    "fictional-excerpts.md",
    "inspiration-note.md",
    "source-excerpt.md",
)
FINDING_IDS = (
    "REDUCTION-DETECTED",
    "ADDITION-DETECTED",
    "ENDPOINT-CHANGE",
    "DIGEST-MISMATCH",
    "UNPINNED-FIXTURE",
    "CONTRACT-INVALID",
    "FIXTURE-MISSING",
    "PATH-MISMATCH",
    "FILE-MISSING",
    "MALFORMED-JSON",
    "MALFORMED-MODEL",
    "INVALID-ARGUMENTS",
    "SELF-TEST-MISMATCH",
    "SCOPE-REFUSED",
)
WORDING = "depends on both ninth-bell entries"


def sha256_bytes(raw):
    return hashlib.sha256(raw).hexdigest()


def sha256_file(path):
    return sha256_bytes(Path(path).read_bytes())


def content_digest(files):
    payload = json.dumps(
        {name: sha256_bytes(raw) for name, raw in files.items()},
        sort_keys=True,
        separators=(",", ":"),
    )
    return sha256_bytes(payload.encode("utf-8"))


def invoke(mirror, args, env=None):
    cmd = [sys.executable, "corpus/tools/dependency_freeze.py", *args]
    run_env = os.environ.copy()
    if env:
        run_env.update(env)
    result = subprocess.run(
        cmd, cwd=mirror, capture_output=True, text=True, env=run_env
    )
    findings = []
    for line in result.stdout.splitlines():
        if line.startswith("FINDING "):
            rest = line[len("FINDING "):]
            finding_id, _, detail = rest.partition(": ")
            findings.append((finding_id, detail))
    return {
        "exit": result.returncode,
        "ids": [item[0] for item in findings],
        "details": [item[1] for item in findings],
        "stdout": result.stdout,
        "stderr": result.stderr,
        "migrated": [line for line in result.stdout.splitlines() if line.startswith("MIGRATED ")],
    }


def make_mirror(dest, tool, contract, fixture_root):
    if dest.exists():
        shutil.rmtree(dest)
    (dest / "corpus/tools").mkdir(parents=True)
    (dest / "corpus/fixtures").mkdir(parents=True)
    shutil.copy2(tool, dest / "corpus/tools/dependency_freeze.py")
    shutil.copy2(contract, dest / "corpus/tools/dependency-freeze-contract.json")
    for name in CHAIN:
        shutil.copytree(fixture_root / name, dest / "corpus/fixtures" / name)
    return dest


def contract_sha(mirror):
    path = mirror / "corpus/tools/dependency-freeze-contract.json"
    if not path.is_file():
        return "MISSING"
    return sha256_file(path)


def load_contract(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def save_contract(path, contract):
    Path(path).write_text(json.dumps(contract, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def named_files(details):
    found = []
    for detail in details:
        for name in CLAIM_FILES:
            if name in detail and name not in found:
                found.append(name)
    return found


class Matrix:
    def __init__(self, tool, contract, label, fixture_root=None):
        self.tool = Path(tool)
        self.contract = Path(contract)
        self.fixture_root = Path(fixture_root) if fixture_root else LANE / "corpus/fixtures"
        self.label = label
        self.work = SCRATCH / "mirrors" / label
        self.work.mkdir(parents=True, exist_ok=True)
        self.rows = []
        self.seen_ids = set()
        self.delivered = load_contract(self.contract)
        self.baseline = load_contract(BASE_CONTRACT)

    def mirror(self, tag):
        return make_mirror(self.work / tag, self.tool, self.contract, self.fixture_root)

    def record(self, row_id, claim, observed, note=""):
        ids = observed["ids"]
        self.seen_ids.update(ids)
        self.rows.append({
            "id": row_id,
            "claim": claim,
            "exit": observed["exit"],
            "ids": ids,
            "named": named_files(observed["details"]),
            "migrated": observed["migrated"],
            "stdout": observed["stdout"],
            "stderr": observed["stderr"],
            "stable": observed.get("stable"),
            "note": note,
            "contract_unchanged": observed.get("contract_unchanged"),
        })

    def twice(self, tag, args, mutate=None, env=None):
        runs = []
        for nth in (1, 2):
            mirror = self.mirror(f"{tag}-{nth}")
            if mutate:
                mutate(mirror)
            before = contract_sha(mirror)
            observed = invoke(mirror, args, env=env)
            observed["contract_unchanged"] = contract_sha(mirror) == before
            runs.append(observed)
        def norm(text):
            text = re.sub(r"dependency-freeze-self-test-[A-Za-z0-9_]+", "dependency-freeze-self-test-TMP", text)
            text = re.sub(r"/mirrors/[^/\s]+/", "/mirrors/TAG/", text)
            return text

        stable = (
            runs[0]["exit"] == runs[1]["exit"]
            and runs[0]["ids"] == runs[1]["ids"]
            and norm(runs[0]["stdout"]) == norm(runs[1]["stdout"])
            and norm(runs[0]["stderr"]) == norm(runs[1]["stderr"])
        )
        runs[0]["stable"] = stable
        return runs[0]

    def run(self):
        self.pin_shape()
        self.inherited_inventory()
        self.chain_verify()
        self.self_test()
        self.ten_file_edits()
        self.wording_removal()
        self.baseline_wording()
        self.semantic_class()
        self.precedence()
        self.structural_class()
        self.schema_class()
        self.freeze_guards()
        self.migration()
        self.upgrade_path()
        self.neutralize()
        self.env_marker()
        self.bounds()
        return self.rows

    def pin_shape(self):
        pins = self.delivered["pins"]
        problems = []
        if list(self.delivered.get("pinned_files", [])) != list(CLAIM_FILES):
            problems.append(f"contract pinned_files {self.delivered.get('pinned_files')}")
        if self.delivered.get("payload_schema_version") != 2 or self.delivered.get("schema_version") != 2:
            problems.append(
                f"root schema {self.delivered.get('schema_version')}/"
                f"{self.delivered.get('payload_schema_version')}"
            )
        if sorted(pins) != sorted(CHAIN):
            problems.append(f"pin set {sorted(pins)}")
        digests = {}
        for name in CHAIN:
            pin = pins[name]
            fixture = self.fixture_root / name
            files = {}
            missing = [item for item in CLAIM_FILES if not (fixture / item).is_file()]
            if missing:
                problems.append(f"{name} missing {missing}")
                continue
            for item in CLAIM_FILES:
                files[item] = (fixture / item).read_bytes()
            recomputed_files = {item: sha256_bytes(raw) for item, raw in files.items()}
            recomputed = content_digest(files)
            digests[name] = recomputed
            if pin.get("payload_schema_version") != 2:
                problems.append(f"{name} payload_schema_version {pin.get('payload_schema_version')}")
            if pin.get("pinned_files") != list(CLAIM_FILES):
                problems.append(f"{name} pinned_files mismatch")
            if sorted(pin.get("files", {})) != sorted(CLAIM_FILES):
                problems.append(f"{name} files keys {sorted(pin.get('files', {}))}")
            elif pin["files"] != recomputed_files:
                problems.append(f"{name} per-file digest mismatch")
            if pin.get("content_sha256") != recomputed:
                problems.append(
                    f"{name} content {pin.get('content_sha256')} != recomputed {recomputed}"
                )
        extra = self.fixture_root / "r88-m3-maya-cluster/symbolism-clause-map.md"
        if extra.is_file() and "symbolism-clause-map.md" in pins["r88-m3-maya-cluster"].get("files", {}):
            problems.append("r88 extra symbolism-clause-map.md was pinned")
        observed = {
            "exit": 0 if not problems else 1,
            "ids": [] if not problems else ["PIN-SHAPE"],
            "details": problems,
            "stdout": "\n".join(problems) + ("\n" if problems else ""),
            "stderr": "",
            "migrated": [],
            "stable": True,
        }
        note = " ".join(f"{name}={digest}" for name, digest in digests.items())
        self.record("P0-pin-shape", "ten-file schema-2 pins match independent digests", observed, note)

    def inherited_inventory(self):
        problems = []
        for name in CHAIN:
            old = self.baseline["pins"][name]
            new = self.delivered["pins"][name]
            for key in ("events", "relations", "counts"):
                if old.get(key) != new.get(key):
                    problems.append(f"{name}.{key} changed")
            if old.get("content_sha256") == new.get("content_sha256"):
                problems.append(f"{name} content digest did not move off the JSON-only pin")
            if set(old.get("files", {})) - set(CLAIM_FILES[:5]):
                problems.append(f"{name} baseline files unexpected")
        expected = set(self.baseline["self_test"]["expected"])
        got = set(self.delivered["self_test"]["expected"])
        if got - expected != {"markdown_tamper"} or expected - got:
            problems.append(f"self-test key delta extra={sorted(got - expected)} missing={sorted(expected - got)}")
        for key in expected:
            if self.baseline["self_test"]["expected"][key] != self.delivered["self_test"]["expected"][key]:
                problems.append(f"inherited expectation {key} changed")
        observed = {
            "exit": 0 if not problems else 1,
            "ids": [] if not problems else ["INVENTORY-DRIFT"],
            "details": problems,
            "stdout": "\n".join(problems) + ("\n" if problems else "inherited events/relations/counts identical; only markdown_tamper added\n"),
            "stderr": "",
            "migrated": [],
            "stable": True,
        }
        self.record("P0-inherited", "semantic inventory and 17 expectations unchanged", observed)

    def chain_verify(self):
        for name in CHAIN:
            observed = self.twice(f"chain-{name}", [f"corpus/fixtures/{name}"])
            self.record(f"P1-chain-{name}", "verify clean exit 0", observed)

    def self_test(self):
        observed = self.twice("self-test", ["--self-test"])
        self.record("P2-self-test", "SELF-TEST 18/18 exit 0", observed)

    def ten_file_edits(self):
        for filename in CLAIM_FILES:
            def mutate(mirror, filename=filename):
                path = mirror / "corpus/fixtures/r95-crossing-aftermath" / filename
                path.write_bytes(path.read_bytes() + b"\n")

            observed = self.twice("edit-" + filename.replace(".", "-"), ["corpus/fixtures/r95-crossing-aftermath"], mutate)
            self.record(f"N-edit-{filename}", "DIGEST-MISMATCH names the file exit 2", observed)

    def wording_removal(self):
        def mutate(mirror):
            path = mirror / "corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md"
            text = path.read_text(encoding="utf-8")
            if WORDING not in text:
                raise SystemExit(f"wording phrase absent: {WORDING}")
            path.write_text(text.replace(WORDING, "follows both ninth-bell entries", 1), encoding="utf-8")

        observed = self.twice("wording", ["corpus/fixtures/r95-crossing-aftermath"], mutate)
        self.record("N-wording-removal", "prose dependency-wording removal DIGEST-MISMATCH", observed)

    def baseline_wording(self):
        dest = self.work / "baseline-wording"
        make_mirror(dest, BASE_TOOL, BASE_CONTRACT, self.fixture_root)
        path = dest / "corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md"
        text = path.read_text(encoding="utf-8")
        path.write_text(text.replace(WORDING, "follows both ninth-bell entries", 1), encoding="utf-8")
        observed = invoke(dest, ["corpus/fixtures/r95-crossing-aftermath"])
        observed["stable"] = True
        observed["contract_unchanged"] = True
        self.record("B-wording-invisible", "baseline prose edit invisible exit 0", observed)

    def semantic_class(self):
        specs = [
            ("N-reduction", "REDUCTION-DETECTED", self._drop_edge),
            ("N-addition", "ADDITION-DETECTED", self._add_edge),
            ("N-endpoint", "ENDPOINT-CHANGE", self._flip_place),
            ("N-relation-flip", "ENDPOINT-CHANGE", self._flip_relation),
            ("N-relation-removed", "REDUCTION-DETECTED", self._clear_relations),
            ("N-relation-added", "ADDITION-DETECTED", self._add_relation),
            ("N-event-removed", "REDUCTION-DETECTED", self._drop_event),
        ]
        for row_id, _expected, mutate in specs:
            observed = self.twice(row_id, ["corpus/fixtures/r95-crossing-aftermath"], mutate)
            self.record(row_id, "semantic finding exit 1, digest not consulted", observed)

    def _timeline(self, mirror):
        path = mirror / "corpus/fixtures/r95-crossing-aftermath/timeline.json"
        return path, json.loads(path.read_text(encoding="utf-8"))

    def _write_timeline(self, path, rows):
        path.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")

    def _drop_edge(self, mirror):
        path, rows = self._timeline(mirror)
        for row in rows:
            if row["id"] == "paired-crossing-decision":
                row["depends_on"] = [dep for dep in row["depends_on"] if dep != "evin-ninth-bell"]
        self._write_timeline(path, rows)

    def _add_edge(self, mirror):
        path, rows = self._timeline(mirror)
        for row in rows:
            if row["id"] == "aftermath-missing-evin":
                row["depends_on"] = row["depends_on"] + ["phantom-ninth-bell"]
        self._write_timeline(path, rows)

    def _flip_place(self, mirror):
        path, rows = self._timeline(mirror)
        for row in rows:
            if row["id"] == "paired-crossing-decision":
                row["place_id"] = "salt-court"
        self._write_timeline(path, rows)

    def _flip_relation(self, mirror):
        path = mirror / "corpus/fixtures/r95-crossing-aftermath/relations.json"
        rows = json.loads(path.read_text(encoding="utf-8"))
        rows[0]["from"], rows[0]["to"] = rows[0]["to"], rows[0]["from"]
        path.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")

    def _clear_relations(self, mirror):
        path = mirror / "corpus/fixtures/r95-crossing-aftermath/relations.json"
        path.write_text("[]\n", encoding="utf-8")

    def _add_relation(self, mirror):
        path = mirror / "corpus/fixtures/r95-crossing-aftermath/relations.json"
        rows = json.loads(path.read_text(encoding="utf-8"))
        rows.append({"from": "aru", "to": "jorin", "type": "unpinned_relation"})
        path.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")

    def _drop_event(self, mirror):
        path, rows = self._timeline(mirror)
        rows = [row for row in rows if row["id"] != "aftermath-missing-evin"]
        self._write_timeline(path, rows)

    def precedence(self):
        def mutate(mirror):
            self._drop_edge(mirror)
            path = mirror / "corpus/fixtures/r95-crossing-aftermath/README.md"
            path.write_bytes(path.read_bytes() + b"\n")

        observed = self.twice("precedence", ["corpus/fixtures/r95-crossing-aftermath"], mutate)
        self.record("N-precedence", "semantic exit 1 wins over markdown byte change", observed)

    def structural_class(self):
        def bad_json(mirror):
            (mirror / "corpus/fixtures/r95-crossing-aftermath/timeline.json").write_text("[{\n", encoding="utf-8")

        def missing_timeline(mirror):
            (mirror / "corpus/fixtures/r95-crossing-aftermath/timeline.json").unlink()

        def missing_md(mirror):
            (mirror / "corpus/fixtures/r95-crossing-aftermath/inspiration-note.md").unlink()

        def missing_optional_json(mirror):
            (mirror / "corpus/fixtures/r95-crossing-aftermath/contradictions.json").unlink()

        def bad_utf8(mirror):
            (mirror / "corpus/fixtures/r95-crossing-aftermath/timeline.json").write_bytes(b"\xff\xfe")

        def bad_utf8_md(mirror):
            path = mirror / "corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md"
            path.write_bytes(path.read_bytes() + b"\xff")

        def not_array(mirror):
            (mirror / "corpus/fixtures/r95-crossing-aftermath/timeline.json").write_text("{}\n", encoding="utf-8")

        def dup_id(mirror):
            path, rows = self._timeline(mirror)
            rows.append(dict(rows[0]))
            self._write_timeline(path, rows)

        def bad_deps(mirror):
            path, rows = self._timeline(mirror)
            rows[0]["depends_on"] = [1]
            self._write_timeline(path, rows)

        def bad_rel(mirror):
            path = mirror / "corpus/fixtures/r95-crossing-aftermath/relations.json"
            path.write_text("[{}]\n", encoding="utf-8")

        def unpinned(mirror):
            src = mirror / "corpus/fixtures/r95-crossing-aftermath"
            shutil.copytree(src, mirror / "corpus/fixtures/v43-unpinned")

        def missing_pinned_dir(mirror):
            shutil.rmtree(mirror / "corpus/fixtures/r95-crossing-aftermath")

        def foreign(mirror):
            src = mirror / "corpus/fixtures/r95-crossing-aftermath"
            dest = mirror / "corpus/fixtures/foreign/r95-crossing-aftermath"
            shutil.copytree(src, dest)

        specs = [
            ("N-malformed-json", ["corpus/fixtures/r95-crossing-aftermath"], bad_json),
            ("N-missing-timeline", ["corpus/fixtures/r95-crossing-aftermath"], missing_timeline),
            ("N-missing-md", ["corpus/fixtures/r95-crossing-aftermath"], missing_md),
            ("N-missing-optional-json", ["corpus/fixtures/r95-crossing-aftermath"], missing_optional_json),
            ("N-bad-utf8-json", ["corpus/fixtures/r95-crossing-aftermath"], bad_utf8),
            ("N-bad-utf8-md", ["corpus/fixtures/r95-crossing-aftermath"], bad_utf8_md),
            ("N-malformed-model-array", ["corpus/fixtures/r95-crossing-aftermath"], not_array),
            ("N-malformed-model-dup", ["corpus/fixtures/r95-crossing-aftermath"], dup_id),
            ("N-malformed-model-deps", ["corpus/fixtures/r95-crossing-aftermath"], bad_deps),
            ("N-malformed-model-rel", ["corpus/fixtures/r95-crossing-aftermath"], bad_rel),
            ("N-unpinned", ["corpus/fixtures/v43-unpinned"], unpinned),
            ("N-absent-unpinned-name", ["corpus/fixtures/does-not-exist"], None),
            ("N-fixture-missing", ["corpus/fixtures/r95-crossing-aftermath"], missing_pinned_dir),
            ("N-path-mismatch", ["corpus/fixtures/foreign/r95-crossing-aftermath"], foreign),
            ("N-invalid-args", ["corpus/fixtures/r95-crossing-aftermath", "--freeze", "corpus/fixtures/r95-crossing-aftermath"], None),
        ]
        for row_id, args, mutate in specs:
            observed = self.twice(row_id, args, mutate)
            self.record(row_id, "exit 2 structural class", observed)

    def schema_class(self):
        def schema1(mirror):
            path = mirror / "corpus/tools/dependency-freeze-contract.json"
            contract = load_contract(path)
            contract["pins"]["r95-crossing-aftermath"]["payload_schema_version"] = 1
            save_contract(path, contract)

        def drop_file_key(mirror):
            path = mirror / "corpus/tools/dependency-freeze-contract.json"
            contract = load_contract(path)
            del contract["pins"]["r95-crossing-aftermath"]["files"]["README.md"]
            save_contract(path, contract)

        def pinned_list(mirror):
            path = mirror / "corpus/tools/dependency-freeze-contract.json"
            contract = load_contract(path)
            contract["pins"]["r95-crossing-aftermath"]["pinned_files"] = list(CLAIM_FILES[:-1])
            save_contract(path, contract)

        def no_contract(mirror):
            (mirror / "corpus/tools/dependency-freeze-contract.json").unlink()

        def bad_contract(mirror):
            (mirror / "corpus/tools/dependency-freeze-contract.json").write_text("{", encoding="utf-8")

        def drop_case(mirror):
            path = mirror / "corpus/tools/dependency-freeze-contract.json"
            contract = load_contract(path)
            del contract["self_test"]["expected"]["markdown_tamper"]
            save_contract(path, contract)

        def corrupt_clean(mirror):
            path = mirror / "corpus/tools/dependency-freeze-contract.json"
            contract = load_contract(path)
            contract["self_test"]["expected"]["clean"]["exit"] = 1
            save_contract(path, contract)

        def root_schema_documentary(mirror):
            path = mirror / "corpus/tools/dependency-freeze-contract.json"
            contract = load_contract(path)
            contract["schema_version"] = 1
            save_contract(path, contract)

        specs = [
            ("N-schema-version", ["corpus/fixtures/r95-crossing-aftermath"], schema1),
            ("N-pin-files-incomplete", ["corpus/fixtures/r95-crossing-aftermath"], drop_file_key),
            ("N-pinned-list", ["corpus/fixtures/r95-crossing-aftermath"], pinned_list),
            ("N-contract-missing", ["corpus/fixtures/r95-crossing-aftermath"], no_contract),
            ("N-contract-bad-json", ["corpus/fixtures/r95-crossing-aftermath"], bad_contract),
            ("N-expectation-set", ["--self-test"], drop_case),
            ("N-self-test-mismatch", ["--self-test"], corrupt_clean),
            ("N-root-schema-documentary", ["corpus/fixtures/r95-crossing-aftermath"], root_schema_documentary),
        ]
        for row_id, args, mutate in specs:
            observed = self.twice(row_id, args, mutate)
            self.record(row_id, "contract class", observed)

    def freeze_guards(self):
        def outside(mirror):
            target = mirror / "outside-target"
            target.mkdir()
            return target

        specs = []

        def scope_outside(mirror):
            target = mirror / "outside-target"
            target.mkdir()

        def scope_root(mirror):
            return None

        def same_name(mirror):
            src = mirror / "corpus/fixtures/r95-crossing-aftermath"
            dest = mirror / "corpus/fixtures/nested/r95-crossing-aftermath"
            shutil.copytree(src, dest)

        observed = self.twice("scope-outside", ["--freeze", "outside-target"], scope_outside)
        self.record("N-scope-outside", "SCOPE-REFUSED exit 2 contract unchanged", observed)
        observed = self.twice("scope-root", ["--freeze", "corpus/fixtures"], scope_root)
        self.record("N-scope-root", "SCOPE-REFUSED on fixtures root", observed)
        observed = self.twice(
            "scope-samename",
            ["--freeze", "corpus/fixtures/nested/r95-crossing-aftermath"],
            same_name,
        )
        self.record("N-scope-samename", "SCOPE-REFUSED same-named elsewhere", observed)

        def missing_md_freeze(mirror):
            src = mirror / "corpus/fixtures/r95-crossing-aftermath"
            dest = mirror / "corpus/fixtures/v43-freeze-miss"
            shutil.copytree(src, dest)
            (dest / "inspiration-note.md").unlink()

        observed = self.twice(
            "freeze-miss",
            ["--freeze", "corpus/fixtures/v43-freeze-miss"],
            missing_md_freeze,
        )
        self.record("N-freeze-missing-md", "FILE-MISSING on freeze, pin not written", observed)

    def migration(self):
        def pathless(mirror):
            path = mirror / "corpus/tools/dependency-freeze-contract.json"
            contract = load_contract(path)
            contract["pins"]["r95-crossing-aftermath"].pop("fixture", None)
            save_contract(path, contract)

        observed = self.twice("migrate", ["--freeze", "corpus/fixtures/r95-crossing-aftermath"], pathless)
        pin = None
        mirror = self.work / "migrate-1"
        if (mirror / "corpus/tools/dependency-freeze-contract.json").is_file():
            pin = load_contract(mirror / "corpus/tools/dependency-freeze-contract.json")["pins"]["r95-crossing-aftermath"]
        note = ""
        if pin:
            note = (
                f"fixture={pin.get('fixture')} schema={pin.get('payload_schema_version')} "
                f"nfiles={len(pin.get('files', {}))} keys={sorted(pin.get('files', {}))}"
            )
        self.record("N-migrate-canonical", "path-less pin migrated in place to schema 2 / 10 files", observed, note)

        def pathless_foreign(mirror):
            pathless(mirror)
            src = mirror / "corpus/fixtures/r95-crossing-aftermath"
            dest = mirror / "corpus/fixtures/nested/r95-crossing-aftermath"
            shutil.copytree(src, dest)

        observed = self.twice(
            "migrate-foreign",
            ["--freeze", "corpus/fixtures/nested/r95-crossing-aftermath"],
            pathless_foreign,
        )
        mirror = self.work / "migrate-foreign-1"
        pin = load_contract(mirror / "corpus/tools/dependency-freeze-contract.json")["pins"]["r95-crossing-aftermath"]
        note = f"fixture={pin.get('fixture')}"
        self.record("N-migrate-foreign", "path-less migration adopts invoked in-scope path", observed, note)

    def upgrade_path(self):
        dest = self.work / "upgrade"
        make_mirror(dest, self.tool, BASE_CONTRACT, self.fixture_root)
        before = invoke(dest, ["corpus/fixtures/r95-crossing-aftermath"])
        before["stable"] = True
        before["contract_unchanged"] = True
        self.record("N-old-pin-refused", "schema-1 pin refused by delivered tool", before)
        frozen = invoke(dest, ["--freeze", "corpus/fixtures/r95-crossing-aftermath"])
        frozen["stable"] = True
        pin = load_contract(dest / "corpus/tools/dependency-freeze-contract.json")["pins"]["r95-crossing-aftermath"]
        delivered = self.delivered["pins"]["r95-crossing-aftermath"]
        note = (
            f"schema={pin.get('payload_schema_version')} nfiles={len(pin.get('files', {}))} "
            f"digest_eq_delivered={pin.get('content_sha256') == delivered.get('content_sha256')} "
            f"files_eq_delivered={pin.get('files') == delivered.get('files')}"
        )
        self.record("N-upgrade-freeze", "guarded --freeze upgrades schema-1 pin to 10-file digest", frozen, note)

    def neutralize(self):
        def patch(mirror):
            path = mirror / "corpus/tools/dependency_freeze.py"
            text = path.read_text(encoding="utf-8")
            old = "    for name in MARKDOWN_FILES:\n"
            new = "    for name in ():\n"
            if text.count(old) != 1:
                raise SystemExit(f"neutralize anchor count {text.count(old)}")
            path.write_text(text.replace(old, new, 1), encoding="utf-8")
            excerpt = mirror / "corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md"
            excerpt.write_bytes(excerpt.read_bytes() + b"\n")

        observed = self.twice("neutral-verify", ["corpus/fixtures/r95-crossing-aftermath"], patch)
        self.record("N-neutral-verify", "markdown excluded from digest: tamper becomes invisible", observed)

        def patch_only(mirror):
            path = mirror / "corpus/tools/dependency_freeze.py"
            text = path.read_text(encoding="utf-8")
            old = "    for name in MARKDOWN_FILES:\n"
            path.write_text(text.replace(old, "    for name in ():\n", 1), encoding="utf-8")

        observed = self.twice("neutral-self", ["--self-test"], patch_only)
        self.record("N-neutral-self-test", "case 18 fails closed when markdown hashing is removed", observed)

    def env_marker(self):
        observed = self.twice(
            "env-self",
            ["--self-test"],
            env={"DEPENDENCY_FREEZE_SELF_TEST_CHILD": "1"},
        )
        self.record("N-env-self-test", "ambient child marker fails self-test closed", observed)
        observed = self.twice(
            "env-verify",
            ["corpus/fixtures/r95-crossing-aftermath"],
            env={"DEPENDENCY_FREEZE_SELF_TEST_CHILD": "1"},
        )
        self.record("N-env-verify", "ambient child marker does not affect verify", observed)

    def bounds(self):
        def extra(mirror):
            path = mirror / "corpus/fixtures/r88-m3-maya-cluster/symbolism-clause-map.md"
            path.write_bytes(path.read_bytes() + b"\n")

        observed = self.twice("extra", ["corpus/fixtures/r88-m3-maya-cluster"], extra)
        self.record("B-unpinned-extra", "file outside the declared ten is invisible", observed)

        def multi(mirror):
            for filename in ("README.md", "source-excerpt.md"):
                path = mirror / "corpus/fixtures/r95-crossing-aftermath" / filename
                path.write_bytes(path.read_bytes() + b"\n")

        observed = self.twice("multi", ["corpus/fixtures/r95-crossing-aftermath"], multi)
        self.record("N-multi-file", "DIGEST-MISMATCH names every changed pinned file", observed)

        def stale_file_map(mirror):
            path = mirror / "corpus/tools/dependency-freeze-contract.json"
            contract = load_contract(path)
            pin = contract["pins"]["r95-crossing-aftermath"]
            pin["files"]["README.md"] = "0" * 64
            save_contract(path, contract)

        observed = self.twice("stale-map", ["corpus/fixtures/r95-crossing-aftermath"], stale_file_map)
        self.record("B-stale-file-map", "per-file map not rechecked when content digest matches", observed)

        def digest_lie(mirror):
            path = mirror / "corpus/tools/dependency-freeze-contract.json"
            contract = load_contract(path)
            contract["pins"]["r95-crossing-aftermath"]["content_sha256"] = "ab" * 32
            save_contract(path, contract)

        observed = self.twice("digest-lie", ["corpus/fixtures/r95-crossing-aftermath"], digest_lie)
        self.record("N-digest-lie", "content digest disagreement names the no-diff fallback or files", observed)


def main():
    label = sys.argv[1] if len(sys.argv) > 1 else "run"
    tool = Path(sys.argv[2]) if len(sys.argv) > 2 else LANE / "corpus/tools/dependency_freeze.py"
    contract = Path(sys.argv[3]) if len(sys.argv) > 3 else LANE / "corpus/tools/dependency-freeze-contract.json"
    fixture_root = Path(sys.argv[4]) if len(sys.argv) > 4 else LANE / "corpus/fixtures"
    live_before = (sha256_file(LANE / "corpus/tools/dependency_freeze.py"), sha256_file(LANE / "corpus/tools/dependency-freeze-contract.json"))
    matrix = Matrix(tool, contract, label, fixture_root)
    rows = matrix.run()
    live_after = (sha256_file(LANE / "corpus/tools/dependency_freeze.py"), sha256_file(LANE / "corpus/tools/dependency-freeze-contract.json"))
    out = SCRATCH / f"matrix-{label}.log"
    js = SCRATCH / f"matrix-{label}.json"
    missing_ids = [item for item in FINDING_IDS if item not in matrix.seen_ids]
    lines = [
        f"LABEL {label}",
        f"TOOL {sha256_file(tool)}",
        f"CONTRACT {sha256_file(contract)}",
        f"LIVE_BEFORE {live_before[0]} {live_before[1]}",
        f"LIVE_AFTER {live_after[0]} {live_after[1]}",
        f"LIVE_STABLE {live_before == live_after}",
        f"SEEN_IDS {sorted(matrix.seen_ids)}",
        f"MISSING_IDS {missing_ids}",
        "",
    ]
    for row in rows:
        lines.append(
            f"### {row['id']} exit={row['exit']} ids={row['ids']} named={row['named']} "
            f"stable={row['stable']} contract_unchanged={row['contract_unchanged']}"
        )
        if row["migrated"]:
            lines.append("MIGRATED " + " | ".join(row["migrated"]))
        if row["note"]:
            lines.append("NOTE " + row["note"])
        lines.append(row["stdout"].rstrip())
        if row["stderr"].strip():
            lines.append("STDERR " + row["stderr"].rstrip())
        lines.append("")
    text = "\n".join(lines) + "\n"
    out.write_text(text, encoding="utf-8")
    js.write_text(json.dumps({
        "label": label,
        "tool": sha256_file(tool),
        "contract": sha256_file(contract),
        "live_stable": live_before == live_after,
        "seen_ids": sorted(matrix.seen_ids),
        "missing_ids": missing_ids,
        "rows": rows,
    }, indent=2), encoding="utf-8")
    print(text)
    print(f"WROTE {out}")
    return 0 if not missing_ids else 1


if __name__ == "__main__":
    sys.exit(main())
