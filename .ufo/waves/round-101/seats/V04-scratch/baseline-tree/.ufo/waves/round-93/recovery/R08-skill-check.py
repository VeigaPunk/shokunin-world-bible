from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess

root = Path(__file__).resolve().parents[4]
baseline = "65838f867d6ece8e7b8bdcc4ffc667a08a1b785e"
skill_path = root / "SKILL.md"
text = skill_path.read_text(encoding="utf-8")
checks = {
    "frontmatter triggers and arbitration": all(
        token in text
        for token in (
            'Triggers: "world bible"',
            '"fictional canon claim"',
            "Anti-trigger:",
            "Sibling arbitration:",
        )
    ),
    "decision, errors, checklist, registry": all(
        token in text
        for token in (
            "## Decision table",
            "## Error signatures and response",
            "## Executable integration checklist",
            "## Gate registry",
        )
    ),
    "no promotion or author-verification marks": "[x]" not in text and "promotion" not in text.lower(),
    "R8 cites corrected 12-cell record and replay": all(
        token in text
        for token in (
            "#corrected-illustrative-r8-review-record",
            "#corrected-replay",
            "record cells: 12/12",
        )
    ) and "five-field illustrative record" not in text and "5/5" not in text,
    "boundary self-test, manifest, Git inputs, and bounds": all(
        token in text
        for token in (
            "--self-test",
            "boundary-doc-contract.json",
            "git show",
            "git ls-tree",
            "No semantic, AST, or general prose validation",
        )
    ),
    "support and discriminator self-test debt retained": (
        "missing self-tests for `discriminate_check` and `support_check` remain conformance debt"
        in text
    ),
}

fields = (
    "name",
    "gate/probe",
    "entry command",
    "code → class",
    "self-test command",
    "pinned-values path",
    "scope",
    "owner",
)
for name in ("boundary_doc_check", "discriminate_check", "support_check"):
    start = text.index(f"**name:** `{name}`")
    end = text.find("\n### ", start)
    row = text[start:] if end < 0 else text[start:end]
    checks[f"registry fields: {name}"] = all(f"**{field}:**" in row for field in fields)

missing_expected_register = "corpus/knowledge/cross-cluster-contradictions.md"
manifest_path = "corpus/tools/boundary-doc-contract.json"
current_paths = {manifest_path}
refs = re.compile(
    r"(?P<path>(?:\.\./)?(?:[A-Za-z0-9_.-]+/)*[A-Za-z0-9_.-]+\.(?:md|py|json))"
    r"(?P<anchor>#[A-Za-z0-9-]+)?(?::(?P<lines>\d+(?:[,-]\d+)*))?"
)
try:
    manifest = json.loads((root / manifest_path).read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError):
    checks["worktree boundary pin manifest parses"] = False
else:
    checks["worktree boundary pin manifest parses"] = (
        isinstance(manifest, dict)
        and all(key in manifest for key in ("document", "checker", "scope", "self_test"))
        and isinstance(manifest.get("self_test", {}).get("expected"), dict)
    )


def heading_slugs(markdown):
    slugs = set()
    for line in markdown.splitlines():
        heading = re.match(r"^[ \t]*#{1,6}[ \t]+(.+?)[ \t]*#*[ \t]*$", line)
        if heading is None:
            continue
        title = re.sub(r"[`*_~]", "", heading.group(1)).casefold()
        title = re.sub(r"[^a-z0-9 -]", "", title)
        slug = re.sub(r"\s+", "-", title.strip())
        if slug:
            slugs.add(slug)
    return slugs


ref_count = 0
for match in refs.finditer(text):
    path = match.group("path")
    anchor = match.group("anchor")
    lines = match.group("lines")
    if path.startswith("../") or anchor or path in current_paths:
        source = (root / path).read_bytes() if (root / path).is_file() else None
        source_label = "worktree"
    else:
        result = subprocess.run(
            ["git", "show", f"{baseline}:{path}"],
            cwd=root,
            capture_output=True,
            check=False,
        )
        source = result.stdout if result.returncode == 0 else None
        source_label = f"baseline {baseline[:7]}"
    if path == missing_expected_register:
        checks["register destination absent at baseline until a real conflict"] = source is None
        continue
    if source is None:
        checks[f"{source_label} source path resolves: {path}"] = False
        continue
    ref_count += 1
    decoded = source.decode("utf-8")
    if anchor:
        checks[f"worktree section anchor resolves: {path}{anchor}"] = anchor[1:] in heading_slugs(decoded)
    if lines:
        line_count = len(decoded.splitlines())
        for part in lines.split(","):
            first, _, last = part.partition("-")
            first_line = int(first)
            last_line = int(last or first)
            checks[f"{source_label} line range resolves: {path}:{part}"] = 1 <= first_line <= last_line <= line_count

for label, passed in checks.items():
    print(f"{'PASS' if passed else 'FAIL'} {label}")
print(f"source_references_checked={ref_count}")

bundle = sha256()
for relpath in ("SKILL.md", ".ufo/waves/round-93/recovery/R08-skill-check.py"):
    bundle.update(relpath.encode("utf-8") + b"\0")
    bundle.update((root / relpath).read_bytes())
    bundle.update(b"\0")
print(f"R08_ARTIFACT_CONTENT_SHA256={bundle.hexdigest()}")
raise SystemExit(not all(checks.values()))
