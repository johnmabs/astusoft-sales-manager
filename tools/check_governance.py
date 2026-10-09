
#!/usr/bin/env python3

"""Validate initial project governance documentation."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    "PROJECT_STATE.md",
    "docs/00-governance/DOCUMENTATION_POLICY.md",
    "docs/00-governance/STATUS_MODEL.md",
    "docs/00-governance/DELIVERY_WORKFLOW.md",
    "docs/00-governance/RECOVERY_PROTOCOL.md",
    "docs/00-governance/GOVERNANCE_REVIEW.md",
)

LINK_PATTERN = re.compile(
    r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)"
)

def validate_required_files() -> list[str]:
    errors = []

    for relative_path in REQUIRED_FILES:
        file_path = ROOT / relative_path

        if not file_path.is_file():
            errors.append(f"Missing file: {relative_path}")

    return errors


def validate_markdown_links() -> list[str]:
    errors = []

    for document in ROOT.rglob("*.md"):
        if ".git" in document.parts:
            continue

        content = document.read_text(encoding="utf-8")

        # Ignore fenced code blocks containing Markdown examples.
        content = re.sub(
            r"(?ms)^(`{3,}|~{3,})[^\n]*\n.*?^\1[^\n]*$",
            "",
            content,
        )

        for match in LINK_PATTERN.finditer(content):
            target = match.group(1).strip().split()[0]
            parsed = urlsplit(target)

            if parsed.scheme or parsed.netloc:
                continue

            if not parsed.path:
                continue

            if target.startswith(("mailto:", "#")):
                continue

            relative = unquote(parsed.path)

            if relative.startswith("/"):
                continue

            resolved = (document.parent / relative).resolve()

            if not resolved.is_relative_to(ROOT):
                errors.append(
                    f"{document.relative_to(ROOT)}: "
                    f"link escapes repository: {target}"
                )
                continue

            if not resolved.exists():
                errors.append(
                    f"{document.relative_to(ROOT)}: "
                    f"broken link: {target}"
                )

    return errors


def validate_project_state() -> list[str]:
    errors = []
    path = ROOT / "PROJECT_STATE.md"

    if not path.exists():
        return errors

    content = path.read_text(encoding="utf-8")

    required_sections = (
        "## 2. Current delivery focus",
        "## 3. Git checkpoint",
        "## 7. Next actionable step",
    )

    for section in required_sections:
        if section not in content:
            errors.append(
                f"PROJECT_STATE.md: missing section {section}"
            )

    return errors


def main() -> int:
    checks = (
        validate_required_files,
        validate_markdown_links,
        validate_project_state,
    )

    errors = []

    for check in checks:
        errors.extend(check())

    if errors:
        print("Governance validation failed:\n")

        for error in errors:
            print(f" - {error}")

        return 1

    print("Governance validation passed.")
    print("Required documents and basic references are valid.")
    print("Manual semantic review is still required.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
